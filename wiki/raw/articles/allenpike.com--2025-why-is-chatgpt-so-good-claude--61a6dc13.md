---
title: "Why is ChatGPT for Mac So Good?"
url: "https://allenpike.com/2025/why-is-chatgpt-so-good-claude/"
fetched_at: 2026-07-07T07:01:42.160324+00:00
source: "daringfireball.net"
tags: [blog, raw]
---

# Why is ChatGPT for Mac So Good?

Source: https://allenpike.com/2025/why-is-chatgpt-so-good-claude/

Claude, Copilot, and making a good desktop app.
This year, even as Anthropic, Google, and others have challenged OpenAI’s model performance crown, ChatGPT’s lead as an end-user product has only solidified. On the Dithering podcast
last week (paywalled)
, Ben Thompson called out an aspect of why this is:
I need someone to write the definitive article on why the ChatGPT Mac app is so good, and why everyone else is in dereliction of duty in doing these.
Gemini 3 is reportedly coming this week. […] And I’m looking forward to it. I expect it to be good. And it’s just going to have to be so astronomically good for me to not use ChatGPT, precisely because the [Mac] app is so useful.
A model is only as useful as its applications. As AI becomes multimodal and gets better at using tools, these interfaces are getting even more important – to the point that models’
apps now matter more than benchmarks
. And while every major LLM has a mobile app, only three have a Mac app: Copilot, Claude, and ChatGPT.
And of those, only one is truly good.
Hold on – we’re diving in.
The Apps
ChatGPT for Mac is a nice app. It’s well-maintained, stable, performant, and pleasant to use. Over the last year and a half, OpenAI has brought most new ChatGPT features to the Mac app on day one, and even launched new capabilities exclusively for Mac, like
Work with Apps
.
The app does a good job of following the platform conventions on Mac. That means buttons, text fields, and menus behave as they do in other Mac apps. While ChatGPT is imperfect on both  Mac and web, both platforms have the finish you would expect from a daily-use tool.
ChatGPT for Mac (left) vs. ChatGPT on the web (right).
Meanwhile, the Mac apps for Claude and Microsoft’s “365 Copilot” are simply websites residing in an app’s shell, like a digital hermit crab. 365 Copilot is effectively a build of the Edge browser that only loads
m365.cloud.microsoft
, while Claude loads their web UI using the ubiquitous Electron framework.
Claude.app: a website with window controls.
While the Claude web app works pretty well, it only takes a few minutes of clicking around Claude for Mac to find various app-specific UI bugs and bits of missing polish.
As just one example: Mac apps can typically be moved by dragging the top corner of the window. Claude supports this too, but not when you have a chat open?
Your viewer doesn’t support HTML5 video, but you [can see the video here](/images/2025/claude-drag-high.mp4).
A classic case of `-webkit-app-region: no-drag` over-application.
Unsurprisingly, the Microsoft 365 Copilot app is even worse, and Gemini doesn’t have a Mac app at all. The desktop has not been a focus for the major AI labs thus far.
The oddball here is the plain “Copilot” app, which is of course unrelated to the “365 Copilot” app other than sharing an icon, corporate parent, and name. Copilot for Mac is, it seems, a pared-down native Mac reproduction of the ChatGPT app with a bit of Microsoft UI flavor. It’s actually weirdly nice, although it’s missing enough features that it feels clearly behind ChatGPT and Claude.
Fascinatingly, the Copilot app doesn’t allow you to sign in with a work account. For work – the main purpose of a desktop app – you must use the janky 365 Copilot web app. While this dichotomy might be confusing, it’s a perfect illustration of the longstanding tension that’s made cross-platform the norm for business apps.
The Strategies
Cross-platform apps like Claude’s are, of course, cheaper to develop than native ones like OpenAI’s. But cost isn’t the most important tradeoff when these very well-capitalized companies decide whether to make their apps cross-platform. The biggest tradeoff is
between polished UX and coordinated featurefulness
.
ChatGPT has focused more on the vertical axis, Claude more on the horizontal.
It’s easier to get a polished app with native APIs, but at a certain scale separate apps make it hard to rapidly iterate a complex enterprise product while keeping it in sync on each platform, while also meeting your service and customer obligations. So for a consumer-facing app like ChatGPT or the no-modifier Copilot, it’s easier to go native. For companies that are, at their core, selling to enterprises, you get Electron apps.
This is not as bad as it sounds, because despite popular sentiment, Electron apps
can
be good apps. Sure, by default they’re janky web app shells. But with great care and attention and diligence and craft, they can be polished almost as well as native apps.
While they might not feel native, Electron apps like Superhuman, Figma, Cursor, and Linear are delightful. These apps are tools for work, and their teams invest in fixing rough edges, UI glitches, and squirrelly behaviour that might break users’ flow.
Meanwhile, ChatGPT, despite being built on native tech, has its share of problems. These range from the small (the Personalization settings pane currently has two back-arrows instead of one) to the hilarious.
At the end of the day, the ChatGPT app for Mac is good because they care. They have a product-led growth model that justifies spending the resources, an organizational priority on user experience, and a team that can execute on that mission.
Meanwhile, Anthropic’s been going hard on enterprise sales, so it’s not shocking they’ve neglected their desktop experience. It’s unlikely they have a big team of developers on the app who don’t care about these issues – they probably haven’t had many folks working on it at all.
Still, I wouldn’t count out the possibility of a change in course here. While mobile is king, desktop is still where work happens. While OpenAI has
acquired Sky
to double down on desktop, Google has long been all-in on the browser. That leaves Anthropic as the challenger on desktop, with their latest models begging to be paired with well-crafted apps.
While Anthropic could surprise everybody by dropping a native Mac app, I would bet against that. There’s a lot of headroom available to them just by investing in doing Electron well, mixing in bits of native code where needed, and hill-climbing from “website in shell” to “great app that happens to use web technology”.
Just as ChatGPT’s unexpected success woke OpenAI to the opportunities of being more product-centric, the breakout hit of Claude Code might warm Anthropic to the importance of investing in delightful tools. Last year they
brought on Mike Krieger as CPO
, who certainly seems like he could rally a team in this direction given the chance.
Until then, ChatGPT will reign supreme.
Update: Although I think ChatGPT for Mac has problems but is useful,
not everybody agrees
!
