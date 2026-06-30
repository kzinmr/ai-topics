---
title: "How to get your Freshdesk API key (4 steps)"
url: "https://www.merge.dev/blog/freshdesk-api-key"
fetched_at: 2026-06-30T07:01:01.015868+00:00
source: "Merge Blog"
tags: [blog, raw]
---

# How to get your Freshdesk API key (4 steps)

Source: https://www.merge.dev/blog/freshdesk-api-key

Freshdesk, a product offered by Freshworks, offers an AI-driven ticketing platform that helps support teams provide better customer experiences at scale.
While the platform offers a variety of invaluable features and capabilities out-of-the-box, it can provide even more value when it’s integrated to your other internal applications or when customers connect it to your product.
Regardless of your integration use case(s) with Freshdesk, you’ll need to retrieve your unique API key in the platform. We’ll help you do just that below!
Step 1: Start a free trial or login
If you’re not already a user, you can
start a free trial
for any Freshdesk plan. Otherwise, you can
login to your account
.
Related:
A guide to retrieving your API key in Freshservice
Step 2: Click on Profile settings from your dashboard
Once you’re logged into your account, you should see the first initial of your first name on the top right corner. Click on that and then click on “Profile settings.”
Related:
How to generate your access token in Asana
3. Select View API Key
From your profile settings, you should see a button on the top right side that says “View API Key.” Go ahead and click this.
‍
4. Complete the CAPTCHA
The last step is completing the CAPTCHA. Once you’ve done that, your API key should appear!
Freshdesk will only show your API key once, so make sure to copy and secure it in a safe place!
Other considerations for building to Freshdesk’s API
Before building to Freshdesk’s API, you should look into and understand the following areas:
Pricing
Freshdesk offers four plans: “Free”, “Growth”, “Pro”, and “Enterprise.”
While there’s some overlap between the plans, such as the ability to edit and route tickets as well as create tickets from emails and social posts, the more advanced plans come with additional features and functionality. This includes supporting more products, assigning agents more custom roles, and monitoring your team’s activities on Freshdesk via an audit log.
Learn more about
Freshdesk’s pricing
.
Rate limits
The plan you’re on determines the number of API calls you can make to a given endpoint—and in aggregate—per minute.
If you’re on a free plan, you won’t be able to make any API calls. And as you move to more advanced paid plans, you’ll be able to make more calls per minute and additional calls per endpoint.
Learn more about
Freshdesk’s rate limit policies
.
Errors to look out for
While a wide range of errors can occur, here are a few of the most common ones
according to Freshdesk
:
400 client or validation error: when the request body or string is in the incorrect format or is missing when it’s required
401 authentication failure: the authorization header is wrong or isn’t present in the request
404 requested resource not found: if the requested resource, such as a ticket, doesn’t exist
429 rate limit exceeded: when your API rate limit has already been met in the current window
500 unexpected server error: when an error occurs on Freshdesk’s server
Final thoughts
Freshdesk
is a popular ticketing solution, but it isn’t the only one your clients use. They may also be using ticketing tools like Asana, Trello, or GitHub.
You can offer integrations with any of the tickets solutions your clients have by building to
Merge’s Ticketing Unified API
.
To learn more about the unified API, and Merge’s platform more broadly, you can
schedule a demo
with one of our integration experts!
