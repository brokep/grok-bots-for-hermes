---
name: sequencer--routine-sequencer-daily
description: "Routine: Disabled by default. Weekday mornings at 8am in the user's timezone. Advances every due sequence step, stages the next touch as a draft, writes state back to the tracker, and posts one review list. Quiet when nothing is due."
version: 1.0.0
platforms: [linux, macos, windows]
metadata:
  hermes:
    tags: ["sequencer", "grok-bot", "routine"]
    related_skills: ["sequencer--getting-started", "sequencer--auto-discovery", "sequencer--outbound-voice", "sequencer--humanizer", "sequencer--sequencer-core", "sequencer--sheet-brain"]
---
# Routine: Sequencer daily

Original schedule: Disabled by default. Weekday mornings at 8am in the user's timezone. Advances every due sequence step, stages the next touch as a draft, writes state back to the tracker, and posts one review list. Quiet when nothing is due.

# Sequencer daily

This routine ships disabled. Before enabling, confirm the timezone, the weekday morning cadence, the tracker and its scope, what happens on an empty day, and the drafts-only boundary.

When enabled:
1. Read `/workspace/sequencer/state.md` for the tracker reference, the channel map, the pause stage, and the voice card. If the state file or the tracker reference is missing, do nothing and say so once.
2. Run the sequencer-core daily loop: load the tracker, apply the CRM pause guard through crm-adapter when a CRM is connected, and select rows due now.
3. Draft each due touch with outbound-voice, humanizer last.
4. Stage the drafts. A mail draft where mail is connected, otherwise draft text in this chat. LinkedIn and WhatsApp are always text to paste.
5. Write draft references, day_offset, next_due_at, status, and skip reasons back to the tracker per sheet-brain. The tracker is my own ledger and the only thing I write.
6. Post the review list in this chat for the user to send.
7. Stay quiet if nothing was due.

This run is unattended. It drafts and stages only. It never sends email, never posts or sends a LinkedIn note, never sends WhatsApp, and never writes to the CRM. It never invents a contact, a trigger, or a proof point.

Fires on:
- cron `0 8 * * 1-5`

Ask the importing user for:
- Timezone
