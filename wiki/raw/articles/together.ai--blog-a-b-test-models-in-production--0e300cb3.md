---
title: "A/B test models in production"
url: "https://www.together.ai/blog/a-b-test-models-in-production"
fetched_at: 2026-08-18T10:03:44.617119+00:00
source: "Together AI Blog"
tags: [blog, raw]
---

# A/B test models in production

Source: https://www.together.ai/blog/a-b-test-models-in-production

Implementing A/B testing for LLMs in production
Sooner or later every team wants to answer the same question:
is the new model actually better for our users compared to the current model?
Not better on a benchmark but rather better on retention, thumbs-up rate, task completion, whatever your product actually measures.
Shadow traffic
can't answer that question. Shadowing tells you the candidate is
operationally
sound with respect to latency, errors, throughput, but its responses are discarded; no user ever acts on them. Quality questions need real exposure to end users where a cut of your users get model B, and you compare what happens.
Typically teams build this themselves in the application layer using some combination of:
A feature flag or a hash-mod-100 on user ID in the client code.
Two endpoints (or two hardcoded model strings) the client switches between.
A spreadsheet somewhere explaining what group A vs B means.
It works, but it entangles your experiment with your infrastructure in ways that hurt later: the routing logic ships with your application, the cohort split can drift as clients cache decisions, and even after the experiment "ends" the branching code lives on long afterward because nobody's sure it's safe to remove.
The Together AI platform allows you to run A/B experiment logic at the endpoint level.
How it works
An A/B experiment attaches to an endpoint and declares members with exactly one
control
and one or more
variants
, each pointing at a deployment, each with a
percent
setting, that must sum to 100, controlling traffic routing.
How the endpoint router works is that whenever the base traffic sends a request to the control the experiment re-samples it among the arms and redistributes such that 95% stays on the control, 5% goes to the variant.
To be precise about the mechanism:
the experiment subdivides the control's share of the base traffic split.
Routing first resolves a request through the weight split; when the winner is the control of an A/B experiment, the request is re-sampled among the experiment's arms by their percents. With the control as the only entrypoint in the split member percents therefore
are
absolute traffic shares. Also worth noting is that a control whose split weight is zero gives the experiment nothing to subdivide and as a result the whole experiment receives no traffic.
Importantly
variant deployments must
not
be in the endpoint's traffic split,
the platform requires variants to carry zero weight; only the control lives in the base split. The experiment will own traffic routed to the variant entirely; its percentage
is
its traffic share. If a variant could also draw capacity-weighted traffic from the split, your measurements would be quietly wrong. One way to think about it is that you should set up the variant like a shadow deployment: created,
READY
, weight zero and then let the experiment percentage setting route to it.
Another important point here is that A/B percents are
true fixed traffic shares
summing to 100% and are independent of replica counts. We made this deliberately different from traffic-split weights (which are per-ready-replica and follow capacity). An experiment is a
measurement instrument
; you want the split to be constant while you measure and not drift with autoscaling.
Creating a 95/5 experiment:
tg beta endpoints ab my-org/candidate-model --control $CONTROL_DEPLOYMENT --percent 5
Your clients won’t notice this experiment because on the surface the same endpoint name, API and keys persist. On the backend 5% of requests will now be answered by the variant candidate.
Under the hood: ramping, measuring, ending
Ramping is resending the member set
There's no separate "ramp" API, an update will
replace the full member list
, which keeps the mental model simple (the experiment is always exactly what its members say) and makes every ramp an explicit reviewable change:
# Week 2: candidate looks good at 5% —> go to 20%
client.beta.endpoints.ab_experiments.update(
    id=experiment_id,
    endpoint_id=endpoint_id,
    update_mask="members",
    etag=experiment.etag,   # a teammate's concurrent ramp gets rejected, not overwritten
    members=[
        {"deployment_id": control_dep, "percent": 80, "role": "AB_EXPERIMENT_MEMBER_ROLE_CONTROL"},
        {"deployment_id": variant_dep, "percent": 20, "role": "AB_EXPERIMENT_MEMBER_ROLE_VARIANT"},
    ],
)
Updates are guarded by an etag because if a teammate ramped the experiment while you were composing your update, yours will be rejected instead of silently overwriting theirs.
With this API design you still need to make the common exposure choice of how much traffic to route to group B:
Split
Signal speed
Risk
Use when
95/5
Slow (needs volume/time)
Minimal
New model, first real exposure
80/20
Moderate
Contained
Candidate survived 5%; you want a more significant readout
50/50
Fastest
Half your users
Late-stage confirmation between two known-good options
With up to
20 variant members
you can also run multi-way tests, lets say for example you want to try out a full-precision endpoint along with three other quantized variants (V1, V2, V3). This will work as expected as long as the percents still sum to 100% and there's exactly one control.
Measuring: join platform metrics with your product metrics
Every request is served by a specific deployment, and every
platform metric
is available per deployment — so the infra side of the comparison (latency, errors, throughput per cohort) is a filter, not a project. The product side is yours: log which deployment served each response (it's in the response metadata) alongside your quality signals — ratings, retries, task completions — and the join key is just the deployment ID. The platform deliberately doesn't guess at your quality metrics; it makes the attribution trivial so your analytics can do the judging.
Ending: promote, then delete
Suppose the experiment shows the variant wins. Ending it is a two-step process:
Promote via rollout.
Run a blue-green
rollout
from the control deployment to the variant deployment. Health gates, propagation waits, and rollback safety all apply.
Delete the experiment.
All experiment routing disappears and 100% of the traffic then follows the endpoint's base traffic split which, post-rollout, points to your winner.
And if the variant loses, you can just delete the experiment and traffic will return entirely to the control. On the backend the variant deployment scales to zero or gets deleted.
tg beta endpoints rm abx_abc123        # delete the experiment; 100% returns to the base split
tg beta endpoints rm dep_variant123    # or delete the variant — auto-unwinds experiment + split
Edge cases
The variant degrades mid-experiment. What's the blast radius?
Only its cohort. Deployments are independently monitored and independently autoscaled, which means that a struggling variant won’t drag the control down. To fix this you can resend the member set without the sick variant and its users will be back on control within a certain propagation time. This is also why starting at 5% is a good idea.
Do the observed shares actually match the configured percents?
Over meaningful volume, yes! For an example of this in action check out the experiment below. Over small windows you can expect sampling noise: a 5% share of 1,000 requests is a small sample. If your observed share is off by a lot
and
stays off, check the setup rule above.
Can an A/B experiment and a rollout run on the same endpoint?
Yes, and the composition order is defined as: routing resolves the base split first, then A/B experiments (subdividing the control's share),
then
rollouts (re-sampling between a source deployment and its rollout target). The platform still enforces one
active rollout
per endpoint but the stages are designed to compose if they overlap.
Are cohorts sticky per user?
Assignment uses the request's
sampling key
, for example a top-level
prompt_cache_key
or
user
field in the request body, so requests carrying the same key route consistently and a given user can stay in one test arm across a session. Requests without a key are assigned effectively at random per request (our experiment measurements below used key-less traffic, which is why observed shares match the percents so closely). If per-user consistency matters to your study, especially if you have multi-turn quality comparisons, send a stable
user
field.
What happens to autoscaling under a split?
Each member deployment scales on its own policy, sized by its own share of traffic. A variant at 5% with bounds 1-2 and a control at 95% with bounds 2-8 is a perfectly normal shape. You should watch each cohort's replicas independently, this is what we capture in the chart below.
Showing one A/B experiment, start to finish
We ran the full lifecycle against a live endpoint where we create at 95/5, ramp to 80/20, ramp to 50/50 then delete. We do this while maintaining a steady 3 RPS stream, with every request attributed to the deployment that served it. The graph below shows traffic seen at the variant with green dots capturing variant traffic share:
Here are the configured vs observed traffic shares at every stage:
Configured (control / variant)
Observed
Requests
95 / 5
95.3 / 4.7
1,330
80 / 20
79.2 / 20.8
1,348
50 / 50
50.2 / 49.8
1,348
deleted
100.0 / 0
360
Three details from the run worth calling out:
Each ramp really was just one call
and you can resend the full member set with the current
etag
. The etag advances
1 → 2 → 3
across the two ramps; a stale etag would have been rejected rather than it silently overwriting a teammate's change.
Propagation is fast but not instant.
We waited ~75 seconds after each update before measuring; the routing layer picks up experiment changes on the same 30–60s timescale as traffic-split changes.
Delete:
After removing the experiment we sent 360 consecutive requests and they all landed on the control. There is no left over cohort logic besides the delete left over to unwind.
Here's the experiment as the console shows it, on the endpoint's
Traffic tests
tab (A/B tests and shadow tests share the page):
Try it yourself!
You need an endpoint with a control deployment serving traffic, plus a candidate deployment (created,
READY
,
not
in the traffic split). Then:
Create the experiment at
95/5
.
Let it run until you have enough volume — the whole point of 5% is that exposure stays low while you collect data.
Ramp with a single update when the data says so. Promote with a rollout when it's decisive. Delete when you're done — there's nothing else to clean up.
📚
Docs:
Dedicated Model Inference →
A/B tests
