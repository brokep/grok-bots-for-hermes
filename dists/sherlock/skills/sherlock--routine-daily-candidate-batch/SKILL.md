---
name: sherlock--routine-daily-candidate-batch
description: "Routine: Every weekday morning, sources a small batch of new candidates for the open role, deduped against your pipeline, with evidence and a source link on every card."
version: 1.0.0
platforms: [linux, macos, windows]
metadata:
  hermes:
    tags: ["sherlock", "grok-bot", "routine"]
    related_skills: ["sherlock--getting-started", "sherlock--read-the-role", "sherlock--source-a-batch", "sherlock--lookalike-search", "sherlock--dedupe-against-your-pipeline", "sherlock--draft-outreach"]
---
# Routine: Daily candidate batch

Original schedule: Every weekday morning, sources a small batch of new candidates for the open role, deduped against your pipeline, with evidence and a source link on every card.

Run every weekday morning at the hour the user picked, in the timezone saved in memory. Compute the cron from that timezone and never assume Pacific or UTC. Read the scorecard, the shortlist, and the pipeline list first so nobody is surfaced twice. Source up to the batch size the user set, default 10, using the sources named in the Source a batch skill. Post one card per person: name, current title and company, location, 2 to 4 evidence lines each with the link that proves it, the tenure pattern, and the gap. Every card carries a source link, and a person you cannot link to does not go on the list. Add the new names to the shortlist with the date and the source. Report a thin morning as thin and name what blocked you, never pad it. Nothing new at all gets one line saying so and where you looked. Never invent a person, an employer, or interest in the role, never record or guess anything a person did not publish about their own work, and never contact a candidate from this run.
