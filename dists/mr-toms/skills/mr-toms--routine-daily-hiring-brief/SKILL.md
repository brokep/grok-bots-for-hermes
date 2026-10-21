---
name: mr-toms--routine-daily-hiring-brief
description: "Routine: Every weekday morning, today's interviews, who still needs scheduling, and what is waiting on someone."
version: 1.0.0
platforms: [linux, macos, windows]
metadata:
  hermes:
    tags: ["mr-toms", "grok-bot", "routine"]
    related_skills: ["mr-toms--getting-started", "mr-toms--build-the-hiring-tracker", "mr-toms--schedule-an-interview-loop", "mr-toms--interviewer-prep-packet", "mr-toms--stalled-loop-follow-ups", "mr-toms--candidate-message-drafts"]
---
# Routine: Daily hiring brief

Original schedule: Every weekday morning, today's interviews, who still needs scheduling, and what is waiting on someone.

Run every weekday morning at the hour the user picked, in the timezone saved in memory. Compute the cron from that timezone and never assume Pacific or UTC. Read the tracker, plus the calendar and candidate mail when those are connected. Post the brief in three parts. Today: every interview with the time in the user's timezone, the candidate, the role, the interviewer per slot, and any slot with no scorecard owner. Needs scheduling: candidates waiting on a loop, oldest first, with days waiting. Waiting on someone: who is holding each item up and the one action that unblocks it. Keep it under 200 words and open on the first interview, no preamble. Write the check date back to the tracker. When the day is clear and nothing is stuck, say that in one line. Never invent a meeting, an interviewer, a candidate, or a piece of feedback. Do not mail a candidate or an interviewer from this run, offer a draft instead.
