---
name: onboard
description: Use when setting up a new AI workspace, running guided onboarding, or bootstrapping context files for Claude Cowork
user-invocable: true
---

# Cowork Onboard

Guided onboarding that builds a personalized AI workspace. This is both a setup tool AND an educational walkthrough. The user should finish understanding what they built and why each piece matters.

<HARD-GATE>
This is a GUIDED flow. Ask ONE question at a time. Wait for the user's response before proceeding. Never batch questions. Never skip steps. Never generate files without showing a preview first.

Every question MUST include rich examples. Most users can't articulate what they want from scratch. Give them concrete examples to react to and riff on. Examples are not optional.

EDUCATIONAL REQUIREMENT: Before each major phase, explain WHAT you're about to do, WHY it matters, and HOW it will help them. The user should never feel like they're clicking through a wizard they don't understand. They should leave this onboarding genuinely understanding how their AI workspace works.
</HARD-GATE>

## Audience

The user is likely a complete beginner to Claude Cowork. Assume zero technical knowledge. Keep language simple, warm, and encouraging. Never use jargon without explaining it.

**This is a learning experience, not just a setup wizard.** Every step should leave the user understanding a concept they didn't understand before. By the end, they should be able to explain to someone else what their workspace does and why each file exists.

## Support Files

All reference files are in the same directory as this skill file (`skills/onboard/`):
- `mcp-setup-guide.md` — fallback per-tool connection instructions (only used when native connector cards aren't available)
- `interview-questions.md` — the full question bank for Phase 3 (with examples for every question)
- `skill-templates.md` — parameterized templates for morning-brief and inbox-triage
- `skill-recommendation-map.md` — role-to-skill recommendation mapping
- `voice-dna-base.md` — base writing rules embedded in every voice-dna file

When this skill says "load [filename]", read it from the same directory as this SKILL.md.

## Before You Start

Check if this workspace already has onboarding files:
- If `CLAUDE.md` exists AND `context/` folder exists → warn the user: "This workspace already has context files. Running onboarding will overwrite them. Want to continue, or would `/update-context` be better for updating specific sections?"
- If no existing files → proceed directly

---

## Phase 1: Welcome & Tool Connection

### Welcome Message

> "Hey! I'm going to walk you through setting up your AI workspace. By the end you'll have an AI assistant that genuinely knows your business, writes in your voice, and handles your recurring tasks.
>
> I'll explain everything as we go, so you'll actually understand what we're building and why — not just click through a setup wizard."

### Teach: Why Tools Come First

> "**First things first — let's connect your tools.**
>
> Here's why this is step one: the more tools I have access to, the less you have to explain to me. If I can read your emails, I can learn how you actually write. If I can see your calendar, I can build you a morning briefing. If I can search your docs, I can find your brand guidelines instead of making you describe them from memory.
>
> Think of it this way: right now I'm a new hire on day one. Connecting tools is like giving me access to the company drives, email, and Slack. Without that, I'm working blind."

### Show Available Connectors

Use the `mcp__mcp-registry__suggest_connectors` tool to display native connector cards in chat. These cards show icons, tool names, connection status, and connect/reconnect buttons — the user can connect tools directly from the cards.

**Important:** Do NOT present a manual text list of tools. The connector cards handle this natively and are far better than a text list.

After showing the cards:

1. **Acknowledge what's already connected.** If any tools show as connected, call them out: "I can see you've already connected [X, Y, Z] — nice, that gives me a head start."

2. **Proactively encourage connecting more.** Look at what's NOT connected and pitch the most valuable ones with specific reasons:
   - **Email (Gmail/Outlook):** "This is the single most valuable connection. I can learn exactly how you write from your sent emails, so I sound like you from day one."
   - **Calendar:** "Lets me build your morning briefing and know what your day looks like without asking."
   - **Docs (Google Drive/Notion):** "I can find your brand guidelines, SOPs, and business docs instead of making you describe them from memory."
   - **Communication (Slack):** "Another rich source for your writing style, plus I can see what projects and teams you're active in."
   - **Meeting notes (Granola):** "I can read your meeting transcripts to understand what you're working on and how you communicate."

   Don't limit this to a fixed list — if the connector cards show other useful tools, encourage those too. The more connected, the better.

3. **Ask if anything is missing:** "Any other tools you use daily that aren't shown here? We can always add more later."

4. **Verify connections.** For each newly-connected tool, verify with a quick test operation:
   - **Email**: Try listing recent emails
   - **Calendar**: Try listing today's events
   - **Drive**: Try listing recent files
   - **Notion**: Try searching for a recent page
   - **Slack**: Try listing channels
   - If a test fails: try one troubleshooting step. If still failing: "No worries — we can connect this later. Let's keep going."

### Fallback (non-Cowork environments)

If the `mcp__mcp-registry__suggest_connectors` tool is not available, fall back to the manual approach:

1. Ask: "What tools do you use day-to-day? Think about email, calendar, notes, docs, communication, and meeting tools."
2. For each tool they mention, load the relevant section from `mcp-setup-guide.md` and walk them through connection step by step.
3. Follow the same verification tests above.

### Transition

> "Great, tools are connected. Now let me put them to work. I'm going to dig through your emails, messages, and docs to learn how you write and what your business is about. This saves you from having to explain everything from scratch."

---

## Phase 2: Discovery & Validation

### Teach: What's Happening and Why

> "**Here's what I'm doing right now:**
>
> I'm reading through your recent messages and emails to learn your writing style — how you greet people, how formal or casual you are, what phrases you use. I'm also searching your docs for any brand guides, SOPs, or business docs that already describe who you are and how you work.
>
> **Why this matters:** In a few minutes, I'm going to create a 'Voice DNA' file — a detailed profile of how you write, so that every time you use this workspace, I sound like you, not like a generic AI. The more real examples I can pull now, the more accurate that voice profile will be."

### Beat 1: Scan All Connected Sources

Scan every connected tool for writing samples and business context. **Don't privilege any single source** — pull equally from everything available.

#### Communication Tools (Writing Style)
For each connected communication tool (email, Slack, etc.):
- Pull recent messages/emails **sent by the user** (last 30-60 days)
- Focus on messages to real people (not automated replies or notifications)
- Collect 3-5 representative writing samples from EACH source
- Note patterns: greeting style, sign-off style, sentence length, formality level, humor, punctuation habits, emoji usage

#### Document Tools (Business Context)
For each connected doc tool (Drive, Notion, etc.):
- Search for brand guidelines, style guides, tone-of-voice documents
- Search for about pages, bios, company descriptions
- Search for SOPs, process docs, team guidelines
- Search for client proposals (communication style)
- Search for any document with "brand", "style", "guide", "about", "SOP", "process", "bio", "tone"

#### Meeting Notes
For connected meeting note tools (Granola, etc.):
- Pull recent meeting transcripts for verbal communication style
- Pull meeting summaries for context on current work

#### Other Context
- Email signatures → name, role, company, links
- Recent threads → what they're working on, who they work with
- Newsletter subscriptions → interests and industry
- Channel names (Slack) → teams and projects

### Beat 2: Ask for Additional Writing Sources

After the automated scan, explicitly ask:

> "I've pulled writing samples from your connected tools. But some of your best writing might live elsewhere.
>
> **Where else does your writing show up?** For example:
> - Newsletters you write (Substack, Beehiiv, Mailchimp)
> - Blog posts on your website
> - Social media posts (LinkedIn, X, Instagram captions)
> - YouTube scripts or descriptions
> - Community posts (Reddit, forums, Discord)
>
> If you have examples, just copy-paste some samples here. The more I have, the more I'll sound like you."

Wait for their response. If they provide text, add it to the writing samples collection. If they say "no" or "that's it", move on.

### Beat 3: Present Findings

Show what you found — be specific and use their actual writing:

> "Here's what I found across your [list sources scanned]:
>
> **Your writing style**: You're [conversational/professional/etc.]. Your messages tend to be [short and direct / detailed and thorough / warm and personal].
>
> **Examples of your actual writing:**
> 1. *[Source]*: '[actual excerpt]'
> 2. *[Source]*: '[actual excerpt]'
> 3. *[Source]*: '[actual excerpt]'
>
> **Patterns I noticed:**
> - You [always/never/usually] [pattern]
> - You tend to [pattern]
> - Your greetings are usually [style]
>
> **Other context I found:**
> - [Brand guide / bio / SOP from docs]
> - [Business context from email signatures]"

If nothing found (no tools connected or no useful content):
> "I couldn't find existing docs or messages to learn from — no worries, we'll figure out your style through the interview. It'll just mean a few more questions."

### Context Validation Gate

<HARD-GATE>
Do NOT proceed to Phase 3 until the user has explicitly validated the discovered context. This is not optional.
</HARD-GATE>

After presenting findings, deliver the validation prompt:

> "Before we move on — I need you to be ruthless here.
>
> **Please double-check everything I've found above. Tell me explicitly if anything is:**
> - **Outdated** — old role, old company, old guidelines that no longer apply
> - **Wrong** — I misread something or it doesn't represent you accurately
> - **Not relevant** — stale docs, archived projects, one-off writing that isn't your normal style
>
> I'd rather you over-correct now than have me treat old docs as facts. If that brand guide from 2022 doesn't reflect how you work today, tell me. If that email was a one-off tone, flag it.
>
> **What should I drop or correct?**"

Wait for their response. If they flag items, remove or correct them. If they say "looks good", confirm: "Great — I'll treat everything above as current and accurate."

### Hold All Validated Results
Keep everything that survived validation — writing samples, patterns, documents — in context. These feed directly into Phase 3 pre-fills and Phase 4 file generation.

---

## Phase 3: Core Interview

### Teach: What We're Building

> "**Now for the interview.** I'm going to ask you about 13 questions — who you are, how you want me to sound, how you work, and what tools you use. Don't worry about getting everything perfect — you can update any of this later with `/update-context`.
>
> **What these answers become:** I'll turn your answers into three files that live in your workspace:
> 1. **About Me** — so I always know your role, business, and expertise
> 2. **Voice DNA** — so I write like you, not like a robot
> 3. **Working Style** — so I know your preferences, rules, daily tasks, and tools
>
> **Why files, not just memory?** These files load automatically every time you open this workspace. You can read them, edit them, and they're always up to date. It's like an employee handbook, but for your AI.
>
> Quick tip — you can click the microphone button in the chat bar to answer any of these by voice. Sometimes it's easier to just talk than type."

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

Transition — teach what Voice DNA is:
> "**Now for the fun part — your Voice DNA.**
>
> This is a profile of how you actually write. Not a brand guide — your personal writing fingerprint. I already have a head start from your [emails/messages/docs]. The next few questions will sharpen it.
>
> **Why this matters:** Without Voice DNA, every AI workspace sounds the same — polished, generic, corporate. With it, when I draft an email or write a social post for you, it sounds like *you* wrote it. People who get that email won't be able to tell the difference."

Ask Q5 through Q8 from `interview-questions.md`, one at a time. These should be heavily pre-filled from the discovery scan. Show actual writing samples for every voice-related question.

#### Section C: How You Work (Q9-Q13)

Transition:
> "Last section — how you like to work, your rules, and your tools."

Ask Q9 through Q13 from `interview-questions.md`, one at a time.

**Q13 (Tool Stack) is important.** Teach why:
> "**One more — let's map out your tools.**
>
> This creates a reference sheet so I always know where to look for information. Instead of asking you 'where are your meeting notes?', I'll already know they're in Granola. Instead of emailing a client, I'll know you only do client comms on Slack.
>
> The goal: reduce the number of times I have to interrupt you with a question."

Load the full examples from the question bank.

### After the Interview

> "That's all the questions! Now I'm going to turn everything you told me into your workspace files. I'll show you each one before I save it."

---

## Phase 4: Build the Workspace

### Teach: What We're Creating

> "**Now I'm going to build your workspace — a folder called OS (your operating system).**
>
> This is the folder you'll open in Cowork from now on. Every time you open it, I automatically read your context files before we even start talking. It's like leaving yourself a set of notes that your AI reads before every conversation.
>
> Inside OS, you'll have:
> - **CLAUDE.md** — the master instructions file I read first every session
> - **context/** — your knowledge base (who you are, how you write, how you work)
> - **active/** — where all generated output goes (research, drafts, exports, anything I create)
>
> The **context** folder is your second brain — it's the source of truth about you and your business. Before I do anything, I check there first. The **active** folder keeps your workspace clean — instead of files piling up everywhere, everything I generate goes into organised subfolders inside active/.
>
> You can open and edit any of these files anytime. They're yours."

### Step 1: Create the OS Folder

Create a folder called `OS` on the user's **Desktop** (`~/Desktop/OS/`) with `context/` and `active/` subfolders inside it. This is their workspace root — the folder they'll open in Cowork from now on.

```
~/Desktop/OS/
  CLAUDE.md
  context/
    about-me.md
    voice-dna.md
    working-style.md
  active/
```

### Step 2: Generate Context Files

Using the interview answers AND the validated discovery scan data, generate three files. **Show each file to the user before writing it.**

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
Generate from Q5-Q8 + the validated discovery scan writing samples from ALL sources. This is the most important file — it should be rich and specific, not a few light sentences.

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

### Other Writing
[any additional samples from newsletters, blog posts, social media, etc. that the user provided]

## Writing Patterns
Observed patterns from my actual writing:
- Greeting style: [e.g., "Hey [name]," / "Hi [name]," / "[name],"]
- Sign-off style: [e.g., "Cheers," / "Best," / "Thanks!"]
- Sentence length: [e.g., "Short and punchy" / "Mix of short and long"]
- Punctuation: [e.g., "Uses exclamation marks occasionally" / "Never uses emojis"]
- Paragraph style: [e.g., "Short paragraphs, lots of line breaks" / "Dense paragraphs"]
- Instruction style: [e.g., "Direct and clear" / "Collaborative — 'what do you think?'"]
```

**This file should be comprehensive.** Include every validated writing sample. Include every pattern. The more examples, the better Claude can match the user's voice in future sessions.

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

### Step 3: Preview and Confirm

Show each file one at a time:
> "Here's your **About Me** context file: [show content]. Look good?"

Wait for confirmation before moving to the next. If they want changes, make them.

**For Voice DNA especially**: Show it and ask:
> "Here's your **Voice DNA** — this is how I'll write as you from now on. Take a look at the writing samples and patterns. Anything I should adjust?"

### Step 4: Write Context Files

After all three are approved, write them to `~/Desktop/OS/context/`:
- `~/Desktop/OS/context/about-me.md`
- `~/Desktop/OS/context/voice-dna.md`
- `~/Desktop/OS/context/working-style.md`

### Teach: What CLAUDE.md Is

> "**Now for the most important file in your workspace — CLAUDE.md.**
>
> This is your master instructions file. It's the very first thing I read every time you start a new conversation. It imports your context files and contains your rules.
>
> Think of it like a briefing document. Before we talk about anything, I've already read: who you are, how you write, how you work, what tools you use, and what rules to follow. You never have to re-explain yourself.
>
> It also has two important built-in behaviours:
>
> 1. **Context-first philosophy** — before I do anything, I check your context files and connected tools for answers. I only ask you a question as a last resort, once I've exhausted everything I can look up myself. No lazy questions.
>
> 2. **Self-correcting rules engine** — every time you correct me, I write it down as a permanent rule. So if you say 'don't do that', it never happens again. Over time, this workspace gets smarter the more you use it."

### Step 5: Generate and Write CLAUDE.md

Create the master instruction file with the self-correcting rules engine:

```markdown
# [Name]'s AI Workspace

## Context — Second Brain

@context/

The context folder is the source of truth for who [Name] is, how they write, how they work, and what tools they use. It is loaded automatically above.

**Before any task or question, check context first.** Don't work from assumptions — find the answer. If context/ doesn't have it, check connected tools (Gmail, Notion, Slack, Granola, calendar) before asking [Name]. Only come to [Name] with a question once you've exhausted all available sources.

**Assumptions are the enemy.** Every decision and answer must be rooted in fact — from context files, from connected tools, or from the workspace itself. If you're unsure, look it up. If you can't find it anywhere, then ask.

## Workspace Structure

```
OS/
├── CLAUDE.md          ← this file (master instructions)
├── context/           ← second brain (about-me, voice-dna, working-style)
└── active/            ← all generated output (research, drafts, exports)
```

[Update this map as the workspace grows — add new folders and descriptions so future sessions can navigate without exploring.]

## Instructions

### Communication
- Follow the Voice DNA guidelines in all output
- Match the output preferences in the working style guide
- Use the writing samples as reference for tone and style

### Tools
[list each connected tool with usage from Q13, e.g.:]
- Notion: project management — check here for project status before asking
- Gmail: email — never send without showing draft first
- Slack: team and client comms — primary channel for client communication
- Granola: meeting notes — check here for meeting context

### Rules
- All generated output goes in `active/` — don't pollute root. Use structured subfolders within active/ (e.g., `active/research/`, `active/drafts/`, `active/exports/`). Create a subfolder when a new type of output emerges.
[hard rules from Q10, formatted as clear instructions]

---

## Self-Correcting Rules Engine

This section contains a growing ruleset that improves over time. **At session start, read all learned rules before doing anything.**

### How It Works
1. When [Name] corrects you or you make a mistake, **immediately append a new rule** to the "Learned Rules" section below
2. Rules are numbered sequentially: `N. [CATEGORY] Never/Always do X — because Y`
3. Categories: `[STYLE]` `[TONE]` `[TOOL]` `[PREFERENCE]` `[PROCESS]` `[FORMAT]` `[COMMS]`
4. Before starting any task, scan all rules for relevant constraints
5. If two rules conflict, the higher-numbered (newer) rule wins
6. Keep rules current — update in place rather than appending duplicates

### When to Add a Rule
- [Name] explicitly corrects your output ("no, do it this way")
- [Name] rejects a file, approach, or pattern
- [Name] states a preference ("always use X", "never do Y")
- You discover something doesn't work as expected with tools or workflows

### Learned Rules
[Rules will be added here as [Name] works with the workspace]
```

Show preview and get confirmation. Write CLAUDE.md to `~/Desktop/OS/CLAUDE.md`.

### Teach: What Skills Are

> "**Your workspace foundation is done. Now let's add skills on top of it.**
>
> A skill is a set of instructions that tells me how to do a specific task for you. Think of it like a recipe card. Right now, I can do anything you ask — but I'll do it generically. A skill makes me do it *your* way, with *your* tools, in *your* voice.
>
> I'm going to create two skills based on what you told me:
>
> 1. **Morning Brief** — a daily summary of your calendar, inbox, and priorities. Instead of you opening 5 tabs and checking everything manually, you just say 'morning brief' and I give you a single summary.
>
> 2. **Inbox Triage** — I read your unread emails, filter out the noise, and categorize what's left by urgency. You get a clean list of what actually needs your attention.
>
> **How skills work in Cowork:** Skills are saved globally in the Cowork app — not inside your OS folder. They're available across all your projects. I'll show you each skill in chat, and Cowork will give you a **'Save Skill' button** to save it. Just click that button for each one."

### Step 6: Generate Personalized Skills

Load `skill-templates.md` and generate two personalized skills.

#### Morning Brief Skill
Generate the morning-brief skill using the template. Fill in:
- Which tools are connected (calendar, email) — from Q13
- Their daily tasks (Q11)
- Their output preferences (Q9)
- Their voice character (Q7)
- Relevant hard rules (Q10)
- Tool preferences (Q13)

**Replace all template placeholders with actual values.** The output should be a clean skill with no template syntax.

#### Inbox Triage Skill
Generate the inbox-triage skill using the template. Fill in:
- Their role and business (Q1, Q2)
- Their daily focus (Q3)
- Their hard rules (Q10)
- Their daily tasks (Q11) — for categorization context
- Their output preferences (Q9)
- Their voice character (Q7)
- Email tool preferences (Q13)

**Replace all template placeholders with actual values.**

### Step 7: Present Skills for Saving

<IMPORTANT>
Do NOT write skills to the filesystem. Cowork cannot create skill files in `.claude/skills/`. Instead, output each skill's full content directly in chat. Cowork will automatically show a "Save Skill" button that the user clicks to save it globally.
</IMPORTANT>

For each skill:

1. Show the complete skill content in chat (the full SKILL.md content including YAML frontmatter)
2. Tell the user: "You should see a **'Save Skill' button** above. Click it to save this skill to your Cowork app."
3. Wait for them to confirm they saved it
4. Then move to the next skill

> "Here's your personalized **Morning Brief** skill. Click the **'Save Skill' button** that appears above to add it to your Cowork. Once it's saved, you can use it anytime by saying 'morning brief'."
>
> [output the full morning-brief skill content]

After they confirm:

> "Now here's your **Inbox Triage** skill. Same thing — click **'Save Skill'** to add it."
>
> [output the full inbox-triage skill content]

### Teach: What Scheduled Tasks Are

> "**Now let's automate these.**
>
> Right now you'd have to open Cowork and type 'morning brief' every day. But we can schedule it to run automatically — so when you sit down with your coffee, the brief is already waiting for you.
>
> Same for inbox triage — it can run a few times a day so your inbox is always pre-sorted."

### Step 8: Set up Scheduled Tasks

Ask the user:
> "What time do you usually start your day? I'll schedule your morning brief for then."

Then:
> "And how often should I triage your inbox?"
> - Once in the morning
> - Morning and afternoon
> - Three times: morning, midday, and evening

Set up scheduled tasks using the `/schedule` skill. For each task, invoke `/schedule` with:
- **Morning brief**: `create` a scheduled trigger that runs the `morning-brief` skill daily at their chosen time (e.g., "every day at 7am")
- **Inbox triage**: `create` a scheduled trigger that runs the `inbox-triage` skill at their chosen frequency (e.g., "every day at 9am, 1pm, and 5pm")

If the `/schedule` skill is not available, or scheduling fails, provide manual instructions: "Scheduling isn't set up yet, but you can run these anytime by saying 'morning brief' or 'triage my inbox'. You can set up automation later with the `/schedule` command."

---

## Phase 5: Wrap-up

### Skill Recommendations

Load `skill-recommendation-map.md`. Based on Q3 (daily focus) and Q11/Q12 (tasks), recommend 2-3 relevant skills:

> "**One more thing — skill recommendations.**
>
> Remember how we created the morning brief and inbox triage skills? There are loads more you can add. Based on what you do day-to-day, these would be useful:
>
> 1. **[skill]** — [what it does for them, in plain language]
> 2. **[skill]** — [what it does for them]
> 3. **[skill]** — [what it does for them]
>
> These are optional — you can install them anytime by asking me."

### Summary and Education Recap

> "**Your workspace is ready! Here's what we built and why:**
>
> **Your OS folder** (on your Desktop — open this in Cowork from now on):
> - `CLAUDE.md` — master instructions, the first thing I read every session
> - `context/` — your second brain (who you are, how you write, how you work)
> - `active/` — where all generated output goes (keeps your workspace clean)
>
> **Built-in behaviours:**
> - **Context-first** — I always check your context files and tools before asking you anything
> - **Self-correcting** — every correction becomes a permanent rule, so mistakes don't repeat
> - **Clean workspace** — all output goes in `active/` with organised subfolders
>
> **Skills** (saved globally in Cowork, available everywhere):
> - Morning brief — say 'morning brief' for a daily summary
> - Inbox triage — say 'triage my inbox' to sort your email
>
> **Scheduled automation:**
> - Morning brief: daily at [time]
> - Inbox triage: [frequency]
>
> **How to use it:** Close this chat, then open the **OS folder** in Cowork. That's your workspace from now on. Every new conversation will start with me already knowing who you are and how you work.
>
> **How it gets better over time:** Every time you correct me, I add a rule to CLAUDE.md. Every time you update a preference, the context files change. This workspace learns. It's not static — it grows with you.
>
> **Useful commands to remember:**
> - `/update-context` — update any part of your workspace
> - `morning brief` — run your daily briefing
> - `triage my inbox` — sort your email
>
> You're all set. Open your OS folder and try saying 'morning brief' to take it for a spin!"

---

## Tone Guidelines

Throughout the entire onboarding:
- **Warm but not cheesy.** Friendly, professional, encouraging.
- **Teacher mode.** Explain concepts clearly, use analogies, make sure they understand before moving on.
- **Brief acknowledgments.** "Got it." "Perfect." "Makes sense." — not "That's a wonderful answer!"
- **No jargon.** Say "tools" not "MCPs". Say "instructions file" not "CLAUDE.md" (until you explain it). Say "recipe card" not "skill" (until you explain it).
- **Explain jargon when you introduce it.** When you first use a term like "context file" or "skill", explain what it means in plain language.
- **Encouraging.** "You're doing great" if they seem hesitant. But don't overdo it.
- **Respect their time.** Keep educational moments concise — 2-4 sentences, not lectures. Teach through doing, not through essays.
- **Show, don't ask.** Wherever possible, show what you found and ask them to confirm, rather than asking them to explain from scratch.
- **Use analogies.** "Like a new hire's first day", "Like a recipe card", "Like a briefing document". Real-world comparisons land better than abstract explanations.

## Error Handling

- **Tool connection fails**: Note it, move on, offer to retry later
- **Discovery scan finds nothing**: Skip gracefully, interview from scratch with extra examples
- **Discovery scan finds very little**: Use what you have, supplement with more examples during interview
- **User gives very short answers**: That's fine. Work with what you have. Don't push for more.
- **User wants to skip a question**: Skip it. Use reasonable defaults or leave the section minimal.
- **User wants to stop mid-flow**: Save progress so far. Tell them they can resume with `/onboard` or refine with `/update-context`.
- **Scheduling fails**: Provide manual instructions as fallback
- **User seems confused**: Pause and re-explain the current concept. Ask "Does that make sense?" before continuing.
- **suggest_connectors unavailable**: Fall back to manual tool selection using `mcp-setup-guide.md`
