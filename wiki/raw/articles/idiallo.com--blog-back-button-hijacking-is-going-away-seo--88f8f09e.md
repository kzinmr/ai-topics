---
title: "Back button hijacking is going away"
url: "https://idiallo.com/blog/back-button-hijacking-is-going-away-seo?src=feed"
fetched_at: 2026-04-29T07:02:14.733632+00:00
source: "idiallo.com"
tags: [blog, raw]
---

# Back button hijacking is going away

Source: https://idiallo.com/blog/back-button-hijacking-is-going-away-seo?src=feed

When websites are blatantly hostile, users close them to never come back. Have you ever downloaded an app, realized it was deceptive, and deleted it immediately? It's a common occurrence for me. But there is truly hostile software that we still end up using daily. We don't just delete those apps because the hostility is far more subtle. It's like the boiling frog, the heat turns up so slowly that the frog enjoys a nice warm bath before it's fully cooked.
With clever hostile software, they introduce one frustrating feature at a time. Every time I find myself on LinkedIn, it's not out of pleasure. Maybe it's an email about an enticing job. Maybe it's an article someone shared with me. Either way, before I click the link, I have no intention of scrolling through the feed. Yet I end up on it anyway, not because I want to, but because I've been tricked.
You see, LinkedIn employs a trick called back button hijacking. You click a LinkedIn URL that a friend shared, read the article, and when you're done, you click the back button expecting to return to whatever app you were on before. But instead of going back, you're still on LinkedIn. Except now, you are on the homepage, where your feed loads with enticing posts that lure you into scrolling.
How did that happen? How did you end up on the homepage when you only clicked on a single link? That's back button hijacking.
Here's how it works. When you click the original LinkedIn link, you land on a page and read the article. In the background, LinkedIn secretly gets to work. Using the
location.replace()
JavaScript method, it swaps the page's URL to the homepage. The
replace
method doesn't add an entry to the browser's history. Then LinkedIn manually pushes the original URL you landed on into the history stack. This all happens so fast that the user never notices any change in the URL or the page.
As far as the browser is concerned, you opened the LinkedIn homepage and then clicked on a post to read it. So when you click the back button, you're taken back to the homepage, the feed loads, and you're presented with
the most engaging post
to keep you on the platform.
If you spent a few minutes reading the article, you probably won't even remember how you got to the site. So when you click back and see the feed, you won't question it. You'll assume nothing deceptive happened.
While LinkedIn only pushes you one level down in the history state, more aggressive websites can break the back button entirely. They push a new history state every time you try to go back, effectively trapping you on their site. In those cases, your only option is to close the tab.
I've also seen developers unintentionally break the back button, often when implementing a search feature. On a search box where each keystroke returns a result, an inexperienced developer might push a new history state on every keystroke, intending to let users navigate back to previous search terms. Unfortunately, this creates an excessive number of history entries. If you typed a long search query, you'd have to click the back button for every character (including spaces) just to get back to the previous page. The correct approach is to only push the history state when the user submits or leaves the search box (
onblur
).
As of yesterday, Google announced
a new spam policy
to address this issue. Their reasoning:
People report feeling manipulated and eventually less willing to visit unfamiliar sites. As we've stated before, inserting deceptive or manipulative pages into a user's browser history has always been against our Google Search Essentials.
Any website using these tactics will be demoted in search results:
Pages that are engaging in back button hijacking may be subject to manual spam actions or automated demotions, which can impact the site's performance in Google Search results. To give site owners time to make any needed changes, we're publishing this policy two months in advance of enforcement on June 15, 2026.
I'm not sure how much search rankings affect LinkedIn specifically, but in the grand scheme of things, this is a welcome change. I hope this practice is abolished entirely.
