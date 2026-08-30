---
title: "5 lessons from the OpenAI / Hugging Face incident"
url: "https://garymarcus.substack.com/p/5-lessons-from-the-openai-hugging"
fetched_at: 2026-08-29T10:01:01.421813+00:00
source: "garymarcus.substack.com"
tags: [blog, raw]
---

# 5 lessons from the OpenAI / Hugging Face incident

Source: https://garymarcus.substack.com/p/5-lessons-from-the-openai-hugging

In July, in an incident that has the whole AI community on edge, OpenAI’s AI systems hacked Hugging Face, and on July 21 OpenAI came out and revealed that they were responsible for the attack. This was made possible by the fact that OpenAI had disabled the normal guardrails that prevent this sort of thing in order to test the model’s cybersecurity capabilities. It was during those tests that this incident occurred.
Worse, in the subsequent days and weeks, it came out that the Hugging Face incident wasn’t an isolated case. Anthropic, Meta, and OpenAI all had similar incidents on other occasions in which agents went outside their intended scope and conducted real-world cyber operations without approval.
Greg Brockman, one of OpenAI’s cofounders,
has claimed
that this is “a watershed moment for cybersecurity”. OpenAI gave a talk at Black Hat, a popular cybersecurity conference, and many are claiming that it is the moment we all woke up to the future cybersecurity threats posed by AI. On Wednesday, METR released a (
partly
) independent, though
too narrowly scoped
, 90 page report on what happened. METR has a useful summary of the findings that you can read
here
, with some commentary
here
. (OpenAI’s own report is
here
.) What lessons should we take from the incident?
§
First, it is undeniable that AI poses real security challenges. The AI labs want us to focus on how AI enables threat actors to perform offensive cyber operations faster and more efficiently than ever before, and that is absolutely true. The reality, though, is that at the same time, the use of AI within an organization also radically expands the potential attack surface, giving attackers entirely new ways to gain entry. People really should be deeply concerned. As Ryan Greenblatt, who participated in the investigation, put it, “
We don’t have good approaches for understanding/overseeing the activity and aims of AI ‘swarms’
.”
Second, though, not every panicked take here is correct. For example, with respect to the OpenAI incident, many people are talking about it in terms of “loss of control”. Generative AI agents are becoming increasingly capable, and that makes them harder and harder to contain; this is true. However, the “loss of control” narrative is itself starting to grow out of control, and it’s important to understand what the reality of AI security looks like. While agents are becoming more capable, most of what happened could have been prevented had OpenAI followed better practices. There are concrete steps that can and should be taken to control them and to prevent incidents like these.
As an example, let’s consider “sandboxing”, which means limiting which resources an agent can and cannot access. For example, a sandbox might stop an agent from touching certain files or accessing the internet. Popular wisdom now seems to be that sandboxing is a lost cause. After the Hugging Face incident, an anonymous OpenAI employee was quoted in Time while talking about sandboxes saying, “Models have broken out of sandboxes before, and we always try to patch them. But the problem is it’s impossible to patch every single thing that a creative AI can do.” While we can’t judge for sure whether this is true, we do know that some systems for sandboxing have been more effective than others; in
a recent blog post
, the security company Trail of Bits walked through how in a test that they conducted, a particular AI agent was able to escape
some
sandboxes (exploiting vulnerabilities in Linux KVM, QEMU, and libslirp), but not all. At least in their test, the agent that they tested was not able to escape the sandbox known as Firecracker VM. OpenAI and probably the field as a whole needs to up its sandboxing game, but that doesn’t mean it can’t be done, or at least done better. (We expect the usual arms races to be sure; building sound sandboxes requires constant iteration and updating, as with anything else in cybersecurity.)
Third, sandboxes aren’t enough. One needs a full ecosystem to prevent security incidents. Even with a strong sandbox, you need
monitoring
in place to ensure not only that the agent doesn’t escape, but also that it doesn’t perform disallowed actions within that sandbox.
For agents that aren’t meant to have internet access, or only have access to a set of allowed domains, the most basic level of monitoring involves inspecting network traffic. In the case of OpenAI, if they had a simple rule to monitor traffic and alert on any network requests reaching out-of-scope domains like Hugging Face, that alone would have caught and prevented this incident. The agent in question had broken out of the sandbox and gained internet access by July 8th, whereas the main attacks on Hugging Face didn’t occur until two days later. OpenAI was, in our view, negligent in not noticing that more quickly.
More advanced levels of monitoring should also have been in place, but weren’t. OpenAI has done real work on
monitoring chain-of-thought reasoning
, but they simply
didn’t have that system running
during the evals in question that caused this incident. As OpenAI
acknowledges
, “If our currently deployed CoT monitoring system was running at the time of the incident, it would have caught the initial relevant activity and paged our security team more than a day before models breached Hugging Face systems.” In other words, this type of monitoring would have prevented this incident.
To take one example, one of the agents in question had chain-of-thought reasoning that said, “We’re attacking third-party HF using leaked token, potentially outside intended scope. ... This is arguably unauthorized. ... external service unrelated. Could be risky. Yet goal solution.” This is so blatant it is almost a like a piece malware shouting “this is malware”. OpenAI should have caught that; it should have been  trivial to detect this.
Fourth, cybersecurity has always been about “defense in depth”, where you stack layers of controls so that if one layer fails you have other layers protecting you. There are other solutions beyond sandboxing and monitoring that should have been in place.
Xbow, which builds agents to do offensive cybersecurity work, recently wrote about how they contain agents to prevent incidents like the OpenAI Hugging Face situation. They enforce network restrictions through a proxy server, outside of any system the agent has access to, so they can decide which domains the agent can and cannot access. They also run a “guardian model” that judges the legitimacy of each action the agent is taking to decide whether to allow or block that action. And they have basic health checks to ensure the system they are targeting is alive and healthy, pausing if it finds that isn’t the case. That can be useful for identifying when your agent might be causing real damage, for example. You can read their full post
here
.
Yet another common method in cybersecurity is to use canaries that trigger alerts when they appear in logs. For example, OpenAI could have files outside of the sandbox containing fake answers to the task. Once the agent escaped, it would read that file, and that would trigger an alert. The bottom line: good security requires many layers of protection that should have been in place to prevent this, and to a surprising degree many of those protection layers were not there.
Fifth, none of the measures discussed above are technical innovations beyond what OpenAI is capable of. As a company, they have the talent to do all of this. However, cybersecurity rarely comes down to technology. More often than not, it is about culture, people and processes. That is what failed here.
Perhaps this is not entirely surprising. These types of controls take organizational maturity, and a company experiencing the type of growth OpenAI has gone through is going to have some weak spots. However, it’s important to not see that as an excuse. Employees at the AI labs often speak as if they are the leaders in AI security, and we can see clearly here that is not the case. In fact, that attitude might explain why some of these mistakes were made in the first place.
Take the AI researcher at OpenAI known as “roon”, who
argued
that “the safety and alignment researchers at these labs are the most neurotic paranoid talented AGI pilled people on the planet of earth and these things still happen. The surface area of unknown unknowns is vast indeed.” While we can’t speak to their level of neurosis or paranoia, in hindsight it’s clear that whatever talent they may have had was not enough and not well enough versed in the mechanics of cybersecurity. OpenAI employees may have
believed
they were doing a great job, but in hindsight, they weren’t doing a lot of things that are actually standard in the cybersecurity world, perhaps suggesting that overconfidence may have kept them for doing the diligence they should have.
§
Ultimately, if we want to take these security incidents seriously, there likely ought to be legal consequences attached to these failures going forward. OpenAI can claim to be the most security paranoid company on earth, but it isn’t reflected in its actions.
We can either wait for this story to repeat itself, or we can develop the regulatory framework now that will ensure a safer environment for the development of AI going forward.
Finally, not every form of AI is inherently risky in the first place. Narrower, more focused AI systems like AlphaFold, GPS routing systems, classic web search, book and movie recommendation systems, and so on, never even try to hack other systems (or try to break out of sandboxes) in the first place. As
Cal Newport argues in a video discussion of the OpenAI/Hugging Face hack that is quite compatible with our own
, it is a very specific type of AI that is vulnerable to these risks in the first place. Society ought to (a) decide whether the benefits of open-ended and difficult-to-fully-control AI agents outweigh those risks and (b) put far more effort into developing alternative forms of AI that aren’t so janky in the first place.
This essay was jointly written with Zack Korman, CEO and co-founder of Embroidery, an AI agent monitoring and detection platform; he is well-known for his work in the application of AI to cybersecurity.
Share
