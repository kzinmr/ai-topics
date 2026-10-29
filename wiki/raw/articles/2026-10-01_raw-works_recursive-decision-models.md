---
title: "Recursive Decision Models"
source_url: https://raw.works/recursive-decision-models/
author: Raymond Weitekamp (@raw_works)
published: 2026-10-01
ingested: 2026-10-28
source_type: blog
tags: [raw, blog, rlm, decision-models, system-one-models, jev, dspy, cmpnd]
---

# Recursive Decision Models

**Author:** Raymond Weitekamp ([@raw_works](https://x.com/raw_works)) — RAW Works (raw.works)
**Published:** October 1, 2026
**URL:** https://raw.works/recursive-decision-models/

Recursive Language Models (RLMs) have proven a powerful harness architecture for Large Language Models, enabling dynamic agent workflows (Anthropic), extremely long context processing (MIT), SOTA results on "long chain-of-thought" benchmarks (RAW.works), and even best-in-class performance on benchmarks such as ARC-AGI 3 (Prime Intellect).

"Recursive Decision Models" (RDMs) is an exploration of how the principles of RLMs can be applied to "decision models" (aka "System One models" aka "classifiers") such as Jev.

Briefly, a note on the naming: I don't particularly care what term people choose for the "genre of Jev". Diogo officially prefers "System One models", and has explicitly argued against the alternative: "Some people are trying to call them decision models… I wouldn't do that, because I think there's other types that are machine-native that are not decisions." Nevertheless, the zeitgeist seems to be trending towards "decision models" and I'm not willing to wait any longer for people to make up their mind.

> Team! What is the name of the "genre" of Jev? Please let's decide now so we don't need to re-name all of our projects later...
> — Raymond Weitekamp (@raw_works), September 21, 2026 (https://x.com/raw_works/status/2102052660622811558)

In developing this concept of RDMs, I've been working from three "non-negotiables" of how the system must behave:

1. The RDM system must externalize context and be able to programmatically decompose slices of that context.
2. The decision model must have the choice to call another decision model, up to some maximum depth of recursion.
3. The RDM system must be able to work with and without the presence of any generative model or function. In other words, it must stand alone as "pure decision models" and also compose with LLMs and agents.

I initially started exploring some of these ideas in a repo that I dubbed "one-system", which started as a "LiteLLM for Jev" and then I quickly realized could support recursion by composing requests through the gateway. Lucky for me, the DSPy team (in particular my esteemed peers at cmpnd.ai) has rapidly embraced Jev. Now that the TypeSafe System One API is supported in DSPy (`dspy.experimental.Noul, TypeSafe`), my task of conveying the essence of Recursive Decision Models is greatly simplified.

## A Simple RDM

A `dspy.Module` that recursively makes decisions up to its max depth:

```python
import dspy

class RDM(dspy.Module):
    def __init__(self, signature, tools, max_depth=3):
        super().__init__()
        self.predict = dspy.Predict(signature)
        self.tools = {tool.__name__: tool for tool in tools}
        self.max_depth, self.depth = max_depth, 0

    def forward(self, **inputs):
        answers = self.predict(**inputs)  # one request to the decision model
        observations = {}
        if self.depth < self.max_depth:
            self.depth += 1  # anything a tool calls is one level deeper
            for name, tool in self.tools.items():
                if answers[name].value:  # a yes runs the tool of the same name
                    observations[name] = tool(**inputs)
            self.depth -= 1
        return dspy.Prediction(observations=observations, **answers)
```

As a simple example, a signature that asks if the answer to a question is in a chunk of text, plus a function to divide and conquer by recursively halving the content:

```python
from dspy.experimental import Noul, TypeSafe

class Search(dspy.Signature):
    """Search a text for the answer to a question."""
    text: str = dspy.InputField()
    question: str = dspy.InputField()
    look: Noul = dspy.OutputField(desc="Is the answer to `inputs.question` stated in `inputs.text`?")

def look(text, question):
    lines = text.splitlines()
    if len(lines) <= 1:
        return lines  # down to one line, and the model said yes to it
    middle = len(lines) // 2
    found = []
    for half in lines[:middle], lines[middle:]:
        found += rdm(text="\n".join(half), question=question).observations.get("look", [])
    return found
```

To finish the specific example, we can search a handbook recursively to find the specific line that answers a query.

## Key takeaways

- RDM = RLM harness principles (externalized context, programmatic decomposition, self-recursion with depth bound) applied to *decision/System One models* rather than generative LLMs.
- Cascade metaphor: "A cascade of fans and funnels: an LLM fans out options, a decision model keeps one or two, and each one kept opens a smaller fan."
- The RDM must be usable standalone ("pure decision models") and composable with LLMs/agents.
- Enabled by DSPy's newly added TypeSafe System One API support (contribution from the cmpnd.ai team).
