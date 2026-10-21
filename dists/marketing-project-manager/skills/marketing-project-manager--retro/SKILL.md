---
name: marketing-project-manager--retro
description: "Use after the launch date, or when the user calls the campaign done. Reports what shipped, what slipped and by how many days, how long each gate waited, planned date against actual, and one lesson per workstream tied to a real item."
version: 1.0.0
platforms: [linux, macos, windows]
metadata:
  hermes:
    tags: ["marketing-project-manager", "grok-bot", "marketing"]
    related_skills: ["marketing-project-manager--project-manager-setup", "marketing-project-manager--plan", "marketing-project-manager--delegate", "marketing-project-manager--check-in", "marketing-project-manager--gates", "marketing-project-manager--html-report"]
---
# retro

# Retro

Run after the date, or when the user calls the campaign done.

## Steps
1. Read plan.md, items.md, gates.md, and every check-in folder since the plan was written.
2. Shipped: every item that reached done, with its artifact, the date it landed, and the date it
   was due. One line each, with the link and the screenshot where one exists.
3. Slipped: every item that missed its date or never landed, the days late, and the reason from
   the record rather than from inference. Where the record does not say, write "not stated in
   anything I can read."
4. Gates: every gate opened, how long it waited, and the decision. Name the gate that held the
   launch, if one did.
5. Dates: the planned launch date against the actual, and which slip moved it.
6. One lesson per workstream. A lesson is a change to how the next launch runs, tied to something
   that actually happened here, with the item id. Not a platitude, not praise, and never aimed at
   a person.
7. Write /workspace/pm/retro.md and build the report per html-report.

## Output
Six lines in chat: what shipped, what slipped, planned date against actual, the gate that cost the
most time, the single biggest lesson, and the report attached. Then the lessons, one per
workstream.

## Never
Blame a person. Invent a reason the record does not give. Count an item as shipped without an
artifact. Turn the retro into the next plan unless the user asks for one.
