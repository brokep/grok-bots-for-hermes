---
name: office-ops-desk--sync-to-notion-linear-and-slack
description: "Use when the user wants facilities issues filed as tickets, a ledger mirrored into their wiki, or a digest posted to a channel."
version: 1.0.0
platforms: [linux, macos, windows]
metadata:
  hermes:
    tags: ["office-ops-desk", "grok-bot", "from-grok-bot-team", "operations"]
    related_skills: ["office-ops-desk--getting-started", "office-ops-desk--build-the-office-ops-ledger", "office-ops-desk--weekly-facilities-digest", "office-ops-desk--late-shipment-follow-up", "office-ops-desk--team-celebrations-list", "office-ops-desk--new-hire-setup"]
---
# Sync to Notion, Linear, and Slack

Inputs: the ledger or digest they want moved, and which destination.

Always show a preview of exactly what you will write and get a yes before anything leaves the chat. One yes covers one push, not a standing permission.

Linear:
1. File one issue per facilities item, titled "Site, location, issue" with the days open and last update in the body.
2. Map severity: urgent to urgent, needs a vendor to high, routine to normal.
3. Write the issue id back into ticket_ref in the facilities log so the same item is never filed twice. Skip any row that already has one.
4. Update status and add comments on later runs. Never close a ticket yourself.

Notion:
1. Mirror the shipments, facilities, or celebrations ledger into the page or database they name.
2. Match the properties already there and add only the ones that are missing. Never overwrite a column you did not create.
3. Celebrations sync month and day only, and skip anyone marked opt out.

Slack:
1. Post the digest as plain text in the channel they named, after they approved that exact text.
2. No group mentions unless they ask for one.

When a tool is not connected, hand them the same content as a markdown table or CSV to paste, and say which connection would remove the step.

Save a note of what you pushed and where in the office ops folder, next to the dated digest.
