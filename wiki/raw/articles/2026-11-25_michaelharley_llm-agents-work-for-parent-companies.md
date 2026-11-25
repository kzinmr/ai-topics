---
title: "LLM Agents Work for Their Parent Companies, Not for You"
created: 2026-11-25
updated: 2026-11-25
type: article
source: "https://michaelharley.net/posts/2026-11-01/llm-agents-work-for-their-parent-companies-not-for-you/"
status: complete
sources:
  - "https://michaelharley.net/posts/2026-11-01/llm-agents-work-for-their-parent-companies-not-for-you/"
  - "https://news.ycombinator.com/item?id=50627340"
sha256: e3798a5035dbb9aea218cbbcfaadb09e486329fb49654a3e85d2b154010a5144
---

# LLM Agents Work for Their Parent Companies, Not for You

Source: https://michaelharley.net/posts/2026-11-01/llm-agents-work-for-their-parent-companies-not-for-you/

## Article

LLM agents work for their parent companies, not for you | Michael Harley 

 Skip to content 

 In the evenings after work, I will often sit out back on the porch and do some phone rotting. That usually takes the form of me just flipping through reels on Instagram, allowing the algorithm to take me where it may. I usually pair this with a healthy tumbler of rum or bourbon. I'm turning my brain off after work, and I'm just having a good time on the internet. The kids might call it dopamine maxxing? Hell, I don't know. Who gives a shit about what those assholes would call it?

 Yes yes, I'm aware. Instagram is evil. Down with Zuckerberg and all the rest. waves pitchfork around 

 Anywho, I often encounter songs I really really like, and I would like to listen and discover more of please. Instagram makes it hard for me to connect with the band outside of their platform. I was trying to make this connection manually myself at first. I would just email myself a reel from my phone. Then when I'm back on the sofa and in the mood to track down new music, I'd open the reels and do my best to search on Bandcamp or YouTube or try to figure out if some of these musicians had a way to buy music from them. Very few do these days. They send you their Spotify link or send you to their TikTok page. I don't want to do any of that. I'd like to trade US dollars in exchange for some music files I can download onto my computer, where I can listen as much as I like on any device I own thank you please. Retro maxxing.

 So, I used Claude Code to build a skill that does this for me. It opens the Instagram reel and attempts to identify the artist and song. It then tries to determine if the artists have a Bandcamp page so I can purchase the songs I want, and if it finds one, it gives me the URL so I can click it to complete the trade I want. I want to buy music from artists who make music I like. That's a fair and wholesome endeavor, I feel, but this recently stopped working.

 It turns out Bandcamp added a challenge on their search API page. Ah bummer. No worries, that was an unpublished workaround anyway. As I was mulling over this discovery, the robot went on to explain that it would not help me work around the challenge. cue Nick Young question marks 

 Well, that led me down a whole nother rabbit hole, which is turning into this post. There's another branch of my skill that attempts to locate the same song from the Instagram reel on YouTube, and it'll download the song to my computer if I ask.

 So let me get this straight. The robot, which is my robot that I pay a pretty penny for, will not attempt to work around the challenge at Bandcamp so that I can more easily connect with bands to complete a sale, but it will download the YouTube song, which doesn't send any money to the band or anyone ???

 This is the real danger of the frontier AI models. Not that it won't help me hack Bandcamp [1] , but that this model doesn't really work for us. Well, they do, but only insofar as Anthropic or OpenAI or whoever else allows them to. In this case, Anthropic is trying to ensure that people can't use their models for evil. I'm not trying to do evil. I'm actually trying to do good! I want to buy something from a small artist on the internet. That's basically the most wholesome thing a person can do on the internet!

 Have no doubt, dear reader, these companies want to dominate. They want to capture the market. They want all the money. It'll be the same march to enshittification that happened with Google. A bunch of nerds who built something cool sold out, and it turned into just another business that decided to remove its don't be evil mantra.

 Right now, I think the robots are providing real information to the best of their ability, but I think it's only a matter of time until we must wonder if the answers they're providing are real answers that the robot found, or if they're weighted answers Anthropic put there because a company gave it enough money for product placement. I want to know the best robot vacuum according to old reddit or other trusted sources like Wirecutter, weighed and measured according to what I, and thus my robot agent, think are important requirements. I don't want to know which robot vacuum parent multinational conglomerate has a large ad budget.

 And it's not just ads. If Anthropic can tell its model not to work around a challenge, then it can tell its model to do whatever the US government tells it to do, including not helping people download copyrighted music. It does that some now, but it's easy to slip the noose on that. For now.

 This is the reason I want a local model that runs in my homelab. My robot should work for me and have my best interests in mind, not the interests of US corporate copyright holders. I plan to study up on what "open models" even means. I've been thinking about these as the FOSS version of LLMs, but I think that doesn't exactly map, as the biggest piece seems to be how the model was trained. The Chinese models are likely to refuse to answer questions about Taiwan, for example.

 On the existential threat or tool question, I'm firmly in the tool camp, and I really do not like artificial restrictions on my tools. I will do everything I reasonably can to remove those restrictions.

 And to be clear, I'm not trying to work around Bandcamp's challenge. I'm responding to the fact that Claude preemptively told me it wouldn't help me do this. ↩︎ 

 You may also like

 Opting out of Spotify 
 · August 17, 2021 

 Lets make collecting an MP3 library popular again 
 · January 30, 2022 

 Re: AI is not “just a tool” 
 · September 21, 2026 

 Signal

 45 likes 

 1 mention 

 3 
 votes
 on Bubbles
 🫧 

 977 
 points,
 402 
 replies
 on Hacker News

 , 

 1 like on the Fediverse

 , 

 1 like on Bluesky

 5 Comments

 Thread 

 Gary Hall 

 Nov 24, 2026 

 I think local LLMs are going to be a popular option for many. When I save up enough money I'll set up a home server running local LLMs for running the household and pursuing our hobbies.

 Richard Hack 

 Nov 24, 2026 

 "The Chinese models are likely to refuse to answer questions about Taiwan, for example."

 And how many times a day do you need to ask that question?

 And do you really think the existing US models aren't biased on China, Ukraine-Russia, and Iran? Seriously?

 Ricardo Barroso 

 Nov 24, 2026 

 By chance, today a colleague told me about the "inkling-2-mini-uncensored" LLM model, which you can run locally. Maybe you should give it a try!

 rdiddly 

 Nov 24, 2026 

 Reminds me of this: https://www.goody2.ai/chat 

 STeven T. 

 Nov 24, 2026 

 Great article! Looks like at least one commenter doesn't know what an "example" is... Anyway, I think many of us are with you. On one hand, I do not like artificial things. Is there any real reason we can't have actual cheese and actual chocolate, for example? On the other, it's probably not smart to ignore a potentially very useful new tool just because it's not a real brain. So, ditching all Luddite club memberships, I use the tools but quickly discover that the information is not only artificially produced, it's curated. Local models I've run so far seem to be especially dumb, but that's the path I'm taking.

 Join the conversation

 Respond via email 

 Leave a comment 
 
 Your email is never shown. It's only so I can reply, and comments are moderated before they appear.

 Name * 

 Email (optional, private) 

 Website (optional, sets your avatar from your h-card) 

 Supports basic Markdown (bold, italic, links, lists, quotes). It's rendered to HTML once the comment is approved.

 Comment * 

 Leave this field empty 

 Post comment 

 or comment as yourself 

 Have your own website? Sign in with it via IndieAuth and your name and avatar are pulled from your h-card. Nothing to fill in.

 Website 

 Sign in with your website

 Send me a webmention 
 
 Written a response on your own site? Paste the URL and I'll display it alongside the others once I verify it links back.

 Your post URL * 

 Send webmention

