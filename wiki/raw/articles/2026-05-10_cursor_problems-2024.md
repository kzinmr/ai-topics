---
title: "More problems · Cursor"
source: "Cursor Blog"
url: "https://cursor.com/blog/problems-2024"
scraped: "2026-05-10T01:19:51.463235+00:00"
lastmod: "2026-05-09T16:09:42.638Z"
type: "sitemap"
---

# More problems · Cursor

**Source**: [https://cursor.com/blog/problems-2024](https://cursor.com/blog/problems-2024)

Blog
/
research
May 25, 2024
·
research
More problems
Several exciting problem areas for the next phase of AI-programming.
Aman Sanger
·
7 min read
Table of Contents
↑
Next action prediction
Promising directions
Perfect edits
Hallucinated pseudocode
Multi-file edits
Promising directions
Optimal context
Multi-hop context
Promising directions
Bug detection and debugging
Detecting bugs in AI review
AI linting
Smarter debugging
Promising directions
As a follow-up to
our original problems post
, here are some more of the problems we believe matter most for the next phase of AI-programming.
#
Next action prediction
Cursor comes with
Copilot++
, a more intelligent version of copilot that predicts your next edit. Can we take this idea to its natural limit?
When coding, you don’t just make low-entropy
edits
. Across the entire editor, you take low-entropy keystrokes, clicks,
actions
. Can we build a model to predict each with low-latency?
To start, we’ve extended Copilot++ to predict your next location. Combine this with next edit prediction, and the model can play through a sequence of low-entropy changes:
We press tab 11 times and all other keys 3 times. We call this Cursor Flow (for obvious reasons).
We’re working on predicting the next file you will move to. The next terminal command you will run. The next edit, conditioned on your previous terminal commands! A
next action prediction model
.
Furthermore, the model should surface information the moment you need it. Whether it be the right piece of code or documentation.
Cursor should
feel
like an extension of your will. The moment you think of a change, the language model requires minimal intent to execute it instantly.
#
Promising directions
Fundamental research on
action prediction
across a codebase.
Continued pre-training and post-training on ~5–13B active parameter code-models (for prefill-bound low-latency predictions).
Additional inference tricks similar to
Speculative Edits
Clever UX for surfacing “actions” in a non-obtrusive way. (How do you propose the next file a user should move to? Or the next location outside the current viewport?)
#
Perfect edits
Can we scale up inference time compute to produce higher-quality, larger edits? How do we compensate for the increased latency?
It may be necessary to perform the edit
in the background
. Spawning off a unit of work that you can trust to intelligent models.
We’ll need models with strong editor-specific tool-use abilities, smarter codebase-wide context, and improved long-term reasoning.
And how can we make async code-generation
flow-preserving
. This sounds like an oxymoron, but we believe clever research in model capabilities and UX may make this possible.
#
Hallucinated pseudocode
We implement functions/code that don’t exist, then the model creates them for us in the background.
Users will write pseudocode that describes the desired change. Then we can trust Cursor to compile the pseudocode into the full change in the background.
#
Multi-file edits
Cmd-k
is already fantastic, but what if you could ask for a generic edit across your entire codebase? In particular, one that accurately spans multiple files?
#
Promising directions
Scaling inference-time compute. We know reward models and rejection sampling will show quick and easy improvements, but how much farther can we go?
Better reasoning models (gpt-5, claude-4, gemini 2.0)
Running multiple language-server/file-system copies for a given user workspace. This will require model tool use and remotely reproducing runtime environments.
Training/improving model performance on agent trajectories
Significant UX experimentation for in-flow async edits
#
Optimal context
There can be millions of tokens of documentation, tens of millions of tokens of source code, another tens of millions of tokens of commit history, all potentially useful tokens to resolve a single query.
Not to mention, the pixels in your UI, logs in production and localhost, messages in Slack, etc...
We believe the best coding systems will use a mix of retrieval, recurrence, and long-context attention to ingest all this information.
We emphasize
systems
as in the short-term, this may be an ensemble of models and infra that comprise an infinite context engine for coding. In the long-term, we expect it to be baked into the architecture.
We’re especially excited when thinking creatively about the future of retrieval. Moving past embeddings, what is the best performance possible given the primitive of an expensive indexing step and a cheap querying step (sublinear in the size of the corpus)?
Maybe it looks like some variant of
transformer memory as a differentiable search index
. Perhaps something else entirely. It’s an underexplored research direction.
#
Multi-hop context
Inside my codebase, I want to compute a diff between two strings. With embeddings, I get the chunk:
function
computeDiff
(
firstModel
:
ITextModel
,
secondModel
:
ITextModel
,
)
:
string
{
//...
}
To satiate the original query, I must determine how to create an
ITextModel
from a string. This is a query that requires two-hops to resolve.
The hardest questions and queries in a codebase
require
several hops. Vanilla retrieval only works for one hop.
#
Promising directions
Specialized/improved embeddings and rerankers for codebases.
Training multi-hop embedders. Given a query and the relevant code we’ve found so far, determine the next piece of code to hop to.
Clever prefix-caching and perhaps custom attention masks better suited for codebases.
Novel research on codebase-level retrieval.
Teaching a model to
learn
a codebase in the weights, similar to transformers as a search index.
#
Bug detection and debugging
Existing bug-detection systems struggle with calibration and sufficient codebase understanding.
Models are smart enough to correctly identify bugs, but are plagued by false-positives. Identifying the trickiest bugs require a deeper understanding of the codebase. And buggy-looking code may be benign after seeing the larger picture.
One way this could surface is a much better experience for code review using language models:
#
Detecting bugs in AI review
The benefit of “AI review” is that the user is more tolerant of false-positives, since they are requesting a review. The downside is it requires changing user behavior.
#
AI linting
The best version of bug detection is an always-on linter that catches your bugs in the background. It needs to be a cheaper, faster model than AI-review, since we’d run it several times a minute. It must also be tuned to a lower false-positive rate.
#
Smarter debugging
Perhaps more impressive than bug detection is debugging difficult issues.
We’ll need to go beyond LLM-based static analysis. For example, we’ve built a
cursor/debug
package. When injected into your code, it tracks runtime information.
In the background, we can even use it to track additional variable states (akin to print-debugging with relevant outputs piped into Cursor’s context).
#
Promising directions
Clever dataset curation (likely synthetic data) and RL on frontier code models to improve calibration.
Track relevant information from other surfaces (the browser or non-integrated terminal).
Improve frontier model performance on debugger-specific tool-use and chains.
Infinite context and near-perfect codebase understanding.
Expand the scope of our
cursor/debug
library to track all useful program-state information.
If any of these problems interest you, please reach out at
hiring@cursor.com
Filed under:
research
Author
:
Aman Sanger
