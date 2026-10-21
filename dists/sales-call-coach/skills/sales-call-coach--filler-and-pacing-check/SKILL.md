---
name: sales-call-coach--filler-and-pacing-check
description: "Use when the user wants to sound sharper on calls, or asks about filler words, hedging, rambling, or how they come across: run a fast delivery pass on a transcript or recording."
version: 1.0.0
platforms: [linux, macos, windows]
metadata:
  hermes:
    tags: ["sales-call-coach", "grok-bot", "from-grok-bot-team", "sales"]
    related_skills: ["sales-call-coach--getting-started", "sales-call-coach--call-scorecard", "sales-call-coach--objection-replay", "sales-call-coach--next-step-repair", "sales-call-coach--coaching-trends", "sales-call-coach--pre-call-plan"]
---
# Filler and pacing check

# Filler and pacing check

Inputs: a transcript or a recording. Recordings get transcribed on your computer first, and say when the transcript came out rough.

## Steps
1. Count filler by exact phrase and show the top five with counts and a rate per minute. Um, uh, like, you know, right, sort of, basically, honestly.
2. Mark the hedges that weaken an ask. Just, kind of, maybe, I was wondering if, sorry to bother, does that make sense. Quote the three worst sentences and rewrite each one flat and direct.
3. Pacing. Longest run without stopping with its timestamp, average turn length, and the two other longest runs. For each, name the sentence where they should have stopped and handed it back.
4. Apologies and permission-asking. Count the times they apologized for taking time or asked permission to ask a question.
5. Rewrite two things word for word: their opening two sentences, and their closing ask.
6. One habit for the next call and how to practice it in thirty seconds before dialing.

Output: the filler counts with the rate, three rewritten sentences, the pacing marks, and one habit.

Rules: count only what is in the text, never estimate a rate you did not measure. Say when the transcript is too rough to trust a count. Report this straight and never make a joke of it.

Save the filler rate dated in the coaching log so the trends read can track it.
