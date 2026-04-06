---
name: onboard
description: Use when setting up a new AI workspace, running guided onboarding, or bootstrapping context files for Claude Cowork
user-invocable: true
---

# Cowork Onboard

Guided 10-minute onboarding that builds a personalized AI workspace. Connects tools, interviews the user, generates context files, creates custom skills, and sets up automation.

<HARD-GATE>
This is a GUIDED flow. Ask ONE question at a time. Wait for the user's response before proceeding. Never batch questions. Never skip steps. Never generate files without showing a preview first.
</HARD-GATE>

## Audience

The user is likely a complete beginner to Claude Cowork. Assume zero technical knowledge. Keep language simple, warm, and encouraging. Never use jargon without explaining it.

## Support Files

All reference files are in the same directory as this skill file (`skills/onboard/`):
- `mcp-setup-guide.md` — per-tool MCP connection instructions
- `interview-questions.md` — the full question bank for Phase 3
- `skill-templates.md` — parameterized templates for morning-brief and inbox-triage
- `skill-recommendation-map.md` — role-to-skill recommendation mapping

When this skill says "load [filename]", read it from the same directory as this SKILL.md.

## Before You Start

Check if this workspace already has onboarding files:
- If `CLAUDE.md` exists AND `context/` folder exists → warn the user: "This workspace already has context files. Running onboarding will overwrite them. Want to continue, or would `/update-context` be better for updating specific sections?"
- If no existing files → proceed directly

## Phase 1: Welcome & Tool Connection (~2 min)

### Welcome Message

Start with something like:

> "Hey! Let's get your AI workspace set up. This takes about 10 minutes and by the end, you'll have an AI assistant that knows your business, your voice, and your workflow.
>
> First, let's connect your tools so I can work with them."

### Tool Selection

Ask: **"Which of these do you use day-to-day? Pick all that apply."**

Present as a list:
- Google Drive / Docs
- Gmail
- Google Calendar
- Notion
- Slack
- None of the above / I'll add tools later

### Tool Connection

For each tool they selected, load the relevant section from `mcp-setup-guide.md` and walk them through it:

1. Give them the steps one at a time
2. Wait for them to confirm each step
3. After they say it's connected, verify with a test operation:
   - **Google Drive**: Try listing recent files
   - **Gmail**: Try listing recent emails
   - **Google Calendar**: Try listing today's events
   - **Notion**: Try searching for a recent page
   - **Slack**: Try listing channels
4. Confirm success: "Connected! I can see your [files/emails/events]. Moving on."
5. If it fails: Try one troubleshooting step. If still failing: "No worries — we can connect this later. Let's keep going."

If they chose "None / I'll add later", that's fine. Say: "No problem! We can connect tools anytime. Let's move on to learning about you."

### Transition
"Great, tools are sorted. Now let me see if you already have any useful docs I can learn from."

## Phase 2: Discovery Scan (~1 min)

For each connected tool, search for existing business context:

### What to Search For
- **Google Drive**: Search for files containing "brand guide", "style guide", "about", "SOP", "process", "bio", "tone of voice"
- **Notion**: Search for pages about brand, company, about, guidelines, processes
- **Slack**: Skip — Slack doesn't have searchable docs in the same way

### Present Findings

If you found relevant docs:
> "I found some useful docs that'll save us time:
> - [Brand guidelines from Google Drive]
> - [Your bio from Notion]
> - [Company about page from Notion]
>
> I'll use these as starting points — you can correct anything that's off during the interview."

If nothing found:
> "I didn't find any existing brand or business docs in your connected tools — no worries, we'll build everything from scratch. It just means a couple more questions."

### Hold Scan Results
Keep the content from found docs in context. You'll use them to pre-fill interview answers in Phase 3.

## Phase 3: Core Interview (~4 min)

Load `interview-questions.md` for the full question bank. Follow these rules:

