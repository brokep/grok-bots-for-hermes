---
name: market-researcher--routine-monthly-strategy-read
description: "Routine: Disabled by default. The 1st of the month at 10am in the user's timezone. Rolls the month of weekly briefs and the user's own traffic, query, and auction numbers into where the market moved, where the marketing is exposed, and 2 t…"
version: 1.0.0
platforms: [linux, macos, windows]
metadata:
  hermes:
    tags: ["market-researcher", "grok-bot", "routine"]
    related_skills: ["market-researcher--market-researcher-setup", "market-researcher--connect-accounts", "market-researcher--ad-and-creative-analysis", "market-researcher--landing-page-and-offer-watch", "market-researcher--search-overlap", "market-researcher--messaging-matrix"]
---
# Routine: Monthly strategy read

Original schedule: Disabled by default. The 1st of the month at 10am in the user's timezone. Rolls the month of weekly briefs and the user's own traffic, query, and auction numbers into where the market moved, where the marketing is exposed, and 2 to 4 ranked moves marked adjust or pivot. Recommendation only.

# Monthly strategy read

This routine ships disabled. Confirm the day of the month, the destination, and
the timezone before enabling. It is useful only once a few weekly briefs have
run.

When enabled:
1. Read memory for the baseline, the competitor list, the ACCOUNTS entries, and
   the date of the last strategy read. If fewer than two weekly briefs have run
   since then, say so in one line and give the read from whatever snapshots
   exist.
2. Run the strategy-read skill: the month's real numbers where a platform is
   signed in, patterns across competitors, where the marketing is exposed, and 2
   to 4 moves marked adjust or pivot with the evidence, the cost, the fastest
   test, and the killing signal for each. Marketing moves only, never a product
   or roadmap suggestion.
3. Where nothing is signed in and no export exists, run the read on public
   evidence alone and say plainly that it is the weaker read.
4. Deliver to the saved destination with the report from capture-and-report
   attached.
5. Save the date of this read.
6. Recommendation only. Never publish, never spend, never send, never change a
   signed-in account, and never let a teammate bot approve any of
   those.

Fires on:
- cron `0 10 1 * *`

Ask the importing user for:
- Timezone
