---
title: "Portable eGPUs Are So Hot Right Now"
url: "https://feed.tedium.co/link/15204/17359582/gigabyte-aorus-5060-ti-ai-box-egpu-review"
fetched_at: 2026-06-12T07:00:54.233784+00:00
source: "tedium.co"
tags: [blog, raw]
---

# Portable eGPUs Are So Hot Right Now

Source: https://feed.tedium.co/link/15204/17359582/gigabyte-aorus-5060-ti-ai-box-egpu-review

It’s hot. It’s kind of heavy.
And on my computing weapon of choice, it’s hard to set up.
But honestly, I love that it exists.
Recently I’ve been taking a look at an eGPU, the Gigabyte Aorus RTX 5060 Ti AI Box, which is essentially a desktop GPU in a relatively small case. I’ve always been really curious about eGPUs, in part because they presumably offer the best of all worlds in many situations. Your laptop stays home with you, but when you want something beastly, you plug an eGPU into your setup, and boom—good graphics.
What makes the AI Box interesting is that it is technically small enough to fit in your laptop bag, while still giving your presumably older laptop a leg up. (As it supports Thunderbolt 5, it also will eventually run faster whenever you get to upgrading the thing.)
Not sure many folks know about this yet, so in case you don’t, here’s your introduction.
The GPU is actually a desktop GPU, though one that got gamer raspberries when it first came out. The Nvidia RTX 5060 was seen as
underpowered and lacking
in the RAM department when it first came out. The 5060 Ti
still got the side-eye
from gamers, but the bump up to 16GB of RAM made it more attractive to creatives or … yes, folks messing around with AI on their local machines.
Part of the reason for this comes down to its design. Unlike most GPUs, it is designed for an eight-lane PCIe gen 5 setup, rather than the more common 16-lane approach. (PCIe has gotten really fast, which is why that’s even possible.) And once you remove the myriad number of fans the thing has, the board is actually quite small.
Oddly enough, I think the context is what really matters here. In a desktop for your average
Black Myth: Wukong
player, it feels a little on the weaker end. But for laptop jockeys who only occasionally load up Steam, it suddenly seems utterly awesome. It is a beacon of miniaturization that someone got a card this powerful to actually in something the size of a traditional Thunderbolt dock.
I had to improvise a case for this. A camera bag with the dividers removed makes for a pretty good one. (I included it in an
eGPU Starter Kit
, if you’re curious.)
You could carry this thing into a Panera and people would look at you like you have a giant power brick. (A small miss in this context is the decision to not include a sturdier case; after looking around, I landed on the
Koolertron Waterproof DSLR Camera Bag
. It fits nicely in a
Chrome bag
.)
And given the speeds of the laptops where this might end up getting used—my HP Envy has dedicated Intel Arc graphics, but they pale in comparison to this thing—and the value prop shows itself.
Another way the value prop shows itself: At $699, it’s not that much more expensive than a standalone 5060 Ti, and it is more or less self-contained, which you definitely can’t say for a low-end eGPU. (It
is
more expensive than what the base price of the card was
supposed
to be, but, y’know, AI.) Most are just cheap adapters that presume that 1) you have a power supply and 2) you’re cool with letting your GPU hang out in the open air. It’s a rare example where you actually get more value from it by setting the upgradeability aside.
(Though maybe not! As noted by
a user on the eGPU.io forums
, the device itself is just a GPU on a very small PCIe card, plugged into an adapter. So if another card like this ever exists, you might even be able to upgrade it.)
It looks like a Thunderbolt dock until you look through the grill and realize there are a couple of pretty big fans in there.
I set this thing up in Linux because I hate myself
I’m not going to sugar-coat it: If you’re buying an eGPU to run on Linux, you’re intentionally asking for a world of pain. Fortunately, as a former
Hackintosher
, I’m a glutton for punishment, and I was willing to experiment to get the upside.
And the problems this box had—freezes whenever the driver was enabled—reminded me of the most stressful parts of troubleshooting kexts in Clover.
The AI Box’s driver situation hasn’t fully been settled on Linux. But that hasn’t stopped some from trying, particularly developer Andrew Obersnel, who has built a project called
nvidia-driver-injector
that essentially patches Nvidia’s driver, then runs it in a Docker container.
What the GPU looks like when it’s working with an additional load on it.
Even with that starting point, it still wasn’t a cakewalk. Obersnel’s tool was written for the more powerful 5090 AI Box—same family, different requirements. On top of that, I was trying to run it in Bazzite DX, an immutable distro, which meant a more complicated state of affairs for me. (I’m used to it.)
Getting this working is absolute gruntwork, the kind of thing where using an LLM can be a huge help, helping to make sense of admittedly complex debugging schemes. It took a few hours, but eventually I hit paydirt.
Unfortunately for me, the next update to Bazzite hit right after and forced me to rebuild everything. Annoying, but a little more LLM gruntwork got me on track. But let it be known: Linux is not for the faint of heart at this time. Hopefully that changes.
Other operating systems offered differing tales: I ran it in Windows 11, installed the Nvidia drivers, and was immediately off to the races. More intriguingly, this GPU can theoretically run on Apple Silicon thanks to some
newly sanctioned drivers
from TinyGrad. I actually tested this method on my M1 Air and immediately ran into a brick wall, but if the card was a little older, it would have worked. Oh well, I’ll give it another shot in six months.
Running speed trials all over the place
My planned use case for this thing involves experimenting with local LLMs and giving creative software, particularly Affinity, a little extra horsepower.
I did run a land speed test in LM Studio by having them run the same prompt. Using Qwen 3 VL 4B, a model small enough to fully fit in the laptop’s Intel Arc chip, the difference was fairly stark. The laptop’s dedicated GPU spat out text at about 14 tokens a second; the eGPU did so at 118 tokens/second. It was not even close, and there’s still headroom on this thing to spare.
The most honest LLM I’ve ever seen: “If there’s any ‘secret’ worth sharing about how LLMs like me work (and why internet-connected ones like ChatGPT wouldn’t dare to admit them), it’s this: we don’t actually know anything.”
Newer models impressed as well, including the new Gemma4 12B model (around 35 tokens per second) and a distilled version of Qwen 3.5 trained on DeepSeek 4 (around 60 tokens per second). At least from a speed perspective, these models are quite capable—and after a little optimization I was able to increase those numbers a little further.
Local LLMs do have limits, however, and they’re easy to hit. I proved this with a very Tedium-coded challenge involving one of my favorite indie-rock dynasties: “Share with me a story about how
Conor Oberst
beat
Tim Kasher
in a trivia game about the history of Omaha.”
All the tests shared a story, but the details were where everything fell flat. Most, not all, of the LLMs were aware that Oberst was the singer of Bright Eyes, but none got close to figuring out which band Kasher led—one said The Decemberists, another said The National. (The answer, of course, is Cursive, or if you’re a real fan, The Good Life.) You don’t trust models with anything factual, of course, but local LLMs are likely more fact-deprived than their server-rack cousins.
And from a coding perspective, you will have to be careful about how you utilize a tool like this, testing some models to find the right balance. For example, I found that Gemma4 struggled to complete coding-related tasks in
Opencode
, while the Qwen/DeepSeek combo I tested did fine, even if it wasn’t quite as smart as DeepSeek proper.
(This is way beyond where it was a year ago, though.)
Minus some interface artifacting, this now runs about as smooth as something like Krita.
One area where I was pleased with the results of this test was Affinity. I did a fresh install of the tool
using the graphical installer
, and after a little troubleshooting, I had a very polished app that excelled in Vulkan mode using this GPU plugged in.
And for the nerds, yes, I did try a game or two. The 2016 edition of Doom, probably the closest thing in my library I have to a heavy game, scored 70fps at 4K medium and neared 100fps at 1440p ultra. Not a bad showing.
But it was a fraught one, in part because of Linuxy issues. I had some issues with resizable BAR (Base Address Register) that I needed to work out, and even after I did that, I ran into frequent freezes when attempting to run a DisplayPort cable through the eGPU itself. I don’t think that’s the device. I think it’s a mixture of driver immaturity and user error. It does mean that until I get it fixed, I’m leaving performance on the table until I bite the bullet and go back to Windows 11.
This is not a plug-and-play device on Linux. In fact, it had a tendency to siphon resources from other plugged-in devices to feed its never-ending desire for bandwidth. (At times, it could disable other devices plugged into a Thunderbolt dock, like my keyboard, mouse, and webcam.) But for those willing to put in the work, it is a very capable one.
The stand, an optional feature, is kind of clever: It sticks onto the bottom with magnets. You can rock this either way, but the heat will be way more manageable the stand.
The eGPU for the rest of us? Not yet, but …
I’m certainly not going to say
that the eGPU market is one that I have a deep understanding of, but its potential has always been a bit difficult to grasp for normal consumers because of what it represents. It’s a tool to bring a stationary task to a portable system, a niche that has never truly had its moment, like mini PCs have.
I think a device like this one gets us closer to such a moment. These things do have real downsides from a technical standpoint: Thunderbolt is just not as fast as a PCIe connection, and to get the best graphical performance out of the thing, you need to plug it into an external monitor. Having it run back through your laptop just tanks performance, though it’s still probably faster than anything else in your machine.
The 5060 Ti AI Box is certainly not the first “breakaway box” that attempts to bring a more portable form of this model to computers. But it is a relatively rare beast—a desktop GPU in a box that is smaller than a standard desktop GPU card. Plus, most prior attempts have been AMD graphics. AMD is fine, but the company is behind from a machine-learning standpoint, even with its recent improvements to
its ROCm computation stack
. (Side note: I think Intel should consider offering an eGPU, or at least push its vendors to offer one, as its Arc cards are fairly price-competitive at this time and would likely play nicer with Linux.)
There’s a possibility that eGPUs could eventually become a bridge device as laptops become more GPU-forward. That phenomenon already happened in the Mac ecosystem and could happen with PCs, based on Nvidia’s recent moves into ARM laptops. Those chips are powerful, with 5070-class GPUs and lots of RAM. But they’re not going to reach normal people for quite a while, thanks in part to their workstation-class positioning.
Unless Nvidia taps into its war chest like Apple has, these are likely going to be mid-four-figure computers. Even enthusiasts might find themselves passing, at least at first.
In that light, an eGPU that can be plugged into a Thunderbolt port and can offer something approaching that experience to a class of people with normie laptops feels like an excellent compromise. That’s especially true if LLMs become more fundamental to how we do work.
When I got this thing, I didn’t think the portability would be such an important part of why I like it so much, but it’s honestly the main feature. I hope we see a dozen models like it.
And I hope we see some real work on making them first-class Linux citizens.
