---
title: "Making cooled clothing:"
url: "https://maurycyz.com/projects/cooled/"
fetched_at: 2026-07-13T07:01:31.383300+00:00
source: "maurycyz.com"
tags: [blog, raw]
---

# Making cooled clothing:

Source: https://maurycyz.com/projects/cooled/

Making cooled clothing:
2026-07-12
So, summer gets really hot, and it's not going to
get better
anytime soon.
At my place, it isn't actively dangerous
yet
, but it's still unpleasant.
A normal air conditioner
uses a low boiling-point liquid:
something like liquid propane will boil all the way down to -42 C.
Just like water, this evaporation absorbs a lot of heat and the remaining liquid becomes very cold.
Of course, releasing flammable gas is be wasteful and dangerous,
so the vapor is captured and compressed:
This increases the boiling point causing it to condense into a hot liquid.
This condensed refrigerant is cooled back to ambient with a radiator before being passed through a flow restriction to drop the pressure back down:
A fridge or AC (depending on the size of the box)
While this is excellent for cooling a building, it's not great for small-scale applications:
the compressor and hot-side radiator are quite bulky and require a source of electricity.
Thermometric cooling sounds great
:
replace all the plumbing with a solid state semiconductor junction.
Except they don't work particularly well.
Most coolers produce several times more heat than they remove and require huge radiators to avoid overheating.
... on top of their massive power draw and high cost...
Evaporative cooling
is the single most common hot day "hack":
just a bit of water and some airflow.
The problem is that this only works at low humidity.
In most climates (including mine) it's entirely useless when you need it the most.
... although a system with a way to remove humidity (desiccant cooling) would work as a
DIY air conditioner
.
Ok, but what if I could leave the fridge at home and take the cold with me
?
Melting one gram of ice will bottle up a whole 333 joules of heat while staying at a constant temperature.
... but 0 C is just too cold:
direct skin contact is painful so the ice needs to be insulated from the body.
On a hot day, it's >30 C below ambient, so it must also be well insulated from the environment.
What's needed is a (cheap, safe) material with a freezing point around ~20 C.
Pure glycerin
looks promising:
it's melting point is 17.8 C and heat-of-fusion is around 200 J/g.
However, commercial grades contain a few percent of water which pushes the freezing point below that of regular ice.
I don't know of any easy way to purify it. (which is why the factory doesn't bother)
Sodium sulfate
is a very boring chemical:
It's non-corrosive, non-reactive, and less salty than regular salt.
... but it can form "decahydrate" crystals which are 55% water by mass.
Above 32 C, the decahydrate decomposes into water and sodium sulfate.
When cooled, this mixture reforms hydrated crystals.
Thermodynamically, releasing trapped water is the same as melting ice:
absorbing 252 J of heat per gram of decahydrate.
Now, 32 C is just slightly too warm for personal cooling but, just like ice, 
its "freezing point" can be reduced by adding regular salt.
A eutectic mixture gets down to around 18 C —
perfect for staying cool while being easy to transport.
As a bonus, it can be frozen by leaving it in a basement, or any other shaded hole in the ground:
no electricity required.
18 C "ice"
formula:
Quantity (by mass)
1000 g or ml
Water
320 g
Sodium sulfate (anhydrous)
75 g
Table salt
10 g
Polysaccharide thickener [optional]
10 g
Borax [optional]
The preparation is mostly just "mix and heat", but I do recommend adding the thickener last because it can cause the mixture to boil over.
Heat the water, sodium sulfate and sodium chloride until it forms a saturated solution.
  Use a covered container to minimize evaporation.
Mix the borax and thickener as powders and slowly add them to the hot solution.
  Slow addition and constant stirring helps avoid clumping.
