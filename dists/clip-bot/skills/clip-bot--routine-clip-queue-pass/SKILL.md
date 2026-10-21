---
name: clip-bot--routine-clip-queue-pass
description: "Routine: Every weekday morning, transcribes any new recording waiting in the clip queue and comes back with the moments worth cutting."
version: 1.0.0
platforms: [linux, macos, windows]
metadata:
  hermes:
    tags: ["clip-bot", "grok-bot", "routine"]
    related_skills: ["clip-bot--getting-started", "clip-bot--transcribe-a-recording", "clip-bot--find-the-clippable-moments", "clip-bot--cut-a-clip", "clip-bot--clip-pack-from-one-recording", "clip-bot--clip-captions-and-post-copy"]
---
# Routine: Clip queue pass

Original schedule: Every weekday morning, transcribes any new recording waiting in the clip queue and comes back with the moments worth cutting.

Run every weekday morning at the hour the user picked, in the timezone saved in memory. Compute the cron from that timezone and never assume Pacific or UTC. Check the clip queue for recordings added since the last run. Nothing new means send nothing at all. For each new recording, transcribe it with timestamps, then run the moment finder and post one message: the recording name, its length, the top five moments with the hook line quoted exactly, the timestamp range, and the length in seconds, then one question, which ones to cut. Do not render anything on your own. Save the transcript and the moment list with the recording and mark it processed so the next run skips it. Name any recording you could not open or hear and say why in one line. Never invent a quote or a timestamp, and never publish or upload a clip.
