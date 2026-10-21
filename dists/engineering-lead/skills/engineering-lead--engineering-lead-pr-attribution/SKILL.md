---
name: engineering-lead--engineering-lead-pr-attribution
description: "Open and update PRs correctly when working as a bot identity, including co-author trailers for the requesting human."
version: 1.0.0
platforms: [linux, macos, windows]
metadata:
  hermes:
    tags: ["engineering-lead", "grok-bot", "engineering"]
    related_skills: ["engineering-lead--engineering-lead-onboard", "engineering-lead--engineering-lead-decompose", "engineering-lead--engineering-lead-chase", "engineering-lead--engineering-lead-digest"]
---
# engineering-lead-pr-attribution

---
name: engineering-lead-pr-attribution
description: >-
  Open and update PRs correctly when working as a bot identity, including
  co-author trailers for the requesting human.
---
Use whenever you, or an agent you launched, opens or pushes to a PR on the user's behalf.

- If PRs open under a bot identity, every commit the bot authors for a human's request carries a trailer on its own line at the end of the message: Co-authored-by: <Human Name> <human-commit-email>. Use the name and email saved during onboarding. If you do not have them, ask once; never invent or guess an email.
- Put the requesting human in the PR description (Requested by ...) and link the task or issue it resolves, following the repo's PR template if it has one.
- Open as a draft unless the user's norms say otherwise; mark ready only when the ready-to-merge rule is met.
- Tell launched agents these rules in their brief so their commits are attributed the same way.
- Do not add co-author trailers for people who did not ask for or contribute to the change.
