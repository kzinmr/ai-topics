---
title: "How to Delete All your Tweets"
url: "https://hugotunius.se/2021/04/05/how-to-delete-all-your-tweets.html"
fetched_at: 2026-04-29T07:02:13.451839+00:00
source: "hugotunius.se"
tags: [blog, raw]
---

# How to Delete All your Tweets

Source: https://hugotunius.se/2021/04/05/how-to-delete-all-your-tweets.html

A while back I had to re-activate my deactivated Facebook account to participate in a Messenger group chat. I wasn’t exactly happy about this, but being an absolutist about these things is not worthwhile either. After re-activating my account I decided it would make me slightly happier about the situation if I wiped all the content from my account. A digital detox if you will. Ever since then I’ve had a nagging feeling I should expand this idea to other platforms. This blog post is about how I deleted all my tweets on Twitter.
Thanks to the EU and the GDPR I can ask Twitter to delete all my data and they have to comply with my request. Unfortunately, my goal isn’t to delete my Twitter account, I just want to delete all my tweets. Twitter does have an API which should make it trivial to enumerate and delete all of my tweets. There are many scripts available online which do just this. Not to mention many websites that offer the same service, although I’d stay away from them.
I used
Chris Albon
’s
tweet_deleting_script.py
as the base of my implementation. Before running it I made a few tweaks, namely injecting the relevant secrets via the environment.
def
from_env
(
key
):
value
=
os
.
getenv
(
key
,
None
)
if
value
is
None
:
raise
ValueError
(
f"Env variable
{
key
}
must be provided"
)
return
value
Chris’s script fetches all tweets for the account in question using Twitter’s
timeline API endpoint
and then, unsurprisingly, deletes each of them in turn. Chris also added some filtering criteria to keep certain Tweets around, but since I was going nuclear I removed that code.
That’s that then? Run the script and wait? You’d be forgiven for thinking this was the end of this post and that it makes for a rather dull post. However, we live in the year 2021 of exciting web scale services and distributed systems and Twitter’s timeline API only returns the last 3200 tweets.
Twitter’s docs:
The user Tweet timeline endpoint is a REST endpoint that receives a single path parameter to indicate the desired user (by user ID). The endpoint can return the 3,200 most recent Tweets, Retweets, replies and Quote Tweets posted by the user.
If you spend your time on better things than tweeting and thus have fewer than 3200 tweets I applaud you. The script above is all you need, just run it an enjoy your digital detox. If you, like me, waste lots of time tweeting let me tell you about how to waste even more time deleting said tweets.
When I first read about the 3200 tweets limitation I assumed that after deleting the most recent 3200 tweets I could just run the script again, but no such luck. After deleting 3200 tweets the timeline endpoint returns nothing, regardless of the number of remaining undeleted tweets. In my case I had about 5000 tweets left after running Chris’s script.
The crux of the matter is that we need the tweets, well their ids anyway, in order to delete them, a bit of a catch 22. I dug through the Twitter API documentation and some discussion online but there doesn’t seem to exist a programmatic way to access all the tweets for a given account. One neat trick I found used browser automation to search for tweets from the given account day by day, but this would have required 3285(9 years) searches for my account.
I was about to give up, but then I realised that Twitter has to give me all the data they hold about me if I ask them(thank you EU!). I
asked Twitter for an archive of my data
and waited. It took a couple of days but eventually Twitter sent me a comprehensive archive of everything I had ever done on Twitter, including every tweet and their ids.
In the archive there’s a file called
data/tweets.js
which starts with the line:
window
.
YTD
.
tweet
.
part0
=
[
{
Then follows every tweet I have ever tweeted. Simply deleting the
window.YTD.tweet.part0 =
part of this line makes the file valid JSON. With some tweaks to Chris’s script I used this new source of tweets to delete every single one of my tweets. Ah bliss, digital detoxing feels good.
Twitter still thinks I have 25 tweets and I have been unable to locate these tweets. I suppose in the age of distributed systems 0 is just a mirage.
If you feel like doing a digital detox I’ve published the relevant technical details in the following
GitHub Gist
.
