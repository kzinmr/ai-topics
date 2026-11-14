---
title: "Releasing Personal Agent Protocol 1.0"
url: "https://sierra.ai/blog/releasing-poppy"
fetched_at: 2026-11-14T10:02:24.865957+00:00
source: "Sierra Blog"
tags: [blog, raw]
---

# Releasing Personal Agent Protocol 1.0

Source: https://sierra.ai/blog/releasing-poppy

Personal Agent Protocol
— or Poppy for short — has gained real momentum since we first announced this new standard with our initial design partners Meta, Genesys, Instinct, NiCE, Rocket, Shopify, Stripe, and Walmart last month. Poppy enables personal agents to interact with companies through business agents, websites, and APIs and today we’re excited to announce that:
v1.0 of the protocol is
now available
.
Shopify has enabled Poppy for every merchant on its platform.
Multiple design partners are now going live with Poppy, including Mercury, Synchrony, and Turkish Airlines.
Poppy is now on for everyone who uses Muse, Meta’s AI agent, which automatically looks for Poppy first on every site it visits.
60 new companies are joining as design partners, bringing the total to more than 100 — including
Affirm, Aflac, Agoda, Aircall, Akoya, Aviva, Banco Sabadell, Braze, Browserbase, Checkout.com, Cisco, Cover Genius, Creditas, Crunch Fitness, Cue, Delta Air Lines, Descope, EarnIn, Five9, Freshworks, Fullstory, Gen Digital, Global Payments, GoFundMe, GoodRx, Guardian, HealthEx, HelloFresh, Hyatt, Infoblox, Intuit, Kernel, Kin Insurance, Lemonade, Liberty Global, Manus, Mercury, Navy Federal Credit Union, Neptune Flood, Ora, Persona, Pindrop, Ping Identity, Profound, Prosus, Remitly, Runlayer, Salesforce (including Fin, Commerce Cloud, and Agentforce), Socure, SoFi, Symphony by Wix, The Knot, The Zebra, Travelers, Turkish Airlines, Twilio, Wayfair, Wix, WorkOS, and Zoom.
Poppy v1.0
Version 1.0 of Poppy reflects what design partners have learned over the past five weeks as they’ve tested the drafts against real websites, APIs, and agents.
The protocol defines how personal agents connect with companies that implement it, providing clear and comprehensive access to everything they offer, largely built with existing standards like MCP, OpenAPI, and UCP. With authentication through OAuth, customers control what personal agents can and can’t do, and can manage their access over time.
Since the initial draft, we’ve:
Made it easier for companies to adopt the protocol in stages, starting with the basics and adding capabilities over time;
Refined how the protocol uses existing standards;
Expanded a company’s ability to provide guidance and collect feedback from the personal agent;
Introduced extensions, such as the commerce extension co-authored by Shopify, so industries can build on the core protocol without changing it.
With v1.0, any company can implement Poppy on its own and immediately start delivering a better experience for customers who use Muse. Our
implementation kit
walks you through setup and includes a validator to check your work.
Sierra and Shopify bring Poppy to millions of merchants
Shopify powers businesses in more than 175 countries, and every Shopify store supports Universal Commerce Protocol (UCP) by default. As more shopping moves to personal agents, every Shopify store now automatically publishes a Poppy file, so merchants don’t need to do any extra implementation.
UCP and Poppy complement each other. UCP handles the shopping itself, like finding products, filling a cart, and checking out. Poppy handles what happens before that, when an agent shows up at a store, says who it is, and finds out what it’s allowed to do.
Shopify co-authored Poppy’s commerce extension, which links the two protocols. It lets an agent shop as a guest or sign in with the customer’s account, and it makes the agent ask the customer before taking certain actions, so it only acts with their permission. It also connects to UCP Ask, so a shopper’s agent can talk directly to the store’s agent.
Poppy in the wild
A number of businesses are now live with Poppy:
Mercury puts personal agents to work on finances:
People who use Mercury for business and personal banking can now ask their personal agent to check balances, review recent transactions, categorize spending, or keep budgets and receipts up to date. Customers can even ask their personal agent to initiate a payment or transfer, with Mercury ensuring the request goes through the account’s approval policy before anything is sent.
Synchrony will bring financing and rewards into agent-led shopping:
The work explores how a personal agent could help customers find the right product while considering affordability and relevant Synchrony offers and financing products along the way. Over time, that could create new ways to bring Synchrony capabilities into shopping experiences across their network of more than 500,000 merchant locations.
Turkish Airlines welcomes personal agents from search to business class
: Personal agents can now check out fares, flight status, and stopovers, as well as pull up a booking with a reference number and surname. Miles&Smiles members can even have their agent find business-class upgrades, which customers approve before paying. It’s now working to let members complete a purchase without leaving the conversation.
Choice, control, trust
We’re so grateful to all the companies that are contributing to this new standard, and excited to welcome more to our design partnership. As personal agents take on more of our everyday tasks, companies need clear, secure ways to work with them while continuing to deliver a trusted experience. Poppy gives them that foundation — so the company and the personal agent can get the job done for the customer they share.
Mercury is not a bank. Banking services provided through Mercury’s FDIC-insured partner banks.
