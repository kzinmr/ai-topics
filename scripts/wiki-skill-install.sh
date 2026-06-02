#!/bin/bash
# Promote the repo's ai-topics-wiki project skill (+ the `wiki` CLI) to a personal
# GLOBAL install, so any Claude Code session — in any project — can query the wiki.
#
# It symlinks (not copies) so the repo stays the single source of truth:
#   ~/.local/bin/wiki                    -> scripts/wiki
#   ~/.claude/skills/ai-topics-wiki      -> .claude/skills/ai-topics-wiki
#
# Usage:
#   scripts/wiki-skill-install.sh            # install (symlink both)
#   scripts/wiki-skill-install.sh uninstall  # remove the symlinks
#   scripts/wiki-skill-install.sh status     # show current state
set -euo pipefail

REPO_ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
CLI_SRC="$REPO_ROOT/scripts/wiki"
SKILL_SRC="$REPO_ROOT/.claude/skills/ai-topics-wiki"
BIN_DST="$HOME/.local/bin/wiki"
SKILL_DST="$HOME/.claude/skills/ai-topics-wiki"

link() { # src dst
  local src="$1" dst="$2"
  if [ -L "$dst" ] && [ "$(readlink "$dst")" = "$src" ]; then
    echo "  ok    $dst -> $src"; return
  fi
  if [ -e "$dst" ] && [ ! -L "$dst" ]; then
    echo "  SKIP  $dst exists and is not a symlink (remove it manually to proceed)"; return 1
  fi
  mkdir -p "$(dirname "$dst")"
  ln -sfn "$src" "$dst"
  echo "  link  $dst -> $src"
}

case "${1:-install}" in
  install)
    echo "Installing ai-topics-wiki globally (symlinks):"
    link "$CLI_SRC" "$BIN_DST"
    link "$SKILL_SRC" "$SKILL_DST"
    echo
    case ":$PATH:" in
      *":$HOME/.local/bin:"*) : ;;
      *) echo "NOTE: $HOME/.local/bin is not on PATH — add it so \`wiki\` resolves." ;;
    esac
    echo "Done. New Claude Code sessions will discover the 'ai-topics-wiki' skill."
    ;;
  uninstall)
    echo "Removing global symlinks (repo files untouched):"
    for d in "$BIN_DST" "$SKILL_DST"; do
      if [ -L "$d" ]; then rm "$d"; echo "  rm    $d"; else echo "  --    $d (not a symlink, skipped)"; fi
    done
    ;;
  status)
    echo "CLI   : $BIN_DST -> $(readlink "$BIN_DST" 2>/dev/null || echo '(not installed)')"
    echo "Skill : $SKILL_DST -> $(readlink "$SKILL_DST" 2>/dev/null || echo '(not installed)')"
    echo "wiki on PATH: $(command -v wiki || echo 'no')"
    ;;
  *)
    echo "usage: $0 {install|uninstall|status}" >&2; exit 2 ;;
esac
