# Skill Templates

Parameterized templates for the two personalized skills generated during onboarding. Replace all `{{placeholders}}` with values from the interview.

---

## Morning Brief Skill Template

Generate this at `.claude/skills/morning-brief/SKILL.md` in the user's workspace.

```markdown
---
name: morning-brief
description: Use when starting the day, checking what's on the agenda, or asking for a morning summary
user-invocable: true
---

# Morning Brief

Generate a personalized daily briefing for {{user_name}}.

## What to Check

### Calendar
{{#if google_calendar_connected}}
- Check Google Calendar for today's events
- Highlight meetings in the next 2 hours
- Note any all-day events or deadlines
{{/if}}
{{#if no_calendar}}
- No calendar connected — skip this section
{{/if}}

### Email
{{#if gmail_connected}}
- Check Gmail inbox for unread messages from real people (not automated notifications)
- Prioritize emails from: {{priority_contacts_or_categories}}
- Flag anything that needs a response today
{{/if}}
{{#if no_email}}
- No email connected — skip this section
{{/if}}

### Daily Priorities
Based on {{user_name}}'s typical day, check on:
{{#each daily_tasks}}
- {{this}}
{{/each}}

## Output Format
{{output_format_instructions}}

Present the brief in this structure:
1. **Today's Schedule** — what's on the calendar
2. **Inbox Highlights** — important emails needing attention
3. **Focus Areas** — top priorities for today based on recurring tasks and any calendar context

## Style
{{voice_instructions}}

## Rules
{{#each hard_rules}}
- {{this}}
{{/each}}
```

### How to Fill the Template

| Placeholder | Source |
|-------------|--------|
| `{{user_name}}` | Q1: Name |
| `{{google_calendar_connected}}` | Phase 1: Tool connection |
| `{{gmail_connected}}` | Phase 1: Tool connection |
| `{{priority_contacts_or_categories}}` | Derived from Q3 (daily focus) and Q11 (daily tasks) — e.g., if they do client work, prioritize client emails |
| `{{daily_tasks}}` | Q11: Daily repeated tasks |
| `{{output_format_instructions}}` | Q9: Output preferences — translate choice into instructions (e.g., "Use concise bullets, no fluff") |
| `{{voice_instructions}}` | Q7: Voice character — translate into instruction (e.g., "Keep it warm and friendly, like a helpful colleague") |
| `{{hard_rules}}` | Q10: Hard rules that apply to morning briefs |

### Important Notes

- **Don't include Handlebars syntax** in the generated file. Replace all placeholders with actual values.
- If a tool isn't connected, **omit that section entirely** — don't leave "no calendar connected" in the final skill.
- The daily tasks list should be specific to what the user told you, not generic.
- Keep the skill concise. It should fit in one screen.

---

## Inbox Triage Skill Template

Generate this at `.claude/skills/inbox-triage/SKILL.md` in the user's workspace.

```markdown
---
name: inbox-triage
description: Use when checking email, triaging inbox, or asking what needs a response
user-invocable: true
---

# Inbox Triage

Scan and categorize {{user_name}}'s inbox, highlighting what needs attention.

## Process

1. **Fetch recent unread emails** from Gmail
2. **Filter out noise** — skip automated notifications, marketing emails, and system alerts
3. **Categorize** each real email into one of these priority levels:

### Priority Levels

| Level | Meaning | Examples |
|-------|---------|---------|
| **Urgent** | Needs a response today | {{urgent_examples}} |
| **Important** | Needs attention this week | {{important_examples}} |
| **FYI** | Good to know, no action needed | {{fyi_examples}} |
| **Skip** | Auto-notifications, marketing, spam | Filtered out automatically |

## Categorization Rules

{{user_name}} is a {{role}} who focuses on {{daily_focus}}. Use this context to prioritize:

{{#each categorization_rules}}
- {{this}}
{{/each}}

## Output Format
{{output_format_instructions}}

For each email that's not "Skip", show:
- **From**: sender name
- **Subject**: email subject
- **Priority**: Urgent / Important / FYI
- **Summary**: one-sentence summary of what it's about
- **Suggested action**: what to do (reply, schedule, delegate, read later)

Group by priority level. Urgent first, then Important, then FYI.

## Style
{{voice_instructions}}

## Rules
{{#each hard_rules}}
- {{this}}
{{/each}}
- Never mark automated notifications as Urgent
- When in doubt about priority, mark as Important rather than Urgent
```

### How to Fill the Template

| Placeholder | Source |
|-------------|--------|
| `{{user_name}}` | Q1: Name |
| `{{role}}` | Q1: Role |
| `{{daily_focus}}` | Q3: Daily focus areas |
| `{{urgent_examples}}` | Derived from role + daily tasks — e.g., "Client asking about a deadline, team member blocked on your input" |
| `{{important_examples}}` | Derived from role — e.g., "New lead inquiry, collaboration request, feedback on draft" |
| `{{fyi_examples}}` | Generic + role-specific — e.g., "Industry news, team updates, event invitations" |
| `{{categorization_rules}}` | Derived from Q2 (business), Q3 (focus), Q10 (rules), Q11 (daily tasks) |
| `{{output_format_instructions}}` | Q9: Output preferences |
| `{{voice_instructions}}` | Q7: Voice character |
| `{{hard_rules}}` | Q10: Hard rules that apply to email handling |

### Important Notes

- **Replace all placeholders** with actual values. No template syntax in the output.
- The categorization rules should be highly specific to the user's business. A consultant's "urgent" is different from a content creator's "urgent."
- The priority examples should use real-world scenarios from their industry.
- If they mentioned specific people or clients in the interview, reference those in the categorization rules.
