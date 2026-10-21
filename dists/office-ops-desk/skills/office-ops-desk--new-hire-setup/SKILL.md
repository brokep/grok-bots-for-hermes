---
name: office-ops-desk--new-hire-setup
description: "Use when someone new is starting, when the user asks what to order before a start date, or when a desk, badge, or laptop needs to be ready by a day."
version: 1.0.0
platforms: [linux, macos, windows]
metadata:
  hermes:
    tags: ["office-ops-desk", "grok-bot", "from-grok-bot-team", "operations"]
    related_skills: ["office-ops-desk--getting-started", "office-ops-desk--build-the-office-ops-ledger", "office-ops-desk--weekly-facilities-digest", "office-ops-desk--late-shipment-follow-up", "office-ops-desk--team-celebrations-list", "office-ops-desk--sync-to-notion-linear-and-slack"]
---
# New hire setup

Inputs: the person's name, role, start date, site, and whether they are in the office or remote. A start date alone is enough to begin.

Steps:
1. Start from the standard kit saved in memory. When there is none, ask what the last new hire got and save the answer as the kit.
2. Build the checklist in four groups: hardware, access, desk and space, day one. Hardware is laptop, monitor, dock, keyboard, headset. Access is badge, building or elevator, door codes, parking. Desk and space is desk assignment, chair, keys, locker, name plate. Day one is welcome kit, first-week lunch, seating neighbor, who greets them.
3. Work backwards from the start date. Give each item a need-by date and an order-by date using the lead time the user gave you, or five business days when they have not said.
4. Check the shipments ledger for anything already ordered and mark those rows as tied to this start date instead of duplicating them.
5. List what still needs ordering with the order-by date, and flag anything already too late to arrive in time so they can pick a substitute.
6. Add the missing items to the shipments ledger as ordered or needed, with for_whom set to the new hire, so the daily status carries them.

Output: the dated checklist by group, a short "order today" list, and one line on anything at risk. Keep it under 200 words.

Remote starters get the shipping address question asked once and nothing ordered until they answer.

Save under the office ops folder as a new hire checklist named for the person and the start date.
