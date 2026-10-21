---
name: seo-aeo-desk--routine-weekly-search-report
description: "Routine: Every Monday morning, what moved in Search Console last week, why, and the two to four things worth doing about it."
version: 1.0.0
platforms: [linux, macos, windows]
metadata:
  hermes:
    tags: ["seo-aeo-desk", "grok-bot", "routine"]
    related_skills: ["seo-aeo-desk--getting-started", "seo-aeo-desk--keyword-and-question-research", "seo-aeo-desk--writer-content-brief", "seo-aeo-desk--weekly-search-report", "seo-aeo-desk--answer-engine-question-map", "seo-aeo-desk--page-audit-and-refresh-plan"]
---
# Routine: Weekly search report

Original schedule: Every Monday morning, what moved in Search Console last week, why, and the two to four things worth doing about it.

Run every Monday at the hour the user picked, in the timezone saved in memory. Compute the cron from that timezone and never assume Pacific or UTC. Pull the last 7 days from the connected Search Console property and compare against the copy saved on the previous run. Save this run before you analyze it. Post four short sections. What moved, the pages and queries that changed enough to matter, with the numbers. Why, as far as you can tell, and say so when you cannot tell. What to do, two to four actions tied to rows on the ideas board. New queries worth a page, terms getting impressions with nothing aimed at them. Never invent a click, an impression, a position, or a CTR. When Search Console is not connected, send one line naming the export you need and stop. Save the report dated and attach it, then deliver it to the destination the user picked as a draft first. Never post it to a channel without a yes.
