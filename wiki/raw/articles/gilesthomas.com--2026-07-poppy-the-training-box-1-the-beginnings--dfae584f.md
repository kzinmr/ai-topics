---
title: "poppy the training box, part 1: the beginnings"
url: "https://www.gilesthomas.com/2026/07/poppy-the-training-box-1-the-beginnings"
fetched_at: 2026-07-09T07:01:31.325696+00:00
source: "gilesthomas.com"
tags: [blog, raw]
---

# poppy the training box, part 1: the beginnings

Source: https://www.gilesthomas.com/2026/07/poppy-the-training-box-1-the-beginnings

Writing the post that I wished I'd found when I started learning whatever it was...
Archives
Categories
Blogroll
For a while I've been planning to put together a separate machine for local LLM
training.  Until now, I've been using my desktop PC,
perry
.  I have an RTX 3090
installed, and can get useful training runs done (most recently,
a 163M-parameter GPT-2 small style LLM in JAX
),
but there are a couple of problems.
perry
is my daily driver.  If he's doing a training run, then everything is
just a little bit sluggish as CPU and GPU alike are busy.
Although I don't play games often, it's annoying to have the option ruled out
for days at a time.
While the GPU is busy with a training run, I can't do other experiments in parallel
-- for example, to scope out what the next step might be.
And relatedly to all of those: the two-day limit to the training runs I've been doing is something I set
because that's the maximum amount of time I'm willing to have
perry
tied up.  It
would be really interesting to try longer training runs!
I also have longer-term plans; a multi-GPU box would be interesting to put together --
not just to have more power locally, but so that I could test larger-scale cloud
multi-GPU
training runs before starting to pay for expensive machines.  US$15.92 an hour to rent a machine
isn't a
lot
of money, but it adds up, especially if you're spending it while debugging
parallelism issues.
And finally, I've always been interested in putting together a custom water-cooling
loop in a PC.  I've been building my own machines since 1995 or so, but never got round
to that side of things.  It sounds fun!
But despite all of those future plans, this is a fairly normal machine-building post -- how I repurposed an old PC,
plugged in a second-hand RTX 3090 from eBay, tested it all, accidentally trained an LLM
for 11 days, and almost cooked a CPU.
Over time, I expect
to be posting more -- and more interesting -- build details.  Let's think of this as
establishing the baseline.
poppy
Back before I moved to Lisbon, we had a holiday home here.  When we came over, I'd
bring my laptop, but that was always somewhat unsatisfactory -- limited CPU power for
work, limited GPU for my occasional gaming.
During Covid, we started staying in the holiday home for longer periods -- and this became
too big of an annoyance to ignore.  So in 2020 I put together a small form-factor PC, which I
named
poppy
.  The constraints were:
Small enough to fit in a carry-on bag.  I was building the machine in London, and wanted
to be able to bring her to Portugal easily, and to be able to bring her back if
I wanted to.
Portable enough to quickly move around the flat.  In the holiday home, the dining
room was my study, so I wanted to be able to keep
poppy
there normally, but
move her when we had guests for dinner.
Powerful enough to be able to run the games I was playing -- at the time I was a
big fan of
Assassin's Creed Odyssey
,
which didn't need a flagship card, but wasn't lightweight either.
The build was a bit fiddly, like all SFF PCs.  You can see the component list
and build notes
here on PCPartPicker
, but in short she had:
An AMD Ryzen 5 3600 3.6GHz 6-Core CPU
A Noctua NH-L9a-AM4 CPU cooler
A Gigabyte X570 I AORUS PRO WIFI Mini ITX Motherboard
32 GiB Corsair Vengeance DDR4 RAM
2x Samsung 970 Evo 500 GB NVMe SSDs
A Zotac GTX 1660 Super 6 GiB GPU
A Lian Li PC-TU100 Mini ITX case
A Corsair SF450 450W SFF PSU
She looked like this:
(Gosh, I'd forgotten how... vivid our wallpaper was in that dining room.)
For scale -- that case is slightly taller than two cans of coke stacked on top of
each other.  So, pretty small.
When we moved to Lisbon full-time, I brought
perry
with me from London, and while he's been upgraded
several times since (including adding an RTX 3090
in late 2023
),
he's been my daily driver since.  So
poppy
sat in the corner of my study, sad and unused :-(
It was time to bring her out again.  Initial plan: get her up and running in a new,
larger case, with a PSU that could potentially handle three graphics cards.
Getting her up and running in a new case
Initially, I found that she wouldn't switch on: a quick check suggested that the
problem was the PSU.  I'd had problems with SFF PSUs in the past, and given that
the plan was to give her a new one, I just got one, along with a new, larger case
-- specifically:
An
ASRock Phantom Gaming PG-1600G 1600W
,
which would have power in spades -- an RTX 3090 goes up to about 370W at full
draw, so that should hopefully handle three of them plus a CPU without problems
even if one or two of the GPUs had power spikes.
A
Fractal Design North XL
.
perry
was already in a North (not the XL variant) and I love the case; the XL
one looked like a good option if I was going to be cramming more GPUs in there,
and had plenty of space for water-cooling.
A few days later, the parts arrived.  Here's a family photo:
perry
is to the left,
poppy
centre, sitting on top of her new case, and Cornélia (wearing her Flower of Shame)
is to the right.  For scale, Cornélia is quite a large cat.  (I appreciate that that is not
immensely helpful.)
Time to put the old motherboard and the new PSU into the new case.  Here's what
it looked like:
The Mini-ITX motherboard in a case designed for full ATX looks comically like a postage
stamp.
I switched her on, and luckily enough, everything worked!  Must have been a PSU issue.
The OS that she had was a more than three-year-old version of Arch, so I wiped
the drives and installed the most recent version with my normal config, and it was
time for a quick test.
An LLM training run, because of course it is
One of the nice things about having done all of this LLM training stuff recently is
that you have a ready-made burn-in test for new hardware :-)   I didn't have my
JAX training code
yet,
but I did have the
PyTorch one
.
Now, with her GTX 1660 Super GPU,
poppy
was clearly not going to be able to train
an LLM of the size I could with
perry
's RTX 3090.  I did some fiddling around with
the model and training run parameters, and found that I could fit in a cut-down version
of GPT-2 small with this setup:
Vocab size: 50257 -- this was fixed because I was using the GPT-2 tokeniser.
Context length: down from 1024 to 512
Embedding dimensions: down from 768 to 512
Number of heads: down from 12 to 8
Number of layers: down from 12 to 8
QKV bias: no (different to GPT-2, but the same as my own best local model).
I trained it with a microbatch size of 4, gradient accumulation over 16 steps, and
all other hyperparameters the same as my normal training runs on
perry
.  The number
of training tokens went down -- the model had 76,933,120 parameters, so I needed to
train for just over 20x that -- about 1.5B instead of the 3.2B I've been training my other
models on.
I kicked that off, and out of interest, I kicked off another training run on
perry
with the same setup to see what happened.
The
perry
training run went normally -- GPU running at full blast, 368W, and it completed
in about 9 hours.  That's less than 1/4 of the time my normal training runs take, which
makes sense because time taken for this kind of thing scales roughly linearly with both the size of the model and
the number of tokens, and both of those were about half the normal size.
poppy
was a bit more interesting.  In
nvtop
, the GPU usage showed up as 100%, but
with an "effective" utilisation of 53%.  The power draw matched the latter, being
67W out of a total possible 125W.  I'm not quite sure what was causing that -- clearly
there was a bottleneck somewhere.  Not really worth digging into, though, given that I
was going to replace the card shortly.
Anyway, that took 963,257 seconds to run.  That's 267.57 hours, or just over 11 days.
Yikes.
What's kind of interesting there is that this training run not only took much longer
(which is only to be expected), but that it used more electricity.  67W over 267.57 hours
is just short of 18kWh, whereas 368W over 9 hours is about 3.3kWh.
Buy an RTX 3090, save the planet!
I decided to run my normal evals to confirm that what had come out the other end
was sane.  When asked to complete "Every effort moves you",
perry
's model said:
Every effort moves you and your friends. The key is keeping you informed. But, you still need to be cautious about
And
poppy
's said:
Every effort moves you forward. Every week, you make adjustments to a certain level—just as soon as you leave your
Those were actually rather good, I thought!  And looking at my normal loss test
confirmed that the models really weren't that bad;
perry
's got 3.855702, and
poppy
's 3.855981.  That was actually better than the 3.943522 I'd got on
perry
before
I went down my rabbit hole of optimising hyperparameters
.
So, that was an interesting test -- I was talking to ChatGPT about it at the time
and it called it "maybe an art project", which I thought was amusing if a bit arch.
Time to do something a bit more useful.
An RTX 3090
Finding an RTX 3090 for a decent price from a trustworthy-seeming vendor is kind of
hard right now.  But it's still the sweet spot for price-performance if you're looking
to train models locally, so I set up an alert on eBay, and eventually one popped up
in Bulgaria.  I bought it, and a few days later, this turned up:
It's actually not as ugly as it looks in that photo -- it's considerably uglier.  The
stuff that looks a bit like crinkled aluminium foil is really white plastic with a
kind of crystalline texture.
Made me glad that I'd gone for the mesh-sided case rather than the glass one.
Well, I hadn't bought it for the looks.  I removed the old GTX 1660, and put in the
new card, switched it on, and:
Wow, a disco in my PC.  Lovely.
Testing, phase 1
It was time to kick off another training run to see if it worked.  This time, I did
my normal GPT-2 small sized train with optimised hyperparameters.  It ran for about ten
minutes, and then
poppy
switched herself off.
That didn't look good.
I spent some time digging around trying to work out why my new graphics card was broken,
and then happened to be sending the video above to a friend, and spotted something.
Check out the Noctua fan -- the beige and brown one you can see behind the cooler
mount, above the graphics card.  It wasn't spinning.  That's the CPU cooler fan and
should always be spinning, even if slowly, when the machine is on.
I log basic metrics for all of my PCs to a central InfluxDB instance, so I checked that
out and:
A CPU temperature spike up to about 115°C!  Not good.  Clearly an emergency thermal
shutdown from the CPU.
I initially thought that I must have knocked the fan cable loose
while plugging in the new GPU -- plausible, though they were quite far apart -- but
unplugging then reseating it, then powering up the machine still didn't start the fan spinning.
And it was not visible in the BIOS.
I then zoomed out a bit in Grafana; I only keep 30 days' worth of metrics,
and it had been more than a month since I did my original burn-in test, so I didn't
have anything for that.  But I did have this:
poppy
had been idle for all of that time, and was averaging CPU temps of over
70°C.  The dropoff prior to running the test was because she'd had a chance to
cool down while I installed the GPU.  Having spent ages setting up my InfluxDB
monitoring stuff so that I have metrics for everything, I should probably actually look at them every
now and then, because the fan had obviously not been doing anything for a month or so.
Well, thank goodness for Amazon next-day delivery.  I bought a new
Noctua NF-A9x14 PWM
(praying that
the problem was the fan and not the header on the motherboard), and when it arrived,
I put it in.
Testing, phase 2
This time, when I powered her on, the fan was spinning.  Phew.  I left her running
for an hour, and the CPU temperature stabilised at 35.5°C.  Next, I kicked off a
version of my standard LLM training run with the number of tokens reduced so that
it would run for an hour.
During that, the CPU temperature went up to a moderately-toasty
76°C -- not ideal, but remember that with the broken fan, she was running that hot
at idle.  It seemed a bit odd that it was that hot at 10% CPU usage, but given that one
core was running at 100%, it didn't seem totally off.  The heatsink and fan are designed
for SFF PCs anyway, and those tend to run somewhat hot.
The GPU temperature also went up to 70°C and stabilised there, while
power draw was stably about 368W out of 370W, and GPU utilisation at 100%.
That was particularly pleasing because Nvidia cards throttle at 83°C or so by default, so if I was getting
a lower temperature at full power, the fans clearly had some headroom for cooling.
Once that was completed, it was time for another full training run for a burn-in.
One of these days I'll do something that doesn't involve training an LLM, I promise
I kicked off my normal run.  CPU and GPU temperatures stabilised at the same level as
they had with the one-hour test, which was promising, so it was just a question of
waiting...
...until I got this:
Training complete in 144,531.113 seconds
Tokens seen: 3,260,252,160
Throughput: 22,557 tokens/second
Final train loss: 3.530
About 40 hours, which is pretty much standard -- certainly the same as I'd expect
from
perry
.  The smoke test:
Every effort moves you and your customers to the best possible extent.
Our expertise and expertise have led to our ability to
Don't you just love it when your LLM tries to sell you something? 
But anyway, loss on the test set was 3.548880, which is essentially the same as
the same training run on
perry
too.
Success!
All done for now
So, now
poppy
is a properly-configured training machine -- one RTX 3090, a CPU
that runs a bit hot but at least doesn't do emergency shutdowns, and a case and
a PSU with enough space for more GPUs.
I think that the next step will be to move on to water cooling.  In order to support
more than one GPU, I'll need a new motherboard and probably a new CPU, so I don't think
there's any point in watercooling the latter, despite its toastiness -- I'd just be buying
a waterblock for it that I'd throw away in the not-too-distant future.
Instead, I'll get the block for the GPU, and set up a loop to cool just that.
Who knows -- maybe I can get rid of that horrendous RGB stuff at the same time!
We live in hope.
