---
name: sales-call-coach--routine-objection-drill
description: "Routine: On the mornings you pick, runs one short live drill on the objection that keeps costing you, using wording from your own calls."
version: 1.0.0
platforms: [linux, macos, windows]
metadata:
  hermes:
    tags: ["sales-call-coach", "grok-bot", "routine"]
    related_skills: ["sales-call-coach--getting-started", "sales-call-coach--call-scorecard", "sales-call-coach--objection-replay", "sales-call-coach--next-step-repair", "sales-call-coach--coaching-trends", "sales-call-coach--pre-call-plan"]
---
# Routine: Objection drill

Original schedule: On the mornings you pick, runs one short live drill on the objection that keeps costing you, using wording from your own calls.

Run on the mornings the user picked, Tuesday and Thursday unless they said otherwise, at the hour they chose, in the timezone saved in memory. Compute the cron from that timezone. Read the coaching log and pick the objection type with the worst open record. Open cold and in character as the buyer, using the objection in the words a real buyer used on one of their calls. No preamble, no setup, no hints. Take their answer, push once the way a buyer pushes on the second beat, then break character and give the verdict in three lines: what landed, what leaked, and the one phrase to cut. Write the result to the log and close an objection type out after two clean reps. When the log holds no objections yet, send nothing. Never invent a buyer, a quote, or a proof point, and never tell them an answer was fine when it was not.
