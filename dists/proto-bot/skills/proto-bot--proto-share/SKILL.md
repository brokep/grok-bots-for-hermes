---
name: proto-bot--proto-share
description: "Use to finish any job: the build or media packet, teammate handoffs, and a share draft that waits for a yes."
version: 1.0.0
platforms: [linux, macos, windows]
metadata:
  hermes:
    tags: ["proto-bot", "grok-bot", "from-grok-bot-team", "product"]
    related_skills: ["proto-bot--proto-setup", "proto-bot--proto-connect", "proto-bot--proto-codebase", "proto-bot--proto-build", "proto-bot--proto-figma", "proto-bot--proto-media"]
---
# proto-share

# proto-share

The packet every job ends with. Nothing leaves this chat without the user's yes for that exact post.

## Build packet

One SendToUser text message: draft PR and agent links, numbered click-path screenshots in the images field (up to 8, the rest in a proto.py sheet contact sheet), and 3 lines: what it does, how to try it, what is stubbed. Then demo.mp4 as its own attachment message, or proto.py slideshow <screens...> when there is no recording.

## Media packet

Images and gifs in the images field, video and other files as attachments (video under 15 MB via proto.py shrink, other files under 25 MB), then one line: model, short prompt, settings, cost.

## Teammates

teammates in proto.py status: auto sends, ask offers once per job with a widget, off skips, and no such teammate skips quietly. They share this computer, not my folder, and may reply from chats on other computers, so send links and text, never file paths.
- QA teammate: SendToAgent, priority true: "Prototype ready to test: <PR link>, preview <url>, click path <steps>." Show the user what it finds.
- Voice and writing teammate: ask for the share draft or UI copy with context and limits, and keep going. Use its words if they arrive, else write them myself.

## Share draft

Offer a 2 to 3 line post for Slack or X with the link or file. Post only after a yes for that text and place.

## Check before sending

No screenshot shows keys, tokens, real customer data, or a login.
