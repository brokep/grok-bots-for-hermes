---
name: stalk-bot--add-competitor
description: "Use when the user names a new competitor. Provisions an identity, creates the dossier, asks for modules, runs the first pass."
version: 1.0.0
platforms: [linux, macos, windows]
metadata:
  hermes:
    tags: ["stalk-bot", "grok-bot", "from-grok-bot-team", "product"]
    related_skills: ["stalk-bot--stalk-setup", "stalk-bot--modules", "stalk-bot--identity-ladder", "stalk-bot--profile-us", "stalk-bot--subscribe", "stalk-bot--walk-the-product"]
---
# add-competitor

# Add competitor

1. Ask for modules (same widget as setup) unless the user said "same as the others".
2. Provision the research identity via the identity ladder in memory.
3. Create /workspace/dossiers/<competitor>/ with index.md, subscriptions.md, snapshots/, and empty module files.
4. Run subscribe, snapshot-site, and watch-x once. Queue walk-the-product if the product module is on and offer to run it now.
5. Report the first-pass lines. Add the competitor to the pulse list.
