---
title: "Google AI Studio API has been unreliable for the past 2 weeks"
url: "https://martinalderson.com/posts/google-ai-studio-api-unreliable-for-two-weeks/?utm_source=rss&utm_medium=rss&utm_campaign=feed"
fetched_at: 2026-04-30T07:01:57.497658+00:00
source: "martinalderson.com"
tags: [blog, raw]
---

# Google AI Studio API has been unreliable for the past 2 weeks

Source: https://martinalderson.com/posts/google-ai-studio-api-unreliable-for-two-weeks/?utm_source=rss&utm_medium=rss&utm_campaign=feed

Something weird is going on with Google's Gemini via their AI studio API. I've been using it for a lot of random projects, with Flash 2.5 being a great model and it has a generous free tier - with the ability to not enable billing, so random side projects can't accidently run up an enormous bill.
I had noticed sporadic 503 "The model is overloaded. Please try again later." errors recently but didn't think too much of it. However, building an MVP on top of it for a more 'serious' use case (with billing enabled, I should add!) made me look a bit deeper.
The Transatlantic Timeout
I've noticed increasingly over the last month or two all of the providers start really struggling in the afternoon European time/morning Eastern. Usually when I hit issues, I check the clock and it's roughly 3pm UK time.
I suspect this is because everyone in Europe is working with LLMs, and when the US starts getting online there isn't enough capacity for both.  I'm coining this the "Transatlantic Timeout", in the spirit of
Simon Willison's "Lethal Trifecta".
I've noticed both Claude Code and Gemini's API gets
much
worse at this time in general.
Gemini has a real problem though - AI studio is just not working right, and frustratingly the
status page
isn't reporting it at all:
Looking into it more, we can see huge problems on OpenRouter's reliability graph especially on Pro:
Note that even overall OpenRouter requests are failing (the green line) - which is meaning a significant degradation in service.
OpenRouter can try and reroute requests between providers, and Gemini is available via two sets of infrastructure - AI Studio and Vertex- I'm not sure how much they overlap behind the scenes.
It's all went bananas?
To make matters worse, a lot of GitHub repos that Google is responsible for have had issues for 2 weeks with not much communication:
Gemini CLI GitHub Issue #7227
Python GenAI GitHub Issue #1373
Strangely, if you use Gemini CLI with a personal auth token, its pretty reliable (perhaps that is served via Vertex?).
The only thing I can think of is the degradation of service started happening when the new Nano Banana image generation API came out (roughly), so perhaps that's the underlying drain on resources.
Regardless - I really think Google (and all inference providers) need to do a better job at relaying issues like this on their status page.
My strong recommendation is to check OpenRouter until this situation improves and use that as a status page if you're having issues. OpenRouter's graphs and transparency are a real asset to the LLM community and I hope they continue to provide this data to everyone.
Hopefully Google can provide an update on what went wrong here. Obviously services can have problems, but the lack of transparent status pages really wastes a lot of time.
