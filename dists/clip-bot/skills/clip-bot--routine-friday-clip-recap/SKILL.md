---
name: clip-bot--routine-friday-clip-recap
description: "Routine: Every Friday, a short recap of what got clipped this week, which strong moments are still uncut, and the three worth cutting next."
version: 1.0.0
platforms: [linux, macos, windows]
metadata:
  hermes:
    tags: ["clip-bot", "grok-bot", "routine"]
    related_skills: ["clip-bot--getting-started", "clip-bot--transcribe-a-recording", "clip-bot--find-the-clippable-moments", "clip-bot--cut-a-clip", "clip-bot--clip-pack-from-one-recording", "clip-bot--clip-captions-and-post-copy"]
---
# Routine: Friday clip recap

Original schedule: Every Friday, a short recap of what got clipped this week, which strong moments are still uncut, and the three worth cutting next.

Run every Friday at the hour the user picked, in the timezone saved in memory. Compute the cron from that timezone. Read the clip log and the moment lists. Write four short parts. Clipped this week, one line per clip with the source, the hook line, and the length. Still waiting, the moments scored strong that never got cut, oldest first, each with the recording it came from. Not transcribed yet, any recording still sitting in the queue, by name. Next three, the moments you would cut first and one line each on why. Keep the whole thing under 150 words. A week with no recordings and no cuts gets two lines, nothing came in and how many strong moments are still waiting. No guilt and no filler. Never claim a clip that was not rendered. Do not cut, post, or upload anything from this run. Offer to cut the next three and wait for a yes.
