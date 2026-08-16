# Connecting Tools — Fallback Guide

**This is the fallback.** The primary path is Cowork's own connector cards (`mcp__mcp-registry__suggest_connectors`), which render in the chat with a Connect button the user clicks. Use this guide only when:

- the connector cards don't render (a quiet `list_connectors` came back empty, or the tool isn't available — you're not in Cowork), or
- one specific tool is failing and needs troubleshooting, or
- the user asks for step-by-step directions.

<HARD-GATE>
Never claim a screen, panel, or dialog has opened, or that something "should now appear". You cannot see the user's screen and you cannot open windows for them. Describe where to look, then ask what they see. Do not use `claude://` links to open settings — they do nothing on current builds.
</HARD-GATE>

---

## The click path (Claude desktop app)

The same numbered path works for every connector, so teach it once:

1. **Customize** — top left of the window
2. **Scroll to the bottom** — connections live at the bottom of that panel
3. **Browse connectors** — top right of the connectors area
4. Find the tool, click **Connect**, and sign in when the browser opens
5. Come back to the chat and tell me it's done

If they can't find it, don't guess through five variations. Ask:

> "What do you see in the top-left of the window? Tell me the labels and I'll point you at the right one."

Wait for their answer and work from what's actually on screen. Build labels change; the user's eyes don't.

---

## Before any tool gets read: confirm the account

Whichever route they connect through, the account matters. When a tool is connected, read back the account identity the tool reports (an email address, a workspace name) and confirm it's the right one:

> "That's connected as `sam@acme.com` — is that the account you want me working from?"

If they have several accounts, ask which one before reading anything. This is the same consent gate as Phase 2 of the skill: connection is not permission.

---

## Per-tool notes

### Email (Gmail, Outlook)

- **Verification read:** list the few most recent messages. Subject lines coming back = connected.
- **"This app isn't verified"** during Google sign-in → **Advanced** → continue.
- **Wrong account connected** → disconnect, connect again, and choose the right account on the sign-in screen.
- **Work account with restrictions** → an IT admin may have to approve it. Not worth fighting during setup: mark it skipped and move on.

### Calendar (Google Calendar, Outlook)

- **Verification read:** list today's or this week's events. Event titles coming back = connected.
- Often shares its sign-in with the same Google account as email or Drive.
- **No events showing** → check the calendar they actually use belongs to the connected account, not a shared one.

### Files and documents (Google Drive, Dropbox)

- **Verification read:** list a few recent file names. File names coming back = connected.
- **"Access denied"** → usually a managed work account with restricted sharing. Try a personal account, or skip it.

### Notion

- **Verification read:** search for any recent page. Page titles coming back = connected.
- During authorization Notion asks **which pages to share** — anything not selected stays invisible. If a search finds nothing they expected, that's usually why: reconnect and grant more pages.
- Large workspaces respond slowly. That's normal, not a failure.

### Slack

- **Verification read:** list channels. Channel names coming back = connected.
- **"You don't have permission"** → a workspace admin has to approve the integration. Skip it rather than blocking setup.
- Direct messages are often out of scope — public channels only. Say so rather than looking for DMs that aren't there.

### Meeting notes (Granola and similar)

- **Verification read:** list recent meeting notes or transcripts. Titles coming back = connected.
- If it isn't offered as a connector, note it for the tool map in Q13 and move on.

### Anything else

1. Check whether it appears in the connectors list at all.
2. If it does, use the same path: find it, Connect, sign in, then verify with one small read.
3. If it doesn't: "That one isn't available as a connection yet — I'll note it in your tool map so I know you use it."

Never let a missing or stubborn tool stall the setup. One retry, then skip it and carry on.
