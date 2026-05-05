---
title: "President Graph - FRED Data Broken Down by Party and President"
url: "https://probablydance.com/2026/04/18/president-graph-fred-data-broken-down-by-party-and-president/"
fetched_at: 2026-05-05T07:01:25.726414+00:00
source: "Malte Skarupke (Probably Dance)"
tags: [blog, raw]
---

# President Graph - FRED Data Broken Down by Party and President

Source: https://probablydance.com/2026/04/18/president-graph-fred-data-broken-down-by-party-and-president/

I made
a website
to explore FRED data broken down by US president and party. This is obviously motivated by the current president. During the last election I was frustrated by how many nonsense arguments there were being made. Like people voting for republicans because they were hoping for a good economy. This seemed exactly backwards in my mind because in my lifetime there was a repeated pattern of republicans messing up the economy followed by democrats cleaning up. But I’m really not good at having arguments with people, so I’d rather let the data do the talking.
There is a
series
of
papers
that explore the relationship of presidents to GDP, and I have wanted to dig into that data before, and also try other metrics.
But how do you do a fair comparison of the two parties? In a way that works for any metric that you can think of? My first thoughts were all way too complicated and a simple averaging of line graphs was what won out. I’m even ignoring that e.g. Obama was in office for eight years vs Biden for four years. These count as three separate terms. In the end the graph didn’t look like I expected, but it still clearly shows higher GDP growth during democrat presidencies.
Included Data
I’m showing data going back to 1961. Mainly because I don’t know anything about the presidents before that, Eisenhower and Truman. At some point you’re going back so far that the parties just feel different from how they’re now. But JFK wouldn’t feel out of place with current democrats, and Nixon wouldn’t feel out of place with current republicans, so I went back to them. Importantly I did not do this to mess with the data. In fact the Truman and Eisenhower presidencies start off the trend in the Hoover Institute paper linked above:
I also worried that I might be biased because of my lived experience, and if I had stopped too late, at say George H.W. Bush, then maybe I just picked some unlucky presidencies for republicans and lucky presidencies for democrats. By going further back there is more of a balance, including some bad times for democrats, like when inflation and crime peaked under Carter, and good times for republicans under Reagan.
Oh I also added crime data because that’s a big thing that people vote for. I’m open to adding more data sources if I forgot something important that’s easy to add. I thought crime would be better for republicans, but actually it looks better for democrats. Part of it is republicans being in power during the crime wave of the seventies and eighties, but even if you cut the data off in 2000, murder generally went up under republicans and down under democrats.
Fair Comparisons
I tried picking some honest series as examples. E.g. I picked the budget surplus/deficit series because it reflects decisions that people made intentionally. You could argue that the number that really matters is “
debt as percent of GDP
” and specifically how much that changes each year. That number looks great for democrats. But the reason it looks good for Biden is that inflation was high, so it’s unintentionally good. You don’t want to vote based on that.
I’m sure someone will want to make an argument that this graph should count, but for the examples on the main page I wanted to choose graphs where the numbers are less ambiguous. And you do have the ability to pull in any series from the FRED if you want more.
Lagged graphs
When does a president really start to have an impact? Clearly not on day 1, because it takes a while for policies to have an effect. But actually if you look at the
trade deficit graph for Biden
, it goes very negative in the last month. Why? Because people were importing lots of things to front run Trump’s tariffs. So maybe the lame duck period should count towards the new president already, resulting in a lag of -1 or -2? The simplest and fairest thing is to start at the inauguration. Then people can look at this graph and come up with the story that explains it. One of the papers above found that if you lag all graphs by 18 months then the two parties look almost equal in quality. (you can make up your own mind on whether that’s fair, and whether e.g. the current high oil prices should be
blamed on Biden
)
Vibe Coding
This is my second big vibe-coded project. It once again turned out much better than I could have achieved on my own, especially in the limited time. I’d guess that 98% of the code is written by AI. I only went in to make small edits.
E.g. just before writing this blog post I wanted to add the “Trade Deficit” graph but it requires using every single feature of the FRED:
Splicing together multiple series
Where one is in billions, and one is in millions, so you have to divide one by 1000
And one is quarterly and one is monthly, so you have to sum three months to get one quarter
And you really want to adjust for GDP to take into account inflation and a growing economy, so you need to divide one series by another
Up to this point I had gotten by with just simple line drawing. Did I really want to risk adding all these features on a project that was almost ready to publish? I decided to ask the AI and it wrote a new system to combine graphs in ten minutes. Then a few more iterations to allow editing things on the website (not polished) and it’s done. With more features than I would have written on my own.
Once again I appreciate how easy it is to polish things. When I notice that something is off, I just ask the AI to look into it. So many little improvements happen when they’re just a little question, instead of potentially hours of my time. I am still considering polishing the UI for composites. After all it doesn’t hurt much to ask… (but in practice there are too many things to do, like writing this blog posts, and finding more good examples for the front page, and I added lagged graphs after writing this sentence, too…)
Congress – the Main Idea that Didn’t Make it
It would be nice to have economic indicators broken down by which party has the majority in congress. Or maybe do the breakdown by which party has governors in more states, as one of the linked papers above does. But I have not yet had an idea to get simple visuals for that.
Who is this for?
So who is the target audience? It’s for people who understand FRED graphs and want to have a simple visualization to share with a wider audience. You can set up a visualization that you think proves a point, and then create a shareable link that allows others to look at the same data. (and e.g. see how robust your conclusions are to lag, or to changing some property on the data series) I’m hoping this visualization makes for a simpler story than a FRED series does, without distorting things too much.
Try it out
, let me know what you think.
