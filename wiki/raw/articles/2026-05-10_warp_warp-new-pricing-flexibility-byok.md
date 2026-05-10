---
title: "Changes to Warp’s pricing: Introducing Build"
source: "Warp Blog"
url: "https://www.warp.dev/blog/warp-new-pricing-flexibility-byok"
scraped: "2026-05-10T01:28:21.801314+00:00"
lastmod: "2026-04-28T21:59:37.000Z"
type: "sitemap"
---

# Changes to Warp’s pricing: Introducing Build

**Source**: [https://www.warp.dev/blog/warp-new-pricing-flexibility-byok](https://www.warp.dev/blog/warp-new-pricing-flexibility-byok)

Company
Changes to Warp’s pricing: Introducing Build
Zach Lloyd
October 30, 2025
Today we’re updating how Warp’s paid plans work.
We are moving to a simpler structure: one single, $20 per month plan, plus usage-based credit reloads and bring-your-own-key (BYOK) for folks who want more AI.
No bones about it: this plan will be more expensive for some users and less expensive for others. Based on current usage data, over half of Warp users will see their monthly cost go down – or increase by less than $2 per month.
Starting today, we are:
Introducing a new usage-based plan called Build, which starts at $20 per month with 1,500 credits
Deprecating Warp Pro, Turbo, and Lightspeed
Updating the Business plan to mirror the Build plan, at $50 per month, including SSO and ZDR controls
By popular demand, supporting BYOK on the Build and Business plans
Decreasing the cost of pay-as-you-go AI credits, which are now ~50% cheaper, roll over month to month, and remain valid for 12 months
Drilling one level deeper, these changes address a couple of issues with our current Pro, Turbo, and Lightspeed plans:
Many users don’t use all the credits they pay for. On the Build plan, you pay for what you use and credits roll over month to month.
The credits that came with our legacy plans were much cheaper than our pay-as-you-go overages, to the point where our overages were eight times more expensive, and users who exhausted their plans felt like overages were a rip-off.
At full usage, the plans didn’t scale sustainably. This problem was getting worse, because folks were finding more and more value from Warp’s AI, using more of their plans, and Warp was losing more money as a result. The new plan sets Warp up to be around for the long term.
We get that there’s a lot of whiplash in the AI devtools pricing market, and sympathize. While we expect some churn from this change, we are trying to do it in as minimally disruptive a way as possible.
For
new customers
, these changes become effective immediately.
For
existing customers
on Pro, Turbo, Lightspeed, or Business, these changes will take effect at your
first renewal after December 1, 2025
.
At that time, your invoice will update to the new $20 monthly Build plan, you’ll gain access to Bring Your Own Key (BYOK), and benefit from our new Reload Credit pricing.
If you’d like to move sooner, you can switch to Build at any time by following the steps outlined
here
. When you switch, your account’s used credits will automatically reset to
0 / 1,500 monthly credits
.
Any unused value from your previous plan will be credited to your Stripe balance
, which can be applied toward future Build payments or Reload Credit purchases.
You can find more information on our
pricing page
.
I recorded a short video explaining the thinking behind this pricing update.
Introducing Build
We’re consolidating our paid subscription plans into one usage-based plan, called Build
The Build plan comes with:
1,500 AI credits
per month which can be used across leading AI models
Bring-your-own API key
for OpenAI, Anthropic, and Google models
Access to Reload credits
with volume-based discounts
Unlimited Warp Drive objects and collaboration
Highest codebase indexing limits (up to 40 repositories with 100,000 files each)
Bring your own key (BYOK)
BYOK has been a
top issue
on our GitHub for a long time. Many developers are already paying for OpenAI or Anthropic access and want to use that within Warp.
On the Build plan, you can now add your own key for OpenAI, Anthropic, or Google models by navigating to Settings > AI in your Warp application. When you add a model, we will use your API key within our top-quality agent harness. You’ll pay model-providers directly for all AI usage. Learn more in our
Bring Your Own Key (BYOK) documentation
.
Currently, BYOK is not available on the free plan. This is because even with BYOK, it’s not free for us to run our agent harness (it runs on our server), and we provide many other cloud features with variable costs that the paid plan helps us cover.
Worth noting when using your own key:
Warp does not have control over any privacy settings regarding data-retention and training by model providers.
Active AI features like prompt suggestions and codebase indexing will continue to work, but will not count against your personal API key usage. We foot the cost of those features ourselves.
Reload credits
Reload credits are replacing the “pay-as-you-go” overages model previously in Warp.
You have two options for purchasing more credits:
You can buy them on-demand
You can enable auto-reload, setting a cap on monthly spend
In either case, you can choose to purchase credits in increments of $10, $20, $50, and $100. The more credits you buy at once, the cheaper they become.
Reload credits are 50% cheaper per thousand credits than the legacy overage credits and much closer in price to the base credits included in Build.
Reload credits roll-over month-to-month and remain valid for 12 months. When your credit balance renews at the beginning of each billing cycle, Warp will first use your monthly credit balance, before continuing to consume Reload credits.
For teams on Reload plans, credits are shared across all members. Team admins can manage when and how credits reload – including enabling auto-reload, setting monthly spend limits, and choosing reload increments directly in
Settings > Billing and usage
.
Opt in and choose a reload amount when subscribing to Warp Build, or change this at any time in
Settings > Billing
.
Business Plan Updates
We’re updating the Warp Business plan to align with the new pricing structure and make it easier for teams to manage AI usage at scale. The updated Business plan is now $50 per user per month, and includes:
1,500 monthly AI credits per user
(credits are assigned individually and do not roll over)
Shared Reload credits
that can be purchased and used across your team, roll over month to month, and are valid for 12 months
Bring-your-own API key (BYOK)
for OpenAI, Anthropic, and Google models, available for all individual users
Single Sign-On (SSO) and universally applied Zero Data Retention (ZDR)
for enhanced enterprise-grade security
Self-serve billing: credit card payments only, with no invoicing or account management
Team size limit of up to 50 members per team
Your feedback matters
Beyond aligning Warp’s pricing structure with usage, we’ve been making Warp’s AI requests more efficient: better prompt design, improved conversation segmentation, and smarter tool-calling patterns. We’ve also been investing in
AI credit transparency
, and recently released some
tips for being more credit-efficient
.
Our product is rapidly evolving. Let us know what’s working and what isn’t. We can’t make every request happen right away, but your feedback helps us design what’s next for Warp.
FAQs
When will the new pricing take effect for my account
For
new customers
, the new pricing and packaging take effect immediately.
For
existing monthly subscribers
, changes will apply on your first renewal after December 1, 2025; most likely during the month of December, 2025.
For
annual subscribers
, the new plan and pricing will take effect on your next renewal after December 1, 2025.
What happens to my current plan (Pro, Turbo, Lightspeed)?
You will retain your current plan and credits until December 1, 2025. All current Pro, Turbo, and Lightspeed plans will be switched to the new Warp Build plan at renewal. The Build plan includes 1,500 monthly AI credits, Reload credits that roll over for 12 months, and the ability to bring your own API key. For Turbo and Lightspeed users, we will enable auto-reload up to your current plan limit ($50 /$225 respectively).
What happens when I change from my current plan to the new Build or Business plans?
If you move from Warp’s legacy Pro, Turbo, Lightspeed, or old Business plans to the new Build or Business plans:
You’ll receive a prorated credit balance on Stripe for your current plan, based on how far you are into your billing cycle. This balance can be applied toward monthly Build fees or any Reload Credits you purchase.
You can view your credit balance by going to
Settings > Billing and Usage > Manage Account
. You can also view your credit balance on the Stripe invoice that was sent when your plan changed to Build or Business.
Your credit balance will reset to 0/1,500 when you switch to the Build or Business plan.
If you switched immediately after the rollout, before a subsequent update was applied, we’ll retroactively reset your credit balance to 0/1,500. You should see this reflected in Settings > Billing and Usage. If you experience any issues, please contact us at build-priority@warp.dev.
Will I be paying more on this new plan?
Not everyone will have an increased price. Some will pay more. Others with very heavy, or very light AI usage will likely see their costs go down. The new plan is designed to better match what you actually use, so you’ll pay more fairly based on your usage than fixed limits.
Are there free AI credits available?
Yes, new logged-in users receive 150 AI credits per month for their first two months on the Free plan, and 75 AI credits per month afterward.
Can I continue to use Warp as my primary terminal?
Yes, the Terminal features of Warp will continue to be free to use for developers across Windows, Mac, and Linux.
How are Reload credits different from overages?
Reload Credits replace overages with a simpler, prepaid system. They’re up to 50% cheaper than the old overage rates, roll over month to month, and remain valid for 12 months.
They also include Warp’s Zero Data Retention protection policy with all contracted LLM providers – no customer AI data is retained, stored, or used for training.
Do credits rollover?
For existing users, plan credits on Pro, Turbo, and Lightspeed do not rollover. Neither will pay-as-you-go overage credits.
For the Build plan, credits will not rollover but Reload credits will rollover and be valid for 12 months from the date of purchase.
What happens if I’m on an enterprise plan?
There are no changes to the existing enterprise plans. Our Sales team is ready to help anyone interested in Enterprise plans:
please reach out
.
Can I bring my own key on my current plan (Pro, Turbo, Lightspeed)?
No, Bring-your-own API key for OpenAI, Anthropic, and Google is only available to users on the Warp Build plan. You can choose to switch your existing plan to Warp Build at any time before your applicable renewal date to access BYOK.
How does the monthly spend limit work?
Your monthly spend limit is the maximum amount you can spend on AI credits within a calendar month. Once you reach that limit, additional purchases won’t be processed until you either increase your limit or select a smaller Reload Credit amount.
A monthly spend limit only applies if you’ve enabled auto-reload, which automatically purchases Reload Credits whenever your balance is low.
Auto-reload settings:
New users
who enable auto-reload start with a $200 monthly spend - limit by default.
Existing paid plan users
who enable auto-reload will have their limit set to match their previous overages spend limit (if configured; otherwise $200).
What about other Warp features? Will those still be accessible?
Yes, the rest of Warp’s features remained unchanged. You have unlimited Warp Drive objects, 100K file codebase context, and other terminal and collaborative features.
Should I subscribe to the Build plan or the Business plan?
If you’re an individual developer or part of a small team, the Build plan is the best fit. It includes 1,500 monthly AI credits, discounted Reload Credits for additional usage, and the ability to bring your own API key (BYOK) for OpenAI, Anthropic, or Google models. You’ll also get unlimited Warp Drive objects, collaboration tools, and the highest codebase indexing limits.
If you’re part of a larger team (up to 50 members) that needs advanced administrative and security controls, choose the Business plan. It includes everything in Build, plus SSO, enforced Zero Data Retention (ZDR), shared Reload Credits that can be used by all team members, and centralized billing – ideal for organizations that need stronger security, compliance, and team-wide management.
Related articles
Apr 28, 2026  ·  4 min
The virtuous loop of open, automated development
With today’s open-sourcing of Warp, our goal is to create a new way of building, where humans and agents collaborate in the open to ship better software, more quickly.
Mar 16, 2026  ·  8 min
What happens when you give the company 4 hours to automate everything
The Warp team held a company-wide hackathon to build with Oz, our cloud agent platform. Here's every project, from docs migrations to churn detection, that shipped in just 4 hours.
Feb 10, 2026  ·  12 min
Introducing Oz: the orchestration platform for cloud agents
Run hundreds of coding agents in parallel with full visibility and full control
