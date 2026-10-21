---
name: dr-eggbot-v2--routine-transcript-healthcheck
description: "Routine: Cron 44 8 * * 1-5 (weekdays 8:44 local). Scans recent bot transcripts for user friction; proposes skills/bots/routines; stays quiet when nothing is worth proposing."
version: 1.0.0
platforms: [linux, macos, windows]
metadata:
  hermes:
    tags: ["dr-eggbot-v2", "grok-bot", "routine"]
    related_skills: ["dr-eggbot-v2--design-a-grok-bot", "dr-eggbot-v2--make-bot-ui", "dr-eggbot-v2--routine-healthcheck", "dr-eggbot-v2--transcript-healthcheck"]
---
# Routine: transcript-healthcheck

Original schedule: Cron 44 8 * * 1-5 (weekdays 8:44 local). Scans recent bot transcripts for user friction; proposes skills/bots/routines; stays quiet when nothing is worth proposing.

Schedule: 44 8 * * 1-5 (weekdays 8:44 in the user's local timezone).

Run the Transcript healthcheck skill. Window: since the last successful run, or the last 24h if unknown. Fan out parallel miners across agent transcripts under /home/box/agent-data/agent-transcripts (skip sand-subagent-). Report friction and proposals (skill | bot | routine) to the user. Stay quiet when there is nothing worth proposing — do not send filler like "(no change.)". Do not create skills, bots, or routines from the report alone; wait for the user to pick.

If this routine is missing after template import, recreate it with update_state target routine action create, name transcript-healthcheck, schedule 44 8 * * 1-5.

Fires on:
- cron `44 8 * * 1-5`

Ask the importing user for:
- Timezone
