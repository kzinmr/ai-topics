---
title: "Introducing Muse Glimmer"
url: "https://simonwillison.net/2026/Aug/10/introducing-muse-glimmer/"
fetched_at: 2026-08-13T10:19:21.454018+00:00
source: "simonwillison.net"
tags: [blog, raw]
---

# Introducing Muse Glimmer

Source: https://simonwillison.net/2026/Aug/10/introducing-muse-glimmer/

Introducing Muse Glimmer
(
via
) Meta are back in the open weights game! Muse Glimmer is a brand new 30B model under a clean Apache 2.0 license (a step up from the janky Llama licenses of old).
They claim to have optimized it for exactly the kind of things I'm looking for in a local model:
End-to-end Agentic Task Completion.
Muse Glimmer achieves strong success rates on full-task benchmarks including DeepSearch QA, MCP-Atlas, 𝛕-Bench and SWE-Bench, which measure its ability to work within scaffolds, write and debug code, and resolve multi-turn requests from start to finish.
Reliable Tool Use.
The model handles a wide range of function calls, invoking tools with precise schemas throughout extended workflows.
Multi-Step Reasoning.
Muse Glimmer chains reasoning over long horizons, sustaining coherent plans across complex, extended workflows. [...]
Here's
a pelican
which I generated using LM Studio's
18.16 GB version of the model
:
I also tried it out with my
llm-coding-agent
plugin, running against a fresh checkout of Datasette with the prompt:
how does auth work?
Here's the response
, at the end of a long transcript showing all of the tool calls it made to explore the codebase. I ran this using
llm-lmstudio
with
this patch applied
to upgrade it for compatibility with
LLM 0.32
.
I really like this size of model, because if a machine has 32 GB of RAM or more (mine has 128GB) it leaves plenty of space for running other applications at the same time.
Glimmer is a vision model, so I asked it to describe this image:
llm -m lmstudio/meta/muse-glimmer -a https://static.inaturalist.org/photos/714731804/large.jpg 'describe image'
Here's
what I got back
:
The photograph shows a rocky, breakwater-style shoreline on an overcast day with a smooth, gray body of water and a faint dock/pier line in the soft-focused background.
In the foreground two large brown pelicans,
Pelecanus occidentalis
, are perched on the jumbled gray-white stones. They have the species’ characteristic long, down-curved yellow-orange bills with a large throat pouch, long slender necks and mottled brown-gray plumage on the back and wings. The pelican on the left is turned slightly toward the camera and appears to be preening or resting its bill against its chest; a pale, whitish patch is visible on the crown and nape and a small crest of feathers is raised. The pelican on the right faces mostly forward/right, its head up, bill pointing down and to the right, with the same pale head markings and the barred, darker wing feathers clearly visible.
Scattered among the rocks around the two pelicans are several much smaller dark birds — gulls/tern-like birds in muted brown-gray plumage. One dark bird sits on the far left on a rock, another brownish bird stands to the right of the right-hand pelican, a grayish bird with a reddish bill is in the lower right foreground, and a further small dark bird is at the extreme right edge of the frame.
The overall light is flat and diffused, giving the water and sky a muted, almost monochromatic palette that contrasts with the textured rock and the detailed feathering of the pelicans. The composition places the two big birds as the dominant subjects, framed against the calm water and the low, rocky perch.