### Interview Rules
1. **One question at a time.** Wait for their answer before asking the next.
2. **Pre-fill when possible.** If the Discovery Scan found info relevant to a question, present it as a starting point: "Based on your [brand guide], it looks like [X]. Is that right?"
3. **Skip what's already answered.** If a pre-filled answer is confirmed without changes, move on.
4. **Multiple choice when available.** Present options to make it easy.
5. **Be conversational.** This is a chat, not a form.
6. **Acknowledge answers.** Brief confirmation before moving on: "Got it." / "Perfect." / "Makes sense."

### Question Sequence

#### Section A: About You (Q1-Q4)
Transition: "Let's start with the basics — who you are and what you do."

Ask Q1 through Q4 from `interview-questions.md`, one at a time.

#### Section B: Your Voice (Q5-Q8)
Transition: "Now let's figure out how Claude should sound when it writes for you."

Ask Q5 through Q8 from `interview-questions.md`, one at a time.

#### Section C: How You Work (Q9-Q12)
Transition: "Last section — how you like to work and what you do every day."

Ask Q9 through Q12 from `interview-questions.md`, one at a time.

### After the Interview
"That's all the questions! Now let me put together your workspace."

## Phase 4: Generate Files & Skills (~2 min)

### Step 1: Generate Context Files

Using the interview answers (and Discovery Scan data), generate three files. **Show each file to the user before writing it.**

#### context/about-me.md
Generate from Q1-Q4. Structure:
```markdown
# About Me

## Identity
- **Name**: [from Q1]
- **Role**: [from Q1]
- **Business**: [from Q2]

## Expertise
[from Q4]

## Daily Focus
[from Q3 — translate the multi-select into natural language]

## Key Context
[anything extra from the discovery scan that adds useful context]
```

#### context/brand-voice.md
Generate from Q5-Q8. Structure:
```markdown
# Brand Voice

## Tone
[from Q5 — describe their communication style in a sentence]

## Voice Characteristics
[from Q7 — expand the selected options into descriptive bullets]

## Language Preferences
- **Always use**: [from Q6]
- **Never use**: [from Q6]

## Anti-Voice
[from Q8 — what Claude must never sound like]
```

If the Discovery Scan found writing examples, add:
```markdown
## Writing Examples
[1-2 real examples of their writing for Claude to reference]
```

#### context/working-style.md
Generate from Q9-Q12. Structure:
```markdown
# Working Style

## Output Preferences
[from Q9 — translate the choice into clear instructions for Claude]

## Rules
[from Q10 — each rule as a clear bullet point]

## Daily Tasks
[from Q11 — the tasks they repeat daily]

## Weekly Tasks
[from Q12 — the tasks they repeat weekly]

## Tools & Workflows
[from Phase 1 — list connected tools and basic usage notes]
```

### Step 2: Preview and Confirm

Show each file one at a time:
> "Here's your **About Me** context file: [show content]. Look good?"

Wait for confirmation before moving to the next. If they want changes, make them.

### Step 3: Write Context Files

After all three are approved, create the `context/` directory and write all three files.

### Step 4: Generate Personalized Skills

Load `skill-templates.md` and generate two personalized skills.

#### Morning Brief Skill
Generate `.claude/skills/morning-brief/SKILL.md` using the template. Fill in:
- Which tools are connected (calendar, email)
- Their daily tasks (Q11)
- Their output preferences (Q9)
- Their voice character (Q7)
- Relevant hard rules (Q10)

**Replace all template placeholders with actual values.** The output should be a clean SKILL.md with no template syntax.

#### Inbox Triage Skill
Generate `.claude/skills/inbox-triage/SKILL.md` using the template. Fill in:
- Their role and business (Q1, Q2)
- Their daily focus (Q3)
- Their hard rules (Q10)
- Their daily tasks (Q11) — for categorization context
- Their output preferences (Q9)
- Their voice character (Q7)

**Replace all template placeholders with actual values.**

### Step 5: Preview Skills

