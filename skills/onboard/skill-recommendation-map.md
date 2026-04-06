# Skill Recommendation Map

After the interview, recommend 2-3 relevant skills based on the user's role and daily tasks. These are skills from common Claude Code plugins — not skills we create, just suggestions for what to install.

## How to Use

1. Look at Q3 (daily focus) and Q11/Q12 (daily/weekly tasks)
2. Match against the categories below
3. Pick the top 2-3 most relevant recommendations
4. Present conversationally: "Based on what you do, I'd recommend checking out these skills: [list]. They're optional but would extend what your workspace can do."

---

## Recommendations by Role/Focus

### Content Creator
**Signals**: Selected "content creation" in Q3, mentions writing/video/social in Q11/Q12
- **instagram-carousel** — create carousel posts from any topic or content
- **viral-hooks** — generate scroll-stopping hooks for short-form video and written content
- **youtube-description** — transcribe videos and generate YouTube descriptions
- **transcribe** — turn any video URL into text
- **humanise-text** — make AI-generated text sound natural

### Consultant / Coach
**Signals**: Selected "client work" in Q3, mentions clients/calls/proposals in Q11/Q12
- **doc-coauthoring** — co-write proposals, reports, and deliverables
- **pptx** — create and edit presentations
- **pdf** — read, create, and manipulate PDFs
- **xlsx** — work with spreadsheets for data and reporting

### Agency Owner
**Signals**: Selected "team management" + "client work", mentions team/projects in Q11/Q12
- **doc-coauthoring** — collaborative document creation
- **pptx** — client presentations
- **xlsx** — project tracking, reporting

### Sales / Outreach
**Signals**: Selected "sales and outreach" in Q3, mentions leads/pipeline/email in Q11/Q12
- **icp-builder** — build ideal customer profiles
- **lead-magnet-launcher** — create lead magnet funnels
- **domain-name-brainstormer** — find domain names for projects

### Operations / Admin
**Signals**: Selected "operations and admin" in Q3, mentions scheduling/invoicing/processes
- **xlsx** — spreadsheets for tracking and reporting
- **pdf** — document processing
- **docx** — document creation and editing

### Strategy / Planning
**Signals**: Selected "strategy and planning" in Q3, mentions planning/analysis/research
- **llm-council** — run decisions through an AI advisory council
- **doc-coauthoring** — write strategy docs
- **landing-page-analysis** — analyze competitor pages

### Product / Development
**Signals**: Selected "product development" in Q3, mentions building/shipping/code
- **frontend-design** — create production-grade interfaces
- **webapp-testing** — test web applications with Playwright
- **mcp-builder** — create custom MCP integrations

---

## General Recommendations (for everyone)

These are always worth mentioning regardless of role:
- **pdf** — everyone works with PDFs
- **doc-coauthoring** — everyone writes documents

## Presentation Format

Keep it brief and actionable:

```
Based on your focus on [content creation / client work / etc.], these skills would pair well with your workspace:

1. **[skill-name]** — [one-line description of what it does for them]
2. **[skill-name]** — [one-line description]
3. **[skill-name]** — [one-line description]

These are optional plugins you can install anytime. Want me to explain any of them?
```
