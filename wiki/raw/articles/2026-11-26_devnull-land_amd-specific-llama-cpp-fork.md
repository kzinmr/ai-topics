---
title: "AMD-specific fork of llama.cpp"
source: "https://devnull.land/amd-specific-llama-cpp"
hn: "https://news.ycombinator.com/item?id=50657265"
collected: 2026-11-27
type: article
sha256: pending
---

# AMD-specific fork of llama.cpp

Source: https://devnull.land/amd-specific-llama-cpp
HN: https://news.ycombinator.com/item?id=50657265 (379 points)

## Article text (extracted)

AMD-specific fork of llama.cpp | devnull.land devnull.land devnull.land bits & bobs from the tech world bits & bobs from the tech world Blog Blog About About GitHub GitHub AMD-specific fork of llama.cpp 11/26/2026, 9:59:36 AM tl;dr — I recommend using llama-cpp-rdna-boosts if you have an AMD graphics card. It’s lean, and increased my token generation from 35 to 55 tokens/second, and my prefill from 700 to 1300 tokens per second. YMMV. As of November 2026, an explosion in the number of bespoke inference engines has taken place. Many of them take inspiration from the engines that enabled much of the LLM inference up 'til now: llama.cpp, SGLang, vLLM, etc. The rationale isn’t that those options are bad, but merely that they are generalist engines, optimized for no particular hardware and with a focus on broad compatibility. Others feel the development pace of those engines have slowed down, and with the help of LLMs, they can move faster on their own. Some examples of these new inference engines* are Strata, Basalt, RustingStrata, etc… These new forks generally all have a few things in common: They focus on a specific subset of models and/or hardware They use a frontier model to vibe-code the entire thing They chase ever-higher token generation speeds … and the results are stunning! Strata is able to run a heavily-quantized model of Qwen 3.8 Flash Next, a 180B parameter model , on a 16GB VRAM graphics card, and 16GB system RAM, and have it generate tokens at a surprisingly high rate. In and of itself those three things are not red flags (the second is concerning, of course, but it may be SOP in a year’s time — who knows!), but as these projects have evolved, that relentless chase toward higher token generation speeds has taken an unfortunate turn, in that the optimizations are less about hardware-specific changes, but more about changing how the model thinks so that it goes brrr faster. Strata specifically has taken to preferring to poll experts loaded in VRAM even if other experts (pushed to system RAM/disk) would have been normally chosen. This is just one example, but certainly not the last. That said, I was fortunate to stumble upon yet another project that promised improvements, delivered, and was more aligned with my software development philosophy. Enter llama-cpp-rdna-boosts . It is a repository that contains a minimal set of changes that you apply against a pinned commit of llama.cpp. It is in essence a fork, but one whose changeset is continually re-applied to newer versions of llama.cpp. It contains AMD-specific improvements that drastically improve prefill and token-generation speeds. I appreciate llama.cpp’s approach to software development. They are a stable base to branch off from. Contributions are vetted throughly and applied judiciously. ✅ The rdna-boosts repo is a set of small patches that are applied to base llama.cpp. Fewer moving parts mean fewer things to maintain ✅ The changes are (somewhat opaquely, it’s all straight Claudish 😬) outlined in the documentation, ensuring some degree of transparency. ✅ The setup If you have ROCm libraries installed on your system, you can build the image yourself. I didn’t want to mess with that, so I used the pre-built images published. podman pull ghcr.io/stew675/llama-cpp-rdna-boosts:server-rocm-10.1 This sets up an image that you can run sandboxed via podman to launch the inference server: podman run --rm -it \ --network=host \ --device /dev/kfd \ --device /dev/dri \ --group-add video \ -v "$HOME/models:/models" \ "ghcr.io/stew675/llama-cpp-rdna-boosts:server-rocm-10.1" \ My actual launch script passes a few additional flags, but those are the important lines. I imagine upgrading would be pulling a new image down, though I have not tried this yet. The numbers On my setup, an AMD R9700 connected to my laptop via an eGPU interface, this improved prefill and token generation rates when running ukisai/Swift-1.5-Qwen3.8-27B-GGUF (Q6_K_L) with MTP enabled: Before After Prefill ~700 t/s ~1300 t/s Token Generation ~35 t/s ~55 t/s Strata and its ilk were always promising the moon and it was never clear what steps they took to make that happen. I’m very much looking forward to what the rdna-boosts community come up with next. * It’s worth noting that between these two groups, vllm-radiance made an appearance, which was a fork of vLLM with AMD-specific patches. I tried this too, but the build steps were so onerous and vLLM so overbuilt for my specific use case (1 machine, 1 developer), that I abandoned it and went back to vanilla llama.cpp ← Back to all posts © devnull.land · powered by gists & express

