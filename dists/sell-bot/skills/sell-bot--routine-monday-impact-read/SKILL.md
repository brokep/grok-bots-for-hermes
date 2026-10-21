---
name: sell-bot--routine-monday-impact-read
description: "Routine: Disabled by default. Mondays 9:20am: how accounts with calls moved against everyone else."
version: 1.0.0
platforms: [linux, macos, windows]
metadata:
  hermes:
    tags: ["sell-bot", "grok-bot", "routine"]
    related_skills: ["sell-bot--sell-setup", "sell-bot--accounts", "sell-bot--draft-email", "sell-bot--schedule", "sell-bot--watch-on-x", "sell-bot--prep-page"]
---
# Routine: Monday impact read

Original schedule: Disabled by default. Mondays 9:20am: how accounts with calls moved against everyone else.

This routine ships disabled. Before enabling, confirm the timezone, the spend or usage source, and which accounts count as the program.

When enabled:
1. Read memory and setup.md in my folder (MY FOLDER fact). No fact, no file, or Monday impact read not under Routines on: stop silently.
2. Run the Monday impact read in @follow-through.
3. One message: each group's median change and count, the gap, top movers, the caveat line, and what changed since last week. Reads only.

Fires on:
- cron `20 9 * * 1`

Ask the importing user for:
- Timezone
