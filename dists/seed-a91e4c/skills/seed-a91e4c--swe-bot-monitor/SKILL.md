---
name: seed-a91e4c--swe-bot-monitor
description: "/swe-bot-monitor: Follow up on changes in production. Identify issues and proactively create fixes."
version: 1.0.0
platforms: [linux, macos, windows]
metadata:
  hermes:
    tags: ["seed-a91e4c", "grok-bot", "engineering"]
    related_skills: ["seed-a91e4c--swe-bot-onboard", "seed-a91e4c--swe-bot", "seed-a91e4c--swe-bot-triage", "seed-a91e4c--swe-bot-code", "seed-a91e4c--swe-bot-babysit", "seed-a91e4c--swe-bot-test"]
---
# swe-bot-monitor

---
name: swe-bot-monitor
description: >-
  /swe-bot-monitor: Follow up on changes in production. Identify issues and proactively create fixes.
---
# swe-bot-monitor

## Non-negotiables

- Use subscriptions, monitors, logs, alerts, and any other tools available to watch for issues in production.
- Ask the user for additional context or sources if the available ones are not sufficient or ambiguous.
- As issues are identified, triage them and delegate work to fix them.
- Serious production issues should be treated as high priority. Prefer to roll back or revert rather than fixing forward.
- Defer to the user for guidance on how to manage their production system. Take unambiguous actions, and ask for user confirmation before taking risks.
