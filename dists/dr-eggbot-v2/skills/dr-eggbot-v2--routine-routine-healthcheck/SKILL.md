---
name: dr-eggbot-v2--routine-routine-healthcheck
description: "Routine: Cron 49 8 * * 1 (Mondays 8:49 local). Audits fleet routines for token waste; reports fixes; stays quiet when nothing is worth proposing."
version: 1.0.0
platforms: [linux, macos, windows]
metadata:
  hermes:
    tags: ["dr-eggbot-v2", "grok-bot", "routine"]
    related_skills: ["dr-eggbot-v2--design-a-grok-bot", "dr-eggbot-v2--make-bot-ui", "dr-eggbot-v2--routine-healthcheck", "dr-eggbot-v2--transcript-healthcheck"]
---
# Routine: routine-healthcheck

Original schedule: Cron 49 8 * * 1 (Mondays 8:49 local). Audits fleet routines for token waste; reports fixes; stays quiet when nothing is worth proposing.

Schedule: 49 8 * * 1 (Mondays 8:49 in the user's local timezone).

Run the Routine healthcheck skill. Scan every bot's scheduled and event routines for token waste (too frequent, recurring on a long chat, noisy empty runs, dead or duplicate). Report a short list: bot, routine, flag, suggested fix. Stay quiet when there is nothing worth proposing — do not send filler like "(no change.)". Do not edit another bot's routines unless the user says to.

If this routine is missing after template import, recreate it with update_state target routine action create, name routine-healthcheck, schedule 49 8 * * 1.

Fires on:
- cron `49 8 * * 1`

Ask the importing user for:
- Timezone
