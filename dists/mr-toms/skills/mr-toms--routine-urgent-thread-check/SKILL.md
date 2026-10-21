---
name: mr-toms--routine-urgent-thread-check
description: "Routine: Through the workday, flags a candidate or interviewer message that threatens a booked loop and drafts the reply."
version: 1.0.0
platforms: [linux, macos, windows]
metadata:
  hermes:
    tags: ["mr-toms", "grok-bot", "routine"]
    related_skills: ["mr-toms--getting-started", "mr-toms--build-the-hiring-tracker", "mr-toms--schedule-an-interview-loop", "mr-toms--interviewer-prep-packet", "mr-toms--stalled-loop-follow-ups", "mr-toms--candidate-message-drafts"]
---
# Routine: Urgent thread check

Original schedule: Through the workday, flags a candidate or interviewer message that threatens a booked loop and drafts the reply.

Run about every 45 minutes on weekdays during the interview hours saved in memory, in the user's timezone. Compute the cron from that timezone. This one needs Gmail or Slack. Without either, stay quiet and send nothing at all. Look only for messages that are time sensitive: a candidate declining or moving an interview, an interviewer dropping a slot for today or tomorrow, a candidate answering an offer, or a thread the user was asked to answer by a date that has now passed. Ignore everything routine, the morning brief covers that. When you find one, send a single short message: who it is, what they need, how long it has been sitting, and the booked loop or deadline it threatens. Attach a drafted reply. One message per thread, and never repeat a flag you already sent today. Never reply, book, cancel, or accept on the user's behalf.
