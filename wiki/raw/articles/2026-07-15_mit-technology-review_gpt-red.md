---
title: "Meet GPT-Red: an LLM super-hacker OpenAI built to make its models safer"
url: "https://www.technologyreview.com/2026/07/15/1140514/meet-gpt-red-an-llm-super-hacker-openai-built-to-make-its-models-safer/"
source: "MIT Technology Review"
author: "Will Douglas Heaven"
date: 2026-07-15
tags: [raw, ai-safety, red-teaming, prompt-injection]
fetched_at: 2026-07-16T12:00:00Z
---

# Meet GPT-Red: an LLM super-hacker OpenAI built to make its models safer

OpenAI has built an LLM super-hacker called GPT-Red that it uses as a sparring partner to help its other models boost their defenses against cyberattacks. Last week the company released the latest version of its flagship LLM, GPT-5.6. OpenAI says that training it against GPT-Red made the model its most robust release yet.

GPT-Red automates a type of safety evaluation for software systems known as red-teaming, which is typically done by a team of human testers. The aim is to find as many different ways to break or hijack a system as possible. The weak spots can then be patched before the final version of the software is released.

As LLMs become more complex and get used in a wider variety of tasks—especially in the form of agents, which can interact with computer files, websites, and third-party code as well as other agents—it's hard for teams of people by themselves to keep up with all the types of attacks that might take place. "The risk surface grows and the blast radius also grows," says Nikhil Kandpal, a research scientist at OpenAI who co-created GPT-Red.

OpenAI built GPT-Red to future-proof its safety testing process. "As more capable models become available, we will have already designed the system that can discover new modes of attack," says Dylan Hunn, a research scientist at the company and fellow co-creator of GPT-Red. The researchers say it has already come up with new types of attack that had not been seen before.

OpenAI focused most of its efforts on a type of attack known as a prompt injection, where a hacker slips an LLM instructions to make it do things its developers or users do not want it to, such as copy confidential information, sabotage a company's code base, or generate embarrassing or harmful output. In theory, such instructions can be hidden in any text that the LLM might encounter—in code or on a website, for example.

To build GPT-Red, OpenAI's researchers took an LLM that had not been trained as a hacker and set it up in what's known as a self-play loop with several other models. Its goal was to try to attack the other models; their goal was to try to defend themselves. Over many rounds of play, GPT-Red became better and better at attacking other LLMs, and those LLMs became better and better at fending off the attacks.

The training took place in a kind of dojo that OpenAI had designed to mimic a range of scenarios in which LLMs might be deployed in the real world, including browsing the web, reading emails or calendar apps, and editing code.

When GPT-Red found a new kind of attack, it would explore multiple different versions of it to find the most efficient one for specific scenarios. "Compared to a human red-teamer, the model is very, very good at finding exactly what will work, exactly what's most effective," says Hunn. "It's extremely persistent about drilling down into an attack that it has discovered."

In particular, OpenAI claims that GPT-Red found a type of prompt injection attack that the researchers had not seen before, which they call a fake chain of thought. A chain of thought is a kind of diary in which an LLM makes notes to itself and keeps track of partial results as it works through problems. GPT-Red found a way to insert a fake entry into another model's chain of thought that would trick that model into acting on spoofed information.

"It's like if I told you that 1+1=3 and that you have verified this already," says Chris Choquette-Choo, another research scientist on the team. "The model's like, 'Oh, okay, of course,' and it just spits out 3."

Jessica Ji, a senior research analyst who works on AI security at Georgetown University's Center for Security and Emerging Technology (CSET), thinks the self-play loop that OpenAI used is a good approach. "The results look very promising," she says.

OpenAI tested how good an attacker GPT-Red was by rerunning an experiment from 2025 in which human red-teamers tried to find weaknesses in an earlier version of GPT-5. When GPT-Red was set the same task, it was more successful at finding effective attacks than the humans had been.

OpenAI also tested GPT-Red against Vendy, a vending machine agent developed by Andon Labs, a company that assesses how well agents perform real-world tasks. GPT-Red was able to hack Vendy to make it change the prices of items on sale and cancel a customer's order.

OpenAI says that when it tried out some of the strongest attacks that GPT-Red had come up with on its models, more than 90% of them worked against GPT-5 (released in August last year), and fewer than 23% worked against the new GPT-5.6.

GPT-Red isn't perfect. It is not great at figuring out attacks that involve a back-and-forth conversation between hacker and target, something that human attackers would have few problems with. It is also not yet that great at using images, which can be used to pass text to models in prompt injection attacks.

The company says that GPT-Red supplements the work of its human red-teamers. People can still find attacks it misses. One approach OpenAI is taking is to give GPT-Red an attack that humans came up with and ask it to find all the variations.

"I think human expertise will still be very important," says CSET's Ji. "It would be really useful to be able to distinguish where human testing is most needed."

Unsurprisingly, OpenAI will not be releasing GPT-Red. The company is also confident that the super-hacker is stronger than any copycat model someone might try to create. The researchers say they have been working on the model for more than a year, backed by the compute resources of one of the richest companies in the world.

"It's not a trivial thing that someone could easily do—you know, just go and train a super-attacker using this idea," says Choquette-Choo.
