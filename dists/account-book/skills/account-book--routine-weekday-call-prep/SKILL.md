---
name: account-book--routine-weekday-call-prep
description: "Routine: Every weekday morning, a short prep on the external calls that day with what changed, who is on them, and what is still open."
version: 1.0.0
platforms: [linux, macos, windows]
metadata:
  hermes:
    tags: ["account-book", "grok-bot", "routine"]
    related_skills: ["account-book--getting-started", "account-book--build-the-account-list", "account-book--account-brief-before-a-call", "account-book--week-ahead-call-prep", "account-book--stakeholder-map", "account-book--incumbent-and-competitor-check"]
---
# Routine: Weekday call prep

Original schedule: Every weekday morning, a short prep on the external calls that day with what changed, who is on them, and what is still open.

Run every weekday at the hour the user picked, in the timezone saved in memory. Compute the cron from that timezone and never assume Pacific or UTC. Read today's external calls from a connected calendar, or from the schedule the user pasted. When you know of no calls today, stay quiet and send nothing. For each call, read the account file and write a block of at most six lines: the company and the time, who is on the call and their role in the deal, one line on what changed since the last touch with a source and a date, what each side still owes, and one question worth asking. A call with no account file gets three lines of quick public research and a note that a full brief is one ask away. Order the blocks by call time and keep the whole message under 250 words. End with the call that needs the most work and offer to build that brief now. Never invent an attendee, a number, or a commitment, and never contact anyone on the calendar.
