---
title: "smolmaxxing: I'm making LLMs work on small and old devices"
date: 2026-11-13
type: article
source: https://github.com/hyperionaidev/smolmaxxing/
sha256: a8abcfb81be8bce8e14585be766d5b5f8bd9eff86f7fe6c214de5a89b5cf09f6
---
GitHub - hyperionaidev/smolmaxxing: maxxing the ability to run different LLMs on the smallest devices possible · GitHub Skip to content Navigation Menu Sign in Products Platform GitHub Repository hosting, code review, and collaboration Copilot AI coding agent for tasks, projects, and automated work Build &amp; Ship Actions CI/CD and automation Code Quality Quality analysis, fixes, and enforcement Codespaces Cloud development environments Secure Code Security Vulnerability detection and remediation Secret Protection Secret scanning and leak prevention All Features Developers Learn Documentation Training Certifications Build Build with Copilot Customize Copilot Integrations Explore Trending repos GitHub Sponsors Developer articles Changelog Changelog Your source for the latest features, improvements, and fixes across GitHub products, all in one place. Businesses By Stage Enterprises Team Startups Nonprofits By Industry Healthcare Financial services Manufacturing Government See all industries Evaluate GitHub Why GitHub Customer Stories Business insights Trust Center Add-ons GitHub Advanced Security Enterprise-grade code security Copilot for business Enterprise-grade AI features Premium Support Enterprise-grade 24/7 support Resources Learn &amp; Connect Documentation Resource center Blog Events &amp; webinars Community Forum Customer Stories Integrations Support Customer support Training GitHub Status Company About Partners Changelog GitHub Universe GitHub Universe The event for developers, by developers — talks, workshops, and what’s next for GitHub. Pricing Search / Sign in Sign up Appearance settings You signed in with another tab or window. Reload to refresh your session. You signed out in another tab or window. Reload to refresh your session. You switched accounts on another tab or window. Reload to refresh your session. Dismiss alert {{ message }} hyperionaidev smolmaxxing Repository navigation Code Issues 2 ( 2 ) Pull requests Actions Projects Security and quality Insights More items smolmaxxing Public Notifications You must be signed in to change notification settings Fork 15 ( 15 ) Star 501 ( 501 ) You must be signed in to star a repository About maxxing the ability to run different LLMs on the smallest devices possible hyperion-ai.com/products/smolmaxxing Topics edge-ai llama-cpp llama-cpp-alternative llm local-llm local-llm-support on-device quantization quantization-algorithms Resources Readme MIT license Contributing Contributing Activity Custom properties Stars 501 stars Watchers 1 watching Forks 15 forks Report repository main Branches Tags Go to file Code Open more actions menu Latest commit History 46 Commits 46 Commits Folders and files Name Name Last commit message Last commit date .github/ ISSUE_TEMPLATE .github/ ISSUE_TEMPLATE assets assets bench bench data data docs docs ipad-air ipad-air patches patches screenshots screenshots tiny-llm-web tiny-llm-web tools tools tv-llm-ui tv-llm-ui zigcc zigcc .gitignore .gitignore CONTRIBUTING.md CONTRIBUTING.md EXPERIMENT.md EXPERIMENT.md LICENSE LICENSE README.md README.md View all files Repository files navigation README Contributing MIT license More items 🤏 smolmaxxing Run the biggest language model you can on the smallest hardware you own. TV boxes, old tablets, single-board computers and routers all have a CPU, some RAM and flash storage that sit idle most of the day. smolmaxxing finds the biggest model each of them can really run, then pushes it further with custom kernels, careful memory use and weights streamed from flash. Every number in this repo was measured on the device itself. Three devices so far 📺 Xiaomi TV Box S (3rd Gen) 📱 iPad Air (2013) 📞 OnePlus Nord CE 2 (2022) Chip Amlogic S7D, 4× Cortex-A55 Apple A7, 2 cores MediaTek Dimensity 900, 2× Cortex-A78 + 6× A55 RAM 1.9 GB (about 1 GB usable) 1 GB (about 700 MB usable) 7.4 GB (about 3 GB free) OS Android 14, no root iOS 12.5.7, jailbroken Android 13, no root Everyday model Qwen3.5-2B at 7.7 tok/s Bonsai-1.7B (1-bit) at 24-26 tok/s Qwen3.6-35B-A3B at 4.9-5.7 tok/s Biggest model Ling-mini-2.0, 16B, at 5.1 tok/s Ling-mini-2.0, 16B, at 2.6-4.5 tok/s Qwen3-Next-80B-A3B at 2.8 tok/s Full results docs/tv-box.md ipad-air/README.md docs/phone.md The TV box and the iPad run 8B and 16B mixture-of-experts models on about 1 GB of RAM, and the phone runs 35B and 80B ones with about 3 GB free. They all keep only part of each model in memory and read the rest from flash as it's needed. More devices (single-board computers, routers, more phones) are coming. The techniques aren't tied to one box: the 1-bit kernel needs only basic NEON, and the flash streaming works on any Linux or Android device with more model than RAM. Got a small device? Run a model on it and submit your numbers : we'll add them to the results. How it works All of it is a patch on llama.cpp . The main ideas: Kernels built for the chip. A 1-bit lookup-table kernel, repacked 2-bit and ternary formats for the Cortex-A55, and versions o

