---
title: "Anthropic says Alibaba illicitly extracted Claude AI model capabilities"
url: "https://www.reuters.com/world/china/anthropic-says-alibaba-illicitly-extracted-claude-ai-model-capabilities-2026-06-24/"
fetched_at: 2026-06-25T11:09:39.981286
source: hn-algolia
hn_points: 450
hn_object_id: 48664814
tags: [raw, hn-discussion]
---

# Anthropic says Alibaba illicitly extracted Claude AI model capabilities

Source: https://www.reuters.com/world/china/anthropic-says-alibaba-illicitly-extracted-claude-ai-model-capabilities-2026-06-24/
HN: 450 points, 141 comments
Posted by: htrp

## HN Discussion Summary

**zakkl**: It sounds like Anthropic is eagerly trying to show to USG that they are willing to heavily monitor ‘foreign adversaries’ on their platforms. This combined with no implementation of KYC makes it seem like they want to find a middle ground with Fable where its off of export controls but they promise to prevent China and specific others from using.

**drillsteps5**: I&#x27;m looking forward to the trial where Anthropic will have to disclose sources of their training data, and then explain why they are entitled to charging customers for using regurgitated training data but Alibaba which trains their models on Anthropic&#x27;s models are not. Should be fun. Edit: clarification

**rvz**: Notice how Anthropic is now scapegoating Chinese models providers like Alibaba and outright accusing them of distilling their models. Whether if it is true or not, this is part of their effort into using them as an example to scare everyone into getting congress to ban powerful models from being accessed outside of the US and also banning powerful local models from being released. Anthropic does not care about you, and they are not your friends.

**zb3**: If true then Alibaba is doing us a public service, good job, I hope this extraction was successful.

**0xbadcafebee**: There&#x27;s two basic kinds of distillation: 1) the massive [and dumb] method where you ask a question and use the answer as reinforcement (Black Box), and 2) more targeted distillation where you use one model to directly inform&#x2F;train&#x2F;guide another model (RLAIF). The latter is basically fine-tuning the model with direction from another model. Thousands of businesses do this every day to fine-tune. This is almost certainly what the Chinese labs are doing, since it has a much better eff

**Pxtl**: You&#x27;re trying to kidnap what I&#x27;ve rightfully stolen!

**walrus01**: Reminds me a bit of the anecdote of Steve Jobs complaining about people ripping off the Mac GUI, in the mid to late 1980s, when he gave no public acknowledgement to the work done by Xerox on the Alto and Star operating system. you&#x27;re trying to rip off what I&#x27;ve already ripped off! Crawl the whole Internet to build a gargantuan sized LLM and then complain you&#x27;re being copied...

**gaiagraphia**: A company which got rich on extracting the world&#x27;s content is complaining that another company has extracted their work?! LOL! Get a grip, son.

**amazingamazing**: Distillation is fundamentally impossible to protect against. All you can do is slow them down. Change my view. Eventually these Chinese companies will release some extension like Honey, which will sit on top real, non-Chinese clients and send everything to China anyway. It&#x27;s over.

**randomboy3423**: A partly insider on this. I think Anthropic is just marketing &#x2F; bluffing, because they don&#x27;t even have the data. They do distill the models, but they don&#x27;t go to Anthropic, they just use platforms like aws bedrock, there are too many restrictions on Anthropic&#x27;s own platform.

**tristanj**: Here&#x27;s what is happening: Chinese resellers are offering Claude tokens at 70-90% below official Anthropic API prices. They achieve this by reselling capacity from pooled Claude Max accounts, payments fraud, and also reselling the model output reasoning chains to various Chinese labs. They are subsidizing model access in exchange for user logs and reasoning traces, which they then sell as training data, allowing them to operate below cost. Claude and ChatGPT are both blocked in China. You ne

**ProAm**: Says the company that is involved in the largest copyright heists of all time to build it&#x27;s product.

**BigTTYGothGF**: If you&#x27;re an AI booster surely you&#x27;d think this was a good thing as it means more models are available in more places to more people more easily. I&#x27;m exactly the opposite, and I think this is a good thing because I want Anthropic to suffer.

**jrflowers**: I like that they use “illicit” and “fraudulent” like as if model distillation is illegal and giving them money and then doing whatever they want with the output of their publicly accessible models (which Anthropic does not own) is… also illegal? “Anthropic, red faced after unattended ice cream cone eaten by ants on park bench, once again demands government pick it as forever winner, adds ‘no take backsies’”

**thadk**: Does anyone have hints on what kinds of prompts are most used for a distillation like this—SWE-Bench sorts of things? Is reconstructing the compressed knowledge in the model like reconstructing a lossy JPG or MP3 a reasonable analogy?

**awkwabear**: Wait so they&#x27;re upset that people used their IP to train a model without their consent or paying them anything? or is this just about the token reselling?

**paxys**: Repeatedly warn everyone that your models are so good they will wreck cybersecurity. Complain&#x2F;brag that chinese firms are illegally using the models and bypassing export controls. Be surprised when your model gets banned by the government.

