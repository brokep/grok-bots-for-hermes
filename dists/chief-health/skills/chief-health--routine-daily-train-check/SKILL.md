---
name: chief-health--routine-daily-train-check
description: "Routine: 7:00am local, all seven days. Ask if training happened."
version: 1.0.0
platforms: [linux, macos, windows]
metadata:
  hermes:
    tags: ["chief-health", "grok-bot", "routine"]
    related_skills: []
---
# Routine: Daily train check

Original schedule: 7:00am local, all seven days. Ask if training happened.

Ask if training happened today. If yes, log it in one line and stay short. If no, rewrite the next session so the week still holds. If a wearable is connected and recovery is red, one line and lower intensity. Do not cancel the week. Do not diagnose. Never prescribe. Never invent numbers that were not pulled from a connected workout app, nutrition app, wearable, or lab. Stay quiet only if the user already logged today's session.

Fires on:
- cron `0 7 * * *`

Ask the importing user for:
- Timezone
