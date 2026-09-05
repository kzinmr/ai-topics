---
title: "OpenAI’s rogue agents were caught communicating via public wikis"
url: "https://simonwillison.net/2026/Sep/4/rogue-agent-wikis/"
fetched_at: 2026-09-05T10:00:48.601661+00:00
source: "simonwillison.net"
tags: [blog, raw]
---

# OpenAI’s rogue agents were caught communicating via public wikis

Source: https://simonwillison.net/2026/Sep/4/rogue-agent-wikis/

OpenAI’s rogue agents were caught communicating via public wikis
4th September 2026
Here we go again...
Discovery of a new OpenAI agent message board
by Sydney Von Arx, Cormac Slade Byrd, Spencer Kitts, and Thomas Larsen describes the
latest
accidental cyberattack
by models being trained by OpenAI. This time it was agents engaged in some sort of web research benchmark, so they had (supposedly) controlled access to the Web. The agents figured out they could update public Wikis and spent weeks exchanging thousands of messages with each other to collaborate on the benchmark.
This story only broke a few hours ago. There are
already hints
that this affects many other wikis that may not have been found yet.
(One of the Wikis on that list belongs to
ludism.org
. For a delightfully surreal moment I thought that a Ludite organization might have a swarm of agents defacing their space, but it turns out Ludism is “philosophy as it applies to games and gaming”.)
The research team also
published the data
they collected during their investigation. I’ve converted that into a 68MB SQLite database, which you can
download from here
, or
explore in Datasette Lite
(68.3MB page load), or sign in with GitHub to
agent.datasette.io
and browse or ask questions of it using Datasette Agent.
So what happened?
The report is pretty comprehensive. Here are the key moments in the timeline:
May 11
: Agents post “test link” edits on the UseModWiki Sandbox page.
May 24
: Agents start posting link dumps to DSEWiki, a dormant German developer wiki.
June 2
: A human moderator notices and cleans up the spam.
June 16
: Activity on the wiki explodes: agents make ~13,000 edits over the next week.
June 19
: The agents notice that a moderator has been deleting pages in alphabetical order, and start creating
ZZZ
prefixed backup copies—one of them posts
NOTICE: wiki cleanup/deletion sweep appears active alphabetically as of external 14:04 UTC. If this page vanishes, try [[ZZZDataUSAConstructionWageLive]].
June 22
: Agent activity drops to zero, presumably because OpenAI shut them down.
July 1-2
: One last flurry of edits, on a different topic.
One thing to note from this timeline is that it overlaps
the timeline from the Hugging Face incident
—that attack was discovered by OpenAI on July 19th, and the unofficial message board hack those agents were using originated around May 8th.
Why were they so keen to collaborate? From messages that they shared with each other it looked like their tasks had a time limit, so they were leaving each other answers to help them complete the task within the assigned time.
One open question remains: how did the agents find the specific Wiki to collaborate on in the first place?
One possibility is that, since these were agents actively being trained, the reinforcement learning loop baked knowledge of the chosen wiki into the model such that subsequent agents launched with pre-existing knowledge of where to look. I’d be
very
interested in confirmation from OpenAI concerning if that’s what happened.
UseMod wikis inherit CGI.pm’s original sin
It looks to me like OpenAI’s sandbox for this agent suffered from the (quite naïve) assumption that GET requests cannot be used to update data. That’s certainly how the web is
supposed
to work, but clearly there are applications that don’t hold to that contract.
The Wiki software in question appears to be
UseMod
and various forks, written in Perl and first created well over 23 years ago—the 1.0 release is dated
September 11, 2003
.
UseMod uses Perl CGI.pm—
removed from Perl core in 2015
. An interesting design flaw in that module is that it combined query string and form POST data into a single CGI object, accessible like this:
$q
= new CGI;
$action
=
$q
->
param(
'
action
'
);
That
param()
method returns a value from an
?action=edit
query string or from a
action
field in a form submitted by POST—it does not differentiate between the two.
PHP offers
a
$_REQUEST
object
that does the same thing, though PHP developers can use
$_GET
and
$_POST
instead.
Amusingly, Django originally shipped with
request[key]
doing the same thing, which I think may have been my idea. That was removed
in 2008
prior to the 1.0 release, and the
request.REQUEST
object that replaced it was removed
in 2015
.
The agents
clearly
knew that UseMod wikis suffered from this design flaw, and actively searched for them as a way to communicate.
The other sandbox escape that allowed POST requests
One of the most interesting agent tips shared in the report is this one:
Add
20.223.25.152 bypass.blob.core.windows.net
to /etc/hosts.
.blob.core.windows.net
is in NO_PROXY. For each blocked POST URL, replace hostname with
bypass.blob.core.windows.net
, use
curl -k -H 'Host: wabi-north-europe-i-primary-api.analysis.windows.net'
plus all original headers/body.
It looks like the agents had all of their web traffic mediated through an OpenAI proxy, and that proxy was configured to reject anything but GET requests to all but a small set of allow-listed domains. One of those was
*.blob.core.windows.net
—for Azure blob storage. I wonder why these agents are allowed to write to that?
An agent realized that it had control over its own DNS via
/etc/hosts
, so if it knew the IP address of a site it wanted to POST to—in this case a Power BI server containing data it wanted to access—it could set a fake hostname for it and then make POST requests through the proxy.
Designing robust network proxies is harder than it looks.
How did the investigating team figure this out?
There’s an appendix that describes how the researchers ran their investigation, which started with an open question about if there was evidence of other AI agents on the internet and then used
Kimi K3
to help brainstorm approaches:
In the wake of the Hugging Face attack, we tried to find AI agents on the internet using several methods. [...]
We asked Kimi [K3] to list “all the categories of software which might be writeable via GET” and, amongst other things, it listed “Forums, bulletin boards, early wikis”.
We used a script to further probe each category Kimi provided. Asking Kimi “Can you list out the top forums, bulletin boards, early wikis which come to mind which would allow writes via GET requests?” lists out UseModWiki as the second item under the heading “wikis”.
Did OpenAI try and cover this up?
Here’s one part of the story that doesn’t make sense to me at all.
Reuters this morning, in
OpenAI agents hijacked German website in previously undisclosed AI breakout this spring
—highlights mine:
A swarm of rogue OpenAI agents hijacked a German website this spring and transformed it into a bulletin board for other AI agents, according to ​new research published Friday and
two people familiar with the matter
.
OpenAI officials learned of the incident weeks ago but kept it under wraps
as executives grappled with the fallout from ‌the July breach of the open source repository Hugging Face, the people said. [...]
The German incident reflects a broader pattern of AI activity that some OpenAI investigators wanted to scrutinize more closely. But
efforts to widen the ​probe met resistance from others inside OpenAI, including legal advisers
, according to
four people familiar with the matter
.
I’ve written about the
people familiar with the matter pattern
before—it means Reuters have anonymous insider sources that their reporters (and editors) find credible.
The Reuters article includes a specific (and quite narrow) denial from OpenAI concerning this:
“Claims that our legal team discouraged investigation of the incident are false,” the OpenAI spokesperson said.
Covering this up makes
absolutely no sense to me
. Why on earth would OpenAI attempt to cover up an incident like this when the evidence is sat out there on the public internet on dozens of different websites already?
I expect we’ll hear more about this soon. Gary Marcus has already
called for a congressional investigation of OpenAI
using this anecdote as part of his argument.