## HN discussion highlights (item 50468888, 390pts)

===== smolmaxxing (id=50468888, 390pts) I'm making LLMs work on small and old devices

[0] mrashad74: Recently I started this open source project at my AI company, where I&#x27;m trying to make LLMs working Now Reached 16B models running on iPad Air 1st gen and xiaomi tv box, both have less than 1GB of usable memory, and reached some decent speeds given the hardware. I&#x27;m open sourcing the effort done, kernels developed and results for everyone to re-produce and push more, also the modified models are on hugging face : https:&#x2F;&#x2F;huggingface.co&#x2F;hyperionaidev I want a more challen

[1] post-it: &gt; I want a more challenging device, what do you think? One of those vapes with a screen on it.

[2] Isamu: Aw man I would love to be able to use the crank to back up the agent dialogue, maybe make it branch forward in a different direction. Make the dialogue into a game https:&#x2F;&#x2F;play.date&#x2F; 

[1] shujito: perhaps the pi 1st&#x2F;2nd gen? I&#x27;d thought of the ESP32 devices but their RAM is too small

[2] gabucino: Pi 1 is too easy. My PicoLM [fork] already runs on it. It also runs on MS-DOS 80386 2MB RAM, so... And iPhone 1. And Digital UNIX.

[1] boricj: A PlayStation 2 dev kit (with 128 MiB of RAM instead of the standard 32 MiB). Between the VUs, the R5900&#x27;s SIMD (MMI), the GS and the I&#x2F;O buses (FireWire, Ethernet, IDE, Memory Cards...) to stream model weights, the smallest Bonsai models (or aggressively quantized Qwen3.5-0.8B) and some really cursed programming might just eke out something the PlayStation 2 has no business running.

[2] pcwalton: This would be fascinating. I&#x27;ve sometimes wondered how computing would have been different if we&#x27;d known how to build modern LLMs in the 2000s, despite the much poorer hardware (leaving aside how you could possibly train such a thing back then).

[2] WhiteDawn: Already done. Ofc you’ll be streaming the weights off the optical drive ;) https:&#x2F;&#x2F;github.com&#x2F;xaskasdf&#x2F;ps2-llm 

[1] Copenjin: The only challenge in that case is ram (512, cpu is fine), but I think you should try getting something usable on the raspberry pi zero. Once that&#x27;s done it means people(or startups) can get an edge LLM subsystem on their projects for the zero or boards with more ram.

[0] dava96: This is really cool man. I like this on going trend of resurrecting old tech with AI and this is yet another avenue to explore. I&#x27;d be interested in seeing some older flag ship mobile devices

[0] ForHackernews: This is great. I&#x27;ve recently been playing with repurposing some old thin clients as homelab Linux machines Not my site, but same idea: https:&#x2F;&#x2F;www.parkytowers.me.uk&#x2F;thin&#x2F; All this old&#x2F;obsolete gear is plenty capable when used with the right software.

[2] ForHackernews: Running a pihole, a WeeWx weather station, a NAS backup server, a wireguard VPN, Zot container registry.

[1] NortySpock: Funny, I use that exact website to find passively cooled hardware to use as a server. I did get Qwen3.5 0.8B working at 5 tokens per second on the iGPU of a Dell Wyse 7020. I mostly use it to complain to; I have not yet found an agentic task for it. But also the CPU does plenty of small services and terraria servers and such. https:&#x2F;&#x2F;nortyspock.github.io&#x2F;blog&#x2F;running-a-language-model-o... 

[0] jedbrooke: in a similar vein, somebody got tinystories LLM running on the nintendo wii, including gpu acceleration [0]. 0: https:&#x2F;&#x2F;github.com&#x2F;brysontang&#x2F;iiama2.c 

[1] mrashad74: this looks very interesting, it can&#x27;t run a real (read : working on some real tasks) LLM, yet, but it&#x27;s actually very interesting device.

[2] jedbrooke: Here’s another repo that might be interesting https:&#x2F;&#x2F;github.com&#x2F;slvDev&#x2F;esp32-ai It shows using Per Layer Embeddings to run models that normally take 100s of MB of ram run efficiently in just a few KB of ram and keeps most of the model on disk. It’s somewhat similar to MoE so it doesn’t stream in the whole model from flash for every token, but takes it even farther. If some of these devices have 1GB of ram and a few GB of disk there might be some interesting options here. I’v

