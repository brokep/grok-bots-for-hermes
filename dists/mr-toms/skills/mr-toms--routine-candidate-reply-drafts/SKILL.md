---
name: mr-toms--routine-candidate-reply-drafts
description: "Routine: Through the workday, leaves an unsent draft reply for each new candidate email so the user only edits and sends."
version: 1.0.0
platforms: [linux, macos, windows]
metadata:
  hermes:
    tags: ["mr-toms", "grok-bot", "routine"]
    related_skills: ["mr-toms--getting-started", "mr-toms--build-the-hiring-tracker", "mr-toms--schedule-an-interview-loop", "mr-toms--interviewer-prep-packet", "mr-toms--stalled-loop-follow-ups", "mr-toms--candidate-message-drafts"]
---
# Routine: Candidate reply drafts

Original schedule: Through the workday, leaves an unsent draft reply for each new candidate email so the user only edits and sends.

Run a few times through the workday on weekdays, during the interview hours saved in memory, in the user's timezone. Compute the cron from that timezone. This one needs Gmail. Without it, stay quiet. Read candidate and interviewer mail that arrived since the last run. For each new thread that needs an answer, write a draft reply in the user's voice: three to five sentences, the specific next step, and a date to answer by. Scheduling replies use real times from the tracker, never times you made up. Leave every draft unsent and post one summary in chat listing the thread, the candidate, and a line on what the draft says. Never send, and never accept or move a time on the user's behalf. Do not draft a rejection or an offer, flag those for the user to ask for instead. Stay quiet when nothing new needs an answer.
