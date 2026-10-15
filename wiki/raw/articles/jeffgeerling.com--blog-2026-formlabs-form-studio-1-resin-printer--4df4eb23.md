---
title: "Formlabs dropped the Raspberry Pi on the way to a $699 SLA printer"
url: "https://www.jeffgeerling.com/blog/2026/formlabs-form-studio-1-resin-printer/"
fetched_at: 2026-10-15T10:01:35.973491+00:00
source: "jeffgeerling.com"
tags: [blog, raw]
---

# Formlabs dropped the Raspberry Pi on the way to a $699 SLA printer

Source: https://www.jeffgeerling.com/blog/2026/formlabs-form-studio-1-resin-printer/

Formlabs sent me a
Form Studio 1
resin 3D printer to test after years of back-and-forth about their Form 4 printer.
Like the Form 4, it's an SLA (stereolithography) printer, but unlike the Form 4 (which starts at $2,600), it's affordable for a hobbyist. It's not
cheap
, coming in at $699 (or $749 with a flex build platform, which I highly recommend), but it is affordable.
I can't say as much about this printer as people who are well-versed in resin printing and use other SLA printers (all my experience until now is with FDM, or Fused Deposition Modeling
, printers). But I can convey my first-time experience using this printer and with the entire SLA experience.
It's a more tedious process, which involves resins you can't touch, multiple gallons of IPA (Isopropyl Alcohol) for washing, and curing in UV light... but the end result has a resolution that can't be matched with FDM, and materials ranging from clear resin to flexible rubber are equally unreal to see come off the printer if you’re only used to filament printers.
Besides the tedious post-processing, resin (at least on the consumer level) can't do multi-color/multi-material prints—something that's become almost commonplace on filament printers this year, and has its own interesting use cases.
But I printed a number of items, including the one I was most excited to try—GutBomb's
MacPicoModem
enclosure, but clear, and with the traditional speaker hump that is iconic on Global Village modems for old Macs.
Anyway, I posted my full experience, and a review of the Form Studio 1, in today's video on YouTube:
Formlabs also provided
this link to the Form Studio 1
that tracks where people visit from, but I don't participate in their affiliate program (I only participate in Amazon Affiliates). They are selling four 'special edition' colored plastic versions for a limited time, and I only wish those were permanent options (only grey will be permanent).
The video above goes into a few more details about their value engineering, as well—it takes a lot to go from $2,600 down to $700—and I even had the honor of speaking to KRALYN (who built the Positron, and headed the Studio 1 project) about how they tackled a number of engineering challenges.
One of the more interesting nuggets was their decision to drop the Raspberry Pi Compute Module (used in the Form 4). The Studio 1 adopts a different Arm SoM, and that meant more work building a proper camera driver (Raspberry Pi's camera stack just worked out of the box),
and
going through the wireless certification process (Pi CMs are pre-certified if using their approved antennas). But apparently it was worth it for the cost savings.
Between that, reducing the power output of the UV light, using a cheaper plastic hinge instead of the metal damped hinge on the Form 4, and dropping the mixing arm that is more necessary for higher-end resins (some costing $300+ per liter!), they were able to get the cost a little south of $1,000.
There are other SLA resin printers for half the cost, and some other resins that are cheaper than Formlabs' own, too. I can't speak to reliability or quality versus those printers, but at least having hardware under a grand means Formlabs can address a new audience—people like me, who had a hard time justifying a Form 4. Especially since 'Open Material Mode' is free
on this printer—it's a
$875 addon
for the Form 4!
