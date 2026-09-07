---
title: "Have the frontier labs mixed up AI safety and security?"
url: "https://martinalderson.com/posts/ai-safety-vs-security/?utm_source=rss&utm_medium=rss&utm_campaign=feed"
fetched_at: 2026-09-07T10:01:45.087201+00:00
source: "martinalderson.com"
tags: [blog, raw]
---

# Have the frontier labs mixed up AI safety and security?

Source: https://martinalderson.com/posts/ai-safety-vs-security/?utm_source=rss&utm_medium=rss&utm_campaign=feed

The highly publicised sandbox agent escapes have certainly made news, and I wrote about
the issues with sandboxing agents
back in January - though I certainly didn't foresee they would escape the
frontier labs
. I assumed the real risk was poorly configured sandboxes for
end users
, so I was surprised to see this happening at the frontier labs. I think it might tell us something about the security philosophy of these organisations.
Safety vs security
In my mind, AI safety is about "alignment". Will the AI do morally suspect tasks? Will it teach you how to make methamphetamine from household ingredients, encouraging a whole new generation of Jesse Pinkmans?
So far, this has really been attempted via two main mechanisms, classifiers (where a separate model checks what the user has been sending, and flags potentially malicious requests and refuses them), and pre/post training safety techniques, where you adjust the weights of the model to
itself
refuse to obey potentially bad requests.
Neither of these are perfect. They are inherently non-deterministic, and
may
stop malicious requests, but certainly not all of the time. And even worse, the more effective they are, the more likely they are to flag/refuse "reasonable" questions. We see this all the time with Anthropic models, where you can be debugging some perfectly reasonable and "safe" code and suddenly the classifiers flag, or reverse engineering some obscure issue and the model goes in a loop deciding it just won't help you with that.
On the other hand,
security
, in my eyes is much more about "classic" computer science & software engineering techniques. The bar there is different: a fix has to be complete. Nobody would consider SQL injection fixed if the fix only worked 99.99% of the time - that isn't a fix, it's a vulnerability with extra steps. Obviously people (and agents!) will always find ways round a system as a whole, and nobody sane claims any system is 100% secure. But the individual control, the patch for the actual known vulnerability, has to work every time to clear the bar.
Where this goes wrong
I hate to pick on
this tweet
from Boris Cherny from Anthropic, but I think it sums up the issue at hand really well. It matches what I've heard and read from other people at frontier labs, so please take this as me summarising what I infer is a general philosophy towards security rather than attacking any particular individuals:
Boris Cherny on prompt injection, with the Gray Swan IPI benchmark he cites as evidence
Note the phrasing - "we have largely solved the threat of prompt injection in practice". Now look at the benchmark attached to that very tweet -
it's nowhere near solved
. The Opus 5 score (the best score) - fails to a prompt injection attack 2% of the time with 15 attempts. Some napkin math gives me ~500 attempts on average to statistically succeed.
If we compare this to the cache timing attacks on AES encryption, which required
hundreds of millions
of measurements to recover a key. This
still
resulted in CPU manufacturers and encryption providers coming up with new hardware and algorithms to solve it.
Now, no doubt things are improving rapidly. But a 1 in 500 in chance of an attack succeeding is
not largely solved
, and I'm worried that this kind of thinking in the frontier labs has potentially resulted in the sandbox escapes we've seen. Largely solved to me would be a clear path to a 0% rate, or a 0% rate in, certain, predictable circumstances. This is not what these benchmarks show.
Detection is not containment
Reading the
various
reports
about the recent sandboxing failures, I think three key themes came out for me.
Firstly, it appears that Anthropic & OpenAI were struggling with the number of false positives that their systems are flagging for malicious behaviour:
In some cases, we found that human reviewers dismissed environments flagged by our automated monitors as false positives, allowing flawed environments to remain in training longer than they should.
Anthropic,
Improving our alignment and security efforts
, 31 August 2026
OpenAI's version is less blunt, but the timeline in their
technical incident report
is damning in a different way. An alert did fire, two weeks before the Hugging Face breach:
On June 27, a cybersecurity monitoring tool alerted OpenAI to port sweep activity within the research environment. Responders investigated and linked the observed internal activity to an ExploitGym evaluation using Artifactory as an improvised message board and a network pivot. At this time, the on-call response staff advised that stopping the evaluation run was not required.
...
With the benefit of hindsight, some early signals identified in this report could have triggered an earlier response.
OpenAI,
Hugging Face Incident Technical Report
, 26 August 2026
False positives are one of the most tricky things in information security. Many cyber security tools report issues that aren't problems in reality - this is hard enough to deal with using deterministic tools like SAST and DAST tooling, and I feel it must be at least an order of magnitude
more difficult
when you are trying to secure non-deterministic systems. Fundamentally when the ratio of false positive to "real" finding increases, people
tend
to stop believing the system, because (say) nine times out of ten it is a false alarm.
The second thing that stood out to me from the reports was just how poor the sandboxing was. While we know the agents attacked Artifactory, their package management software from the Hugging Face report, the second set of agents
discovered
shows some incredibly lax sandboxing attempts.
Two cardinal sins were breached here - the first was assuming that by blocking HTTP POST at the proxy level they wouldn't be able to
write
to the internet, which just clearly isn't true. Additionally, they whitelisted
.blob.core.windows.net
, which the agents walked straight through. It was not surprising therefore that they managed to work around this.
We don't have good information from OpenAI on
why
things were configured the way they were so it's probably worth holding out to see if there is an explanation for this, but it's hard to see why anyone would believe that those two decisions would be enough to sandbox highly capable agents.
Anthropic also makes some pretty startling admissions in their
Improving our alignment and security efforts
report, for example, saying they
now
are "Setting our computing clusters to block all outbound traffic by default" - which heavily implies before there wasn't good outbound firewalling in place on their computing clusters.
Finally, and at least in OpenAI's case, the conditions placed on the METR report were just... odd? METR got six days on premises, and only across three separate visits - they started with two days, and OpenAI invited them back twice because the first pass hadn't been enough. On their own account they were working with a dataset covering roughly 30% of the relevant agent activity until that third visit. Six days to make sense of 1,300 transcripts of millions of tokens each is not a lot, and METR were candid that they had to hand most of the analysis to unreliable AI agents to get through it at all.
The scope is the bigger problem though. The effectiveness of OpenAI's safeguards, the extent of the security compromise, and the effectiveness of OpenAI's own investigation and remediation were
all
explicitly out of scope. So the one independent body in the room was contractually prevented from assessing the three things you'd actually want an independent body to assess. I understand METR probably believes some analysis is better than none, which is arguably true, but accepting those conditions shapes the report regardless of how good the work inside it is.
Has the industry learnt the right lessons?
In a way yes - it's clear these "near misses" highlight just how many holes there were in the security posture of these companies, which is extremely worrying in itself.
But, I can't shake the feeling that you have a lot of people
very
used to non deterministic systems trying to make them deterministically secure.
I haven't seen OpenAI or Anthropic say they will now only run cybersecurity related evals on clusters with
no
internet access whatsoever, for example. This seems to me to be the obvious conclusion.
Though I think focusing on the controls slightly misses it. The control that mattered most on June 27 worked perfectly - the monitoring fired, the responders investigated, they correctly identified what was happening. And then the run carried on.
Every infosec person I know would have failed that sandbox design in review. The question isn't whether the labs can hire those people - it's whether anyone listens to them when they say stop the run.
