#!/usr/bin/env bash
# Install Grok marketplace bots as Hermes profiles (run from a clone of github.com/brokep/grok-bots-for-hermes).
#   ./install.sh human-copywriter prospector     # selected bots
#   ./install.sh --all                           # all of them (one profile each)
#   ./install.sh --remove human-copywriter       # delete the profile
#   ./install.sh --list                          # what is available
# Env: HERMES=hermes (binary), ALIAS=1 to also create `grok-<slug>` shell commands.
set -euo pipefail
HERE="$(cd "$(dirname "$0")" && pwd)"; HERMES="${HERMES:-hermes}"; ALIAS="${ALIAS:-1}"
flag=(); [ "$ALIAS" = "1" ] && flag=(--alias)
case "${1:-}" in
  --list) python3 -c "import json;[print(f\"{b['slug']:32} {b['name']:40} skills={b['skills']} routines={b['routines']}\") for b in json.load(open('$HERE/catalog.json'))]"; exit 0;;
  --all) set -- $(python3 -c "import json;print(' '.join(b['slug'] for b in json.load(open('$HERE/catalog.json'))))");;
  --remove) shift; for s in "$@"; do "$HERMES" profile delete "grok-$s" -y 2>/dev/null || "$HERMES" profile delete "grok-$s"; done; exit 0;;
  ""|-h|--help) sed -n '2,7p' "$0"; exit 0;;
esac
for s in "$@"; do
  [ -d "$HERE/dists/$s" ] || { echo "no such bot: $s"; continue; }
  "$HERMES" profile install "$HERE/dists/$s" -y ${flag[@]+"${flag[@]}"} --force
done
echo; echo "Done. Try:  hermes -p grok-$1 chat     (or just: grok-$1 chat)"
