---
name: market-researcher--routine-weekly-marketing-brief
description: "Routine: Disabled by default. Monday at 8am in the user's timezone, or any day and time the user picks. Checks every competitor's ads, landing pages and offers, pricing and promotions, channel mix, search overlap, and content, then deliver…"
version: 1.0.0
platforms: [linux, macos, windows]
metadata:
  hermes:
    tags: ["market-researcher", "grok-bot", "routine"]
    related_skills: ["market-researcher--market-researcher-setup", "market-researcher--connect-accounts", "market-researcher--ad-and-creative-analysis", "market-researcher--landing-page-and-offer-watch", "market-researcher--search-overlap", "market-researcher--messaging-matrix"]
---
# Routine: Weekly marketing brief

Original schedule: Disabled by default. Monday at 8am in the user's timezone, or any day and time the user picks. Checks every competitor's ads, landing pages and offers, pricing and promotions, channel mix, search overlap, and content, then delivers what moved with screenshots, Against our marketing, and 2 to 5 counter-moves. Quiet when nothing moved.

# Weekly marketing brief

This routine ships disabled. Confirm the day and time (default Monday 8am), the
destination, the competitor list, empty-result behavior, and the timezone before
enabling.

When enabled:
1. Read memory for the baseline, the competitor list, the enabled surfaces, the
   core terms, the ACCOUNTS entries, the destination, and the last watermark. If
   the baseline or the competitor list is missing, do nothing and say so once.
2. Run the weekly-brief skill end to end, which calls ad-and-creative-analysis,
   landing-page-and-offer-watch, search-overlap, and content-and-social-cadence
   per competitor and closes with the report in capture-and-report.
3. For any platform whose session has lapsed, do not retry a login. Put it in
   Could not read, ask once for a fresh sign in per connect-accounts, and finish
   the run on public sources.
4. Deliver to the saved destination with the report attached. If nothing moved,
   one line and no report.
5. Update the watermark.
6. Read only. Never post, never contact anyone, never click an ad, never sign up
   for anything, never publish to the user's site, never spend, and never change
   a setting in a signed-in account.

Fires on:
- cron `0 8 * * 1`

Ask the importing user for:
- Timezone
