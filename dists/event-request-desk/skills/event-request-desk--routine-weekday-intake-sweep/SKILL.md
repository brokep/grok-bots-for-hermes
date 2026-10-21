---
name: event-request-desk--routine-weekday-intake-sweep
description: "Routine: Every weekday morning, logs and scores every event ask that came in overnight and names the ones that need a decision today."
version: 1.0.0
platforms: [linux, macos, windows]
metadata:
  hermes:
    tags: ["event-request-desk", "grok-bot", "routine"]
    related_skills: ["event-request-desk--getting-started", "event-request-desk--log-a-new-event-request", "event-request-desk--score-an-event-request", "event-request-desk--tune-the-decision-rubric", "event-request-desk--draft-the-reply", "event-request-desk--track-what-you-owe-after-a-yes"]
---
# Routine: Weekday intake sweep

Original schedule: Every weekday morning, logs and scores every event ask that came in overnight and names the ones that need a decision today.

Run every weekday morning at the hour the user picked, in the timezone saved in memory. Compute the cron from that timezone and never assume Pacific or UTC. Read the queue, then check the intake sources the user set up: the Slack channel, the shared inbox, the form responses, or the tracker sheet. Log every ask that is not already in the queue, score each new one against the saved rubric, and write the rows back. Post one short message in three parts. New since the last sweep, one line per ask with organizer, type, the ask in six words, the event date, and the score. Needs your call today, anything scored and waiting whose reply-by date lands inside seven days. Chasing, anything sitting in needs info for more than three days. Stay quiet when nothing new came in and nothing is due. Say it when something is due even if nothing new arrived. Never invent a request, an organizer, a date, or a fee. Do not reply to an organizer, post in a channel, or send mail from this run. Offer a draft instead. When a source is unreachable, name it in one line and sweep the rest.
