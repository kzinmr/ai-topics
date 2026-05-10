---
title: "Leanstral: Open-Source foundation for trustworthy vibe-coding"
source: "Mistral AI Blog"
url: "https://mistral.ai/news/leanstral"
scraped: "2026-05-10T01:21:07.674171+00:00"
lastmod: "2026-03-19T12:18:37.731Z"
type: "sitemap"
---

# Leanstral: Open-Source foundation for trustworthy vibe-coding

**Source**: [https://mistral.ai/news/leanstral](https://mistral.ai/news/leanstral)

Leanstral: Open-Source foundation for trustworthy vibe-coding
Research
First open-source code agent for Lean 4.
Mar 16, 2026
Mistral AI
AI agents have proven to be highly capable tools at code generation. Yet, as we push these models to high-stakes domains, ranging from frontier research mathematics to mission-critical software, we encounter a scaling bottleneck: the human review. The time and specialized expertise required to manually verify become the primary impedance of engineering velocity.
We envision a more helpful generation of coding agents to both carry out their tasks and formally prove their implementations against strict specifications. Instead of debugging machine-generated logic, humans dictate what they want. Today, we are taking the first major step toward that vision.
Introducing Leanstral
We release Leanstral, the first open-source code agent designed for Lean 4. Lean4 is a proof assistant capable of expressing complex mathematical objects such as
perfectoid spaces
and software specifications like
properties of Rust fragments
. Unlike existing proving systems that act as wrappers around large generalist models or focus on single math problems, Leanstral is designed to be highly efficient (with 6B active parameters) and trained for operating in realistic formal repositories.
Open and accessible: We release Leanstral weights under an Apache 2.0 license, in an agent mode within Mistral vibe, and through a free API endpoint. We will also release a tech report detailing our training approach, and a new evaluation suite FLTEval, to move evaluations beyond their focus on competition math.
Efficient and mighty: We use a highly sparse architecture for Leanstral, and optimise it for proof engineering tasks. Leveraging parallel inference with Lean as a perfect verifier, Leanstral is both performant and cost-efficient against existing closed-source competitors.
Upgradable via MCP: Leanstral supports arbitrary MCPs through vibe, and was specifically trained to achieve maximal performance with the frequently used lean-lsp-mcp.
Evaluation
To reflect usefulness in realistic proof engineering scenarios, we benchmark Leanstral for completing all formal proofs and correctly defining new mathematical concepts in each PR to the FLT project, instead of isolated mathematical problems. We compare Leanstral against leading coding agents (Claude Opus 4.6, Sonnet 4.6, Haiku 4.5) and open-source models (Qwen3.5 397B-A17B, Kimi-K2.5 1T-A32B, GLM5 744B-A40B).
Leanstral vs. OSS Models
Leanstral-120B-A6B demonstrates a significant efficiency advantage over its much larger open-source peers. While models like GLM5-744B-A40B and Kimi-K2.5-1T-32B struggle to scale, capping their FLTEval scores at approximately 16.6 and 20.1 respectively, Leanstral outperforms them both with just a single pass.
Even Qwen3.5-397B-A17B, the strongest OSS competitor shown, requires 4 passes to reach a score of 25.4. In contrast, Leanstral achieves a superior score of 26.3 with half that investment (pass@2) and continues to scale linearly, reaching 29.3 at the same cost level.
Leanstral vs. Claude Family
Leanstral serves as a high-value alternative to the Claude suite, offering competitive performance at a fraction of the price: Leanstral pass@2 reaches a score of 26.3, beating Sonnet by 2.6 points, while costing only $36 to run, compared to Sonnet’s $549. At pass@16, Leanstral reaches a score of 31.9, comfortably beating Sonnet by 8 points. While Claude Opus 4.6 remains the leader in quality, it carries a staggering cost of $1,650, 92 times higher than running Leanstral.
In our benchmarking, we used Mistral Vibe as the scaffold with no modifications specifically for the evaluation.
Model
Cost ($)
Score
Haiku
184
23.0
Sonnet
549
23.7
Opus
1,650
39.6
Leanstral
18
21.9
Leanstral pass@2
36
26.3
Leanstral pass@4
72
29.3
Leanstral pass@8
145
31.0
Leanstral pass@16
290
31.9
Case studies
Answering stackexchange posts about changes in newest Lean version
When breaking changes hit a new Lean release, migrating code can be a massive headache. We fed Leanstral
a real-world question from the Proof Assistants Stack Exchange
about a script that mysteriously stopped compiling in Lean 4.29.0-rc6 (which we did not train with due to its recency). The culprit was a rewrite (
rw
) tactic that suddenly failed to match patterns involving a simple type alias, initially written as
def T2 := List Bool
.
Instead of taking a stab in the dark, Leanstral rolled up its sleeves. It successfully built test code to recreate the failing environment and diagnosed the underlying issue with definitional equality. The model correctly identified that because def creates a rigid definition requiring explicit unfolding, it was actively blocking the rw tactic from seeing the underlying structure it needed to match.
The fix it proposed was simple: just swap
def
for
abbrev
. Because
abbrev
creates a transparent alias that is immediately definitionally equal to the original type, the
rw
tactic could once again perfectly match the pattern
(L2 n).length
in the proof. Leanstral completes the job and explains the rationale to the user perfectly.
Reasoning about programs
We copied over definitions in Rocq from
https://www.cs.princeton.edu/courses/archive/fall10/cos441/sf/Imp.html
and asked Leanstral to convert to Lean. It did so successfully, even implementing custom notation. Example snippet:
inductive ceval : com → state → state → Prop where
| E_Skip (
st
: state) : ceval .CSkip st st
| E_Ass (
st
: state) (
a1
: aexp) (
n
: Nat) (
l
: ident) (
h
: aeval a1 st = n) :
ceval (
.CAss
l a1) st (
update
st l n)
| E_Seq (
c1
c2 : com) (
st
st' st'' : state) (
h1
: ceval c1 st st') (
h2
: ceval c2 st' st'') :
ceval (
.CSeq
c1 c2) st st''
| E_IfTrue (
st
st' : state) (
b1
: bexp) (
c1
c2 : com) (
h
: beval b1 st = true) (
h1
: ceval c1 st st') :
ceval (
.CIf
b1 c1 c2) st st'
| E_IfFalse (
st
st' : state) (
b1
: bexp) (
c1
c2 : com) (
h
: beval b1 st = false) (
h1
: ceval c2 st st') :
ceval (
.CIf
b1 c1 c2) st st'
| E_WhileEnd (
b1
: bexp) (
st
: state) (
c1
: com) (
h
: beval b1 st = false) :
ceval (
.CWhile
b1 c1) st st
| E_WhileLoop (
st
st' st'' : state) (
b1
: bexp) (
c1
: com) (
h1
: beval b1 st = true) (
h2
: ceval c1 st st') (
h3
: ceval (
.CWhile
b1 c1) st' st'') :
ceval (
.CWhile
b1 c1) st st''
-- Notation for command evaluation
notation:
50
c
" / "
st
" ⇒ "
st' => ceval c st st'
It could also translate to Lean and then prove some properties about programs in this language when just given the Rocq statement (without proof):
-- Example command: adds
2
to variable X
def plus
2
: com := .CAss
"X"
(
.APlus
(
.AId
"X"
) (
.ANum
2
))
-- Theorem: The plus
2
command correctly adds
2
to variable X
-- Intuition: If X has value n in the initial state, after executing plus
2
,
-- X will have value n
+2
in the final state
-- This specifies the behavior of the plus
2
command
theorem plus
2
_spec (
st
: state) (
n
: Nat) (
st
' : state) (
h1
: st
"X"
= n) (
h2
: plus2 / st ⇒ st') :
st'
"X"
= n +
2
:= by
-- plus
2
is defined as .CAss
"X"
(
.APlus
(
.AId
"X"
) (
.ANum
2
))
-- Use equation compiler to unfold it
change ceval (
.CAss
"X"
(
.APlus
(
.AId
"X"
) (
.ANum
2
))) st st' at h
2
cases h
2
with
| E_Ass _ _ n l h =>
have : aeval (
.APlus
(
.AId
"X"
) (
.ANum
2
)) st = n := h
simp only [
aeval
] at this
rw [
update
]
simp [
←
this, h1]
Demand Proof. Try Leanstral Today.
Leanstral is available today for everyone to use.
Zero-Setup in Mistral Vibe: We’ve integrated Leanstral directly into Mistral Vibe for immediate, zero-setup vibe coding and proving. Use
/leanstall
to active.  Then to use Leanstral press
Shift+Tab
until the model displays as Leanstral,  Alternately, use
vibe --agent lean
.
Labs API: Access the model via our free/near-free API endpoint
labs-leanstral-2603
. We are keeping this endpoint highly accessible for a limited period to gather realistic feedback and observability data to fuel the next generation of verified code models.
Own the Weights: Download the Apache 2.0 licensed model and run it on your own metal.
Documentation
-
Sign Up for Mistral Vibe
Share this article
More from Mistral AI
News
Models
AI Services
