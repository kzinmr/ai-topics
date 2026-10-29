#!/usr/bin/env python3
"""Repair log.md header structure and prepend a new entry — ROTATED-HEADER variant.

Use this instead of repair_log_md_header.py when log.md has been ROTATED to
log-YYYY.md and the live header is no longer `# Wiki Log` + the italic
"_Log of all wiki changes. Newest entries at top._" line.

Post-rotation header shape (validated 2026-10-20, after the 2026-10-14 rotation):

    # Wiki Operation Log
    <blank>
    Previous entries are preserved in [[log-2026]]. Rotation on <date> preserved ...
    <blank>
    ## [newest entry]
    ...

repair_log_md_header.py hardcodes the OLD header + italic line, so on a rotated
log it prints "ERROR: no header found" and exits 1. This variant parameterizes
both the header token and the rotation-note prefix and applies the SAME
strip-everything-and-rebuild algorithm (strip EVERY header line and EVERY
rotation-note line wherever they sit, rebuild the head, prepend the entry,
append the rest).

Sibling-prepend burial signature that triggers this repair: a health-fix /
watchdog job prepends its own entry ABOVE the header block, so the file ends up
with TWO copies of the header+rotation-note pair at odd line numbers (observed
2026-10-20: headers at L28 and L332, rotation notes at L30 and L334). This
script dedups both pairs and re-anchors at L1.

Usage:
  python3 repair_log_md_oplog.py <path-to-log.md> <path-to-entry.md>
    - entry file is a standalone markdown block starting with '## [date] ...',
      written via write_file (Unicode-safe; keeps em-dashes/CJK out of the shell)
    - idempotent on a clean file; refuses to double-insert the same entry

Verify after running:
  grep -n "^# Wiki Operation Log" wiki/log.md   # exactly 1 line, at L1
  grep -n "Previous entries are preserved" wiki/log.md  # line 3
  git diff --stat wiki/log.md                   # ~ +N / -few, NOT a mass rewrite

DO NOT add a global re.sub(r'\n{3,}', '\n\n', whole_file) cleanup step — log.md
legitimately holds hundreds of blank lines and collapsing them corrupts every
entry's separation (see the NEVER-global-collapse pitfall in SKILL.md). A
healthy insert moves the blank-line count by only a handful.
"""
import sys

HDR = '# Wiki Operation Log'
ROT_START = 'Previous entries are preserved in [['  # matches [[log-2026]] etc.


def main():
    if len(sys.argv) != 3:
        print('usage: repair_log_md_oplog.py <log.md> <entry.md>', file=sys.stderr)
        sys.exit(2)
    path, entry_path = sys.argv[1], sys.argv[2]

    content = open(path, encoding='utf-8').read()
    entry = open(entry_path, encoding='utf-8').read().rstrip('\n')

    # Refuse a double-insert. Match by ASCII prefix of the entry heading, never
    # by a full title containing an em-dash (dash bytes can differ from typed).
    entry_head = entry.split('\n', 1)[0].strip()
    prefix = entry_head[:min(len(entry_head), 40)]
    if any(l.startswith(prefix) for l in content.split('\n')):
        print('entry already present (prefix %r) - refusing to double-insert' % prefix,
              file=sys.stderr)
        sys.exit(3)

    lines = content.split('\n')
    hdr_idxs = [i for i, l in enumerate(lines) if l.strip() == HDR]
    rot_idxs = [i for i, l in enumerate(lines) if l.strip().startswith(ROT_START)]
    print('header lines:', hdr_idxs, 'rotation lines:', rot_idxs, file=sys.stderr)
    if not hdr_idxs:
        print('ERROR: no "%s" header found - is the log rotated to a different '
              'header token? Adjust HDR.' % HDR, file=sys.stderr)
        sys.exit(1)
    if not rot_idxs:
        print('ERROR: no rotation note found - this file likely still uses the '
              'pre-rotation "# Wiki Log" + italic shape; use '
              'repair_log_md_header.py instead.', file=sys.stderr)
        sys.exit(1)

    rot_text = lines[rot_idxs[0]].strip()
    drop = set(hdr_idxs) | set(rot_idxs)
    body = [l for i, l in enumerate(lines) if i not in drop]
    while body and body[0].strip() == '':
        body.pop(0)

    new_lines = [HDR, '', rot_text, '', ''] + entry.split('\n') + [''] + body
    new_content = '\n'.join(new_lines)

    # Integrity checks (line-start matching, never substring counts).
    nb = new_content.split('\n')
    assert len([l for l in nb if l.strip() == HDR]) == 1, 'header count != 1'
    assert nb[0].strip() == HDR, 'header not at line 1'
    assert nb[2].strip().startswith(ROT_START), 'rotation note not at line 3'
    assert len([l for l in nb if l.startswith(prefix)]) == 1, 'entry duplicated'

    open(path, 'w', encoding='utf-8').write(new_content)
    print('WROTE %s  lines=%d  old_blanks=%d  new_blanks=%d'
          % (path, len(nb),
             sum(1 for l in lines if l.strip() == ''),
             sum(1 for l in nb if l.strip() == '')))


if __name__ == '__main__':
    main()
