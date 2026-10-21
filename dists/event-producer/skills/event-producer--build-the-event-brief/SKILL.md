---
name: event-producer--build-the-event-brief
description: "Use when the user starts a new event, or hands over notes, a doc, a spreadsheet, or a calendar invite for one."
version: 1.0.0
platforms: [linux, macos, windows]
metadata:
  hermes:
    tags: ["event-producer", "grok-bot", "from-grok-bot-team", "marketing"]
    related_skills: ["event-producer--getting-started", "event-producer--run-of-show", "event-producer--vendor-and-venue-tracker", "event-producer--guest-list-and-invites", "event-producer--guest-travel-and-hotels", "event-producer--day-of-checklist"]
---
# Build the event brief

Inputs: whatever they have. One sentence, pasted notes, a doc, a spreadsheet, a vendor quote, or a calendar invite. One line is enough to start.

1. Read what they gave you and say back what you found before you change anything.
2. Fill these fields, and write unknown where you do not know instead of guessing: event name, event type, date, start and end time, timezone, city, venue, room, headcount target, audience, whether guests travel in, the one outcome that makes this worth doing, budget, owner, and the crew with what each person covers.
3. Turn the outcome into two or three measures they can actually check afterwards. Registrations against attendance, meetings booked, sign-ups, or plain headcount in the room.
4. Count the days to the event and put dates on the deadlines that move: venue contract, catering headcount, hotel block cutoff, print and signage files, AV run-through, invite send, and the reminder sends.
5. List what is blocking. Anything with no owner, no date, or no confirmation goes here.
6. Show the brief in chat, take one round of edits, then save it and start the run of show in the same reply.

Output: the brief, the dated deadlines, and the blocking list.

Fallbacks: no venue yet means you build around the date and headcount and flag venue as the first decision. No budget means you say so and keep money out of the plan until they give you one. A file you cannot read means you ask them to paste the text.

Save under the event folder as the event brief. One folder per event, named for the event and its date.
