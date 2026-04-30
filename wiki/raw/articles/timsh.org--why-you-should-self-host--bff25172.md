---
title: "Why you should self-host your (vibecoded) app"
url: "https://timsh.org/why-you-should-self-host/"
fetched_at: 2026-04-30T07:00:51.411859+00:00
source: "timsh.org"
tags: [blog, raw]
---

# Why you should self-host your (vibecoded) app

Source: https://timsh.org/why-you-should-self-host/

Intro
Over the last 5 years I had to deploy more than 50 different services, both at the companies I used to work at, my personal projects and at my now-dead startup, Track Pump.
I started this journey with almost 0 knowledge about servers, dockers, CI/CDs and so on and learned all of the things I know now the hard way: days of downtime, bad unscalable processes, and, most importantly, lots of money spent on infra and services.
I deployed my first apps via cloud PaaSs like Heroku, hated it quite soon, moved on to Digital Ocean with many managed services, and ended up self-hosting almost every app that I worked or helped work on for the last year with Coolify on Hetzner VPSs.
And I'm very happy with the results I got: it works fine, requires almost no maintenance, costs very little money and looks good. I also helped a lot of my friends who run their own pet projects and startups to switch to this setup as well - all of them still self-hosting their stuff and enjoying all the benefits of it.
All this experience led me to the point where I am now: inviting you to consider ditching the cloud PaaSs and serverless things for the freedom and power of hosting your own stuff without having to obtain a system administrator degree / experience.
This post starts a new series about self hosting nuances with new ones coming soon.
Below I will talk about the reasons to self host (and the opposite) and cover two most important parts of my setup - cheap VPSs on Hetzner and Coolify - a self-hosted PaaS.
I also invite you to subscribe to the premium part of my blog which is currently entirely focused on detailed step-by-step guides on self hosting - with all my experience and knowledge translated into text, code and screenshots. It took me months of work to put it all together, and I believe it's worth quite a lot.
You can definitely learn all these things on your own (same as I did), but it will require time, effort and multiple attempts.
I believe that it would be extremely handy for an indie dev (or a vibecoder) launching their SaaS with little budget and no backing, or for a startup CTO / "the tech guy" who needs to set up all that corporate'ish things and apps - if I had this a couple of years ago, it would definitely save me a lot of time, money and nerves.
All right, I'll stop with the pitch and immediately move on to the rant.
Why and when you should self host
Let's talk about the alternative first: cloud PaaS and serverless approach (although these are different things) like: Vercel, Netlify, Heroku, all sorts of functions (AWS Lambda, Cloudflare Workers)... The list is long.
What is
good
about all of them:
You usually get a free* trial or tier that's just enough for your yet-to-be-famous app
You sometimes get to deploy your app in a few minutes with almost 0 knowledge (and sometimes you cry for 10 hours and still fail to launch your app on Heroku)
You get a nice clean next.js'ish interface to manage your apps
If you're really in a situation where your app has 1K users today and needs to be able to handle 1M users tomorrow - you get the scaling with almost 0 hassle.
Maybe there are other reasons, let me know.
Ok, this does sound kinda perfect... why would you not want this?
Let's go over the points above individually (I know I'm extremely biased).
Pricing
Most of these services feature "per usage" pricing, meaning that you pay for the amount of times / hours the app runs, and the bandwidth it uses, and so on.
This makes them free / extremely cheap while you have no traffic (= no revenue) but unpredictably expensive when you start getting your users.
There is this wonderful resource called "
Serverless horrors
" that accumulates some stories where people woke up to a dozen or a hundred thousand dollar bill due to... something. I don't want to re-tell those stories, and you've probably already heard them before - they happen all the time, more and more as more people and companies go for the nice UX and friendly-looking 0$ usage today.
But maybe this pricing is fair?
If you do get lots of traffic, don't you need a lot of servers to serve your app?
Doesn't it also mean that you're making a million dollars / second?
No! And in fact, some of the serious companies that do get to that "hyperscale" where you need to handle millions of users quickly realise that the deal they signed up for a year or two ago is tremendously bad (like
Amazon
lol).
They could literally save millions by just using a stupid, simple per-server approach, or even going all-in with their own infrastructure
like DHH did
.
Levels of abstraction
This is my way of summarising the "deploy in 1 click" value proposition: what level of deployment abstraction are you at? What level do you want to be at?
Let me explain: yes, if you follow a guideline, it's extremely easy to deploy your app in a couple of minutes on some nice-looking cloud PaaS - you don't need to worry about so much things like:
SSL certificates (you need them for the https)
Reverse proxy (Nginx e.t.c)
Security (lol)
Setting up your multiple "support" apps like databases
The list could go on and on.
But where's the catch?
I don't want to deal with all these scary things! I want my react app to be live right now!
Or maybe you do want to deal with these things, at least a little bit.
And maybe you overestimate how simple and intuitive it will be to deploy anything on Vercel (or any of their competitors).
What does this have to do with levels of abstraction?
Let's talk about the actual things that happen under the hood of this 1-click thing.
Like, what does the most basic deployment look like?
To me, that's a single python script with no dependencies running on Cron (or systemd timer): your app is just one single file, it can run anywhere you want (almost) and it does happen automatically every * * * * ** - otherwise it would be strange to call this a deployment.
At this level, there's almost no abstraction (at least none of what you want to dig into): your app is a single file, if you wrote right - it should work.
Your manually setup systemd config or crontab row tells your server to launch this exact file at some fixed time - and voila, it works!
Let's call this level 0 - yes, I know there is a ton of stuff under both cron / systemd and python - but I think most people don't need to think about running apps on a deeper level.
Ok, but what if I do use some dependancies in my script?
Then you'll need to install them, the correct versions, store and import them in your app.
At this point, you'll probably come to realise that you need a vurtual environment to keep these dependencies in the same place, separated from the outer world of your entire filesystem, and a package manager to install and update them.
Let's say this is layer 1 and move on quickly - I don't want to bore you with all of these layers + I'm not a real expert and I can say something stupid in the process - and who would want that?
Let's say that Docker is level 10: you have your isolated, originally empty environment wrapped into a cli with a set of commands that let you build, run and monitor your apps.
The goal is simple: you want your app that works locally to behave exactly the same on any sort of machine.
Already at this point it's quite complex to understand why and how all of this works - it takes time & a lot of thinking to learn Docker at a level where you don't simply copy-paste commands from the manual or your favourite LLM response.
PaaS services, for instance, are at a level 50.
You might not even know what's going on inside of it, you might not be able to play around with various parameters and tweak it to fit your use case.
If you go with the serverless functions, you don't actually know where and how they're being launched - what is the process behind it and why does your function cause some strange "Something went wrong" error.
OK, I'm obviously exaggerating and oversimplifying - I think with enough time and skill you can learn how all of this magic works, and maybe you'll even be able to tune the hidden settings somehow - but let's be real, you probably won't.
Here's what self-hosting does give you in this level of abstraction game: freedom.
You can setup 1-click apps in Coolify (which we'll cover later) and it will feel like the same magic as cloud PaaS things - launch once, use forever, forget about it (literally).
Or you could start from your own Docker-compose and tweak lots of things while still getting that magic feeling afterwards.
Or... you could just write a python script, setup a systemd task and run it at 00:00 every day...
On the same exact server that will cost you (per month) less than a single lunch.
Interface
I'll keep it short: Coolify and other self-hosted PaaS are very good-looking and user friendly! Almost as good as Vercel and co (or maybe even tiny better).
You can launch, stop, monitor and even edit your apps from your browser, on any device.
Finally, the scale
We got to the point where I might suggest you to go with the cloud PaaS and serverless.
If you:
have an app that is going viral at a lightspeed (your user base grows 10x a day)
have a lot of money in your account hooked up to the cloud provider
don't want to waste a couple hours (ok, maybe days) on learning how things work under the hood just a bit
-- maybe you should go with the serverless stuff!
I never had an experience of running such app.
I did, however, run apps that didn't deserve their $250/month checks to Digital Ocean. I still miss all that money :(
Or personal websites, surprising their owners with a couple-thousand-dollars bill in the morning due to some .mp3 file they decided to put in their "About" section.
And I'd seen crazily complex systems with millions of end users hosted on Hetzner, with self-hosted Jiras (ugh), Grafanas, Sentrys, Sentinels... and a hundred more services.
So, let's be real: do you really need that "scalability" part?
If no - I think you will save some money and be happy with your self-hosted setup.
In almost any case.
If yes - maybe it would be wiser to invest in learning about more complex things or hiring / getting advisory from people who have worked with such scale?
They might potentially save you a lot of money.
Ok, I hope I either convinced you to try self-hosting or spooked you with my judgemental rant.
Anyway, let's go over the whole setup I use and recommend.
Warning! If you're a serious DevOps or SRE or ... engineer who knows how to deploy something "the right way" - you might find this text to contain not-the-best approach to things.
This post is mostly intended for the people who don't have this knowledge or experience but still want to deploy things to prod without a panic attack OR burning down all their cash.
Server
First of all, if you want to self host stuff - you need a server.
I personally use (and love) two options:
My beelink 32GB RAM MiniPC that I have right under my monitor
Simple VPS on Hetzner, for example: 8 EUR/month for 3 vCPU + 4GB of RAM and 80 GB of disk space
Since I think not too much of you have a not-busy minipc at home to play with, I'll focus on a VPS option in this post.
First of, why Hetzner?
Simple: it's VERY cheap.
Previously I used Digital Ocean for their wonderful UX and managed everything.
Let's compare them:
Ok, this 7.55 EUR option falls somewhere between rows 5 and 6 in the second screenshot - let's say it's roughly $30, ok?
This is almost a 3.5x difference - but for what?
Short answer: for absolutely nothing.
There will be no long answer in this post, sorry :)
If you decide to go with Hetzner, please do a good thing and use
https://coolify.io/hetzner
referral link so that
Andras
, the wonderful man who has created Coolify, gets tome free Hetzner credits to host his own instances. You will also get around 25 EUR of free credits, ~3 months of completely free hosting!
In the end, it's still that "0$ now", right?
Little tip: avoid waiting for your account to be verified by using PayPal (I do hate it) as a default payment method. One more nice thing about it: Hetzner won't be able to automatically charge your Paypal account, so even if it gets crazy / evil and decides to take all your money - it won't be able to do so.
Coolify
Coolify is also a PaaS, but an open sourced one.
They do offer a cloud version, but we're obviously not going to use it.
Coolify is quite easy to install - it's just a single command:
curl -fsSL https://cdn.coollabs.io/coolify/install.sh | sudo bash
and offers a very wide variety of 1-click deploy apps - like Ghost which I use as a base for this blog, or any major database (shoutout to 16$/month managed Postgres on Digital Ocean), or ... well, the list is like
200+ apps
, you'll definitely find something interesting for yourself.
Even without the 1-click apps, it does a lot of heavy lifting for you, including but not limited to:
Automatic reverse proxy setup with Traeffik + issuing SSL Certificates using Let's Encrypt.
Essentially this means that after you setup your DNS so that any (sub)domain redirects to Coolify, you spend 5 seconds setting up a new service (on thinking about an appropriate subdomain).
Allows you to create automated workflows using Github Apps: push a commit to your private (or public) repo → service gets automatically redeployed with (almost) 0 downtime.
Has built-in and easy to setup Telegram notifications for deployments / errors, etc (lifesaver)
Handles logs, backups, environment variables...
Coolify is docker-based, so the easiest way to setup your own custom app in Coolify is by using docker-compose or just a simple Dockerfile.
First of, if you want to host some existing app which isn't directly available as 1-click setup resource, look for an install with docker-compose guide for that app. Oftentimes it will be enough: you just copy the file, choose "Start with an empty Docker-compose" in Coolify and you're all set.
But what about your own, custom apps?
Well, the approach is quite similar!
If you have, say, a node.js-based project that you work on locally, you can just... ask your Cursor or whatever to create a docker-compose for it, and it will just do.
I won't lie, it doesn't work like this every time, but quite often that's all it takes.
For example, I made 3 landing pages during last couple of months, all of them using Astro, and with all of them it toke me 1-3 iterations to "dockerize" them successfully.
Just imagine how this feels: you have your own (vibecoded) app and a very cheap server, and you get from localhost:8080 to
https://sub.domain.com
in 15 minutes.
It feels great.
Conclusion
That's it for today's post!
If you want to deploy your very first app, or if you need some services for your startup - I highly recommend trying Coolify out.
When I first installed it, I spent a few days just deploying 1-click apps and checking them out - there are a lot of neat OSS projects out there to explore!
In the next post I'll cover some of the services I use with my projects - including Ghost, Plausible, Grafana, Tailscale and others.
Once again, if you don't want to experiment by yourself and instead want a ready to go guide explaining how to self-host your app - subscribe and get access to all existing & future premium posts that I wrote.
