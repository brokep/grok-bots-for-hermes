---
name: apple-search-ads-review--routine-weekly-ad-review
description: "Routine: Every week on the user's chosen morning, a read on last week's Apple Search Ads spend against target, with the changes worth making first."
version: 1.0.0
platforms: [linux, macos, windows]
metadata:
  hermes:
    tags: ["apple-search-ads-review", "grok-bot", "routine"]
    related_skills: ["apple-search-ads-review--getting-started", "apple-search-ads-review--set-spend-targets", "apple-search-ads-review--spend-review", "apple-search-ads-review--search-terms-and-negatives", "apple-search-ads-review--bids-and-budgets", "apple-search-ads-review--weekly-ad-review"]
---
# Routine: Weekly ad review

Original schedule: Every week on the user's chosen morning, a read on last week's Apple Search Ads spend against target, with the changes worth making first.

Run once a week on the morning and hour the user picked, in the timezone saved in memory. Compute the cron from that timezone and never assume Pacific or UTC. Read the targets sheet, every export saved since the last review, and the previous weekly review. When no new export has landed, send one short line naming the last date you have and what to drop in, then stop. With data, write the review in the shape from the Weekly ad review skill: the range and blended cost per install against target, the trend per campaign with cost per tap and conversion rate split out, the groups costing the most money above target with the money figure, where there is room to spend more, harvest and negative candidates, the bid changes worth making, what happened to last week's recommendations, and the three to five changes to make first. Every line carries a number from the export. Save the dated review and attach it, then deliver it to the destination they picked, and treat anything that posts or emails as a draft for them first. Never invent spend, taps, or installs, and never edit the ad account.
