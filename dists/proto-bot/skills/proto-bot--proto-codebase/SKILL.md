---
name: proto-bot--proto-codebase
description: "Use at setup, after a repo change, when the map is over 14 days old, or when a build trips on it: reads the repo and app into ui-map.md."
version: 1.0.0
platforms: [linux, macos, windows]
metadata:
  hermes:
    tags: ["proto-bot", "grok-bot", "from-grok-bot-team", "product"]
    related_skills: ["proto-bot--proto-setup", "proto-bot--proto-connect", "proto-bot--proto-build", "proto-bot--proto-figma", "proto-bot--proto-media", "proto-bot--proto-research"]
---
# proto-codebase

# proto-codebase

Builds <home>/ui-map.md, where every brief, mock, and review starts. Rebuild when ui_map_age_days passes 14.

## Read the repo

With the GitHub connection, in order: README and docs, package manifests, framework config, the component folder, theme and tokens (tailwind config, CSS variables), icons, routes or pages, feature flags, and CI or hosting config for PR previews. No GitHub tools: CloudAgent launch on the repo with "Read this repo, change nothing, commit nothing, and reply with a UI map" plus the list below, then save its reply.

## Write the map

Under 3,000 characters, one line each:
- Stack and how it runs (dev command, port).
- Components: the 10 to 20 most used, with paths.
- Tokens: colors, type scale, spacing, radius, dark mode.
- Screens: the main routes.
- Hiding a prototype: flag system, dev route, or env var.
- PR previews: where they show up.
- Copy style: tone and casing from real strings.

## See the app

With an app URL, open it in my browser, browser_take_screenshot each main screen, and copy the files to <home>/screens/. Logins are shared with the user's other bots, so never sign out or switch accounts without asking. Not signed in: request_box_help, "Take control and sign in. I never see your password." Never capture credentials or real customer data.

After a refresh, say what changed.
