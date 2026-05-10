---
title: "Deploy and inference any model from HuggingFace"
url: "https://www.together.ai/blog/deploy-and-inference-any-model-from-huggingface"
fetched_at: 2026-05-10T07:00:44.179971+00:00
source: "Together AI Blog"
tags: [blog, raw]
---

# Deploy and inference any model from HuggingFace

Source: https://www.together.ai/blog/deploy-and-inference-any-model-from-huggingface

Something real is shifting in how developers work. Agents open up work that used to be off-limits, not because it was technically impossible, but because it required niche expertise most of us didn't have. Containerization, inference server configs, model-specific environment setup: these are the kinds of tasks that used to demand either deep expertise or hours of self-education before you could even get started. Agents allow for an elegant way to bridge those pre-requisite knowledge gaps. You describe what you want, and the agent fills in the knowledge gaps.
That's the unlock. Not speed.
Access.
‍
The day Netflix dropped a new model
Netflix recently released
void-model
on Hugging Face. The day it came out, my instinct was the same as always: I want to try this. But wanting to try a new model and actually
running
it are two different things. Getting it into a usable environment, handling the inference server setup, figuring out the container configuration, wiring it all up correctly: that's the part that usually introduces a day or two of lag between "this looks cool" and "okay I'm actually using it."
This time, that lag was basically zero.
Using
Goose
, a CLI agent runner, combined with Together's
dedicated containers skill
, I went from "Netflix just dropped a model" to "I have a running container for it" in a single session. The agent produced all the code needed to deploy void-model on Together's Dedicated Container Inference (DCI) infrastructure, essentially on release day.
The output lives here:
github.com/blainekasten/together-void-model-container
‍
Exactly what I did
The whole setup took three steps.
Step 1: Install the Together dedicated containers skill.
npx skills add togethercomputer/skills
That pulls in the
together-dedicated-containers skill
, which gives Goose the specific knowledge it needs to work with Together's infrastructure: how to configure the inference server, what the container spec should look like, how to wire everything up for a given model.
Step 2: Start a Goose session and run one prompt.
I want to deploy this model on togethers dedicated containers https://huggingface.co/netflix/void-model
That's it. One sentence.
Step 3: Sit back and watch it work.
From there, the agent pulled the model details from Hugging Face, figured out the right inference server configuration for the model architecture, generated the container config files, and produced a complete, runnable setup, all without me having to look anything up or guide it through individual steps.
The result:
blainekasten/together-void-model-container,
a clean, working repo anyone can use to run void-model on Together infrastructure.
Step 4: Use your model!
After the agent deploys your application you can start running inference against it. The
Together CLI
has commands to easily test inference.
tg beta jig submit --watch --payload '{
    "video_url": "https://github.com/Netflix/void-model/raw/refs/heads/main/sample/lime/input_video.mp4",
    "quadmask_url": "https://github.com/Netflix/void-model/raw/refs/heads/main/sample/lime/quadmask_0.mp4",
    "prompt": "Empty park bench with fallen leaves on the ground",
    "use_pass2": false
  }'
This model removes objects from videos along with all interactions they induce on the scene — not just secondary effects like shadows and reflections, but physical interactions like objects falling when a person is removed.
Our inference calls with this model are asynchronous. Therefore the response of this request will return a payload with an identifier we can poll for. The response looks like this:
{
  "model": "void-byoc",
  "request_id": "019dc0f3-3c73-7a3f-b4b6-87ad06091180",
  "status": "running",
  "claimed_at": "2026-04-24T19:24:19.447457Z",
  "created_at": "2026-04-24T19:24:19.444567Z",
  "done_at": null,
  "info": null,
  "inputs": {
    "prompt": "Empty park bench with fallen leaves on the ground",
    "quadmask_url": "https://github.com/Netflix/void-model/raw/refs/heads/main/sample/lime/quadmask_0.mp4",
    "use_pass2": false,
    "video_url": "https://github.com/Netflix/void-model/raw/refs/heads/main/sample/lime/input_video.mp4"
  },
  "outputs": null,
  "priority": 1,
  "retries": null,
  "warnings": null
}
When the inference completes, the outputs includes a URL to the hosted video. We can download it using cURL and our Together API key:
curl -L -O \
  https://api.together.ai/v1/storage/019dc0f3-3c73-7a3f-b4b6-87ad06091180-tmpddmhtvar.mp4 \
  --header "Authorization: Bearer $TOGETHER_API_KEY"
‍
Note: -L is required to follow the http redirect in the storage url and -O will write the output to a local file.
Why Together Dedicated Container Inference
This story only works because Together's Dedicated Container Inference (DCI) is genuinely a great place to run models like this, and it's worth explaining why.
DCI gives you a private, GPU-backed environment running the model of your choice, fully managed by Together. You're not fighting for shared resources, you're not configuring your own cluster, and you're not locked into a fixed menu of available models. You bring the model; Together handles the infrastructure.
This is a big deal for teams that want to move fast. When a new model drops from Netflix, from a research lab, from the open-source community, you can have it running in a production-grade environment almost immediately. No spinning up your own GPU VMs, no wrestling with inference server dependencies, no waiting for someone to add support for it in a managed endpoint. DCI is flexible by design: if the model exists, you can deploy it.
The cost model also makes it easy to experiment. You're paying for what you use, on a container that's yours, without the overhead of managing the underlying compute. That's the kind of setup that lets you say yes to testing new models instead of filing it away for "when I have time."
If you're interested in Together's DCI,
reach out to us
to get set up.
