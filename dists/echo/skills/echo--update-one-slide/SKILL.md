---
name: echo--update-one-slide
description: "Use when the user wants one slide changed: a correction, a commitment that landed after the meeting, or an update while the meeting is still running."
version: 1.0.0
platforms: [linux, macos, windows]
metadata:
  hermes:
    tags: ["echo", "grok-bot", "from-grok-bot-team", "sales"]
    related_skills: ["echo--getting-started", "echo--read-the-slide-template", "echo--build-the-recap-deck", "echo--recap-note-without-slides", "echo--share-the-approved-recap", "echo--next-steps-to-tickets"]
---
# Update one slide

Inputs: which slide, and what changed.

1. Change only the slide they named. Leave every other slide exactly as it is, including wording you would have written differently.
2. When the change comes from new notes, read those notes first and say which line you are acting on.
3. Updates mid-meeting are normal. When they say the meeting is still going, take the fragment they give you, update the slide, and stay quiet until they hand you more.
4. Show the old text and the new text next to each other in short form so they can see exactly what moved.
5. Keep the card inside the size the template profile allows. Something that no longer fits gets shortened rather than spilled onto a new slide, unless they ask for one.
6. Write the change into the dated recap so the next version starts from the corrected text.
7. A slide that already went out is a different situation. Say so, show the change, and ask whether they want a short correction note to go with it.

Fallbacks: a correction with no note behind it is still fine, take their word for it and mark that line as theirs. A request for a whole new slide gets one question first, since extra slides are the fastest way to make a recap read like a pitch.

Output: the rewritten slide text in chat and the updated deck file.

Save the updated recap under the recaps folder.
