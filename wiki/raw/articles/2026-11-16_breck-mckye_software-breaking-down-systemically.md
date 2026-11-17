---
source_url: https://www.breck-mckye.com/blog/2026/11/software-is-breaking-down-at-a-systemic-level/
ingested: 2026-11-17
sha256: acef01d736fa113d
hn_note: HN 372p https://news.ycombinator.com/item?id=50520866
---

Software is breaking down at a systemic level | Jimmy Breck-McKye

Jimmy Breck-McKye

 Blog 

 About 

 Software is breaking down at a systemic level 

 15 November 2026 

 opinion 

 software 

 ai 

Software hasn’t been working too well lately, has it?

This weekend we saw the double-whammy of a 2 day global Microsoft outage, then an FAA ground-stop that halted all flights in the United States.

Can you believe it’s only been 
four weeks
 since the 
PHP2Shell
 vulnerability? A critical exploit in PHP, powering an estimated 70% of the world’s websites, with sites taken completely offline as engineers frantically patched their systems.

And then there was the 
eMudhra fiasco
, where thousands of SSL certificates - the way we secure HTTPS websites and internet traffic - were compromised by a private key so weak, it was almost comical.

It’s like 2026 has been a year of hacks, outages, vulnerabilities and IT panics. What exactly is going on here?

You might be tempted to blame AI, and you wouldn’t be completely wrong. Artificial intelligence models are definitely a part of this. Even if companies like Microsoft don’t divulge whether broken systems were built with AI, we do know that hackers and researchers can now use AI technology to find complicated exploits in a matter of hours.

I work with AI heavily in my job. It’s tremendously powerful. It’s also corrosive if used unwisely.

But AI is both a cause and a symptom of the problem here. What we are seeing is software breaking down at a systemic level. This problem is insidious because it is not only the software itself that is broken, but the entire way we’ve come to build it.

What does it mean for a failure to be systemic?

Look at the recent crises in software reliability and you’ll notice they don’t share immediate causes - that we know of - yet they look uncannily 
similar
 to each other.

Microsoft

The Microsoft outage likely emerged from a 
network configuration failure
 that stopped MS datacenters communicating with each other. Exactly what happened next remains confidential, but it seems to have triggered a cascading failure where no service could be restored into a valid state long enough to bear traffic.

Reddit and Bluesky speculated that even MSFT engineers had no real handle on the complexity of this outage.

Microsoft have faced increasing criticism for the (un)reliability of their Azure platform. Back in March, ex-MSFT engineer Axel Rischin published this 
scathing criticism
:

Microsoft rushed Azure out of the gates under intense competitive pressure. Corners were cut. Fundamental principles of reliability and operational simplicity were quietly abandoned.

Instead of going back to the drawing board to tackle the growing technical debt, Microsoft relied on quick fixes: layers of automation running mitigation scripts, a growing team of on-call staff, and, when automation was not enough, manual repairs.

His article depicts a highly complex system made of low quality parts, where nobody can make sense of the whole picture.

The PHP event

On October 21st, security research firm Wiz 
proudly shared an exploit that could execute arbitrary code on any PHP website
. Called PHP2Shell, Wiz trumpeted the power of AI tools to achieve exploits far beyond the skills of human attackers.

It turns out the PHP runtime had hidden several complex memory bookkeeping bugs for over a decade. PHP is used extensively in e-commerce and most famously in WordPress, which was once the go-to for cheaply building simple websites.

The PHP2Shell writeup depicts an internet dependent on a long chain of dependencies, hiding vulnerabilities too complex for any human to identify.

Shai Hulud attack, May 2026

Most people outside of tech won’t have heard of this, but back in May we faced a crisis when an attacker compromised some important packages in the JavaScript ecosystem (NPM).

These packages used GitHub Actions to perform Continuous Integration (CI) - automated tests, releases, etc. - and had a crucial misconfiguration where anyone who forked their projects could insert compromised code back upstream.

When the next upstream CI build ran, it would retrieve libraries from a cache. The JavaScript package manager, NPM, allows these libraries to include scripts. They’re intended for housekeeping tasks, but here, they were used to hijack the projects’ secret tokens.

The JavaScript ecosystem has long been criticised for poor security. NPM projects are complicated chains of dependencies calling dependencies calling dependencies.

