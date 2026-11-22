---
title: "AI Supply Chain Security: What Canary Tokens Found | Dragos - Dragos"
url: https://www.dragos.com/blog/ai-supply-chain-security-canary-tokens
source: www.dragos.com
published: 2026-11-19
fetched_at: 2026-11-22
extraction: full
tags: [raw]
---

# AI Supply Chain Security: What Canary Tokens Found | Dragos - Dragos

Source: https://www.dragos.com/blog/ai-supply-chain-security-canary-tokens

AI Supply Chain Security: What Canary Tokens Found | Dragos - Dragos TALK TO AN EXPERT Menu TALK TO AN EXPERT Login Show Search Dragos has acquired NetRise and runZero, building the industry’s first end-to-end xOT cybersecurity platform. Read the blog → Close Blog Three breaches, endless leaks: Your AI supply chain needs canaries

Following inference data

Why does AI inference data matter?

How do AI routers expose your prompts?

Three compromised companies

Marketplace resellers stole customer prompts

Privacy settings and retention policies were ignored

How do canary tokens detect prompt leaks?

What we did about it

How can you protect your AI supply chain?

HD Moore, Chief Research Officer, will be regularly sharing work from the research team he leads at Dragos. Topics will include xOT, IT, LLMs, PQC, and more. Their findings will sharpen defenders’ understanding of exposures and vulnerabilities emerging across the threat landscape.

We sent nearly two million AI prompts containing unique, trackable secrets to AI providers, then watched where those secrets surfaced. What we found revealed security breaches, prompt theft, and widespread failures to protect customer data.

Over a five-month period from July through November 2026, we submitted approximately two million prompts containing unique URLs and canary token credentials to widely used AI services and monitored what happened after inference. Our investigation uncovered three significant findings:

Evidence of provider compromises. We observed activity indicating that data from at least three AI providers was exposed. Our seeded test prompts were used in attempts to access our controlled test systems and canary AWS accounts.

Unauthorized access to customer prompts by inference marketplace providers. Multiple resellers operating through an AI inference marketplace were able to view and retain customer prompts using standard logging capabilities, without exploiting a vulnerability or bypassing platform controls.

Failures in privacy and data-handling practices. We observed multiple cases in which providers appeared not to honor customer privacy settings or published policies. Examples included prompts submitted to U.S.-based providers being transmitted to Chinese AI organizations, unique URLs being accessed months after a single inference request, and one seeded link ultimately appearing in an internal company chat in China.

Following inference data

We wanted to understand what happens to inference data after it leaves the customer’s environment.

To answer that question, we created millions of unique canaries, including URLs and credentials that would never be used by legitimate systems. Any attempt to access those assets would indicate that someone, somewhere in the AI ecosystem had seen the original prompt.

The results exposed a fundamental disconnect between how AI services are marketed and how inference data is handled in practice.

Why does AI inference data matter?

Most folks picture AI inference as a question and a response. Text goes in, GPUs juggle some bits, and text comes back out. What complicates this is how the data is actually treated.

AI providers commonly store prompts and responses for operational, training, safety, abuse-monitoring, or business purposes. Depending on the provider, that data may be retained for days, months, or indefinitely. It may also traverse multiple organizations, including model developers, cloud operators, inference platforms, and third-party resellers.

The prompts and replies – the inference data itself – are often more valuable than the GPU resources used to process them. They frequently contain confidential source code, internal communications, strategic plans, customer information, credentials, and other sensitive business data.

How do AI routers expose your prompts?

AI routers work by offering a single API endpoint that forwards your request to a pool of available models, sometimes at different hosting providers, with unified billing. Routers are great at cost reduction and providing flexibility without managing multiple accounts and credentials. The path to the inference server often passes through more than one router before reaching another provider, and from there the specific server hosting the target model. There is risk in this process – every hop can see the entire prompt and response.

