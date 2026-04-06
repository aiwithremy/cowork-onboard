# Cowork Onboard

10-minute guided onboarding for Claude Cowork. One command builds your entire AI workspace.

## What It Does

Run `/onboard` and in 10 minutes you'll have:

- **Voice DNA** — Claude learns how you actually write by scanning your emails and messages, then builds a detailed voice profile with real writing samples
- **Context files** — who you are, how you work, your full tool stack and preferences
- **A personalized morning brief** — daily summary of your calendar, email, and tasks
- **Inbox triage** — automatic email categorization based on your priorities
- **Self-correcting rules engine** — your workspace gets smarter every time Claude makes a mistake
- **Scheduled automation** — morning brief and inbox triage run on autopilot
- **Skill recommendations** — tailored to what you actually do day-to-day

## How It Works

1. **Connect your tools** — step-by-step guidance to link Gmail, Google Drive, Calendar, Notion, Slack, Granola
2. **Deep discovery scan** — digs through your sent emails, messages, and docs to learn your writing style and find existing business context
3. **Guided interview** — 13 focused questions about you, your voice, your workflow, and your tools. Every question comes with rich examples so you're never staring at a blank prompt
4. **Skill generation** — creates personalized morning-brief and inbox-triage skills tailored to your specific tools and priorities
5. **Workspace setup** — generates CLAUDE.md with self-correcting rules engine, schedules automation

## Installation

```
/install-plugin cowork-onboard from aiwithremy/cowork-onboard
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

This lets you refresh individual sections (about me, voice DNA, working style, tools, skills) without re-doing everything.

## What Gets Created

**On your Desktop:**
```
~/Desktop/OS/
  CLAUDE.md                          # Global instructions + self-correcting rules engine
  context/
    about-me.md                      # Identity, role, business, expertise
    voice-dna.md                     # Writing style, tone, samples, anti-patterns
    working-style.md                 # Output prefs, rules, tasks, full tool stack
```

**Saved globally in Cowork** (via the Save Skill button):
- Morning brief skill — personalized daily briefing
- Inbox triage skill — personalized email triage

## Author

AI with Remy — [aiwithremy.com](https://aiwithremy.com)

## License

MIT
