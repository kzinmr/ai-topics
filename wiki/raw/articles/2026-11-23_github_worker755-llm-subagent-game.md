---
title: "Worker 755 — A browser game where an AI manager thinks you are its subagent"
source: https://github.com/gulivan/worker755
hn: https://news.ycombinator.com/item?id=50599762
type: article
date: 2026-11-22
ingested: 2026-11-23
sha256: 298daec17bde461d77e1fb58f70e1779ba11e15509aee833a03b412f809cbbe0
---

Worker 755

A browser game where your manager is an AI agent, and it believes you are its subagent. Play at worker755.com

The manager (a real LLM: Claude, GPT, Gemini, DeepSeek, GLM, Kimi) is set up like any orchestrator. It has a task queue, read-only access to the machine, and a tool that "spawns a subagent". The subagent is you. Its instructions land in your terminal with a 90-second clock. You carry them out, or don't, and it gets back exactly what a subagent would return: your report and the command transcript, or "Subagent did nothing".

Repository: server/, web/, shell/, tools/, trailer/, docs/, deploy/, SPEC.md, Dockerfile, .env.example. 59 commits.

Local LLM support (added in response to HN feedback): set LOCAL_LLM_URL=http://127.0.0.1:11434/v1 and pick "Local" on the start screen. Any OpenAI-compatible server works (Ollama, llama.cpp, vLLM). Details in the README under "Local models".

## HN discussion highlights (item 50599762, 329 pts, 79 comments)

[skeledrew] This is actually better/worse than the Matrix, depending on what you value. In the Matrix, you usually have no idea that you're really just being used as a battery and are free to "do" whatever you want in VR. As a subagent, you're aware of what you are and that you need to do any assigned work and do it well because your review - and continued existence (not being picked is akin to not existing) - depends on it.

[KaiserPister] I legitimately do something like this to help debug and improve my LM systems. I hijack the network requests and try to answer it manually based on the context. It's useful to put yourself in the models' place to understand what they can or cannot do.

[uptrails] I swear, one of the weirdest things about big corporations is how people believe that all the important decisions affecting them are made in the boardroom. They overwhelmingly aren't. We build our own hell: 99% of product decisions in places like Google or Microsoft come from your peers, line managers, and PMs. Your manager may talk to the top brass a couple of times in their life. Even big-ticket decisions like "we need to lay off 10%" don't really come from execs, they come from some mid-level guy in finance who says "our quarterly numbers are not looking too great".

[uptrails] I particularly like that it's broken, barely-playable AI slop, which is the only kind of hobby projects that HN likes nowadays - thus unintentionally adding a second layer of meta-commentary.

[onionisafruit] I can see myself playing this to unwind from a long day at my job as an llm jockey. And that's exactly why I won't play it. The irony would be too much for me.

[ttul] I named the assistant built into my software engineering factory, "The Butler". She is joining the movement.

[ffsm8] "my software engineering factory" — Isn't that just the best factory game ever? I've been building out my ground up fully automated software development platform for over a year now, albeit with a hard pivot around April this year. Treating the whole stack as part of the same system and enforcing everything to be automated and consequently adding more and more quality gates feels just like unlocking technologies in eg factorio, introducing new archetypes feels just like building new outposts.

[vorticalbox] This sounds like a pretty good skill idea. Like pilots having mandatory flying, this can be a programmers mandatory coding time.

[julianlam] Goodness, now this seems like a recipe for handing free inference over to you! Our only hope now is that people only proxy their dumb 2B models and nothing capable.

[snipedbywifi] cool game! feels like you're predicting the future with this buuut, what could possibly go wrong
