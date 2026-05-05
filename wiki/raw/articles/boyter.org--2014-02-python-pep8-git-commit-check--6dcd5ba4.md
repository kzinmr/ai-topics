---
title: "Python pep8 git commit check"
url: "https://boyter.org/2014/02/python-pep8-git-commit-check/"
fetched_at: 2026-05-05T07:02:03.839985+00:00
source: "Ben Boyter"
tags: [blog, raw]
---

# Python pep8 git commit check

Source: https://boyter.org/2014/02/python-pep8-git-commit-check/

Python pep8 git commit check
2014/02/13
(105 words)
Without adding a git commit hook I wanted to be able to check if my Python code conformed to pep8 standards before committing anything. Since I found the command reasonably useful I thought I would post it here.
git status -s -u | grep '\.py$' | awk '{split($0,a," "); print a[2]}' | xargs pep8
Just run the above in your projects directory. It’s fairly simple but quite effective at ensuring your Python code becomes cleaner ever time you commit to the repository. The nice thing about it is that it only checks files you have modified, allowing you to slowly clean up existing code bases.
