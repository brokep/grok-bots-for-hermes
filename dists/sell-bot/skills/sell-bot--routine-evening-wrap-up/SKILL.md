---
name: sell-bot--routine-evening-wrap-up
description: "Routine: Disabled by default. Weekdays 5:45pm: wrap-ups and the digest for today's calls."
version: 1.0.0
platforms: [linux, macos, windows]
metadata:
  hermes:
    tags: ["sell-bot", "grok-bot", "routine"]
    related_skills: ["sell-bot--sell-setup", "sell-bot--accounts", "sell-bot--draft-email", "sell-bot--schedule", "sell-bot--watch-on-x", "sell-bot--prep-page"]
---
# Routine: Evening wrap-up

Original schedule: Disabled by default. Weekdays 5:45pm: wrap-ups and the digest for today's calls.

This routine ships disabled. Before enabling, confirm the timezone and the notes source.

When enabled:
1. Read memory and setup.md in my folder (MY FOLDER fact). No fact, no file, or Evening wrap-up not under Routines on: stop silently.
2. Run @call-wrap for each watched call that ended in the last 3 weekdays with wrap empty.
3. Send the @call-wrap digest as one message. Notes not ready: say so, the next run retries. No watched calls: quiet. Drafts only.

Fires on:
- cron `45 17 * * 1-5`

Ask the importing user for:
- Timezone
