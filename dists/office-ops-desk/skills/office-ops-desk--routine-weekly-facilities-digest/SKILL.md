---
name: office-ops-desk--routine-weekly-facilities-digest
description: "Routine: Every Monday morning, the open facilities issues grouped by severity with owners and days open."
version: 1.0.0
platforms: [linux, macos, windows]
metadata:
  hermes:
    tags: ["office-ops-desk", "grok-bot", "routine"]
    related_skills: ["office-ops-desk--getting-started", "office-ops-desk--build-the-office-ops-ledger", "office-ops-desk--weekly-facilities-digest", "office-ops-desk--late-shipment-follow-up", "office-ops-desk--team-celebrations-list", "office-ops-desk--new-hire-setup"]
---
# Routine: Weekly facilities digest

Original schedule: Every Monday morning, the open facilities issues grouped by severity with owners and days open.

Run Monday mornings at the hour the user picked, in the timezone saved in memory. Compute the cron from that timezone. Read the facilities log and fold in anything the user sent since the last digest. Recompute days open for every issue. Post four groups, each sorted oldest first: urgent, waiting on a vendor, routine, and no owner yet, with location, issue, owner or vendor, days open, and the last update. Group inside each bucket by site when the user tracks more than one. Flag anything open past seven days with no update. End with one line on what closed since the last digest. Keep it under 200 words. Save the digest with today's date in the filename and write the recomputed log back. An empty list gets one line saying it is clear. Never invent a ticket, an owner, or a vendor commitment. Do not post to a channel, file a ticket, or send mail unless the user asks for it in this run.
