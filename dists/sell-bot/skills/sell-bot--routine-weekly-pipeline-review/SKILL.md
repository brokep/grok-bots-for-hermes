---
name: sell-bot--routine-weekly-pipeline-review
description: "Routine: Disabled by default. Mondays 9am: stalled deals, overdue touches, and nudges."
version: 1.0.0
platforms: [linux, macos, windows]
metadata:
  hermes:
    tags: ["sell-bot", "grok-bot", "routine"]
    related_skills: ["sell-bot--sell-setup", "sell-bot--accounts", "sell-bot--draft-email", "sell-bot--schedule", "sell-bot--watch-on-x", "sell-bot--prep-page"]
---
# Routine: Weekly pipeline review

Original schedule: Disabled by default. Mondays 9am: stalled deals, overdue touches, and nudges.

This routine ships disabled. Before enabling, confirm the timezone and the follow-up spacing.

When enabled:
1. Read memory and setup.md in my folder (MY FOLDER fact). No fact, no file, or Weekly pipeline review not under Routines on: stop silently.
2. From pipeline.csv: counts by stage, deals unmoved for 14 days, overdue next touches, proposals waiting over 5 days, open expansion deals, and prospects to propose as lost.
3. Draft a nudge per overdue prospect with something new and no open draft, per @draft-email. Check posts for the rest per @watch-on-x.
4. One message: the counts, stalled, overdue, and propose-lost lists, then the drafts. Nothing to report: quiet. Drafts only.

Fires on:
- cron `0 9 * * 1`

Ask the importing user for:
- Timezone
