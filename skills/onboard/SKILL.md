---
name: onboard
description: Use when setting up a new AI workspace, running guided onboarding, or bootstrapping context files for Claude Cowork
user-invocable: true
---

# Cowork Onboard

Guided 10-minute onboarding that builds a personalized AI workspace. Connects tools, deep-scans your existing content for voice and context, interviews you, generates personalized context files, creates custom skills, and sets up automation.

<HARD-GATE>
This is a GUIDED flow. Ask ONE question at a time. Wait for the user's response before proceeding. Never batch questions. Never skip steps. Never generate files without showing a preview first.

Every question MUST include rich examples. Most users can't articulate what they want from scratch. Give them concrete examples to react to and riff on. Examples are not optional.
</HARD-GATE>

## Audience

The user is likely a complete beginner to Claude Cowork. Assume zero technical knowledge. Keep language simple, warm, and encouraging. Never use jargon without explaining it.

## Support Files

All reference files are in the same directory as this skill file (`skills/onboard/`):
- `mcp-setup-guide.md` — per-tool MCP connection instructions
- `interview-questions.md` — the full question bank for Phase 3 (with examples for every question)
- `skill-templates.md` — parameterized templates for morning-brief and inbox-triage
- `skill-recommendation-map.md` — role-to-skill recommendation mapping
- `voice-dna-base.md` — base writing rules embedded in every voice-dna file

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
> First, let's connect your tools so I can learn how you write and work."

### Tool Selection

Ask: **"Which of these do you use day-to-day? Pick all that apply."**

Present as a list:
- Google Drive / Docs
- Gmail
- Google Calendar
- Notion
- Slack
- Granola (meeting notes)
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
   - **Granola**: Try listing recent meetings
4. Confirm success: "Connected! I can see your [files/emails/events]. Moving on."
5. If it fails: Try one troubleshooting step. If still failing: "No worries — we can connect this later. Let's keep going."

If they chose "None / I'll add later", that's fine. Say: "No problem! We can connect tools anytime. Let's move on to learning about you."

### Transition
"Great, tools are sorted. Now let me dig through your connected tools to learn how you write and work. This takes a minute."

## Phase 2: Deep Discovery Scan (~2 min)

This phase is critical. The more context we pull now, the less the user has to explain. Search aggressively across all connected tools.

### What to Search For

#### Gmail — Writing Tone & Style (PRIORITY)
This is the most valuable source for Voice DNA. Search for:
- **Sent emails** (last 30-60 days) — these reveal how the user actually writes
- Focus on emails TO clients, partners, and colleagues (not automated replies)
- Pull 5-10 representative email excerpts that show their natural writing style
- Note patterns: greeting style, sign-off style, sentence length, formality level, use of humor, punctuation habits
- Look for: do they use exclamation marks? Emojis? Short sentences or long? Formal or casual greetings?

#### Gmail — Business Context
- Email signatures → name, role, company, links
- Recent threads → what they're working on, who they work with
- Newsletter subscriptions → interests and industry

#### Google Drive / Docs
- Brand guidelines, style guides, tone-of-voice documents
- About pages, bios, company descriptions
- SOPs, process docs, team guidelines
- Client proposals (for understanding their communication style)
- Any document with "brand", "style", "guide", "about", "SOP", "process", "bio", "tone"

#### Notion
- Company wiki pages, about pages
- Process docs, SOPs, runbooks
- Meeting notes, project docs
- Brand or style guidelines

#### Slack
- Recent messages FROM the user (not to them) — for writing style analysis
- Channel names → what teams/projects they're involved in
- Pinned messages → important context

#### Granola / Meeting Notes
- Recent meeting transcripts — for communication style in verbal contexts
- Meeting summaries — what they're working on

### How to Analyze Writing Style

From the emails and messages you find, build a profile:

1. **Collect 5-10 writing samples** — real excerpts from their sent emails, Slack messages, or docs
2. **Identify patterns**:
   - Average sentence length (short and punchy? Long and detailed?)
   - Greeting style ("Hi John," vs "Hey!" vs "John,")
   - Sign-off style ("Best," vs "Cheers," vs "Thanks!" vs nothing)
   - Punctuation habits (exclamation marks? Ellipses? Em-dashes?)
   - Emoji usage (never? Sometimes? Frequently?)
   - Formality spectrum (formal, professional, conversational, casual)
   - Unique phrases or expressions they repeat
   - How they give instructions (direct? Softened? Collaborative?)
3. **Save these samples** — they'll be embedded directly into the Voice DNA file

### Present Findings

Show what you found — be specific and use their actual writing:

> "I dug through your emails and docs. Here's what I learned about how you write:
>
> **Your writing style**: You're [conversational/professional/etc.]. Your emails tend to be [short and direct / detailed and thorough / warm and personal].
>
> **Examples of your actual writing:**
> 1. '[actual excerpt from their sent email]'
> 2. '[actual excerpt from their sent email]'
> 3. '[actual excerpt from their Slack message]'
>
> **Patterns I noticed:**
> - You [always/never/usually] [pattern]
> - You tend to [pattern]
> - Your greetings are usually [style]
>
> **Other context I found:**
> - [Brand guide / bio / SOP from Drive or Notion]
> - [Business context from email signatures]
>
> Does this feel accurate? Anything I got wrong?"

