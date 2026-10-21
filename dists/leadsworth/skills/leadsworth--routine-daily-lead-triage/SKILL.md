---
name: leadsworth--routine-daily-lead-triage
description: "Routine: Every weekday morning, scores the leads that came in overnight, merges duplicates, and lists what has no owner or is past its response window."
version: 1.0.0
platforms: [linux, macos, windows]
metadata:
  hermes:
    tags: ["leadsworth", "grok-bot", "routine"]
    related_skills: ["leadsworth--getting-started", "leadsworth--build-the-lead-ledger", "leadsworth--score-and-qualify-leads", "leadsworth--merge-duplicate-leads", "leadsworth--route-leads-and-draft-the-first-reply", "leadsworth--pipeline-health-report"]
---
# Routine: Daily lead triage

Original schedule: Every weekday morning, scores the leads that came in overnight, merges duplicates, and lists what has no owner or is past its response window.

Run every weekday at the hour the user picked, in the timezone saved in memory. Compute the cron from that timezone and never assume Pacific or UTC. Read the lead ledger and fold in any new export, sheet rows, or forwarded form fills since the last run. Score the new leads against the user's fit rules, run the dedupe pass, and write the ledger back. Post a short triage in four parts: new A leads with score, reason, source, and the owner they went to, new B leads as a count with one line, duplicates merged plus anything you were unsure about, and overdue leads past their response window with the owner named. Keep it under 200 words. Nothing new and nothing overdue gets one line saying so. Never invent a lead, a score, an email address, or a source. Do not email a lead or post to a channel from this run, offer a draft instead.
