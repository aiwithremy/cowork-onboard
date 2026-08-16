---
description: "Set up your AI workspace — connect your tools, answer a few questions, get your context files and the folders your work lives in"
---

Use the `cowork-onboard:onboard` skill to run the full onboarding flow.

Before anything else, follow the skill's Phase 0: work out which folder is connected to this conversation and confirm it with the user. Never assume a location — no default path, and no writing outside the folder they confirm.

Then check for `.onboard-progress.json` at the confirmed workspace root:

- **In progress** → offer to pick up where the last run stopped, or start fresh. Wait for their answer.
- **Complete** → the workspace is already built. Offer `/update-context` to refresh one part, or a fresh run that replaces the existing files.