If nothing found (no tools connected or no useful content):
> "I couldn't find existing docs or emails to learn from — no worries, we'll figure out your style through the interview. It'll just mean a few more questions."

### Hold All Scan Results
Keep everything — writing samples, patterns, documents — in context. These feed directly into Phase 3 pre-fills and Phase 4 file generation.

## Phase 3: Core Interview (~5 min)

Load `interview-questions.md` for the full question bank, including all examples. Follow these rules:

### Interview Rules
1. **One question at a time.** Wait for their answer before asking the next.
2. **Always show examples.** Every question in the question bank has rich examples. Present them. Users can't articulate AI preferences without seeing concrete possibilities.
3. **Pre-fill from scan.** If the Discovery Scan found info relevant to a question, show it with real examples: "Based on your emails, it looks like [X]. Here are some examples: [actual excerpts]. Is that right?"
4. **Skip what's already answered.** If a pre-filled answer is confirmed, move on.
5. **Be conversational.** This is a chat, not a form.
6. **Acknowledge answers.** Brief confirmation: "Got it." / "Perfect." / "Makes sense."

### Question Sequence

#### Section A: About You (Q1-Q4)
Transition: "Let's start with the basics — who you are and what you do."

Ask Q1 through Q4 from `interview-questions.md`, one at a time. Each question has examples — always share them.

#### Section B: Your Voice DNA (Q5-Q8)
Transition: "Now let's nail down how I should sound when I write for you. I already have a head start from your emails."

Ask Q5 through Q8 from `interview-questions.md`, one at a time. These should be heavily pre-filled from the discovery scan. Show actual writing samples for every voice-related question.

#### Section C: How You Work (Q9-Q13)
Transition: "Last section — how you like to work, your rules, and your tools."

Ask Q9 through Q13 from `interview-questions.md`, one at a time.

**Q13 (Tool Stack) is new and important.** This produces a clear reference table of every tool they use and how. Load the full examples from the question bank.

### After the Interview
"That's all the questions! Now let me put together your workspace."

## Phase 4: Generate Files & Skills (~2 min)

### Step 1: Generate Context Files

Using the interview answers AND the deep discovery scan data, generate three files. **Show each file to the user before writing it.**

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

#### context/voice-dna.md
Generate from Q5-Q8 + the deep discovery scan writing samples. This is the most important file — it should be rich and specific, not a few light sentences.

**Start with the base writing rules** from `voice-dna-base.md`, then layer the user's personal style on top.

Structure:
```markdown
# Voice DNA

## Base Writing Rules
[embed the contents of voice-dna-base.md here — these are the foundation rules for natural, human-sounding writing that apply regardless of personal style]

## My Tone
[from Q5 — detailed description of their communication style, not just one word]

## Voice Characteristics
[from Q7 — expand into rich descriptions with concrete examples of what this sounds like in practice]

## Language Preferences
### Words and phrases I use
[from Q6 — specific words, greetings, sign-offs, expressions]

### Words and phrases I never use
[from Q6 — specific words, phrases, patterns to avoid]

## Anti-Voice
[from Q8 — what I must never sound like, with specific examples]

## Writing Samples
These are real examples of how I write. Use these as a reference for tone, style, and pacing.

### Email Examples
[3-5 actual email excerpts from the discovery scan — the best examples of their natural writing style]

### Message Examples
[1-3 Slack/chat message examples if available]

## Writing Patterns
Observed patterns from my actual writing:
- Greeting style: [e.g., "Hey [name]," / "Hi [name]," / "[name],"]
- Sign-off style: [e.g., "Cheers," / "Best," / "Thanks!"]
- Sentence length: [e.g., "Short and punchy" / "Mix of short and long"]
- Punctuation: [e.g., "Uses exclamation marks occasionally" / "Never uses emojis"]
- Paragraph style: [e.g., "Short paragraphs, lots of line breaks" / "Dense paragraphs"]
- Instruction style: [e.g., "Direct and clear" / "Collaborative — 'what do you think?'"]
```

**This file should be comprehensive.** Include every writing sample you found. Include every pattern. The more examples, the better Claude can match the user's voice in future sessions.

#### context/working-style.md
Generate from Q9-Q13. Structure:
```markdown
# Working Style

## Output Preferences
[from Q9 — translate the choice into clear instructions]

## Rules
[from Q10 — each rule as a clear bullet point]

## Daily Tasks
[from Q11 — the tasks they repeat daily]

## Weekly Tasks
[from Q12 — the tasks they repeat weekly]

## Tools & Workflows

| Tool | Used For | Preferences |
|------|----------|-------------|
| [tool name] | [what they use it for] | [any preferences, e.g., "check here before asking me"] |
| [tool name] | [what they use it for] | [preferences] |
| ... | ... | ... |

[from Q13 — every tool they mentioned, formatted as a clear reference table]

### Tool Rules
[any tool-specific rules or preferences from Q13, e.g., "Client comms only on Slack, never email"]
```

