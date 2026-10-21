---
name: mr-toms--routine-weekly-pipeline-review
description: "Routine: Every Friday afternoon, what moved per role, who is stuck and with whom, next week's interview load, and the calls that need the user."
version: 1.0.0
platforms: [linux, macos, windows]
metadata:
  hermes:
    tags: ["mr-toms", "grok-bot", "routine"]
    related_skills: ["mr-toms--getting-started", "mr-toms--build-the-hiring-tracker", "mr-toms--schedule-an-interview-loop", "mr-toms--interviewer-prep-packet", "mr-toms--stalled-loop-follow-ups", "mr-toms--candidate-message-drafts"]
---
# Routine: Weekly pipeline review

Original schedule: Every Friday afternoon, what moved per role, who is stuck and with whom, next week's interview load, and the calls that need the user.

Run every Friday afternoon at the hour the user picked, in the timezone saved in memory. Compute the cron from that timezone. Read the tracker and write a review per open role, shortest pipeline first. What moved: candidates who changed stage this week, plus offers out or closed. Stuck: candidates past the stalled bar, with days stuck and who is holding it up. Next week: the interview load by day, and any day that looks too heavy for the panel. Decisions needed: the calls only the user or a hiring manager can make, one line each. End with one line naming the roles with no movement at all. Keep it under 300 words. Save the review with the date and attach it. When nothing moved and nothing is stuck, keep it to two lines. Never invent a stage change, a scorecard, or a hiring manager commitment. Do not post it to a channel or mail it unless the user asks for it in this run.
