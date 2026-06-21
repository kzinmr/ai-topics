---
title: "Temporary Cloudflare Accounts for AI Agents"
source: "https://blog.cloudflare.com/temporary-accounts/"
author: "Cloudflare"
date: "2026-06-19"
date_ingested: "2026-06-21"
type: raw_article
tags: ["ai-agents", "cloudflare", "agent-infrastructure", "sandbox", "deployment"]
---

# Temporary Cloudflare Accounts for AI Agents

**Author**: Cloudflare  
**Date**: 2026-06-19  
**Source**: [https://blog.cloudflare.com/temporary-accounts/](https://blog.cloudflare.com/temporary-accounts/)

# Temporary Cloudflare Accounts for AI agents

2026-06-19
- [](/author/sid/)[Sid Chatterjee](/author/sid/)
- [](/author/celso/)[Celso Martinho](/author/celso/)
- [](/author/brendan-irvine-broque/)[Brendan Irvine-Broque](/author/brendan-irvine-broque/)
4 min read
Everyone&#39;s writing code with AI agents today. But the moment an agent needs to deploy something — and needs to sign up and create an account — it slams face-first into a wall built for humans: a browser-based OAuth flow, a dashboard to click through, an API token to copy-paste, a multi-factor authentication prompt to satisfy. For an interactive copilot sitting next to a developer, that&#39;s annoying. For a background agent, it&#39;s a hard stop.

Today we&#39;re rolling out Temporary Cloudflare Accounts for Agents.

Agents can now deploy [websites](https://www.cloudflare.com/solutions/frontends/), [APIs](https://www.cloudflare.com/products/workers/), and [agents](https://www.cloudflare.com/products/agents/) right away, without first needing to sign up for an account.

          
          
          
Any agent can now run wrangler deploy --temporary and deploy a Worker to Cloudflare. This temporary deployment stays live for 60 minutes, during which time you can claim the temporary account, making it permanently your own. If you don&#39;t, it expires on its own.

          
          
          
Our goal? Let your agent code and ship.

    
      
## Why frictionless deployments matter for AI agents

      
        

      
    
    
Frictionless temporary accounts matter more than it might first seem:
- 
Background AI sessions have no human in the loop, and are becoming the norm. Any auth step that needs a browser, a copy-paste, or &quot;click here in 60 seconds&quot; means an agent gets stuck and may choose to deploy elsewhere.

- 
Trial-and-error is the agent&#39;s superpower. Agents need a tight write → deploy → verify loop. They need cheap, throwaway deployment targets, so they can curl their own output and decide whether they got it right.

- 
Agent platforms are building their own ways for deploying code to &quot;just work&quot; without extra steps or credentials. People are starting to expect that this process just works, without the need to sign up for other services that they&#39;ve not used before or heard of.

    
      
## How it works

      
        

      
    
    
Temporary accounts are built around [Wrangler](https://developers.cloudflare.com/workers/wrangler/), our Developer Platform command-line interface (CLI) tool that lets developers bootstrap new projects, manage their configurations and resources, and deploy and update them.

Wrangler usage is widely [documented](https://developers.cloudflare.com/workers/examples/) online and agents know how to use it very well. But if you hadn’t yet signed in and granted Wrangler permission to your Cloudflare account, when the agent tried to deploy, it would get stuck at the sign-up and authentication step. And you might rightly ask: How do agents and LLMs know that this new --temporary flag in Wrangler exists, so that they actually use it without a human explicitly telling them to do so?

To solve this, we updated Wrangler to prompt the agent with a message that tells it about the --temporary flag:

          
          
          
When the agent discovers this, and then runs wrangler deploy again with the --temporary flag, Cloudflare provisions a temporary account for the agent to use, gives Wrangler an API token to work with, and provides a claim URL that the agent can give back to the human.

    
      
## Let’s go over every step of the flow

      
        

      
    
    
    
      
### Deploying and iterating on a new project

      
        

      
    
    
Make sure you’re using the latest [Wrangler release](https://github.com/cloudflare/workers-sdk/releases), fire up your favorite coding agent, and write a prompt to deploy a &quot;hello world&quot; app in build mode:

Make a very simple hello world Cloudflare Worker in TypeScript and deploy it using wrangler, don&#39;t ask me questions, do the best you can

The agent will run wrangler, pick up the --temporary flag from the output messages, build your script, and deploy it instantly, no human in the loop required:

          
          
          
As you can see, the agent wrote the script, deployed it using the --temporary flag, curled the preview link it got from the output, and verified that the result matches the code.

This is great, but agentic coding is often not about one single deployment. A session can go through a cycle of multiple code changes. This is not a problem: the agent can iterate on the Worker script and redeploy the changes as many times as it wants (within the 60-minute claim window). Type this prompt:

Now change hello world to &quot;hello cloudflare&quot; and redeploy

Look at the agent changing the source code, reusing the previously created temporary account, redeploying a new version and rechecking the result:

          
          
          
    
      
### Claiming the account

      
        

      
    
    
At any point, you can claim the temporary account and make it yours permanently. When you click the claim link you will be taken to a page where you can either sign up for or sign in to Cloudflare, and then claim the temporary account that your Worker was deployed to. This includes claiming not just Workers, but resources like databases and other bindings, too.

          
          
          
If you do not claim these temporary accounts within 60 minutes, they will be automatically deleted.

    
      
## The road to frictionless agentic deployments 

      
        

      
    
    
This is just one way we’re eliminating the signup barrier for agents. We recently [announced a partnership with Stripe](https://blog.cloudflare.com/agents-stripe-projects/) and a new protocol we co-designed that lets agents provision Cloudflare on behalf of their users — creating an account, starting a subscription, registering a domain, and getting an API token to deploy code, with no copy-pasting tokens or entering credit card details. Last month, we collaborated with WorkOS on the launch of [auth.md](https://workos.com/auth-md), which anyone can adopt, to let agents provision new accounts using well-established, existing OAuth standards. 

There’s a ton going on in this space, and we’re excited to keep making it easier for agents to use Cloudflare, and for developers to make their own apps [agent-ready](https://isitagentready.com/). Temporary accounts are one more step toward frictionless agentic deployments — stay tuned for more. 

Temporary accounts have some limitations, and their capabilities may change over time; check the [developer documentation](https://developers.cloudflare.com/workers/platform/claim-deployments/) for more information and then go build something. Point your agent at Cloudflare, see how far it gets, and tell us what we can improve or what delights you — share what you’ve built on [X](https://x.com/CloudflareDev) or hop into the [Cloudflare Community](https://community.cloudflare.com/).
 server-island-startconst headers = new Headers({});
let response = await fetch('/_server-islands/SocialLinks?e=default&p=&s=ACB827BCB712D5C6F9C3F0E2JO2ON%2FhzdzFvNxudNTVw8m%2FTJ1fX8X9YB339LTfl9epxwWRk8T1Oc3oiauY87NSbkVqRrcsqJkQcqC0mLn4AO1YLr%2B484aSUiHhsLJWLbn%2BdSbmsHeFqR2Hd8cyWWYvzVxuR3iUk%2FFko27FlN8Q7cW673UQs2YPFbp%2FIEAYU56K4rp1%2BEpthYGnMApAFqEwjwi2SZIJ%2Fxgnw2ARacAUMhR2qbLz2FByZlKamDskycw%2FndgV3jH9lvC4lxEOsF6XHZVsvkf7zZ4dt7efZ4UJrmXXdxQ%2BktxV0CsD8QHZRm%2B9uW0gvSuh%2Fi9trbKJycCT1F%2BpXb3y3Y%2Fd624jXfLtmFR9tcm0uM9Rly81eeOc3W3hKziwycydIvcDbKZZ%2F7TQA%2FQsi4LmGgPbajbX%2FXaQjGsnmpUK2zqAtx6MpT1IU%2B1jjY27IS8iio%2B5Vrf5m8kE%2BPR4KwteHG8oj1EQ%2BGkqW23Nup7v7PjogoUDAANtYWNjJmdD1aLe6L9TW6W0CQ9XaKsM0GkKgBmWPVSutVlTrUW%2BMqG9FxSzcUmxwgVlzKmv9GoxbRhuFsdWHnOOJ%2FsbkE8%2BUoBBaiHMrT89srUbHqZhIcAwI3ttm34XuwaKGsnsfsh%2Fe7zwNy5QcNCaxbjr8jmKfsF%2FVYNCqExJR5%2B0JLXi47niO5E3%2FVAHLH69CAUcRL6dfuaFjIoBtzUA4HZ9DlKD7xNEgfkprv9lqQ3kJxMh3w6ffvyEu%2ByeDLezfwC%2FT6ZdCCZjanvG8xgcsfYdZKhHurLd7laSm3U0L%2F4r%2FtGsdFba2WZ85%2BPZR2btiw8iGTlsEYFq0X2MwH1cBXJ%2FfyWlpvpookU1yEojyaVt6IEKRORqwAe6sqF8J7p9qHKIVDCzatOy%2F5MABdtprqdgPL9PtgujtPD7A9hgyLRTvDuoUq01zlYQozFJ%2BCYUCltsTIVDMup3pKk0XPg9gquLJZ6VxO9nZqtQLFE2MwHk%2BAeILzhmG2ZqleT8wNF%2B2C3WIRb4kY42mApkZT7KTeSMxrl%2FCyi%2FifvDPTVQuIclHAmY1PiGYs2lWNR3XB1f3%2FEJADvSveoTIg7IfHYYxZsF0sM8jWKEtF1awAUkOGk%2FuQrn13Kf74X28B4bOd2z7Uh3se42toq9VjLR1fdXPHsbCCNJP9YT9TY%2B6RvAB0ALE7%2F4DXJgsZ2%2F6lP1EQqKHSSX4BlKjN2yTVDi7upK3DicSHAnhPsM6ct1udfnwbwK7QCDdmkbndzffUB2dj3xpRJnavKJbrLQPi67lJed3b8XqVBFk9CSw5yv1r0A1xGof3uVI%2FacWGVJm5vwl3zi%2BgrSVrOyxmjdZoKKR%2FBXXYksIn50NbxfRqGcUyT4ETc16PscWS9pey0cGmGXVCl0DOOASrpm8EHnmWl8%3D', { headers });replaceServerIsland('97637341-42a0-430f-a615-722084f7b60a', response); [Agents](/tag/agents/)[Wrangler](/tag/wrangler/)[AI](/tag/ai/)[Cloudflare Workers](/tag/workers/)
