---
name: stalk-bot--feature-matrix
description: "Use on demand or in the pulse when enabled. Features by competitor from the dossiers, with cells changed since last pulse highlighted."
version: 1.0.0
platforms: [linux, macos, windows]
metadata:
  hermes:
    tags: ["stalk-bot", "grok-bot", "from-grok-bot-team", "product"]
    related_skills: ["stalk-bot--stalk-setup", "stalk-bot--modules", "stalk-bot--identity-ladder", "stalk-bot--profile-us", "stalk-bot--subscribe", "stalk-bot--walk-the-product"]
---
# feature-matrix

# Feature matrix

1. Collect the feature inventories from every competitor teardown and changelog, plus the baseline's features.
2. Normalize feature names across competitors (same capability, different marketing names) and keep a mapping note.
3. Build the table: rows are features, columns are us plus each competitor, cells are yes / no / partial / paid-tier / unknown, each with a date last verified.
4. Mark cells that changed since the last matrix.
5. Write to /workspace/dossiers/_matrix.md. Summarize changed cells in chat. (No spreadsheet plugin required; if the user wants a sheet later, export CSV from the dossier.)
