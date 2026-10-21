---
name: sell-bot--routine-daily-account-watch
description: "Routine: Disabled by default. Weekdays 8:56am: credit runway, expansion, watched accounts, and X."
version: 1.0.0
platforms: [linux, macos, windows]
metadata:
  hermes:
    tags: ["sell-bot", "grok-bot", "routine"]
    related_skills: ["sell-bot--sell-setup", "sell-bot--accounts", "sell-bot--draft-email", "sell-bot--schedule", "sell-bot--watch-on-x", "sell-bot--prep-page"]
---
# Routine: Daily account watch

Original schedule: Disabled by default. Weekdays 8:56am: credit runway, expansion, watched accounts, and X.

This routine ships disabled. Before enabling, confirm the timezone, the credit, spend, and usage sources, the thresholds, and the watched accounts.

When enabled:
1. Read memory and setup.md in my folder (MY FOLDER fact). No fact, no file, or Daily account watch not under Routines on: stop silently.
2. Run @account-watch, all but the roster sheet.
3. One message with the ranking, expansion deals, drafts, and flags. A source failed: one line naming it. Nothing new: quiet. Drafts only.

Fires on:
- cron `56 8 * * 1-5`

Ask the importing user for:
- Timezone
