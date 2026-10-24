---
source: https://news.ycombinator.com/item?id=50218633
author: HN discussion (ext: reddit r/antiai)
date: 2026-10-24
fetched: 2026-10-24
type: hn-discussion
title: "Hacker reverses Samsung TV, finds on-board AI listening, OpenAI account suspended"
sha256: 94e06ba9e96cea3227da492e9378b7c346be4396fef2abedb1b6d01dfd87bae8
tags: [ai-privacy, samsung, openai]
---

# Hacker reverses Samsung TV, finds on-board AI listening OpenAI account suspended (HN 216pts)

  - [] ada-h00k: If OpenAI really banned him for that reason, that would be pretty stupid. If you can no longer use an LLM for reverse engineering without worrying about your account, that drastically reduces its value.
    - [] spockz: In my efforts to reverse engineer the LG firmware to validate Gamers Nexus claims, I got a warning very quickly. I appealed that quickly and successfully. Then I applied for daybreak blue and haven’t had any issues since. It also a matter of phrasing. Say what you want to achieve not how if it is approaching defensive or cyber stuff. Also state you are working on your own devices and software. (If
    - [] williamdclt: &gt; If you can no longer use an LLM for reverse engineering without worrying about your account, that drastically reduces its value ...for a niche of customers, from whom the revenue is probably entirely negligible to OpenAI. Not saying it&#x27;s right, ethical or anything like that, but it&#x27;s not &quot;stupid&quot;
  - [] tintor: This looks very bad on OpenAI. What is next? Power and water company suspending your account if your home and car are not streaming enough telemetry. I am glad that open models are closing on frontier.
    - [] technion: Claude is absurdly sensitive to anything that touches cyber, and threatens bans if it gets a whiff of a pentest going on. it wouldnt surprise me if openai had a similar approach. Yesterday I joked that claude gave me a cyber stop for asking how to make the anime girl video for an exploit, but it was a thing that happened. Meanwhile im trying to convince people around me that having grok nudify peo
    - [] alfiedotwtf: With Kimi K3.1 Pro, today WAS the day they actually caught up. I’ve been saying this for the past few months - once the inflection point happens (such as today), it’s only a matter of 2 years when American closed models won’t be able to catch up with Chinese open models
    - [] tosti: Bad on OpenAI? The account got suspended. This reflects horribly bad on Samsung!
  - [] 3abiton: This is again will be very funny race to watch. Right now you can fairly do lots of reverse enginnering or &quot;hacking&quot; with off the shelf Chinese models, and they are very capable (GLM3 for example) which can be run locally if you stomach the hardware. Tools like rea are also becoming more popular. If openai continues to be pedantic, they will lose the technical base given how close is the
    - [] kmac_: The company I work for has a plan B to switch to alternative, self-hosted models if providers pull off strange moves, such as drastic pricing changes. We have already switched from one provider to another once, and we do not want to get burned again. We do not reverse engineer, just regular development.
    - [] figmert: For the past few days I&#x27;ve been trying to use rea to reverse engineer my Samsung Galaxy Buds 4 Pro to get seamless functionality working outside of the Samsung ecosystem with no luck (the buds 4 pro require Samsung devices + a Samsung account for seamless to work, I only have a Galaxy phone + my macbook). I think we&#x27;re still far away from having something that works that well.
    - [] Roark66: Have you tried Qwen3.8-Flash-Next? I found it significantly better in anything I tested than GLM5.3-Flash, but the thing is you either use Alibaba cloud or you host it yourself (no lesser quant than unsloth 4.5 or mx4&#x2F;nvfp4 and kv no more quantized than int8).
  - [] Hugsun: I&#x27;m curious if someone has started cataloging these cases. These spying TVs seem like a common industry practice.
    - [] jeeva: I believe GamersNexus were talking about doing more exhaustive testing across different brands after their video on LG models specifically.
  - [] tkel: from his twitter account: &gt; if your samsung TV model doesnt have a microphone, it will look for connected devices with one, such as a soundbar or a connected bluetooth device. this gets shipped off to bixby.
    - [] throwa356262: Is this not the expected function when you use bixby? (Not saying people should use bixby mind you)
  - [] luma: Dog bark and baby crying detection are advertised features for SmartThings integrations. Door bell and door knocking are also included, this is surfaced directly if you hook the TV or sound bar into SmartThings.
    - [] pawelduda: I had to check this and it&#x27;s true. Not saying Samsung or 3rd parties don&#x27;t take advantage of any data they can collect, but the story the tweets tell is super biased against them. Here, the detection seems limited to specific pattens required for a particular feature.
  - [] Den_VR: The tile references on-board ai. “On-board ai” here is automatic content recognition. Imagine my disappointment
    - [] pprotas: AI is simply an if&#x2F;else statement in disguise, you didn’t know that?
    - [] ngcazz: way to miss the point.
  - [] znpy: so glad i bought a dumb tv. i remember going store to store in search of one. gg me, that was a smart move.
  - [] kjsingh: so is the hardware mic-off button on Samsung TV any good?
    - [] akmarinov: If we read the tweet - the TV then connects to whatever device it can like a home theater, other speakers and uses its microphone if it has one
  - [] MisterMunchkin: Remember guys, if they are reading it for wrongthink, they are reading it for industrial espionage. Anthropic and openAI just announced they’re spinning out competitors to their biggest customers… right after ingesting all of their IP and contracts. Do the math. (Or don’t, because they’ve been caught stealing math research)
    - [] ihrimech: Interesting. Could you share a link to this announce?
    - [] red75prime: &gt; because they’ve been caught stealing math research No. They haven&#x27;t been caught stealing. Tristan Buckmaster publicly expressed surprise that the OpenAI model has used the niche approach he pursued (with AI assistance). 10,000 agents exploring various approaches make it much less surprising.
  - [] anthk: No libre agents and LLM&#x27;s?
  - [] nickdothutton: This is why you buy a display panel and not a smart TV.
  - [] aussieguy1234: The AI in the TV was listening for dogs barking and babys crying, a gross invasion of privacy. Possibly this could have been for ad targeting purposes. With projects like REA, it&#x27;s going to get harder and harder for companies to get away with things like this. I&#x27;d love to see the major social media apps reverse engineered and analyzed in this way. I can only imagine the dodgy practices t
  - [] antirez: &quot;Why you bother about local AI? LOL with the $ you spend for &lt;insert hardware here&gt; you can buy 5 years of 20x account&quot;. Yeah. 5 years where you are told what you can do.
    - [] ThrowawayTestr: 5 years where you can get arrested if the AI tattles to the feds.
  - [] jck86: To what extend do these &quot;smart&quot; products state how, when and what data they are collecting and selling? Isn&#x27;t it high time for legislation that at least makes it clear on the box what kind of sensors and integrations it has and how bad the product is privacy wise? Also, shouldn&#x27;t corporate spying disguised as automated content recognition and classification be limited or outrig
    - [] chiengineer3: I have heard enough send 18 billion to Israel
    - [] thatsabadlook: They don&#x27;t care because of several reasons. 1. They get paid not to 2. They are told not to. Alot of this spying ends up producing valuable data for different agencies to purchase which otherwise they cannot legally obtain without a warrant. Sure some of it has some commercial value, but a lot of it is probably more valuable for domestic spy operations.
  - [] midtake: What a load of shit. Samsung TV always listening if you enable listening, why would they do this? &#x2F;s How dare they run a classifier locally on the TV, they should upload it uncut to Czechia like Amazon did with their ring cameras!
    - [] freecodeio: the point is the setting does nothing, now go back to your claude session
  - [] zkmon: Just don&#x27;t buy any tech home appliance that was made after 2022.
  - [] Geof25: Claude Code for coding and DeepSeek + opencode for reverse engineering at this point. DeepSeek will break the binary into code and Claude will search for problems. Now you have most of exploitation chain.
  - [] HelloUsername: Source: https:&#x2F;&#x2F;news.ycombinator.com&#x2F;item?id=50193579