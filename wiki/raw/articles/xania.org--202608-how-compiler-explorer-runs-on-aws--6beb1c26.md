---
title: "How Compiler Explorer Runs on AWS in 2026"
url: "http://xania.org/202608/how-compiler-explorer-runs-on-aws?utm_source=feed&utm_medium=rss"
fetched_at: 2026-08-06T10:18:24.304133+00:00
source: "xania.org"
tags: [blog, raw]
---

# How Compiler Explorer Runs on AWS in 2026

Source: http://xania.org/202608/how-compiler-explorer-runs-on-aws?utm_source=feed&utm_medium=rss

How Compiler Explorer Runs on AWS in 2026
Written with LLM assistance.
Details at end.
I’ve been meaning to write an update on how
Compiler Explorer
actually runs on Amazon’s cloud, and it’s been sat on my list for a good while now, somewhere behind the other random things that take up what laughably I refer to as my spare time
.
The last time I wrote about this was
2016
, when the whole site was a load balancer, a couple of instances and some Docker containers I built on my laptop. I wrote a much longer
how it works
last summer, but that one is mostly about Compiler Explorer and only incidentally about the cloud it sits on.
It’s no secret that we run on AWS, and none of it is hidden: the
infra repository
has all the terraform, the install scripts and the
ce
command line tool we drive the whole thing with, so if you’d rather read the real thing than my description of it, help yourself. So this one goes the other way round, through the Amazon services we lean on, roughly in the order your compile request runs into them.
Getting your code as far as our servers
Your browser talks to
CloudFront
, Amazon’s CDN. We run two separate CloudFront distributions. The one in front of
godbolt.org
mostly just hands requests on to our load balancer, caching what it sensibly can and compressing things on the way back out
. The bulky static stuff lives in an S3 bucket behind a second distribution at
static.ce-cdn.net
: the compiled JavaScript, the images, the web fonts. Much the largest part of that is
Monaco
, the editor component out of Visual Studio Code, which is what gives you the syntax highlighting and the squiggly underlines and the rest of it. It’s a lot of JavaScript to send someone who only wants to look at some assembly, so it’s worth having it cached near them.
Sitting in front of that is
WAF
, doing our rate limiting. Our limits are
very
simple and
very
high, mostly because we used to be stricter and it kept catching C++ trainers: a whole classroom behind a conference’s NAT looks like a single very keen IP address. We could probably do something cleverer with fingerprinting, but raising the limit was easier and it hasn’t been a problem since.
Rather a lot of fleets behind one load balancer
Behind CloudFront is a single
Application Load Balancer
. It works out from the path which cluster a request is for, and then picks a healthy instance in that cluster to send it to. Almost everything has no special prefix at all and goes to the production fleet, which is where the overwhelming bulk of the traffic ends up.
/beta*
and
/staging*
go to the beta and staging fleets
.
/winprod*
goes to a fleet of Windows instances running
MSVC
,
/aarch64prod*
to
Graviton
machines that run ARM code natively rather than under emulation, and
/gpu*
to machines with real NVIDIA cards in them
.
Each of those is an
Auto Scaling Group
, and these days each one is doubled up: a blue and a green. To deploy, we bring up the other colour, wait for it to go healthy, point the load balancer’s target group at it and drain the old one. If it’s wrong, we point it back. Before that, deploying meant a rolling restart of the fleet with our
ce
command line tool, one instance at a time. That worked well enough, but backing out a bad release meant rolling the whole fleet forward again onto the previous version, which is a bit slow when you’ve just broken the site.
The scaling itself is simple: we just try and keep the average CPU load below a threshold. We’ve kicked around more sophisticated ideas but this one is supported out of the box
.
Renting the bits nobody else wants
The production fleet is almost entirely
spot instances
– unused EC2 capacity, sold off cheap, on the understanding that you can be evicted at two minutes’ notice. It’s a 60-90% saving over on-demand – quite a lot of money, for us.
We can get away with that because our instances don’t really matter. Everything that needs to survive lives on the shared filesystem, in S3 or in DynamoDB, so an instance that vanishes is just an instance that gets replaced. We ask for sixteen different instance types across the
m5
,
m6
,
m7
,
r6
and
i3
/
i4i
families. The allocation strategy is
price-capacity-optimized
– Amazon’s way of saying “pick whichever of these is cheapest and least likely to get yanked”. In practice we get evicted, the scaling group notices, and a new one turns up.
Why the compilers are the hard part
We have around 6,000 compiler entries
across 93 languages, and we never delete any of them
. Once a compiler version goes up it stays up, so that Stack Overflow answer showing a GCC 4.8 codegen quirk still compiles today. It’s our bit against link rot, and it does mean we hoard an awful lot of binaries.
All of that lives on
EFS
, Amazon’s elastic NFS, and NFS has latency. C-like languages pull in an enormous number of very small header files, so the naive version of this is unusably slow. Our fix, which sounds daft, is to build a
SquashFS
image per compiler, store the image
also
on EFS, and mount it through a loopback device. The kernel then thinks it’s talking to a local block device and caches blocks properly instead of checking with a server in another building every time
.
That worked, but it meant mounting a couple of thousand images at every boot, which took the best part of a minute and kept the metadata for thousands of filesystems resident in kernel memory. That cached metadata is a good chunk of why squashfs beats NFS in the first place, so it’s not wasted as such; it’s just that any one instance is only ever going to touch a handful of those compilers, so we were paying for all of it to use a fraction of it. It took me three years and several abandoned attempts to fix that, and the answer was
CEFS
: content-addressed images, packed into bundles of around 20GB, mounted on demand by
autofs
the first time something touches the path. The migration took us from 2,182 images down to 121, and OS startup from 50 seconds to 20! It’s crept back up to around 883 since, because the nightly builds keep making new images and consolidation only packs down whatever is already there. A garbage collection while I was writing this turned up 111 images that nothing references any more, about 63GiB’s worth
.
Our storage has come down a lot over the year too, though I’m honestly not sure how much of that is CEFS and how much is me finally deleting the old squash images:
Aug/04
01
:55
admin-node~
$
df
-h
Filesystem
Size
Used
Avail
Use%
Mounted
on
/dev/nvme0n1p1
97G
20G
77G
21
%
/
fs-db4c8192.efs.us-east-1.amazonaws.com:/
8
.0E
2
.2T
8
.0E
1
%
/opt
2.2T, where a year ago it was 3.9T. Still nowhere near 8 exabytes, mind.
Building compilers all night, every night
We build a pile of compilers from scratch every night: GCC trunk, Clang trunk, and a long tail of experimental branches for reflection, contracts, coroutines and all the other fun stuff. That’s 94 nightly build jobs at the moment
, up from 73 a year ago and 33 in 2022.
Those run on our own
GitHub Actions
runners on
EC2
, spun up on demand with the excellent
terraform-aws-github-runner
, with all the compiler orchestration on top being ours. Building trunk LLVM wants a big machine and a decent chunk of time, and GitHub’s hosted runners weren’t up to it when we set this up.
This is the part of the bill that goes up every time somebody asks us for another compiler and we say yes
.
The bits that are half-finished
One thing we’ve built but not finished rolling out is what we call the CE Router: a small fleet whose job is to decide
where
a compilation should happen, look the answer up in
DynamoDB
and drop the request on an
SQS
queue, with the result coming back to your browser over an
API Gateway
WebSocket. The point is to stop the machine that answers the HTTP request having to be the machine that owns the compiler.
It works, but it isn’t carrying production traffic yet: the load balancer rules that would send compilations through it are still commented out, and we’re migrating gradually. Your compile today still goes straight to a machine in the prod fleet, the way it always has.
Building it did turn up a good AWS gotcha, though. API Gateway WebSocket frames top out at 32KiB, and the assembly for almost any non-trivial program is bigger than that; in the other direction SQS messages cap out at 256KB, which a decent-sized multi-file project will go past. So in both directions, if the thing is too big we shove it in S3 and send a key instead.
Everything else
A scattering of other services doing one job each:
DynamoDB
holds the short links. Every
godbolt.org/z/...
you’ve put in a slide deck is a row in a table, and there are a couple of million of them.
S3
holds the compilers we build, the static assets, the logs, and a daily-expiring content-addressable compilation cache, so the second person to compile the same thing gets it for free.
Lambda
does the odd jobs: the
Claude Explain
backend, the nightly version tracking, and the one that pushes CloudWatch alarms into our Discord so it’s not just my phone buzzing at 3am.
Route 53
,
ACM
,
CloudTrail
,
Backup
and
SES
are the plumbing. I don’t think about them much.
CloudWatch
drives the auto-scaling triggers, though for actually looking at things we run
Grafana
,
Prometheus
and
Loki
. Those
dashboards are public
.
Everything is in
us-east-1
. If you’re compiling from Sydney your code goes a long way round, and I’m afraid it’s going to keep doing that: keeping a couple of terabytes of compilers in sync across regions would be an absolute nightmare.
Some numbers
We log a heavily anonymised JSON record to S3 for every compilation, with a
Glue
table over the top, so while writing this I went and counted them properly:
5,238,210
compilations in July, and
78.7 million
over the last twelve months. It’s been sliding gently all year, down about a third from last autumn’s peak.
Compilations per month over the last year. Generated from
this script
.
The big drop before that, from 2024’s 14 million a month, I can at least half explain: in mid-2024 we doubled the default delay before we auto-recompile as you type, from 750ms to 1500ms, and then to 2 seconds
. If you type continuously, doubling that delay roughly halves the number of compilations you generate, without anybody noticing anything much. This latest slide isn’t that, though: it started well over a year later.
So I don’t really have a good explanation, and I can’t easily go and find one, because we deliberately
don’t track who you are
: no cookies, nothing that would let me tell you how many people used the site yesterday. I’d make that trade again every time, but it does leave me squinting at graphs occasionally.
Since I had the query open, here’s what folks actually compiled in July:
id                      compiles   compiler
g161                   1,386,532   GCC 16.1 (C++)
cg161                    403,659   GCC 16.1 (C)
gsnapshot                298,256   GCC trunk
clang_trunk              287,885   Clang trunk
g152                     239,331   GCC 15.2
clang2210                177,958   Clang 22.1
vcpp_v19_latest_x64      132,186   MSVC
r1970                     65,380   Rust 1.97
python314                 51,104   Python 3.14
That top entry is
26%
of everything – roughly what you’d expect when you’re the default
. The load balancer sees around 14 million requests a month; our busiest day this year was the 21st of April at 1.44 million. The auto-scaling dealt with that one by itself; I only found out about it while writing this.
All of that costs us somewhere around $3,600 a month on AWS at the moment, which works out at about $0.0007 per compilation
. For the best part of a year we barely paid any of that: AWS’s
open source credits
covered almost all of it. Those ran out in the spring, we paid our own way for a few months, and AWS have just renewed them for another year, which is a huge help. Either way we’re fine for money, thanks to our
Patreon
supporters, our
GitHub sponsors
and our
commercial sponsors
. I did a
full breakdown of the costs
last year and it’s still roughly the right shape.
The wall of compilers, a year on: 6,157 entries across 93 languages.
Regenerated from
the same script
as last year's.
Things I’d still like to fix
Deployment is better than it was but there’s still more hand-holding in it than I’d like
. The CE Router migration has been “nearly done” for a while now… I still wish I’d laid out the NFS directory structure properly at the start instead of growing it one compiler at a time for a decade. And we moved everything to
Ubuntu 24.04
this year, which was not the tidy little upgrade it sounds like
.
None of this is especially clever: it’s a load balancer, some scaling groups full of cheap spot instances, a network filesystem and a decade of accumulated hacks. It does keep working, though, and these days it mostly keeps working without anyone having to go and poke it. I’m pretty happy with that.
Thanks
As ever, the people who keep this running are the contributors.
Partouf
(Patrick Quist) above all – I really don’t know what CE would do without them – along with the core team and the many, many people who send PRs and file issues. Thank you all. Thanks too to AWS, whose
open source credits programme
paid for the best part of a year of everything described above, and who have just renewed for another year – which is not a small thing for a project our size, and it lets us get on with the interesting problems instead of watching the bill. Thank you AWS! And thanks, as always, to our
Patreon
and
GitHub Sponsors
supporters and our
commercial sponsors
, who cover the rest.
Questions? Complaints? Compilers we’re missing? Drop by our
Discord
, or find me on
Bluesky
or
Mastodon
.
Disclaimer
This article was a collaboration between a human and an
LLM
. I set it off to dig through our infrastructure repositories and our AWS account for the current numbers, which turned up several things I had wrong, and worked from that. It also ran the Athena queries and regenerated the graphs. The opinions, em- and en-dashes, and mistakes are all mine.
