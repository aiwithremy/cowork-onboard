# Cowork Onboard

10-minute guided onboarding for Claude Cowork. One command builds your entire AI workspace.

## What It Does

Run `/onboard` and in 10 minutes you'll have:

- **Context files** — Claude learns who you are, how you communicate, and how you work
- **A personalized morning brief** — daily summary of your calendar, email, and tasks
- **Inbox triage** — automatic email categorization based on your priorities
- **Scheduled automation** — morning brief and inbox triage run on autopilot
- **Skill recommendations** — tailored to what you actually do day-to-day

## How It Works

1. **Connect your tools** — step-by-step guidance to link Google Drive, Gmail, Calendar, Notion, Slack
2. **Discovery scan** — searches your connected tools for brand guides, bios, and SOPs
3. **Quick interview** — 12 focused questions about you, your voice, and your workflow
4. **Skill generation** — creates personalized morning-brief and inbox-triage skills
5. **Workspace setup** — generates your CLAUDE.md and context files, schedules automation

## Installation

```
/install-plugin cowork-onboard
```

## Usage

Open any folder in Cowork — this will become your workspace. Then run:

```
/onboard
```

Follow the guided flow. That's it.

### Updating Later

To update specific parts of your workspace:

```
/update-context
```

This lets you refresh individual sections (about me, brand voice, working style, skills) without re-doing everything.

## What Gets Created

```
your-workspace/
  CLAUDE.md                          # Global instructions
  context/
    about-me.md                      # Identity, role, business, expertise
    brand-voice.md                   # Tone, anti-voice, language preferences
    working-style.md                 # Task approach, output defaults, rules
  .claude/
    skills/
      morning-brief/SKILL.md         # Personalized daily briefing
      inbox-triage/SKILL.md          # Personalized email triage
```

## Author

AI with Remy — [aiwithremy.com](https://aiwithremy.com)

## License

MIT
