---
name: image-gen-bot--routine-weekly-pull-queue
description: "Routine: Every week, works through the stills and clips waiting in the pull queue and posts each finished file here for review."
version: 1.0.0
platforms: [linux, macos, windows]
metadata:
  hermes:
    tags: ["image-gen-bot", "grok-bot", "routine"]
    related_skills: ["image-gen-bot--getting-started", "image-gen-bot--look-and-size-sheet", "image-gen-bot--pull-a-still-from-footage", "image-gen-bot--pull-a-short-clip", "image-gen-bot--screenshot-cleanup-for-docs", "image-gen-bot--export-sizes-captions-and-alt-text"]
---
# Routine: Weekly pull queue

Original schedule: Every week, works through the stills and clips waiting in the pull queue and posts each finished file here for review.

Run once a week on the day and at the hour the user picked, in the timezone saved in memory. Compute the cron from that timezone and never assume Pacific or UTC. Read the look and size sheet first, then the pull queue, and pick up anything filed as a request in a connected tracker. For every open request, pull the frame or the range it names, finish it in the sizes that destination needs, write the alt text, and post the files here with one line each on what it is and where it came from, including the source recording and the timecode. Cap the run at five requests and say how many are still waiting. Update each request with the date and what you produced. An empty queue gets one line saying it is empty and nothing else. Never guess at a timecode a request does not give you, ask instead and leave it open. Never overwrite an original, never redo an asset the user already signed off on, and never post or publish anything anywhere.
