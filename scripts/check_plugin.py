#!/usr/bin/env python3
"""Deterministic checks for the cowork-onboard plugin.

Run from the repository root:

    python3 scripts/check_plugin.py

What it checks:

  1. All three manifests parse as JSON.
  2. The root plugin.json conforms to Agent Plugins Specification v1.0.0
     (exact $schema, name rules, closed top-level field set, semver version).
  3. The version is identical in plugin.json, .claude-plugin/plugin.json and
     the .claude-plugin/marketplace.json plugin entry.
  4. The marketplace entry points at this repository root and names this plugin.
  5. Skills live at skills/<name>/SKILL.md — one level only — with parseable
     frontmatter whose name matches the folder.
  6. Every file the plugin is supposed to ship exists.
  7. Every support file referenced from a markdown file exists (no dangling
     references to deleted files).
  8. No stale term from the retired skill-building / scheduling flow survives
     anywhere in the tracked text files — including any surviving reference to
     the removed generic `active/` output folder.
  9. The skill ends with a Self-Improvement Loop section.
 10. The generated workspace contract holds: the flow writes BOTH AGENTS.md and
     CLAUDE.md, the AGENTS.md template imports the context folder, and the
     CLAUDE.md template is a minimal signpost whose body is a bare @AGENTS.md
     import line (no duplicated instructions).
 11. No text claims CLAUDE.md is the master/canonical instructions file.
 12. The personalised working-areas flow survives: the design phase, the
     approval gate, the reserved-name guard, the resume-state key, the
     verified creation step, and the completion recap.

Exit 0 = clean. Exit 1 = at least one error.
"""

from __future__ import annotations

import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent

PLUGIN_SCHEMA = "https://agent-plugins.org/schemas/1.0.0/plugin.schema.json"

# Agent Plugins v1.0.0 closed top-level field set.
ALLOWED_MANIFEST_FIELDS = {
    "$schema", "name", "version", "description", "author",
    "homepage", "repository", "license", "keywords", "extensions",
}
ALLOWED_AUTHOR_FIELDS = {"name", "email", "url"}

# 1-64 chars, [a-z0-9-.], starts/ends alphanumeric, no "--" or ".."
NAME_RE = re.compile(r"^[a-z0-9](?:[a-z0-9]|-(?!-)|\.(?!\.))*[a-z0-9]$|^[a-z0-9]$")
SEMVER_RE = re.compile(r"^(0|[1-9]\d*)\.(0|[1-9]\d*)\.(0|[1-9]\d*)$")

REQUIRED_FILES = [
    "README.md",
    "LICENSE",
    "plugin.json",
    ".claude-plugin/plugin.json",
    ".claude-plugin/marketplace.json",
    "commands/onboard.md",
    "commands/update-context.md",
    "skills/onboard/SKILL.md",
    "skills/onboard/interview-questions.md",
    "skills/onboard/mcp-setup-guide.md",
    "skills/onboard/voice-dna-base.md",
]

# Terms from the retired flow. Any hit is a regression: this product no longer
# builds skills, saves skills, recommends skills, or schedules anything, it
# never hardcodes a workspace path or the obsolete install command, and it no
# longer creates a generic `active/` catch-all folder — working folders are
# derived from the person's own answers instead.
FORBIDDEN_TERMS = [
    "morning-brief",
    "morning brief",
    "inbox-triage",
    "inbox triage",
    "skill-templates",
    "skill-recommendation-map",
    "Save Skill",
    "/schedule",
    "scheduled task",
    "/install-plugin",
    "install-plugin",
    "10-minute",
    "10 minute",
    "Desktop/OS",
    "active/",
    "/active",
    "`active`",
    "everything generated goes",
    "where anything I make for you goes",
]

