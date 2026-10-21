---
name: event-request-desk--routine-weekly-queue-review
description: "Routine: Every Monday morning, the whole event request queue grouped by what needs a decision, what is stale, and what is already committed."
version: 1.0.0
platforms: [linux, macos, windows]
metadata:
  hermes:
    tags: ["event-request-desk", "grok-bot", "routine"]
    related_skills: ["event-request-desk--getting-started", "event-request-desk--log-a-new-event-request", "event-request-desk--score-an-event-request", "event-request-desk--tune-the-decision-rubric", "event-request-desk--draft-the-reply", "event-request-desk--track-what-you-owe-after-a-yes"]
---
# Routine: Weekly queue review

Original schedule: Every Monday morning, the whole event request queue grouped by what needs a decision, what is stale, and what is already committed.

Run Monday mornings at the hour the user picked, in the timezone saved in memory. Compute the cron from that timezone. Read the whole queue and fold in anything logged since the last review. Recompute days waiting, days to the reply-by date, and days to the event date for every open request. Post five groups, each sorted by tightest reply-by date first: needs your call, needs info, decided but not replied, committed with an event date coming up, and closed since the last review. One line per request with organizer, type, the ask in six words, score, days waiting, and the reply-by date. Flag anything waiting more than five days with no movement, and any two committed events landing in the same week. End with two numbers, how many came in and how many closed this week, plus the current yes rate. Keep it under 200 words. Save the review with today's date and write the recomputed queue back. An empty queue gets one line saying it is clear and naming the next committed event. Never invent a request or a commitment, and do not reply to anyone from this run.