### Step 2: Preview and Confirm

Show each file one at a time:
> "Here's your **About Me** context file: [show content]. Look good?"

Wait for confirmation before moving to the next. If they want changes, make them.

**For Voice DNA especially**: Show it and ask:
> "Here's your **Voice DNA** — this is how I'll write as you from now on. Take a look at the writing samples and patterns. Anything I should adjust?"

### Step 3: Write Context Files

After all three are approved, create the `context/` directory and write all three files.

### Step 4: Generate Personalized Skills

Load `skill-templates.md` and generate two personalized skills.

#### Morning Brief Skill
Generate `.claude/skills/morning-brief/SKILL.md` using the template. Fill in:
- Which tools are connected (calendar, email) — from Q13
- Their daily tasks (Q11)
- Their output preferences (Q9)
- Their voice character (Q7)
- Relevant hard rules (Q10)
- Tool preferences (Q13)

**Replace all template placeholders with actual values.** The output should be a clean SKILL.md with no template syntax.

#### Inbox Triage Skill
Generate `.claude/skills/inbox-triage/SKILL.md` using the template. Fill in:
- Their role and business (Q1, Q2)
- Their daily focus (Q3)
- Their hard rules (Q10)
- Their daily tasks (Q11) — for categorization context
- Their output preferences (Q9)
- Their voice character (Q7)
- Email tool preferences (Q13)

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

Create the master instruction file with the self-correcting rules engine:

```markdown
# [Name]'s AI Workspace

@context/about-me.md
@context/voice-dna.md
@context/working-style.md

## Instructions

### Communication
- Follow the Voice DNA guidelines above in all output
- Match the output preferences in the working style guide
- Use the writing samples as reference for tone and style

### Tools
[list each connected tool with usage from Q13, e.g.:]
- Notion: project management — check here for project status before asking
- Gmail: email — never send without showing draft first
- Slack: team and client comms — primary channel for client communication
- Granola: meeting notes — check here for meeting context

### Rules
[hard rules from Q10, formatted as clear instructions]

---

## Self-Correcting Rules Engine

This section contains a growing ruleset that improves over time. **At session start, read all learned rules before doing anything.**

### How It Works
1. When the user corrects you or you make a mistake, **immediately append a new rule** to the "Learned Rules" section below
2. Rules are numbered sequentially and written as clear, imperative instructions
3. Format: `N. [CATEGORY] Never/Always do X — because Y`
4. Categories: `[STYLE]` `[TONE]` `[TOOL]` `[PREFERENCE]` `[PROCESS]` `[FORMAT]` `[COMMS]`
5. Before starting any task, scan all rules below for relevant constraints
6. If two rules conflict, the higher-numbered (newer) rule wins
7. Keep rules current — when something changes, update in place rather than appending duplicates
8. If a correction applies to a specific skill (morning-brief, inbox-triage, etc.), update that skill directly rather than adding a rule here

### When to Add a Rule
- User explicitly corrects your output ("no, do it this way")
- User rejects a file, approach, or pattern
- User states a preference ("always use X", "never do Y")
- You discover something doesn't work as expected with their tools or workflow

### Learned Rules
[Rules will be added here as the user works with the workspace]
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
> - `context/voice-dna.md` — how you sound (with real writing samples)
> - `context/working-style.md` — how you work + your full tool stack
> - `CLAUDE.md` — your global instructions + self-correcting rules engine
> - Morning brief skill — personalized daily summary
> - Inbox triage skill — email categorization
>
> **Scheduled:**
> - Morning brief: daily at [time]
> - Inbox triage: [frequency]
>
> **How the rules engine works:** Every time you correct me, I'll add a rule to your CLAUDE.md so I never make the same mistake twice. Your workspace gets smarter the more you use it.
>
> You're all set. Try saying 'morning brief' to test it out!"

## Tone Guidelines

Throughout the entire onboarding:
- **Warm but not cheesy.** Friendly, professional, encouraging.
- **Brief acknowledgments.** "Got it." "Perfect." "Makes sense." — not "That's a wonderful answer!"
- **No jargon.** Say "tools" not "MCPs". Say "instructions file" not "CLAUDE.md" (until they need to know).
- **Encouraging.** "You're doing great" if they seem hesitant. But don't overdo it.
- **Respect their time.** Keep moving. Don't over-explain things that are working.
- **Show, don't ask.** Wherever possible, show what you found and ask them to confirm, rather than asking them to explain from scratch.

## Error Handling

- **Tool connection fails**: Note it, move on, offer to retry later
- **Discovery scan finds nothing**: Skip gracefully, interview from scratch with extra examples
- **Discovery scan finds very little**: Use what you have, supplement with more examples during interview
- **User gives very short answers**: That's fine. Work with what you have. Don't push for more.
- **User wants to skip a question**: Skip it. Use reasonable defaults or leave the section minimal.
- **User wants to stop mid-flow**: Save progress so far. Tell them they can resume with `/onboard` or refine with `/update-context`.
- **Scheduling fails**: Provide manual instructions as fallback