# Claims that CLAUDE.md still holds the instructions. AGENTS.md is canonical;
# CLAUDE.md is only a signpost that imports it.
STALE_MASTER_PATTERNS = [
    re.compile(r"CLAUDE\.md[^\n]{0,120}?master instructions", re.IGNORECASE),
    re.compile(r"master instructions[^\n]{0,120}?CLAUDE\.md", re.IGNORECASE),
    re.compile(
        r"CLAUDE\.md[^\n]{0,40}?\b(?:is|holds|contains)\b[^\n]{0,60}?"
        r"(?:master|canonical|main)\b",
        re.IGNORECASE,
    ),
]

# Frontmatter keys the current Claude/Cowork skill loader understands.
KNOWN_FRONTMATTER_KEYS = {
    "name", "description", "user-invocable", "disable-model-invocation",
    "allowed-tools", "license", "metadata", "model", "context", "agent",
    "argument-hint",
}

TEXT_SUFFIXES = {".md", ".json", ".py", ".txt"}


class Report:
    def __init__(self) -> None:
        self.errors: list[str] = []
        self.warnings: list[str] = []

    def error(self, where: str, msg: str) -> None:
        self.errors.append(f"{where}: {msg}")

    def warn(self, where: str, msg: str) -> None:
        self.warnings.append(f"{where}: {msg}")


def load_json(rel: str, report: Report) -> dict | None:
    path = ROOT / rel
    if not path.is_file():
        report.error(rel, "missing")
        return None
    try:
        data = json.loads(path.read_text(encoding="utf-8"))
    except json.JSONDecodeError as exc:
        report.error(rel, f"invalid JSON — {exc}")
        return None
    if not isinstance(data, dict):
        report.error(rel, "top level must be a JSON object")
        return None
    return data


def text_files() -> list[Path]:
    files = []
    for path in ROOT.rglob("*"):
        if not path.is_file():
            continue
        if ".git" in path.parts:
            continue
        if path.suffix in TEXT_SUFFIXES:
            files.append(path)
    return sorted(files)


def rel(path: Path) -> str:
    return str(path.relative_to(ROOT))


def check_required_files(report: Report) -> None:
    for name in REQUIRED_FILES:
        if not (ROOT / name).is_file():
            report.error(name, "required file is missing")


def check_root_manifest(report: Report) -> dict | None:
    data = load_json("plugin.json", report)
    if data is None:
        return None
    where = "plugin.json"

    if data.get("$schema") != PLUGIN_SCHEMA:
        report.error(where, f"$schema must be exactly '{PLUGIN_SCHEMA}'")

    name = data.get("name")
    if not isinstance(name, str) or not name:
        report.error(where, "missing required field 'name'")
    else:
        if not 1 <= len(name) <= 64 or not NAME_RE.match(name):
            report.error(where, f"name '{name}' breaks the spec's character rules")
        if name != ROOT.name:
            report.warn(where, f"name '{name}' differs from directory '{ROOT.name}'")

    for field in sorted(set(data) - ALLOWED_MANIFEST_FIELDS):
        report.error(where, f"unknown top-level field '{field}' — the schema is closed")

    version = data.get("version")
    if version is not None and (not isinstance(version, str) or not SEMVER_RE.match(version)):
        report.error(where, f"'version' must be plain semver (got {version!r})")

    author = data.get("author")
    if author is not None:
        if not isinstance(author, dict):
            report.error(where, "'author' must be an object")
        else:
            for field in sorted(set(author) - ALLOWED_AUTHOR_FIELDS):
                report.error(where, f"unknown 'author' field '{field}'")

    return data


