---
title: "Notes on optimizing battery life:"
url: "https://maurycyz.com/misc/battery/"
fetched_at: 2026-05-28T07:00:50.759464+00:00
source: "maurycyz.com"
tags: [blog, raw]
---

# Notes on optimizing battery life:

Source: https://maurycyz.com/misc/battery/

Notes on optimizing battery life:
2026-05-27
(
Electronics
)
Ok, so you have something with a battery, and you want it to run for a long time.
I'll be using the classic CR2023 non-rechargeable lithium "coin cell" as an example, but everything here applies to other types of battery.
(except the exact voltage and capacity numbers)
First off, it helps to measure power draw in current
and charge in well, charge.
It is tempting to convert everything into power and energy, but don't.
Most circuit's power draw is much closer to constant current than constant power:
a single clock cycle on a microcontroller involves charging or discharging some number of MOSFET gates.
That requires some number of coulombs, not some number of joules.
Linear regulators turn any circuit into a perfect current sink:
no matter what potential is supplied, the device sees a constant voltage and will always draw the same current.
Even if you don't use any, most chips will use a few to generate internal voltages. 
This is the "typical" current draw of an AVR32DD32 microcontroller over voltage from the
datasheet
:
Black: 25 °C. Yellow: 125 °C.
Also, battery capacity is nearly-universally specified as charge, usually in milliamp hours:
a 100 mAh battery can support 1 mA of current for 100 hours before it's "dead".
(more on what this means later)
Non-ideal
batteries
:
This battery has 3 volts stamped right on it... but that's kinda of a lie:
Measuring the battery with a meter, the voltage is actually 3.3 volts.
However, checking the datasheet, getting the manufacturer's claimed 235 mAh capacity requires operating down to 2 volts:
From the
datasheet
(yes, these have one)
With these "CR" Li/MnO
2
cells, the discharge curve is fairly flat:
a device that only works down to 85% of nominal (2.6 volts) can still use a good 90% of the capacity.
However, an "Alkaline" Zn/MnO
2
1.5 volt cell falls below 80% of nominal with a quarter of it's charge remaining.
The manufacturer considers them dead at 0.8 volts — around half the original voltage.
In a typical circuit, two batteries will be connected in series to produce a 3 V-ish supply.
To get the advertised capacity, the device must be able to run down to 1.6 volts:
the same as a (fresh) single cell!
Think of supply voltage like a budget
:
If your battery will drop down to 2 volts and the MCU needs 1.8 V, any other components
involved in supplying power must not drop more than 200 mV.
It's not that the same MCU won't work on two AA batteries,
but it won't be able to use the last 10% or so of capacity because it requires
at least 1.8 / 2 = 0.9 volt per cell.
Ok, so design for half the nominal supply voltage
?
Nope!
Batteries have non-trivial internal resistance, which causes a voltage drop when any current is drawn:
a coin cell is usually around 10 ohms, while large AA cells sit around 0.1 ohms.
To understand what causes this, let's look at how a coin cell works:
On the negative electrode, a piece of lithium metal looses it's electron and dissolves into the electrolyte.
Li → Li
+
+ e
-
The resulting ions travel over to positive electrode and steal oxygen from the manganese dioxide:
2 MnO
2
+ 2 Li
+
+ e
-
→ Li
2
O + Mn
2
O
3
This reaction releases a lot of energy because lithium is an alkali metal the manganese doesn't really care.
That released energy is actually what powers the connected circuit.
Crucially, the whole thing depends on positive lithium ions reaching and reacting with the positive electrode:
moving against the electric field produced by the battery.
The open circuit voltage, 3.3 volts, is enough to completly stop the reaction.
This is why batteries only discharge once a circuit drains some of the accumulated electrons...
but for the reaction to proceed at a reasonable rate, the voltage must drop quite a bit below the measured open-circuit voltage.
If you've done any chemistry, it should come as no surprise that this is affected by temperature
:
As a rule-of-thumb, to operate down to -40 C, plan for ten times the internal resistance at room temp.
If you see the voltage rail dropping by 50 mV at 20 C, make sure there's still enough voltage to go around if it drops 500 mV.
Another thing that impacts reaction rate is the amount of reagents present
,
or in other words, the charge left in the battery:
resistance increases as the battery is drained.
As a test, I discharged an Alkaline battery at 400 mA:
Orange: open circuit, blue: under load
With a fresh cell, pulling almost half an amp only results in 100 mV of drop, or 0.25 ohms.
By the time the battery is half empty, the resistance doubled to around half an ohm.
At 60% discharge, the under-load voltage has dropped below the 0.8 V "dead" threshold.
Reducing the voltage requirement won't help here:
shortly afterwards, the resistance increased so much my test rig needed to supply power to force those 400 mA through.
The smaller CR2032 cells start at around 10 ohms, and reach several hundred ohms by the time the open-circuit voltage falls to 2 V.
It follows that any circuit that draws a lot of current can not use the full rated capacity.
For pulsed loads, large capacitors can help, but they have their own problems which I'll discuss later.
Also, batteries get worse as they age
.
Electrolytes can evaporate/leak and side-reactions can form layers that impede current.
There's a good chance you've experienced this:
a battery that tests fine on a meter but refuses to actually power anything.
What's happened is that it developed a huge internal resistance (many killohms).
In series with a high-impedance multimeter, it doesn't create any noticeable voltage drop.
When connected to an actual device, the voltage drops to almost nothing.
This is why you should be skeptical of any claims of 20 year, 30 year, 50 year battery life.
Sure, that might be what you get by dividing nominal capacity by average current draw, but there's no telling how well the battery will work after all that time:
I doubt even the manufacture really knows what happens past a decade or two.
There's also self discharge
, where leakage currents drain the battery, even when it's sitting on a shelf:
This is usually given by the manufacturer as percent of capacity per year.
Because the cell's voltage doesn't change all that much during discharge,
— and the current is quite small —
it's a fraction of the original capacity, not of what's remaining.
This alone is enough to kill a AA battery in only 5 years depending on temperature (hotter is worse)...
but again, this is not the only mechanism at play:
Just because self-discharge might suggest a hundred year shelf-life, doesn't mean it will actually work in a hundred years.
Another "fun" effect is voltage droop
:
Drawing current can deplete the chemicals around the electrode, causing a temporary increase in resistance.
Applying a 400 mA current pulse to a half-empty ZnMnO
2
500 mAh cell caused the internal resistance
to triple over the course 40 seconds:
Yellow: cell voltage. Blue: Current
Eventually, the battery does recover, but it took a good minute or so:
Actually a trace of a different pulse, so the starting voltage is higher.
What's interesting is that even though no current is being drawn, the battery circuit voltage is still not back to where it should be.
This is where the "resistance" model starts to break down. 
It's more accurate to say that the pulse temporarily pushed the cell down it's discharge curve:
increasing the resistance and decreasing the open circuit voltage.
This gets worse when the battery is nearly empty:
I applied a similar 10 second pulse to an 80% drained cell,
it took around 5 minutes minutes to for it's open circuit voltage rise back above 0.8 volts.
This effect highly variable depending on temperature (colder is worse) and state of charge, so it's good to include
a wide voltage margin when designing a circuit that will draw sustained current.
In short
, internal resistance increases when...
... it's cold
... the battery is close to being empty
... the battery is used
... you do nothing at all
Plan for a much worse voltage drop than what you see on your workbench:
it's possible to loose as much as a volt per each mA drawn with a mostly empty coin cell on a cold night.
With that in mind
, it's time to look at those capacity numbers.
As already discussed, aiming for longer than a decade or so is largely pointless because of battery aging.
These CR2023 batters have quoted shelf life of 10 years, so it's going to be my target:
From a CR2032 (~230 mAh), a device can draw an average of 2.6 uA if it runs down to 2 volts.
From a AA (~3000 mAh) AA battery, a device can draw 34 uA if it runs down to 0.8 volts per cell.
... so we have a voltage budget and a target current.
Keep in mind that internal resistance will cut into the voltage if when draw pulses in excess of a few microamps.
Measurement
techniques:
These small currents present a problem:
most multimeters don't really do well below a microamp.
Benchtop models that can measure down to the nanoamps exist but are quite expensive.
On paper, measuring current is easy:
Insert a known resistor into the circuit and measure the voltage drop across it...
except this either requires adding a large resistance or measuring a tiny voltage.
A better way is to use an op-amp to hide the voltage drop from the device under test:
The amplifier tries to keep its two inputs at the same voltage, which requires it to exactly match the
device's current through the feedback resistor.
This results in exactly the same voltage as if it was used as a shunt, except with zero burden voltage.
What's with that other opamp?
Since most chips have two opamps, I use the other to create a VDD/2 supply rail which is used as the ground.
This allows the chip to have access to voltages both above and below it.
Most modern chips are "rail-to-rail", meaning they are designed to operate close to one of the supply rails...
but this doesn't work too well:
Consider what happens when the input current drops to zero.
The amplifier has to pull the output (with a non-trivial amount of capacitance) down to zero. 
If the best the amplifier could do is connect the output to the negative rail,
the voltage would exponentially decay, approaching zero but never reaching it.
Would this be a huge problem? Probably not.
Is it a good idea to make the chip's job as easy as possible? Yes.
As a bonus, this allows the device to measure currents in both directions.
Using the 100 pA/mV range, the circuit has an offset of ~10 pA, so it's not quite a picoammeter, but it's close.
This makes it good for testing the leakage of MOSFETs, diodes, capacitors and the such.
However, this design has one huge snag:
It's zero burden voltage up to a fairly modest point.
Once the output maxes out (100 nA - 100 uA depending on the range), the device will can see the full shunt resistance.
This is a non-issue for testing component leakage,
but it becomes a problem when measuring the current drawn by a microcontroller.
For measuring sleep current, it's best to build a firmware image that never wakes up,
and short the meter's input or connect a second power source during startup.
Another option is to use a tiny feedback resistor:
connecting a 1 kohm resistor between the input and output yields a 1 uA/mV range with a maximum of 1 mA.
Once the microcontroller boots, the resistor can be removed to measure it's sleep current.
(and if you are drawing more than this, you probably shouldn't)
This is also a good trick to avoid crashing MCUs when switching ranges,
which can cause a momentary disconnection depending on the geometry of your selector switch.
Shielding is not optional
:
100 picoamps is a kind of current that floats around on the air.
It's best to put the whole setup inside a metal box connected to the meter's ground.
Running coax to a scope or meter is fine because the wire's sheath is connected to the rest of the shield:
this isn't RF stuff.
If you don't have a box, wrapping the whole thing in aluminum foil works almost as well.
(make sure it's not touching anything!)
Also, it's a little silly to carefully screen out interference only to reintroduce it with a power supply,
so it's best to run everything with batteries:
Two 1.5 volt alkaline cells provides 3 volts and four is close enough to 5 volts.
Also, be careful with what's touching the meter
or part under test:
a post-it note can easily conduct a whole nanoamp at 5 volts.
Wood and fabric are similarly problematic.
If in doubt as to if something is a problem, test it.
When measuring capacitors, there's a really annoying property to be aware of
:
The dielectric material can slowly absorb or release charge over multiple hours.
This effect is mostly known for recharging high-voltage capacitors after they've been removed from circuit
— with unpleasant results —
but it can also result in a deceptively high leakage current that goes away if the capacitor is used in a real circuit.
Unless you have fancy polypropylene capacitors, you'll have to leave them in the test rig for several hours before taking a reading.
Circuit testing
:
Of course, it's not enough to test individual components.
The whole system has to work correctly with an imperfect power supply:
A device running on a coin cell should be able to tolerate the full 1k with a two volt supply.
... also, it's a good idea to simulate a dead battery:
an empty battery shouldn't result in hardware damage or data loss.
Temperature can greatly effect leakage currents.
If you expect the components to get up to 80 C, grab a heat gun and see how it performs at those temperatures.
Practical
advice:
Before considering any components, does to circuit board itself consume any power?
There's lots of people on forums saying you shouldn't use a soldermask, or that flux on the board causes leakage...
For testing, I used a nothing special JLCPCB, green, FR4, 2-layer board.
It had two quarter millimeter traces 30 mm long and separated by 2.7 mm.
For the measurements, I used a 9 volt bias, which should represent worst case results:
Clean
: Testing the board as it came from the factory
Humid
: Breathing on it for a few seconds (99% RH, no visible condensation)
Fingers
: Touching it to get skin oils on the board
Rosin
: Spread some RMA flux and burned it with a soldering iron.
Board condition and soldermask
Current
Soldermask, clean
< 5 pA
Soldermask, fingers
< 5 pA
Soldermask, humid
< 5 pA
Soldermask, rosin
< 5 pA
No soldermask, clean
< 5 pA
No soldermask, fingers
10 pA
No soldermask, humid
30,000 pA
No soldermask, rosin
20 pA
The main troublemaker is humidity.
If you are designing a circuit that needs to work outside,
underwater or underground, it would be a good idea to include some desiccants:
most plastic will allow water vapor to permeate inside.
The soldermask prevented any significant leakage between traces,
but problems could still happen between component pins.
Conformal coatings will protect against short exposures, but will suffer from the permation problem.
Soldering residue or skin oils aren't a problem unless you are doing picoamp metrology.
Capacitors
:
Electrolytic or tantalum capacitors can leak multiple microamps at just a few volts:
A jellybean 100 uF 16V electrolytic pulled 26 uA at nine volts,
which is ten times the entire current budget for a CR2032!
That cap alone could discharge the battery just a year or two.
Ceramic capacitors a lot better:
I grabbed a random 1 uF capacitor from my parts bin initially pulled several hundred nanoamps, but it dropped down to 920 pA @9 volts after two hours.
Even a hundred of these would only draw 92 nA, which is only 3% of the budget.
TLDR
; Don't use electrolytic or tantalums. Ceramic capacitors are fine
in reasonable quantities and when run well below their rated voltage.
Diodes
:
Diodes are very commonly used for reverse polarity protection, but there are two possible configurations:

A series diode uses a forward biased diode to prevent reverse current from getting to the device.
A parallel diode adds a reverse biased diode to clamp the reverse voltage before the device is damaged.
In the series configuration, voltage drop is very important
:
Real diodes are quite different from the idealized model.
The voltage drop of a 1N4148 is only 0.6 V at 1 mA of draw and at 25 C.
The relationship between current and voltage drop is roughly exponential:
For a silicon PN diode, passing 10 times the current requires an extra 100 mV.
This also works in the other direction:
A circuit that only needs 10 uA (peak) will only see around 0.4 volts of drop across that diode.
Temperature affects this:
The threshold will rise ~2 mV for each degree the diode is cooled.
At -40, expect 130 mV of extra voltage drop compared at room temperature.
A Schottky diode has a much lower threshold voltage:
1 mA of current only needs 0.25 V.
This can be a huge improvement to your voltage budget, although it's still a non-trivial amount.
In the parallel configuration, reverse leakage matters
.
Because it's highly dependent on voltage, I measured a few diodes at 5 volts, which is closer to normal operating conditions:
2N4148 [PN] @5V: 2.3 nA
BAT46 [Schottky] @5V: 2.4
uA
In this test, the schottky doesn't do so well:
It's three orders of magnitude worse than a similar PN diode.
So, use a PN diode right?
Well, if the battery can supply 50 mA into a short (fresh coin cell), there might be around a volt across the device.
That can be enough to cause damage.
So, what's a good reverse polarity protection circuit?
An n-channel low-side switching version is also possible
A MOSFET can act as a near ideal diode:
If the gate (connected to the negative rail) is in fact, the lowest voltage, it's switched on.
If the battery is inserted backwards, the gate now has the highest voltage in the circuit and the transistor stays off.
However, it's still important to consult the datasheet or conduct experiments:
the battery voltage might not be enough to fully turn on the FET,
and even a properly "on" MOSFET still has a voltage drop.
The final option is nothing:
Battery clips that physically prevent a user from inserting a battery backward exist.
These have no electrical penalties except for the contact resistance (which is negligible when compared to the battery's).
Schottky leakage also poses a problem for dual power supply circuits.
A microamp of backfeed into the backup battery can actually be enough to damage it.
In these cases, you may be forced to use a PN diode or use a variation of the MOSFET trick:
connect the gate to the primary supply rail.
This will, at a minimum, perform as well as a silicon diode because of the transistor's intrinsic body diode.
Once the power rail drops down to zero, the MOSFET's gate will be negative and it will turn on.
However, it's performance won't be perfect if the main rail takes more than a millisecond or so to loose voltage.
It's best to plan for a PN diode drop and consider any extra voltage as be a nice bonus.
Computers
:
In theory, CMOS logic doesn't draw any power when sitting idle.
In practice, it absolutely does.
An 8-bit AVR128DD28 microcontroller draws 1.5 uA during sleep mode.
Connecting a 32KHz crystal and using the integrated RTC to provide wake ups bring it up to 1.8 uA.
This leaves just 700 uA of average current to work with.
Ok, but at some point, the processor has to do something.
Each clock cycle has a fixed cost:
For the AVR, I measured it at ~0.28 nanoamp seconds, meaning that the battery has enough power for 3,000 billion cycles.
Individual clock cycles on an AVR128DA28 running at 32 kHz.
However, it's almost always a good idea to use a slow clock:
The chip will draw an extra 277 uA of current draw per MHz.
At the default four MHz clock speed, that's just over a milliamp.
There's no guarantee the battery will be able to supply that kind of power.
Decoupling caps aren't going to save you here:
1 mA is enough to drain a rather big 1 uF capacitor at 1 volt per millisecond.
(remember, no electrolytics allowed.)
Since the MCU has a minimum voltage of 1.8 volts,
and the batteries can go as low as two, it's only safe to run like this for 200 microseconds / 800 cycles!
However, running at 32 kHz only draws an average of 10 microamps.
There are still current pulses from each clock cycle, but there are small enough to that they only drop a 1 uF capacitor by 0.27 millivolts.
The processor does draw more a bit more quiescent current while running then in sleep mode.
This is why some people suggest you should run at the maximum clock speed to save power...
but while it is more efficient on paper, it simply doesn't work with real batteries.
This also lets us calculate how long it can run for:
10 microamps is 14 times the remaining 700 nanoamp budget, so the processor can be running 7% of the time.
Also, on this particular MCU, wakeups cause a big current pulse:
Because of stray capacitance, applying power to the processor costs a whole 2.62 nanoamp seconds.
With a 1 uF capacitor, this would drain it by 2.62 mV.
However, with smaller caps like 6.8 nF, it could would discharge them a whole 385 mV.
Stuff like this is why I'd recommend using around a microfarad:
A decent 1 uF (MLCC) ceramic rated at a few times the supply voltage will leak almost nothing.
To be fair, the datasheet does recommend this value,
but plenty of people are in the habit of using smaller ones:
When you have a 5 volt supply, loosing a third of a volt is not a big deal.
Using a 3-but-actually-2 volt battery, it's enough to drop below the chip's minimum operating voltage.
Some parts claim a much lower sleep current (in the nanoamps), but that's without retaining memory:
Most applications can't use these modes.
Consider a data-logger.
Because flash consumes the same amount of power when writing a few bytes or a kilobyte, being able to buffer readings actually saves power.
... although there are some applications where a feature like this does make sense:
This is something you have to consider before taking sleep current specs at face value.
Related
:
