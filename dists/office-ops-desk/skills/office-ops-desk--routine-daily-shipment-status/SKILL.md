---
name: office-ops-desk--routine-daily-shipment-status
description: "Routine: Every weekday morning, a short status on what was delivered, what is late, and what has stopped moving."
version: 1.0.0
platforms: [linux, macos, windows]
metadata:
  hermes:
    tags: ["office-ops-desk", "grok-bot", "routine"]
    related_skills: ["office-ops-desk--getting-started", "office-ops-desk--build-the-office-ops-ledger", "office-ops-desk--weekly-facilities-digest", "office-ops-desk--late-shipment-follow-up", "office-ops-desk--team-celebrations-list", "office-ops-desk--new-hire-setup"]
---
# Routine: Daily shipment status

Original schedule: Every weekday morning, a short status on what was delivered, what is late, and what has stopped moving.

Run every weekday morning at the hour the user picked, in the timezone saved in memory. Compute the cron from that timezone and never assume Pacific or UTC. Read the shipments ledger plus any carrier mail or pasted update since the last run, and refresh tracking on anything still open. Post a status in three parts: delivered since the last run, late (past eta with no delivery, with days late and owner), and stalled (no tracking movement in three days). One line per shipment with item, vendor, carrier, tracking, and the date it is now expected. Call out separately anything tied to a start date or an event that will not arrive in time. Write the updated rows back to the ledger, including last_checked. Stay quiet when nothing changed and nothing is late. Say it when something is late, even if nothing else moved. Never invent a scan, a date, or a tracking number. Do not mail a carrier, vendor, or teammate from this run, offer a draft instead. When the ledger or the source is missing, say which one in one line and stop.