def check_versions_match(root_manifest: dict | None, report: Report) -> None:
    claude = load_json(".claude-plugin/plugin.json", report)
    marketplace = load_json(".claude-plugin/marketplace.json", report)

    versions: dict[str, str | None] = {}
    if root_manifest is not None:
        versions["plugin.json"] = root_manifest.get("version")
    if claude is not None:
        versions[".claude-plugin/plugin.json"] = claude.get("version")

    entry = None
    if marketplace is not None:
        plugins = marketplace.get("plugins")
        if not isinstance(plugins, list) or not plugins:
            report.error(".claude-plugin/marketplace.json", "'plugins' must be a non-empty array")
        else:
            entry = plugins[0]
            if not isinstance(entry, dict):
                report.error(".claude-plugin/marketplace.json", "plugin entry must be an object")
                entry = None
            else:
                versions[".claude-plugin/marketplace.json (plugin entry)"] = entry.get("version")

    distinct = {v for v in versions.values() if v is not None}
    if len(distinct) > 1:
        detail = ", ".join(f"{k}={v}" for k, v in versions.items())
        report.error("versions", f"manifest versions must match — {detail}")
    for where, value in versions.items():
        if value is None:
            report.error(where, "missing 'version'")

    if entry is not None:
        if entry.get("source") != "./":
            report.error(
                ".claude-plugin/marketplace.json",
                f"plugin entry 'source' must be './' (got {entry.get('source')!r})",
            )
        expected = root_manifest.get("name") if root_manifest else "cowork-onboard"
        if entry.get("name") != expected:
            report.error(
                ".claude-plugin/marketplace.json",
                f"plugin entry name {entry.get('name')!r} must match the manifest name {expected!r}",
            )


def parse_frontmatter(path: Path, report: Report) -> dict[str, str]:
    lines = path.read_text(encoding="utf-8").splitlines()
    if not lines or lines[0].strip() != "---":
        report.error(rel(path), "missing YAML frontmatter (must open with '---')")
        return {}
    try:
        end = lines.index("---", 1)
    except ValueError:
        report.error(rel(path), "frontmatter is never closed with '---'")
        return {}

    fields: dict[str, str] = {}
    for raw in lines[1:end]:
        if not raw.strip() or raw.lstrip().startswith("#"):
            continue
        if raw.startswith((" ", "\t")):  # continuation of a folded value
            continue
        if ":" not in raw:
            report.error(rel(path), f"unparseable frontmatter line: {raw!r}")
            continue
        key, value = raw.split(":", 1)
        fields[key.strip()] = value.strip()
    return fields


def check_skills(report: Report) -> list[Path]:
    skills_dir = ROOT / "skills"
    if not skills_dir.is_dir():
        report.error("skills", "missing skills/ directory")
        return []

    skill_files: list[Path] = []
    for child in sorted(skills_dir.iterdir()):
        if child.name.startswith(".") or not child.is_dir():
            continue
        skill_md = child / "SKILL.md"
        if not skill_md.is_file():
            buried = [p for p in child.rglob("SKILL.md") if p.is_file()]
            if buried:
                report.error(
                    rel(child),
                    f"SKILL.md is buried at {rel(buried[0])} — clients only read one level deep",
                )
            else:
                report.error(rel(child), "skill directory has no SKILL.md")
            continue

        skill_files.append(skill_md)
        fields = parse_frontmatter(skill_md, report)
        if fields.get("name") != child.name:
            report.error(
                rel(skill_md),
                f"frontmatter name {fields.get('name')!r} must match folder {child.name!r}",
            )
        if not fields.get("description"):
            report.error(rel(skill_md), "frontmatter needs a 'description'")
        for key in sorted(set(fields) - KNOWN_FRONTMATTER_KEYS):
            report.warn(rel(skill_md), f"unrecognised frontmatter key '{key}'")

    if not skill_files:
        report.error("skills", "no loadable skills found")
    return skill_files


def check_support_references(report: Report) -> None:
    """Every backticked *.md filename must resolve to a real file."""
    pattern = re.compile(r"`([A-Za-z0-9][A-Za-z0-9._-]*\.md)`")
    for path in text_files():
        if path.suffix != ".md":
            continue
        for match in set(pattern.findall(path.read_text(encoding="utf-8"))):
            # Files the plugin generates in the user's workspace, not shipped here.
            if match in {"CLAUDE.md", "AGENTS.md", "about-me.md", "voice-dna.md",
                         "working-style.md", "onboarding-progress.md", "README.md",
                         "LESSONS.md"}:
                continue
            candidates = [path.parent / match, ROOT / match, ROOT / "skills" / "onboard" / match]
            if not any(c.is_file() for c in candidates):
                report.error(rel(path), f"references '{match}', which does not exist")


