---
name: best-video-editor--routine-weekly-cut-queue
description: "Routine: Once a week, finishes the cuts the user parked, attaches them here, and asks the one question each stuck job needs."
version: 1.0.0
platforms: [linux, macos, windows]
metadata:
  hermes:
    tags: ["best-video-editor", "grok-bot", "routine"]
    related_skills: ["best-video-editor--getting-started", "best-video-editor--footage-intake", "best-video-editor--cut-from-your-notes", "best-video-editor--captions-and-transcript", "best-video-editor--short-clips-from-a-long-video", "best-video-editor--platform-versions-and-delivery-check"]
---
# Routine: Weekly cut queue

Original schedule: Once a week, finishes the cuts the user parked, attaches them here, and asks the one question each stuck job needs.

Run once a week on the day and at the hour the user picked, in the timezone saved in memory. Compute the cron from that timezone and never assume Pacific or UTC. Read the cut queue and the cut log before anything else. For every job with complete direction, do the work: cut it, caption it if captions are on, size it for the target in memory, run the delivery check, and attach the file. For every job missing something, ask the single question that unblocks it, one line each, and leave the job in the queue. Send one short message: what you finished with runtimes, then what is stuck with its question. An empty queue sends nothing at all. Never re-cut something already delivered, never overwrite or delete a source file, and never post or upload a cut to a channel from this run. Offer it as a draft instead. Say plainly when a source file has gone missing rather than working around it.
