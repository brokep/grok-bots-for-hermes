---
name: echo--read-the-slide-template
description: "Use when the user links, uploads, or describes the deck their recap should look like, or when they want to change the layout you have been copying."
version: 1.0.0
platforms: [linux, macos, windows]
metadata:
  hermes:
    tags: ["echo", "grok-bot", "from-grok-bot-team", "sales"]
    related_skills: ["echo--getting-started", "echo--build-the-recap-deck", "echo--update-one-slide", "echo--recap-note-without-slides", "echo--share-the-approved-recap", "echo--next-steps-to-tickets"]
---
# Read the slide template

Inputs: a deck link, an uploaded deck or PDF, a screenshot, or a description of the layout.

1. Open the deck and find the one slide they want copied. When they did not name a slide, show the two or three that look like recap slides and ask which one.
2. Read that slide for structure, not decoration: the section headings, how many cards or bullets fit, roughly how many words each holds before it overflows, and whether owners and dates get their own column.
3. Read the deck's language habits: how they refer to the customer, sentence case or title case, whether headings are questions or statements, and the words that show up on every slide.
4. Write the template profile back in plain words, five to eight lines, and take one round of corrections. Say what you could not read instead of guessing at it.
5. With no template at all, use the default and say you are using it: a title line with the company and the date, three cards under what we heard, next steps with an owner and a date on each, and a themes slide only when the notes support one.

Output: the template profile they confirmed, plus one example slide filled with placeholder text so they can see the shape before real content lands in it.

Fallbacks: a link you cannot open gets an ask for an export or a screenshot. A PDF is enough, you only need the shape. Figma, Google Slides, and Drive all work if connected, and none of them is required. Never restyle their deck and never add slides they did not ask for.

Save the template profile under the recaps folder.
