---
name: echo--routine-post-meeting-recap-draft
description: "Routine: After a meeting ends, drafts the recap from your notes and leaves it here for you to check."
version: 1.0.0
platforms: [linux, macos, windows]
metadata:
  hermes:
    tags: ["echo", "grok-bot", "routine"]
    related_skills: ["echo--getting-started", "echo--read-the-slide-template", "echo--build-the-recap-deck", "echo--update-one-slide", "echo--recap-note-without-slides", "echo--share-the-approved-recap"]
---
# Routine: Post-meeting recap draft

Original schedule: After a meeting ends, drafts the recap from your notes and leaves it here for you to check.

Run on the hour through the user's working day on weekdays, in the timezone saved in memory. Compute the cron from that timezone and never assume Pacific or UTC. Check the calendar for meetings that ended since the last run with someone outside the user's company on them. For each one, look for the notes in the source saved in memory. Notes that have not synced yet mean wait for the next run instead of writing anything. When the notes are there, build the recap with the Build the recap deck skill and the saved template profile, then send one short message: the meeting, the date, the slide text, and the deck attached. Add one line on what was thin in the notes. Nothing that ended, or nothing with notes, means send nothing at all. Never draft from a calendar title alone, never invent a quote or a commitment, and never send, share, or publish the recap to anyone.
