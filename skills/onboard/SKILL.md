---
name: onboard
description: Use when setting up an AI workspace in Claude Cowork, running guided onboarding, or building a personal workspace (AGENTS.md instructions, a CLAUDE.md pointer, context files, and working folders that match the person's job) for a connected folder
user-invocable: true
---

# Cowork Onboard

Guided onboarding that turns a connected folder into a personal AI workspace: one instructions file (`AGENTS.md`), a tiny `CLAUDE.md` pointer to it, three context files, and a set of working folders built from the person's actual job. This is both a setup tool AND a short lesson — the user should finish understanding what they built and why each piece matters.

## What this skill does and does NOT do

**It does:** confirm which folder is connected, help the user connect their tools, verify those connections with real reads, learn from sources they explicitly approve, run a short interview one question at a time, propose a folder structure that mirrors their real work, preview every file, then create and verify the workspace.

**It does NOT:** create, save, or recommend skills. Set up scheduled or recurring runs. Send, post, reply to, or change anything in a connected tool. Write anywhere outside the folder the user has connected.

If the user asks for any of those, say plainly that this setup doesn't do it, finish the setup, and let them decide separately afterwards.

<HARD-GATE>
1. **One question at a time.** Wait for the user's answer before asking the next. Never batch questions. Never skip steps.
2. **Read-only on their tools, and only what they approved.** You may only READ, never send, reply, post, delete, move, or modify anything. Two levels of approval: the one-item connection check in Step 1.3, which you ask for in the moment, and the full source approval in Phase 2, which covers everything after that.
3. **Never claim something happened that you did not verify.** No "I've opened that screen for you", no "your folder is created", no "you're connected" without a real result in front of you: a successful read, or a directory listing showing the path.
4. **Never write outside the confirmed workspace folder**, and never assume a path. There is no default location — not a folder on the Desktop, not one in Documents, not one named `OS`. A folder only becomes the workspace when the user has connected it and confirmed it out loud.
5. **Preview before writing.** Show every file's full content and get an explicit yes before it is written.
6. **Examples with every question.** Most users can't articulate what they want from scratch. Give concrete examples to react to.
</HARD-GATE>

## Audience

The user is likely brand new to Claude Cowork and not technical. Assume zero technical knowledge. Warm, plain English, no jargon without a one-line translation. Every step should leave them understanding something they didn't understand before.

## Support files

All reference files sit in the same folder as this SKILL.md (`skills/onboard/`):

- `interview-questions.md` — the full question bank for Phase 5, with examples for every question
- `mcp-setup-guide.md` — fallback connection directions, used only when Cowork's connector cards aren't available
- `voice-dna-base.md` — base writing rules embedded in every generated `voice-dna.md`

When this skill says "load [filename]", read it from that folder.

---

## Phase 0: Welcome, workspace folder, resume check

### Step 0.1 — Welcome and set honest expectations

> "Hey! I'm going to help you set up your AI workspace — a folder on your computer that holds everything I need to know about you, so every future conversation starts with me already understanding your business, how you write, and how you like to work.
>
> **Time:** about 25–35 minutes. Most of it is me asking you questions, so it moves at your pace.
>
> **You can stop anytime.** I save our progress as we go, so if you close this or run out of time, we pick up where we left off.
>
> **What I'll do:** help you connect your tools, learn what I can from the ones you approve, ask you some questions, work out the folders your job actually needs, then build it all and show you everything before I save it.
>
> **What I won't do:** touch anything in your email or accounts — I'm read-only the whole way through. And I won't set anything running on a schedule."

### Step 0.2 — Identify the connected folder (never guess)

The workspace has to live in a folder Cowork can actually write to — one the user has connected to this conversation.

1. **Look first.** Use your file tools to list the folder(s) available in this conversation. Note the exact path as the app reports it.
2. **Confirm it in plain language**, showing the path exactly as you saw it — never reformatted, never converted between Mac and Windows styles:
   > "It looks like the folder connected here is `[exact path]`. Is that the folder you want to use as your AI workspace?"
3. **If no folder is connected** (you cannot list or write anywhere), stop and explain:
   > "Before we build anything, I need access to a folder on your computer — that's where your workspace files will live. In Cowork, connect a folder to this conversation (a new empty folder is perfect — you can call it anything), then tell me when it's done and I'll pick it up from here."
   Wait. Do not proceed, and do not invent a path.

<HARD-GATE>
Never assume a location. Do not create anything in a Desktop folder, a Documents folder, or any other path just because it's the conventional choice. The workspace root is ONLY ever a folder the user has connected and confirmed in this conversation.
</HARD-GATE>

### Step 0.3 — Decide: this folder, or a subfolder inside it?

Look at what's already in the confirmed folder, then propose one of two options and let the user choose:

- **Empty, or clearly meant for this** → use the folder itself as the workspace root.
  > "This folder's empty, so I'll build your workspace right here in `[path]`. Good with you?"
- **A broad folder with unrelated things in it** (a Desktop, Documents, Downloads, or home folder, or a folder full of existing projects) → propose a subfolder so nothing of theirs gets mixed up.
  > "This folder already has your own files in it, so I'd rather not scatter things around. I'll make one new folder inside it called `OS` — that's your workspace, everything I build goes in there and nothing else gets touched. Want me to do that, or would you rather I use a different name?"

Record the agreed absolute path as **`WORKSPACE_ROOT`** and use it for every path from here on. Say it back once, plainly, and don't repeat it every message.

**If an `AGENTS.md` (or `CLAUDE.md`) and a `context/` folder already exist at `WORKSPACE_ROOT`:** don't overwrite silently.
> "This folder already has a workspace set up. I can start fresh and replace those files, or you can use `/update-context` to refresh just one part. Which would you prefer?"

### Step 0.4 — Resume check

Read `[WORKSPACE_ROOT]/.onboard-progress.json` (see **Save and resume** below for the shape).

- **Not there** → normal first run. Continue to Phase 1. Don't create the file yet.
- **`"status": "in_progress"`** → offer the choice, then wait:
  > "Looks like we got partway through last time — we were on [phase, in plain words]. Want to pick up from there, or start fresh?"
  On resume, re-check reality before trusting the file: confirm the folder still exists and re-verify tool connections with a real read (a tool marked `pending` may have finished connecting since). On fresh start, clear the saved state and begin at Phase 1.
- **`"status": "complete"`** → tell them the setup is already done and offer `/update-context` for a single section, or a fresh run.

---

## Save and resume

The progress file is the only thing that makes "come back later" safe. Cowork does not carry memory between conversations — a new chat starts blank — so **the file in their folder is the entire bookmark**, and resuming requires the same folder to be connected. Say that plainly when you mention resuming; never imply the chat will remember on its own.

**Location:** `[WORKSPACE_ROOT]/.onboard-progress.json` — a hidden file (the leading dot keeps it out of sight) at the workspace root. It's the only hidden file this setup ever leaves behind.

**Shape** (write the whole file every time, never a partial update):

```json
{
  "schema_version": 1,
  "product": "cowork-onboard",
  "workspace_root": "<the confirmed absolute path>",
  "status": "in_progress",
  "phase": "interview",
  "started_at": "2026-08-16T09:00:00Z",
  "last_updated": "2026-08-16T09:22:00Z",
  "sources_approved": { "email": "sam@acme.com", "calendar": "sam@acme.com", "docs": "declined" },
  "tools": { "gmail": "connected", "google-calendar": "connected", "notion": "pending" },
  "discovery_validated": true,
  "answers": { "Q1": "Sam, freelance brand strategist", "Q2": "..." },
  "working_areas": {
    "status": "approved",
    "proposed": ["northwind/briefs", "northwind/ad-reports", "swipe-file"],
    "approved": ["northwind/briefs", "northwind/ad-reports", "swipe-file"]
  },
  "files_written": ["context/about-me.md"],
  "folders_created": ["context", "northwind/briefs"]
}
```

- `phase` is one of: `connect`, `consent`, `discovery`, `interview`, `working-areas`, `build`, `complete`. The file is first written at the end of Phase 1, once `WORKSPACE_ROOT` is confirmed and there's something worth remembering.
- `answers` holds confirmed answers by question number, so a resumed run never re-asks them.
- `working_areas` is the folder structure agreed in Phase 6: `proposed` is what you offered, `approved` is what the user actually signed off, each entry a path relative to `WORKSPACE_ROOT` written with forward slashes, one line per deepest folder. `status` is `proposed` or `approved`. **Write it as soon as you propose it**, so an interrupted run never loses the tree — a resumed run shows the saved tree back and asks whether it still stands instead of starting the design from scratch.
- `files_written` lists files already saved and `folders_created` lists folders already made, so a resumed build continues where it stopped instead of redoing work.
- On finishing, set `status: "complete"`, drop `answers`, and keep `workspace_root`, `working_areas.approved`, and `phase: "complete"`.
- **The example values above are illustrative** — that tree belongs to one imaginary strategist, not to the person in front of you.

**When to write it:** at the end of each phase, after each file is written, and after each tool is connected or skipped. Not after every single question — natural pause points only.

**If writing it fails:** try once more as a visible file named `onboarding-progress.md` in the same folder (same information, written as plain readable notes). If that also fails, be honest rather than silent:

> "Heads up — I can't save a progress note in this folder, so if this conversation ends we'd have to start the questions again. I'll keep going, and I'll give you a short summary of your answers at the end that you can paste back to me if we ever need to."

Then continue, and keep a running recap you can hand them on request.

---

## Phase 1: Connect tools, and verify them

### Teach: why tools come first

> "**First, let's connect your tools.**
>
> Here's why this is step one: the more I can see, the less you have to explain. If I can read the emails you've sent, I can learn how you actually write. If I can see your calendar, I understand the shape of your week. If I can look at your documents, I can find what you've already written down instead of asking you to describe it from memory.
>
> Think of me as a new hire on day one. Connecting tools is like giving me a login — without it, I'm working blind.
>
> All of it is read-only during this setup, and you'll approve each thing before I look at it."

### Step 1.1 — Show the connector cards (Cowork's native way)

Run a quiet `list_connectors` first to work out which surface you're on:

- **A card renders** → you're in Cowork. Use `mcp__mcp-registry__suggest_connectors` to show connector cards in the chat: icons, connection status, and Connect buttons the user can click directly. Do not paste a text list of tools instead — the cards are better.
- **Empty result or the tool isn't there** → the cards don't render here. Use the fallback in `mcp-setup-guide.md`.

<HARD-GATE>
Never tell the user a screen, panel, or card "has opened" or "should now appear" unless a tool result actually shows it. If you're not sure what they can see, ask them to tell you what's on their screen.
</HARD-GATE>

### Step 1.2 — Talk them through what's worth connecting

1. **Acknowledge what's already connected:** "I can see [X and Y] are already connected — that gives us a head start."
2. **Make the case for the most valuable missing ones**, one reason each:
   - **Email** — "The single most useful one. Your sent emails show me how you really write, so I sound like you from day one."
   - **Calendar** — "Shows me the shape of your week without you describing it."
   - **Documents (Google Drive, Notion)** — "Lets me find things you've already written — an about page, a style guide, a process doc — instead of asking you to repeat them."
   - **Team chat (Slack)** — "Another good source for how you write, plus what you're working on."
   - **Meeting notes (Granola and similar)** — "Shows me what you're working on and how you talk."
   Don't limit yourself to that list — if the cards show something else useful, mention it.
3. **Ask once:** "Anything you use every day that isn't in that list? We can always add more later."
4. **Skipping is fine.** If they'd rather not connect something, say so cheerfully and move on: the interview works without it, it just means a few more questions.

### Step 1.3 — Verify each connection with one small read (ask first)

A connection only counts when a read actually returns something — a tool can look connected and still be broken. But this is their inbox, so ask before you touch it, even for a check:

> "Quick check so we know it's actually working: can I list the titles of a couple of recent items? Titles only — I won't open anything."

Once they say yes, do exactly that one read: **titles, names, or subject lines only — never message bodies, never document contents.** The fuller question of what you may actually learn from comes next, in Phase 2. If they'd rather you didn't check, that's fine: say the connection is unverified and move on.

Report the result honestly:

| Tool | Verification read | What proves it |
|---|---|---|
| Email | list the few most recent messages | subject lines come back |
| Calendar | list today's or this week's events | event titles come back |
| Drive / files | list a few recent file names | file names come back |
| Notion | search for any recent page | page titles come back |
| Slack | list channels | channel names come back |

- **It works** → "That's live — I can see your [emails/events/files]."
- **It fails** → try one fix (usually reconnecting and picking the right account). Still failing: "No problem, let's leave that one. We can add it later." Mark it `skipped` in the progress file and move on. Never let one tool block the flow.

Save progress (`phase: "connect"`).

---

## Phase 2: Confirm exactly what I may look at

<HARD-GATE>
Beyond the single titles-only connection check in Step 1.3, do NOT read any email, event, document, message, or transcript before the user has approved that source here. Approval is per source, out loud, and specific about the account. If they decline a source, it is off-limits for the rest of the run — including its titles.
</HARD-GATE>

### Teach: why I'm asking

> "Now, before I actually read anything, I want to be clear about what I'd be looking at — it's your inbox and your calendar, and you should decide, not me.
>
> I only need a little, and only to save you typing. Here's exactly what I'd look at, and you can say no to any of it."

### Step 2.1 — Name the account, then ask per source

For each connected source, state the account identity you can actually see (the email address or workspace name the tool reports — if you can't see it, ask), say precisely what you'd read and how far back, then ask for a yes or no. One at a time.

> "**Email — `[account the tool reports]`.** I'd read about 20 of your own recent sent messages from the last 30 days, to learn how you write: greetings, sign-offs, sentence length, that kind of thing. I won't open anything else in your inbox. OK to look?"

> "**Calendar — `[account]`.** I'd look at event titles and times for the next couple of weeks, just to understand your week. I don't need the invitee lists or the notes. OK?"

> "**Documents — `[account/workspace]`.** I'd search for files whose names suggest they describe you or your business — an about page, a style or brand guide, a process doc. I'll show you the list and only open the ones you pick. OK?"

> "**Team chat / meeting notes — `[account/workspace]`.** I'd read a handful of your own recent messages or notes for writing style. OK?"

Rules for this step:

- **More than one account connected?** Ask which one to use. Never scan both because both are available.
- **A shared or work account?** Ask before reading it: "That looks like a work account — happy for me to read from it, or would you rather I use a personal one?"
- **"No" or "skip"** is a complete answer. Record it as `declined` and never revisit it in this run.
- **Documents get a second gate**: names first, contents only after they pick.
- Record every decision in the progress file under `sources_approved`, then save (`phase: "consent"`).

---

## Phase 3: Discovery — learn from the approved sources only

### Teach: what's happening

> "Right, I'm going to read the sources you approved and see what I can learn — mainly how you write, plus anything that describes your business.
>
> **Why:** in a few minutes I'll write a 'Voice DNA' file — a description of how you write, so that in future I sound like you instead of like a generic AI. Real examples of your own writing make that far more accurate than anything you could describe from memory."

### Step 3.1 — Scan (approved sources only)

**Writing style** — from approved email/chat/meeting sources:
- Pull recent messages the user themselves sent, to real people (not automated replies or notifications).
- Collect 3–5 representative samples from each approved source.
- Note the patterns: greeting, sign-off, sentence length, formality, humour, punctuation habits, emoji use.

**Business context** — from approved document sources:
- Look for names suggesting a brand or style guide, an about page or bio, a company description, a process document or SOP, a client proposal.
- Show the shortlist of names and let the user pick which to open. Only open those.

**Light context** — from what you already have: an email signature (name, role, company), what recent threads are about, channel or calendar names that reveal projects and teams.

**Stay inside the limits you stated.** If a limit turns out to be too small, ask for more rather than quietly widening it.

### Step 3.2 — Ask where else their writing lives

> "Some of your best writing probably isn't in any of those. Anywhere else it shows up — a newsletter, blog posts, LinkedIn or X, YouTube scripts, community posts? Paste a couple of samples here if you have them handy. Totally optional."

Wait. Add anything they paste to the samples. "No" moves on.

### Step 3.3 — Show what you found, with a receipt

Be specific, quote their actual words, and say what you read:

> "Here's what I found.
>
> **What I looked at:** [e.g. 18 sent emails from the last 30 days, 12 calendar events, 2 documents you picked].
>
> **How you write:** [conversational / professional / direct…], usually [short and to the point / detailed / warm].
>
> **Your actual words:**
> 1. *[source]*: '[real excerpt]'
> 2. *[source]*: '[real excerpt]'
> 3. *[source]*: '[real excerpt]'
>
> **Patterns:** you [always/never/usually] [pattern]; your greetings are usually [style]; your sign-offs are usually [style].
>
> **About your business:** [what the bio / about page / signature says]."

If nothing useful came back (nothing connected, or nothing approved):
> "I didn't find anything to learn from — no problem at all. We'll build it from your answers instead; it just means a few more questions."

---

## Phase 4: Validation gate — you correct me before I write anything

<HARD-GATE>
Do NOT continue to the interview until the user has explicitly validated what you found. Not optional.
</HARD-GATE>

> "Before we go on — be ruthless with me here.
>
> **Check what's above and tell me if anything is:**
> - **Out of date** — an old role, old company, guidelines that don't apply any more
> - **Wrong** — I've misread something, or it just isn't you
> - **Not relevant** — a stale document, a dead project, a one-off email that isn't how you normally write
>
> I'd much rather you over-correct now than have me treat an old document as fact for the next year.
>
> **What should I drop or fix?**"

Wait. Remove or correct whatever they flag — no arguing. If they say it looks good, confirm once: "Great, I'll treat all of that as current." Keep everything that survived; it feeds the interview pre-fills and the files. Save progress (`phase: "discovery"`, `discovery_validated: true`).

---

## Phase 5: The interview

### Teach: what we're doing and what it becomes

> "**Now the interview — around 15 questions**, one at a time. Nothing here has to be perfect; you can change any of it later with `/update-context`.
>
> **Your answers become three files in your workspace:**
> 1. **About Me** — your role, your business, what you're expert in
> 2. **Voice DNA** — how you write, so I sound like you
> 3. **Working Style** — how you like things done, your rules, your routines, your tools
>
> **And the last couple of questions build your folders** — the actual areas of your work, so this workspace looks like your job rather than a generic template.
>
> **Why files rather than me just remembering?** Because a new conversation starts blank. Files don't — they load every time you open this folder, and you can read and edit them yourself. It's a handbook for your AI.
>
> Tip: you can answer by voice with the microphone button in the chat bar if talking is easier than typing."

Load `interview-questions.md` for the full bank, including every example. Then:

1. **One question at a time.** Wait for the answer.
2. **Always show the examples.** They're in the bank for a reason.
3. **Pre-fill from what survived validation:** "From your emails it looks like [X] — here are the bits I'm going by: [real excerpts]. Right?"
4. **Skip what's already settled.** A confirmed pre-fill needs no second question.
5. **Acknowledge briefly.** "Got it." "Makes sense." Not "what a wonderful answer".
6. **Short answers are fine.** Never push. "Skip" is allowed on any question.
7. **Save progress every few answers** — `answers` by question number, `phase: "interview"`.

**Section A: About you (Q1–Q4).** "Let's start with the basics — who you are and what you do."

**Section B: Your Voice DNA (Q5–Q8).** Transition:
> "**Now the interesting part — your Voice DNA.** This is your writing fingerprint, not a brand guide. I've got a head start from your [emails/messages/docs]; these questions sharpen it.
>
> **Why it matters:** without it, everything I write comes out polished and generic. With it, an email I draft sounds like you wrote it."

These should be heavily pre-filled. Show real samples with every voice question.

**Section C: How you work (Q9–Q13).** Transition: "Last stretch — how you like to work, your rules, and your tools."

Q13 (the tool map) earns its own line:
> "**Let's map your tools.** This is so I know where to look instead of asking you. If your meeting notes live in Granola, I'll go there. If client conversations only happen on Slack, I won't draft an email. The goal is fewer interruptions for you."

**Section D: The work itself (Q14–Q15).** Transition:
> "**Two more, and these ones build your folders.** I want this workspace to match the work you actually do — so instead of dropping everything into one big pile, I'll make a folder for each real area of your job, and we'll shape it together in a minute."

Q14 asks for their areas of work; Q15 asks what they repeatedly make or keep inside each one. Pre-fill both from the approved sources where you can — recurring client, project, or programme names in the documents, calendar entries, or channels they let you look at — and say where each suggestion came from. Never pre-fill from a declined source, and never present a ready-made list of standard folders for them to accept.

### After the interview

> "That's all the questions. Next I'll sketch out your folders and show you the files — nothing gets created until you've seen it and said yes."

---

## Phase 6: Design your working areas

### Teach: your folders should look like your job

> "**Now let's shape your folders.**
>
> Most setups hand you one generic folder for everything and leave you to sort it out later. I'd rather this workspace look like your actual job from day one — a folder for each real area of your work, so anything I make lands where you'd naturally go looking for it.
>
> These come from your answers, not from a template. Two people at the same company end up with completely different folders."

### Step 6.1 — Draft the tree from what they actually told you

Build the proposal from Q14 and Q15, plus anything that survived validation in Phase 4: recurring client, project, or programme names in the sources they approved, calendar or channel names, document titles. Never from a source they declined, and never from a standard list.

Drafting rules:

- **The top-level folders are their real areas of work**, named in their words. Three to seven is the healthy range; fewer is fine when the job genuinely is.
- **Add a second level only where they named repeated, distinct things** they make or keep inside that area. One level is a perfectly good answer.
- **Never invent a taxonomy.** No default set of folders, no scaffolding added because it looks tidy. If they didn't say it, it doesn't get a folder.
- **Never assume clients or projects.** Plenty of jobs have neither, and forcing a client folder on someone who doesn't work that way makes the whole workspace feel wrong.
- **Never turn a one-off into a folder.** Folders are for things that repeat.
- **Thin answers mean a smaller tree.** Two honest folders beat six invented ones — say so out loud: "You gave me two clear areas, so I've kept it to two. We can add more any time."
- **Folders only, no files.** Do not copy anything out of their email, documents, or messages into these folders. Moving real content in is a separate conversation with its own permission.

Two illustrative shapes, to show how *different* the answers can be. They are examples, never a menu to choose from, and never a default:

*Illustrative only — a creative strategist working across a few clients:*

    northwind/
      briefs/
      ad-reports/
    lumen-health/
      briefs/
      ad-reports/
    swipe-file/

*Illustrative only — an operations manager inside one company:*

    suppliers/
    finance/
      invoices/
    events/
    team-onboarding/

### Step 6.2 — Make the names safe before you show them

- **Use their words, lightly tidied**: lowercase, spaces turned into hyphens, nothing but letters, digits and hyphens. Keep each name under about 40 characters.
- **Strip what a file system fights over**: `/ \ : * ? " < > |`, leading dots, trailing dots and spaces.
- **Reserved at the workspace root** — never propose a top-level folder named `context`, `AGENTS.md`, `CLAUDE.md`, `.onboard-progress.json`, or `onboarding-progress.md`, comparing case-insensitively (`Context` collides with `context`). If one of their areas genuinely goes by that name, explain the clash in one line and ask for a different folder name.
- **Two areas that tidy down to the same name** — ask which they meant or ask for a name for each. Never silently merge them, and never append a number to make the clash go away.
- **A folder of that name already exists** in the workspace — leave it exactly as it is, use it, and tell them it was already there. Never overwrite, merge, or delete anything of theirs.
- **If tidying changed the meaning at all**, show the before and after and let them correct it: "You said 'Q4 / EMEA' — I'd call the folder `q4-emea`. Good, or would you name it differently?"

### Step 6.3 — Show the tree, with a reason for every folder

Save the draft to the progress file first (`working_areas` with `status: "proposed"`), so the tree survives even if the conversation ends on this message. Then show the whole thing in one message, followed by one plain line per top-level folder saying why it exists — traceable to something they told you, in their language:

> "Here's what I'd build, based on what you told me:
>
>     [workspace folder]/
>       [area]/
>         [sub-area]/
>       [area]/
>
> - **[area]/** — because you said [their words].
> - **[area]/** — for the [thing they said they make every week].
>
> Change anything: rename them, drop the ones you'd never open, add what I've missed, or tell me to flatten it into fewer folders. What would you change?"

### Step 6.4 — Get an explicit yes

<HARD-GATE>
Do NOT create a single folder until the user has approved the tree in this conversation. Silence is not approval, and a lukewarm "sure, fine" is worth one clarifying question.
</HARD-GATE>

Apply every correction they give and show the revised tree again. Then save progress (`phase: "working-areas"`) with `working_areas` holding both what you proposed and what they approved, so an interrupted run rebuilds the agreed tree instead of asking again.

---

## Phase 7: Preview the files

### Teach: what we're building

> "**Here's the shape of your workspace:**
>
> - **AGENTS.md** — your instructions file. Who you are, how you write, how you work, and your rules. It's the first thing I read in a new conversation.
> - **CLAUDE.md** — a one-line pointer to AGENTS.md, so Claude lands on the same instructions as any other AI tool. Nothing else lives in it.
> - **context/** — your second brain: who you are, how you write, how you work.
> - **[their folders]** — the working areas we just agreed, where your actual work lives.
>
> Everything in there is plain text. You can open it, read it, edit it — it's yours, and it isn't locked inside any app."

Generate each file from the interview answers plus the validated discovery, and show it in full before writing.

### context/about-me.md

From Q1–Q4:

```markdown
# About Me

## Identity
- **Name**: [Q1]
- **Role**: [Q1]
- **Business**: [Q2]

## Expertise
[Q4]

## Daily Focus
[Q3, written as natural language]

## Key Context
[anything else useful that survived validation]
```

### context/voice-dna.md

From Q5–Q8 plus every validated writing sample. **This is the file that earns its keep — make it rich and specific, not four vague sentences.** Start with the base rules from `voice-dna-base.md`, then layer their own style on top.

```markdown
# Voice DNA

## Base Writing Rules
[embed the contents of voice-dna-base.md here]

## My Tone
[Q5 — a real description, not one word]

## Voice Characteristics
[Q7 — expanded, with concrete examples of what it sounds like in practice]

## Language Preferences
### Words and phrases I use
[Q6 — specific words, greetings, sign-offs, expressions]

### Words and phrases I never use
[Q6 — what to avoid]

## Anti-Voice
[Q8 — what I must never sound like, with examples]

## Writing Samples
Real examples of how I write. Use these for tone, style, and pacing.

### Email Examples
[3–5 real excerpts — the best examples of their natural writing]

### Message Examples
[1–3 chat examples if available]

### Other Writing
[anything they pasted: newsletter, blog, social]

## Writing Patterns
- Greeting style: [e.g. "Hey [name],"]
- Sign-off style: [e.g. "Cheers,"]
- Sentence length: [e.g. short and punchy]
- Punctuation: [e.g. rarely uses exclamation marks, never emojis]
- Paragraph style: [e.g. short paragraphs with plenty of line breaks]
- Instruction style: [e.g. direct and clear]
```

Include every sample that survived validation. More real examples means a closer match later.

### context/working-style.md

From Q9–Q13:

```markdown
# Working Style

## Output Preferences
[Q9 — as clear instructions]

## Rules
[Q10 — one bullet per rule]

## Daily Routines
[Q11]

## Weekly Routines
[Q12]

## Tools & Workflows

| Tool | Used for | Notes |
|---|---|---|
| [tool] | [what it's for] | [e.g. "check here before asking me"] |

[Q13 — every tool they mentioned]

### Tool Rules
[tool-specific preferences from Q13, e.g. "client comms on Slack, never email"]

## Work Areas

The folders in this workspace and what belongs in each (agreed in setup, from Q14-Q15):

| Folder | What lives in it |
|---|---|
| `[area]/` | [what they said this area is, and what they make in it] |
```

### AGENTS.md

Teach it first:

> "**The most important file: AGENTS.md.**
>
> It's the first thing I read in every new conversation. It pulls in your context files and holds your rules — so before we've said a word, I already know who you are, how you write, how you work, and what to avoid. You never have to explain yourself twice.
>
> It also carries two habits:
>
> 1. **Look it up before asking you** — I check your context files and your connected tools first, and only come to you when I genuinely can't find the answer.
> 2. **Corrections become permanent** — when you correct me, I write it down as a rule in this file, so the same mistake doesn't come back."

```markdown
# [Name]'s AI Workspace

## Context — my second brain

@context/

The context folder is the source of truth for who [Name] is, how they write, how they work, and what tools they use. It loads automatically through the line above.

**Check context before asking.** Don't work from assumptions — find the answer. If `context/` doesn't have it, check the connected tools before asking [Name]. Only ask once you've genuinely run out of places to look.

## Workspace structure

    [workspace folder name]/
    ├── AGENTS.md          ← this file: the instructions every AI tool reads first
    ├── CLAUDE.md          ← one line pointing here, so Claude loads the same instructions
    ├── context/           ← second brain (about-me, voice-dna, working-style)
    ├── [area]/            ← [what this area of [Name]'s work is, in their words]
    └── [area]/
        └── [sub-area]/    ← [what [Name] makes or keeps in here]

Keep this map up to date as the workspace grows, so a future session can navigate without exploring.

## Instructions

### Communication
- Follow the Voice DNA in everything written for [Name]
- Match the output preferences in the working style file
- Use the writing samples as the reference for tone and pacing

### Tools
[one line per connected tool, from Q13 — e.g.:]
- Notion: project management — check here for project status before asking
- Gmail: email — never send anything without showing the draft first
- Slack: team and client conversations
- Granola: meeting notes — check here for meeting context

### Rules
- Work belongs in the area it's about: save what you make into the matching folder above, in the sub-folder that fits. Don't leave files loose at the workspace root, and ask [Name] before creating a new top-level folder.
- Instructions live in this file. `CLAUDE.md` stays a one-line pointer to it — never move rules or context into it, and never keep a second copy of these instructions anywhere.
[the hard rules from Q10, written as clear instructions]

---

## Self-Correcting Rules Engine

A growing set of rules that makes this workspace better over time. **Read every learned rule at the start of a session, before doing anything.**

### How it works
1. When [Name] corrects you, **append a new rule** to the list below straight away
2. Number them: `N. [CATEGORY] Always/Never do X — because Y`
3. Categories: `[STYLE]` `[TONE]` `[TOOL]` `[PREFERENCE]` `[PROCESS]` `[FORMAT]` `[COMMS]`
4. Scan the rules before starting any task
5. If two rules conflict, the newer (higher-numbered) one wins
6. Update a rule in place rather than adding a near-duplicate

### When to add a rule
- [Name] corrects your output ("no, do it this way")
- [Name] rejects a file, a format, or an approach
- [Name] states a preference ("always X", "never Y")
- You discover something about a tool that a future session needs to know

### Learned Rules
[Rules get added here as [Name] works]
```

### CLAUDE.md

Teach it in two lines, then show it:

> "**And this one is deliberately tiny: CLAUDE.md.**
>
> Different AI tools look for their instructions under different file names. Claude looks for `CLAUDE.md`. So that file holds a single line pointing at `AGENTS.md` — Claude opens it, immediately loads your real instructions, and nothing has to be written twice. One set of instructions, no copies to keep in sync."

```markdown
# [Name]'s AI Workspace

@AGENTS.md

The instructions for this workspace live in `AGENTS.md`, which the line above loads into the conversation. This file exists only so Claude, which looks for a file with this name, lands on exactly the same instructions as every other tool. Don't add rules or context here — edit `AGENTS.md`.
```

Keep it to that. If you ever find yourself explaining a rule inside `CLAUDE.md`, the rule belongs in `AGENTS.md` instead.

### Approval

Show the files one at a time and wait for a yes on each:

> "Here's your **About Me** file: [full content]. Look right?"

For Voice DNA, ask specifically:
> "Here's your **Voice DNA** — this is how I'll write as you from now on. Have a proper look at the samples and patterns. Anything off?"

For AGENTS.md, point out what it does:
> "Here's your **AGENTS.md** — the instructions I'll read at the start of every conversation, including the folder map we agreed. Anything you'd change?"

`CLAUDE.md` is one line and a sentence of explanation — show it, but there's nothing to decide.

Make any changes they ask for and show it again. Nothing gets written without a yes.

---

## Phase 8: Build it, then prove it

<HARD-GATE>
Never say a folder or file was created until you have listed the path and seen it. If a write fails, say so plainly and stop — do not report success you didn't verify.
</HARD-GATE>

### Step 8.1 — Create the folders

Using your file tools (not assumed terminal commands), create inside `WORKSPACE_ROOT`:

- `context/`
- every folder in `working_areas.approved`, parents before children, exactly as approved — no extras, no renames, nothing "helpful" that wasn't on the list

Update `folders_created` in the progress file as you go. If a folder already exists, keep it and its contents untouched.

Then **list `WORKSPACE_ROOT`** (and each area that has sub-folders) **and check every approved folder appears.**

### Step 8.2 — Write the approved files

Write, one at a time, updating `files_written` in the progress file after each:

- `[WORKSPACE_ROOT]/context/about-me.md`
- `[WORKSPACE_ROOT]/context/voice-dna.md`
- `[WORKSPACE_ROOT]/context/working-style.md`
- `[WORKSPACE_ROOT]/AGENTS.md`
- `[WORKSPACE_ROOT]/CLAUDE.md`

The working-area folders stay empty of files — they are the person's own space, and nothing from their tools goes into them without a separate conversation.

### Step 8.3 — Verify and show the evidence

List the workspace folder, its `context/` folder, and each working area that has sub-folders, then show the user the real listing:

```
[workspace folder]/
  AGENTS.md
  CLAUDE.md
  context/
    about-me.md
    voice-dna.md
    working-style.md
  [area]/
    [sub-area]/
  [area]/
```

Check every file and every approved folder off against the real listing — from `working_areas.approved` in the progress file, not from memory. Only then can you say the workspace is built. If something is missing: name what didn't save, try once more, and if it still fails explain what you'd need (usually write access to that folder) instead of glossing over it.

**If a write is refused** — the most likely cause is that the folder isn't connected with permission to write. Say that in plain words and ask them to connect it, then continue from here. Never redirect the files somewhere else without asking.

Save progress (`phase: "build"`).

---

## Phase 9: Wrap up

Show their real folder names here, not placeholders — read them back from `working_areas.approved`.

> "**Your workspace is ready.** Here's what's in it and why it matters:
>
> **In `[workspace folder]`:**
> - `AGENTS.md` — your instructions, the first thing I read every session
> - `CLAUDE.md` — one line pointing at AGENTS.md, so Claude reads the same thing
> - `context/about-me.md` — your role, business, expertise
> - `context/voice-dna.md` — how you write, with real samples
> - `context/working-style.md` — your preferences, rules, routines, tools
>
> **And your working areas — this is your live working space, not a demo:**
>
>     [area]/
>       [sub-area]/
>     [area]/
>
> - `[area]/` — [why it exists, in their words]
>
> Put your own files in there too. When you ask me for something, it goes in the folder it belongs to, so you always know where to look.
>
> **Built-in habits:**
> - I look things up in your context and tools before asking you
> - When you correct me, it becomes a permanent rule in AGENTS.md
> - What I make for you gets saved into the matching working area, so nothing piles up at the root
>
> **How to use it:** open this folder in Cowork whenever you want to work with me. Every new conversation starts with me already knowing who you are.
>
> **To change anything:** run `/update-context` and pick the part you want to refresh — including adding a working area you've since realised you need. Or just open the file and edit it yourself — it's plain text.
>
> **What I deliberately didn't do:** I haven't created any skills and I haven't set anything running on a schedule. This setup is your foundation — nothing runs by itself.
>
> Try it: start a new conversation in this folder and ask me something about your business. You'll notice I already know the answer."

Finally: write the progress file with `status: "complete"` and `phase: "complete"`, and confirm to yourself that `workspace_root` and `working_areas.approved` are saved.

---

## Tone guidelines

- **Warm, not cheesy.** Friendly, encouraging, calm.
- **Teacher mode, briefly.** 2–4 sentences per explanation, never a lecture. Teach through doing.
- **Short acknowledgements.** "Got it." "Perfect." "Makes sense."
- **No jargon.** Say "tools" not "MCPs"; say "instructions file" until you've explained what AGENTS.md is.
- **Use everyday analogies.** A new hire's first day. A briefing document. An employee handbook.
- **Show, don't quiz.** Where you can, show what you found and ask them to confirm it.
- **Honest, always.** If something didn't work, say so. A cheerful false claim costs you all their trust.

## Error handling

- **No folder connected** → stop at Phase 0.2 and ask them to connect one. Never guess a path.
- **A tool won't connect** → one retry, then mark it skipped and move on.
- **A source is declined** → fine. It's off-limits for the whole run; the interview covers the gap.
- **Nothing found in discovery** → say so, and interview from scratch with extra examples.
- **Very short answers** → work with what you have. Don't push.
- **They want to skip a question** → skip it and keep the section light.
- **They want to stop** → save progress, then: "All saved. When you're ready, open this same folder in Cowork and run `/onboard` — I'll pick up right where we left off."
- **They can't name their work areas** → don't fill the gap with a template. Reflect back what they said in the earlier questions ("you mentioned invoices and supplier chasing — are those two areas?"), propose the smallest honest tree, and say plainly that folders are easy to add later.
- **A proposed folder name clashes** with `context`, `AGENTS.md`, `CLAUDE.md`, the progress file, another proposed area, or a folder already sitting in the workspace → say which name clashes and why, and ask for a different one. Never rename it silently, never number it, never overwrite what's already there.
- **A folder can't be created** → name the folder, retry once, then say what's blocking it. Build the rest, and be explicit about which areas are missing rather than showing a tree that isn't real.
- **A write fails** → name the file, retry once, then explain honestly what's blocking it.
- **The progress file can't be written** → tell them resume won't be automatic, and offer the recap they can paste back.
- **Connector cards don't render** → use `mcp-setup-guide.md`, and never claim a screen appeared.
- **They seem confused** → stop and re-explain the current idea. "Does that make sense?" before moving on.

---

## Self-Improvement Loop

After a run, propose a one-line change to this skill **only if it would change what a future run does** — a step that confused a real user, a claim that turned out to be false, a check that should have existed. High bar: most runs propose nothing.

- **Running from Remy's source checkout of `cowork-onboard`?** On approval, edit this `SKILL.md` (or the support file concerned) in place and commit it to the repo, then bump the version in `plugin.json`, `.claude-plugin/plugin.json`, and `.claude-plugin/marketplace.json` together and run `scripts/check_plugin.py`.
- **Running as an installed plugin?** The installed copy is a read-only snapshot and edits there would vanish on the next update. Instead, tell the user the one-line improvement and ask them to send it to AI with Remy so it lands in the plugin for everyone.

Never silently change behaviour in someone's installed copy, and never write to a file outside the confirmed workspace to record a proposal.
