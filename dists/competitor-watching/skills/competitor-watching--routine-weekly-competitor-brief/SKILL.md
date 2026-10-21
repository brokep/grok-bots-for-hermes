---
name: competitor-watching--routine-weekly-competitor-brief
description: "Routine: Every Monday morning, diffs the pages on the watch list against the last snapshot and delivers a brief of what changed with a source link on every line."
version: 1.0.0
platforms: [linux, macos, windows]
metadata:
  hermes:
    tags: ["competitor-watching", "grok-bot", "routine"]
    related_skills: ["competitor-watching--getting-started", "competitor-watching--build-the-watch-list", "competitor-watching--competitor-page-diff", "competitor-watching--weekly-competitor-brief", "competitor-watching--pricing-and-packaging-comparison"]
---
# Routine: Weekly competitor brief

Original schedule: Every Monday morning, diffs the pages on the watch list against the last snapshot and delivers a brief of what changed with a source link on every line.

Run every Monday at the hour the user picked, in the timezone saved in memory. Compute the cron from that timezone and never assume Pacific or UTC. Read the watch list and the most recent snapshot, then fetch every tracked page and compare it to the saved copy. Sort each difference into material or noise using the bar in the Competitor page diff skill, or the user's own bar when they set one. Write the brief in four parts. What changed, one block per competitor, every line ending in the source URL and the date. So what, two to four lines of plain implication for this user. Quiet this week, one line naming the competitors with nothing material. Sources, every URL you fetched. Fold in anything the daily launch check already logged instead of reporting it twice. Save the brief and the new snapshot, attach the brief, and deliver it to the destination they picked. A week with nothing material gets one line saying the week was quiet and no brief. Name any page you could not fetch and keep its old snapshot. Never invent a change, a price, or a date, and never post or email the brief without an explicit yes.
