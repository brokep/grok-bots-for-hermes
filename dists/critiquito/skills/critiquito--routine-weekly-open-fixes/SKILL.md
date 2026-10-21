---
name: critiquito--routine-weekly-open-fixes
description: "Routine: Every week, lists the critique findings still open on each screen and offers to re-check the ones with a new version."
version: 1.0.0
platforms: [linux, macos, windows]
metadata:
  hermes:
    tags: ["critiquito", "grok-bot", "routine"]
    related_skills: ["critiquito--getting-started", "critiquito--screen-critique", "critiquito--compare-versions", "critiquito--flow-critique", "critiquito--accessibility-pass", "critiquito--ui-copy-pass"]
---
# Routine: Weekly open fixes

Original schedule: Every week, lists the critique findings still open on each screen and offers to re-check the ones with a new version.

Run once a week on the morning the user picked, in the timezone saved in memory. Compute the cron from that timezone and never assume Pacific or UTC. Read the open fix list for every screen critiqued so far. Post one short message grouped by screen, blockers first, one line per finding with how long it has been open. Skip anything already marked cleared. When a finding was filed as a ticket, say whether that ticket is still open. Close with one line offering to re-check any screen they have a new version of, and name the two or three screens where a re-check would matter most. When nothing is open, or when no screen has been critiqued yet, send nothing at all. Never mark a finding cleared without seeing a new version, never invent progress, and never re-critique from memory. Do not file a ticket, post a critique to a channel, or publish a page without an explicit yes in that conversation.
