---
name: import-bot--resync
description: "use this on a later visit: bring over only what changed in the old tools, and fold in a late export or sign-in"
version: 1.0.0
platforms: [linux, macos, windows]
metadata:
  hermes:
    tags: ["import-bot", "grok-bot", "from-grok-bot-team", "personal"]
    related_skills: ["import-bot--import-bot-setup", "import-bot--collect-local", "import-bot--collect-accounts", "import-bot--parse-import", "import-bot--transcript-toolkit", "import-bot--cleanup-fix"]
---
# resync

# Resync

People keep using the old tools for a while. A resync brings over only what is new since the last import, and it is also how a late export email or a finished sign-in gets folded in.

## Steps

1. Read the last import date and the "waiting on" list from the Import state fact, `/workspace/migration/state.md`, or `receipt.md`.
2. `mv /workspace/migration/inventory.json /workspace/migration/inventory.prev.json`.
3. If the user pasted an export link, download it on this computer's browser and extract into `raw/accounts/<service>/export/`. If a sign-in was pending, run that part of collect-accounts.
4. Run collect-local (two cards, say so) and parse-import.
5. Diff against `inventory.prev.json`, in this order, and list what is new: memory notes and memory entries changed or added, new projects and new notes inside existing projects, new or changed scheduled tasks, sessions and conversations created after the last import, new skills.
6. Route the new items: shared facts per write-user-memory (write, then show), unit updates to the owning expert as a short `SendToAgent` pointing at `pack/<slug>-update-<date>.md`, new units to the expert whose expertise fits, a new expert only when a new expertise appears with real evidence.
7. Receipt titled "Resync receipt, <date>", deltas only, same shape. Rewrite the Import state fact the way import-receipt does, with the new date. Delete raw and strip samples as usual.

If nothing changed: "Nothing new since <date>." and stop.