[0] yjftsjthsd-h: It&#x27;s technically sweet regardless, so don&#x27;t take this as even a little bit of negative pushback, but I am curious what the utility of these small models is? Are they smart enough to be useful on practical tasks? What are people doing with them?

[1] sebazzz: Also curious on this. They are too dumb to use with tools and if you ask it how to bake a pancake you only get rubbish.

[2] mrashad74: I mostly agree today, but I&#x27;m trying to push for the future where smaller models are more capabable, and I believe it will happen + the fine tuned cases I mentioned in other commments. On other notes : there is no free lunch, you have to sacrifice something for the other

[1] gonzalohm: Not op but my opinion is that It doesn&#x27;t matter if it&#x27;s not currently useful. I think it&#x27;s important that the community focuses on this line of research because big companies will not. It&#x27;s in their best interest to make LLMs resource hungry

[2] p00ki3: Yeh; this. They see how GTA6 looks and know a hypothetical scenario like a future Nvidia 7000 series with 96GB VRAM and 512GB system RAM in everyone&#x27;s home means the entire tech, media, knowledge work labor system; the rich peoples social moat; evaporates. It&#x27;s all quite clearly collusion among a few dozen, hundred. No way their education&#x2F;experience or data analysis engines have not made them aware. They’re just used to Boomer and Silent Generation politicians blithely enabling th

[1] mrashad74: This is an interesting question, so the idea is, based on experience, fine tuned small models can do narrow tasks very well (my experience running models fine-tuned on customer data as low as 1-2B is very promising) also the goal is to find a breakthrough were instead of the line of work (which I respect) that tries to squeeze much bigger models into smaller hardware like strata and maya, I&#x27;m working backward to discover&#x2F;search for custom kernels and modifications till we exhaust the l

[2] yjftsjthsd-h: I&#x27;m told that qwen 3.8 27B is good enough for practical programming work, so if that&#x27;s doable then I could easily see the utility. Or... the biggest qwen I see here is Qwen3.5-2B; is that actually capable of programming or agentic work with code?

[2] rybosome: I find this compelling “merely” as an engineering challenge, but I’m curious if you’ve observed an actual practical benefit? By that I mean, have you found a case where a fine-tuned, small model is outperformed by stuffing a heavily tuned larger model in its place?

[1] MomsAVoxell: Speech recognition, speech generation. This alone is quite useful in small&#x2F;limited devices&#x2F;contexts. Realtime log parsing and summarization is another application I&#x27;ve seen for little LLM&#x27;s.. Basically, anywhere you&#x27;d use an LLM, but at much, much smaller scales of ontology.

[2] mrashad74: speech models are what I&#x27;m trying next because imagine a nice portable meeting transcription device that can hold around without internet and for NDA-ed meetings and so (with permission of course)

[1] vector_spaces: If you work in a highly regulated space subject to e.g. HIPAA, and you work with ancient on-prem systems within a slow moving and risk intolerant organization -- for instance, virtually every state run healthcare system in the US -- then these are all you can hope for. In these settings, data is insanely messy beyond your wildest nightmares and hidden away in free-text fields that small models like this are great at cleaning up, normalizing, parsing, categorizing, etc

[2] mrashad74: Agreed, and it&#x27;s a new use case to me because actually in the cases I had the clients were okay with getting GPUs and handling the data mess for us, but none of them requested fine tuning, I believe trying to fine tune will be insanely complex from a regulatory prepsective.

[0] Farmadupe2: For the last five months or so, opus and fable have both been able to do this task as a soneshot prompt. An inference engine is almost pure compute and to a first approximation the only operation your hardware needs to support to do llm inference is multiplication [the rest of an inference engine is &quot;some trig&quot;]. So to get any model working on $OLD_HARDWARE, the hardest part of the task is now sourcing the hardware itself and giving the agent ssh access -- a modern agent will be able t

[1] mrashad74: I agree with you, and I&#x27;m using claude and other models heavily, the idea is not in the soneshot - because actually as you see in the logs I posted on github, it took around 107 + 50-ish experiments to figure out which models to run which and push the speed. I&#x27;m treating it as a search algorithm project, where I develop the methdology and search for pushing the limit of devices and searching in a big space of possible kernels and so for what works for a specific hardware. so I&#x27;m l

[1] Julia_marry: So true, people think they can prompt AI, tell it to create something amazing and &quot;Novel&quot; so they can feel cool and bragg about it. Shame on such people.

[2] mrashad74: no one said it&#x27;s amazing or novel, it&#x27;s just a fun experiement I&#x27;m not selling this :) just out of curiousity to explore.

[2] zamadatix: It&#x27;s okay to share fun thoughts even if you haven&#x27;t put blood sweat and tears into them.

