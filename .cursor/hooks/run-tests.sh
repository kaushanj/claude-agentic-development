#!/usr/bin/env bash
echo "Hook ran at $(date)" >> /tmp/cursor-lab11-hook.log

set -euo pipefail

# Drain postToolUse JSON so unittest does not inherit hook stdin.
cat >/dev/null

exec python3 -m unittest test_pricing.py
