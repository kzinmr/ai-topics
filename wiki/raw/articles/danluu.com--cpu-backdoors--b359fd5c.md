---
title: "CPU backdoors"
url: "https://danluu.com/cpu-backdoors/"
fetched_at: 2026-05-05T07:01:33.883152+00:00
source: "Dan Luu"
tags: [blog, raw]
---

# CPU backdoors

Source: https://danluu.com/cpu-backdoors/

It's generally accepted that any piece of software could be compromised with a backdoor. Prominent examples include the
Sony/BMG installer
, which had a backdoor built-in to allow Sony to keep users from copying the CD, which also allowed malicious third-parties to take over any machine with the software installed; the
Samsung Galaxy
, which has a backdoor that allowed the modem to access the device's filesystem, which also allows anyone running
a fake base station to access files on the device
;
Lotus Notes
, which had a backdoor which allowed encryption to be defeated; and
Lenovo laptops
, which pushed all web traffic through a proxy (including HTTPS, via a trusted root certificate) in order to push ads, which allowed anyone with the correct key (which was distributed on every laptop) to intercept HTTPS traffic.
Despite sightings of backdoors in
FPGAs
and
networking gear
, whenever someone brings up the possibility of CPU backdoors, it's still common for people to claim that it's
impossible
. I'm not going to claim that CPU backdoors exist, but I will claim that the implementation is easy, if you've got the right access.
Let's say you wanted to make a backdoor. How would you do it? There are three parts to this: what could a backdoored CPU do, how could the backdoor be accessed, and what kind of compromise would be required to install the backdoor?
Starting with the first item, what does the backdoor do? There are a lot of possibilities. The simplest is to allow privilege escalation: make the CPU to
transition from ring3 to ring0 or SMM
, giving the running process kernel-level privileges. Since it's the CPU that's doing it, this can punch through both hardware and software virtualization. There are a lot of subtler or more invasive things you could do, but privilege escalation is both simple enough and powerful enough that I'm not going to discuss the other options.
Now that you know what you want the backdoor to do, how should it get triggered? Ideally, it will be something that no one will run across by accident, or even by brute force, while looking for backdoors. Even with that limitation, the state space of possible triggers is huge.
Let's look at a particular instruction,
fyl2x
. Under normal operation, it takes two floating point registers as input, giving you
2*80=160
bits to hide a trigger in. If you trigger the backdoor off of a specific pair of values, that's probably safe against random discovery. If you're really worried about someone stumbling across the backdoor by accident, or brute forcing a suspected backdoor, you can check more than the two normal input registers (after all, you've got control of the CPU).
This trigger is nice and simple, but the downside is that hitting the trigger probably requires executing native code since you're unlikely to get chrome or Firefox to emit an
fyl2x
instruction. You could try to work around that by triggering off an instruction you can easily get a JavaScript engine to emit (like an
fadd
). The problem with that is that if you patch an add instruction and add some checks to it, it will become noticeably slower (although, if you can edit the hardware, you should be able to do it with no overhead). It might be possible to create something hard to detect that's triggerable through JavaScript by patching a
rep string
instruction and doing some stuff to set up the appropriate “key” followed by a block copy, or maybe
idiv
. Alternately, if you've managed to get a copy of the design, you can probably figure out a way to use debug logic triggers or performance counters to set off a backdoor when some arbitrary JavaScript gets run.
Alright, now you've got a backdoor. How do you insert the backdoor? In software, you'd either edit the source or the
binary
. In hardware, if you have access to the source, you can edit it as easily as you can in software. The hardware equivalent of recompiling the source, creating physical chips, has tremendously high fixed costs; if you're trying to get your changes into the source, you'll want to either compromise the design and insert your edits before everything is sent off to get manufactured, or compromise the manufacturing process and sneak in your edits at the last second.
If that sounds too hard, you could try compromising the patch mechanism. Most modern CPUs come with a built-in patch mechanism to allow bug fixes after the fact. It's likely that the CPU you're using has been patched, possibly from day one, and possibly as part of a firmware update. The details of the patch mechanism for your CPU are a closely guarded secret. It's likely that the CPU has a public key etched into it, and that it will only accept a patch that's been signed by the right private key.
Is this actually happening? I have no idea. Could it be happening? Absolutely. What are the odds? Well, the primary challenge is non-technical, so I'm not the right person to ask about that. If I had to guess, I'd say no, if for no other reason than the
ease of subverting other equipment
.
I haven't discussed how to make a backdoor that's hard to detect even if someone has access to software you've used to trigger a backdoor. That's harder, but it should be possible once chips start coming with built-in
TPMs
.
If you liked this post, you'll probably enjoy
this post on CPU bugs
and might be interested in
this post about new CPU features over the past 35 years
.
Updates
See
this twitter thread
for much more discussion, some of which is summarized below.
I'm not going to provide individual attributions because there are too many comments, but here's a summary of comments from @hackerfantastic, Arrigo Triulzi, David Kanter, @solardiz, @4Dgifts, Alfredo Ortega, Marsh Ray, and Russ Cox. Mistakes are my own, of course.
AMD's K7 and K8 had their microcode patch mechanisms compromised
, allowing for the sort of attacks mentioned in this post. Turns out, AMD didn't encrypt updates or validate them with a checksum, which lets you easily modify updates until you get one that does what you want.
Here's an example of a backdoor that was created for demonstration purposes
, by Alfredo Ortega.
For folks without a hardware background,
this talk on how to implement a CPU in VHDL is nice, and it has a section on how to implement a backdoor
.
Is it possible to backdoor RDRAND by providing bad random results? Yes. I mentioned that in my first draft of this post, but I got rid of it since my impression was that people don't trust RDRAND and mix the results other sources of entropy. That doesn't make a backdoor useless, but it significantly reduces the value.
Would it be possible to store and dump AES-NI keys? It's probably infeasible to sneak flash memory onto a chip without anyone noticing, but modern chips have logic analyzer facilities that let you store and dump data. However, access to those is through some secret mechanism and it's not clear how you'd even get access to binaries that would let you reverse engineer their operation. That's in stark contrast to the K8 reverse engineering, which was possible because microcode patches get included in firmware updates.
It would be possible to check instruction prefixes for the trigger. x86 lets you put redundant (and contradictory) instruction prefixes on instructions. Which prefixes get used are well defined, so you can add as many prefixes as you want without causing problems (up to the prefix length limit). The issues with this are that it's probably hard to do without sacrificing performance with a microcode patch, the limited number of prefixes and the length limit mean that your effective key size is relatively small if you don't track state across multiple instructions, and that you can only generate the trigger with native code.
As far as anyone knows, this is all speculative, and no one has seen an actual CPU backdoor being used in the wild.
Acknowledgments
Thanks to Leah Hanson for extensive comments, to Aleksey Shipilev and Joe Wilder for suggestions/corrections, and to the many participants in the twitter discussion linked to above. Also, thanks to Markus Siemens for noticing that a bug in some RSS readers was causing problems, and for providing the workaround. That's not really specific to this post, but it happened to come up here.
