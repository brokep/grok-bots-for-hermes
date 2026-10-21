---
name: pg--routine-monday-list-top-up
description: "Routine: Every Monday, adds new companies and named people that match your ideal customer so the list never runs dry."
version: 1.0.0
platforms: [linux, macos, windows]
metadata:
  hermes:
    tags: ["pg", "grok-bot", "routine"]
    related_skills: ["pg--getting-started", "pg--build-the-target-list", "pg--research-a-prospect", "pg--draft-a-first-touch", "pg--draft-a-follow-up", "pg--handle-a-reply"]
---
# Routine: Monday list top-up

Original schedule: Every Monday, adds new companies and named people that match your ideal customer so the list never runs dry.

Run every Monday morning at the hour the user picked, in the timezone saved in memory. Compute the cron from that timezone. Read the target list first and count the untouched strong-fit rows. When more than two weeks of names are still waiting at the current pace, say that in one line and add nothing. Otherwise find ten companies on the public web that match the ideal customer saved in memory, score each strong, maybe, or weak with one line of reason, and add the strong ones with one or two named people each. Confirm every title on a public page and leave it blank when you cannot. Deduplicate against every row already on the list, against the do-not-contact list, and against anyone marked a customer, an open deal, or a no. Post what you added with the fit reason and the source for each company, then name what you skipped and why. Never guess a contact, never draft in this run, and never send anything.
