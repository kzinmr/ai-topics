---
title: "Webinar Recap: Reaching At-Risk Patients When Minutes Matter"
source: "ElevenLabs Blog"
url: "https://elevenlabs.io/blog/webinar-recap-reaching-at-risk-patients-when-minutes-matter"
scraped: "2026-10-22T06:00:16.053577+00:00"
lastmod: "2026-10-22T00:49:53.758Z"
type: "sitemap"
---

# Webinar Recap: Reaching At-Risk Patients When Minutes Matter

**Source**: [https://elevenlabs.io/blog/webinar-recap-reaching-at-risk-patients-when-minutes-matter](https://elevenlabs.io/blog/webinar-recap-reaching-at-risk-patients-when-minutes-matter)

Blog
Product
Webinar Recap: Reaching At-Risk Patients When Minutes Matter
Written by
John
Durovsik
Published
Oct 21, 2026
Last updated
Oct 22, 2026
Listen
Listen to this article
0:00
0:00
0:00
1.0x
Watch the live session
On this page
Introduction
Key takeaways
Why reaching at-risk patients matters
What fast outreach looks like for patients
Demo: Remote patient monitoring agent
Best practices for building a critical care agent
Best practices for expanding to new workflows
Watch the full session
When a remote monitoring device flags a dangerous reading, the clock starts. In Behind the Agent: Reaching At-Risk Patients When Minutes Matter, Rachel Wang (VP of Engineering, Cadence) sat down with Caleb Wright (Enterprise Deployment, ElevenLabs) to walk through how Cadence uses ElevenAgents to reach patients within minutes of an out-of-range vital. The session covered what the Cadence engineering team learned while building critical alert agents, where mistakes carry clinical consequences.
Key takeaways
Speed changes outcomes.
Cadence cut the time to reach a patient after an out-of-range vital from a median of 1 hour and 48 minutes to 3.5 minutes.
Design for the cost of being wrong.
When the agent is uncertain, the patient stays safe: "not sure" counts as not cleared, and the alert cannot be resolved. Agents should also over-escalate to a nurse rather than missing a critical issue.
Real calls teach more than theory.
Getting on live calls early with a clinician in the loop, and turning every miss into a test, is how the agent improves.
Agents free nurses for clinical work.
Voice agents handle the first outreach and symptom screen so nurses can practice at the top of their license.
Why reaching at-risk patients matters
Healthcare leads all industries in AI spending, and almost 50% of healthcare teams are using or exploring AI tools. The focus is moving from back-office administration to direct patient engagement.
The need is clear - chronic conditions affect 95% of the Medicare population, and those conditions need daily attention. At the same time, the US faces a projected shortage of up to 86,000 physicians. Clinical teams can't close that gap with headcount alone. Cadence
built
an always-on care engine to address this gap. Before ElevenAgents, Cadence’s human clinicians reached patients in a median time of 1 hour and 48 minutes. With ElevenAgents, time to patient contact dropped to 3.5 minutes.
What fast outreach looks like for patients
Cadence's agent monitors incoming vitals. When a reading falls out of range, the agent calls the patient, runs a symptom screen, and either escalates to a nurse or closes the alert. Rachel shared two patient stories that showed what that speed means in practice:
Elevated heart rate.
A patient's heart rate came in above 150. The agent called immediately, and a nurse advised them to go to the emergency department, where they were diagnosed with atrial flutter. The patient later said Cadence saved their life and was struck by how quickly the call came after their reading.
Uncertain next steps.
A patient in their mid-seventies wasn't sure what to do after a reading. The agent called within minutes, and a Cadence nurse practitioner adjusted their medication and contacted their primary care doctor - at the moment it mattered.
Timing also changes whether patients pick up. Answer rates on critical calls rose from 41% to 60%, and patients answer the agent 47% more often than human callers. Relevant, timely outreach gets answered.
Demo: Remote patient monitoring agent
Scenario:
A remote patient monitoring agent contacts a patient after receiving a high blood pressure reading.
What was shown:
The agent's system prompt, structured into context, response guidance, guardrails, and tool descriptions
A live call covering identity verification and a symptom check
Escalation to a nurse based on the symptoms the patient reported
Post-call analysis with evaluation criteria (such as completing the symptom screen and not giving medical advice) and structured data collection (such as verified patient and symptoms reported)
Simulation tests used to validate agent behavior across scenarios before deployment
Dashboards for monitoring agent performance and key metrics
Why it matters:
Clinical agents need more than good prompts. Identity verification and automated escalation keep patients safe on the call while testing and analytics confirm the agent keeps behaving correctly as call volume grows.
Best practices for building a critical care agent
Design for the cost of being wrong.
Assume the agent will sometimes make mistakes, and design so the patient stays safe when it does. In practice, that means over-escalating to a nurse rather than missing a critical issue.
Require evidence before closing an alert.
The agent must confirm every required symptom question was asked, and every answer must be a clear "no" to resolve the alert. "Not sure" counts as a "yes." A second judge then checks the conclusion against the transcript.
Bound access and authority.
Give the agent only the protected health information (PHI) it needs for the immediate goal. Enforce authorization checks in code.
Get on real calls early.
Deploy with a clinician in the loop as soon as possible. Real conversations surface details a test plan won't, like how long to pause or how individual patients tend to speak.
Leave room for warmth.
Let the agent engage briefly in pleasantries before gently steering back to the critical questions. Patients are more comfortable when the call doesn't feel like a checklist.
Personalize repeat interactions.
For patients who hear from the agent often, adjust the greeting and acknowledge previous calls. Continuity builds trust.
Define success before testing.
Give nurses specific feedback criteria when they review the agent. Use that feedback to build ground truth datasets and set rollout gates.
Turn every miss into a test.
Each time the agent does something unexpected, add a test case for it, including varied voicemail scenarios. This prevents regressions as the agent changes.
Track containment and handoffs.
Measure how many calls the agent resolves versus hands off to a nurse. The reasons behind each handoff show where the agent needs to improve.
Best practices for expanding to new workflows
Start with repeatable, constrained workflows.
First deployments work best where the process is structured and the protocol is clear.
Build trust on every call.
Patients stay on the line when they trust the agent. That comes from delivering value, being upfront, using the right voice and tone, and keeping latency low.
Harden production systems.
Critical workflows need observability, monitoring, and failover. No alert should be missed because of a dropped call or a vendor outage.
Choose the next workflow deliberately.
Look for where agents can excel and where clinical teams spend the most time. Prioritize high-volume, repeatable tasks and time-consuming issues.
Watch the full session
Watch the
full webinar here
.
Written by
John Durovsik
Growth
View profile
John is on the ElevenAgents growth team, with a focus on the healthcare industry.
