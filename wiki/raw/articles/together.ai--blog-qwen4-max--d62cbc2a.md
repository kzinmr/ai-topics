---
title: "Qwen4 Max is live on Together AI"
url: "https://www.together.ai/blog/qwen4-max"
fetched_at: 2026-11-22T10:01:11.738136+00:00
source: "Together AI Blog"
tags: [blog, raw]
---

# Qwen4 Max is live on Together AI

Source: https://www.together.ai/blog/qwen4-max

We gave
Qwen4 Max
a bug report and an entire codebase in one request. The codebase was Tornado, the Python web framework: all 344 files, 652,519 tokens. The model had no tools, and we didn't select relevant files or run a retrieval step first. Seventy-two seconds later it returned a patch, and the patch passes the tests Tornado's maintainers wrote for that bug. The request cost 69 cents.
It also found a precedent elsewhere in the repository. The bug report never mentions
tornado/iostream.py
, but the model pointed to code there that already handles errors the way its patch needed to. Tornado's maintainers cite the same code in their own fix.
Qwen4 Max is Alibaba's flagship Qwen model. It's live on Together AI today, and it's 30% off through November 22, 2026.
The test
Tornado is an open-source Python web framework. Its repository holds about 340 files of code, tests and docs. That fits in Qwen4 Max's context window, and it's far more than anyone would paste into a prompt by hand. We picked a fix the maintainers committed on November 18, 2026, two days after Qwen4 Max was released, and tested against the repository as it was just before that commit.
This is one example, chosen to show what a single call can do and what it costs.
The bug is in Tornado's websocket code. When a connection closed with messages still unsent, every
write_message()
call that wasn't awaited logged an error, even though awaiting it is optional. We sent every text file in that checkout as one prompt, with a bug report that describes only the symptom:
write_message logs "Task exception was never retrieved" when the connection closes
When a websocket connection closes while messages are still unsent (for example, the client sends its messages and a FIN, or resets the connection, without reading the replies), every write_message() call whose result was not awaited logs "Task exception was never retrieved" at ERROR level.
Awaiting the Future returned by write_message is optional, so an unawaited call should not log anything. A caller that does await it should still get WebSocketClosedError.
We asked for the cause and a patch. This is the request, replayed:
What came back
The first token arrived after 54 seconds, and the reply was complete at 72. Qwen4 Max traced the error to
WebSocketProtocol13.write_message
in
tornado/websocket.py
. That method wraps each write in a task. When the connection closes, the task fails with an exception that nobody is required to collect, and Python logs that as "Task exception was never retrieved."
The model's patch marks the exception as retrieved. Nothing is logged, and a caller who does await the write still gets the error:
-        return asyncio.ensure_future(wrapper())
+        task = asyncio.ensure_future(wrapper())
+
+        # Awaiting the returned Future is optional, so an error nobody looks
+        # at must not be reported as "Task exception was never retrieved".
+        # Retrieving it here leaves it in place for callers that do await.
+        def _mark_retrieved(t: "asyncio.Task[None]") -> None:
+            if not t.cancelled():
+                t.exception()
+
+        task.add_done_callback(_mark_retrieved)
+        return task
The precedent is what makes the patch read like it belongs in the project. The model's explanation says the fix should do what
BaseIOStream.write
already does for its own futures. That method is in
tornado/iostream.py
, one layer below the websocket code, and it solves the same problem the same way. The maintainers' commit makes the same comparison.
Nobody picked those files for it. All 344 went in, and the model found the two that mattered.
How we checked it
Tornado's maintainers added two regression tests with their fix: one for a write that isn't awaited, and one for a write that is. On the code before the fix, the first one fails. With the model's patch applied, both pass. We then ran Tornado's full suite, 1,673 tests, with the patch in place, and none failed.
What it cost
At the sale price, the request works out to about 69 cents, nearly all of it for the 652,519 input tokens. At list price it would be 98 cents.
Sending the same repository again costs far less. Together AI caches prompt input automatically, and cached input is \$0.0525 per million tokens during the sale. When we repeated a request of about 630,000 tokens, nearly all of it came back cached. The first token arrived in 8 seconds instead of 54, and the input cost about 3 cents instead of 66.
About Qwen4 Max
Alibaba released Qwen4 Max on November 16, 2026, and describes it as the most capable model in the Qwen family to date. It positions the model for long agent work, including coding across large repositories, which is the kind of task we tested.
Qwen4 Max is a sparse mixture-of-experts model with 2.4 trillion parameters, of which 71 billion are active for each token. On Work360, Alibaba's own benchmark of industry tasks across 721 specialized fields, Alibaba reports that it outperforms Qwen3.8 Max overall, uses 35% fewer tokens at high reasoning effort, and costs about 60% less per task on average. Those are Alibaba's figures, and
its announcement
has the details.
Run it on Together AI
Qwen4 Max is on Together Serverless Inference under the model string
Qwen/Qwen4-Max
. This script sends a whole repository and a bug report in one request, the way our test did. You need the Together Python SDK (
pip install together
), a
TOGETHER_API_KEY
, a local clone of the repository and the bug report saved as
bug_report.md
. It sends every text file git tracks, so check the repository for secrets first.
import subprocess
from pathlib import Path

