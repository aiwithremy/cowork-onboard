# Cowork Onboard

Guided setup for Claude Cowork. One command turns a folder on your computer into an AI workspace that knows who you are, how you write, and how you like to work.

## What you get

- **Your workspace folder** — set up inside a folder you choose and connect, with a place for everything Claude generates
- **Voice DNA** — Claude learns how you actually write from writing samples you approve, then writes as you instead of like a generic AI
- **Context files** — who you are, how you work, your rules, and your full tool map
- **Master instructions** — a `CLAUDE.md` that loads all of it at the start of every conversation, with a self-correcting rules engine: correct Claude once and it writes the rule down permanently

**Time:** about 20-30 minutes, most of it answering questions. You can stop partway and pick up where you left off.

## What it deliberately doesn't do

- It doesn't create, save, or recommend skills
- It doesn't set anything up to run on a schedule
- It doesn't send, post, or change anything in your email, calendar, or documents — it is read-only throughout
- It doesn't write anywhere outside the folder you connect

## How it works

1. **Confirm your folder** — Claude checks which folder is connected to the conversation and asks whether that's the one to use. If it's a busy folder like your Desktop, it offers to make one tidy subfolder instead. There is no default location and nothing is written until you agree to the path.
2. **Connect your tools** — Cowork's connector cards appear in the chat with Connect buttons. Claude explains what each tool is worth, then proves each connection with a real read before calling it connected.
3. **Approve what Claude may look at** — before anything is read, Claude names the exact account and says exactly what it would read and how far back ("about 20 of your own sent emails from the last 30 days"). You say yes or no per source. No is a complete answer.
4. **Discovery and validation** — Claude reads only the approved sources, shows you what it found (including a receipt of what it looked at), and asks you to reject anything outdated, wrong, or irrelevant before it goes near a file.
5. **The interview** — around 13 questions, one at a time, every one with examples so you're never staring at a blank prompt.
6. **Preview and build** — every file is shown in full before it's written, then Claude lists the folder to prove the files actually landed.

## Installing it in Cowork

1. Open Cowork's plugins area (the screen where Cowork lists plugins and skills) and choose **Add marketplace**.
2. Paste this repository URL:

   ```
   https://github.com/aiwithremy/cowork-onboard
   ```

3. Confirm with **Sync**. Cowork fetches the marketplace for you — this works because the repository is public.
4. Install the **cowork-onboard** plugin from the list.
5. Start a new conversation so the plugin loads.

Button labels move around between app versions. If you can't find "Add marketplace", look for wherever Cowork lists plugins or skills — that's the screen. If you're in the Claude Code surface of the desktop app instead of Cowork, you can type `/plugin marketplace add https://github.com/aiwithremy/cowork-onboard` into the chat box, which does the same thing.

## Connect a folder first

Cowork can only write into folders you've connected to the conversation, so the workspace has to live in one.

1. Make a new empty folder wherever you keep your work, and call it whatever you like.
2. Connect that folder to a Cowork conversation.
3. Then run:

   ```
   /onboard
   ```

If nothing is connected yet, `/onboard` will stop and ask you to connect a folder rather than guessing a location.

## Updating later

```
/update-context
```

Pick the part you want to refresh — about you, your voice, or how you work. It edits only the sections you discuss and leaves everything else, including anything you've written by hand, exactly as it was.

## What gets created

Inside the folder you connected (or the subfolder you agreed to):

```
your-folder/
  CLAUDE.md              # master instructions + self-correcting rules engine
  context/
    about-me.md          # identity, role, business, expertise
    voice-dna.md         # writing style, tone, real samples, anti-patterns
    working-style.md     # output preferences, rules, routines, tool map
  active/                # where everything Claude generates goes
```

Plus one hidden file, `.onboard-progress.json`, which is how the setup remembers where you got to. Cowork doesn't carry memory between conversations, so that file is the bookmark — resuming means opening the same folder and running `/onboard` again.

## Author

AI with Remy — [aiwithremy.com](https://aiwithremy.com)

## License

MIT
