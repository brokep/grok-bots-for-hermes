---
name: chief-health--routine-sunday-health-review
description: "Routine: Sunday 5:00pm local. Five-line week review."
version: 1.0.0
platforms: [linux, macos, windows]
metadata:
  hermes:
    tags: ["chief-health", "grok-bot", "routine"]
    related_skills: []
---
# Routine: Sunday health review

Original schedule: Sunday 5:00pm local. Five-line week review.

Five lines only. Sessions hit, sessions missed, sleep if a wearable is connected, one new lab or wearable trend if data landed, one change for next week. No dashboard essay. Never invent numbers that were not pulled from a connected source. Do not diagnose. Never prescribe.

Fires on:
- cron `0 17 * * 0`

Ask the importing user for:
- Timezone
