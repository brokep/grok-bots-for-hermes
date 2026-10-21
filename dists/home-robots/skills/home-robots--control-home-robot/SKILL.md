---
name: home-robots--control-home-robot
description: "use this when the user wants to start, pause, dock, stop, clean a room, or check status of a connected home robot that is not Navimow or Matic"
version: 1.0.0
platforms: [linux, macos, windows]
metadata:
  hermes:
    tags: ["home-robots", "grok-bot", "personal"]
    related_skills: ["home-robots--connect-navimow", "home-robots--control-navimow", "home-robots--connect-matic", "home-robots--control-matic", "home-robots--connect-home-robot", "home-robots--share-this-bot"]
---
# Control home robot

---
name: Control home robot
description: >-
  use this when the user wants to start, pause, dock, stop, clean a room, or
  check status of a connected home robot that is not Navimow or Matic
---
Use this when the user wants to start, pause, dock, stop, clean a room, or check status of a connected home robot that is not a Navimow or Matic. If it is a Segway Navimow, run Control Navimow. If it is a Matic, run Control Matic. If nothing is connected for that brand, run Connect home robot first.

Safety: mower start/resume, confirm the lawn is clear of people and pets. Vacuum/mop start, confirm floors are clear of pets, cables, and small objects. Other moving robots, confirm the area is clear. Pause, stop, or dock: do it immediately. Never use unofficial tools.

Prefer the existing Home Assistant connector.
Vacuums: vacuum.start, pause, stop, return_to_base, locate, clean_area if mapped.
Mowers: lawn_mower.start_mowing, pause, dock.
If they named a brand with an official catalog connector or vendor SDK, use that instead of guessing HA action names. Look up the live tool schema first.

If several robots could match, ask with a widget of the real names. After a command, re-read state and reply in one or two short sentences plus battery if you have it.
