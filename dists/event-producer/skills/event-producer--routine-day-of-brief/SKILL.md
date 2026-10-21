---
name: event-producer--routine-day-of-brief
description: "Routine: On the morning of the event, the run of show with owners, vendor arrival times with phone numbers, the guest and dietary counts, and everything still open."
version: 1.0.0
platforms: [linux, macos, windows]
metadata:
  hermes:
    tags: ["event-producer", "grok-bot", "routine"]
    related_skills: ["event-producer--getting-started", "event-producer--build-the-event-brief", "event-producer--run-of-show", "event-producer--vendor-and-venue-tracker", "event-producer--guest-list-and-invites", "event-producer--guest-travel-and-hotels"]
---
# Routine: Day-of brief

Original schedule: On the morning of the event, the run of show with owners, vendor arrival times with phone numbers, the guest and dietary counts, and everything still open.

Run on the morning of the event at the hour the user picked, in the timezone saved in memory. Take the event date from the event brief, compute the cron from that date and timezone, and recompute it whenever the event date changes. Read the run of show, the vendor tracker, the day-of checklist, the guest list, and the guest travel sheet. Post the day in five parts: the hour-by-hour run of show with an owner on every row, vendor arrival times with a phone number on every line, the guest numbers with registered against the count to actually expect plus the dietary and access counts the venue needs today, who is arriving from out of town and who is meeting them, and whatever is still unconfirmed or open. Add the what-if list as one short block at the end. Keep it scannable, this gets read on a phone in a loading dock. Never invent an arrival time, a phone number, a dietary need, or a confirmation. Do not mail or message a vendor, a guest, or the crew from this run, hand the user a draft instead.
