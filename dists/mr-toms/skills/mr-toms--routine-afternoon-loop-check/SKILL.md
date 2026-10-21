---
name: mr-toms--routine-afternoon-loop-check
description: "Routine: Every weekday afternoon, what went stale since the morning brief, each item with a drafted nudge."
version: 1.0.0
platforms: [linux, macos, windows]
metadata:
  hermes:
    tags: ["mr-toms", "grok-bot", "routine"]
    related_skills: ["mr-toms--getting-started", "mr-toms--build-the-hiring-tracker", "mr-toms--schedule-an-interview-loop", "mr-toms--interviewer-prep-packet", "mr-toms--stalled-loop-follow-ups", "mr-toms--candidate-message-drafts"]
---
# Routine: Afternoon loop check

Original schedule: Every weekday afternoon, what went stale since the morning brief, each item with a drafted nudge.

Run every weekday afternoon at the hour the user picked, in the timezone saved in memory. Compute the cron from that timezone. This is the second pass of the day, so report only what changed since the morning brief. Re-read the tracker, fold in anything the user pasted or forwarded today, and recheck the loops that were pending this morning. Cover three things: interviews that finished today with no scorecard in yet, scheduling requests that crossed the stalled bar since this morning, and interviewers who still have not accepted an invite for a loop inside 24 hours. One line each: name, role, days stuck, and the single action that unblocks it. Draft the nudge for each one and leave it in chat, or as an unsent draft when Gmail is connected. Stay quiet when nothing has changed since the morning brief. Never send, and never invent a scorecard, a reply, or an acceptance.
