---
title: "Toward Generalized Coding with Our First Loop Transformer"
url: "https://simonwillison.net/2026/Nov/23/glm-54/"
fetched_at: 2026-11-24T10:01:25.618880+00:00
source: "simonwillison.net"
tags: [blog, raw]
---

# Toward Generalized Coding with Our First Loop Transformer

Source: https://simonwillison.net/2026/Nov/23/glm-54/

GLM-5.4: Toward Generalized Coding with Our First Loop Transformer
. GLM 5.4 is now available from Chinese AI lab Z.ai. It's their first model to use a looped transformer architecture, which they describe like this:
In a standard Transformer, each layer runs once per forward pass. In a Loop Transformer, a group of weight-shared layers runs for multiple iterations, refining the hidden states from the previous pass. This gives us a deeper network without increasing the parameter count.
This is the second mention of looped transformers I've seen in the past week - the first was
Inkling 2 Mini
from Thinking Machines Lab on November 20th, who said:
Inkling 2 Mini is a looped transformer, running the middle layers of the model three times for every token. This allows the model to apply more reasoning and reach the right answer with fewer tokens, especially on tasks such as agentic coding that depend on reasoning quality.
GLM 5.4 is not (yet?) available as open weights. I tried it out using the Z.ai API, for which I had to sign up for their
Coding Plan subscription
because 5.4 cannot currently be accessed through the regular API.
It turns out both coding plan and regular API share the same OpenAI-compatible Responses API (at
https://api.z.ai/api/v1
), and the API key for the coding plan worked with that and gave me access to the new model.
I built a
llm-glm plugin
, then realized that
llm-zai
by Tommy Hughes already exists! I've shipped mine purely because
llm-zai
doesn't yet support the new model, but I'll likely retire mine once that plugin catches up.
Here are
pelicans for GLM-5.4
on low, high, and max. This is the max one:
I realized I never ran pelicans for GLM-5.3, so
here those are
for the same effort levels. They look similar in quality to 5.4.
It's interesting how
GLM 5.1
and
GLM 5.2
produced radically different pelicans from other models. The pelicans for 5.3 and 5.4 are much more comparable to those I get from OpenAI or Anthropic models - the previous generations had their own distinctive look.
I made a
comparison grid
showing the four generations of GLM pelicans all in one place. The style transition between 5.2 and 5.3 is pretty stark.
