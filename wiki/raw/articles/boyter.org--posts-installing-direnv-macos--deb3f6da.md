---
title: "Installing direnv on macOS"
url: "https://boyter.org/posts/installing-direnv-macos/"
fetched_at: 2026-05-05T07:01:55.310855+00:00
source: "Ben Boyter"
tags: [blog, raw]
---

# Installing direnv on macOS

Source: https://boyter.org/posts/installing-direnv-macos/

Having had to install direnv multiple times over the last few days to get a team up and running im writing the method down because I keep having to look it up.
Install based on the following instructions
https://github.com/direnv/direnv/blob/master/docs/installation.md
Then hook it up to your shell via
https://github.com/direnv/direnv/blob/master/docs/hook.md
Lastly to have it work with .env files create the following directory and file
~/.config/direnv/direnv.toml
and edit the contents to contain the following,
[
global
]
load_dotenv
=
true
You will need to restart your shell after doing this. Opening a new terminal is the easiest way to do this.
You need to allow the .env file when you enter the directory, which will be prompted, but for reference the following is the command.
Should do it for you.