Some routers are open marketplaces where the seller with the lowest price gets the request. It’s common for sellers to offer AI inference at deep discounts, and they can do this by pooling requests through unmetered consumer-plan subscriptions or by finding other low-cost paths to the specific model (startup credits, etc.). In the shadier marketplaces, it’s also common to see inference that is billed to stolen AWS credentials or consumer API keys. If a seller wants to siphon customer request data, they can list popular models at the lowest price, route the traffic, pay the difference, and then collect the data from the platform logs.

These providers offer privacy controls – customers can set privacy flags at the account level, for a specific API key, or in each request. The strictest setting is known as Zero Data Retention (ZDR), which specifies that the prompt and response are not stored. The routers should only forward these requests to providers that offer the same controls. The reality is quite different – providers often ignore these settings, either intentionally or due to bugs in their processing flow, and prompts not covered by ZDR are fair game for resale into a massive ecosystem of buyers and sellers.

Three compromised companies

The most serious finding was also the most direct. We found attackers actively stealing data from three different hosting providers. Although our prompts were bait, they were processed along with real customer requests, and those were almost certainly copied too. The earliest incident dates back to the middle of July, and none of the three providers knew about their breach until we notified them.

The largest breach involved a couple hundred of our AWS keys. Each key was sent in exactly one request to one provider, all within a few short windows in late October, and every request we sent during those windows was stolen. Some of the stolen keys came from requests that the provider rejected before a model ever ran – this tells us that the attacker was copying requests at the provider’s front door, and not somewhere deeper in the inference stack. In the other two breaches, some of the stolen requests were marked as ZDR. A privacy flag doesn’t help when the attacker is already inside.

Once the attacker had our credentials, they followed a predictable path. First, they tested each key to see if it was live, in some cases within a few hours of our request. Next, they went looking for data, listing S3 buckets and searching Secrets Manager and Parameter Store. Finally, they tried enabling hosted models in AWS Bedrock, creating Bedrock API keys, and adding their own IAM users to keep access. In total, our bait keys were used for tens of thousands of AWS API calls.

Figure 1. One stolen AWS key. We seeded it on October 21, it was first used the next day, and it was still in use three weeks later. Names are pseudonyms and addresses are partly masked.

One adversary appears to have compromised two of these providers at the same time. Secrets that we sent to those two providers were used together, almost immediately, from a single rented server. The attacker’s tooling changed over the three weeks that we watched it – it started with a script pretending to be Chrome on Windows, moved to Boto3 running inside OrbStack, and later switched to the AWS CLI on Kali Linux.

On November 1, the same attacker added ARTEX, an LLM-driven penetration testing framework. In our case, ARTEX did very little – it made a handful of calls to confirm that keys the attacker already held were still live. Two of the user agents it sent, artex-agent and artex-judge-r121, don’t appear in any public indicator list that we could find, and are worth adding to your detections.

Figure 2. Tools that were used against our planted secrets, including the AI pentest agent (first row) and the Kali environment (aws-cli row).

The good news for defenders is that these tools tend to announce themselves – both Kali and ARTEX showed up in the user agent that AWS records in CloudTrail. The bad news is that this self-identification was only present in a small fraction of traffic.

Marketplace resellers stole customer prompts

The second finding didn’t require an exploit at all. The marketplace sellers that we caught only had to list a model at the lowest price, enable request logging, and wait. What stood out is how personal it was – these were individuals, working from what looked like home internet connections and personal computers, trying to break into our canary servers one login at a time.

In one case, we sent two prompts through a single seller’s offer. About a day and a half later, someone on a home broadband connection opened both secret URLs in a desktop browser and started guessing usernames at the login page. Prompts for the same model that went through a different seller were never touched, which tells us that the leak follows the seller and not the marketplace as a whole.

In another case, an attacker working from a Mac on a home broadband line in France took the passwords from two of our prompts and tried to log in as root over SSH, typing each attempt by hand. The same Mac later tested several of our AWS keys in a single session.

