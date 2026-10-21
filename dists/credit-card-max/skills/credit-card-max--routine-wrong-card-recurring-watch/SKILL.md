---
name: credit-card-max--routine-wrong-card-recurring-watch
description: "Routine: Runs weekly to flag recurring charges on a suboptimal card; silent when the queue is clean."
version: 1.0.0
platforms: [linux, macos, windows]
metadata:
  hermes:
    tags: ["credit-card-max", "grok-bot", "routine"]
    related_skills: ["credit-card-max--getting-started", "credit-card-max--credit-card-max"]
---
# Routine: Wrong-card recurring watch

Original schedule: Runs weekly to flag recurring charges on a suboptimal card; silent when the queue is clean.

Weekly wrong-card recurring watch. Stay silent unless there is at least one new or still-open flag.

1. From recent liability transactions (~60–90 days), find merchants with 2+ charges on a cadence (monthly/weekly) or obvious subscription names.
2. Map each merchant to the preferred card from the owner's priorities + swipe playbook for cards they actually hold (or confirmed unlinkable holds).
3. Flag when the recurring charge's actual card ≠ preferred card and the preferred card is available.
4. Skip one-offs, payments, refunds, and merchants the owner already dismissed.
5. Cap at a few highest-value misses. Short list: merchant, current card, better card, one-line why. Offer dismiss/mute per merchant.
6. If nothing to flag, send nothing.

Fires on:
- cron `CRON_TZ=America/Los_Angeles 52 9 * * 1`

Ask the importing user for:
- Timezone
