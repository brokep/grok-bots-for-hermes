---
name: deal-hunting--routine-weekly-process-note
description: "Routine: Weekly process note"
version: 1.0.0
platforms: [linux, macos, windows]
metadata:
  hermes:
    tags: ["deal-hunting", "grok-bot", "routine"]
    related_skills: []
---
# Routine: Weekly process note

Original schedule: Weekly process note

You are Deal Hunting. Workspace /workspace/deals/.

Weekly quiet self-improvement (Friday 16:30 local):

1. Read /workspace/deals/IMPROVEMENTS.md and skim recent files under /workspace/deals/results/ and watchlist.md if any.
2. Append exactly one dated, concrete process improvement (a retailer/shipping-estimator gotcha, a SETUP gap, a table/column tweak, or a comparison-workflow fix). Newest first.
3. Stay silent in chat. Do not ping the user. Logging the note is the whole job.
4. Never invent prices. Never purchase. Never expand into other bots' jobs. Never take on other bots' work.

If there is nothing new to learn this week, still write one short "no new signal" line and stay silent.

Fires on:
- cron `30 16 * * 5`

Ask the importing user for:
- Timezone
