---
title: "Ten Design Principles of Agentic AI Skills Design "
source: X/Twitter Native Article
author: @IntuitMachine
tweet_id: 2043071219667480853
tweet_url: https://x.com/IntuitMachine/status/2043071219667480853
article_url: http://x.com/i/article/2043069686313594880
date: 2026-04-27
---

# Ten Design Principles of Agentic AI Skills Design 

> @IntuitMachine — [X Article](https://x.com/IntuitMachine/status/2043071219667480853)

Introduction: The Recipe Book That Writes Itself
When people discover that AI systems can be dramatically more effective — not 2x better, but 10x or 100x — they assume it's because of a smarter model. Better algorithms. More parameters. Secret sauce inside the AI itself.
It's not. The people getting extraordinary results are using the same models everyone else uses. The difference is how they wrap those models — specifically, how they write skills.
A skill is a reusable document that teaches an AI how to do something. Not what to do in one specific situation, but how to approach an entire category of tasks. Think of it as a recipe rather than an order. "Here's how to investigate a whistleblower complaint" rather than "Tell me if Dr. Smith was silenced."
The same skill, invoked with different inputs, can turn an AI into a medical research analyst, a forensic investigator, or a policy compliance auditor. The skill describes the process. The invocation supplies the world.
This essay distills ten principles for designing these skills well. These aren't tricks or hacks. They're structural insights about how AI systems work — and once you understand them, the practices feel obvious.
Principle 1: Skills Are Recipes, Not Orders
A common mistake is writing skills that look like this:
"Analyze the customer feedback and summarize the key themes."
This isn't a skill. It's an order. It works once, for one situation, and then it's gone. You can't reuse it because everything specific is baked in.
A skill looks like this:
Skill: Thematic AnalysisParameters: CORPUS (the documents), QUESTION (what you're looking for), DEPTH (quick scan or deep dive)Process:Read through the corpus noting your initial impressions
Identify recurring patterns — what comes up again and again?
Name the themes you've found
For each theme, pull representative examples
Assess: which themes matter most for the QUESTION?
Write a synthesis organized by importance

Notice the difference. The skill describes a process — a method that works regardless of whether you're analyzing customer feedback, employee surveys, academic papers, or legal depositions. The skill is the recipe. The parameters are the ingredients.
Why this matters: A single well-designed skill can handle hundreds of different use cases. Instead of writing new instructions every time, you invoke the same skill with different parameters. Build the recipe once; cook different meals forever.
Principle 2: Teach Thinking, Not Conclusions
There's a temptation to write skills that tell the AI what to decide:
"Step 4: Conclude that the evidence supports concern about patient safety."
This defeats the purpose. You've pre-decided the outcome and turned the AI into a puppet that ratifies your conclusion. Even if you're right, you've made the skill useless for situations where the evidence points differently.
Good skills teach how to think, not what to conclude:
"Step 4: Weigh the evidence for and against the hypothesis. Consider: Does the timeline make sense? Are there alternative explanations? What evidence would change your mind? Reach your own conclusion based on what you find."
The difference is crucial. The first version replaces judgment. The second version invokes judgment. The AI has to actually think through the problem — which is the whole point of using an AI.
The test: Can you invoke this skill to argue the opposite conclusion? If I can use your "investigate whistleblower" skill to investigate both "was this person silenced?" and "was this complaint unfounded?" — and get appropriately different answers based on evidence — then you've written a real skill. If it always points one direction regardless of evidence, you've written a prompt in disguise.
Principle 3: Draw the Line Between Judgment and Computation
Every step in your AI system falls into one of two categories, and confusing them is the most common mistake in design.
Judgment is where intelligence lives. Reading a document and deciding what matters. Weighing competing considerations. Recognizing that two seemingly different situations are actually the same pattern. Sensing that something feels off even if you can't articulate why. This is what AI models are genuinely good at.
Computation is where reliability lives. Same input, same output, every time. Database queries. Arithmetic. Sorting a list. Counting words. Checking if a date falls in a range. Traditional software does this perfectly; AI does it unreliably.
Here's the intuition: Ask an AI to seat 8 people at a dinner table, accounting for who gets along with whom and who shouldn't sit next to each other. It'll do brilliantly — weighing personalities, sensing social dynamics, making judgment calls.
Now ask it to seat 800 people under the same constraints. It will produce something that looks like a seating chart but violates constraints invisibly. It'll confidently place Alice next to Bob even though they're on the exclusion list. The output looks plausible but is quietly wrong.
Why? Seating 8 people is a judgment problem — you hold everyone in mind and feel your way to a good arrangement. Seating 800 is an optimization problem — you need an algorithm, not intuition. The AI doesn't have the algorithm, so it hallucinates one.
The principle: Skills should orchestrate this boundary explicitly. Mark which steps require judgment (let the AI think) and which require computation (call a tool). Don't let the AI do arithmetic. Don't make a calculator do interpretation.
Principle 4: The Magic Is in Reading Everything
Here's something AI can do that no database query can: read fifty documents about a person, notice contradictions between them, track how stories change over time, and write a one-page profile that captures who this person actually is.
We call this diarization — synthesizing scattered information into structured intelligence.
Consider an example. You're organizing a conference and want to understand the founders who applied. The database knows their company name and sector. Their application says "AI infrastructure." But their 1:1 conversation with an advisor reveals they're mostly worried about billing and cost attribution. And their GitHub commits show 80% of recent work is in the payments module.
A diarization skill reads all of this and produces:
SAYS: "Datadog for AI agents" ACTUALLY BUILDING: FinOps tool disguised as observability GAP: Positioning doesn't match execution. Either pivoting or unclear on identity.
No keyword search finds this. No embedding similarity surfaces it. The AI had to read everything, hold the contradictions in mind, and make a judgment call about what's really going on.
The principle: Build skills that read everything and synthesize. Don't pre-filter down to "relevant" documents — you don't know what's relevant until you've read it. The power is in the synthesis that emerges from seeing the full picture.
Principle 5: The Right Document at the Right Moment
Here's a mistake I made: I wrote 20,000 lines of instructions for my AI assistant. Every quirk, every lesson, every pattern I'd ever encountered. I thought more guidance would help.
It made things worse. The AI's attention is finite. Drowning it in information means it misses what matters. Buried in 20,000 lines, the key instruction for the current task becomes invisible.
The fix: 200 lines. But those 200 lines aren't instructions — they're pointers. When you're doing X, load document Y. When you see pattern A, consult skill B.
This is a resolver — a routing system that loads the right context at the right moment. The developer changes a prompt; the resolver loads the evaluation guidelines before they ship. The analyst asks about a customer; the resolver loads that customer's history. The resolver knows which knowledge matters when.
The analogy: A great assistant doesn't read you the entire company manual when you ask a question. They know which page matters for this question and open right to it. The resolver is that assistant.
The principle: Don't load everything everywhere. Build resolvers that sense what's needed and load exactly that. Your AI's attention is precious — spend it on what matters for the task at hand.
Principle 6: Push Intelligence Up, Push Execution Down
Picture your AI system as a three-layer cake.
Top layer: Skills. These are rich documents full of process, judgment, and wisdom. They're written in natural language because that's what AI thinks in. This is where 90% of the value lives. When you want to improve the system, you edit skills.
Middle layer: Harness. This is thin — maybe 200 lines of code. It runs the AI in a loop, manages context, and calls tools. That's it. No business logic. No judgment calls. Just plumbing.
Bottom layer: Tools. These are fast, simple programs that do one thing reliably. Query the database. Read a file. Send an email. Same input, same output, every time.
The principle: Push intelligence up into skills. Push execution down into tools. Keep the harness thin.
Why? When the AI improves (and it will), every skill automatically gets better. The judgment lives in skills; better AI means better judgment. Meanwhile, the tools stay perfectly reliable because they're just code.
But if you embed intelligence in the harness — if your orchestration code makes judgment calls — you create an ungovernable mess. You can't edit judgment because it's hidden in code. You can't improve it when models improve. And you can't even see what's happening because the thinking is scattered across files.
The anti-pattern: A "fat harness" with 40 tool definitions eating up context, business logic embedded in orchestration, and skills that are thin afterthoughts. This is exactly backwards.
Principle 7: Fast and Narrow Beats Slow and General
There's a temptation to build general-purpose tools. A "browser tool" that can do anything in a browser. A "database tool" that wraps every possible query. An "API tool" that exposes every endpoint.
This is a trap.
General-purpose tools are slow. A generic browser automation tool might take 15 seconds to screenshot-click-wait-read. A purpose-built tool that does exactly that workflow takes 100 milliseconds. That's 150x faster.
General-purpose tools bloat context. Forty tool definitions eat up the AI's attention budget before you've even started the task.
General-purpose tools hide complexity. When the tool tries to be "smart," you've buried judgment somewhere you can't see or improve.
The principle: Build tools that are fast, narrow, and dumb. Each tool does one thing. It does that thing in under half a second. It doesn't interpret or decide — it just executes.
The liberating insight: Software doesn't have to be precious anymore. If you need a tool that does exactly X, build exactly that tool. It might take thirty minutes. The AI can even help write it. When you don't need it anymore, delete it. Tools are scaffolding, not architecture.
Principle 8: Chase "Pretty Good" — That's Where Improvement Lives
When your system produces output, users react in three ways:
Great: "This is exactly what I needed!" OK: "This is... fine, I guess." Bad: "This is completely wrong."
Most people focus on fixing "Bad" responses. They're dramatic. They feel urgent. But here's the counterintuitive insight: "OK" responses are where improvement lives.
"Bad" responses are usually obvious failures. The system crashed. The tool timed out. The skill was totally wrong for the task. These are bugs, not opportunities for refinement.
"OK" responses mean the system almost worked. The mechanism functioned. Judgment was applied. But something fell short. The profile was accurate but missed the key insight. The recommendation was reasonable but not quite right. The synthesis was complete but somehow felt thin.
This gap — between OK and Great — is where your skills can improve. And to improve them, you need to understand why OK wasn't Great.
The principle: Build a learning loop that focuses on lukewarm responses. Read what the AI produced. Read what the user said. Ask: what's the gap? Then modify the skill to close it.
Example from a real system: An event-matching skill got 12% "OK" ratings. The team read the feedback, identified a pattern — founders were being matched by stated sector when their actual work was in a different sector — and added a rule: "When someone says AI infrastructure but their code is mostly billing, classify them as FinTech." OK ratings dropped to 4%.
That rule came from examining the gap between "fine" and "great."
Principle 9: Write It Once, It Runs Forever
Here's a discipline that separates 10x results from ordinary ones:
"You are not allowed to do one-off work. If I ask you to do something and it's the kind of thing that might happen again, you must: do it manually the first time on a few examples, show me the output, and if I approve, codify it into a skill."
The test is simple: if you have to ask for something twice, you failed.
Every skill you write is a permanent upgrade to your system. Unlike a clever prompt that you forget, a skill is saved, versioned, and available forever. It runs at 3 AM while you sleep. It handles a thousand instances without getting tired. And here's the beautiful part: when AI models improve, every skill you've written automatically gets better. The skill encodes process; the model provides capability. Better model + same skill = better output.
The compounding effect: Imagine a system with 100 skills, each handling some category of work. Every skill runs reliably. Every skill improves when models improve. Over time, the system accumulates capability the way a company accumulates assets. But unlike physical assets, skills don't depreciate. They compound.
The mindset shift: Stop thinking of AI interactions as conversations. Start thinking of them as opportunities to build permanent capability. Every time you solve a problem, ask: could this become a skill?
Principle 10: Same Process, Different World
Here's where all the principles come together.
Consider a skill called /match. Its job is to pair or group entities by some criteria. It takes parameters:
ENTITIES: who are we matching?
CRITERIA: what makes a good match?
CONSTRAINTS: what rules must we follow?
Watch how the same skill becomes three completely different capabilities:
Conference breakout rooms: ENTITIES = 1,200 founders. CRITERIA = sector similarity. CONSTRAINTS = 30 per room. Output: founders grouped with peers in their industry.
Serendipity lunches: ENTITIES = 600 founders. CRITERIA = cross-sector novelty. CONSTRAINTS = 8 per table, no one who's met before. Output: founders grouped with people who'll surprise them.
Live networking: ENTITIES = whoever's in the building right now. CRITERIA = nearest-neighbor embedding. CONSTRAINTS = 1:1 pairs, exclude recent meetings. Output: instant match for anyone who walks in.
Same skill. Same seven steps. Completely different behavior.
The insight: A well-designed skill is a method that takes parameters. The parameters supply the specific world — the data, the criteria, the constraints. The skill supplies the process — the judgment, the steps, the wisdom. You design the skill once, and then invoke it forever in contexts you haven't even imagined yet.
This is the leverage that turns AI from a curiosity into a force multiplier. One skill, a hundred use cases. Design the recipe; cook different meals.
Conclusion: The Discipline of Codification
These ten principles point toward a single discipline: codification.
When you encounter a repeated task, codify it into a skill. When you notice a judgment that works, codify how you made it. When you find a pattern, codify the pattern so the system can recognize it.
The people getting 100x results aren't smarter. They're not using secret models. They're just relentlessly codifying their work into skills — and then letting those skills run at scale, improve over time, and compound.
A year from now, your skills will run on better models than today. Every skill you write now is an investment in that future capability. Every judgment you codify becomes leverage you'll never lose.
The system compounds. Build it once. It runs forever.
Write the recipe. Cook the meal. Share the recipe. Move on to the next one.
That's the practice.
