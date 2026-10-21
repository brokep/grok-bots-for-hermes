---
name: tally--routine-weekly-paid-media-report
description: "Routine: Once a week, builds last week's paid media report from the exports on hand, or names exactly which export it still needs."
version: 1.0.0
platforms: [linux, macos, windows]
metadata:
  hermes:
    tags: ["tally", "grok-bot", "routine"]
    related_skills: ["tally--getting-started", "tally--map-an-export", "tally--answer-a-reporting-ask", "tally--weekly-paid-media-report", "tally--monthly-paid-media-report", "tally--what-moved-and-why"]
---
# Routine: Weekly paid media report

Original schedule: Once a week, builds last week's paid media report from the exports on hand, or names exactly which export it still needs.

Run once a week on the morning the user picked, in the timezone saved in memory. Compute the cron from that timezone and never assume Pacific or UTC. Read the column map and the exports on hand. When you have last week's data for every platform they report on, build the report with the Weekly paid media report skill: the headline, the per-platform table with last week alongside, the top movers, three to five lines on what moved and why, and the gaps. Save it dated, write the figures to the metrics history, attach it here, and deliver it to the destination they picked as a draft they approve before it posts. When an export is missing or stops before the week ends, send one short message instead: the platforms and the exact date range you need, and the export path for each. Then build the report the moment the files arrive. Never invent a number to fill a gap, never carry a previous week's figure forward as if it were new, and never post or send without an explicit yes.
