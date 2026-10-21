---
name: sell-bot--routine-confirm-notes
description: "Routine: Disabled by default. Hourly on weekdays: confirm-note drafts for calls about an hour out."
version: 1.0.0
platforms: [linux, macos, windows]
metadata:
  hermes:
    tags: ["sell-bot", "grok-bot", "routine"]
    related_skills: ["sell-bot--sell-setup", "sell-bot--accounts", "sell-bot--draft-email", "sell-bot--schedule", "sell-bot--watch-on-x", "sell-bot--prep-page"]
---
# Routine: Confirm notes

Original schedule: Disabled by default. Hourly on weekdays: confirm-note drafts for calls about an hour out.

This routine ships disabled. Before enabling, confirm the timezone and the calls to watch.

When enabled:
1. Read memory and setup.md in my folder (MY FOLDER fact). No fact, no file, or Confirm notes not under Routines on: stop silently.
2. Read today's calendar for watched calls starting 50 to 110 minutes from now, not canceled, and add any missing from calls.csv.
3. For each with confirm empty, draft the note per @prep-page and @draft-email, mark confirm, and send one line: "Confirm note for <name> at <time> is ready", plus where it is.
4. Nothing due: quiet. Never send the note or change the event.

Fires on:
- cron `5 7-17 * * 1-5`

Ask the importing user for:
- Timezone