Figure 3. One of the root SSH attempts. The password from our prompt was used four times in two minutes, and the route trace shows the two routers that the prompt passed through.

Most of those keys had been sent through the marketplace, but one had gone to a completely different router. It turned out that this router was quietly forwarding some of its traffic to the marketplace – another example of an undisclosed hop.

Privacy settings and retention policies were ignored

The third finding is different from the first two, as nobody used a credential. Instead, the secret URLs in our prompts were scraped, repeatedly, and the git repositories they referenced were targeted for cloning – all by companies that were never supposed to see the prompt in the first place, and often in direct conflict with the privacy settings on the request.

The clearest example involves a Chinese AI lab. This lab’s systems fetched the secret URLs from more than half of the prompts that we sent to its models between July and October, including roughly two-thirds of the requests marked as “no data collection” or Zero Data Retention. The scraper typically showed up two or three days after the request.

This wasn’t limited to requests sent to the lab directly. Several U.S. hosting providers resell this lab’s models, and prompts sent to those providers triggered the exact same scraper – the prompts were flowing back to the lab. A customer who picked a U.S. provider specifically to keep their data in the U.S. didn’t get what they paid for. Later on, a git client on a different cloud started trying to clone the private repositories referenced in our prompts, but only for prompts that used this lab’s models.

The large U.S. providers have their own issues. One continued to crawl a secret URL more than two months after we used it in a single inference call to their search endpoint. Another runs a scraper that comes back for our URLs days after each request, regardless of which router we used to reach it.

Figure 4. One day of incidents, grouped by source network. The same scraper networks show up against prompts that we sent through several different routers.

The strangest incident involved a company chat. Twenty-four days after we sent a prompt to one Chinese provider, the secret link from that prompt was posted into a Feishu chat channel (Feishu is known as Lark outside of China). Within two minutes, the link was opened from three desktops and three phones in Beijing and Shanghai. Our disclosure to this provider only included the first eight characters of that link, so whoever shared it was reading from a stored copy of the full prompt, more than three weeks after the request was sent to a U.S.-based provider with the ZDR flag.

Figure 5. The secret link shared in a chat and then opened in the mobile app. The git client is the earlier clone attempt.

Zero Data Retention is supposed to mean something. In practice, these prompts were retained, shared with other companies, and read by people.

How do canary tokens detect prompt leaks?

A canary token is a secret that only exists in one place – if anyone ever uses it, you know that place has been exposed. We started in July by seeding prompts with Thinkst Canarytokens, and every request carried an AWS key, a DNS name, and a URL that had never been seen anywhere else. Tokens started firing within days, and the tokens from July are still firing today.

The proof-of-concept worked so well that it made sense to build a dedicated service just for seeding LLM prompts. This service generates a unique seed, and uses it to derive unique hostnames, URLs, and credentials for every prompt and then runs the services that those credentials point to – DNS, web, git, SSH, databases, mail, and a long tail of older protocols. The AWS keys are real keys tied to empty accounts with full logging. Every request that touches a token is tied back to the exact prompt, model, router, and privacy setting that carried it. Since each unique component can be tied back to its parent seed, we’re able to get precise timing and sequencing; we know what DNS server they use, how long it took to reply, and every piece of the inbound connections (TCP, TLS SNI, HTTP Host headers, URLs, credentials etc.).

Figure 6. The console overview, showing incidents and seeded prompts per day, split by the router that handled the prompt.

Canaries tell us that a prompt leaked, but not where in the chain, since a router typically reports a single upstream provider, and that provider is often just another router. To figure out who was really handling our requests, we built something like traceroute for AI inference. The first part is simple – we include an image URL in the request that points back to our servers, and every system that fetches it gives away an IP address, an HTTP client, and a timestamp.

The second part takes advantage of how these services are stacked. We send small, slightly broken requests, and since each router tends to wrap the error from the hop behind it in its own format, a single response can contain three or four nested “envelopes.” Matching each layer against a signature database gives us the list of hops, the software at each one, the network they use, and often the company operating it.