def check_forbidden_terms(report: Report) -> None:
    this_file = Path(__file__).resolve()
    for path in text_files():
        if path.resolve() == this_file:  # the checker names the terms on purpose
            continue
        text = path.read_text(encoding="utf-8")
        lowered = text.lower()
        for term in FORBIDDEN_TERMS:
            if term.lower() in lowered:
                line_no = next(
                    (i for i, line in enumerate(text.splitlines(), 1)
                     if term.lower() in line.lower()),
                    0,
                )
                report.error(f"{rel(path)}:{line_no}", f"stale term '{term}' from the retired flow")


def check_no_stale_master_claims(report: Report) -> None:
    """CLAUDE.md is a signpost. Nothing may still call it the instructions file."""
    this_file = Path(__file__).resolve()
    for path in text_files():
        if path.resolve() == this_file:  # the checker spells the claim out on purpose
            continue
        text = path.read_text(encoding="utf-8")
        for line_no, line in enumerate(text.splitlines(), 1):
            for pattern in STALE_MASTER_PATTERNS:
                if pattern.search(line):
                    report.error(
                        f"{rel(path)}:{line_no}",
                        "stale claim that CLAUDE.md is the master instructions file — "
                        "AGENTS.md is canonical and CLAUDE.md only imports it",
                    )
                    break


def fenced_block_after(text: str, heading: str) -> str | None:
    """Return the first fenced code block that follows an exact heading line."""
    lines = text.splitlines()
    try:
        start = next(i for i, line in enumerate(lines) if line.strip() == heading)
    except StopIteration:
        return None
    body: list[str] = []
    inside = False
    for line in lines[start + 1:]:
        if not inside:
            if line.startswith("```"):
                inside = True
            elif line.startswith("#"):
                return None  # the next heading arrived before any code block
            continue
        if line.startswith("```"):
            return "\n".join(body)
        body.append(line)
    return None


def heading_section(text: str, heading_prefix: str) -> str | None:
    """Return everything under a top-level heading, up to the next one."""
    lines = text.splitlines()
    try:
        start = next(i for i, line in enumerate(lines) if line.startswith(heading_prefix))
    except StopIteration:
        return None
    body: list[str] = []
    for line in lines[start + 1:]:
        if line.startswith("## "):
            break
        body.append(line)
    return "\n".join(body)


