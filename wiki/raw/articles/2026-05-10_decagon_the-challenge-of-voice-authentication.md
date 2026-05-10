---
title: "May I ask who’s calling? How Decagon handles the challenge of voice authentication"
source: "Decagon Blog"
url: "https://decagon.ai/blog/the-challenge-of-voice-authentication"
scraped: "2026-05-10T01:19:48.734613+00:00"
lastmod: "None"
type: "sitemap"
---

# May I ask who’s calling? How Decagon handles the challenge of voice authentication

**Source**: [https://decagon.ai/blog/the-challenge-of-voice-authentication](https://decagon.ai/blog/the-challenge-of-voice-authentication)

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
Technology & Research
Blog
/
May I ask who’s calling? How Decagon handles the challenge of voice authentication
May I ask who’s calling? How Decagon handles the challenge of voice authentication
December 4, 2025
Written by
Ben Draffin
Share to
Copy link
Table of contents
Example h2
Subscribe to our newsletter
Get monthly updates with our latest articles, podcasts, videos, and more.
Enterprises are giving voice AI agents the power to check account balances, reset passwords, make order exchanges, and resolve complex issues end-to-end. But before any of that can happen, the agent needs to answer a deceptively simple question: Who is the person on the other end of the call?
Authentication is one of the hardest and most underestimated problems in voice AI. It sits at the intersection of security, user experience, and system design, and it’s the foundation of every safe, seamless customer interaction. Across millions of production calls, we’ve seen how small choices in authentication flow can dramatically impact security posture, resolution rates, and implementation overhead.
In this post, we’ll break down why voice authentication is uniquely difficult, how enterprises should navigate authentication tradeoffs, and why the future of conversational AI security depends not only on who the caller is, but also on what the agent should be allowed to do at each stage of the call.
Why voice authentication is uniquely hard
Authenticating end users with voice agents is notably more complex than in other channels (e.g., chat) for three key reasons:
Transcribing identifiers over voice is inherently difficult:
Member IDs, order numbers, and emails require precise capture of long alphanumeric fields. Speech-to-text (STT) models were not designed for precise, structured data like identifiers. A brittle transcription pipeline can cascade quickly into failed authentication attempts.
Callers are almost always multitasking:
People call support while driving, walking, or cooking. They’re less willing to open apps, check email, or complete multi-step verification mid-call. Voice authentication must minimize cognitive load, as each extra step introduces friction and increases abandonment.
Phone numbers are unreliable identifiers:
Voice interactions start with a phone number, but caller ID can be spoofed and cannot be treated as verified identity in isolation. While it’s a helpful signal, it’s insufficient on its own.
Getting voice authentication right requires a framework that balances security with the realities of real-time conversation, minimizing friction without compromising enterprise-grade safety.
Designing a robust voice authentication system
The right approach to voice authentication balances security with conversational ease, minimizes friction, and ensures the agent can confidently take action on behalf of the user. In practice, most implementations fall into one of two authentication models (pre-authenticated or mid-conversation), with additional considerations around identifier selection and data collection methods.
1. Pre-authenticated users
In the strongest and most seamless setup, users arrive at the voice agent already verified. Their identity is established before the call begins, enabling the agent to immediately access account data or initiate sensitive workflows without additional checks.
This model is typically implemented through:
Web- or app-gated calls:
The user initiates a call from an authenticated session.
Callback after verification:
The user completes a one-time verification (e.g., OTP, magic link) and receives a callback from the system.
SIP or metadata transfer:
Existing telephony infrastructure passes authenticated user data along with the call.
Pre-authentication drastically reduces friction and removes the need to collect structured identifiers over voice, though it requires technical infrastructure that many enterprises don’t yet have. Telephony services in this space continue to become easier, and engineering efforts can support development of these methods of interaction. While pre-authentication is an effective solution, some customers will initiate calls without any preauthentication, and mid-conversation authentication methods can be used.
2. Mid-conversation authentication
For most enterprises, authentication must happen in real time during the call. This is the most flexible and widely deployed model, though also the one most affected by the inherent constraints of voice. The following table outlines common mid-call authentication techniques and their tradeoffs.
Authentication method
Security (identification confidence)
Level of friction to UX
Details
Mobile app authentication / push notifications
High
Low
User clicks a notification to confirm identity if they have installed a mobile application
Confirmation of multi-part customer identifier(s)
Medium
Low
User verifies multiple pieces of information, such as their date of birth, customer ID, and ZIP code against existing member information
One Time Password (OTP) / Magic Link through Email
Medium
High
Collect a user’s email over the phone and send a magic link
One Time Password (OTP) / Magic Link through inbound phone number
Low
Low
Send an SMS OTP to the phone number being used by the customer (subject to some spoofing attacks and social engineering)
Test for knowledge of single basic identifier
Low
Low
User verifies their name or phone number they are calling in on (often this information can be learned from other methods)
Authentication triggers, such as initiating push notifications or sending magic links to users, can work well but require either integration with existing systems or adding user friction. Testing user knowledge can be an effective authentication method, however, these information-collection flows may need fallback information types when users do not know the required identifiers.
It’s worth noting that these comparisons do not account for implementation complexity, which may vary based on existing systems.
The most successful voice deployments also mirror existing human support workflows, using multiple identifiers that are easy to speak, easy to validate, and resistant to transcription errors.
3. Choosing the right information identifiers for knowledge challenges
Selecting the right identifiers is as important as designing the flow itself. Effective identifiers balance three attributes:
Ease of retrieval:
Most users should have easy access to an identifier associated with their account
Security:
Only the correct user should reasonably know it
Reliable voice capture:
It can be spoken, heard, and transcribed accurately
No single identifier maximizes all three, which creates natural tradeoffs. In practice, short numeric identifiers tend to offer the best balance between reliability and assurance.
Authentication method
Security
Difficulty of reliable collection
Member ID number
High
Low
Order ID (number)
High
Low
Order ID (alphanumeric)
High
Medium
Business-specific information
Medium / High
Medium
Last 4 digits of SSN
Medium
Low
Date of birth
Medium
Medium
ZIP code
Medium
Low
Email address
Medium
High
Phone number
Low (often public information)
Low
Name
Low (often public information)
Medium
4. Information collection methods
Even the best identifiers fail if collected through the wrong modality. Voice authentication relies on choosing the right input method for the identifier type and the user’s context. The table below summarizes the most common collection methods and their tradeoffs.
Collection method
Reliability
Level of friction to UX
Example
SMS input
High
Low
User replies to an SMS with their email address
DTMF tones (numeric only)
Medium
High
User presses a series of numbers to indicate their order confirmation number or member ID
Voice transcription
Medium
Low
User verbally tells the agent their email address; agent repeats information back to confirm receipt
Voice transcription technology continues to improve rapidly, but the variety of call quality, accents, word choice, and language adds complexity.
Choosing the right methods require balancing user friction with sensitivity of the action to be performed. Many actions do not demand the same level of identity assurance: asking about appointment times is lower sensitivity than changing a password or accessing financial information. Effective voice authentication combines methods based on risk, not applying uniform strictness.
Some actions only require a lightweight, low-friction signal, while others warrant more robust collection methods.
Incremental agent authentication: The other half of the equation
User authentication is only part of the story. Once a user is verified, the agent itself must prove to backend systems what it is allowed to access or modify on the user’s behalf. This is where many conversational AI systems fall short.
In many deployments, the agent is granted a single, broadly scoped token that provides the agent sweeping access to customer data and the ability to take high-risk actions. While convenient, this model breaks fundamental security principles like least privilege and Zero Trust. A universally privileged token makes it difficult for compliance teams to determine what the agent was authorized to do at any given moment, and why. It collapses the distinction between low-risk and high-risk operations, and creates an opaque access model that’s increasingly out of step with modern security expectations.
A more robust approach (and the one Decagon advocates) is to treat authorization as something that strengthens over the course of the conversation. In this model, the agent begins with minimal access and earns additional privileges only as the user provides stronger proof of identity. Early, low-risk interactions may only require a lightweight assurance signal, while actions involving sensitive data, billing details, or account recovery demand a higher level of verification. Each step up in identity confidence corresponds to an appropriately scoped token, granting only the permissions needed for the task at hand.
This incremental-permissions pattern mirrors how human agents naturally operate: trust is built gradually, based on context and intention, not granted all at once. It enables clearer audit trails, tighter control over data access, and a more transparent alignment between authentication strength and system capabilities, without disrupting the flow of conversation.
Advancing voice AI security with Decagon
Authentication failures in voice AI systems often stem from the inherent difficulty of reliably capturing identifiers in an audio channel. General-purpose transcription models were never designed for structured data like alphanumeric fields, domain-specific vocabularies, or noisy mobile environments, but these are exactly the conditions under which voice authentication must operate.
One area we’re investing in is fine-tuning STT models to optimize them for authentication-centric utterances, where clarity and precision matter far more than in general conversational speech. Tailored transcription systems like these will drive the next major leap in reliability and trust.
Voice authentication is not a single gate but a layered process that evolves over the course of a call. Done well, it becomes a brand differentiator by delivering safer operations, higher resolution rates, and a customer experience that feels natural rather than burdensome. At Decagon, our mission is to help every enterprise reach that standard.
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
