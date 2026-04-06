# MCP Setup Guide

Reference document for guiding users through connecting their tools in Claude Cowork. Load the relevant section based on which tool the user selected.

## How to Use This Guide

For each tool the user wants to connect:
1. Read the relevant section below
2. Walk them through step-by-step
3. After they say it's connected, verify with the test operation
4. If the test fails, troubleshoot briefly. If it still fails, note it and move on

Keep instructions conversational, not robotic. One step at a time, wait for confirmation before the next.

---

## Google Drive / Docs

### Connection Steps
1. In Cowork, click the **tools icon** (wrench/plug icon) in the bottom-left area
2. Look for **Google Drive** in the available integrations
3. Click **Connect** — a browser window will open
4. Sign in to your Google account and grant access
5. Return to Cowork — you should see Google Drive listed as connected

### Verification Test
Search for a recent document:
- Try listing recent files from Google Drive
- If you can see file names, the connection works

### Common Issues
- **"Access denied"**: The user may need to use a personal Google account rather than a managed workspace account with restricted permissions
- **Browser didn't open**: Try clicking Connect again. If it still doesn't work, check that the default browser is set correctly
- **Wrong account**: Click Disconnect, then Connect again and choose the right Google account

---

## Gmail

### Connection Steps
1. In Cowork, click the **tools icon** in the bottom-left area
2. Look for **Gmail** in the available integrations
3. Click **Connect** — a browser window will open
4. Sign in and grant Gmail access (read and send permissions)
5. Return to Cowork — Gmail should show as connected

### Verification Test
Try listing recent emails:
- Search for recent inbox messages
- If you can see subject lines, the connection works

### Common Issues
- **"This app isn't verified"**: Click "Advanced" → "Go to [app name]" to proceed
- **Only want read access**: Note that some operations require send access. You can always decline individual actions later
- **Multiple email accounts**: Connect your primary business email first. You can add more later

---

## Google Calendar

### Connection Steps
1. In Cowork, click the **tools icon**
2. Look for **Google Calendar** in the available integrations
3. Click **Connect** — may share the same auth as Google Drive if already connected
4. Grant calendar access
5. Return to Cowork — Calendar should show as connected

### Verification Test
Try listing upcoming events:
- Check today's or this week's calendar events
- If you can see event titles and times, the connection works

### Common Issues
- **No events showing**: Check that the calendar you use is the primary calendar on the connected account
- **Shared calendars**: Shared/team calendars may not appear. Focus on the primary calendar for now

---

## Notion

### Connection Steps
1. In Cowork, click the **tools icon**
2. Look for **Notion** in the available integrations
3. Click **Connect** — a Notion authorization page will open
4. Select which Notion workspace to connect
5. Choose which pages/databases to grant access to (you can select all or specific ones)
6. Click **Allow access**
7. Return to Cowork — Notion should show as connected

### Verification Test
Try searching for a recent page:
- Search Notion for a page you know exists
- If you can see page titles, the connection works

### Common Issues
- **"No workspaces available"**: Make sure you're logged into the right Notion account in your browser
- **Can't see certain pages**: During authorization, you need to explicitly select which pages to share. Reconnect and select more pages if needed
- **Slow response**: Notion API can be slow with large workspaces. This is normal

---

## Slack

### Connection Steps
1. In Cowork, click the **tools icon**
2. Look for **Slack** in the available integrations
3. Click **Connect** — Slack authorization will open
4. Select your Slack workspace
5. Review and approve the permissions
6. Return to Cowork — Slack should show as connected

### Verification Test
Try listing recent channels:
- Search for a channel you know exists
- If you can see channel names, the connection works

### Common Issues
- **"You don't have permission"**: You may need workspace admin approval. Ask your Slack admin to approve the integration
- **Wrong workspace**: Disconnect and reconnect, making sure to select the correct workspace
- **Can't see DMs**: The integration may only have access to public channels by default

---

## Other Tools

If the user mentions a tool not covered above:
1. Check if it's available in Cowork's integrations panel
2. If yes, guide them through the generic flow: tools icon → find the integration → Connect → authorize → verify
3. If not available, note it for later: "That tool isn't available as a direct integration yet, but we can work with it in other ways later."

Don't let a missing tool block the onboarding flow.
