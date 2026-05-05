---
title: "Vibe coding searchcode a new UI and saving myself 40+ hours of work"
url: "https://boyter.org/posts/searchcode.com-vibe-coding/"
fetched_at: 2026-05-05T07:01:54.570751+00:00
source: "Ben Boyter"
tags: [blog, raw]
---

# Vibe coding searchcode a new UI and saving myself 40+ hours of work

Source: https://boyter.org/posts/searchcode.com-vibe-coding/

I have been working on a secret project within
https://searchcode.com/
and ran into a blocker where the UI had become a road-block. I will be the first to admit that I do not like styling things with CSS very much. In fact working with HTML and CSS is probably my least favorite part of modern web development.
I have never discussed any use of “AI” on this blog. Not for lack of using it, as I had been using ChatGPT and other tools since day one. I had always previously found that the models were a neat party trick, but had a lot of issues dealing with code. Given the new
“vibe coding”
shift that been happening in the industry I thought I would give it a go, and use it to redo the searchcode UI.
I did however outline the following rules, which while technically are not “vibe coding” but close enough.
I was going to not give access to my codebase. I didn’t want any tool to have that power right now, and being a greenfield redesign it didn’t matter that much.
During iteration I would not modify or tweak the CSS in any way, relying only on prompts.
The strongest model I had easy access to at the time was Grok 3 so, Sunday afternoon I sat at my desk with the following prompt.
You are now my HTML CSS guru. We are going to rebuild the searchcode.com site together. 
I will describe each page and we will then build the HTML and CSS together for it. 
While I am familiar with code, and the ideas behind CSS I am not familiar with 
modern techniques. You will up-skill me in CSS as we do this. 
We are going to remake it with the following things.

It will be responsive.
It will support dark mode.
It will not use any frameworks.
We will use flexbox for layout stuff (unless you have a reason to not do so).
We will make a modern clean design.
We won't use any custom fonts, as we want it to load as fast as possible.
We will ensure its good for SEO.
We want shared components to be re-usable, I will tell you which parts they are.

We are going to do it part by part.
Lets start with the home page. We want a basic HTML page to start. 
The layout should look a bit like google, with a navbar, with links to home, 
about and api on it. We also want a smaller version of the logo on the left for this. 
Then we want some space, then a centered logo, under it should be a 
search input box with a button next to it. Under that we are going to 
list some example searches as links E.G. Format, re.compile lang:python
With the prompt done, I poured myself a nice glass of wine, and dutifully copy pasted the outputs into index.html and a styles.css file, refreshing my browser as I went. I spent the next 3 hours or so going back and forth with the model for each page I needed to recreate.
A few things occurred to me while doing this.
A larger context window is essential for what I was doing.
Asking the model to print out the entire HTML and CSS after each change takes longer for the model but saved me having to think and savor the wine.
Iteration was pretty easy, however validation that changes didn’t break other pages was mildly annoying.
This technology is an easy way to plug any holes in your technology skill set.
Within 3 hours I had not only every page redesigned, (Home, Results, Code, About, API, and a few secret pages) it was responsive, supported dark mode, got near perfect lighthouse scores, reusable, and looking good enough that I did not hate it.
I estimate for me to have done something similar by myself would have taken a week, or about 40 hours of effort.
Honestly I was pretty shocked. So much so I wrote this comment on
Hacker News
while doing it
I detest writing CSS and HTML. I just find it boring fiddly and annoying. I have started doing “vibe” coding with LLM’s. Giving a decent prompt produces results that are… pretty good.
Almost 100% in lighthouse for both mobile and desktop, responsive, reusable components, dark/light mode and a design that was better than I could do in the 2-3 hours I spent doing it (while sipping wine).
I know its not a solution for everyone, and probably won’t work for the prettier designs out there, but you can go a long way with these tools this day.
I know there is a reluctance to not use LLM’s for code tasks, and I am one of the largest critics, but for me this solves a real pain point. I don’t want to write CSS/HTML anymore and these tools do a good enough job of it that I don’t have to.
The result has now been deployed to
https://searchcode.com/
and a screenshot below for those disinclined to click the link.
In addition to the new look searchcode has some new tricks such as the ability to do some
SAST scanning
which is partly there to help with the secret project work.
You can view a live example of it here
https://searchcode.com/file/51394/trunk_go/nonce/nonce.go/
where in addition to pointing out flaws that it is able to identify it can also point out code hot-spots of complexity, which is done through the integration of the code counter
scc
.
I digress. Back to vibe coding, which was the main point of this post. My take away is this,
For getting to market, this is a game changer. If you take a back seat and just work as a PM telling the tools what you want you will be able to work faster than anyone, no matter HOW good they are on the tools.
Knowing how the tech works only accelerates this as you know exactly what prompts to use, however this edge will probably be removed in time.
However what you produce will probably not scale, and is likely to have a lot of edge case bugs. This is where experience is going to be more valuable.
How long the latter will remain is up for debate. We have been told for the last few years that coding as a skill is going away, and that in time 90% of code will be written by AI
https://x.com/slow_developer/status/1899430284350616025
Thinking on that… it probably will turn out to be true.
But nobody has mentioned if it will be good or more importantly
useful code
.
