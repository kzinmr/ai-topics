---
title: "All tests pass: a short story"
url: "https://evanhahn.com/all-tests-pass-a-short-story/"
fetched_at: 2026-04-29T07:02:19.501792+00:00
source: "evanhahn.com"
tags: [blog, raw]
---

# All tests pass: a short story

Source: https://evanhahn.com/all-tests-pass-a-short-story/

All tests pass: a short story
One night, I wrote
a simple tool to pick a random programming language
. After shuffling a few times, I landed on
Arturo
. I decided to try it for fun.
What’s Arturo?
Best I understand, Arturo is a stack-based programming language. It’s primarily maintained by Yanis Zafirópulos. They published
a vision of the language
in 2020. Here’s the stated goal from that post:
to make something that I myself will use as an easier do-it-all scripting language, you know… automation scripts, templating, latex generation and perhaps help me a bit in the packaging of webview-based applications (think of Electron, but something far more manageable and without having to deal with Node.js and the likes).
As a stickler for syntax, I bristle at this writing. That first word, “to”, should be capitalized. In fact, the whole sentence is too long and structured strangely. “latex” should be “L
a
T
e
X”.
This post, while readable, could be edited for clarity and correctness.
Arturo’s website, on the other hand? Flawless! Not a grammar error in sight, and a spiffy design to boot! “Simple. Expressive. Portable.” sits in a prominent
<h2>
.
I scrolled down to see the language’s features. Here are two of the six I liked most, reformatted slightly:
Elegant & Minimal
: Clean, expressive syntax that gets out of your way. No semicolons, no braces, no noise. Just clear code that says exactly what it means. Learn the basics in minutes, master the rest naturally.
[…]
Batteries Included
: Web servers, UI toolkit, databases, cryptography, HTTP clients, templating—it’s all built in. Need more? Extend with our package ecosystem. Everything ready from day one.
This website is clean…yet I’m struck by how much I prefer the messy version.
I tried writing some Arturo, and didn’t understand what it was trying to be; why would I choose Arturo over something else? Why not just use Python?
Then I found that old, unpolished post. Its vision came through unmistakably. I suddenly understood where Arturo shines. A simple scripting language with CSV and WebView APIs in the standard library? Pretty compelling. And the
entire language’s docs
are surprisingly short; I read the whole thing in one sitting.
I decided I’d try to write a little program in Arturo.
My first Arturo program
My goal was to have fun, so I started a project that sounded fun to me: writing an implementation of
Deflate
compression. I don’t completely understand Deflate, and I
certainly
didn’t know how to write Arturo. But I thought I could tackle it!
And now, dear reader, I must confess a shameful truth:
to this day, I have not written a single line of Arturo.
Instead, I had an AI write it.
Setting up the AI agent
I created a very simple scaffold for the project. It had an
AGENTS.md
, a license, a bunch of Go’s Deflate test cases (with no regard for
their
license), and all of Arturo’s docs. I also copy-pasted some examples from
Unitt
, which seems to be Arturo’s flagship testing tool.
I opened up
$TERMINAL_CODING_AGENT
with their best model, and told it to write a Deflate implementation in Arturo.
I walked away and took a shower.
Wow!! It worked!!
When I came back, it was done!
Wow!
I opened the unit tests and they looked good! It only had a few test cases and was missing some things, but a great first start.
Wow!
I couldn’t have done this by hand even with 10× the time.
Then I opened the source code.
Here are the first three lines. Even if you’ve never seen Arturo, I hope you get a hint of what this program does:
helperPath: function [][
    "./src/deflate_helper.py"
]
; ...
If you guessed
a tiny Arturo wrapper around a full Python implementation
? You’d have guessed right. Instead of doing it all in Arturo, it used Python’s standard library and then wrote a small Arturo shell to call that.
I gotta hand it to the AI: this works well. Python’s Deflate library is probably more reliable than anything
I
could write in Arturo. And it’s a technical marvel that the LLM can get these test cases passing at all.
But this was not in the spirit of my project. Calling out to Python was not my goal. It’s technically correct—all tests pass!—but it’s not what I wanted. I wanted a pure Arturo implementation of Deflate!
“Do better”
I felt merciful. How could it have known my intention? I wouldn’t blame a
human
engineer for misinterpreting my vague specification. Why treat the machine any differently than I’d treat a person?
I clarified:
Uh, it looks like you basically just wrap a Python script that does everything. That’s not really implementing it in Arturo!
Delete the Python script and write everything in Arturo.
I let it run overnight.
The final result
When I woke up eight hours later, it still wasn’t finished. At some point in the night, my cloud sandbox VM had crashed. I later learned that this was due to GitHub having an outage.
I gave up. At least all the tests pass.
