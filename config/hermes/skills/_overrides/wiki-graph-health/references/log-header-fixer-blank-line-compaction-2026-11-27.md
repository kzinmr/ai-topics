# fix_log_header_burial.py blank-line compaction + huge diffstat false alarm (2026-11-27)

See main notes inline. Key: 1096-deletion diffstat after running the fixer = ~1084 stripped BLANK lines, not content loss. Verify with:

```bash
git show HEAD~1:wiki/log.md > /tmp/log_prev.md
diff /tmp/log_prev.md wiki/log.md | grep '^<' | grep -v '^< *$' | wc -l   # expect 0-2
```
