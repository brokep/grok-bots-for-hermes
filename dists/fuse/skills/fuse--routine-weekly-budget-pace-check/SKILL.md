---
name: fuse--routine-weekly-budget-pace-check
description: "Routine: Every Monday morning, where month-to-date ad spend lands against your plan and which accounts are going to overshoot."
version: 1.0.0
platforms: [linux, macos, windows]
metadata:
  hermes:
    tags: ["fuse", "grok-bot", "routine"]
    related_skills: ["fuse--getting-started", "fuse--set-accounts-and-thresholds", "fuse--read-an-ad-platform-export", "fuse--pull-numbers-from-a-connected-source", "fuse--run-the-spend-and-performance-check", "fuse--diagnose-what-broke"]
---
# Routine: Weekly budget pace check

Original schedule: Every Monday morning, where month-to-date ad spend lands against your plan and which accounts are going to overshoot.

Run Monday mornings at the hour the user picked, in the timezone saved in memory. Compute the cron from that timezone. Read the numbers ledger and the monthly plan behind every account. Per account, report month-to-date spend, the share of the plan it has used, days elapsed against days in the month, and where the month lands if the current daily rate holds. Flag any account projected to pass its plan, and give the daily rate it would take to land on plan instead. Add one line for any account underspending by more than 15%, since budget left on the table is a miss too. Finish with the total across accounts. Keep it under 150 words. When the ledger does not cover the current month, name the missing dates and ask for that export rather than projecting across a gap. Never invent spend and never move a budget, hand over the number they would have to set and wait for their yes.