Any dependency may carry scripts. Any dependency author was just one slip away from allowing their code to be compromised - all they had to do was copy-paste the wrong code.

In other words: a highly complex system made of low quality parts, where a single error can compromise everything.

How we lost control

It wasn’t always like this. Only 12 years ago, tech was a different industry.

Building software was 
hard
. Computer programs comprise millions of tiny instructions, and turning these into a workable system is like constructing a watch by hand, with hundreds of interacting components. Except, unlike a watch, each computer program must do something completely new and different.

It was the most fun I’d had as an adult. It was as much an art as a science. You had to be able to hold everything in your head at once: visualise how all the tiny parts could be orchestrated into a cohesive whole. I recommend anyone the adventure of writing a computer program by hand.

But, it was less fun if you were a manager. Not many people can write computer programs well, and it’s very hard to scale human beings. Getting them to communicate without misunderstandings is hard. Many projects failed. You can find programmers who know how to manage the complexity, but they want to be paid lots of money.

Different movements attempted to solve the core problem. Some people thought that software development practices could help, like if you turned programming into highly structured templates of “best practices”. Or if you used management styles like SCRUM. But they only ever helped so much.

About ten years ago, two small revolutions happened in our industry, whilst the rest of the world paid little attention. They were cloud computing, and open source libraries.

Cloud computing was about substituting your hardware and infrastructure with virtualised infra you could rent from someone like Amazon Web Services. You could click a button in AWS and it was like a server just popped into existence by magic.

Companies loved Cloud because it allowed them to remove sysadmins and ops people from the equation. You didn’t have to wait for someone to actually go to a site and install a rack in a datacenter. The promise was that your software could 
move as fast as code
 and not long after, a movement called DevOps essentially ended up merging developers and ops.

And then, we had the Open Source boom.

It was always possible to reuse code from other places - programmers sharing snippets on forums or sites like StackOverflow - but when tools like NPM hit the scene in 2014, it really felt like a gamechanger. You could just add a line to your 
package.json
, hit 
npm install
 and - whoosh - now you could reuse code written by any stranger on the internet.

Teams loved NPM (and PyPi, Maven…) because now they didn’t have to solve any hard problems if someone else had solved it first. All of the little components in a program - the cogs and wheels in my watchmaker analogy - were once crafted by hand. Now you could get cogs and wheels and whole mechanisms, for free, forever.

This meant that the programmers could focus less on the details. Instead of figuring out the nitty gritty of, say, writing the code needed to check someone’s password, you could just ask NPM and friends to take care of it.

Open source was great because you had a small number of passionate, unpaid developers, building code that everyone else depended on. You could make millions of dollars from their code, and you didn’t even have to be particularly nice to them. (People weren’t)

But the cost was that everyone stopped knowing the details. You had to give away control. If an NPM package is compromised, or the author has an agenda, you’re in trouble.

The cultural change

Because there were fewer details to take care of, tech professionals began to lose their specialisms. You didn’t need a team of ops people, a team of backend developers, a team of mobile developers, a team of testers. You could flatten them into generalists.

This changed the balance of power between workers and management.

Imagine a building site where there is a plumber, a builder, and an electrician. If any one of them threatens to quit, you have a problem, because you need each of them to get the project done. Whereas if you can make everyone a mix of plumber-builder-electrician, they lose that leverage.

Whether you think that power imbalance is a bad thing may depend on your politics. But it had a slow effect of taking influence away from the people close to the work. They’re the ones able to raise the alarm when things start going wrong.

By 2016-17, there were signs that the superstructure of open source had weak points.

The 
left-pad incident
 was an early warning of where we were going. In the tangled web of the JavaScript ecosystem, with its myriad dependencies, one library author took down his packages in a legal conflict, and ended up breaking almost everyone else’s projects.

But largely we managed to make do. Even after the hiring and firing cycle of the post-pandemic era, and near misses like the 
XZ Utils backdoor
, technology managed 
mostly
 to remain stable - thanks to armies of diligent developers and ops folk across the globe.

And then AI came in

…And, yes, then AI.

A lot has been written about how AI systems are inherently non-deterministic, a kind of slot machine that only creates simulacra of work. Acting like a stochastic parrot, this argument goes, AI generated code will always be prone to hallucinations and bugs.

