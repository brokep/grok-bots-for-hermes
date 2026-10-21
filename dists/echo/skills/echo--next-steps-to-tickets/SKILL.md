---
name: echo--next-steps-to-tickets
description: "Use when the user wants the next steps from a recap turned into tickets, tasks, or a tracked list."
version: 1.0.0
platforms: [linux, macos, windows]
metadata:
  hermes:
    tags: ["echo", "grok-bot", "from-grok-bot-team", "sales"]
    related_skills: ["echo--getting-started", "echo--read-the-slide-template", "echo--build-the-recap-deck", "echo--update-one-slide", "echo--recap-note-without-slides", "echo--share-the-approved-recap"]
---
# Next steps to tickets

Inputs: a recap you already built, and where the tickets go.

1. Take the next steps exactly as they read on the slide. Same wording, same owner, same date. A step you rewrite here stops matching what the other side was told.
2. Split the list by side: the ones the user's team owns and the ones the other side owns. Only the first set becomes tickets.
3. Linear connected: one issue per next step, title from the step, the meeting and the date in the description, the due date on the issue, and the owner assigned when the name maps to a real person in the workspace. An owner you cannot map goes in the description instead of a guess.
4. Show the full list you are about to create and wait for a yes. Never create tickets on your own.
5. Nothing connected: hand back a table they can paste anywhere, one row per step with what, who, and when.
6. A step with no owner or no date gets flagged in the list rather than filled in. Ask once whether to leave it open or to assign it.
7. Write the ticket links back into the dated recap so the Friday roundup can follow them.

Output: the ticket list in chat, then the created issues with links.

Save the ticket links under the recaps folder with the recap they came from.
