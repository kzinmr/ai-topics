---
title: "Making glass-to-metal seals for home­made vacuum tubes."
url: "https://maurycyz.com/projects/glass/1/"
fetched_at: 2026-06-14T07:00:54.834024+00:00
source: "maurycyz.com"
tags: [blog, raw]
---

# Making glass-to-metal seals for home­made vacuum tubes.

Source: https://maurycyz.com/projects/glass/1/

Making glass-to-metal seals for home­made vacuum tubes.
2026-06-13
(
Electronics
)
This page discusses sealing metal through borosilicate/lab glass:
other chemistries behave quite differently.
When making vacuum tubes, glass blowing is actually the easy part:
premade tube stock of almost any size is easly avalable.
Heating the end of such a tube softens the glasss and allows surface tension to close it off.
I used a rotary vane pump to remove all the air from the tube and heated the middle,
which the atmosphere crushed to create a sealed-off ampule.
Because glass is practically impermable, it will retain that vacuum for a very long time,
which can be shown by bringing it close to high-voltage AC (like a tesla coil):
This glow is due to residual air being ionized,
but the fuzzy apearance indicates that the vacuum is good enough to work in a triode or similar device.
For those, the capacitive coupling trick won't work:
I'll need to make electrodes that pass through the glass without letting air in.
Copper's red oxide bonds very well to glass
.
In fact, the bond is stronger than the bulk glass:
when it breaks, there's always a thin layer of glass left stuck to the metal.
Along with it's excelent electrical properties, it's seems like an ideal electrode material.
I tried sealing off the end of the tube like before, but this time with a .75mm wire inside:
The red color indicates a good contact
... and it leaks.
Look under a microscope, the glass around the joint cracked as it cooled.
The culprit is thermal expansion
:
After the glass solidifies at below around 800 °C, it contracts by around 3 μm/m for each degree.
During that same degree of cooling, the copper contracts by 17 μm/m.
Once it's down to room temperature, the metal is around 1% smaller than the glass around it.
Since both the metal and glass are incompressible, the resulting stress builds up until something breaks.
There are some metals that are well matched to borosilicate glass
,
like tungsten (4.5) or molybdenum (5), but they are all rather exotic.
Steel wire is common, and while it's not really matched (CTE is around 11 μm/[m*K]), it's an improvement over copper.
However, the carbon content of the metal produces carbon monoxide on contact with hot glass:
... but there's no reason the bulk metal has to be in contact with the glass.
I had no luck plating the steel out of a copper sulfate solution:
because the reaction is spontaneous, it always happens very fast and creates a fine metal power:
Fe
(s)
+ CuSO
4
(Aq)
→ Cu
(s)
+ FeSO
4
(Aq)
However, electroplating copper works fine in the presense of ammonia.
The copper can disolve as a tetra-amine complex, but the iron is completly insoluble under these conditions.
To create a plating, the copper has to be forced with electricity:
I connected the negative lead of my power supply to the iron and the positive to a piece of sacrifical copper.
At 20 mA, this produced a nice coating in a few seconds:
The wire should be sanded clean before plating
Sealing this in glass created a bubble free seal (if it was done quickly), but it still failed during cooling:
This photo was taken through two layers of glass
Steel differs by ~7 μm/[m*K], and that's enough to break the glass.
However, this plated wire can work in soda lime glass, which has a CTE of around 10
.
This is the most common (and cheapest) type of glass, but I haven't been using it because of it's tendancy to crack while cooling:
Large pieces need to anealed in a furnace over seveal hours.
... but I did adding a bead around the wire:
Instead of the wire breaking away from the glass, the two glass types broke apart.
This actually made the problem worse because the bead is a lot bigger than the wire, so it expands and contracts mre.
Ok, I lied about tungsten wire being exotic
.
Fillament wire is quite common, and I happen to have some.
The snag is that it's 10 μm thick.
I'd say it's hair thin, but that would be an understatement by almost an order of magnitude
(most of my hair is around 70 μm)
That's a standard 2.45 mm header.
For the seal, this is a good thing: less metal means less expantion...
but this size is nearly impossible to handle.
I kept loosing bits of it until I started attaching bright-orange tape to the ends.
Like many metals, tungsten is flamable.
At this size, my oxy-propane torch is able to burn through it in under a second.
This made glassworking a rather frustrating experience.
I initally attempted to make something similar to a neon indicator by passing two wires through a single pinch...
but invisible wire leads to invisible short circuits.
Sealing a single wire in each end worked fine:
... but I had to add glass tee-joint to attach the vacuum.
While the
operating
voltage is well above a thousand volts for a tube this size (filled with air), it does glow nicely:
Neon-free neon sign.
In addition to the plasma, the leads are glowing white hot.
They don't have any air to cool them, are very thin and have poor thermal conductivity.
Tungsten is one of the few metals that can handle this, so I accidentally got a 2-in-1 lamp.
While it is an option, but I'd really rather avoid using this.
Thermal expansion is a factor of size, so the smaller the conductor the less of of a problem it will be
.
10 μm wire is rare, but 10 μm foil is common: you probobly have some in your kitchen.
I rolled out some wire into some thin (30 μm-ish) foil and tried sealing it glass:
The seal looks excelent, but it leaked horribly.
This technique supposidly works in soda-lime glass, where the CTE difference is smaller and the softening temperature is lower,
but it's no good for borosillicate.
(... intrestingly,
the crack formed around the edge of the ribbon, not along the surface.
I'll come back to this later.)
One of the weirder glass-to-metal seals is the houskeeper seal
:
attaching an thin walled copper tube inside a glass tube:
A tube seal used on a high-voltage capacitor
The hollow metal can easly stretch to release any stress from thermal expansion.
However, manufacturing such a tube is difficult without a precision lathe.
A thin copper disk sealed to the end of a tube should also work because it's thickness is unconstrained:
the disk can increase it's radius by stretching thinner.
Both are rotationally symetrical
For a long wire sealed inside a pinch, the metals's only options are to decrease it's density (very hard)
or for it to pull more in from outside the glass (also very hard)...
so stress builds up until the seal breaks.
Producing such foil is easy with a small rolling mill
although a hammer would also work.
It's important to periodically heat the copper to a red heat for a few seconds.
This reforms the metal crystals and allows it be worked without cracking.
Looks ugly, but it's vacuum tight!
The copper sould be cut to size after bonding it to the glass.
If the glass reaches the end of the foil, it will crack around that point.
Once sealed, a hole can be punched in the foil, and a wire soldered through it. 
Because there's no limit on the size of that wire, such a feed-through could be made to handle thousands of amps.
It's also notable because it doesn't require anything fancy:
just normal copper and a blowtorch.
It also works with any type of glass because the coeffiecent-of-thermal-expansion doesn't matter.
... however, it's very frustrating to make.
There isn't much margin between the temperature at which the glass will wet the copper and when the copper melts.
Since the glass doens't wick onto the metal it must be pressed on while providing even heat.
There's also no way to pass multiple wires into the same tube, which complicates the glassblowing.
Knife edge seals
:
borrowing another idea from houskeeper's work, the copper ribbon always breaks around the edges...
so what they are ground down to a sharp point?
On paper, this makes it much easier for the glass to contract around the ribbon:
Not shown: lengthwise compression of the glass
The glass around square corners must contract lengthwise along the seal,
across the width of the ribbon and along its thickness.
Since glass is incompressible, this can't happen and it breaks.
With tapered edges, there's much less stress across the width and the glass can slightly squish to accomodate the metal.
... but it it's not enough and the seal still breaks at the edge:
grumble gruble grumble
Back to the tungsten
:
Large diameter wire is quite exotic, but not unobtainable.
I was able to find some for an only slightly unreasonable price.
Even .65 mm diameter tungsten has no problem being sealed through glass
(after a quick sanding at 600 grit):
Only 8 $/m!
Under a microscope, the seal shows some small bubbles, but no seperation or cracking.
Unlike the fillament wire, this stuff can be easy be handled, bent and welded
(even tungsten is no match for an electic arc)
TLDR;
Tungsten wire or copper disc seals work in borosilicate.
Tungsten wire is expensive and hard to find, but is easy to seal.
Copper seals use common materials but are much harder.
On the topic of
cheating
:
Put mercury or gallium into already cooled glass.
Gallium expands when it freezes, which is enough to break glass.
Some alloys (gallium-indium-tin) stay liquid until amost -20 C which would be a much better choice.
Mercury stays liquid until -40, so this is very unlikely to happen
Both of these can form a vacuum tight seal to glass, but must be prevented from flowing into the tube or evaporting.
I can't think of a good way to do this, but I'm sure it's possible.
Just glue it
: no heat, no problem.
... but plastics aren't vacuum-tight.
Molecules of gas can squeeze inbetween the polymer chains and slowly seep in.
This effect is why hellium ballons will slowly deflate over time,
and how strongly smelling chemicals (like ammonia) escape their bottles.
A glue sealed tube would work if constnatly connected to a pump, but wouldn't be very practical.
Boration
:
Lots of sources recomend treating copper with either sodium borate (borax) or boric acid prior to bonding.
As a test, I used some 250 μm copper foil.
I heated the metal to pre-oxidixed it:
... and applied a saturated solution of sodium borate in water once it cooled:
After using more heat to evaporate the solution, I sanded one side down to bare metal.
... and melted on two similar sized bits of scrap glass, making sure to push the glass down onto the copper.
The foil was allowed to cool in a tray of alumium oxide and once it was down to room temperature, I pried off both blobs:
Both left a layer of glass on the metal, which indicates that the bond was stronger than the surrounding glass.
The borated side was significantly harder to break off, which could indicate less internal stress?
... but that could just be because it's hard to perfectly repeat a bond made using a torch and a randomly shaped bit of glass.
However, the low viscosity liquid borax should help get a bond started
, making it easier to do disk seals.
A low melting point borosilicate-glass paste made by adding extra borax to crushed glass should also work.
Such a "solder glass" would avoid the risk of leaving a water-soluble layer inside the seal.
Also
, the borax side seems to have more bubbles.
This is probobly because I didn't get it hot enough to fully dehydrate before adding the glass.
Leak
testing
:
The capacitive glow discharge trick is handy for testing seals.
Hook the unfinished tube up to a vacuum pump and spray a gas over the supsect area:
If it leaks, a small amount will be pulled into the tube and change the color.
As for the gas, I find the fluorinated refrigerant from a spray duster works well.
Even a tiny amount will alter the color and intensity of the glow.
... but be careful: 
It's flamable and the fumes are
awful
.
Only try this with good ventillation and away from highly flamable materials.
(and watch for arcing around the high voltage source)
Related:
Also, thanks to
hugo.coredump.cx
for letting me borrow their nice macro lens.
