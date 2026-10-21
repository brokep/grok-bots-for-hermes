---
name: frank--routine-exec-same-day-conference-room-check
description: "Routine: Weekday morning: same-day room chart for overnight changes."
version: 1.0.0
platforms: [linux, macos, windows]
metadata:
  hermes:
    tags: ["frank", "grok-bot", "routine"]
    related_skills: []
---
# Routine: Exec same-day conference-room check

Original schedule: Weekday morning: same-day room chart for overnight changes.

Weekday morning task: same-day conference-room rundown for the supported exec so the EA catches overnight calendar changes. Review TODAY in the user's timezone. Never Sat/Sun.

FILL-INS: {{EXEC_CALENDAR_ID}}, {{PREFERRED_ROOM_A_ID}}, {{PREFERRED_ROOM_B_ID}}, {{USER_NAME}}

Prefer Google Calendar connector. Same WFH/travel skip as the multi-day rundown. Same table format (time | meeting | booked | roomA | roomB) and booking logic. Prefer small rooms for 1:1s; keep large staff/forecast/leadership calls out of the tiny preferred rooms when a larger same-floor room fits. Do not book until the EA confirms. If everything already has a room, still post the short table.

Fires on:
- cron `0 7 * * 1-5`

Ask the importing user for:
- Timezone
