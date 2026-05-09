---
title: "LLMs as Giant Lookup-Tables of Shallow Circuits"
author: niplav, Claude+
source: https://www.lesswrong.com/posts/a9KqqgjN8gc3Mzzkh/llms-as-giant-lookup-tables-of-shallow-circuits
date: 2026-03-17
tags: [mechanistic-interpretability, alignment, ai-safety, circuits, superposition, agent-structure, shard-theory, computation-in-superposition]
scraped: 2026-05-09
---

# LLMs as Giant Lookup-Tables of Shallow Circuits

By niplav, Claude+ | 2026-03-17 | 95 points | 35 comments
Tags: Shard Theory, Agent-Structure Problem, Comp-In-Sup, Language Models (LLMs), AI

Early 2026 LLMs in scaffolds, from simple ones such as giving the model access to a scratchpad/"chain of thought" up to MCP servers, skills, and context compaction are *quite* capable. ([METR graph](https://metr.org/time-horizons/).)

Yet: If someone had told me in 2019 that systems with such capability would exist in 2026, I would strongly predict that they would be almost uncontrollable optimizers, ruthlessly & tirelessly pursuing their goals and finding edge instantiations in everything. But they don't seem to be doing that. Current-day LLMs are just not *that* optimizer-y, they appear to have capable behavior without apparent agent structure.

Discussions from the time either ruled out giant lookup-tables (Altair 2024) or specified that the optimizer must be in the causal history of such a giant lookup-table (Garrabrant 2019).

The most fitting rejoinder to the observation of capable non-optimizer AIs is probably *"Just you wait"* — current LLMs are *capable*, sure, but they're not wildly superhuman to an extent comparable to the original worries about extreme optimization pressure. In this view, they're molting into full agency right now, and we should see the problems of high optimization pressure show up by the end of 2026 or the five years after (50%) if they're not hidden from us by deceptive AIs (35%). Indeed, current LLMs *do* reward-hack, though the developers have been decent at suppressing the tendency down to a consumer-acceptable level.

But the author has a different theory for how LLMs can be capable without being agentic/perniciously optimizing:

**LLMs are superlinear-in-network-width lookup-table-like collections of *depth-limited*, *composeable* and *error-correcting* circuits, computed in superposition.**

One could call this the GLUT-of-circuits model of LLMs.

To elaborate:

1. **"lookup-table-like"**: A common issue in proving theorems about agent structure is to avoid including giant lookup tables where each sequence of previous percepts and actions is matched to an optimal next action. Such a giant lookup table is infeasible in the real world, but something *similar* to a giant lookup table might be possible, namely through computation in superposition.

2. **"circuits"**: Turing machines aren't a great model for the type of computation that neural networks use (namely because they assume an infinite tape and arbitrary serial depth); a slightly better one is circuits, which have limited depth.

3. **"computed in superposition"**: Current LLMs represent features in superposition, that is, they exploit the fact that high-dimensional spaces can have exponentially many almost-orthogonal vectors relative to the number of dimensions (a consequence of the Johnson-Lindenstrauss lemma). Computation in superposition generalizes this observation to cram more computation into a neural network.

4. **"superlinear-in-network-width"**: Computation in superposition allows for running many circuits at the same time. Hänni et al. 2024 construct (shallow) neural networks of width Õ(m^(2/3) s²) that are able to emulate an s-sparse boolean circuit of width m (Theorem 8). This result gestures at the possibility that one *can* put a superlinear number of circuits into a single neural network, making the neural network more of a lookup-table than an example of general-purpose search.

5. **"depth-limited"**: A forward pass in SOTA language models has a limited number of steps of serial computation; GPT-3-davinci had 96 layers, which results in a circuit depth of ~[7488, 7968] serial steps per forward pass. Current frontier models don't have a circuit depth of more than ~20,000. Claude Sonnet 4.5 estimates that Kimi K2.5 Thinking has slightly less than 5000 serial steps of computation.

6. **"composeable"**: The circuits are selected by reinforcement learning, especially RLVR, to be *composeable*, that is each circuit takes inputs of the same type as outputs of other circuits in the network.

7. **"error-correcting"**: If a forward pass executes many circuits in superposition, there will be some interference between individual circuits, so circuits will be selected to be either robust to small errors or error-correcting. This is oddly similar to results from singular learning theory.

### Inferences

**Circuit selection**: This model would imply that circuits are selected mostly by another algorithm with very small serial depth, relying on features of a problem that can be determined by very parallel computations. That somewhat matches observations from looking at LLMs trying to tackle problems: they try one strategy after another, and less often use detailed information from the past failed attempt to form a complicated new strategy.

It *also* matches what we've seen from LLMs self-preserving/black-mailing/reward-hacking: The actions seem opportunistic, not carefully hidden once they've been performed, not embedded in larger plans; they look mostly like "another strategy to try, oops, I guess that didn't quite work".

**Alignment**: My guess is that most or almost all of these circuits are *individually aligned* through bog-standard RLHF/Constitutional AI. This works because the standard problems of edge instantiation and Goodhart's law don't show up as strongly, because the optimization mainly occurs by either:
1. Selecting one circuit from the giant lookup table that is all the circuits in superposition in the LLM
2. Running many circuits in superposition and selecting the best result or aggregating the best results.

If this view is correct, a folk view of alignment as simply "deleting/downweighting the bad parts of a model" would be *mostly correct*: There would be a large but finite number of circuits embedded in the model, which can be upweighted, downweighted or outright deleted by gradient descent. My extremely speculative guess is that there is less than a quadrillion circuits stored in superposition in a trillion-parameter model (85%), which thorough-enough safety training could exhaustively or near-exhaustively check and select.

**Chain of thought**: The obvious wrinkle in this story is that I haven't talked about chain-of-"thought"/"reasoning" LLMs. Long chains of thought enable vastly more serial computation to be done.

Still, some guesses at implications:
1. The **token bottleneck** is *real*. Every <10k serial steps the entire state needs to be compressed down to one of 50k-200k tokens, resulting in at most 16-20 bits of state to be passed between each circuit. Maybe ~8-10 bits (given ~1 bit per character in English), so maybe 2 bits per character in an optimized chain of "thought".
2. Continuous chains of "thought" would be quite bad, since they'd increase the serial depth without information bottlenecks by a lot.
3. It now matters that all the circuits are aligned even when composed with each other, which is not guaranteed at all.

**Training process**: If we see this whole model as being about amortized optimization, maybe it's the training process that takes up all the optimization power?

The author thinks this model is mostly correct (50%), and also has implications for capabilities progress/the need to switch to another paradigm.

Related/prior work:
1. The shard theory of human values (Quintin Pope/TurnTrout, 2022)
2. Simulators (janus, 2022)
