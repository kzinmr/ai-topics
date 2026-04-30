---
title: "Everyone knows your location, Part 2: try it yourself and share the results"
url: "https://timsh.org/everyone-knows-your-location-part-2-try-it-yourself/"
fetched_at: 2026-04-30T07:00:51.582353+00:00
source: "timsh.org"
tags: [blog, raw]
---

# Everyone knows your location, Part 2: try it yourself and share the results

Source: https://timsh.org/everyone-knows-your-location-part-2-try-it-yourself/

It's been more than 2 months now since my first post on the topic of location data sharing between various 3rd parties came out – in case you haven't seen it, you should definitely start from there:
Everyone knows your location
How I tracked myself down using leaked location data in the in-app ads, and what I found along the way.
Since then I had a chat with a lot of people working in this field – both members of non-profit organisations, fighting for data privacy rights in various countries, and employees of adtech companies, proving my words right or wrong (but mostly right). I was even invited to "
Lock and Code
" podcast to talk about geolocation data and privacy. Ok, enough with the bragging.
I went through the process described in my initial post and decided to make it faster and more scalable: manually going through hundreds of requests in Charles was very cool for research and educational purposes, but it also took me a lot of time to find "interesting" requests coming from a single app.
I've significantly upgraded my approach (though it could definitely be more efficient), and in this post I wanted to share it with you.
TL;DR
I have created a small guide and a Python notebook that allow anyone to record mobile app traffic and find surprising things in it.
Here's
the link to a GitHub repo
with it.
The initial setup takes 10-30 minutes.
Analysis using this algorithm took me about 10 minutes per app - you can definitely dig deeper and get lost for hours if you find something interesting in there..
Follow the
readme
or the guide below if you'd like to try!
I came up with an idea
: it would take me hundreds of hours to go through each app and record the traffic, though I would love to do that – let's not blindly trust some table from the internet, but find out for ourselves.
I copied the Gravy Analytics Google Sheet and created a simple form that you can fill in (no personal info is collected) that writes to that Google Sheet
Link to the table
Look up any app you already have on your phone or just a random one in the table, check if others have commented on it already and record the traffic.
Finally, if you want to help crowdsource the information on the kinds of data the apps from the list collect and share –
fill in the form
:
I found something interesting in the app traffic
Hey! I don’t know how much people will go through with all the instructions and analysis, but since you’re here, you probably already did it and found something. Thanks for being here and doing this. Fill in the form below and your response will be recorded to a shared spreadsheet. PLEASE CHECK ALL OF YOUR INPUTS FOR YOUR PERSONAL INFORMATION. This form is set in a way that I collect nothing personal from you (like email or Google account or whatever), but your response will be viewable by virtually anyone - so be aware!
Please edit all the private information in your submission (in case it's there).
Visualising "domain power"
Before jumping into the guide, I wanted to share a few cool-looking visualisations with you.
Long story short: lately I've been obsessed with graph visualisations of things, especially branchy-embedded ones.
While analysing the traffic I found myself curious: how are the adtech companies domains distributed across all of the requests?
So I joined these two together and created a visualisation using
PyVis
that would answer that question:
Here's some context:
Every circle is a domain or a subdomain.
The hierarchy is represented by the inclusion of circles into others.
Example:
o-sdk.ads.unity3d.com
is represented by 3 circles:
o-sdk
inside of
ads
inside of
unity3d
.
Colors represent the app (I analysed 5) that the request corresponds to.
I used low opacities for better visibility, and it turns out that in my mix of colors and their opacities purple is the combination of all of them.
Circle sizes, or masses, represent the frequency: how often did this or that domain appear in the requests data.
See any insights?
Unity
rules the mobile game app traffic scene.
For comparison, the
g / doubleclick
thing is Google Ad Network.
Take a look at it in motion:
I included the code for it –
visualise_domains.ipynb
in the same repo so that you could create the same visualisation out of the data you record.
I also included the
ad_domains.html
file with this sample (mine) graph – simply open it in your browser if you want to play around with it.
I also was curious of the density of the requests – in my last post, I mentioned that hundreds of requests happen in just a few seconds, and now I could finally take a look at them:
Filenames in the legend are flows collected from 5 different games.
I cut it at 60s for better visibility, but obviously there were requests after that as well.
This one is again a different view of the domain power – look at the list on the right.
It should be obvious by now that Unity is the leader in this strange contest – it has the most subdomains called and the most requests made to.
Applovin is a Palo Alto-based company that acquired above mentioned Adjust in 2021, has shown
$1.58 bln net income in 2024
, and decided to get rid of it's mobile games development products and focus on its advertising business just a few months ago.
Doubleclick.net is Google Ads
And surprisingly, Facebook, that I've seen in the requests from every single game, is in the last place among these. Well, at least based on this strange metric observed on 5 examples
Now that you've seen these obscure but good-looking graphs - let's move on to the actual guide that you could follow to analyse any app traffic.
Getting started
Step 1: Install mitmproxy on your PC
mitmproxy
is an open-source tool for intercepting traffic with wide capabilities and a surprisingly nice web version called
mitmweb
.
Be aware that
mitmproxy
is recognised as malware by some anti-virus apps - looks scary, but it's not.
Go to their
official downloads page
and choose whatever installation way you like more.
On Mac, for example, you can simply run
brew install mitmproxy
.
After installation run this command to start
mitmweb
(mitmproxy + web interface):
mitmweb --listen-host 0.0.0.0 --listen-port 8080
You can also use
mitmproxy
CLI, but I prefer mitmweb because it is actually very helpful for initial discovery (and understanding the scale of the RTB requests).
We use
--listen-host 0.0.0.0
to avoid
mitmproxy
starting in the default location, which is localhost
128.0.0.1
– this way, you don't record your PC traffic and will see 0 requests until you complete the next step.
Step 2: prepare your mobile device
What you'll need to do is to then setup proxy on your iPhone / Android device and install + trust a certificate.
I focused on iOS in my instruction, but setting up an Android phone for the same experiment is even easier and is well-documented - for example,
here
.
I believe you might need to turn on the developer mode, otherwise you won't have Certificate Trust in your settings. Or maybe not.
Anyway, if it's missing from your settings -
here's a guide
on how to do it.
By the way, your iPhone and computer must be in the same wifi network for all of this to work.
Step 3: start collecting requests!
Run
ipconfig getifaddr en0
to find your PC local IP address.
Next, open the wifi network settings on iPhone, scroll down and setup manual proxy with:
server
= the ip address you just found
port
= 8080
On iPhone, open browser and go to
mitm.it
further instructions are described here:
https://jasdev.me/intercepting-ios-traffic
or here:
https://support.apple.com/en-us/102390
What is this for?
You need to install the certificate and enable full trust to be able to decrypt TLS-encrypted traffic.
Otherwise you'll just see a bunch of encrypted packets flowing in and out.
Congrats! If you completed all the steps correctly, you should now see requests in the
mitmweb
interface.
If you only want to record traffic coming from a specific app, close all apps, "Clear flows" and then open the desired app.
If you don't have an app installed yet, you might have to turn off proxy on iPhone, download the app and then turn it on again and clear the flows - AppStore refused to work with proxy on for me.
If you don't have anything specific on your mind – pick any app with "Checked = False" in the "original list" sheet.
https://docs.google.com/spreadsheets/d/1fJbNT-kmfuWUlIpYr9sduvjZS1ggrmhydCzoDlqaMaA/
Let's find something interesting
All right, now we can record the data!
You can already find interesting requests manually - for example, I'm pretty sure you'll see this Facebook request no matter what app you analyse:
But looking through the requests in
mitmweb
, even with ok (not advanced) filtering is a very slow process. And you'll see – there will be hundreds (if not thousands) of requests in just a few minutes.
When you feel like there's enough (you could even leave it open or play for an hour or so to collect more data), close the app and switch off the phone, then in
mitmweb
press File → Save.
This will give you a
flows
file - rename it as
appname.flow
.
Filtering & analysing the data
Open the
mitm_test.ipynb
- either in a local Jupyter Notebook or in Google Colab (or wherever you work with
.ipynb
s).
Personally, I feel much more comfortable working with this kind of data in the local environment.
However, if you don't code at all / don't use python, e.t.c. – believe me, there's nothing faster and easier than opening up
Colab
and importing the file.
There are quite clear and broad instructions in the file, so I won't repeat the full process, but just highlight a few things:
A very important step - fill in as many keywords as you have on your mind.
I was strictly focused on IP and geo data, but you might want to look for other things, like "screen_brightness", "IDFA" or whatever.
Please note that these will only return the exact matches (imagine an amount of words / strings where "lat" or "lon" would be substrings).
Now that you've put all the keywords in the list, run the cells below and it will create a
df_filtered
table with the requests (or responses) that match the keywords.
Here you'll see a snippet of the match (
matched_in_request
and
matched_in_response
), as well as the "reason" for both cases - the keyword(s) that are in the match.
Below is a simple
.loc
where you can input the index of the row (the first column on the left) and see the full value of a given column – in the example below,
"full_reponse"
.
If the string was too long, I just copied it to Sublime Text and use their built-in search to find more context or other surprising data points in the request or response text.
And that's it!
Finally, if you want to help crowdsource the information on the kinds of data the apps from the list collect and share –
fill in the form
:
I found something interesting in the app traffic
Hey! I don’t know how much people will go through with all the instructions and analysis, but since you’re here, you probably already did it and found something. Thanks for being here and doing this. Fill in the form below and your response will be recorded to a shared spreadsheet. PLEASE CHECK ALL OF YOUR INPUTS FOR YOUR PERSONAL INFORMATION. This form is set in a way that I collect nothing personal from you (like email or Google account or whatever), but your response will be viewable by virtually anyone - so be aware!
Please edit all the private information in your submission (in case it's there).
Room for improvement?
I know this is a very primitive way of doing things – I could've done this all with
mitmdump
and automated saving / filtering straight to .csv, but I deliberately kept it semi-manual.
The format and structure of all these requests and responses is very diverse and the further you go from looking at them manually, the higher chance you'd miss something.
At first I tried filtering out by content type and encoding, but I've noticed that some of the matching requests are missing from the list.
So I turned off the filters... and found this:
gs-loc.apple.com
is an endpoint used by Apple to request user's location information.
It was called during a 3-minute recording of the traffic from a single opened app - Make More game. It didn't turn up ever before [when I was analysing other apps] + this game is on the Gravy list.
However, I don't want to make false claims saying that this app was responsible for Apple's request – that endpoint is not accessible directly for any app except for iOS itself, so in order to get the information from it an app needs to call a dedicated Apple API method and have corresponding permissions. Or maybe not?
Anyway, the response to this request was encoded in protobuf format, so I had to find a way to decode it, obviously. And I found it.
But that's a topic for another post – stay tuned!
Sign up for tim.sh
Thoughts, stories and ideas.
No spam. Unsubscribe anytime.
I really hope some people find this interesting enough to check at least 1 app and contribute to this process, or just to experiment and have fun.
If you have any comments, ideas or just want to chat about it – hit me up at
[email protected]
.