Keep the mixture hot (but not boiling) for ~15 minutes to allow it to gel up.
Cool down to room temperature.
These measurements are slightly above the solubility limit in hot water, so there will be some residual salt:
this doesn't cause any problems.
The thickener
can either be Carboxymethyl cellulose (CMC) or Xanthan gum use whichever is easiest to get.
Guar gum and alginate should work, but I have no idea what a good ratio would be.
It's job is to prevent the crystals of decahydrate from settling or forming a hard mass.
Without it, the mixture will still work, but will require agitation.
Xanthan gum is rather clumpy: I find it helps to mix it with another dry powder before adding...
but don't use sodium sulfate because that also likes to clump.
The borax
helps with crystal nucleation and prevents mold growth.
It's allowed as a food additive in the EU (E285)
at 0.4 %
so accidental exposure shouldn't be a problem.
Very large exposures can cause damage, but it doesn't accumulate.
Even so, I've occasionally had the mixture refuse to crystallize during its first cooling:
if that happens, aggressive mixing will fix it.
If supercooling is a recurring problem, try increasing the borax concentration to around 5%.
I recommend adding a water soluble dye
:
this makes it easier to find leaks and tell apart different batches in case one has a problem.
Packaging
:
I initially tried putting it in plastic sandwich bags, but they always leaked.
Double and triple bagging slows the inevitable, but still resulted in a mess.
Heat sealable polyethylene bags are actually able to hold liquid and can withstand quite a bit pressure.
By being a little creative with the sealer, it's possible to create partitioned bags like this:
This will stop all the goo from falling to the bottom when used vertically.
Sealing wet plastic is somewhat questionable, and I've had a few leaks.
These can be fixed with hot-melt glue (which is one of the few things that will bond to polyethylene)
On their own
, these bags work excellently as seat cushions.
To make them wearable, the heat sealed edges can be directly sewn to a strip fabric:
Ugly, but it works
This strip can then be attached to simple shoulder straps to hold the packs in place.
For stronger cooling, additional straps can be used press the packs tightly against the body.
I recommend wearing a t-shirt under the ice packs to stop them from getting nasty,
and putting a light colored, loose-fitting shirt over everything to protect them from sunlight.
The ice packs and shoulder strap assembly can be laid flat a basement floor to freeze.
For continuous cooling, it's possible to make multiple and swap them out.
Test results
& design notes:
To get an idea of how well the salt works, I built a simple "calorimeter" that melted a sample while measuring the amount of heat needed:
For the first test
, I prepared a sodium sulfate brine at 90 C and chilled it down to 25 C.
Re-heating to 32 C, it absorbed around 171 J/g
... 67% of the theoretical for sodium sulfate decahydrate.
The problem is that even a saturated solution doesn't have enough sodium sulfate:
it's maximum solubility is 0.50 g/mL @ 32.2 C.
Near boiling, it drops down to 0.41 g/mL.
41g Na
2
SO
4
+ 100g water = brine (hot)
On paper, this is enough sodium sulfate to form an 82% decahydrate slurry...
but that's assuming the left over water is pure —
in reality, the product is a mixture of decahydrate and saturated brine:
51g Na
2
SO
4
+ 100g water = decahydrate
28g Na
2
SO
4
+ 100g water = brine (25 C)

let:
  x       = decahydrate fraction
  (x - 1) = brine fraction

41 = 51 x + 28 (x - 1)
41 = 51 x + 28x - 28
41 - 28 = 51 x + 28x 
41 - 28 = (51 + 28)x
(41 - 28)/(51 - 28) = x
x = 0.56
[67% is within experimental error]
This is a inherent problem with any Na
2
SO
4
based thermal storage:
Even if you did make pure decahydrate, instead of melting, it will decompose into brine and anhydrous sodium sulfate.
The dry salt likes to settle out which will prevent it from reforming decahydrate.
A water-rich mixture prevents separation... at the cost of ~50% of the heat capacity.
The leftover brine isn't necessary a bad thing:
since there's always liquid water, the pack stays flexible and the gelling agent can stay dissolved.
As a bonus, such a mixture is easy to make:
everything can be mixed together in hot water, no filtering, continuous mixing or grinding needed.
Adding the 7.5% sodium chloride
reduces the heat capacity to around 90 J/g:
Sample weight: 11 g
Sample temp: 12 C -> 22 C
Calorimeter temp: 24 C
Heater: 5 A @ 1.8 V for 2m 47s

Energy delivered: 1.5 kJ
Heat used to warm sample: 500 J (assuming specific heat is similar to water)
Excess cooling: 1 kJ = 90 J/g
This means the cold mixture is ~36% decahydrate and roughly 30% as effective as pure ice, 
The full formula with additives performs similarly.
Solubility with multiple salts is complicated, so I don't have any theoretical values.
However, the result is similar to the published heat-of-fusion for low temperature decahydrate mixtures:
most papers claim somewhere between 60-140 [J/g].
Replacing the sodium chloride with a salt that can also form hydrates (i.e. sodium carbonate) could improve this,
but all the options I could find are corrosive or/and expensive.
Also, adding another salt reintroduces the separation problem
:
Decahydrate can sink to the bottom, forming a layer with low chloride concentration that doesn't melt.
Fortunately, since the mixture never fully freezes, preventing this is easy enough with a thickener.
In a less scientific "hot day" test
,
two 400g, 1cm thick packs stayed at 18 C for around an hour when worn as described.
Using data from the lab tests, they have a combined 72 kJ of cooling capacity and remove 20 W of heat.
Long excursions will require spares, but considering that the material costs pennies, this isn't a big problem.
Related
:
