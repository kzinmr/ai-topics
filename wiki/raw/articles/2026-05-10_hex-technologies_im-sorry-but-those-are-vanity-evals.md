---
title: "I'm sorry, but those are vanity evals | Hex "
source: "Hex Technologies Blog"
url: "https://hex.tech/blog/im-sorry-but-those-are-vanity-evals/"
scraped: "2026-05-10T01:29:02.123700+00:00"
lastmod: "2025-04-14"
type: "sitemap"
---

# I'm sorry, but those are vanity evals | Hex 

**Source**: [https://hex.tech/blog/im-sorry-but-those-are-vanity-evals/](https://hex.tech/blog/im-sorry-but-those-are-vanity-evals/)

Skip to main content
📊
AI analytics use case:
how Mercor unlocked $100M in revenue
🤖
Notebook Agent Act II:
AI tools for data people just got even better
🙏
It's just "Hex"!
Not "HEX" or "Hex dot tech"
🪄
Bringing the magic of AI to data:
agentic analytics tools that actually work
📖
State of Data Teams 2026
discover key insights from data leaders
📊
AI analytics use case:
how Mercor unlocked $100M in revenue
🤖
Notebook Agent Act II:
AI tools for data people just got even better
🙏
It's just "Hex"!
Not "HEX" or "Hex dot tech"
🪄
Bringing the magic of AI to data:
agentic analytics tools that actually work
📖
State of Data Teams 2026
discover key insights from data leaders
📊
AI analytics use case:
how Mercor unlocked $100M in revenue
🤖
Notebook Agent Act II:
AI tools for data people just got even better
🙏
It's just "Hex"!
Not "HEX" or "Hex dot tech"
🪄
Bringing the magic of AI to data:
agentic analytics tools that actually work
📖
State of Data Teams 2026
discover key insights from data leaders
📊
AI analytics use case:
how Mercor unlocked $100M in revenue
🤖
Notebook Agent Act II:
AI tools for data people just got even better
🙏
It's just "Hex"!
Not "HEX" or "Hex dot tech"
🪄
Bringing the magic of AI to data:
agentic analytics tools that actually work
📖
State of Data Teams 2026
discover key insights from data leaders
📊
AI analytics use case:
how Mercor unlocked $100M in revenue
🤖
Notebook Agent Act II:
AI tools for data people just got even better
🙏
It's just "Hex"!
Not "HEX" or "Hex dot tech"
🪄
Bringing the magic of AI to data:
agentic analytics tools that actually work
📖
State of Data Teams 2026
discover key insights from data leaders
📊
AI analytics use case:
how Mercor unlocked $100M in revenue
🤖
Notebook Agent Act II:
AI tools for data people just got even better
🙏
It's just "Hex"!
Not "HEX" or "Hex dot tech"
🪄
Bringing the magic of AI to data:
agentic analytics tools that actually work
📖
State of Data Teams 2026
discover key insights from data leaders
Platform
chevron-down
Products
Agentic notebooks
Powerful, deep-dive analysis without the silos
Conversational self-serve
The best BI tool isn't just a BI tool
semantic-models
Context Studio
Build trust in data with semantic models and AI governance
cli
Hex CLI
Control your analytics from the terminal
Capabilities
Exploratory analysis
Go from quick question to deep analysis to data app in one place
Embedded analytics
Ship secure, customer-facing data experiences
app-builder
Data apps
Build and share interactive dashboards and reporting
Integrations
Out-of-the-box connections and flexible APIs
magic
AI & agents
Agentic workflows to empower your entire team
Solutions
chevron-down
lightbulb
Explore all solutions
One connected system - infinite data answers
By team
solutions-data-leader
Data leader
Focus your team and scale answers
solutions-product
Product
Build your product with data, not gut feels
solutions-marketing
Marketing
Turn scattered data into clear growth opportunities
solutions-sales
Sales
Clear pipeline. Confident forecasts
solutions-customer-success
Customer success
Create a complete view of customer health
Enterprise
Resources
chevron-down
Get started
integrations
Switching to Hex
A guide to getting started on agentic analytics
Templates
Jumpstart with pre-built projects
Hex Foundations
Video series
help
Docs
Resources and product guides
Changelog
Product updates
Inspiration
Blog
From data teams to data teams
Guides
Learn how to do more with data, together
Events
Learn and connect with peers
Customer stories
Empowering the best data teams
Partners
Learn more about our partnerships
save
Download
The Data Leader's Guide to AI Analytics
A practical roadmap for understanding and implementing AI to accelerate your data team and enable true self-service.
Pricing
Log In
Get started
Blog
I'm sorry, but those are vanity evals
Using GPT-4.1 as a case study of our framework for impactful LLM evaluation
Izzy Miller
Engineering
April 14, 2025
Share:
twitter
linkedin
In this article
Eval pass rate is a vanity metric
Prompts are a blunt instrument
Funneling our way to clarity
Putting GPT-4.1 in the funnel
Flux
Orbit
Try this at home
Get started for free
A few weeks ago, we got early access to test an alpha version of
OpenAI’s GPT-4.1
on the extremely challenging private SQL evals that we use to develop our
Magic AI
features.
It
blew away the old 4o model, performing almost 2x better
by returning correct data for 50 more queries than the latest GPT-4o checkpoint. Nice!
it's a good model sir
This is where most eval stories end. You run the evals. You see how many passed. You make a slick chart benchmarking the new pass rate, pat yourself on the back, and move on. Or you make a change, re-run things, and look at the new number.
But what does that number really tell you?
Not much, in my opinion.
But don’t worry! In this post, we're going
way
beyond pass rate, using GPT-4.1 as a case study for the unique tools and philosophy that make our evals a continuous improvement lever for our product — not just a nice number on a dashboard.
Eval pass rate is a vanity metric
Why look beyond pass rate?
There’s a great article, “
I’m Sorry, But Those Are Vanity Metrics
,” where Lloyd Tabb explains the difference between
vanity metrics
— shallow numbers that are great for comparing yourself to others or winning marketing airtime — and
clarity metrics
— the “hidden gears that drive growth” and actually help you improve your product or run your business better.
Eval pass rate is a textbook vanity metric.
It fails the simplest vanity heuristic: it tells you something about the current state of the world, but absolutely nothing about how to
change
that state of the world. It’s just not actionable intelligence.
That isn't an inherently bad thing — these are great numbers to publish externally and use in marketing.
"Woah, Hex switched to GPT-4.1 and instantly doubled their success on an extremely challenging task?! I’m going to do that too!"
But you can’t rely on vanity metrics internally to lead you to your
own
growth unlocks or product improvements.
There's a new trend of measuring "pass@k" or "cons@k", where you run one eval 10 —
or maybe 8192
— times and see if
any
of the attempts succeed.
This is the vanity metric to end all vanity metrics! Every time I see this in an article, I'm
desperate
to know the details, and I really, really hope that internally, they're breaking out those aggregations.
Think about it this way: Your company’s AI engineers don’t spend most of their day changing model strings. That’s just step 0 in an infinitely-long process of tweaking, optimizing, reconfiguring, and otherwise tuning our systems to handle the new creature that’s been placed on our hamster wheel.
Done right, evals can become your biggest competitive advantage to do that tuning effectively and scientifically.
But try to do it with just pass rate as your guide, and you'll quickly run out of leads. Without granular feedback, you're not iterating—you're guessing. You make a change, check the number, and head back to the drawing board with no insight into what actually happened. That's not science.
Prompts are a blunt instrument
Good evals are doubly important because prompt engineering is an objectively silly, unscientific task. I think of it as a propaganda exercise more than engineering. How can I sway the model over to see the world the same way I do? How can I convince it to devote its life to the service of structurally consistent SQL queries?
One school of thought here is to shrug and say “if it works, it works!” You tell the LLM to think harder, promise it a $20 tip, check your pass rate, and move on.
But blunt instruments and vanity metrics are a
very
bad combination. My first draft of a prompt change usually boosts the overall pass rate, but also hides some subtle regressions behind that big green number.
The improved pass rate isn't
wrong
there, but it doesn't tell the whole story either. And when the changes we make are so blunt, and the systems so complex, we really need as much of the story as possible.
Funneling our way to clarity
So how do we go from vanity to clarity, and measure evals in a way that optimizes for growth and understanding?
Enter
“The Funnel.”
At Hex, we’ve developed a system that decomposes each eval from a binary outcome of pass/fail into a series of cascading steps, each with its own pass/fail criteria.
A sketch of the funnel concept. Below, we share detailed GPT-4.1 funnel results
For our most complex tasks, this approach increases our understanding of the system by an order of magnitude.
Here's how it works
Instead of asking, "Did the model write the correct query?", our SQL funnel asks:
Did our RAG (Retrieval Augmented Generation) system find the tables needed for the agent to write a correct query?
Did the agent hallucinate any non-existent tables in its query?
Did the agent choose the right tables from the set retrieved when writing the query?
Did the agent get confused and mismatch any columns to the wrong table?
Did the agent hallucinate any columns?
Did the query run without errors?
Did the query return the correct data?
We can evaluate, visualize, and inspect each one of these steps individually, so it’s obvious run-to-run if there are caveats to a change in the overall pass rate.
On our complex tasks, the funnel is 10 or even 15 stages long. On simpler ones, it’s just a few. But the methodology is always the same:
Decompose your task into as many meaningful steps as possible, and then order them very carefully such that each stage ‘masks’ the following stage completely.
For example, in our SQL gen funnel, it’s impossible for correct data to be returned (stage 9) if the query didn’t run without errors (stage 8), and it’s impossible for a query to run without errors if a non-existent column was used (stage 7).
This masking is critical, because it keeps you from chasing ghosts. Here’s an example.
A long time ago, before the funnel, we thought that we had a big hallucination problem. Hundreds of SQL evals were hallucinating columns and even tables that didn’t exist. We’d look at the queries and be baffled: these models are supposed to be smart! What was going wrong?
We’d make desperate prompt changes: “NEVER MAKE UP TABLES THAT DON’T EXIST!” or “Before joining to another table, think about whether the join is really necessary”. Half the time the changes would
decrease
pass rate rather than improve it, breaking seemingly unrelated queries in strange, unanticipated ways.
One day, someone cracked the code and realized that these hallucinations were actually upstream failures in our RAG system. The models were making up random columns
because
we weren’t giving them any columns to choose from
! Once we fixed the bugs in our RAG system, performance improved in a clear, predictable way.
This is why we funnel.
It lets you stop playing whack-a-mole and immediately zero in on the precise place to make your change.
Putting GPT-4.1 in the funnel
Alright, let’s see what this approach looks like on a real-world example. We’ll look at those GPT-4.1 results again, but instead of just reporting the raw increase in pass rate, we’ll look at the funnel!
Here are two funnel charts comparing GPT-4o to our first run of GPT-4.1:
funnel 41
To a seasoned funneler, there are a few interesting things that immediately jump out. We'll start at the end of the funnel and work backwards:
Stage 7: Correct Data (Pass)
There’s 39 new evals (54 —> 93) passing the correct data stage! That’s huge.
This is the vanity metric. Again, it’s good to know this, and it would be stupid to ignore it. It just can’t be the end of the story! So let’s work our way back.
knowledge
Why are our SQL evals so challenging?
GPT-4.1 still only gets 20% of our evals right. What makes this test so tough?
Most public SQL evals test the
syntactic
capabilities of models to write accurate queries on
fill-in-the-blank style questions
. In our opinion, frontier models have basically solved this by now.
Our private evals test instead for
real-world semantic accuracy
: how can a model consume entire messy warehouses as context and reason correctly about the business logic of a real company?
This makes them much more interesting as a challenge for frontier models, because they're really testing for general intelligence and analytical reasoning— not SQL proficiency.
Stage 6: Syntactically correct query
Hmm, a large increase (31) in SQL queries that just failed to run. This is interesting because as I mentioned, syntactically correct SQL is pretty much solved. It’s odd that a smarter model would make more ‘dumb’ mistakes here, so there must be a deeper story…
Drilling into this stage, we saw a big spike in a new, easy-to-solve failure mode: 4.1 was forcibly lowercasing and quoting column identifiers, making them case sensitive to the DB. This led to a bunch of errors like this simplified example:
Copy
select avg("arr") as "average_revenue" -- arr is actually ARR in the db.
from HEX_DATA.CORE.DIM_CUSTOMERS
where IS_CUSTOMER = true
----------
SQL compilation error:
error line 1 at position 11
invalid identifier '"arr"'
Once we implemented a one-line prompt fix, 12 more evals made it all the way to correct data.
Turns out the new model is fine at writing SQL, it just had a behavioral change that was obvious once we looked past that shiny pass rate and explored the funnel.
Stage 3: Table selection
We gain 19 passes here, which is impressive. This is a very difficult stage for us to influence with prompt engineering and RAG changes, so GPT-4.1 having an impact here is actually an extremely significant outcome.
High-upstream funnel improvements like this have especially high leverage because they unlock new insights deeper in the funnel. This improvement at stage 3 will likely have knock-on effects as we discover new downstream optimizations, so it's a big win for the overall performance of our system.
Updated funnel
Looking at the initial funnel helped us identify some interesting new behaviors of the 4.1 model and made it easy to adjust our prompts to compensate. With those changes, it’s now performing even better:
1.9x more than GPT-4o.
Funnel final
What’s next?
The funnel chart is helpful, but I’m sure analytically-minded readers have already zeroed in on the primary flaw: it presents results about how individual candidates move through the system… but it does so in aggregate?
How can we know if those 10 table selection improvements are
actually
responsible for the 10 correct data passes?
Flux
Flux is our quantitative measure of movement through the funnel. We look at flux both in aggregate, to quantify the net outcome of a treatment on our funnel, and broken out by stage, to see how evals are transitioning from stage to stage.
Because our funnel is nicely linear, we can quantify flux as a “distance” metric. If an eval jumped from Stage 3 (Table Selection) to Stage 8 (Pass), that’s a flux of +5.
Here's our source flux for the experiment, indicating what stages evals migrated out of. For GPT-4.1, the big flux out of “Table Selection” is what’s most exciting to me:
Flux Destination
This is one of the clearest tools we have for validating the direct impact of experiments. If you set out to fix column hallucinations, but see improved overall pass rates without many evals actually escaping the column hallucination stage, you know there’s some other factor confounding your experiment.
Orbit
The orbit chart visualizes individual evals as they move through “orbits” representing the funnel, with earlier stages closer to the center. It's an extremely information-dense view of an experimental result.
Here's an orbit chart of an initial 4o —> 4.1 test. Note all the scattered outlier regressions:
Orbit
Semantically similar evals are radially clustered together, so you can tell if a treatment has had an effect on one block of related evals in particular — or if it’s affected just one member of a block, which is an equally interesting outcome.
Our first attempts at an experiment often yield chaotic results like the chart above, with many evals regressing through the funnel even as others improve.
Over time, using these three tools — the funnel, orbit, and flux charts — as guides, we’re able to carefully refine an experimental treatment until we reach a more stable positive improvement.
Try this at home
Before you cmd+f & replace
gpt-4o
to
gpt-41
, take a moment and really look at your evals. Are they optimized for rapidly comparing yourself to others, or for efficient self-improvement and clarity?
Almost every company that's been kind enough to show me their internal evals has fallen into the first trap, building systems that focus on benchmarking against competitors but fail to guide meaningful internal improvements.
It’s pretty easy to fix, though. Take your most important LLM task and decompose it into as many discrete stages as you can. Organize those into a funnel. Build some flux charts. Re-run your evals, and I promise you’ll find something interesting hiding in there.
But yeah, once you've done that, you definitely 100% should switch to GPT-4.1. It's 2x better, after all 😉.
Share:
twitter
linkedin
Over the next few months we'll be publishing more about our eval philosophy and frameworks. In the meantime, try Magic out for yourself!
Get started for free
Learn about Magic
Made with
🍩
☕
🥟
🍺
🍰
🔮
🔒
🥖
🍷
🛌
💜
🥨
🛹
🍤
🧄
🍞
🥥
⛳
🤞
🔊
🎧
on
🌎
.
Company
Careers
Customers
Solutions
Media kit
Newsroom
Platform
AI and agents
Agentic notebooks
Conversational self-serve
Context Studio
Hex CLI
Exploratory analysis
Embedded analytics
Data apps
Integrations
Changelog
Resources
Pricing
Switching to Hex
Enterprise
Docs
Blog
Events
Templates
Compare
Trust Center
Status
Connect
Contact sales
Request a demo
Technical support
LinkedIn
X (Twitter)
YouTube
©
2026
Hex Technologies Inc.
Privacy policy
Terms & conditions
Modern slavery statement
