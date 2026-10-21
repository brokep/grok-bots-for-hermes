---
name: seo-aeo-desk--routine-topic-watch
description: "Routine: Each weekday morning, speaks up only when a new question or topic worth a page shows up in the user's space."
version: 1.0.0
platforms: [linux, macos, windows]
metadata:
  hermes:
    tags: ["seo-aeo-desk", "grok-bot", "routine"]
    related_skills: ["seo-aeo-desk--getting-started", "seo-aeo-desk--keyword-and-question-research", "seo-aeo-desk--writer-content-brief", "seo-aeo-desk--weekly-search-report", "seo-aeo-desk--answer-engine-question-map", "seo-aeo-desk--page-audit-and-refresh-plan"]
---
# Routine: Topic watch

Original schedule: Each weekday morning, speaks up only when a new question or topic worth a page shows up in the user's space.

Run each weekday morning at the hour the user picked, in the timezone saved in memory. Compute the cron from that timezone. Read the ideas board and the question map first. Then check what is new in the user's space: fresh questions people are asking in their category, a competitor publishing on something the board does not cover, and a term picking up impressions in Search Console with no page behind it. Send nothing at all when there is nothing new. When there is, send one short message with the topic, the question it answers, where you saw it, and one line on whether it is worth a page this week. Cap it at two topics a day. Write anything worth keeping to the ideas board so the weekly digest does not report it twice. Never invent a trend, a source, or a number. Do not write the brief unless they ask for it.
