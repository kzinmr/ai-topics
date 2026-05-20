---
type: x_article
x_article_title: "Evals, explained"
x_article_url: "https://x.com/i/article/2054598592980234240"
x_tweet_id: "2056754091817361670"
getxapi: false
date: 2026-05-19
source_fallback: false
organization: Langfuse
series: Langfuse Academy
---

# Evals, explained

This is one piece of a series we’re publishing as part of the Langfuse Academy, where we walk through the full AI engineering lifecycle. If you’re new to the series,The AI Engineering Loop is the best place to start.
A short recap of the AI Engineering Loop
The AI Engineering Loop is how teams continuously improve AI systems. It connects what’s happening in production (tracing, monitoring) to structured iteration during development (datasets, experiments, evaluation). Each shipped improvement produces new data, and teams loop through this process continuously.
 
You can read more on this here. 
How evaluation fits into the loop
Offline evaluation is the step in the loop between running an experiment and shipping a change. You have a dataset, you have run your application against it, and now you need to judge whether the outputs are good.
How evaluation typically evolves
Most of the time, you start by manually reviewing outputs to build intuition for what good and bad look like in your application. From there, you identify specific failure modes worth checking for. Once you can define them precisely, you automate with dedicated evaluators.
 
The rest of this page covers the different kinds of evaluation in detail. In practice, you'll likely end up combining all of them. But the path to a well-functioning automated evaluation setup almost always starts from manual review.
Manual evaluation is not a one-and-done step. Good production setups incorporate continuous review by human experts to catch new failure modes and keep automated evaluators calibrated.
Evaluation methods
There are three main ways to evaluate: manually, with code, or with an LLM. Each is suited to different kinds of quality checks.
Manual evaluation
Manual evaluation is the process of manually looking at outputs and scoring it/writing down your thoughts on its quality.
This is an important process, reading outputs builds an understanding of what your application actually does, where it struggles, and what "good" looks like for your specific use case. That understanding is what tells you which automated evaluators to build and how to define their criteria later on. Teams that skip this step and jump straight to automated evaluation often end up measuring things that don't matter.
Manual evaluation also produces human labels that serve as ground truth for validating automated evaluators later.
Code-based evaluation
Code-based evaluators check properties that can be verified with deterministic logic. They are fast, cheap, and produce the same result every time.
Some example checks where code-based evaluators are a natural fit:
The output is valid JSON or follows a required schema
The output contains (or does not contain) specific keywords or patterns
The output stays within a length limit
The generated SQL executes without errors
Their limitation is that they cannot assess meaning. A code-based evaluator can check that an output contains the word "refund," but it cannot check whether the output correctly explains the refund policy.
LLM-as-a-judge
An LLM-as-a-judge evaluator uses a language model to score outputs. It is required to overcome the core issue that quality of AI Applications/Agents depends on grading the quality of a text output.
This is the right method for qualities that require understanding language: whether a response is relevant to the question, whether the tone matches the intended audience, whether a summary captures the key points of the source material, etc.
LLM judges are imperfect and easy to get wrong. This means:
A model does not automatically grade things as a human expert would as they do not have the context of the expert
They need calibration against human preferences to verify they are measuring what you think they are measuring
They can share blind spots with your application's LLM, especially when the same model family is used for both
These limitations aren't reasons to avoid LLM judges. An LLM judge that has been calibrated against human labels and is backed by code-based checks is a reliable evaluator.
Reference-based vs reference-free evaluators
Both code-based and LLM-as-a-judge evaluators can be either reference-based or reference-free. A reference-based evaluator compares the output against a predefined expected output, like a correct answer or a golden response. A reference-free evaluator assesses the output on its own, without needing a ground truth to compare against.
 
The advantage of reference-free evaluators is that they can be applied to unseen production data, while reference-based evaluators always need a pre-defined reference response.
In practice
When to set up evaluators
As mentioned above, you always start by manually reviewing. Once you have done that, the question then becomes: should you set up an automated evaluator for what you found?
Ask yourself whether the issue is a one-time fix or a generalization problem. If a simple prompt change resolves it, just make the change, there's no need for an evaluator. But if you can clearly identify a failure mode that you want to test for repeatedly across different inputs, that's when setting up an evaluator makes sense.
What should you evaluate?
Generic qualities like "helpfulness" or "quality" are tempting starting points, but they rarely produce useful signal. An evaluator that checks a vague criterion will give vague results. The more precisely you can define what "good" or "bad" looks like for your application, the more useful your evaluators will be.
One practical recommendation: prefer binary scores (pass/fail) over graded scales (1-5) when designing evaluators. Binary scores force a clear definition of what separates acceptable from unacceptable. Graded scales introduce ambiguity about what a 3 means versus a 4, which makes scores harder to interpret and less consistent across evaluators and over time.
Combining evaluation methods
Each quality you care about gets its own evaluator.
Most mature evaluation setups use all three evaluation methods. Together, they give you a view on overall quality of your application.
Where to start
Start with manual review, then automate only the checks you need to run repeatedly.
Review outputs manually to build intuition for what good and bad look like in your application.
Write down the specific failure modes you want to catch and define them as clearly as possible.
Set up an automated evaluator only when you need to test that failure mode repeatedly across many inputs or over time.
What comes next
If the results are good enough, you can ship the change. Once it is live, the loop starts again: the updated system produces new traces, new monitoring signals, and new opportunities to improve.
Some evaluators should also move beyond offline experiments. Reference-free evaluators, user feedback signals, and other production-safe checks can be applied to live traffic to confirm that quality in production matches what you saw before deployment.
If production behavior matches expectations, you can keep scaling with more confidence. If it does not, capture those cases in traces, turn them into dataset items, and run the next round of experiments. That is how you close the loop.
