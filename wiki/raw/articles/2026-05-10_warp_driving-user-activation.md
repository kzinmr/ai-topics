---
title: "Driving User Activation: A Summer of Growth and Engineering at Warp"
source: "Warp Blog"
url: "https://www.warp.dev/blog/driving-user-activation"
scraped: "2026-05-10T01:27:21.005932+00:00"
lastmod: "2026-04-24T14:39:26.000Z"
type: "sitemap"
---

# Driving User Activation: A Summer of Growth and Engineering at Warp

**Source**: [https://www.warp.dev/blog/driving-user-activation](https://www.warp.dev/blog/driving-user-activation)

Product
Driving User Activation: A Summer of Growth and Engineering at Warp
Rachel Park
October 11, 2022
Rachel is a sophomore at Stanford University who interned with Warp during the summer of 2022. She’s worked across a couple early-stage startups and founded a non-profit for STEM education, where she discovered her love for the startup journey and building for impact. In this piece, she unpacks her experience and insights working across Warp’s software engineering and product growth teams.
Why I Joined Warp
As someone fascinated by the 0 to 1 process of tech, I wanted to take this summer to learn how to build great product, and make a real impact in crafting one. Now those two qualifiers, “great” product and “real” impact, can be hand-wavy and elusive in the start-up world, but when I learned about Warp through a mentor of mine, I figured I could be onto something. Speaking with founder Zach Lloyd and a couple people closely tied to the team, I quickly learned that I would get the opportunity to own meaningful projects that would help me grow as an engineer while being surrounded by
some of the most brilliant people
in the industry. As someone who is driven by the impact of code in solving real people’s problems, I aligned closely with Warp’s
product-first
ethos; what’s especially neat about building a product for developers is that engineers can truly drive product as well, since they’re solving a lot of their own problems. Plus, Warp’s recent public beta launch and quickly growing user base meant it was a pretty exciting time at the company—a time that made it the perfect place to learn how to build a product that users love.
Fast forward to June 8th 2022, the morning after my last exam of the school year, I was on a flight to NYC to kick off my internship with Warp’s all-team retreat and hackathon.
‍
The Warp team lined up by height for an activity at the 2022 NYC retreat. Didn’t realize how tall the team would be - I’m the 3rd shortest.
Working on User Activation
The key to crafting a great product is developing empathy to discover meaningful user needs, and addressing those needs with a creatively simple and easy-to-use solution. I was originally hired as just a software engineering intern, but after discussing my goals with my Warp mentors, I was excited to develop a deeper sense of user empathy and lean further into the product than the traditional Warp engineer by helping out with product growth as well. I set out to work on improving user activation, a particularly interesting and pressing problem as Warp began to gain virality.
What is user activation? Activation, the steepest portion of the retention curve, is a critical period in the user journey. This is all about the user’s small but unforgettable first impression of your product’s value, what convinces them to come back for the second time, then the third, and more. Activation can be broken up into several steps using the
Reforge
model:
Sign up: User joins the product
Setup moment: User is prepared to experience the core value proposition
Aha moment: User experiences the core value prop for the first time
Habit moment: User establishes habit around the core value proposition
Successful activation for Warp means getting new users to build a habit out of using the product (i.e. running terminal commands in Warp) several days a week within the first week.
‍
Sample retention curve with the activation period marked. As you can see by the pink dotted line, by boosting user activation, we can shift the overall retention curve up.
The coolest part of this activation project was that I could then bring in my engineering background to run the whole product lifecycle: after analyzing the frictions users face within the first week of using the product, I would be able to design solutions to decrease these frictions and improve activation, build what we came up with, and run experiments to see how what I built made an impact.
A question I’ve often been asked is how I divided my time across growth and engineering. The thing about working on a product lifecycle end-to-end is that the growth and engineering functions are like sine and cosine waves. Over the course of a project, when it’s time to prioritize user-facing tasks, the time spent engineering naturally comes to a lull until we have feedback to implement, and vice versa. This meant that I ended up working on each in roughly 5-week intervals, spending most of my time first tackling growth, then engineering, then a bit more growth again at the end.
‍
How to visualize working on growth and engineering across a product lifecycle. In my case, I spent the first five weeks focusing on user research (growth), then the next few building the product (engineering), and then testing the product and conducting more user research (growth), which then would theoretically become a continuous cycle.
Activation Study
To kick off the project, I needed to conduct research to understand the needs of first-time Warp users and the current state of Warp’s user journey. The goals of my study were (1) analyze the reasons that users dropped off within the first week of usage and (2) break down and define the different user activation stages for Warp. By defining the setup, aha, and habit stages for Warp, I could then work backwards from our goal of an engaged user to tighten the funnel and increase retention.
To do this, I conducted over a dozen observed onboarding sessions, recruiting people to explore Warp for the first time as we watched. These hands-off user research sessions helped us better understand the entire first-time user experience; we could hear not only how they felt, but also why they felt that way. When a user exclaimed “Ooh!” I noted it down as a potential Aha moment and asked what was going through their mind. When a user asked about something in the app, I noted it down and asked how they would look for an answer, then noted that down. It was fascinating how these user research sessions uncovered so many fixable micro frictions, as well as some larger rough edges, that had been lost in the quantitative data.
I then combined my observations with an analysis of our overall funnel and retention data to present 3 key findings to the entire team:
Warp has a “blank screen” problem. Users land on an empty app and it takes too long  for them to see Warp’s core value prop.
This core value prop lies in
blocks
(the unique way that Warp groups together commands and their output). But since most users currently do not understand the concept of blocks during their first time in Warp, they don’t experience a true Aha moment.
We have a pretty good pulse on upcoming features and the product roadmap, but need to work on leading users to the value of existing features
We were able to fix some of the low-hanging fruit along the way to bump our retention curve up a bit, but now it was time to build something that made a significant impact.
Building Onboarding 2.0
With these insights, a couple teammates and I began to brainstorm solutions for a revamped product onboarding experience, coined “Onboarding 2.0”. As we floated everything from flashy animations to block-based tours, I found putting together a spreadsheet that weighed the ideas along a couple dimensions to be helpful in evaluating the best solution:
‍
Weighing ideas along the axes of effort (how much work is it?) vs. impact (how much does it help you reach your goals?) is a reasonable framework for evaluating what to prioritize and build. The blue circle marks the sweet spot, when we can have the highest impact with the least amount of engineering effort.
Using this framework, we decided that a block-based onboarding and gamified “Getting Started” checklist would be the most viable and impactful way to lead users towards discovering our core value prop of blocks, as well as other valuable features in Warp. Prioritization is hard—it was challenging to scope some brilliant ideas out of the v0, but if anything, we could experiment further later.
A demo of the revamped onboarding experience we ended up building. First-time users now land on a “welcome” block, which points to the new permanent resource center. The resource center contains a “Getting Started” checklist for the user to complete, along with other tips and resources to explore.
As we were designing the implementation of these features, I learned how Warp’s codebase is shaped by its user-focused mentality. One of the challenges we faced with the resource center was building a system for easy content updates that was agnostic to product release cycles. The goal was for anyone on the team to be able to run experiments with the features and content highlighted in the resource center to make sure it was helpful for users. We considered, for example, storing the resource center data as a JSON file in the cloud and building an API to retrieve it every so often. However, we ultimately decided that this would be too much engineering overhead for a v0 that didn’t have any user feedback yet—user feedback that would not only help us optimize the UI/UX design, but also the implementation design as we contemplated the format of the JSON data, the update frequency, and other requirements of a cloud-based system. So although a cloud-based system seemed like the correct way to go long-term, we tabled the discussion and decided to temporarily hard-code the content to prioritize shipping the feature as quickly as possible.
Testing Onboarding 2.0
Once we built the v0 of the welcome block and resource center, we wanted to test our solution by observing real first-time users interact with the product. This time, we took another approach. The first iteration of user research had required a lot of manual coordination and gave us results with some recruiting bias. Many of the people who signed up for an onboarding session were low-intent users and people in our team’s network. They were only trying Warp either because of the cash reward of participating in UX research or because their friend was working at Warp, which biased the way they approached the app for the first time. But these low-intent users were only a subset of those who usually tried out Warp.
To make sure we weren’t over indexing on problems raised by only a subset of our users, we ran an experiment with live onboardings. By inserting a screen into our sign-up flow that gave users the option to join an onboarding call, we were able to gather live feedback on our new onboarding experience from real users. To build this, we ended up creating a server side app in Retool to make toggling the onboarding screen as easy as possible.
Through these live onboardings, it was awesome to see some early validation in the product we built and to find a couple more kinks to iron out before the public launch. Users immediately began to understand and play around with blocks; I heard the audible “Ooh!” as users discovered Warp’s core value prop so much earlier in the session than in my previous run of onboardings. And although my internship is coming to an end right as we launch our revamped onboarding experience to the public, I’m excited to follow how it impacts our retention rates over time.
What I Learned
As I look back all that I’ve learned during my time at Warp, here are some of my greatest takeaways:
‍
1. Listen closely, and use data sensibly to cut through the noise
It can be tempting to solely optimize for metrics, using metrics. But I learned that only focusing on the quantitative data can turn a blind eye to subtle, yet important details that may break user trust. For example, given that our retention charts indicated relatively higher churn rates for experienced developers, the next logical step would have been to keep building out new features to try and match Warp to their original terminals.
It must be because experienced devs are missing X advanced integration or Y feature that they stop using Warp.
It’s only by watching and listening to users in our observed onboardings that we found that it didn’t matter what valuable features Warp had: experienced developers tended to have dotfile configurations with custom tools and plugins that created a buggy experience when opening Warp for the first time. The users didn’t know their dotfiles were incompatible, so they immediately churned because they thought the product was just super buggy. Zero value discovery.
When it comes to developing empathy with users, nothing beats first hand exposure to their experiences and reactions. It may not be as obvious as a bug; everything from the facial expressions they have to the questions they ask to where they move their cursor as they try out the product can help identify subtler user needs. Yet it’s also easy to become overwhelmed by all these qualitative observations, and this is when we can harness quantitative data to help shape our understanding. In my activation study, for instance, this is how I was able to identify our magical Aha moment. Using stickiness data analysis, I was able to narrow down all the “Ooh!”s I observed in the user research sessions to the one most correlated with retention: blocks.
Striking a balance between qualitative and quantitative data is crucial to building for impact.
2. Ask “Why not?”, then figure out how to build quickly
Figuring out how to build the right stuff is tough. Most people ask “Why?” when evaluating what to build. But I’ve learned that framing the question as “Why
not
?” leans into an idea, promoting a bias towards experimentation that propels you towards creating something that people love. If there isn’t a good enough reason stopping you from trying something out, the execution is most likely a matter of scoping. This is how we decided to go forward with the block-based onboarding; while we were initially hesitant about it because our ideal vision was a bit ambitious, we decided to scope it down to a single “welcome” block and observe how users reacted in order to see if the ultimate vision was worth building out. Now that there was relatively low tradeoff, why not?
Combined with lesson #1, this risk-tolerant mentality creates a killer iteration cycle for building products people love. Note that you should still keep first principles in mind and evaluate the idea on the axes of engineering effort vs. impact to make sure you’re not hovering too far into the danger zone (high effort/low impact), though you can never truly tell the impact of something without testing it out first. If you can build an MVP of an idea without much effort, do it. If you can’t, figure out how to scope the idea down so that you can.
Warp encourages its engineers to try out their ideas, accelerating its shipping velocity and delivering impactful results; many of Warp’s most loved features started out as side projects (e.g.
AI Command Search
). So now, whenever I’m making a decision, I remind myself to lean in and ask, “Why not?”
3. Communicate clearly and early
Warp’s team culture is centered around compassionate and efficient communication. Zach sets a precedent for this by outlining the company’s core values and principles in the
How We Work guide
, which encompasses everything from hiring the best talent to the art of a Slack message. As I was running the product lifecycle and collaborating across different functions, I learned how building an explicit foundation of written and visual artifacts, like the How We Work guide, helps the team align efficiently and work as productively as possible. When I was running product meetings, this meant sending out agendas, PRDs, mocks, and other important documents beforehand so that the precious meeting time was used for collaboration and discussion. When I was engineering, this meant sharing demos and getting partial features launched internally as quickly as possible to get feedback. Especially for engineering, communicating early and often is important as it’s easy to get sucked into building something that may actually be solving the wrong problem or using an overcomplicated approach (i.e. building a cloud-based system for the resource center content, as mentioned earlier). Warp instills a collaborative culture where everyone believes that there’s a huge advantage in leveraging the team’s collective wisdom to build better and faster, and communicating early and efficiently is key to unlocking this collaboration.
As a meta point, just as it’s important to develop a product iteratively with users, it’s important to develop these processes iteratively with the team—to communicate about communication. During my time at Warp, the team was growing so quickly that many of the standing company-wide meetings and norms became unwieldy and unsustainable. It was because of Warp’s open culture of communication that we were able to identify this and adapt collaboration norms to a growing team. As I absorbed Warp’s core values, I also loved learning how to iterate on team culture and processes to continue to uphold these values.
Conclusion
I feel lucky to have been able to work across so many domains at Warp, truly “learning by doing” as I delved into everything from user research to engineering to even some design. Learning how to navigate the codebase efficiently, architect sound code, and of course, develop in Rust, among other learnings, I’ve surely grown exponentially as an engineer. But I think even more valuable is how running the whole product lifecycle with Warp’s pragmatic, collaborative, and user-focused culture fostered my overall growth as a product builder. I developed generalizable principles around decision making, building, and working as a whole this summer that will surely serve me for my entire career and help me pursue my most ambitious dreams. And I learned a bit about user activation, too.
Thank you, Warp, for helping me learn and grow more than I could have ever imagined.
Team bonding with Warp SF
Related articles
Apr 28, 2026  ·  7 min
Warp is now open-source
Warp is now open-source, and the community can participate in building it using an agent-first workflow managed by Oz, our cloud agent orchestration platform.
Apr 14, 2026  ·  2 min
Introducing Universal Agent Support: level up any coding agent with Warp
Warp now supports the most popular CLI coding agents — including Claude Code, Codex, Gemini CLI, and OpenCode — with vertical tabs, notifications, native code review, rich input, and remote control, making it the best terminal for multi-threaded agentic development.
Mar 24, 2026  ·  7 min
Build vs buy: how to deploy coding agents at scale
Should you build an in-house agent orchestration system or buy one off the shelf? Here's how to think about the decision and where the real complexity lies.