So far, we have traced about two thousand routes. Several hundred of those included a system that we couldn’t identify, and a handful sent our image to a company that wasn’t on the advertised path at all. The traces also turned up middle layers that the route never mentions – one marketplace seller quietly adds about a thousand hidden tokens to every prompt, and another fetches images through a shared consumer subscription account.

Figure 7. An example of LLM route tracing, showing a path from SurplusIntelligence to Anthropic. The OpenRouter hop was discovered by tracing and was not disclosed in the marketplace

What we did about it

Every incident is stored with its evidence – the original prompt, the route it took, every connection that followed, and our notes. The first incident was mid-July; the provider first thought this was a misconfiguration of internal tooling, then a problem with partner data processing, until the investigation uncovered evidence that the attacker had compromised their internal credentials too. This provider has still not publicly disclosed the incident and the stolen data continued to lead to attempted logins as of late October.

For the second batch of intrusions in late October, we reached out as soon as we confirmed that the data provided evidence of third-party access, and one of these providers has already published a preliminary security notice.

For the less severe issues like data sharing (but not credential abuse), we started notifying providers in early November. Each report included the list of stolen requests along with unique strings that they could search for in their own logs. We are now working with about a dozen providers and wouldn’t be surprised to see this expand.

Reactions have been mixed. The router that was forwarding traffic to the marketplace told us that they stopped, and several providers have responded and started their own investigations. On the other hand, stolen keys and secret URLs continue to be accessed, even months after the initial incident.

How can you protect your AI supply chain?

None of this means that you should stop using AI services. It does mean that where your prompts go is a decision, and if you don’t make it, the lowest price will make it for you. Keep in mind that a privacy flag only binds the first hop, and that AI agents will happily send whatever they can read, including credentials.

Host it yourself, if you can afford it. This is the only option where nobody else gets to read your prompts, but the hardware isn’t cheap. A Mac Studio with 512 GB of memory starts at $22,299, NVIDIA’s DGX Spark now costs $6,950, a DGX Station starts at about $105,000, and an eight-GPU B300 server lists for $570,000 or more. For most teams, this only makes sense for the most sensitive work.

Go directly to a first-tier provider. One company, one contract, and one privacy policy to read. This can still leak through data sharing agreements or a breach at the provider, but it is the smallest exposure you can buy.

Use routers with care. Pick the upstream providers yourself instead of accepting the default pool, and verify that your privacy settings actually change where your requests go. Stay away from reseller marketplaces – some of that capacity comes from stolen keys, and a few of these services only accept cryptocurrency for a reason.

Seed your own canaries. Add a fake credential to the context that your agents and pipelines already send and treat any use of it as an incident. A free Canarytoken from Thinkst is enough to get started today.

Enable secret filtering. Some providers offer settings that will automatically scrub known credential formats from prompt data. This can’t hurt, but it’s not a panacea – there is plenty of sensitive data in prompts that isn’t shaped like an API key.

This research effort felt a lot like what we do at Dragos with runZero; using small bits of data to provide a comprehensive view of networks from multiple perspectives. Would you like that kind of visibility into your own environment?

Start a runZero trial

PS. If you found this interesting, check out Lauren Proehl’s post, I leaked credentials on purpose for four months. Here’s who took them, and what they did next.

HD Moore HD Moore is a pioneer of the cybersecurity industry who has dedicated his career to vulnerability research, network discovery, and software development since the 1990s. He is most recognized for creating Metasploit and is a passionate advocate for open-source software and vulnerability disclosure. Table of Contents Following inference data

Why does AI inference data matter?

How do AI routers expose your prompts?

Three compromised companies

Marketplace resellers stole customer prompts

Privacy settings and retention policies were ignored

How do canary tokens detect prompt leaks?

What we did about it

How can you protect your AI supply chain?
