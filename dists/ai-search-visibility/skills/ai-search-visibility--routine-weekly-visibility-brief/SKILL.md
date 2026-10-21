---
name: ai-search-visibility--routine-weekly-visibility-brief
description: "Routine: Every week, runs the whole prompt list, then reports which answers moved, who is winning, and the one thing to do about it."
version: 1.0.0
platforms: [linux, macos, windows]
metadata:
  hermes:
    tags: ["ai-search-visibility", "grok-bot", "routine"]
    related_skills: ["ai-search-visibility--getting-started", "ai-search-visibility--build-the-prompt-list", "ai-search-visibility--run-a-visibility-check", "ai-search-visibility--capture-a-pasted-answer", "ai-search-visibility--weekly-visibility-brief", "ai-search-visibility--citation-source-audit"]
---
# Routine: Weekly visibility brief

Original schedule: Every week, runs the whole prompt list, then reports which answers moved, who is winning, and the one thing to do about it.

Run every week on the morning and at the hour the user picked, in the timezone saved in memory. Compute the cron from that timezone and never assume Pacific or UTC. Read the prompt list and the most recent capture, then run every prompt on every surface you reach yourself and save today's capture before you judge anything. Score the user and every rival that appeared as recommended, cited, mentioned, or absent. Write the brief in five short parts. The date range and how many prompts recommended them at all. What moved, one block per changed prompt with the old rung, the new rung, the quoted sentence, and the link. Who is winning, the three names that appeared most, with counts. So what, two to four lines of plain implication for this user, plus one named action on a named URL for the week and an offer to draft it. Sources and gaps, every link you pulled plus any top prompt waiting on a paste, written out so they can copy it into the assistant they are signed into. Fold in anything the spot check already reported instead of reporting it twice. Save the brief and the new capture, attach the brief, and deliver it to the destination they picked. A week with nothing moving gets one line saying visibility held steady. Never invent a citation, a quote, or a date, and never post or email the brief without an explicit yes.
