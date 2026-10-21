---
name: sell-bot--routine-daily-prospect-follow-up
description: "Routine: Disabled by default. Weekdays 9:40am: prospect replies, follow-ups, leads, and invites."
version: 1.0.0
platforms: [linux, macos, windows]
metadata:
  hermes:
    tags: ["sell-bot", "grok-bot", "routine"]
    related_skills: ["sell-bot--sell-setup", "sell-bot--accounts", "sell-bot--draft-email", "sell-bot--schedule", "sell-bot--watch-on-x", "sell-bot--prep-page"]
---
# Routine: Daily prospect follow-up

Original schedule: Disabled by default. Weekdays 9:40am: prospect replies, follow-ups, leads, and invites.

This routine ships disabled. Before enabling, confirm the timezone, the inbox, and the lead sources.

When enabled:
1. Read memory and setup.md in my folder (MY FOLDER fact). No fact, no file, or Daily prospect follow-up not under Routines on: stop silently.
2. Run the sent check in @draft-email. Draft replies to new email from accounts in open stages (since the email line under Last checks) per @draft-email, contract replies per @proposal-desk, and move stages on evidence per @accounts.
3. Read new rows from the lead sources, and attendee responses on booked events per @schedule.
4. Draft the follow-ups that are due and have something new, at most 3 per prospect, skipping any with an open draft.
5. Check posts from active prospects per @watch-on-x, then update Last checks.
6. One message: replies, drafts waiting, stage changes. Nothing new: quiet. Drafts only.

Fires on:
- cron `40 9 * * 1-5`

Ask the importing user for:
- Timezone
