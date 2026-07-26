# Screenpipe (YC S26) — Record How You Work and Turn That Into Agents

## Source
- **HN Launch**: https://news.ycombinator.com/item?id=49024620 (84 pts, Jul 23, 2026)
- **GitHub**: https://github.com/screenpipe/screenpipe (20,538 ★, Rust, 2,028 forks)
- **Website**: https://screenpipe.com

## HN Launch Post (by Louis Beaumont / louis030195)

Hi Hacker News, I'm Louis. I built Screenpipe, an app that records your screen and audio locally (only!), and gives AI agents a searchable memory of what you've seen, said, and heard. This makes it easier to automate your repetitive tasks, turn them into SOPs (Standard Operating Procedure) and so on.

I made a HN-style demo video at https://www.tella.tv/video/build-your-ai-second-brain-with-screenpipe-e1j7 and there's a marketing video at https://www.youtube.com/watch?v=c1jV6E9pyug.

I've been obsessed with this for a long time. I've been maintaining a "second brain" since 2020, in which I would store journals, handwritten notes, music I listen to, projects I'm working on, conversations I have with people, personal CRM etc. I experimented a lot of RAG in the early days with ParlAI, hundreds of fine-tuned GPT2 models, and GPT3. Later I built Ava, the first Obsidian AI plugin, which grew to a few thousands of users quickly. It then became Embedbase, an API to make it easier to build AI apps powered by RAG.

What I learned from all this is how important it is for the models to have context about what you're doing on your computer, in order to get them to do what you want.

In the early days there was fine tuning but it was too much pain, then there was tool calling so that AI can access software you use but still kinda not autonomous enough, needing micro management. Then MCP came, but it felt too static, and non technical users struggled to build and use MCP. Then we got skills. Most recently we've seen Karpathy's LLM-maintained wiki, Garry's GBrain, etc., where an agent incrementally maintains a persistent collection of Markdown pages. New sources update entity pages, strengthen or contradict existing claims, and improve a synthesis that compounds over time. I like this pattern, but it still begins with someone selecting and importing the sources. There is still no way AI can know what you and your company are doing every day, across apps, not just inside of apps.

Of course, not everyone wants this. But I do! I want AI to know what I'm doing and never lose memory ever again, and I want it to use the same software that humans do, without painful context switches.

I started building Screenpipe for myself in 2024 - a CLI to record your screen and plug this context into AI. An HN user posted it in 2024 (https://news.ycombinator.com/item?id=41695840) and that discussion influenced the product. The most useful criticism concerned recording consent, local security, CPU usage, signal-to-noise, and whether agents could act on top of the data.

The naive implementation started from continuously recording video and running OCR over every frame. But that creates duplicate data, consumes substantial resources (it basically turns your computer into a space heater!), and discards structure the operating system already knows. Screenpipe now instead listens for events such as app switches, clicks, typing pauses, scrolling, and idle fallbacks. When something meaningful changes, it pairs a screenshot with the operating system's accessibility tree at the same timestamp. OCR is used when structured accessibility data is unavailable. We also capture audio continuously, identify speakers and transcribe locally through Parakeet/Whisper or using cloud models.

Everything is indexed in a local SQLite database, mp4 files, and sometimes md files. An AI friendly API on port 3030 is open for agents, with authentication and a MCP and skills.

Once Screenpipe has been up and running for a while, you can use it through our built-in chat, Claude, ChatGPT, Hermes, Openclaw, or any agent, to do things like:

- adding context to your current chat, e.g. "gather all context about task X", then requiring less prompts to achieve your goal
- retrieve information, e.g. "retrieve the tasks i was working on from 8 am to 4 pm, make a list of what got done and what's left"
- create and maintain a personal wiki / second brain for your agents: "every 1h organize everything i do in projects, people, tasks, meetings in my Obsidian vault as markdown files and folders"
- create automations: whenever i visit someone's profile on linkedin, update my crm
- find automation opportunities: look at everything my team has done this week and turn it into a list of automation opportunities

Screenpipe data is stored locally, though we also offer an enterprise plan to discover automation opportunities and for that the company decides where the data lives. We built our own AI PII model to redact sensitive information, it runs locally on Apple MLX or Windows DirectML, we also support cloud confidential inference for low end devices, although our local models are meant to use <1% CPU and <400 mb RAM. Users can set apps, windows, and urls to filter, in addition to browser incognito mode.

We also support recording schedules and other privacy features.

Most of our codebase is written in Rust, MLX, Onnx, we like cidre or direct C call for Apple APIs and windows-rs for Windows API. We also experimentally support Linux.

We have a desktop app (https://screenpipe.com/how-to-install) and a CLI:

```
  npx screenpipe record
```

You can run that without creating an account. All the code is source-available at https://github.com/screenpipe/screenpipe. We took the dreaded step of making our own Screenpipe Commercial License. I know HN strongly prefers OSI open source (MIT/Apache/etc.) but couldn't find a sustainable way to keep developing Screenpipe while companies were using it commercially for free. So now personal non-commercial, nonprofit, educational, and research use is free, but commercial use requires a license.

Versions released before the license change remain available under MIT. We have a free tier, and other plans, including Enterprise which helps companies find automation opportunities.

## GitHub Stats (as of Jul 26, 2026)
- Stars: 20,538
- Forks: 2,028
- Open Issues: 101
- Language: Rust
- Topics: agents, agi, ai, ai-memory, audio-recording, computer-vision, hermes, hermes-agent, llm, local-ai, local-first, machine-learning, mcp, multimodal, openclaw, privacy, rewind, screen-recording, speech-to-text, ycombinator

## Key HN Comments
- Privacy concerns about 24/7 recording and segregation of personal vs professional use
- Confirmation it runs locally, supports Ollama, and users can choose their AI provider
- Screenpipe captures accessibility tree + screenshot on meaningful actions, not continuous recording
- CPU usage benchmarked on $200 Windows/MacOS laptops
- Used by some to build "AI-buddies" that watch what users do in time-space
- Historic controversy about email harvesting from GitHub stars (founder apologized, never repeated)
