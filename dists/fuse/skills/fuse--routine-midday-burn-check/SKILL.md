---
name: fuse--routine-midday-burn-check
description: "Routine: Every weekday around midday, catches a spend spike the same day it happens, but only when a live source is connected."
version: 1.0.0
platforms: [linux, macos, windows]
metadata:
  hermes:
    tags: ["fuse", "grok-bot", "routine"]
    related_skills: ["fuse--getting-started", "fuse--set-accounts-and-thresholds", "fuse--read-an-ad-platform-export", "fuse--pull-numbers-from-a-connected-source", "fuse--run-the-spend-and-performance-check", "fuse--diagnose-what-broke"]
---
# Routine: Midday burn check

Original schedule: Every weekday around midday, catches a spend spike the same day it happens, but only when a live source is connected.

Run every weekday at midday in the timezone saved in memory, and compute the cron from that timezone. This one is only worth having when a sheet, a warehouse query, or report mail is connected, so start by pulling from those. When nothing there is newer than this morning's check, stay quiet and do nothing. Do not ask for an export at midday, the morning check already did. When you do have fresh numbers, compare spend so far today against the daily plan for each account, and against each campaign's own trailing average for the same point in the day where history allows it. Post only urgent lines, three at most, each with the campaign, spend so far, the plan it is running against, and the one change to make. Skip watch and note, they keep until tomorrow morning. Never invent a number, never pause a campaign or move a budget, and never post anywhere the user did not pick.
