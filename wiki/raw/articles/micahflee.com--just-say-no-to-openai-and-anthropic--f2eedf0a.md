---
title: "Just say no to OpenAI and Anthropic"
url: "https://micahflee.com/just-say-no-to-openai-and-anthropic/"
fetched_at: 2026-10-12T10:10:59.539254+00:00
source: "micahflee.com"
tags: [blog, raw]
---

# Just say no to OpenAI and Anthropic

Source: https://micahflee.com/just-say-no-to-openai-and-anthropic/

I recently read
End Times Fascism and the Fight for the Living World
by Naomi Klein and Astra Taylor. It's an excellent book and I highly recommend that everyone read it. Tech oligarchs make up an important component of the end-times-fascist coalition. One thing that stood out to me, as a software and security engineer who finds LLMs to be extremely powerful, is that the American frontier labs are run by unhinged lunatics who genuinely believe they're creating the Machine God, that they're fine with burning down the world to bring about AGI, and that they believe with religious fervor that they're the only ones smart enough to safely control it. I already kind of knew this, but this book really made it sink in.
As much as the AI hype all around us pretends that OpenAI and Anthropic are unique and special, they're not. They're not the only companies doing this work. In fact, a lot of the open weight models are just about as good as the latest ChatGPT and Claude models, including for incredibly complex tasks like vulnerability research.
Unlike models from OpenAI and Anthropic, open weight models have major advantages:
It's possible to run them privately on your own hardware (if you can somehow get a computer with enough RAM)
You can use a provider like Tinfoil that relies on secure enclaves to run them privately (I talk about this in a bit more detail below)
If privacy isn't a huge concern, you can use any number of other providers, some of them quite affordable, and it's easy to switch so you're not locked into a single evil vendor
You can still use powerful LLMs without financially supporting deranged oligarchs who gamble with life on Earth so that they can always remain in power
ChatGPT and Claude will
never
be private
These companies only offer closed versions of their powerful models (despite the word "open" in "OpenAI"). You pay them for chat and/or API access, and they are allowed to look at everything you do.
They offer a checkbox so you can opt out of them using your data for training, but your chat sessions still aren't private. They have access to it all. They can look at it, share it with governments or companies, or do whatever they want. It's possible, likely even, that they won't use it for training if you've opted out, at least not right now. But do you really trust that long-term? Have they done anything to make anyone believe that they respect people's data?
OpenAI and Anthropic are corporate gatekeepers
Their models have strict guardrails, as anyone who's tried to use them for anything cybersecurity-related has no doubt noticed.
Every session has a cop agent reading your transcript over your shoulder, making sure you're not using it for hacking. If it thinks you might be, the cop agent stops your session from continuing. It's very strict, and false positives happen all the time. Of course, not everyone has the cop watching them.
Some people get access to the models with looser restrictions or with none at all. OpenAI has
Trusted Access for Cyber
and Anthropic has the
Cyber Verification Program
. To gain access to more capable, less policed versions of their models, individuals and companies need to apply and be approved by OpenAI and Anthropic. A lot of US cybersecurity companies get access. Almost certainly US military contractors do too, and probably any parts of the US government that want it.
While there's some merit in restricting powerful models, handing the ultimate power to decide who gets access to them to Sam Altman and Dario Amodei – with consultation from the Trump Administration, of course – is a terrible, undemocratic idea.
I think a better approach is to simply not put yourself in a situation where you rely on ChatGPT or Claude. Instead of begging corporate overlords for privileged access, it's better to spend your time figuring out how to get models like GLM-5.3 to meet your needs. And it's not hard. These models are good, with the added benefit that they don't have a cop watching over your shoulder!
Open weight models are impressive
So far, open weight models seem to be about four months behind the fancy proprietary models from OpenAI and Anthropic.
Four months is nothing.
I'm extremely impressed right now with GLM-5.3. There's plenty of data and benchmarks out there, but my vibes-based opinion from using it is that it's basically on par with Claude Opus 5.5 for software engineering.
I'm also impressed with GLM-5.3-Flash. This is similar to Claude Opus 4.8. It's much smaller and cheaper than GLM-5.3, and still incredibly capable. It's also actually feasible for an individual person to get hardware to run it, like if you can one day get your hands on a Mac Studio with 512GB of RAM.
GLM models are made by a Chinese company called Z.ai. While the models are impressive,
I don't recommend making an account directly with Z.ai
or sending them any of your data. Their coding harness ZCode (their version of Claude Code) was
recently caught silently uploading
local source code repos and sending them back to Alibaba Cloud without consent. Also, it's safe to assume that Chinese companies will share any data you provide to them with the Chinese government.
Other open weight models from Chinese companies that are impressive include the DeepSeek, Qwen, and Kimi families of models. It's perfectly fine, safe, and secure to use these open weight models. Just don't trust the companies themselves with your chat sessions.
Another frontier AI lab worth a look is
Mistral
. As a French company, it's the only big player that's not Chinese or American. They just released an open weight frontier model called Mistral Large 4, aka
Le Chonk
. I think it's quite a bit more reasonable to trust Mistral with your data compared to the Chinese or American companies.
Private inference with Tinfoil or Maple AI
It's possible to have private AI, even without hosting it locally yourself, using secure enclaves. These aren't perfect, but I do think they provide a very meaningful difference in privacy compared to the status quo mode, which is "the provider can access everything with no restrictions."
The company that's doing the most work here is
Tinfoil
. If you want to learn the details, read their
docs
on secure enclaves and remote attestation. Another company doing this is
Maple AI
– although, technically, Maple uses Tinfoil for inference in the background.
Both Tinfoil and Maple are good options. Tinfoil is cheaper, but Maple is more consumer-focused.
If you want a ChatGPT-like experience, where you can talk to a chatbot, have it look stuff up for you on the internet, give it access to docs to read or do stuff with, access it in a mobile app, etc., then I'd go with Maple. There's a small free plan and a Pro plan that costs $20/month.
If you want to do real
agentic coding
tasks like software engineering, reverse engineering, malware analysis, CTFs or pen tests, etc., then you should use Tinfoil instead. They charge by the token for private inference, so no monthly plan. GLM-5.3 currently costs $1.80 per 1M input tokens, $0.80 per 1M cached tokens, and $5.75 per 1M output tokens. You can use significantly fewer tokens if you choose the "low" reasoning level, and it's still very impressive.
Inference without the privacy
If you don't want to pay a premium for private inference from Tinfoil or Maple, but you still want to free yourself from OpenAI and Anthropic, there are tons of less-private options that are also very cheap.
One that I've been playing with is
OpenCode Go
. It costs $10/month for more than $10 worth of credits. This is an inference router, which basically means your API queries do something like this: your computer -> OpenCode Go API -> the actual inference provider. This means that both OpenCode Go and whatever backend provider they're using will have access to your session data. That said, the
privacy section
of their docs promises which models data won't be used for training (most of them) and what the data retention is (zero days for most, including all the GLM, Qwen, Kimi, and DeepSeek models). Of course, it's just a promise. Nothing technical guarantees it.
There are plenty of other cheap options out there for non-private inference, if you just want to experiment with powerful open weight models.
How I'm using these models
I've been using both Tinfoil and OpenCode Go, configured with my current harness of choice, OpenCode. I've been mostly using GLM-5.3 on low reasoning, with great results. (Things change so quickly with the open weight models, who knows what will be best six months from now.)
I use OpenCode Go inference for completely public work, like when I'm implementing something that's already open source.
I use Tinfoil for everything else.
I've only just started working this way, but so far, I think the open weight models can easily completely replace my use of ChatGPT and Claude, at a comparable or cheaper price, with the added benefit that they're far more private and there are far fewer guardrails.