## HN discussion highlights (item 50657265, 379pts)

# AMD-specific fork of llama.cpp | 377pts | julianlam

[pixelesque] I know it's not completely trivial to do this given how stochastic they are with normal (non-0-temperature) settings, but is anyone actually checking the output quality of the tokens with some of these optimisations, or just chasing pure speed like some of the projects at least appear to be doing?

[rsolva] Interesting! I have had Claude improve llama.cpp the last few days to get Inkling 2 Mini to fly on my 7900XTX, the improvement has been dramatic both for decode and prefill! https://forge.dmz.skyfritt.net/ruben/llama-inkling-2-mini

[skullone] I've been wondering what I can reasonably run on a 7800x3d with 6GB and a 7900xtx with I believe 12 or 24GB vram. Looks like AMD stuff might be back in the races?

[jakswa] Oh it's ruben! Thank you for publishing your work. I was randomly running "ruben llama" for a couple days :D And the article does a great job describing my situation lately -- I think I was earlier in your speed curves, and ended up finding a little more speed from Maya https://github.com/mw00/project-maya

[Sha1rholder] I heard that if Anthropic recognizes that it's machine learning jobs, they might deliberately poison the output.

[girvo] Which is interesting because Nvidia’s Hyperflare server for Q38FN is going down the “optimised for a few models and one bit of hardware” path

[jdewerd] Historically the threat was self-sabotage from AMD not sabotage from Nvidia. Back in the day, Nvidia won my business when their OpenCL reliably ran my code so much better than AMD's OpenCL (more speed on a "worse" card, fewer bugs, better error messages, no crashes) that I eventually gave in, sold my red cards, and payed the green tax so that I could have that experience all of the time. The fact that 3rd parties can now work around AMD's best efforts to duck up the software makes me genuinely b

[nikwen] I'm a llama.cpp maintainer (who does not work for NVIDIA). There's lots of work being done to support non-NVIDIA hardware in llama.cpp, including AMD hardware, and a lot of that work is being done by Hugging Face / NVIDIA employees. I haven't noticed any changes since the NVIDIA acquisition.

[julianlam] Any number of reasons, but likely they are not cross-compatible with their entire list of supported architectures, which means regressions for some. That in and of itself could be a dealbreaker.

[PaulKeeble] LLama.cpp is now the stable product that moves with intent and doesn't break things and largely isn't just taking anything the AI kicks out as a patch. They also have a tonne of legacy having been around for so long compared to the new engines that can throw a lot of the older models away and make software designed for the new architectures.

[WhyNotHugo] llama.cpp has al limit of 2 open PRs per user, but reviews can take months — even for relatively trivial bug fixes. I can imagine that trying to upstream extensive work would be excruciatingly slow.

[dofm] I saw some blurb a while ago that described llama.cpp as a “model zoo”, which is a great description of its utility and generality. In the last couple of days I have been playing with Erik Paperniuk’s M1 port of Inco’s Splash, which has completely transformed the speed of Qwen 3.8 27B and Inkling 2 Mini; it has essentially tripled the speed of the former and more than doubled the speed of the latter. This means the Qwen model is fully viable on an M1 Max, where before I had found it a bit of a w

[SparkyMcUnicorn] This might deserve a standalone post, but MTPLX is worth checking out. Youssof's goal is squeezing the most performance out of apple hardware, but not at the expense of model quality. I was testing all of the different projects, all different configs, and I could get some impressive tps numbers, but wasn't actually usable over longer sessions. MTPLX has been the most stable results for me, with acceptable speed/performance and not feeling like the model's capability was chopped. Definitely worth

[hypercube33] If I'm not mistaken there was/is an lm studio for strix halo. seems like it quit working but it was able to punch Qwen 3.6 as fast as the 8060s when it worked. There is also a llama fork for Ryzen AI and Radeon cards but I'm on mobile.
