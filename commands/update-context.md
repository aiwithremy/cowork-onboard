---
description: "Update specific parts of your workspace context"
---

Ask the user which section they want to update:

1. **About me** — re-interview identity, role, business, expertise → regenerate `context/about-me.md`
2. **Voice DNA** — re-scan all connected communication tools for fresh writing samples, ask for additional sources (newsletters, blog posts, social media), re-interview tone and style → regenerate `context/voice-dna.md`
3. **Working style** — re-interview output preferences, rules, tasks, tool stack → regenerate `context/working-style.md`
4. **Morning brief skill** — update the personalized morning brief at `.claude/skills/morning-brief/SKILL.md`
5. **Inbox triage skill** — update the personalized inbox triage at `.claude/skills/inbox-triage/SKILL.md`
6. **Everything** — re-run the full onboarding (same as `/onboard`)

For options 1-5: read the existing file first, show the user what's currently there, then use the `cowork-onboard:onboard` skill's support files to guide the update:
- **About me** (option 1): load Section A from `interview-questions.md` for targeted questions
- **Voice DNA** (option 2): re-run the discovery scan across ALL connected communication tools (email, Slack, etc.) for fresh writing samples. Then ask: "Any other places your writing lives now? Newsletters, blog posts, social media?" Collect additional samples. Run the context validation gate — ask the user to ruthlessly reject anything outdated or wrong. Then load Section B from `interview-questions.md`. Embed base rules from `voice-dna-base.md`
- **Working style** (option 3): load Section C from `interview-questions.md` (includes tool stack quiz at Q13)
- **Morning brief** (option 4): load `skill-templates.md` for the morning-brief template, re-ask relevant questions
- **Inbox triage** (option 5): load `skill-templates.md` for the inbox-triage template, re-ask relevant questions

Show the current content, ask targeted questions from the question bank (always include examples), then regenerate only the selected file. Preview changes before writing.

For option 6: use the `cowork-onboard:onboard` skill to run the full flow.

After updating, also check if `CLAUDE.md` needs changes to reflect the updates.
