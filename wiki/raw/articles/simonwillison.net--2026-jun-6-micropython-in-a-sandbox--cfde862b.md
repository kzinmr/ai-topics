---
title: "Running Python code in a sandbox with MicroPython and WASM"
url: "https://simonwillison.net/2026/Jun/6/micropython-in-a-sandbox/#atom-everything"
fetched_at: 2026-06-06T07:01:18.740841+00:00
source: "simonwillison.net"
tags: [blog, raw]
---

# Running Python code in a sandbox with MicroPython and WASM

Source: https://simonwillison.net/2026/Jun/6/micropython-in-a-sandbox/#atom-everything

Running Python code in a sandbox with MicroPython and WASM
6th June 2026
I’ve been experimenting with different approaches to running code in a sandbox for several years now, but my latest attempt feels like it might finally have all of the characteristics I’ve been looking for. I’ve released it as an alpha package called
micropython-wasm
, and I’m using it for a code execution sandbox plugin for
Datasette Agent
called
datasette-agent-micropython
.
Why do I want a sandbox?
My key open source projects—
Datasette
,
LLM
, even
sqlite-utils
—all support plugins.
I absolutely love plugins as a mechanism for extending software. A carefully designed plugin system reduces the risk involved in trying new things to almost nothing—even the wildest ideas won’t leave a lasting influence on the core application itself. My software can grow a new feature overnight and I don’t even have to review a pull request!
There’s one major drawback: my plugin systems all use Python and
Pluggy
, and plugin code executes with full privileges within my applications. A buggy or malicious plugin could break everything or leak private data.
I’d love to be able to run plugin-style code in an environment where it is unable to read unapproved files, connect to a network, or generally operate in a way that’s risky or harmful to the rest of the application or the user’s computer.
My interest covers more than just plugins. For Datasette in particular there are many features I’d like to support where arbitrary code execution would be useful. I’ve already experimented with this for
Datasette Enrichments
, where code can be used to transform values stored in a table. I’d love to build a mechanism where you can run code on a schedule that fetches JSON from an approved location, runs a tiny bit of code to reformat it into a list of dictionaries, then inserts those as rows in a SQLite database table.
What I want from a sandbox
My goal is to execute code safely within my own Python applications. Here’s what I need:
Dependencies that
cleanly install from PyPI
, including binary wheels across multiple platforms if necessary. I don’t want people using my software to have to take any extra steps beyond directly installing my Python package.
Executed code must be subject to both
memory
and
CPU
limits. I don’t want
while True: s += "longer string"
to crash my application or the user’s computer.
File access must be strictly controlled
. Either no filesystem access at all or I get to define exactly which files can be read and which files can be written to.
Network access is controlled as well
. Sandboxed code should not be able to communicate with anything without going through a layer I fully control.
Support for interaction with
host functions
. A sandbox isn’t much use if I can’t carefully expose selected platform features to the code that it’s running.
It has to be
robust, supported, and clearly documented
. I’ve lost count of the number of sandbox projects I’ve seen in repos with warnings that they aren’t actively maintained!
WebAssembly looks really promising here
Web browsers operate in the most hostile environment imaginable when it comes to malicious code. Their job is to download
and execute
untrusted code from the web on almost every page load.
Given this, JavaScript engines should be excellent candidates for sandboxes. Sadly those engines are also extremely complicated, and are not designed for easy embedding in other projects. Most of the v8-in-Python projects I’ve seen are infrequently maintained and come with warnings not to use them with completely untrusted code.
WebAssembly is a
much better
candidate. It was designed from the start to support all of the characteristics I care about and has been tested in browsers for nearly a decade. The
wasmtime
Python library is actively maintained and has binary wheels.
MicroPython in WebAssembly
WebAssembly engines like wasmtime run WebAssembly binaries. Some programming languages like Rust are easy to compile directly to WebAssembly. Dynamic languages like JavaScript and Python are harder—they support language primitives like
eval()
, which means they need a full interpreter available at runtime.
To run Python we need a full Python interpreter compiled to WebAssembly, wired up in a way that makes it easy to feed it code, hook up host functions and access the results.
Pyodide offers an outstanding package for running Python using WebAssembly in the browser, but using Pyodide in server-side Python isn’t supported. The most recent advice I could find was
from October 2024
stating “Pyodide is built by the Emscripten toolchain and can only run in a browser or Node.js”.
The other day I decided to take a look at
MicroPython
as an option for this. The MicroPython site says:
MicroPython is a lean and efficient implementation of the Python 3 programming language that includes a small subset of the Python standard library and is optimised to run on microcontrollers and in constrained environments.
WebAssembly sure feels like a constrained environment to me!
Building the first version
I had GPT-5.5 Pro
do some research for me
, which turned up
this PR against MicroPython
by
Yamamoto Takahashi
titled “Experimental WASI support for ports/unix”.
It then produced this
research.md document
, so I let Codex Desktop and GPT-5.5 high
loose on it
to see what would happen:
read the research.md document and build this. You will probably need to write a script that compiles a custom WASM version of MicroPython as part of this project - fetch the MicroPython code to a /tmp directory for this as part of that script.
It worked. I now had a prototype Python library that could execute Python code inside a WebAssembly sandbox!
The trickiest piece to solve was persistent interpreter state. The WASM build we are using here exposes a single entry point which starts the interpreter, runs the code and then stops the interpreter at the end.
This works fine for one-off scripts, but for Datasette Agent I want variables and functions to stay resident in memory so I can reuse them across multiple code execution calls.
A neat thing about working with coding agents is that you can get from an idea to a proof of concept quickly. I prompted:
For keeping variables resident: what if we ran code inside micropython itself which called a host function get_next_python_code() and then passed that to eval() - and that host function blocked until new code was available, maybe by running in a thread with a queue? Could that or a similar idea help here?
After some iteration we got to a version of this that works! In Python code you can now do this:
from
micropython_wasm
import
MicroPythonSession
with
MicroPythonSession
()
as
session
:
print
(
session
.
run
(
"x = 10
\n
print(x)"
).
stdout
)
print
(
session
.
run
(
"x += 5
\n
print(x)"
).
stdout
)
print
(
session
.
run
(
"print(x * 2)"
).
stdout
)
Under the hood this starts a thread, sets up a request queue and then sends messages to that queue for the
session.run()
command, each time waiting on a reply queue for the result of that execution. Inside WASM the MicroPython interpreter blocks waiting for a
__session_next__()
host function to return the next line of code, which it runs
eval()
on before calling
__session_result__({"id": request_id, "ok": True})
when each block has been successfully executed.
The other piece of complexity was supporting host functions, so my Python library could selectively expose functions that could then be called by code running in MicroPython.
Codex ended up solving this with
78 lines of C
, which ends up compiled into the
362KB WebAssembly blob
I’m distributing with the package.
I am by no means a C programmer, but I’ve read the C and had two different models explain it to me (here’s
Claude’s explanation
) and I’ve subjected it to a barrage of tests.
The great thing about working with WebAssembly is that if the C turns out to be fatally flawed the worst that can happen is the WebAssembly execution will fail with an exception. I can live with that risk.
Memory limits are directly supported by wasmtime. CPU limits are a little harder: wasmtime offers a “fuel” concept to limit how many operations a WebAssembly call can execute, and that’s the correct fit for this problem, but the units are hard to reason about. I’m experimenting with a 20 million default “fuel” setting now but I’m not confident that it’s the most appropriate value.
Try it yourself
The
micropython-wasm
alpha is now
live on PyPI
.
You can try it from your own Python code as
described in the README
. I’ve also added a simple CLI mode in
version 0.1a2
which means you can try it using
uvx
without first installing it like so:
uvx micropython-wasm -c
'
print("Hello world")
'
#
To see it run out of fuel:
uvx micropython-wasm -c
'
s = ""; while True: s += "longer"
'
#
Outputs: micropython-wasm: guest exited with code 1
You can also try it in
Datasette Agent
like this:
uvx llm keys
set
openai
#
Paste in an OpenAI key, then:
uvx --with datasette-agent \
  --with datasette-agent-micropython \
  --prerelease allow \
  datasette --internal internal.db \
    -s plugins.datasette-llm.default_model gpt-5.5 \
    --root -o
Then navigate to
http://127.0.0.1:8001/-/agent
and run the prompt:
show me some micropython
Should you trust my vibe-coded sandbox?
Having complained about immature, loosely-maintained sandboxing libraries, it’s deeply ironic that I’ve now built my own!
I deliberately slapped an alpha release version on it, and I’m not ready to recommend it to anyone who isn’t willing to take a significant risk.
I’ve put it through enough testing that I’m OK using it myself. I’ve shipped my first plugin that uses it,
datasette-agent-micropython
. I’ve also locked GPT-5.5 xhigh in that Datasette Agent plugin and
challenged it to break out of the sandbox
and so far it has not managed to.
I’m hoping this implementation can convince some companies with professional security teams and high-stakes problems to commit to using Python in WebAssembly as a sandboxing approach and open source their own solutions.
