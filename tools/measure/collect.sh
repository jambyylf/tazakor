#!/usr/bin/env bash
S="$1"; SITE="$2"; NAME="$3"
CHROME="/c/Program Files/Google/Chrome/Application/chrome.exe"
LOG="$S/netlog/$NAME.json"
PROF=$(mktemp -d)
"$CHROME" --headless --disable-gpu --no-first-run --disable-extensions \
  --user-data-dir="$(cygpath -w "$PROF")" \
  --log-net-log="$(cygpath -w "$LOG")" \
  --virtual-time-budget=14000 --dump-dom "$SITE" >/dev/null 2>&1
if [ -f "$LOG" ]; then
  PYTHONIOENCODING=utf-8 python "$(cygpath -m "$S/hosts.py")" "$(cygpath -m "$LOG")" --json \
    > "$S/hosts/$NAME.json" 2>/dev/null
  rm -f "$LOG"
fi
rm -rf "$PROF"
