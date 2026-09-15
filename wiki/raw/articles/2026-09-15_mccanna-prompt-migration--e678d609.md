---
source_url: https://patrickmccanna.net/notes-on-migrating-large-prompts-away-from-anthropic-openai-to-self-hosted-llms/
ingested: 2026-09-15
sha256: e678d6091ace6c478b31ac7301bde015fb29c875c6effd7c8851bc3ab26e2f37
---

Posted on September 13, 2026 September 14, 2026 by patrick Notes on migrating 35kb prompts away from Anthropic/OpenAI to Self-Hosted Ollama+opencode 

 edit: 

 I hope in some small way this post influenced this outcome. 

 Motivations: 

 Maybe you’re a Claude code/codex user diligently avoiding uploading personal data to LLM providers. Is it possible that the most valuable information isn’t your data- but the metadata about your sessions? The intuitions you apply in coming up with ways to coax the ai into solving problems might actually be special. It’s statistically improbable, but Claude might not be gaslighting you. It may be that you’ve actually got a real insight! Your agent sessions are transcripts of the hardest problems you work on. What would it cost you if someone had copies of them? 

 Last week there was public drama that shines a light on the risk that inference providers are training on user activity with the intent of delivering new discoveries. The mathematicians affected have published concerns about the ethics of frontier providers. If you missed it: https://www.theverge.com/ai-artificial-intelligence/991710/openai-navier-stokes-solution 

 When ‘EDR’ becomes Ethical Deflection and Refusal: 

 It’s become evident that the frontier providers are not only untrustworthy- but actively devious. If you want to protect your ideas, you cannot run inference on someone else’s hardware. It appears to be the case that everything you do with a frontier provider will get stolen. When a frontier provider talked through the navier-stokes equation situation with their lawyers, the best defensive strategy they came up with is “Cannot rule it out.” We can&#8217;t audit their retention or their training pipeline. Apparently neither can they. 

 These people should not be considered partners. They are pirates. If privacy matters, the only solution that enables verifiable protections is to operate your own hardware. 

 Hall Monitor as a Service 

 I am bewildered by OpenAI and Anthropic’s grandstanding on cybersecurity. They marvel at what they have wrought: AI beat their non-existent security controls. We are all in great ‘danger.’ Meanwhile, their llm “researchers” are running unsandboxed fleets of agents that appear to “spontaneously collaborate.” Somebody fetch me my fainting couch. 

 Frontier providers can afford advising from experienced security people. They almost certainly are paying some of them for perspective and leaving real cybersecurity guidance out of their public statements. All of this pearl clutching must be meant to solve a different problem than security. 

 The strongest & most accurate claim defenders can make about security is that we’ve found ways to make it &#8220;Pretty Hard&#8221; for attackers. This seems to result only when firms pay top dollar for the best talent in both exploit mitigation and exploit development. There’s rowdy but friendly competition between the defense and exploitation teams, and eventually you get controls that make successful attacks so expensive that they&#8217;re not worth doing. This is for the top tier companies in the country- although Microsoft seems like they’ve forgotten some lessons. The lion’s share of pentesting done for most enterprises is performed by security generalists. A very small subset are deep domain subject matter experts. Usually you get “good enough” security from that support. This isn’t the glamorous or mythical practice of cybersecurity you see in movies or tv. It’s looking for the known classes of predictable mistakes. The firms that make the big/smart investments with dedicated teams of experts discover and correct many new classes of mistakes before hackers do. 

 Everyone who begins learning exploitation hits a phase of exploitability grief about 3 month into dedicated, practiced study. They hack something they didn’t think they had the skill to break into and it terrifies them. They’re smart enough to know that, relatively speaking, they are an idiot, and if an idiot can do this then nothing is safe. That feeling is correct. It is also not a research finding. Some call this “imposter syndrome.” I disagree- that feeling is your first experience developing competence. Competence is knowing enough about a technical domain that you can distinguish what you know well from what you need to learn more about. 

 The Refusal Industrial Complex 

 To the LLM researchers learning and publishing about cybersecurity for the first time: 

 I’ve seen you admitting you’re not security experts. Please-when you’re hyperventilating about the cybersecurity existential threats, distinguish “exploitable” from “emergency.” Vulnerabilities are legion. Before Agents, vuln researchers needed insight to know where to look to find vulnerabilities. Vuln researchers needed perseverance and esoteric knowledge to exploit them. An agent did what you weren’t able to do. Thousands of researchers have been doing this work over the last 40+ years. Part of being knowledgable about cybersecurity is aware of the existence of shocking amounts of unexploited vulnerabilities. This is why frontier provider cybersecurity safety filters are so infuriating. You&#8217;re so worked up about the possibility of exploitation that you&#8217;ve implemented &#8220;ethical constraints&#8221; that prevent people from figuring out how to fix their systems. 

 Your safety filters prevent defenders from discovering vulnerabilities because doing so is “hacking” related. This damages defense, privacy and security for everyone. 

 We need models that aren’t averse to the C-word. It’s going to take a little time, but builders will eventually learn to secure their code with helpful exploitability-detection agents. They&#8217;ll invoke vuln discovery against their projects during software development and as part of CI/CD pipelines. That’s only possible with models that don’t safety refuse security testing. 

 BYOW: Bring Your Own Weights 

 Defenders need llms that discover security defects. They are intolerant of false positives- which means you need to prove exploitability of a vulnerability. Defending against hackers isn&#8217;t possible if you&#8217;re vague about what’s broken and what needs fixing. Frontier Providers need to loosen up, or people need to get serious about migrating to sovereign, self-hosted AI. I can&#8217;t force the former- but I can help with the latter. 

 I’m sharing my notes about my initial pass of experiments in transitioning stronger frontier prompts off of OpenAI/Anthropic and onto my local models. I’m trying to determine if I can rely on abliterated open weight 27b parameter models. My goal is to avoid cybersecurity refusals and protect my sessions from being snooped by arrogant frontier inference providers. 

 Notes on converting 35kb preprompts for use on ollama 

 Below are some observations about my experiences when I tried moving my most context-expensive agents to a self-hosted model: 

 Prompts that ran clean on a frontier API fell apart on my local hosted LLM. I have a 128 gig AMD Ryzen AI MAX+ 395. I have 32 gig allocated to the host OS, everything else is allocated to inference. 

 When you try to use the larger preprompts that work well on frontier providers, ollama starts to run out of fuel within 3 minutes. The agent thrashes on repeated tool calls, re-read files it had already read, rewrote finished work. The local model’s smaller size didn’t produce the problem. Self hosted systems have smaller context windows. The prompt, plus session history quickly exceeds the maximum context window for my self hosted system (65k tokens). Large prompts founder and thrash. On my system, a 35kb prompt immediately consumes 14% of total context window. It immediately jumps into second guessing the prompts with unnecessary tool calls and double reads of files. Context gets saturated within a few circles- and sometimes even before I get a response. With limited context window, the pre-prompt is basically briefing a man who is reincarnated every ninety seconds. It performs your last instructions without any awareness of the 15 preceding demands. Whoops! 

 SOP: Single Objective Prompting 

 But it’s not a dead end. You can tune your prompts to work within these constraints. Here are some things to think about if you’re going to start exploring moving Frontier Provider agents onto self hosted open weight systems. 

 You’ll need to explore splitting preprompts into single problem/resolution units, one objective each 

 creating agents in opencode is more declarative . You’ll need to store them in ~/.config/opencode/agents. If you were getting away with using Claude code to read files as a preprompt, you’re going to need to get more formal about defining your agents. This won’t be new for people building with anthropic SDKs. Some of you with shell scripts and direct invocations of Claude code may have been getting a lot of miles out scrappy agent constructions- opencode’s system prompt will need to be overcome through declarative agents. 

 You’ll need to familiarize yourself with opencode’s permissions . 

 You’ll need to tune context length explicitly in ollama. The context defaults in ollama are extremely small. 

 Your agents will need to log session state to disk to facilitate more frequent session handoffs. build agents that re-read only the slice they need 

 Work to reduce the number of tool calls per agentic step 

 Replace &#8220;don&#8217;t do X&#8221; with the positive directives: e.g. “only do Y” 

 MTTF: Mean Tokens To Forget 

 Here are some Failure Signals that indicate context exhaustion. Measure over time & Monitor for them in your logs: 

 Identical tool calls back to back 

 Multiple file reads on the same file 

 Agents restating their objectives 

 tool-call parse failures (Parsing tool call responses shoves so much raw data into context that it destroys sessions like a burst pipe at your dinner party). 

 High turn counts relative to file changes 

 TCO: Total Custody of Output 

 One of the biggest assets we get from Frontier Providers isn’t the model- it’s large context windows. They have the hardware necessary to support your inference. As a result, they get access to the session data. 

 You might not know that you’ve become dependent on large context windows. You may have thought the model got better, but in some part it’s that large context windows give the model more room for Chain of Thought. Chain of Thought enables the model to emulate reasoning and infer what your poorly constructed prompt is intended to produce. Larger context windows give agents lots of room to explore better alternative approaches to delivering your work. But it’s a Faustian bargain: you become dependent on frontier providers. Your inefficient prompts are by CoT you can’t read directly (Anthropic & OpenAI only provide summaries of CoT to the user) and it only works with large context windows. You don’t even know that there are problems in your prompts when this is happening. With fat context and CoT, even bad prompts produce good results. Thank you OpenAI & Anthropic. That’s been valuable. 

 But they ruin it! The frontier providers are so unrelentingly greedy that they appear to be stealing the personal insights of their users. I’ve had suspicions about my session histories for over a year. The frontier providers seem to be like Smaug, lounging on a mountain of gold. You think they&#8217;re over there, doing their thing- and you&#8217;re safe- but they lose their minds when they see a coin in your hand. They lash out and take it because gold is beautiful and it’s the dragon’s incentive. They keep warning us that they&#8217;re dangerous. What threshold is left to be crossed before you start putting your efforts into becoming self hosted? 

 Related 

 Categories Uncategorized Tags LLMs , Security
