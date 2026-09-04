# index.md Insertion Pitfalls

## Problem
The wiki `index.md` entities section is **NOT strictly alphabetical**. Entries are in approximate creation/insertion order. Some entries are duplicated across different positions (e.g., `isaac-flath` appears at lines 62 AND 365).

## Correct Approach
1. **Use grep to find insertion neighbors** — search for entries with the same prefix letter(s)
2. **Find the closest alphabetical neighbor** in the actual file order and insert after it
3. **Do NOT assume** `sed` or positional math will work — the order is irregular

## Example (2026-06-08)
```bash
# WRONG: assume alphabetical, insert at computed position
# RIGHT: grep for nearby entries
grep -n "entities/iii\|entities/ilya\|entities/ibm" wiki/index.md
# Then insert ido-pesok between iii-platform and ilya-sutskever
```

## Count Updates
After adding N new entity pages, update:
- `> Last updated:` line — date, Total pages +N, Indexed entries +N, Entities +N
- `## Entities (M pages)` header — M +N