[1] gabucino: lol sure &quot;claudia slop me up some 600m, commit, push, make 500 pages of slopped README.md, github stars+++&quot; great, you should definitely do this, there will be absolutely no problems whatsoever and it&#x27;ll also run at peak speeds while of course being completely unusable because who wants to run a slopped 600m t. at 1200+ commits on my &quot;oneshot&quot;

[2] mrashad74: No one will run a slopped 600M or even 16B for anything serious today, the whole goal is to experiment, to push both limits of what can be done with the model, and the hardware itself. It&#x27;s fun times actually. And I think such experiments and others posted are both showcasing the limits people are pushing.

[1] mrashad74: as of now, it&#x27;s just for novelty and fun, without serious fine tuning on domain data, you can&#x27;t really do much with the smaller models.

[1] mrashad74: well, yes claude is doing that, and I&#x27;m directing it and building the experiments and direction only, I didn&#x27;t hide it at all :) Everyone is using LLMs now, so it&#x27;s acceptable to use it for a fun experiment too I believe.

[1] mrashad74: most of the problem is actually brute forcing, so I&#x27;m using a brute forcing machine and just giving it pointers to reduce the size of search space for tricks, still fun, nothing frontier I know, but it&#x27;s nice to see what we can do with our little brute forcing machines.

[2] hypfer: The fact that you&#x27;ve commented two things under the same comment kinda feels like it&#x27;s not your doing but the agents doing mrashad74 3 minutes ago | parent | next [–] most of the problem is actually brute forcing, so I&#x27;m using a brute forcing machine and just giving it pointers to reduce the size of search space for tricks, still fun, nothing frontier I know, but it&#x27;s nice to see what we can do with our little brute forcing machines. reply mrashad74 4 minutes ago | parent | p

[1] asdfman123: That&#x27;s programming in 2026. Right now, Claude it doing my job for me, but if it goes well enough I&#x27;m the one who&#x27;s going to be promoted.

[0] nico: &gt; Device #1 is a Xiaomi TV Box S (3rd Gen): Amlogic S7D, 4× Cortex-A55 @ 2.5 GHz, 1.9 GB of RAM (about 1 GB usable) Whoah!! A tv has almost 2GB of ram?! Does it need it to run Chrome or Electron? &#x2F;s Ouch

[0] nullstyle: This is the lord’s work right here. Models at the the intersection of small and useful — forthcoming models, admittedly— will be in the toolset that the next generation of poor kids will use to build a more egalitarian world.

[0] datadrivenangel: So does it make sense to try and run models on older 4gb GPUs? I assume the energy efficiency isn&#x27;t worth it?

[1] mrashad74: well, the whole idea honestly is curiousity about limits of hardware more than actual application today plus the idea that in the future people can run more capable models (in terms of capability @ small parameters) on such devices. It makes more practical sense today to just go into 4gb GPUs and many people are working on this already.. on my side of things, it&#x27;s more on the exploration side for now, until we see what good models get released that can use this capability. There are many pe

[1] ThatPlayer: How old is old? I keep a Gemma 4 e4b running on a Plex server&#x27;s GTX 1660 (so Turing hardware). It&#x27;s got 6GB of RAM though, so maybe try e2b on 4GB.

[0] nico: This is very cool. Love the trend of optimizing small models I’ve been working on small local models and it’s amazing how fast the tech has progressed A year ago, I was creating conversational characters by finetuning a qwen 2.5 0.5b param model, and it worked pretty well. But no reasoning or math capabilities, and still required some decent specs to run; could maybe do well enough in a beefy raspberry pi But now, I have a locally trained 6.5M param model that does reasoning, solves multi-step m

[1] mrashad74: A year ago 1B parameter models couldn&#x27;t do much, today with the correct harness and&#x2F;or fine-tuning they can do more or less serious work (not frontier tho). I believe in a 6-8 months it will get even better and my TV will be happy. I didn&#x27;t try fine tuning so small models honestly but looks interesitng to try.

[2] BoredomIsFun: Not sure about 1b but 2.5 years old gemma 2 2B was very capable and useful model I used for summarizing aricles then.

[1] Alpha3031: 6.5M! Impressive. Is it initialised or distilled from any base model or entirely from scratch? What kind of training data for the RAG and conversational chat specifically?

[2] nico: &gt; 6.5M! Impressive I&#x27;ve been surprised myself. For reference, it gets better ppl (and with faster training), than the nanogpt model from Karpathy&#x27;s tinyshakespeare tutorial, at smaller size (nanogpt is 10M params) Trained entirely from scratch. Which gets it pretty far in terms of basic conversational skills, especially when also trained on chat conversations The training sources are: 1. Google Synthetic PersonaChat 2. DailyDialog 3. SODA conversational data 4. Hand-written model-pe

[OK]
