---
title: "What if managing AIs felt like Minority Report?"
created: 2026-02-08
date_ingested: 2026-05-14
type: x_article
x_article_tweet_id: "2020599545206313171"
x_article_author: "Geoffrey Litt"
x_article_author_handle: "@geoffreylitt"
source: "https://x.com/geoffreylitt/status/2020599545206313171"
tags: [x-article]
---

Everyone's wondering: what is the right UI for managing fleets of AI agents? The obvious thing is to juggle chat threads—like a manager of humans. But I think we can do better.
As a thought experiment: what if managing your agents felt like Minority Report? You'd plug in and become one with the machine. The system would support fast high-bandwidth communication: using data viz to efficiently show you compressed views of vast amounts of information, while a combination of natural language and direct manipulation would let you efficiently express your intent to the computer. You'd feel in flow, not scatterbrained.
At first glance, it's tempting to conclude that this kind of "human in flow" UI is sadly a relic of the past. For example, many software engineers have rapidly gone from coding one task at a time in an IDE to managing many parallel agent chats. But I think it's possible that we could come full circle—as models get faster, and we design new information representations suited to higher levels of abstraction, perhaps we can find a new kind of flow.
Why managing AIs is different
As agents can do more on their own, we no longer need to babysit things as closely. So what do we do instead? The most obvious thing is to copy what managers of humans do: juggle a bunch of chat threads, and switch between them, helping when needed.
The problem is, it's hard to keep track of all the tasks, and hard to parse what's going on, when all you have are chats...
 
How might we think differently? Well, let's observe two big differences between humans and AIs:
In the long run, AI will be very fast. AI agents already work faster than people. Right now we're in an awkward phase where that's still often too slow to stay synchronously engaged with the task. But that is changing—consider, for example, @cursor_ai's Composer model, which works so fast that you don't even have time to task switch before it's done. Over time, more tasks will be doable at the speed of thought.
AI is great at status updates. People don't want to give their managers a status update every 10 seconds, but AIs will happily oblige. The chat transcript is in some sense the most direct status update possible, a direct feed of the agent's thoughts. But crucially, we can also design any kind of structured "zoomed-out" status updates we want: a progress bar, a confidence score, a diagram of the work.
These two differences open up a bigger design space. We don't need to be designing for massive multitasking. And we don't need to be wading through huge chat transcripts. What might we do instead?
The Minority Report UI
In the Minority Report UI (designed by @john_under), Tom Cruise stands in front of a huge floating display. He gestures and speaks to interact with the computer, fluidly traversing and reorganizing information on the fly to think through a problem.
 
This UI doesn't feel at all like "managing a team via chat". The connection feels far more direct and intimate—it's a "heads-up display" giving realtime information.
 
Throughput between human and computer is high in both directions. The big screen shows the user a ton of information at once. And a combination of gestures + voice provides high throughput input: voice for higher-level intent; gestures for precision control like rearranging windows or scrubbing video.
Everything feels very live and synchronous. There are no loading spinners. The user isn't multitasking; they are in "flow". It feels like the person and the computer are forming one symbiotic system.
In a sense, this UI might feel quite "traditional" and not very AI-pilled—the user is closely connected to the task, doing a lot of the work themselves. It's not "delegating".
But I think we can imagine a more AI-enabled version of this! We'd just have higher level primitives to work with. We'd be seeing zoomed-out views, and making massive amounts of work happen with the flick of a finger.
Glimpses of the future
OK, so that's pretty vague... what might this actually look like? I don't claim to know the answer, but here are some small bits that I'm pondering.
Recently I (and many other people) been exploring what it feels like to visualize the progress of agents on a kanban board. Instead of a list of raw chat threads, you can see a live status and color code for each task, so you can see at a higher level how the work is going. As models speed up, you could imagine flinging tasks across the board live, rather than treating them as background async tasks.
 
I've also enjoyed following @Wattenberger 's explorations of agent orchestration, which include progress bars and a variety of zoomed-out, abstracted views of agent progress:
 
Another take on this problem is to imagine meta-interfaces that let you live tweak LLM outputs—perhaps by pre-generating many outputs that span a design space and letting you switch between them:
 
A related direction worth exploring to get around the latency limitations of current frontier models is hybrid approaches, where an AI produces traditional UI code that allows for arbitrary info viz + fast direct manipulation inputs. Like a chat that returns a spreadsheet, for example:
 
Similarly, I recently enjoyed seeing Claude Code Playgrounds, where LLMs create ephemeral (fast) UIs where humans can visualize and tinker on a problem together with Claude, again achieving higher bandwidth on both inputs and outputs than traditional code:
 
There's also the approach of directly surfing a latent space with direct manipulation controls; eg work on editing fonts with sliders for semantic dimensions by @michael_nielsen and Shan Carter:
 
IMO, none of these examples shows the whole picture, but they are all gesturing at an interesting idea. Even as we work in more abstract ways using AI, perhaps we can still take advantage of good, old ideas in user interfaces: 1) using information visualization to create compressed abstracted representations that people can use to think with, and then 2) using a combination of both natural language and direct manipulation inputs to achieve a sense of fast, fluid, precise control.
In other words, perhaps using AI could feel like Minority Report.
