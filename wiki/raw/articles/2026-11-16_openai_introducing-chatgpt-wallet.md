---
source_url: https://openai.com/index/introducing-chatgpt-wallet/
ingested: 2026-11-17
sha256: chatgpt-wallet-jina
hn_note: HN 46p/80c https://news.ycombinator.com/item?id=50518501 (low traction vs expected; see thread skepticism)
retrieval_note: openai.com direct fetch 403; full text captured via r.jina.ai proxy 2026-11-17
---

Title: Introducing ChatGPT Wallet

URL Source: https://openai.com/index/introducing-chatgpt-wallet/

Markdown Content:
We're introducing ChatGPT Wallet, setting a new bar for secure payments by agents. It's the first wallet that lets agents pay without access to users' actual card details and that requires a security check for every purchase, while also preserving existing card rewards and protections for eligible disputes. Built in partnership with American Express, Chase, Mastercard, and Visa, ChatGPT Wallet will initially be available through dots for ChatGPT Pro subscribers in the US. Alongside ChatGPT Wallet, we're releasing tools and guidance to help businesses support customers using agents.

1.2B people use ChatGPT each week, and many of them turn to it to research products, compare options, and decide what to buy. With ChatGPT Wallet, we're now helping people complete purchases, and giving their agents a way to pay that businesses can accept with their existing systems.

To accept payment from ChatGPT Wallet, websites need to ensure agents are not inadvertently blocked, and payment and risk systems need to recognize legitimate purchases made by agents. We're starting with limited availability to ChatGPT Pro users, so we can learn from real-world use and work with businesses, banks, and payment networks to improve compatibility and reliability.

## How a purchase works

ChatGPT Wallet gives agents a secure way to pay on a user's behalf. Users add a card once, then approve each purchase without re-entering their payment details.

Before each purchase, the user reviews the items, total, and selected card, then approves it with a security check such as Face ID or a fingerprint scan. Each approval creates a clear record of the purchase the user authorized the agent to make.

After the user approves, the payment network provides a payment token—a substitute for the user's actual card details—with a card number, security code, and expiration date. The payment is charged to their selected card without ChatGPT Wallet sharing their actual card details with the business or agent.

We're building agent-led commerce to fit reliably into existing systems. Users keep their card's existing rewards and protections for eligible disputes with businesses, for example when an item is defective. Banks and networks bring their expertise to evaluating transactions. Users transact directly with businesses, which keep their customer relationships and control over pricing, fulfillment, returns, and customer service.

Over time, we expect users to be able to delegate purchases entirely to their agent by setting clear parameters—such as spending limits, purchase categories, or time periods—and pre-approve those purchases with enhanced safeguards that build on today's protections, including biometric checks and clear records of authorization.

## Equipping businesses for agentic commerce

Agentic commerce is still in its early days. As agents begin to take on more shopping and purchasing tasks, many websites and payment systems are still adapting to this modality. Some sites may unintentionally block purchases through ChatGPT Wallet or other agentic payment products, and we are focused on helping businesses make that transition.

Alongside ChatGPT Wallet, we're publishing a Commerce Partner Playbook (https://developers.openai.com/commerce) with tools and practical guidance to help businesses support customers using agents through their existing websites and systems. It covers making product information available, ensuring agent access, and working with payment and risk providers to reduce unnecessary declines. Businesses can start with the areas most relevant to their customers:

* **Help customers find accurate product information.** Claim your business in ChatGPT and, once verified, update your business details and upload a product feed with current pricing and availability.

* **Ensure ChatGPT agents can access your website.** Configure your CDN or firewall to recognize signed requests using Web Bot Auth and confirm your general site security measures are not inadvertently blocking ChatGPT agents. Browser access does not require a plugin or product feed.

* **Work with your payments and risk providers to support agent purchases.** Wallet's payment tokens work with existing checkout flows, but risk systems may still flag legitimate purchases made by agents, leading to declines or cancellations. You can work with your providers to understand how they recognize these transactions. We're also working with fraud prevention partners including Forter, Riskified, Sardine and Signifyd and payment service providers including Adyen, Checkout.com, and Stripe to help their systems recognize legitimate purchases made by agents.

* **Give agents more ways to work with your business.** Build a plugin to let agents check availability, manage carts, or take other actions through your existing systems. Websites can also add WebMCP tools.

## Availability

ChatGPT Wallet begins rolling out today in dots, enabling users to have their dot complete purchases on their behalf. It will initially be available to ChatGPT Pro subscribers aged 18 and older in the US with eligible US-issued cards. We'll work with businesses, banks, and payment networks to learn from early use and expand availability, helping more customers and businesses benefit from agentic commerce.