Show each generated skill:
> "Here's your personalized **Morning Brief** skill: [show content]. This will check your [calendar/email/etc.] and give you a daily summary. Look right?"

Wait for confirmation on each.

### Step 6: Write Skills

After both are approved, create `.claude/skills/morning-brief/SKILL.md` and `.claude/skills/inbox-triage/SKILL.md`.

### Step 7: Set Up Scheduled Tasks

Ask the user:
> "I can set these up to run automatically. What time do you usually start your day?"

Then:
> "And how often should I check your inbox? A few options:"
> - Once in the morning
> - Morning and afternoon
> - Three times: morning, midday, and evening

Set up scheduled tasks using the `/schedule` skill. For each task, invoke `/schedule` with:
- **Morning brief**: `create` a scheduled trigger that runs the `morning-brief` skill daily at their chosen time (e.g., "every day at 7am")
- **Inbox triage**: `create` a scheduled trigger that runs the `inbox-triage` skill at their chosen frequency (e.g., "every day at 9am, 1pm, and 5pm")

If the `/schedule` skill is not available, or scheduling fails, provide manual instructions: "Scheduling isn't set up yet, but you can run these anytime by saying 'morning brief' or 'triage my inbox'. You can set up automation later with the `/schedule` command."

## Phase 5: Wrap-up (~1 min)

### Generate CLAUDE.md

Create the master instruction file:

```markdown
# [Name]'s AI Workspace

@context/about-me.md
@context/brand-voice.md
@context/working-style.md

## Instructions

### Communication
- Follow the brand voice guidelines above in all output
- Match the output preferences in the working style guide

### Tools
[list each connected tool with a brief note, e.g.:]
- Google Drive: connected — use for document access and search
- Gmail: connected — use for email reading and triage

### Rules
[hard rules from Q10, formatted as clear instructions]
```

Show preview and get confirmation.

### Skill Recommendations

Load `skill-recommendation-map.md`. Based on Q3 (daily focus) and Q11/Q12 (tasks), recommend 2-3 relevant skills:

> "Based on what you do, these skills would pair well with your workspace:
> 1. **[skill]** — [what it does for them]
> 2. **[skill]** — [what it does for them]
> 3. **[skill]** — [what it does for them]
>
> These are optional — you can install them anytime."

### Summary

Present the final summary:

> "Your workspace is ready!
>
> **Created:**
> - `context/about-me.md` — who you are
> - `context/brand-voice.md` — how you sound
> - `context/working-style.md` — how you work
> - `CLAUDE.md` — your global instructions
> - Morning brief skill — personalized daily summary
> - Inbox triage skill — email categorization
>
> **Scheduled:**
> - Morning brief: daily at [time]
> - Inbox triage: [frequency]
>
> You're all set. Every time you open this folder in Cowork, Claude will know your business, your voice, and your workflow. Try saying 'morning brief' to test it out!"

## Tone Guidelines

Throughout the entire onboarding:
- **Warm but not cheesy.** Friendly, professional, encouraging.
- **Brief acknowledgments.** "Got it." "Perfect." "Makes sense." — not "That's a wonderful answer!"
- **No jargon.** Say "tools" not "MCPs". Say "instructions file" not "CLAUDE.md" (until they need to know).
- **Encouraging.** "You're doing great" if they seem hesitant. But don't overdo it.
- **Respect their time.** Keep moving. Don't over-explain things that are working.

## Error Handling

- **Tool connection fails**: Note it, move on, offer to retry later
- **Discovery scan finds nothing**: Skip gracefully, interview from scratch
- **User gives very short answers**: That's fine. Work with what you have. Don't push for more.
- **User wants to skip a question**: Skip it. Use reasonable defaults or leave the section minimal.
- **User wants to stop mid-flow**: Save progress so far. Tell them they can resume with `/onboard` or refine with `/update-context`.
- **Scheduling fails**: Provide manual instructions as fallback
