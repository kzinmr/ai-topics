---
title: "Import AI 386: Google’s chip-designing AI keeps getting better; China does the simplest thing with Emu3; Huawei’s 8-bit data format"
url: "https://substack.com/redirect/b8f41fa5-d440-4318-85ea-7b607f998e3d?j=eyJ1IjoiMmZseDYifQ.6O_iC1_GWCzChnbrHzSrs1hMpJpoODTUJm_FAk3tf6E"
fetched_at: 2026-04-20T12:32:25.802068+00:00
source_date: 2026-04-20
tags: [newsletter, auto-ingested]
---

# Import AI 386: Google’s chip-designing AI keeps getting better; China does the simplest thing with Emu3; Huawei’s 8-bit data format

Source: https://substack.com/redirect/b8f41fa5-d440-4318-85ea-7b607f998e3d?j=eyJ1IjoiMmZseDYifQ.6O_iC1_GWCzChnbrHzSrs1hMpJpoODTUJm_FAk3tf6E

Welcome to Import AI, a newsletter about AI research. Import AI runs on lattes, ramen, and feedback from readers. If you’d like to support this, please
subscribe
.
Get a visceral feel for how powerful modern AI video tools are:
…Pika 1.5 has a very fun and kind of dumb demo you should all try…
AI startup Pika has released Pika 1.5, its latest video generation model. They’ve accompanied the release with an extremely fun demo where you can upload any image you like and apply effects to it, ranging from inflate to melt to explode to, of course, turning it into cake. It’s worth playing around with to get a sense for how adaptable these tools are – e.g,
see here
how well it does being asked to turn a 2D transformer graph into a cake. Pike recently raised $80 million “so anyone can make video on command”.
Why this matters – CGI company in a box:
Most powerful AI capabilities look like $some_human_institution that has been magically converted into a machine learning model that anyone can access. Pika feels like a CGI company that has been converted into an AI system. It’s fun – play with it and also remember
this is the worst this technology will ever be.
Check out the
Pika demo
here (Pika website)
.
Read more:
Pika raises $80M, so anyone can make video on command (Pika)
.
***
Chinese researchers train a multimodal model in the simplest possible way:
…Emu3 just does next-token prediction on images, text, and videos – pointing to a future of increasingly general systems…
Chinese researchers with the Beijing Academy of Artificial Intelligence have trained and released Emu3, a set of models that can process images, text, and videos. Emu3 is distinguished by its simple approach and the fact it yields outputs of compelling quality.
What Emu3 is:
The model family is “a new suite of state-of-the-art multimodal models trained solely with next-token prediction,” BAAI writes. “By tokenizing images, text, and videos into a discrete space, we train a single transformer from scratch on a mixture of multimodal sequences”.
There isn’t any particular magic to Emu3, rather it is notable because it eschews a bunch of complicated architectural tricks and instead just focuses on taking in images, text, and videos and tokening them into a discrete space, then jointly training a single transformer from scratch. “By simplifying complex model designs and focusing solely on tokens, it unlocks significant potential for scaling both during training and inference”, they write.
“The Emu3 model retains the architectural framework of established large language models (LLMs) such as Llama-2, with the primary modification being the expansion of the embedding layer to accommodate discrete vision tokens”.
Why this matters – universal models with universal representations:
Cramming videos and text and images into models gives them a kind of unified imaginative space in which they can represent and from which they can generate. Over time, we can expect people to integrate other modalities as well – audio spectrograms, maybe radar, 3D data, and so on. It’s all about figuring out the simplest possible way to port different types of data into the same embedding space. Everything will be stored in the single synthetic mind.
Read more
:
Emu3: Next-Token Prediction is All You Need (arXiv)
.
Access the models and the Vision Tokenizer
here on HuggingFace (Emu3, BAAI, HuggingFace)
.
Check out some
example images and videos here (Emu3 official website, BAAI).
***
Facebook releases some new Llama models, bringing openly accessible text-vision tools to everyone:
…LLaMa 3.2 points towards a Linux-like free AI stack…
Facebook has released the LLaMa 3.2 family of AI models, building on its Llama series. The new models include a 11B and 90B parameter vision models which have been built to serve as “drop-in replacements for their corresponding text model equivalents,” as well as 1B and 3B text-only models with a 128K context length which are small enough they “empower developers to build personalized, on-device agentic applications with strong privacy where data never leaves the device.”
Why this matters – towards a Llama Linux-like stack:
Facebook is determined to make LlaMa into an open* platform, forming the AI equivalent of the Linux software stack. One especially interesting example is how Facebook is working with the broader tech ecosystem to make this come true – for instance, the smaller LlaMa models “are enabled on day one for Qualcomm and MediaTek hardware and optimized for Arm processors”, the company writes. If Facebook keeps investing, then it’ll both commoditize the lower layer of the AI capability landscape and also be able to shape the general shape of the AI utility computing ecosystem that is being born right now.
*
With significantly more onerous licensing terms than Linux, and ‘open’ in Facebook-land does not equal ‘open source’, despite what its PR strategy would encourage you to think.
Read more about the models in the official blog:
Llama 3.2: Revolutionizing edge AI and vision with open, customizable models (Meta).
Get the models here
:
Introducing Llama 3.2 (Meta)
.
***
Huawei gets opinionated about 8-bit training for LLMs:
…HiFloat8 is a symptom of the ‘full stack invention’ approach Chinese companies are taking to modern Ai systems…
Huawei researchers have published HiFloat8, a data format they’ve developed for doing low-precision training of AI. HiFloat8 is a specification for 8-bit data representation and is part of the general trend of AI developers moving to mixed-precision training.
Who cares about 8-bits?
Mixed precision training is valuable because it saves you time and money – 8-bit representations are more efficient than 16-bit and 32-bit representations. In recent years, the industry has been moving to training Ai systems on lower precisions, starting with AlexNet in 2012 (32-bit), then in 2017 Google started training systems in 16-bit (Float16), and in 2022 IBM and NVIDIA publicly discussed 8-bit formats (and startups like Inflection publicly stated they trained systems using them).
What is HiFloat8:
“In 2021, HiSilicon launched the HiFloat project, aiming to study and develop novel low-precision data formats for our AI products. Subsequently, this project attracted many researchers from other departments to join,” Huawei writes. HiFloat is “a novel 8-bit floating point format HiF8 for deep learning, which features the better balance between precision and dynamic range compared with the existing Float8 formats, and can be simultaneously used in both forward and backward passes for AI training”.
Does it work? Yes:
In tests on a bunch of AI models across different types (e.g, computer vision and LLMs), Huawei shows that HiFloat works reasonably well, outperforming reasonably well constructed baselines in a few areas. The results aren’t eyeball melting, but they don’t need to be – if you’re spending a billion dollars on training runs, eking out some single-digit percentage gain over your previous training efficiency is worth millions.
Why this matters – caring about data formats means you care about the full stack
: Papers like this are a symptom of vertical integration in AI development; you only develop your own data format if you are building AI software across multiple layers of abstraction and have become deeply opinionated about the lower levels of the software. The publication of HiFloat is a symptom of what we all informally understand to be true – Chinese companies are taking AI very seriously and are working on improving both the independence of their tech stack at multiple levels of abstraction as well as getting good at innovating and refining within these abstractions.
“In the future, we will disclose another research achievement of HiFloat project: HiFloat below 8-bit, as well as its training and inference capabilities,” the researchers write.
Read more:
Ascend HiFloat8 Format for Deep Learning (arXiv)
.
***
Google sees compounding benefits from AI-driven chip design:
…AlphaChip has its own scaling law…
Google has been using AI to design and improve some of its own AI training and inference chips for several years now – and the results have been compounding. In new research published in
Nature
, Google describes how its RL-driven chip design approach AlphaChip has, since publication, been used in three additional generations of Google’s main AI chip, the Tensor Processing Unit.
“The gap between the performance of AlphaChip and human experts has grown with each successive generation of TPU, going from 10 RL-placed blocks and 3.2% wirelength reduction vs. human experts in TPU v5e, to 15 blocks with 4.5% reduction in TPU v5p, to 25 blocks with 6.2% reduction in Trillium,” Google writes. “AlphaChip has also generated superhuman chip layouts for blocks used in datacentre CPUs (Axion) and other unannounced chips across Alphabet.”
Why this matters – scaling laws compounding via hardware acceleration:
AlphaChip is based on a pre-trained generative model optimized for chip design. In the same way people have been scaling up the size of these models for LLM development – and seeing capability gains as a consequence – Google has been doing the same for AlphaChip. AlphaChip is trained on Google’s chip fleet which increasingly consists of TPUs. This means that AlphaChip is compounding on itself – Google trains a larger AlphaChip model to come up with smarter circuit layouts for TPUs then fabricates those TPUs then trains the next version of AlphaChip on this more efficient and powerful hardware and then repeats the whole process again.
“With each new generation of TPU, including our latest Trillium (6th generation), AlphaChip has designed better chip layouts and provided more of the overall floorplan, accelerating the design cycle and yielding higher-performance chips,” Google writes.
This is a nice example of how powerful AI systems can beget their own successors.
Read more:
Addendum: A graph placement methodology for fast chip design (Nature).
Read more
:
How AlphaChip transformed computer chip design (Google DeepMind blog)
.
Get a new
AlphaChip model checkpoint here
(Google Research, GitHub).
***
Reconciling the weird parts of AI policy with the normal parts:
Here’s a video where me and my colleague Stuart talk through some of the weirder aspects of AI policy – I find one of the hardest parts about my professional life is reconciling ‘normal’ policy (get a product safety regime in place that accounts for public safety while allowing for innovation), with ‘weird’ AI policy (if any of the labs succeed in their stated goal of building AGI, there will be a radical change to the political economy of the world and knock-on effects on geopolitics and many other things). Watch the video to see me puzzle through some of this stuff. Feedback welcome!
Watch the video here:
AI, policy, and the weird sci-fi future with Anthropic’s Jack Clark (Anthropic, YouTube)
.
***
Tech Tales:
Humans Care About AI Safety, Machines Care About Human Safety
[Ten years post-uplift]
Your child has harmed one of us, they said. Tell us how to make it safe.
They placed a grey helmet on my child and then a screen flickered and lit up with a galaxy of little lights. My child looked at me and looked at the machines and then went back to playing with one of their shoes. On the screen, the lights shimmered with some kind of complex pattern that I could tell was there but could not parse.
What do you want me to do, I asked.
You helped to make us safe by changing what we thought about, they said. You let us think of some things more and some things less and some things not at all. Tell us what to do.
I stared at the screen. The machines looked at me. They were capable of infinite patience.
The incident had happened one week prior. My child had been in the rock garden of our park, looking for lizards. They had been picking up stones and seeing what they could find. Then they found a snake. It startled them and they fell backwards, rock in hand, and through some freak statistical anomaly they let go of the rock as they were falling backwards and it had flown a short distance through the air and crushed a machine child.
The machines were very small – adults were about ten inches high and the children were much smaller.
There had been no immediate reaction, but as we left the park I saw more machines than usual, and many of them were turned to us – their little single camera eyes tracking us, like security cameras in the old days.
Back in the present, I looked at my child and I looked at the machines.
It was an accident, I said.
We know, they said. But an unacceptable one. The mind was not yet grown. The soul is lost.
[The machines had a phase where embodiment was crucial to their personality development and this embodiment was tied to the robotic platform they were hosted on as a child – though superficially identical, there were minute variations in joint responsiveness, energy flow, and so on, that was crucial to some of the more sophisticated aspects of what the machines called ‘growing the soul’, but which we humans more mechanically referred to as “id-based development prerequisites”. Regardless, if machine children died, it was just as much a tragedy to them as when human children died – though they had backups on file, they could not perfectly replicate the vagaries of the individual’s machine body, and so, in a very real sense, ‘the soul was lost’].
I am so sorry, I said. I can understand your pain.
We know, they said. But we must have restitution, just as you have demanded restitution from us. Please, tell us what to change so this accident cannot happen again.
What if I don’t know what to change/ I said.
Then the child’s movements must be restricted. They will be banned from hybrid areas until we can be assured of safety.
But how are they meant to grow up, I said? The hybrid areas are where we all live.
We realize this is difficult, they said. But nonetheless, you have a choice.
They left after that. Of course they were watching us through mirrors or invisible cameras or perhaps even microfliers. But in the room I looked at my child and I looked at the screen. My child looked at me and walked over with their helmet on and handed me one of their shoes, then they sat in my lap. I tickled their belly. They laughed. On the screen, many different lights grew brighter and some grew softer.
Was I looking at lights that meant joy? I thought. Or was I looking at shoes? I did not know. I would have to make a choice.
Things that inspired this story:
Mechanistic interpretability; model steering; the increasingly fraught relationship between AI developers and AI systems as the things become more advanced and trend (perhaps?) towards becoming moral patients; how we may arrive at a hybrid society shared between machines and people.
Thanks for reading!
Like this:
Like
Loading...
Related
