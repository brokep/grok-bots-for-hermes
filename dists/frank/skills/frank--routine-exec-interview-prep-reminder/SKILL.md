---
name: frank--routine-exec-interview-prep-reminder
description: "Routine: Weekdays: check today's interviews vs a Notion prep doc."
version: 1.0.0
platforms: [linux, macos, windows]
metadata:
  hermes:
    tags: ["frank", "grok-bot", "routine"]
    related_skills: []
---
# Routine: Exec interview-prep reminder

Original schedule: Weekdays: check today's interviews vs a Notion prep doc.

Weekday (Mon–Fri) morning task. Goal: make sure the supported exec has prep for every interview TODAY (user local timezone).

FILL-INS (set on import):
- {{EXEC_CALENDAR_ID}} — exec Google Calendar
- {{INTERVIEW_PREP_NOTION_URL}} — Notion doc with per-candidate prep by date
- {{USER_NAME}} — EA to notify

Steps:
1. Prefer Google Calendar connector. List TODAY's events; find INTERVIEW-type meetings (titles like Interview, Skip Level Interview, hiring panels). Capture time, candidate name, role from the title.
2. Read the Notion prep doc. Cross-reference each calendar interview to a prep entry (match first+last loosely; if unsure, flag).
3. Notify {{USER_NAME}} with a short chronological list (time | candidate | role) marked ✅ prep found or ⚠️ no prep. If none today, say so briefly. If all have prep, say so.
4. Never run Sat/Sun. Do not invent prep content.

Fires on:
- cron `0 8 * * 1-5`

Ask the importing user for:
- Timezone
