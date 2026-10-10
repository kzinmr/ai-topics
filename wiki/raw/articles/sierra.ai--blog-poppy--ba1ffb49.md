---
title: "Sharing a draft of Personal Agent Protocol"
url: "https://sierra.ai/blog/poppy"
fetched_at: 2026-10-10T10:00:53.550171+00:00
source: "Sierra Blog"
tags: [blog, raw]
---

# Sharing a draft of Personal Agent Protocol

Source: https://sierra.ai/blog/poppy

Since
announcing
this new protocol on Tuesday with Meta and Genesys, Instinct, NiCE, Rocket, Shopify, Stripe, and Walmart, the response has been overwhelming.
So today we’re publishing a draft of
Personal Agent Protocol
, known as Poppy, and announcing an additional 35 design partners: Adyen, Atomic, Bank of America, BBVA, Chime, Cigna, Cloudflare, Comcast, DIRECTV, ElevenLabs, FOX, Gap Inc., GEICO, Hertz, Insurify, Klaviyo, Liberty Mutual, Mastercard, Nordstrom, Notion, Okta, OneSignal, OpenAI, PayPal, Plaid, SiriusXM, Synchrony, Target, United Airlines, Venmo, Visa, Wells Fargo, Zapier, Zendesk, and 1Password. These companies will participate in the design process for the draft Personal Agent Protocol, contributing valuable feedback from their unique business perspectives.
Today, when someone asks their personal agent to make a purchase or resolve an issue, it often has to sign in as the customer and navigate pages built for people. Businesses have no standard way to help guide the agent, which limits what the customer, their personal agent and the brand can do directly together. With the Personal Agent Protocol, consumers have choice and control, and companies know when they’re dealing with an agent and who it represents.
How Personal Agent Protocol works
Poppy is built on the principle that customers decide what access to give their personal agents, and companies set parameters for what those agents can do. This enables companies to work with personal agents in the way that is best for their customers: through their existing websites and APIs, or through an agent of their own.
Poppy defines five building blocks for how personal agents and companies work together.
Discovery
. Companies publish one file at a standard address on their website (/.well-known/poppy.json). This tells personal agents how to interact with the company, how customers can sign in, and what the agent can do.
Sessions
. The personal agent starts a session on its customer’s behalf. It can begin as a guest, which may be enough to check whether a product is in stock or ask about a returns policy. The personal agent identifies itself, so the company always knows when an agent is acting for a customer.
Sign-in
. When a task needs the customer’s account, the person signs in on the company’s page through OAuth. If permitted by the company, the agent can sign in on the customer’s behalf with a session token that grants only the access the customer approved.
One session across every channel.
The same token works for the company’s APIs, its website and conversations with its agent. A question asked before sign-in and an order change made afterward are part of the same visit. The customer doesn’t have to start over, and the company sees the whole journey instead of disconnected fragments.
Getting the job done.
The company decides which channels to offer, based on what works best for its customers:
Its website
: the agent browses the company’s regular pages, and the company applies the customer’s permissions on each one.
Its APIs
: the agent connects through interfaces built on standards such as OpenAPI and MCP.
Its own agent
: for tasks that need conversation, such as a warranty claim or an exchange. Replies can stream as they’re written, and companies can hold a request open until there’s news to share.
Built on standards companies already use
A company can start with what it already has and add more over time. Companies can connect once through Poppy, rather than building a separate connection for each personal agent.
The protocol is built on OAuth, JSON Web Tokens (JWTs), HTTPS, OpenAPI and MCP. Because these are open and widely used, teams can implement it with libraries and tools they already have. The core is also designed to be extended, so industries can build their own layers on top.
Protocols such as Universal Commerce Protocol (UCP) focus on shopping, from finding products to checking out and managing orders. Personal Agent Protocol is complementary, covering how a personal agent identifies itself, gets the customer’s permission, and works with a company across any kind of task — from buying a sweater to applying for a mortgage.
What it looks like in practice
Personal Agent Protocol works whether a company offers its website, its APIs or its own agent.
Through a website
. A customer asks their personal agent to return a jacket. The agent finds the retailer using the protocol, identifies itself, and the customer signs in once. The agent then uses the retailer’s regular returns page. The retailer knows it’s an agent acting for a signed-in customer, and lets it start a return but not change the payment details on file.
Through APIs
. A customer’s flight is canceled, and they ask their personal agent to rebook them. The agent connects to the airline’s booking tools through MCP using the customer’s approved access. It finds the next available flight and confirms the seat with the customer before booking.
Through a company agent
. At Sierra Summit on Tuesday, Alex McGillis, VP of Product at Rocket, showed the
protocol live
featuring Meta’s personal agent, Muse. Alex asked Muse to get pre-approved for a mortgage. Muse went to Rocket’s website, found Rocket’s agent through Poppy, and asked Alex for permission to connect. Alex then signed in to share the credit and income details a mortgage needs. The two agents worked through the purchase price, down payment and interest rate and within moments, Alex had a pre-approval letter ready. While he was in control at every step of the way, the agents did all the work.
What comes next
This draft is a starting point. Over the next month we will host design workshops and publish a reference implementation to help developers get started. As personal agents grow in popularity and take on more work, our goal is simple: customers choose who acts for them, companies know who they are working with, and both can do so securely and within the boundaries they set.
We’d love as many companies as possible to
read the draft
and help shape this new protocol.
