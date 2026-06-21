---
title: "Glassblowing #3: A better thermionic diode"
url: "https://maurycyz.com/projects/glass/3/"
fetched_at: 2026-06-21T07:00:49.478522+00:00
source: "maurycyz.com"
tags: [blog, raw]
---

# Glassblowing #3: A better thermionic diode

Source: https://maurycyz.com/projects/glass/3/

Glassblowing #3: A better thermionic diode
2026-06-20
My last attempt at a
vacuum tube
technically worked,
but not very well because there was a lot of glass between the anode and cathode:
Because of this, many any electrons that miss anode and build up on the glass.
This negative charge will keep accumulating until it's strong enough to overpower the anode's positive charge.
With enough voltage, some current does flow, but a diode that only conducts a microamp at 1000 V is not very useful.
On paper, the solution is simple: surround the filament in anode.
This shields it against the influence of any accumulated charge and allows continuous current flow:
In practice, building something something like this is tricky
.
There are the three wires that must be precicly aligned while being sealed through hot glass.
For my tube, I started by attaching the leads to a chunk of scrap glass which keeps them aligned throughout the process:
The internals can be attached on one side of the glass, and the other side can be sealed in an envelope without any risk of the tube falling apart.
My filament is ~2 cm of 12 μm tungsten wire, wrapped around hooks made from the lead-in wires.
The anode is a square of copper foil, which I bent into a tube and welded onto the leadframe:
Look, welding to tungsten isn't easy
This tube is a shorter than the fillament to leave the ends visible and reduce the risk of shorts.
Additionally, I left a ~1 mm gap in the anode to monitor for sagging:
Like my other tubes, the lead-ins are 0.3 mm tungsten wire pinched inside borosilicate glass:
My glass bead was slightly too large
and didn't fit in the envelope alongside the (slighly off-axis) anode tube.
The resulting bend caused the filament hook to touch the anode, which I didn't notice before sealing it.
In any case, I fixed the problem by indenting the glass:
Before connecting my vacuum pump, I drew the envelope tube down to ~4 mm diameter which would be easier to seal:
large diameter tubes tend to blow through instead of evenly collapsing when heated under vacuum.
While pumping the tube down, I ran the filament for a few seconds at 4.5 V.
This should be enough to remove trapped gasses that would otherwise contaminate the vacuum.
After a few minutes of pumping, I heated the narrowed section with a torch to seal it.
This is a good time to pull the finished device away from the left over tubing, but this is completly optional.
My pump is a nothing special rotary-vane unit
connected by a meter of rubber hose,
so the vacuum isn't great, but that doesn't matter:
if you're thinking of trying this, there's no need for a fancy turbomolecular pump or high-vacuum system.
I'd estimate the tube is somewhere around 100 μmHg or 10 Pa based on how long it was connected.
There was a stray bit of fillament wire
bridging the heater pins,
which was easly fixed by applying five volts across the tube:
the shorter length draws a lot of current and it burned out in a few seconds.
On the topic, it's common for an insulating layer of oxide to form on the fillament while making a tube.
This breaks down at a fairly modest voltage (15 V-ish), but that's too much to safely put across the filament.
Because of this, I highly recomend doing initial tests with a current limited supply, using a current limiting resistor.
Once a current flows, the metal surfaces weld togther and the device can be driven with constant-voltage.
Performance
:
Without any fancy coatings, the fillament has to be white hot for anything to happen.
At three volts, it visibly glows, but no electrons are emitted.
At four, the tube starts working:
Plotted 2 h after sealing, after a 30 minute burn-in at 4 V
There is a potential gradient across the fillament.
For these graphs, I measured between the plate and the positive side of the filament, so the voltages will be somewhat lower than reality.
Unlike semiconductor diodes, thermionic ones are near-ohmic at low currents.
Here, it plateaus beyond 8 volts because the fillament can only emit a limited number of electrons each second.
At four volts, the fillament is draws 286 mA of current and 1.1 W of power.
(this is typical for small tubes)
Under these same conditions, the reverse leakage is 22 nA at 200 V, which is quite respectable.
Things get weird at higher temperatures
:
If = 285 mA, 300 mA, 322 mA, 333 mA
Running the heater at five volts, the plate current increases sharpy past 13 V.
At 5.5 volts, the same happens except with even more current: the diode passes several milliamps with 18 V on the plate.
I suspect this is townsend discharge:
the electrons emitted by the fillament get eccelerated by the voltage and smash into residual air molecules.
If the voltage is high enough, these impacts knock more electrons free increasing how much current can flow.
Unlike in glow discharge, the larger and heavier positive ions can't pick up enough speed to cause further ionization,
so the plasma doesn't grow exponentially:
it requires a steady influx of fresh electrons from the cathode.
Because of this, the tube still works as a diode in this region...
although with very different properties than one with a high vacuum.
Gas rectifiers operating like this did see some historical use,
like the Soviet GG1-2/5, although they are very obscure today.
Mercury arc rectifiers operate on a similar priniple, except they use a electric arc to generate electrons
... but this doesn't expain why it only happens at high temperatures.
Perhaps the gas being hot adds more kenetic energy to the colisions?
Or perhaps there's some reversible adsorption increasing the pressure?
Ok, but the whole point of working in glass
is make a tube that can exist without being connected to a pump.
Can it?
So far,
yes
: after 24 hours, it performs identically to the initial tests.
I'll update this page with follow up data in a week or so.
Related
:
