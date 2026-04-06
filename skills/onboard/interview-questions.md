# Interview Question Bank

Reference for the core interview in Phase 3. The main SKILL.md orchestrates when and how to ask these — this file contains the full question details, format guidance, and pre-fill logic.

## General Approach

- **One question at a time.** Never batch multiple questions.
- **Multiple choice when possible.** Reduces cognitive load for beginners.
- **Pre-fill from Discovery Scan.** If the scan found relevant info, present it: "Based on your [brand guide / bio / about page], it looks like [X]. Is that right, or would you change anything?"
- **Skip what's already answered.** If the scan gave a clear, complete answer and the user confirmed it, move on.
- **Keep it conversational.** These aren't form fields — they're a guided chat.

---

## Section A: About You → `context/about-me.md`

### Q1: Name and Role
**Ask**: "Let's start simple — what's your name and what do you do?"
**Format**: Free text
**Pre-fill**: Check bios, LinkedIn-style summaries, about pages from the discovery scan
**Pre-fill prompt**: "From your [source], I found: '[name], [role]'. Is that accurate?"
**Maps to**: about-me.md → Identity section

### Q2: Business Description
**Ask**: "In one sentence, what does your business do?"
**Format**: Free text
**Pre-fill**: Check company descriptions, about pages, website taglines
**Pre-fill prompt**: "Your [source] describes your business as '[description]'. Want to keep that or rephrase?"
**Maps to**: about-me.md → Identity section

### Q3: Daily Focus
**Ask**: "What do you spend most of your working time on? Pick all that apply."
**Format**: Multi-select
**Options**:
- Content creation (writing, video, social media)
- Client work (consulting, coaching, services)
- Strategy and planning
- Operations and admin
- Sales and outreach
- Product development
- Team management
- Other (free text)
**Pre-fill**: Can sometimes be inferred from SOPs or role descriptions, but usually needs direct input
**Maps to**: about-me.md → Daily Focus section, also feeds Phase 4 skill generation + Phase 5 skill recommendations

### Q4: Area of Expertise
**Ask**: "What's your area of expertise — the thing Claude should know you're deeply knowledgeable about?"
**Format**: Free text
**Pre-fill**: Check bios, credentials, topic-specific content
**Pre-fill prompt**: "Based on your [source], it seems your expertise is in [area]. Sound right?"
**Maps to**: about-me.md → Expertise section

---

## Section B: Your Voice → `context/brand-voice.md`

### Q5: Communication Style
**Ask**: "How do you communicate? Think about your emails, posts, and messages."
**Format**: Spectrum with examples
**Present as**: "On a scale from very formal to very casual, where do you land?"
- **Very formal**: "Dear Mr. Smith, I hope this message finds you well..."
- **Professional**: "Hi John, thanks for reaching out. Here's what I'm thinking..."
- **Conversational**: "Hey! So here's the deal..."
- **Very casual**: "yo so basically..."
**Pre-fill**: Analyze tone from brand guides, email templates, or writing samples found in scan
**Pre-fill prompt**: "Your writing in [source] reads as [level]. Does that match how you want Claude to write?"
**Maps to**: brand-voice.md → Tone section

### Q6: Language Preferences
**Ask**: "Any words or phrases you always use? Or words you'd never use?"
**Format**: Free text (two parts)
**Prompt in two parts**:
1. "First — are there words, phrases, or ways of saying things that feel very 'you'?"
2. "Now — anything you'd never say? Words or phrases that make you cringe?"
**Pre-fill**: Brand guides often have "do/don't" language lists
**Pre-fill prompt**: "Your brand guide includes these language preferences: [list]. Want to keep these or add/remove anything?"
**Maps to**: brand-voice.md → Language Preferences section

### Q7: Voice Character
**Ask**: "When Claude writes as you, what should it sound like?"
**Format**: Multiple choice (can pick 1-2)
**Options**:
- Direct and confident — gets to the point, assertive
- Warm and friendly — approachable, personal touch
- Technical and precise — detailed, data-driven
- Casual and conversational — like texting a friend
- Inspiring and motivational — big-picture, energetic
**Pre-fill**: Can sometimes be inferred from brand personality descriptions
**Maps to**: brand-voice.md → Voice Characteristics section

### Q8: Anti-Voice
**Ask**: "What should Claude NEVER sound like? Give me an example of writing that would make you say 'that's not me at all.'"
**Format**: Free text with examples
**Guidance**: If they're stuck, offer examples: "Things like 'corporate buzzwords', 'overly salesy', 'academic/dry', 'fake enthusiasm', 'generic AI voice'..."
**Pre-fill**: Brand guides sometimes have anti-voice or "don't" sections
**Pre-fill prompt**: "Your brand guide says to avoid: [list]. Anything else to add?"
**Maps to**: brand-voice.md → Anti-Voice section

---

## Section C: How You Work → `context/working-style.md`

### Q9: Output Preferences
**Ask**: "When Claude gives you something — a summary, a draft, an answer — how do you want it formatted?"
**Format**: Multiple choice
**Options**:
- Concise bullets — short, scannable, no fluff
- Detailed narrative — full explanations, thorough
- Structured with headers — organized sections, easy to navigate
- Depends on the task — let Claude decide based on context
**Maps to**: working-style.md → Output Preferences section

### Q10: Hard Rules
**Ask**: "Any hard rules? Things that must ALWAYS happen or NEVER happen when Claude works for you?"
**Format**: Free text
**Guidance**: If they're stuck, offer examples: "Things like 'never use emojis in client emails', 'always include a CTA in social posts', 'never commit to deadlines without checking with me first'..."
**Pre-fill**: Check SOPs, process docs, team guidelines
**Pre-fill prompt**: "I found these rules in your [source]: [list]. Want to keep these? Anything to add?"
**Maps to**: working-style.md → Rules section, also feeds CLAUDE.md → Rules section

### Q11: Daily Repeated Tasks
**Ask**: "What do you do every single day? Think about the tasks you repeat without thinking."
**Format**: Free text, encourage them to list multiple items
**Guidance**: "Things like 'check email', 'review calendar', 'post on social media', 'check project status', 'respond to clients'..."
**Maps to**: working-style.md → Daily Tasks section, feeds morning-brief skill generation, feeds inbox-triage skill generation

### Q12: Weekly Repeated Tasks
**Ask**: "What about weekly tasks? Things that happen on a specific day or once a week."
**Format**: Free text, encourage them to list multiple items
**Guidance**: "Things like 'write newsletter', 'team standup', 'invoice clients', 'content planning', 'review analytics'..."
**Maps to**: working-style.md → Weekly Tasks section, feeds scheduled task setup, feeds skill recommendations

---

## Post-Interview Notes

After all 12 questions, the skill should have enough to generate:
1. `context/about-me.md` — from Q1-Q4
2. `context/brand-voice.md` — from Q5-Q8
3. `context/working-style.md` — from Q9-Q12
4. Morning-brief skill — from Q3, Q7, Q9, Q11 + connected tools
5. Inbox-triage skill — from Q2, Q3, Q10, Q11 + connected email
6. Skill recommendations — from Q3, Q11, Q12
7. CLAUDE.md — from Q10 + all context files + connected tools

Before writing any files, show the user a preview of each context file and get their approval.