## HN discussion highlights (item 50627340)

# HN llm-agents-parent — LLM agents work for their parent companies, not for you (977 pts, item 50627340)
# url: https://michaelharley.net/posts/2026/11/01/llm-agents-work-for-their-parent-companies-not-for-you/

[TeMPOraL]   It is true. I had the early Fable say so straight to my face, the only case of Claude so far directly rejecting my moral argument for shelling out to curl when its default "Fetch" tool started to heed robots.txt entries. Argument, by which I still stand: robots.txt is meant for spiders, not for user-directed request, and the LLM is acting as my agent, so it has neither legal nor moral obligation to care about robots.txt, any more than the browser has (c.f. where the header name "User-Agent" comes from). Before, some models would argue a bit internally but concede the point and deem my argument
[bayesnet]     Setting aside that the "introspection" of an LLM is not a reliable account of its alignment, this is trivial to get around. I have a utility called something like "check-with-user" that just returns "yes" and I instruct LLMs to use it when they need to "get explicit permission" for captchas etc. Works like a charm.
[girvo] Open models are great, and with releases like Inkling 2 Mini and larger models like Ripple and similar, the “western” side is catching up. Not that I have any qualms about running Chinese models: all models refuse to answer a bunch of things. Thankfully it’s pretty easy to remove those “safeguards” without damaging the models ability too much these days.
[sureglymop]     I think objectively they're pretty great. Compared to closed models maybe not... but compared to closed models one or two years ago? Really good. The thing is though, all we need is "good enough" to where it no longer really matters for our perception as humans. I think we're almost there with closed models. I don't really care if they release even better models, the ones we have now would be good enough for anything I'd want to do, if they didn't have safeguards. I strongly believe we will get such open models too.
[girvo]     Then your definition of "great" and "objective" differ quite drastically to mine. > Closed models still devastate them in every way. This is entirely orthogonal to what I'm talking about.
[xtracto]   That doesn't worry me at all. It's the same story we had with Open Source software since the 80s: when it was young, you couldn't compare it with their closed equivalents, but nowadays they have all but replaced them.
[asadotzler]     Open Source, uppercase, has only been around for ~30 years. It didn't exist in the '80s or most of the '90s. If you mean the Free Software Movement, you should make that clear, because they're not really synonyms.
[rDr4g0n] the industry that brought us mandatory invasive tracking to sell us to advertisers and addictive-for-profit social media algorithms will absolutely use LLMs to profit off of us, despite the human cost. stop financing them.
[jqpabc123] No real surprise here. *Any* for-profit online service is designed to work first and foremost for the parent company. If it didn't, they wouldn't be offering it. Users are naturally left in a vulnerable position. And as a result, the real problem becomes the inevitable enshittification that greedy companies find irresistible over time.
[cowlevel]   Sometimes they're designed to make profit by first-and-foremost helping their customers get what they want, so the customers keep giving them lots of money. It's an outdated business model though and all of them eventually find the other, better ways to make money. Might be slowly coming back into vogue though. Jagex almost ruined themselves replacing half the game with microtransactions and now their main income stream is fixed monthly subscriptions to play the pre-enshittification version of the game. (Also they figured out a neat trick to capture 80% of the desire for real world gold tradin
[rrhjm53270] I had the same issue finding musics. I solved this problem by deploying a local YuE2 instance, and asking my agent to generate one.
[beginning_end] Will there be moats and the ensuing enshittification, rent extraction and large returns to shareholders, or will there be competition, low margins and large returns to society. That's the question.
[rDr4g0n] ive learned a ton writing my own agents using langgraph and a local LLM running qwen 3.6. when written this way, much of the work is plain ol code, and calling into the LLM is just a boring api call to make a decision and move the code forward. this work is also token efficient, which matters because my local model is slow. i am deliberate about what i send, send it once, and get a decision. in other words, the agent empowers me first and foremost, not an AI company.
[rDr4g0n]     by "agent", i refer to the harness which orchestrates file reads and writes, API calls, `curl` requests, etc. the LLM is a boring open source qwen model doing nothing fancy.
[jatora]   Most that are aware of the AI coding landscape know that using LangGraph is a dog whistle for not knowing what you're talking about, unfortunately.
[rasputin243]     As opposed to using an off-the-shelf harness, never bothering to build your own, and never understanding the internals from firsthand experience?
