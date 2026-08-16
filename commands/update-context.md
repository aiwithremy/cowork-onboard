---
description: "Update one part of your workspace — about you, your voice, how you work, or your working folders"
---

First confirm which folder is the workspace (the folder connected to this conversation), exactly as the `cowork-onboard:onboard` skill's Phase 0 does. Never assume a path, and never write outside the confirmed folder.

Then ask the user which part they want to update:

1. **About me** — identity, role, business, expertise → `context/about-me.md`
2. **Voice DNA** — how you write → `context/voice-dna.md`
3. **Working style** — output preferences, rules, routines, tools → `context/working-style.md`
4. **Working folders** — add, rename, or retire one of the folders your work lives in
5. **Everything** — run the full setup again (same as `/onboard`)

For options 1-3, work through these steps in order:

1. **Read the existing file first** and show the user what's currently in it.
2. **Ask targeted questions only** — load the matching section from the onboard skill's `interview-questions.md` (Section A for about me, Section B for voice, Section C for working style) and ask one question at a time, always with the examples.
3. **For Voice DNA specifically:** if they want fresh writing samples, ask permission per source and name the account first ("I'd read about 20 of your own recent sent emails from `sam@acme.com` — OK?"), exactly as Phase 2 of the onboard skill does. A source they decline stays untouched. Then show what you found and let them reject anything outdated or wrong before it goes near the file. Keep the base rules from `voice-dna-base.md` at the top of the file.
4. **Update, don't replace.** This is an edit, not a regeneration:
   - Change only the sections the user actually discussed.
   - Keep every other section byte-for-byte as it was, including anything they wrote or edited by hand, and any section this plugin never created.
   - Never delete a section because it isn't in the template. If something looks out of place, ask before touching it.
5. **Preview the change before writing** — show the sections that will change, old version and new version, and get an explicit yes.
6. **Verify after writing** — read the file back and confirm the new content is there and the untouched sections survived.

For option 4, follow the same rules the onboard skill's Phase 6 uses:

1. **List what exists now** — show the current folders and ask what's changed about their work.
2. **Propose the change as a tree** with a reason for each new folder, in their words, and get an explicit yes before creating anything.
3. **Same safety rules:** tidy names (lowercase, hyphens, no characters a file system fights over), never collide with `context`, `AGENTS.md`, `CLAUDE.md`, or the progress file, never silently merge two names that tidy down to the same thing, and never overwrite a folder that already exists.
4. **Renaming or retiring a folder that has files in it is the user's call, not yours.** Say what's inside it, and never delete anything on their behalf.
5. **Verify by listing the folder afterwards**, then update the Work Areas section of `context/working-style.md` and the workspace map in `AGENTS.md` so all three match reality.

For option 5, hand over to the `cowork-onboard:onboard` skill and let it run its own flow.

Afterwards, check whether `AGENTS.md` needs a matching tweak — a new tool in the Tools list, a changed folder in the workspace map. `AGENTS.md` is the canonical instructions file for this workspace, so treat it carefully:

- Edit only the specific lines that need to change. Never rewrite it wholesale.
- Never touch the Learned Rules section, the `@context/` import line, or a rule the user added by hand.
- Never move instructions or context out of it.

`CLAUDE.md` is not an instructions file and is never edited as one — it is a pointer whose whole job is the `@AGENTS.md` line that sends Claude to the canonical file. Don't add rules, context, or tool notes to it. If it's missing or someone has pasted content into it, restore it to the minimal pointer form from the onboard skill rather than letting a second copy of the instructions grow there.
