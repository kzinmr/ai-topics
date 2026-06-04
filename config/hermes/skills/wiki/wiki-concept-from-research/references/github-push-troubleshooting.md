# GitHub Push Troubleshooting for Wiki Pipelines

## Transient 500 Errors (`remote: Internal Server Error`)

GitHub occasionally returns HTTP 500 during `git push` for the ai-topics repo. This is a server-side transient issue — not credential, network, or repo corruption.

### Symptoms
```
remote: Internal Server Error
remote: Request ID <uuid>
To https://github.com/kzinmr/ai-topics.git
 ! [remote rejected]   main -> main (Internal Server Error)
```

### Diagnosis
Verify GitHub is reachable and the remote ref is correct:
```bash
git ls-remote origin HEAD    # Should return the HEAD commit hash
```

If `ls-remote` succeeds but push fails with 500, it's confirmed transient.

### Fix
Wait 10 seconds and retry:
```bash
sleep 10 && timeout 30 git push origin main
```

### Also: `fatal error in commit_refs`
This different error (`remote: fatal error in commit_refs`) can also be a GitHub transient, but more commonly it indicates a commit without actual page files — see `wiki-concept-from-research` references for the parallel subagent `git add wiki/` collision pattern.

When this error occurs:
1. `git show --stat <problem-commit>` — if only index.md + log.md, it's a thin commit
2. `git reset --soft origin/main` to squash thin commits
3. Re-verify all page files exist on disk
4. Single clean commit + push