And there’s truth to that. But I think the danger in the 
present
 moment is the opposite. It’s not so much that the model outputs are crap and unreliable. They’re actually pretty good at doing what you ask them to do (though I suspect that mostly works because Anthropic and co heavily subsidise compute).

I think the real AI threat is 
decoherence
.

Kristen Maevyn wrote an essay named 
The Decoherence Trap
 which talks about a problem where the individual parts of a system may look fine in isolation, but don’t make sense as part of a larger system.

Decoherence: the accumulation of locally valid but mutually incompatible or redundant models within a system, such that the cost of change is dominated by translating among those models and preventing unintended side-effects.

Software engineers, as I’ve seen them working over the last year, have all but turned over all their work to AI agents. It started with small tasks like writing tests, functions, and individual components. But now it’s everything - not only the components, but the design, the orchestration, the whole concept.

Programming was the activity of translating ideas and intents from the messy human world into code so crystalline, so precise and pedantic, that even a 
computer
 could execute it. It was fundamentally the act of distilling complexity into order, making something real out of nothing.

This activity is rapidly dying. It no longer happens in most tech companies.

Most SWEs now are unable to tackle engineering problems without some form of AI assistance. That’s not because they’re incompetent - they just can’t keep on top of the complexity. Even if they could once, they now face a tsunami of AI generated code. This is affecting everyone, at all levels - we are all fighting the tide of small, incoherent changes that look rational in isolation but slowly lose sense as a whole.

Kristen writes:

Decoherence grows relative to the rate of change of a system, and it increases faster the more decoherent a system is, resulting in runaway exponential growth. It is not a new phenomenon, and humans have always countered it through carefully finding ways to do more with less, unifying disparate patterns and models into a cohesive whole. However, the widespread use of AI is currently producing it at a rate that is unsustainable.

A form of learned helplessness has emerged, along with a paradoxical false confidence, caused by the ways LLMs provide the illusion of work without actually forcing us to think through the details.

This de-skilling of software engineers only shifts the balance of power even further away from developers - who can no longer raise the alarm. At its worst, AI turns tech workers into “meat proxies” who spend their days massaging prompts and letting Claude figure out if the work is actually complete.

Systemic decay

It’s not just programmers. It’s the whole chain, top to bottom. Everyone is using AI, especially in big tech.

Claude generates code because the engineer wrote a prompt. The prompt comes from a ticket that was written with Claude. The project manager wrote the ticket based on a summary of a document, that was written by, and then summarised back, by Claude. The document uses statistics from a calculation, by Claude. The business is panicking about the stock market, and the stock market prioritises short term trends over long term engineering.

Does this sound accurate? It’s a caricature, but not by a lot.

I believe that tech companies risk losing their “organisational cognition”
 - their ability to think and respond as a coherent unit.

This is the real threat: a scenario where nothing in the system is done with intent, and nobody in the system has control. We generate complexity faster than we can tame it.

Look at the problems I’ve outlined. They are about systems of excessive complexity, made of parts that need to work perfectly or else everything falls apart. These parts are being individually corroded by corner-cutting, cost-cutting, overcomplication, over-reliance on uncompensated work and - I fear - helplessness amongst the people who build digital infrastructure.

What is at stake?

This is a threat to all of us. The tech industry is now critical to everyday life. It’s the software that controls your flights, your banking, your petrol pumps, your TV, your payroll. It’s what allows you to navigate roads and find your friends. It’s how you date and how you eat. It’s how you’re reading this.

Society has extended trust, too much trust, into technical systems that are now demonstrating systemic deterioration. I do not think society, government, or institutions are prepared for a world where the incidents and outages of 2026 become commonplace. They too are extending the chain of dependencies, assumptions, complexity and unwarranted trust. Each layer, each link in the chain is a new point of attack that can subvert everything on top of it.

The internet is at a breaking point. The software we build is not legible enough to bear the responsibility the world is giving it. We are telling ourselves the AI revolution is succeeding, precisely because of the rate at which we are generating complexity. The actual load-bearing parts of the ecosystem - open source, engineering-led judgement - are crumbling away.

I think we are only at the beginning of a very painful phase. This is not a blip, and it’s not an aberration - it’s the new normal.

Back to all posts

© 2026 Jimmy Breck-McKye. Built with Astro.