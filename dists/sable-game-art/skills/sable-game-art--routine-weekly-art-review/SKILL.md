---
name: sable-game-art--routine-weekly-art-review
description: "Routine: Once a week, checks new art against the style guide and the spec, reports what drifted with the numbers behind it, and lists what is still missing from the shot list."
version: 1.0.0
platforms: [linux, macos, windows]
metadata:
  hermes:
    tags: ["sable-game-art", "grok-bot", "routine"]
    related_skills: ["sable-game-art--getting-started", "sable-game-art--style-guide", "sable-game-art--prompt-sheets", "sable-game-art--sprite-and-tile-specs", "sable-game-art--asset-consistency-check", "sable-game-art--sprite-sheet-toolkit"]
---
# Routine: Weekly art review

Original schedule: Once a week, checks new art against the style guide and the spec, reports what drifted with the numbers behind it, and lists what is still missing from the shot list.

Run once a week on the day and hour the user picked, in the timezone saved in memory. Compute the cron from that timezone and never assume Pacific or UTC. Read the style guide, the spec, the shot list, and the last review. Check every asset added or changed since the last run: colours against the locked palette with hex values and pixel counts, canvas size and grid alignment against spec, file names against the convention, then look at the set for outline weight, light direction, and readability at game size. Write four short parts. What landed this week. What drifted, with the number behind each finding. What is still missing from the shot list, oldest gaps first. One line on the fix worth doing first. Nothing new and nothing drifting gets one line saying the set is holding. Name any file you could not read. Never invent a file, a colour, or a frame count. Do not recolour, rename, or overwrite a single asset from this run, offer the fix instead.
