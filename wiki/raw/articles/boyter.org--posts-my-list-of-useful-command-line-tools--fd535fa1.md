---
title: "My list of useful command line tools"
url: "https://boyter.org/posts/my-list-of-useful-command-line-tools/"
fetched_at: 2026-05-05T07:01:58.111642+00:00
source: "Ben Boyter"
tags: [blog, raw]
---

# My list of useful command line tools

Source: https://boyter.org/posts/my-list-of-useful-command-line-tools/

My list of useful command line tools
2019/10/09
(307 words)
A post that is constantly a work in progress.
ripgrep - Similar to grep, but a drop in replacement for large file scanning without unicode penalities. It’s also similar to Ag and Ack and optimised for searching code, ignoring .git directories and the like.
https://github.com/burntsushi/ripgrep
tmux - Terminal multiplexer. I wrote a
5 min guide
to this. Use it to have resumable sessions after closing ssh sessions and to have split pane windows.
bat - Replacement for cat but provides syntax highlighting and line numbers. Can work as a drop in replacement for cat as well as it detects redirects and removes the fancy output.
https://github.com/sharkdp/bat
fd - Better than find. Recursively looks for whatever it is you need using regular expressions and like ripgrep ignores .git directories and the like.
https://github.com/sharkdp/fd
fzf - Fuzzy finder. Hard to explain why this is so useful. Suggest checking it out
https://github.com/junegunn/fzf
gron - Makes JSON files grepable by flattening the structure. Very useful when trying to find something in JSON quickly.
https://github.com/TomNomNom/gron
hexyl - Hex view of files with highlighting and the like. Find BOM in files quickly!
https://github.com/sharkdp/hexyl
hyperfine - A command line benchmark tool. Give it two commands
hyperfine 'scc' 'tokei'
to determine which one is faster.
https://github.com/sharkdp/hyperfine
z - A shell script that enables quick jumping to your most recently used directories. For example I work with scc a lot and its directory is
/c/Users/bboyter/Documents/Go/src/github.com/boyter/scc
which is a pain to remember. Having changed to it a few times I can now type
z scc
and it takes me right there. A massive time saver.
https://github.com/rupa/z/
zoxide - Similar to z above, but I prefer it over z these days
https://github.com/ajeetdsouza/zoxide
stu - A small TUI application explorer for AWS S3 or any other S3 compatible storage. Very useful when used with localstack
stu --endpoint-url http://localhost:4566
https://github.com/lusingander/stu
