#!/usr/bin/env bash

echo "Hook ran at $(date)" >> /tmp/claude-lab11-hook.log

set -euo pipefail

# Drain PostToolUse JSON so unittest does not inherit hook stdin.
cat >/dev/null

cd "${CLAUDE_PROJECT_DIR:-.}"
exec python3 -m unittest test_pricing.py
