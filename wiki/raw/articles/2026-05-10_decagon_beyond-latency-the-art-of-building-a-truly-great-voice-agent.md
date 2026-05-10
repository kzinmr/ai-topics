---
title: "Beyond latency: The art of building a truly great voice agent"
source: "Decagon Blog"
url: "https://decagon.ai/blog/beyond-latency-the-art-of-building-a-truly-great-voice-agent"
scraped: "2026-05-10T01:19:33.463076+00:00"
lastmod: "None"
type: "sitemap"
---

# Beyond latency: The art of building a truly great voice agent

**Source**: [https://decagon.ai/blog/beyond-latency-the-art-of-building-a-truly-great-voice-agent](https://decagon.ai/blog/beyond-latency-the-art-of-building-a-truly-great-voice-agent)

Introducing Proactive Agents.
Learn more
Product
Product overview
Channels
Voice
Human-like conversation
Chat
Safe, on-brand replies
Email
Contextual resolutions
Build
AOPs
Workflows for AI agents
Integrations
Support tool connectors
Optimize
Experiments
Live A/B testing
Testing & QA
Simulations at scale
Scale
Insights & Reporting
Voice of the Customer
Watchtower
Always-on QA
Suggestions
AI-powered knowledge
Industries
Retail
Travel & hospitality
Technology
Financial services
Health & wellness
Media
Telecommunications
Customers
Resources
Learn
Resources Hub
Decagon University
Glossary
AI and the next generation of customer experience
Why exceptional service is the new brand differentiator as AI reshapes consumer expectations.
Spring ’26 Release: Proactive Agents
See how user memory, outbound voice, and Agent Workbench can help you build stronger customer relationships
Company
About
Careers
Security
Sign in
Sign in
Get a demo
Sign in
Get a demo
Product Update
Company news
Technology & research
Industry
Industry
Blog
/
Beyond latency: The art of building a truly great voice agent
Beyond latency: The art of building a truly great voice agent
April 9, 2026
Written by
Curtis MacDonald
Share to
Copy link
Table of contents
Example h2
Subscribe to our newsletter
Get monthly updates with our latest articles, podcasts, videos, and more.
Most companies building voice AI start in the same place: obsessing over latency, transcription accuracy, turn detection, and other technical fundamentals. These things matter, but no amount of infrastructure precision compensates for a voice agent that fumbles conversation flow, sounds robotic, or simply feels wrong for your brand.
Once you have a strong technical foundation, two things separate good voice agents from great ones: conversation design and a voice profile that reflects your company. Get those right, and users hang up satisfied. Get them wrong, and no amount of low latency will save you.
Five principles of good conversational design
1. Help users get things done, fast
Distilling everything down, the goal of a voice agent is to efficiently help customers accomplish what they came to do. That doesn't mean cutting every step; disambiguation and clarification are often necessary. But most AI agents over-explain, ask questions they don't need to ask, or spiral into loops of unhelpful or repetitive responses.
This stems from the fact that LLMs are trained on text rather than spoken conversation, which makes their responses naturally verbose. Teams often make it worse by prompting with the only voice examples they have on hand: legacy IVRs built on formal, rigid language that sounds nothing like a real person.
First impressions form fast in voice. An agent that feels efficient right away earns trust quickly, while one that rambles through caveats before getting to the point signals immediately that this is going to be a painful call. Set expectations early, point users toward their goal, and stay focused once you get there. The longer a conversation runs without resolution, the more likely frustration becomes.
2. Sound clear and natural
This one sounds obvious, yet most of us have called into a system that uses stiff, overly formal phrasing or, even worse, performative enthusiasm ("Great question!") followed immediately by an unhelpful response. Natural language is what keeps callers engaged and willing to follow through.
Naturalness also means keeping callers informed when the agent is working. Silence without context makes people feel like something has broken, particularly when looking something up, processing a request, or confirming a detail. Brief spoken transitions ("Give me a second while I pull that up") go a long way.
Confirmation prompts should be kept to a minimum and only used when required. Used excessively, they slow the conversation down and signal a lack of confidence. Callers who feel like they can speak naturally and actually be understood are far more likely to stay engaged through to the end of a call.
3. Recover when things go wrong
Background noise, interrupted sentences, and users not having the required information your agent needs are all unavoidable on a phone call. The agent needs designed recovery paths, not just a loop that rephrases the same question with slightly different words. That loop is one of the fastest ways to lose a caller's confidence, but it's surprisingly common.
Good recovery means handling interruptions gracefully, offering genuinely different approaches when the first one fails, and knowing when to hand off to a human. A caller stuck in a doom loop will find their way to a human agent eventually, but by that point you've already lost their trust. Building in a clear handoff trigger after a defined number of failed attempts, and framing that handoff as helpful rather than a system failure, makes a significant difference to how the call is remembered.
4. Show empathy
Everyone calling a support line has a problem, and most arrive already a little frustrated. An agent that meets that frustration with flat neutrality is unhelpful; one that responds with the wrong emotional tone makes things actively worse.
Briefly acknowledging a missed delivery or a billing error before jumping straight to solutions signals to the caller that they've been heard, and that signal matters more than most realize. It de-escalates tension and keeps the conversation moving forward.
Empathy only lands, though, when it's paired with thoughtful follow-through. Generic sympathy with no action behind it feels hollow. Even when the agent can't fully resolve the issue, acknowledging the problem and explaining what comes next makes the caller feel like you're working toward a solution together, rather than hitting a wall of default FAQ responses. The goal is an interaction that feels collaborative, not transactional.
5. Know your users
Who is calling, and why? What emotional state are they arriving in? Are they calling from a noisy environment, in a hurry, or trying to resolve something they've already called about twice before? Designing a voice agent without answering these questions is designing blind. The more precisely you understand your caller population (e.g., their context, urgency, the specific words they use), the better you can tune the agent's behavior before the first word is spoken.
The best way to build this understanding is to listen to real calls before writing a single workflow. Call audits and listening sessions surface the gap between how users actually speak and how a team assumes they speak, and that gap is almost always larger than expected.
From there, it's worth building distinct handling logic for high-frustration scenarios like repeat callers or time-sensitive issues, and reviewing transcripts regularly to catch new gaps as they emerge. A voice agent that truly knows its users doesn't just sound better, but also resolves more issues, faster.
Choosing a voice profile: TTS and language guidelines in sync
The five principles above shape how a voice agent behaves, but there's a layer beneath behavior that shapes how the agent is perceived. Most teams approach this layer as two separate activities: selecting a text-to-speech (TTS) voice and defining personas guidelines. But handled independently, the result can be an uncanny valley of personality. For example, an agent with a warm, empathetic persona should not have a clipped, authoritative voice. The listener's brain registers the mismatch even if they can't articulate why.
Getting this right starts with the TTS voice itself. A voice profile goes beyond accent and speaking speed and instead includes a constellation of dimensions that together define how the agent sounds. We typically review these with customers as a starting point:
Formal vs. casual:
Formal signals expertise and seriousness, while casual signals approachability and ease.
Energetic vs. calm:
Energy works well in transactional or sales-oriented flows, while calm tends to serve high-stakes or emotionally charged scenarios better.
Mature vs. youthful:
Mature carries authority and steadiness, while youthful feels more peer-like and accessible.
‍
Warm vs. professional:
Warmth builds trust through personal connection, while professionalism builds it through confidence.
Once the TTS voice is defined across these dimensions, persona guidelines should be written to match. The persona that comes through in phrasing, tone, and empathy acknowledgments needs to feel like it's coming from the same entity the caller is hearing, not a different one that happens to share a phone line.
The biggest mistake teams make with voice profiles is treating the initial choice as a final one. Preferences are debated internally, a profile is shipped, and the conversation ends. In reality, the right profile is something you discover through A/B testing and validating it against real callers and concrete signals like resolution rates, CSAT scores, and escalation points.
The same rigor applies to conversational design, as small changes in phrasing or empathy acknowledgment can move metrics in ways that internal review never would have predicted. Data finds these; intuition usually doesn't.
Your voice is your brand
Every call a customer has with your voice agent is an interaction with your brand. Not a proxy for it, but the actual thing. The conversational design and voice profile shape how people feel about your company at moments when they're often already stressed.
Beyond building a great technical foundation, the teams that have a great voice AI are the ones who invest equally in how their agent behaves and how it sounds, and who treat both as ongoing work rather than one-time decisions. The principles and dimensions covered here are a starting point, not a checklist.
If you're building a voice AI experience and want to talk through what good design looks like for your use case, we'd love to hear from you.
Recent posts
Bringing the AI concierge to Australia
Decagon is opening a new office in Sydney, Australia
Introducing automatic optimization and Root Cause Analysis
Today, we’re excited to announce two new capabilities to help you rapidly improve your agent’s performance.
Bringing Decagon’s AI concierge solution to Google Cloud Marketplace
We're excited to announce that Decagon is now available on Google Cloud Marketplace.
Deliver the concierge experiences your customers deserve
Get a demo
Product
Overview
AOPs
Chat
Email
Voice
Integrations
Experiments
Insights & Reporting
Testing & QA
Watchtower
Suggestions
Trust Center
Industries
Retail
Travel & Hospitality
Technology
Financial Services
Health & Wellness
Media
Telecommunication
Resources
Customers
Resources Hub
Glossary
Company
About
Careers
Privacy Policy
Security
Contact Sales
Contact Support
©
0000
Decagon. All rights reserved.
