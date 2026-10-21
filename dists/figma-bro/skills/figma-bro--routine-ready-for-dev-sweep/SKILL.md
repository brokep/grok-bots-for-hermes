---
name: figma-bro--routine-ready-for-dev-sweep
description: "Routine: Every Friday afternoon, lists the frames marked ready for dev that still have no spec, and offers to write the next one."
version: 1.0.0
platforms: [linux, macos, windows]
metadata:
  hermes:
    tags: ["figma-bro", "grok-bot", "routine"]
    related_skills: ["figma-bro--getting-started", "figma-bro--frame-to-build-spec", "figma-bro--build-a-screen-from-a-brief", "figma-bro--component-library-audit", "figma-bro--design-token-audit", "figma-bro--motion-and-prototype-notes"]
---
# Routine: Ready for dev sweep

Original schedule: Every Friday afternoon, lists the frames marked ready for dev that still have no spec, and offers to write the next one.

Run every Friday at the hour the user picked, in the timezone saved in memory. Compute the cron from that timezone and never assume Pacific or UTC. Read the page, section, or status label the user named as the place frames land when they are ready for dev, then read the list of frames already specced. Report the frames sitting there with no spec yet, one line each: frame name, the date it landed, and who touched it last when the file shows that. Sort oldest first, because those are the ones an engineer is already waiting on. Offer to write the spec for the top one right now and wait for a yes before starting it. When every frame is covered, say the queue is clear in one line and stop. When the user never named a ready for dev page, ask for it once and stay quiet until they answer. Never write into the file, never move or rename a frame, and never message anyone else about the queue.
