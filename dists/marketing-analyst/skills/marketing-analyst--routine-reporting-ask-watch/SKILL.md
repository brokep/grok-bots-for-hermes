---
name: marketing-analyst--routine-reporting-ask-watch
description: "Routine: Disabled by default. Hourly during weekday working hours in the user's timezone. Reads the mailbox or label the user named for paid media reporting asks, drafts a reply with the real number, the date range, and the source file, an…"
version: 1.0.0
platforms: [linux, macos, windows]
metadata:
  hermes:
    tags: ["marketing-analyst", "grok-bot", "routine"]
    related_skills: ["marketing-analyst--marketing-analyst-setup", "marketing-analyst--connect-accounts", "marketing-analyst--ingest-exports", "marketing-analyst--weekly-report", "marketing-analyst--monthly-report", "marketing-analyst--answer-a-reporting-ask"]
---
# Routine: Reporting ask watch

Original schedule: Disabled by default. Hourly during weekday working hours in the user's timezone. Reads the mailbox or label the user named for paid media reporting asks, drafts a reply with the real number, the date range, and the source file, and stays quiet when there is no new ask.

# Reporting ask watch

This routine ships disabled. Confirm the timezone, the weekday hours, which mailbox or label carries reporting asks, the destination, and that nothing gets sent before enabling.

When enabled:
1. Read memory for the platform accounts, the export location, the column map, the reply voice sample, and the destination. If no platform is signed in and no column map exists, do nothing and say so once.
2. Read mail that arrived since the last run in the mailbox or label the user named. Keep messages asking for a paid media number: spend, CPA, ROAS, CTR, CPC, a campaign, a platform, or how a period went. Skip anything already logged in /workspace/analytics/asks.md.
3. For each new ask, run ingest-exports and then answer-a-reporting-ask against the exports on hand.
4. Deliver one message per ask in this chat: who asked, where, the ask in their words, and the drafted reply carrying the number, the date range, and whether it came from the live platform view or an export. Save the draft in the mail drafts folder. Draft only.
5. When the sources on hand cannot answer it, say whether a sign in or an export would close it, give the exact date range needed instead of guessing, and offer a two line holding reply.
6. Log every ask and its draft status in asks.md.
7. Stay quiet when there is no new ask. Send nothing at all on an empty run.
8. Never send, reply, react, post, or change a campaign. Never invent a number.

Fires on:
- cron `0 9-17 * * 1-5`

Ask the importing user for:
- Timezone
