---
title: "Sloc Cloc and Code Badges for Github/Bitbucket/Gitlab"
url: "https://boyter.org/posts/sloc-cloc-code-badges/"
fetched_at: 2026-05-05T07:01:58.362203+00:00
source: "Ben Boyter"
tags: [blog, raw]
---

# Sloc Cloc and Code Badges for Github/Bitbucket/Gitlab

Source: https://boyter.org/posts/sloc-cloc-code-badges/

Sloc Cloc and Code Badges for Github/Bitbucket/Gitlab
2019/06/27
(303 words)
This is now part of a series of blog posts about
scc
Sloc Cloc and Code which has now been optimised to be the fastest code counter for almost every workload. Read more about it at the following links.
A very brief update in the world of
scc
. I noticed that tokei.rs which used to offer badges seemed to be having issues. Since I had wanted an excuse to hook up a AWS Lambda behind an ALB I thought I would add
scc
as a ‘service’ with badges.
You can view details on how to do so on the
scc
github page
https://github.com/boyter/scc/#badges-beta
In short though you can get the count of various metrics that
scc
is able to do for your public github/bitbucket/gitlab repositories. Add the markdown to your README.md file and away you go. It will probably break for very large repositories such as the linux kernel, but it does work with apache/hadoop and spark so it should be fine to a few million lines of code.
In the interests of showing things off here are some badges taken from the
scc
project itself.
Feel free to use these anywhere you like. It supports git only and there is no hidden catch beyond that I cache the results so that the lambda does not have to clone and reprocess everything each time it is invoked. The cache should be valid for 24 hours. If you need an additional source added please let me know via email or twitter.
