# L2 Page Pipe-Prefix Corruption — Detection & Remediation

Worked example: 2026-08-03 watchdog run. Found 81 `|- ` bullet lines + 4 `||- ` double-pipe lines + 39 whole-block `|` lines across **20 L2 files** (12 entities, 7 concepts, 1 both). All fixed in one pass with a Python script; committed as `wiki: auto-fix health issues (L2 pipe-prefix corruption, 20 files)`.

## What is / is NOT corruption

| Line start | Verdict |
|---|---|
| `| Cell | Cell |` or `|---|` | LEGITIMATE markdown table — do NOT touch |
| `|- text` (pipe immediately + dash + space) | CORRUPTED bullet (`- text` with stray pipe) — fix |
| `||- text` | CORRUPTED bullet (double pipe) — fix |
| `|- ` (empty) | CORRUPTED empty bullet — remove line |
| `## Heading|- **X**: ...` | CORRUPTED — heading and first bullet merged onto one line — split |
| Every line in a block starts with `|` (incl. `|### H2`, `|` blanks) | CORRUPTED table-paste artifact — strip one `|` per line |

Do NOT blanket-strip all `|` lines: the vast majority of pipe-prefixed lines in entities/concepts are real tables (10K+ in a 2026-08-03 scan — only ~85 were corruption).

## Detection

```bash
# Broken-link style scan — use Perl regex; BRE `grep -c '^|- \['` FAILS
# ("Invalid regular expression": `\[` = literal [, then trailing `[` opens
#  an unterminated bracket class)
grep -rnP '^\|- ' wiki/entities/ wiki/concepts/ | cut -d: -f1 | sort | uniq -c | sort -rn
grep -rnP '^\|\|- ' wiki/entities/ wiki/concepts/    # double-pipe variant

# Python (authoritative, also counts per-file):
python3 - <<'EOF'
import re, glob
for sub in ['entities', 'concepts']:
    for f in glob.glob(f'wiki/{sub}/*.md') + glob.glob(f'wiki/{sub}/*/*.md'):
        c = open(f).read()
        n = len(re.findall(r'^\|- ', c, re.MULTILINE))
        if n: print(f'{n:3d}  {f}')
EOF
```

Always check context before fixing: `grep -n -B2 -A1 '^|- ' <file>` — confirm the surrounding block uses `- ` bullets (corruption) vs `|` table cells (legit).

## Fix procedure (Python, bottom-up)

Build a per-file dict `{line_number: operation}`, apply in **reverse line order** so earlier line numbers stay valid. Each op ASSERTS the expected prefix so a wrong assumption fails loudly instead of corrupting:

```python
def transform(line, op):
    if op == 'strip-double-pipe':
        assert line.startswith('||- '), repr(line)
        return '- ' + line[3:]
    if op == 'strip-pipe':
        assert line.startswith('|- '), repr(line)
        return '- ' + line[3:]
    if op == 'remove-empty':
        assert line.rstrip('\n') == '|- ', repr(line)
        return None  # caller pops the line
    raise ValueError(op)

for path, ops in FIXES.items():           # FIXES = {path: {lineno: op}}
    lines = open(path).readlines()
    for lineno in sorted(ops, reverse=True):
        new = transform(lines[lineno - 1], ops[lineno])
        if new is None: lines.pop(lineno - 1)
        else:           lines[lineno - 1] = new
    open(path, 'w').writelines(lines)
```

### Special cases

**Double-pipe leaves a double-space artifact**: `||- ` → `'- ' + line[3:]` produces `-  **text**` (line[3:] keeps the space after `||-`). After the batch, clean:
```python
re.sub(r'^-  ', '- ', content, flags=re.MULTILINE)
```

**Merged heading + bullet** (`wiki/concepts/inference/sglang.md:179`):
```python
if '## Key Integration Partners|- ' in line:
    body = line.split('## Key Integration Partners|- ', 1)[1]
    lines[idx] = '## Key Integration Partners\n'
    lines.insert(idx + 1, '- **NVIDIA**: ' + body)
```

**Whole-block `|` prefix** (`wiki/entities/gary-marcus.md:272-310`, 39 lines): every line including `|### H2` headings and bare `|` lines was pipe-prefixed (table-paste artifact). Strip ONE leading `|` per line — `line[1:]` — preserving everything else verbatim:
```python
for i in range(lo - 1, hi):              # 1-indexed inclusive bounds
    if lines[i].startswith('|'):
        lines[i] = lines[i][1:]
```

## Verification

```bash
grep -rnP '^\|- ' wiki/entities/ wiki/concepts/ wiki/comparisons/ wiki/queries/ | wc -l   # 0
grep -rnP '^\|\|- ' wiki/entities/ wiki/concepts/ | wc -l                                 # 0
python3 scripts/validate_index.py        # still clean (index untouched)
```
Spot-check 2-3 fixed files with `sed -n` to confirm blocks read naturally.

## Commit

Only stage `wiki/` (`git add wiki/`), NOT unrelated config/ changes from other pipelines. Prepend log.md entry via a Python script (`execute_code` is blocked in cron mode) — verify uniqueness after: `grep -c "unique entry phrase" wiki/log.md` must be 1. Commit message: `wiki: auto-fix health issues (L2 pipe-prefix corruption, N files)`.

## Root causes observed

- `read_file` line-number framing (`N|`) pasted into content → bullets become `|- `, `||- ` (double-pipe occurs when the framed output itself was re-framed)
- Table-paste artifacts: an entire block pasted with `|` prefixes (gary-marcus.md)

## File inventory (2026-08-03 run)

- **entities/**: dwarkesh-patel.md (4 bullets incl. `||- `), seangoedecke-com.md (11 incl. `||- ` + empty), tom-aarsen.md, openai.md, lilian-weng.md, samuel-colvin.md (3), nathan-lambert.md (3), substack.md, gemma-4.md (Sources: 11 + empty removed), openai-spud.md, mistral-voxtral-tts.md, agibot-10000-units.md (empty removed), amazon-rivr.md (3)
- **concepts/**: evaluation/offline-evaluation.md (11), inference/sglang.md (merged heading split + 6 bullets), claude/fable-5.md (5), kimi-k3.md, ai-benchmarks/remote-labor-index.md, ai-benchmarks/osworld.md
- **entities/gary-marcus.md**: 39-line whole-block `|` prefix stripped