from together import Together

repo = Path("tornado")
bug_report = Path("bug_report.md").read_text()

# Every file git tracks, skipping the ones that aren't text
names = subprocess.check_output(
    ["git", "-C", str(repo), "ls-files"], text=True
).splitlines()
files = []
for name in names:
    try:
        files.append(f"=== FILE: {name} ===\n{(repo / name).read_text()}\n")
    except UnicodeDecodeError:
        continue

client = Together()

stream = client.chat.completions.create(
    model="Qwen/Qwen4-Max",
    messages=[
        {
            "role": "system",
            "content": f"This is a complete repository, {len(files)} files.\n\n"
            + "".join(files),
        },
        {
            "role": "user",
            "content": f"Here is a bug report.\n\n{bug_report}\n\n"
            "Explain the cause, then write a patch.",
        },
    ],
    stream=True,
)

for chunk in stream:
    if not chunk.choices:
        continue
    delta = chunk.choices[0].delta
    # delta.reasoning carries the model's thinking, delta.content the answer
    if delta.content:
        print(delta.content, end="", flush=True)
Two things in it are specific to this model. Requests have to set
stream=True
, because Qwen4 Max on Together AI accepts streaming requests only. And thinking is on by default, so the model's reasoning streams first in
delta.reasoning
and there's a pause before the answer starts. Thinking tokens count as output tokens. To skip the thinking on a simple request, pass
reasoning={"enabled": False}
.
To try it without writing code, open it
in the playground
. The
model page
has the same details.
FAQs
How much does Qwen4 Max cost on Together AI?
Qwen4 Max on Together AI has a list price of \$1.50 per 1M input tokens, \$4.50 per 1M output tokens and \$0.075 per 1M cached input tokens. Through November 22, 2026, it's 30% off: \$1.05, \$3.15 and \$0.0525. Thinking tokens count as output tokens.
What is the context window of Qwen4 Max on Together AI?
Qwen4 Max has a 1M-token context window on Together AI. In our test, a request with 652,519 input tokens returned its first token after 54 seconds.
Does Qwen4 Max accept images?
Yes, Qwen4 Max accepts text and image input on Together AI and returns text. Send each image as an
image_url
block in the message content, as described in the
vision docs
.
Why does my Qwen4 Max request fail without streaming?
Qwen4 Max on Together AI accepts streaming requests only. A request without
"stream": true
returns a 400 error with the code
streaming_required
. Set
stream=True
in the SDK, or
"stream": true
in the request body, and read the reply from the stream.
How do I turn off thinking on Qwen4 Max?
Pass
reasoning={"enabled": False}
in the Python SDK, or
"reasoning": {"enabled": false}
in the request body, to turn off thinking on Qwen4 Max. Thinking is on by default, and it comes back in the
reasoning
field ahead of the answer. To get more thinking on a hard problem, set
reasoning_effort
to
"max"
.
Does Qwen4 Max support tool calling?
Yes, Qwen4 Max supports tool calling on Together AI through the standard
tools
parameter. It can return more than one call in a turn.
Does prompt caching work with Qwen4 Max?
Yes, prompt caching is automatic for Qwen4 Max on Together AI, and cached input tokens cost \$0.075 per 1M at list price. In our test, a repeat of a 630,000-token request came back almost entirely cached, and its first token arrived in 8 seconds instead of 54. Caching is best effort, so not every repeat is cached.
Can I fine-tune Qwen4 Max or run it on a dedicated endpoint?
No, Qwen4 Max is serverless only on Together AI today, and it isn't available for fine-tuning. Alibaba says smaller open-weight models from the Qwen4 series will follow.
