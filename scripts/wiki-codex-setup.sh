#!/bin/bash
# Make the ai-topics wiki queryable from the Codex CLI.
#
# Two independent routes (use either or both):
#   cli  — the `wiki` CLI (Codex has shell access). Symlinks it onto PATH and adds
#          an always-on priming block to ~/.codex/AGENTS.md so Codex knows to use
#          it. Lightweight; recommended. Mirrors the Claude Code skill.
#   mcp  — registers the read-only Filesystem MCP via `codex mcp add` (Docker `ro`
#          mount). For `qmd` full-text/semantic search instead, pass `mcp --qmd`
#          (requires the qmd setup in docs/wiki-mcp-qmd.md).
#
# Usage:
#   scripts/wiki-codex-setup.sh cli            # CLI route (PATH + AGENTS.md priming)
#   scripts/wiki-codex-setup.sh mcp [--qmd]    # MCP route (codex mcp add)
#   scripts/wiki-codex-setup.sh status
#   scripts/wiki-codex-setup.sh remove         # undo both routes
set -euo pipefail

REPO_ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
CLI_SRC="$REPO_ROOT/scripts/wiki"
WIKI_DIR="$REPO_ROOT/wiki"
BIN_DST="$HOME/.local/bin/wiki"
AGENTS="${CODEX_AGENTS:-$HOME/.codex/AGENTS.md}"   # override for testing
BEGIN="<!-- BEGIN ai-topics-wiki (managed by scripts/wiki-codex-setup.sh) -->"
END="<!-- END ai-topics-wiki -->"
FS_NAME="ai-topics-wiki"
QMD_NAME="ai-topics-wiki-search"
IMAGE="mcp/filesystem"

read -r -d '' BLOCK <<EOF || true
$BEGIN
## ai-topics wiki (CLI)
A curated, read-only AI/ML knowledge base is queryable via the \`wiki\` command (English).
For questions about LLMs, AI agents, models, AI tooling/frameworks, or the AI ecosystem,
prefer it over web search:
- \`wiki search "<english query>" [--type concept] [--tag <tag>] [--curated]\` — full-text search
- \`wiki show <page>\` / \`wiki meta <page>\` / \`wiki links <page>\` — read & navigate
- \`wiki schema\` then \`wiki index\` to orient. Cite results as path:line. Never write to the wiki.
$END
EOF

upsert_agents() { # writes BLOCK into AGENTS between markers (idempotent)
  mkdir -p "$(dirname "$AGENTS")"; touch "$AGENTS"
  BEGIN="$BEGIN" END="$END" BLOCK="$BLOCK" AGENTS="$AGENTS" python3 - <<'PY'
import os, re
p, b, e, blk = os.environ["AGENTS"], os.environ["BEGIN"], os.environ["END"], os.environ["BLOCK"]
txt = open(p, encoding="utf-8").read() if os.path.getsize(p) else ""
pat = re.compile(re.escape(b) + r".*?" + re.escape(e), re.S)
if pat.search(txt):
    txt = pat.sub(blk, txt); action = "updated"
else:
    txt = (txt.rstrip() + "\n\n" if txt.strip() else "") + blk + "\n"; action = "added"
open(p, "w", encoding="utf-8").write(txt)
print(f"  AGENTS.md priming {action}: {p}")
PY
}

remove_agents() {
  [ -f "$AGENTS" ] || { echo "  AGENTS.md: $AGENTS (none)"; return; }
  BEGIN="$BEGIN" END="$END" AGENTS="$AGENTS" python3 - <<'PY'
import os, re
p, b, e = os.environ["AGENTS"], os.environ["BEGIN"], os.environ["END"]
txt = open(p, encoding="utf-8").read()
new = re.sub(r"\n*" + re.escape(b) + r".*?" + re.escape(e) + r"\n*", "\n", txt, flags=re.S).strip()
open(p, "w", encoding="utf-8").write(new + ("\n" if new else ""))
print("  AGENTS.md priming removed" if new != txt.strip() else "  AGENTS.md priming not present")
PY
}

check_cli() { # report only — CLI symlink ownership belongs to wiki-skill-install.sh
  if command -v wiki >/dev/null 2>&1; then
    echo "  wiki on PATH: $(command -v wiki)"
  else
    echo "  NOTE: \`wiki\` is not on PATH — run scripts/wiki-skill-install.sh install"
    echo "        (or: ln -s $CLI_SRC ~/.local/bin/wiki)"
  fi
}

case "${1:-status}" in
  cli)
    echo "Codex CLI route:"; check_cli; upsert_agents
    echo "Done. Codex will see the priming in $AGENTS."
    ;;
  mcp)
    if [ "${2:-}" = "--qmd" ]; then
      echo "Registering qmd MCP with Codex (needs docs/wiki-mcp-qmd.md setup):"
      codex mcp add "$QMD_NAME" -- qmd mcp
    else
      echo "Registering read-only Filesystem MCP with Codex:"
      codex mcp add "$FS_NAME" -- docker run -i --rm \
        --mount "type=bind,src=$WIKI_DIR,dst=/wiki,ro" "$IMAGE" /wiki
    fi
    codex mcp list 2>/dev/null | grep -iE "ai-topics" || true
    ;;
  status)
    echo "wiki on PATH : $(command -v wiki || echo no)"
    echo -n "AGENTS.md    : "; grep -q "ai-topics-wiki" "$AGENTS" 2>/dev/null && echo "priming present ($AGENTS)" || echo "no priming"
    echo "codex mcp    :"; codex mcp list 2>/dev/null | grep -iE "ai-topics|NAME" || echo "  (none matching ai-topics)"
    ;;
  remove)
    echo "Undoing Codex setup (repo files untouched):"
    remove_agents
    codex mcp remove "$FS_NAME" 2>/dev/null && echo "  codex mcp removed $FS_NAME" || true
    codex mcp remove "$QMD_NAME" 2>/dev/null && echo "  codex mcp removed $QMD_NAME" || true
    echo "  (left ~/.local/bin/wiki alone — managed by scripts/wiki-skill-install.sh)"
    ;;
  *)
    echo "usage: $0 {cli|mcp [--qmd]|status|remove}" >&2; exit 2 ;;
esac
