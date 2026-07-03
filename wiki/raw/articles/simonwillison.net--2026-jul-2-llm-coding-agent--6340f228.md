---
title: "llm-coding-agent 0.1a0"
url: "https://simonwillison.net/2026/Jul/2/llm-coding-agent/#atom-everything"
fetched_at: 2026-07-03T07:00:57.302126+00:00
source: "simonwillison.net"
tags: [blog, raw]
---

# llm-coding-agent 0.1a0

Source: https://simonwillison.net/2026/Jul/2/llm-coding-agent/#atom-everything

Another Fable 5 experiment. Now that my
LLM library
has evolved into more of an agent framework it's time to see what a simple coding agent would look like built on it.
I started a
new Python library
using my
python-lib-template-repository
GitHub template repository, then ran these two prompts (here's the
Claude Code for web transcript
):
Write a spec.md for this project - it will depend on the latest “llm” alpha from PyPI and implement a Claude code style coding agent complete with tools for reading and editing files and executing commands
Then:
Commit the spec, then build it using red/green TDD in a series of sensible commits (each with passing tests and updated docs) - occasionally manually test it using the OpenAI API key in your environment
Here's
the spec
, the
resulting README file
, and the
sequence of commits
.
I've shipped a slop-alpha to PyPI, so you can run the new agent like this:
uvx --prerelease=allow --with llm-coding-agent llm code
It's pretty good for a first attempt! Here's the (Fable-authored)
README
, which lists recipes like
llm code --yolo
and
llm code --allow "pytest*" --allow "git diff*"
.
It also presents
a Python API
based around a
CodingAgent(model="gpt-5.5", root="/path", approve=True).run("Fix the failing test in tests/test_parser.py")
class which I didn't ask for but I'm delighted to see implemented.
Here's the suite of tools
it implemented
, listed using
uvx ... llm tools
:
CodingTools_edit_file(path: str, old_string: str, new_string: str, replace_all: bool = False) -> str
Replace an exact string in a file.
old_string must match the file contents exactly (including
whitespace) and must identify a unique location unless replace_all
is true. Returns a diff of the change so it can be verified.
CodingTools_execute_command(command: str, timeout: int = 120) -> str
Run a shell command in the session root directory.
Returns combined stdout and stderr followed by an Exit code line.
timeout is in seconds (maximum 600); on timeout the whole process
tree is killed.
CodingTools_list_files(pattern: str = '**/*', path: str = '.') -> str
List files matching a glob pattern, newest first.
Skips hidden directories, node_modules, __pycache__ and (in a git
repository) anything covered by .gitignore. Returns at most 200
paths relative to the searched directory.
CodingTools_read_file(path: str, offset: int = 0, limit: int = 2000) -> str
Read a text file, returning numbered lines like cat -n.
Paths are relative to the session root. Use offset (0-based first
line) and limit (max lines) to page through files too large to read
in one call.
CodingTools_search_files(pattern: str, path: str = '.', glob: str = None, max_results: int = 100) -> str
Search file contents for a regular expression.
Returns matches as path:line_number:line, capped at max_results.
Use glob (e.g. "*.py") to restrict which files are searched.
CodingTools_write_file(path: str, content: str) -> str
Create or overwrite a file with the given content.
Parent directories are created as needed. Prefer edit_file for
modifying existing files.
I tried it out by running
llm code --yolo
and then prompting:
mkdir /tmp/demo and then in that folder create a simple swiftui CLI app for telling the time in ascii art
Here's
the transcript
, in which GPT-5.5 reasoning notes that "SwiftUI isn't suitable for a true CLI" and then builds an app that outputs this on
swift run AsciiTime
:
█    █████         ████     █             █     ███   
     ██    █        █        █   ██      █     ██    █   █  
      █    ████           ███     █             █       █   
      █        █    █        █    █      █      █      █    
     ███   ████          ████    ███           ███   █████
