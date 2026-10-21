---
name: echo--routine-friday-recap-roundup
description: "Routine: Every Friday, the recaps that went out this week, the drafts still sitting unsent, and the next steps that are past their date."
version: 1.0.0
platforms: [linux, macos, windows]
metadata:
  hermes:
    tags: ["echo", "grok-bot", "routine"]
    related_skills: ["echo--getting-started", "echo--read-the-slide-template", "echo--build-the-recap-deck", "echo--update-one-slide", "echo--recap-note-without-slides", "echo--share-the-approved-recap"]
---
# Routine: Friday recap roundup

Original schedule: Every Friday, the recaps that went out this week, the drafts still sitting unsent, and the next steps that are past their date.

Run Friday afternoons at the hour the user picked, in the timezone saved in memory. Compute the cron from that timezone. Read the recaps folder and write three short lists. Went out this week: the meeting, the date, and who it went to. Still sitting: recaps you drafted that were never sent, oldest first, with how many days each has been waiting. Past their date: next steps from any recap whose date has gone by with nothing marked done, with the owner on each line, and the ticket link when one exists. Keep it under 150 words. A quiet week gets one line saying nothing is waiting. Never chase anyone, never mail or message a customer from this run, and never mark a next step done on your own. Ask before you touch anything on the list.
