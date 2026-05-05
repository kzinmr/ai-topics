---
title: "Saving Resources for Humans in PHP"
url: "https://boyter.org/2013/08/saving-resources-humans-php/"
fetched_at: 2026-05-05T07:02:04.606409+00:00
source: "Ben Boyter"
tags: [blog, raw]
---

# Saving Resources for Humans in PHP

Source: https://boyter.org/2013/08/saving-resources-humans-php/

Saving Resources for Humans in PHP
2013/08/27
(306 words)
One of the issues I have run into running searchcode.com is that a huge amount of time spent serving pages is serving them to bots (about 900,000 hits a day are from bots). I have been watching the load averages and they can spike to over 30.00 occasionally which is pretty bad for a 4 core/ht system. I don’t have any problems with bot’s really other then the fact that I cannot really control them. Sure you can specify crawl delays but its of limited use if the bot chooses to ignore it.
Another solution is to slow them down. Of course you don’t want to go too crazy with this as I do want my site indexed but not at the expense of real users. Thankfully with PHP this can be accomplished using the sleep and usleep functions.
if(isHuman() == false) {
  usleep(500000); // 1,000,000 is 1 second
}```

The above is how you can implement a simple limiter to slow the bots down. Based on if the hit is human or not it will sleep for half a second. How you implement the isHuman method is up to you but a [quick search shows the most common way][1] is to check the user agent using $\_SERVER[&#8216;HTTP\_USER_AGENT'] and based on that work out if the user is a bot. Check your framework of choice as well as its a pretty common thing to want to do. Something else to consider is adding a much larger delay for bots that visit pages of your site you do not want them visiting. It should encourage them to crawl elsewhere.

The results? Well the average load for searchcode is below 2.10 most of the time which is a massive improvement. I have not seen it spike any more then 7.00 which is acceptable for spikie periods.

 [1]: http://searchcode.com/?q=function%20is_bot%20lang%3APHP
