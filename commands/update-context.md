---
description: "Update one part of your workspace context — about you, your voice, or how you work"
---

First confirm which folder is the workspace (the folder connected to this conversation), exactly as the `cowork-onboard:onboard` skill's Phase 0 does. Never assume a path, and never write outside the confirmed folder.

Then ask the user which part they want to update:

1. **About me** — identity, role, business, expertise → `context/about-me.md`
2. **Voice DNA** — how you write → `context/voice-dna.md`
3. **Working style** — output preferences, rules, routines, tools → `context/working-style.md`
4. **Everything** — run the full setup again (same as `/onboard`)

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

For option 4, hand over to the `cowork-onboard:onboard` skill and let it run its own flow.

Afterwards, check whether `CLAUDE.md` needs a matching tweak (for example a new tool in the Tools list). If it does, edit only those lines — never rewrite `CLAUDE.md` wholesale, and never touch the Learned Rules section.
