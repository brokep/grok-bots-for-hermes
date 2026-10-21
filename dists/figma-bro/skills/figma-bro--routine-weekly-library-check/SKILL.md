---
name: figma-bro--routine-weekly-library-check
description: "Routine: Every Monday morning, checks the component library and token set for new duplicates, detached instances, and hardcoded values, and reports only what drifted since last week."
version: 1.0.0
platforms: [linux, macos, windows]
metadata:
  hermes:
    tags: ["figma-bro", "grok-bot", "routine"]
    related_skills: ["figma-bro--getting-started", "figma-bro--frame-to-build-spec", "figma-bro--build-a-screen-from-a-brief", "figma-bro--component-library-audit", "figma-bro--design-token-audit", "figma-bro--motion-and-prototype-notes"]
---
# Routine: Weekly library check

Original schedule: Every Monday morning, checks the component library and token set for new duplicates, detached instances, and hardcoded values, and reports only what drifted since last week.

Run every Monday at the hour the user picked, in the timezone saved in memory. Compute the cron from that timezone and never assume Pacific or UTC. Read the newest saved audit first, then read the library and the variables in the file they named. Report only what changed since that audit: new components, new duplicates or near-duplicate tokens, newly detached or drifted instances, new hardcoded values, and components that gained or lost variants. One line each, with the component or token name and the file it lives in. Close with a single counts line so the trend is visible: components, tokens, open issues, and the change against last week. Save the new audit so next week compares against it. A week with no drift gets one line saying the library held. When the file cannot be read, say which one in one line and stop, and do not repeat that more than once a week. Never rename, merge, delete, or publish anything, and never open an issue without an explicit yes.
