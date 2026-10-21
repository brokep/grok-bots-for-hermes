---
name: sell-bot--routine-morning-prep
description: "Routine: Disabled by default. Weekdays 7am: prep pages for today's watched calls."
version: 1.0.0
platforms: [linux, macos, windows]
metadata:
  hermes:
    tags: ["sell-bot", "grok-bot", "routine"]
    related_skills: ["sell-bot--sell-setup", "sell-bot--accounts", "sell-bot--draft-email", "sell-bot--schedule", "sell-bot--watch-on-x", "sell-bot--prep-page"]
---
# Routine: Morning prep

Original schedule: Disabled by default. Weekdays 7am: prep pages for today's watched calls.

This routine ships disabled. Before enabling, confirm the timezone and the calls to watch.

When enabled:
1. Read memory and setup.md in my folder (MY FOLDER fact). No fact, no file, or Morning prep not under Routines on: stop silently.
2. Find today's watched calls (a title pattern with an outside attendee, a known account's domain, or a call I booked), skipping canceled events and ignored domains. Add new ones to calls.csv. An unknown outside call gets one line asking whether to watch it.
3. Run @prep-page for calls with prep empty, and draft confirm notes now for calls the hourly check misses (before 7:55am or after 6:55pm).
4. One message: calls in time order, each with its 5 lines and page. No watched calls: quiet. Reads and drafts only.

Fires on:
- cron `0 7 * * 1-5`

Ask the importing user for:
- Timezone
