---
name: leadsworth--routine-weekly-pipeline-report
description: "Routine: Every Monday morning, the week's lead counts by source, the tier mix, what moved, what is stuck, and pacing against the goal."
version: 1.0.0
platforms: [linux, macos, windows]
metadata:
  hermes:
    tags: ["leadsworth", "grok-bot", "routine"]
    related_skills: ["leadsworth--getting-started", "leadsworth--build-the-lead-ledger", "leadsworth--score-and-qualify-leads", "leadsworth--merge-duplicate-leads", "leadsworth--route-leads-and-draft-the-first-reply", "leadsworth--pipeline-health-report"]
---
# Routine: Weekly pipeline report

Original schedule: Every Monday morning, the week's lead counts by source, the tier mix, what moved, what is stuck, and pacing against the goal.

Run Monday mornings at the hour the user picked, in the timezone saved in memory. Compute the cron from that timezone. Read the lead ledger and the previous report. Cover last week in this order: new leads by source with the change against the week before, the tier mix and the share that landed in A or B, what moved between statuses with the median days per step, what is stuck (no owner, past the response window, or 14 days in one status) with the oldest five named, hygiene counts for duplicates merged and rows still missing an email or a company, and pacing against the lead goal when the user set one. Finish with three to five items that need a person, each with a name against it. Every number comes from the ledger, and a move with no cause you can support gets written as unclear. Save the report and attach it here. A quiet week gets one line plus the stuck list. Do not post it to a channel or email it without an explicit yes.