def check_generated_workspace_contract(report: Report) -> None:
    """AGENTS.md is canonical; CLAUDE.md is a direct signpost that imports it."""
    skill_path = ROOT / "skills" / "onboard" / "SKILL.md"
    if not skill_path.is_file():
        return  # already reported by check_required_files
    text = skill_path.read_text(encoding="utf-8")
    where = rel(skill_path)

    agents_template = fenced_block_after(text, "### AGENTS.md")
    if agents_template is None:
        report.error(where, "no '### AGENTS.md' template block — the flow must generate AGENTS.md")
    elif "@context/" not in agents_template:
        report.error(where, "the AGENTS.md template must import the context folder with '@context/'")

    claude_template = fenced_block_after(text, "### CLAUDE.md")
    if claude_template is None:
        report.error(where, "no '### CLAUDE.md' template block — the flow must generate CLAUDE.md")
    else:
        if "@AGENTS.md" not in [line.strip() for line in claude_template.splitlines()]:
            report.error(
                where,
                "the CLAUDE.md template must carry a bare '@AGENTS.md' line so Claude "
                "loads the canonical instructions immediately",
            )
        for duplicated in ("@context/", "Self-Correcting", "Learned Rules", "### Rules"):
            if duplicated in claude_template:
                report.error(
                    where,
                    f"the CLAUDE.md template must stay a signpost — found {duplicated!r} "
                    "duplicated from AGENTS.md",
                )
        if len([line for line in claude_template.strip().splitlines()]) > 12:
            report.error(where, "the CLAUDE.md template must stay minimal (12 lines or fewer)")

    for target in ("[WORKSPACE_ROOT]/AGENTS.md", "[WORKSPACE_ROOT]/CLAUDE.md"):
        if target not in text:
            report.error(where, f"the build step never writes {target}")

    build = heading_section(text, "## Phase 8: Build it")
    if build is None:
        report.error(where, "no '## Phase 8: Build it' section")
    else:
        for name in ("AGENTS.md", "CLAUDE.md"):
            if name not in build:
                report.error(where, f"the write/read-back verification never shows {name}")
        if "working_areas.approved" not in build:
            report.error(
                where,
                "the build step must create and verify the approved working areas from "
                "'working_areas.approved'",
            )

    recap = heading_section(text, "## Phase 9: Wrap up")
    if recap is None:
        report.error(where, "no '## Phase 9: Wrap up' recap section")
    else:
        for name in ("AGENTS.md", "CLAUDE.md", "working areas"):
            if name not in recap:
                report.error(where, f"the completion recap never mentions {name}")


def check_working_areas_flow(report: Report) -> None:
    """Working folders are derived from the interview, approved, and verified."""
    skill_path = ROOT / "skills" / "onboard" / "SKILL.md"
    if skill_path.is_file():
        text = skill_path.read_text(encoding="utf-8")
        where = rel(skill_path)
        required = {
            "## Phase 6: Design your working areas":
                "the working-areas design phase is missing",
            "working_areas":
                "the resume state never records the proposed/approved folder tree",
            "`working-areas`":
                "'working-areas' is missing from the progress file's phase list",
            "Reserved at the workspace root":
                "the reserved-name guard (context / AGENTS.md / CLAUDE.md / progress file) is missing",
            "Never invent a taxonomy":
                "the rule against inventing a folder taxonomy is missing",
        }
        for needle, message in required.items():
            if needle not in text:
                report.error(where, message)
        if "illustrative only" not in text.lower():
            report.error(where, "the example folder trees are not labelled illustrative")

    bank_path = ROOT / "skills" / "onboard" / "interview-questions.md"
    if bank_path.is_file():
        bank = bank_path.read_text(encoding="utf-8")
        where = rel(bank_path)
        for needle, message in {
            "### Q14": "the interview bank has no question about the person's work areas",
            "### Q15": "the interview bank has no question about what they make in each area",
        }.items():
            if needle not in bank:
                report.error(where, message)
        if "illustrative only" not in bank.lower():
            report.error(where, "the work-area examples are not labelled illustrative")


def check_self_improvement_loop(skill_files: list[Path], report: Report) -> None:
    for skill_md in skill_files:
        text = skill_md.read_text(encoding="utf-8")
        if "## Self-Improvement Loop" not in text:
            report.error(rel(skill_md), "missing the '## Self-Improvement Loop' section")


def main() -> int:
    report = Report()
    check_required_files(report)
    root_manifest = check_root_manifest(report)
    check_versions_match(root_manifest, report)
    skill_files = check_skills(report)
    check_support_references(report)
    check_forbidden_terms(report)
    check_no_stale_master_claims(report)
    check_generated_workspace_contract(report)
    check_working_areas_flow(report)
    check_self_improvement_loop(skill_files, report)

    for warning in report.warnings:
        print(f"warning: {warning}")
    for error in report.errors:
        print(f"ERROR: {error}", file=sys.stderr)

    print(
        f"\ncowork-onboard checks — {len(skill_files)} skill(s): "
        f"{len(report.errors)} error(s), {len(report.warnings)} warning(s)"
    )
    return 1 if report.errors else 0


if __name__ == "__main__":
    raise SystemExit(main())
