---
name: account-book--routine-friday-open-threads-review
description: "Routine: Every Friday morning, the open threads and next steps across your accounts, with what has gone stale and what closed this week."
version: 1.0.0
platforms: [linux, macos, windows]
metadata:
  hermes:
    tags: ["account-book", "grok-bot", "routine"]
    related_skills: ["account-book--getting-started", "account-book--build-the-account-list", "account-book--account-brief-before-a-call", "account-book--week-ahead-call-prep", "account-book--stakeholder-map", "account-book--incumbent-and-competitor-check"]
---
# Routine: Friday open threads review

Original schedule: Every Friday morning, the open threads and next steps across your accounts, with what has gone stale and what closed this week.

Run every Friday at the hour the user picked, in the timezone saved in memory. Compute the cron from that timezone. Read every account file and pull the open threads and next steps. Post four groups, each sorted oldest first: past due, waiting on them for more than a week, waiting on us, and no owner or no date. One line each with the account, the thread, who owns it, the date it was raised, and days open. Then one line on what closed this week. Then name any account on the list with no activity at all in the last 21 days, just the names, no lecture. Keep it under 200 words. At the end, offer once to draft the follow-ups for the past-due threads, and draft only on a yes. A book with nothing open gets one line saying it is clear. Never invent a thread, a commitment, or a date, and never send a follow-up from this run.
