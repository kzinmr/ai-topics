---
title: "A really cheap chatbot in Python"
url: "https://boyter.org/posts/really-cheap-python-chatbot/"
fetched_at: 2026-05-05T07:01:58.413913+00:00
source: "Ben Boyter"
tags: [blog, raw]
---

# A really cheap chatbot in Python

Source: https://boyter.org/posts/really-cheap-python-chatbot/

Let me start by stating that I think all chat-bots are rubbish and that a better solution is a decent search implementation. Type in some terms and get some useful results. Much better than typing to a machine.
A while ago I was working at a client site where there was an internal discussion group about building a chat-bot. Many meetings had passed, discussing using neural networks, building flows, should we use IBM Watson. Lots of talk, but not much delivery.
Personally I am a man of action. Throw things at the wall, see what sticks and double down on it. Endless discussions covering the same ground might feel productive to some people but not myself. So I made a plan. During the next discussion while it was happening see if I could write a cheap chat-bot that was further along than anything else delivered, which was not hard as nothing had been delivered.
Generally most chat-bots are trying to work out what you want, and the funnel you down some path. In effect moving you through a decision tree. Thats what this client was attempting to create as well.
So given that I decided to create a very simple decision tree, and then code around that. I took the companies own help/about pages on the company website to get keywords, and built a simple work-flow where you either learn about the company or attempt to pay a bill using credit card or paypal.
The result of my interacting with the bot is included below.
Hello! RCC (really cheap chatbot) here what are you trying to do today? At any time type quit to quit.: i want to pay a bill

Do you want to pay your bill using a credit card or using paypal?: credit card please

You can pay online using your credit card at <https://plumbus.com.au/pay>
Hello! RCC (really cheap chatbot) here what are you trying to do today? At any time type quit to quit.: pay bill

Do you want to pay your bill using a credit card or using paypal?: dunno
Sorry I did't quite catch what you were saying. Could you try typing it using different words please.

Do you want to pay your bill using a credit card or using paypal?: credit card mate

You can pay online using your credit card at <https://plumbus.com.au/pay>
Hello! RCC (really cheap chatbot) here what are you trying to do today? At any time type quit to quit.: pay bill using paypal

You can pay online using paypal at <https://plumbus.com.au/paypal>
Hello! RCC (really cheap chatbot) here what are you trying to do today? At any time type quit to quit.: i want to learn the history of your company

We're the leading Australian company supplying things to 4.2 million customers and developing and producing natural widgets. We also aspire to be the number one plumbus company in Australia.
It turned out really well for the 30 minutes or so it took me to code it up. Well somewhat. I think I may have annoyed some of the more senior people in that group as I was then excluded from further meetings. Seeing as the code was never actually used nor even put into source control I thought someone might like mocked version I created. You can find it on github
https://github.com/boyter/really-cheap-chatbot
