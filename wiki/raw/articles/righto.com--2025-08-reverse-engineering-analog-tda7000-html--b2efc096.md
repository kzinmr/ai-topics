---
title: "How to reverse engineer an analog chip: the TDA7000 FM radio receiver"
url: "http://www.righto.com/2025/08/reverse-engineering-analog-TDA7000.html"
fetched_at: 2026-04-30T07:01:07.528116+00:00
source: "righto.com"
tags: [blog, raw]
---

# How to reverse engineer an analog chip: the TDA7000 FM radio receiver

Source: http://www.righto.com/2025/08/reverse-engineering-analog-TDA7000.html

Have you ever wanted to reverse engineer an analog chip from a die photo?
Wanted to understand what's inside the "black box" of an integrated circuit?
In this article, I explain my reverse engineering process, using the
Philips TDA7000 FM radio receiver chip as an example.
This chip was the first FM radio receiver on a chip.
1
It was designed in 1977—an era of large transistors and a single layer of
metal—so it is much easier to examine than modern chips.
Nonetheless, the TDA7000 is a non-trivial chip with over 100 transistors.
It includes common analog circuits such as differential amplifiers and current mirrors, along with
more obscure circuits such as Gilbert cell mixers.
The die photo above shows the silicon die of the TDA7000; I've labeled the main functional blocks and some interesting
components.
Arranged around the border of the chip are 18 bond pads: the pads are connected by thin gold bond wires
to the pins of the integrated circuit package.
In this chip, the silicon appears greenish, with slightly different colors—gray, pink, and yellow-green—where the
silicon has been "doped" with impurities to change its properties.
Carefully examining the doping patterns will reveal the transistors, resistors, and other microscopic components that make up the chip.
The most visible part of the die is the metal wiring, the speckled white lines that connect the silicon structures.
The metal layer is separated from the silicon underneath by an insulating oxide layer, allowing metal lines to pass over
other circuitry without problem. Where a metal wire connects to the underlying silicon, a small white square is visible;
this square is a hole in the oxide layer, allowing the metal to contact the silicon.
A close-up of the TDA7000 die, showing metal wiring above circuitry.
This chip has a single layer of metal, so it is much easier to examine than modern chips with a dozen or more
layers of metal.
However, the single layer of metal made it much more difficult for the designers to route the wiring while
avoiding crossing wires.
In the die photo above, you can see how the wiring meanders around the circuitry in the middle, going the long way
since the direct route is blocked.
Later, I'll discuss some of the tricks that the designers used to make the layout successful.
NPN transistors
Transistors are the key components in a chip, acting as switches, amplifiers, and other active devices.
While modern integrated circuits are fabricated from MOS transistors, earlier chips such as the TDA7000 were
constructed from bipolar
transistors: NPN and PNP transistors.
The photo below shows an NPN transistor in the TDA7000 as it appears on the chip.
The different shades are regions of silicon that have been doped with various impurities, forming N and P regions
with different electrical properties.
The white lines are the metal wiring connected to the transistor's collector (C), emitter (E), and base (B).
Below the die photo, the cross-section diagram shows how the transistor is constructed.
The region underneath the emitter forms the N-P-N sandwich that defines the NPN transistor.
An NPN transistor and cross-section, adapted from the die photo. The N+ and P+ regions have more doping than the N and P regions.
The parts of an NPN transistor can be identified by their appearance. The emitter is a compact spot, surrounded
by the gray silicon of the base region.
The collector is larger and separated from the emitter and base, sometimes separated by a significant distance.
The colors may appear different in other chips, but the physical structures are similar.
Note that although the base is in the middle conceptually, it is often not in the middle of the physical layout.
The transistor is surrounded by a yellowish-green border of P+ silicon; this border
is an important part of the structure because it isolates the transistor from neighboring transistors.
2
The isolation border is helpful for reverse-engineering because it indicates the boundaries between transistors.
PNP transistors
You might expect PNP transistors to be similar to NPN transistors, just swapping the roles of N and P silicon.
But for a variety of reasons, PNP transistors have an entirely different construction.
They consist of a circular emitter (P), surrounded by a ring-shaped base (N), which is surrounded by the collector (P).
This forms a P-N-P sandwich horizontally (laterally), unlike the vertical structure of an NPN transistor.
In most chips, distinguishing NPN and PNP transistors is straightforward because NPN transistors are rectangular
while PNP transistors are circular.
A PNP transistor and cross-section, adapted from the die photo.
The diagram above shows one of the PNP transistors in the TDA7000.
As with the NPN transistor, the emitter is a compact spot.
The collector consists of gray P-type silicon; in contrast, the
base
of an NPN transistor consists of gray P-type silicon.
Moreover, unlike the NPN transistor, the base contact
of the PNP transistor is at a distance, while the collector contact is closer.
(This is because most of the silicon inside the isolation boundary is N-type silicon. In a PNP transistor, this
region is connected to the base, while in an NPN transistor, this region is connected to the collector.)
It turns out that PNP transistors have poorer performance than NPN transistors for semiconductor reasons
3
,
so most analog circuits use NPN transistors except when PNP transistors are necessary.
For instance, the TDA7000 has over 100 NPN transistors but just nine PNP transistors.
Accordingly, I'll focus my discussion on NPN transistors.
Resistors
Resistors are a key component of analog chips.
The photo below shows a zig-zagging resistor in the TDA7000, formed from gray P-type silicon.
The resistance is proportional to the length,
4
so large-valued resistors snake back and forth to fit into the available
space.
The two red arrows indicate the contacts between the ends of the resistor and the metal wiring.
Note the isolation region around the resistor, the yellowish border.
Without this isolation, two resistors (formed of P-silicon) embedded in N-silicon could form an unintentional PNP transistor.
A resistor on the die of the TDA7000.
Unfortunately, resistors in ICs are very inaccurate; the resistances can vary by 50% from chip to chip.
As a result, analog circuits are typically designed to depend on the
ratio
of resistor values, which is
fairly constant within a chip.
Moreover, high-value resistors are inconveniently large. We'll see below some techniques to reduce the need for
large resistances.
Capacitors
Capacitors are another important component in analog circuits.
The capacitor below is a "junction capacitor", which uses a very large reverse-biased diode as a capacitor.
The pink "fingers" are N-doped regions, embedded in the gray P-doped silicon.
The fingers form a "comb capacitor"; this layout maximizes the perimeter area and thus increases the capacitance.
To produce the reverse bias, the N-silicon fingers are connected to the positive voltage supply through the upper metal strip.
The P silicon is connected to the circuit through the lower metal strip.
A capacitor in the TDA7000. I've blurred the unrelated circuitry.
How does a diode junction form a capacitor?
When a diode is reverse-biased, the contact region between N and P silicon becomes "depleted", forming a thin insulating region between the two conductive silicon regions.
Since an insulator between two conducting surfaces forms a capacitor, the diode acts as a capacitor.
One problem with a diode capacitor is that the capacitance varies with the voltage because the thickness of the
depletion region changes with voltage.
But as we'll see later, the TDA7000's tuning circuit turns this disadvantage into a feature.
Other chips often create a capacitor with a plate of metal over silicon, separated by a thin layer of oxide or other dielectric.
However, the manufacturing process for bipolar chips generally doesn't provide thin oxide, so junction capacitors are a common alternative.
5
On-chip capacitors take up a lot of space and have relatively small capacitance, so IC designers try to avoid capacitors.
The TDA7000 has seven on-chip capacitors but most of the capacitors in this design are larger, external capacitors:
the chip
uses 12 of its 18 pins just to connect external capacitors to the necessary points in the internal circuitry.
Important analog circuits
A few circuits are very common in analog chips.
In this section, I'll explain some of these circuits, but first,
I'll give a highly simplified explanation of an NPN transistor, the minimum you should know for reverse engineering.
(PNP transistors are similar, except the polarities of the voltages and currents are reversed.
Since PNP transistors are rare in the TDA7000, I won't go into details.)
In a transistor, the base controls the current between the collector and
the emitter, allowing the transistor to operate as a switch or an amplifier.
Specifically, if a small current flows from the base of an NPN transistor to the emitter, a much larger current can flow from the collector
to the emitter, larger, perhaps, by a factor of 100.
6
To get a current to flow, the base must be about 0.6 volts higher than the emitter.
As the base voltage continues to increase, the base-emitter current increases exponentially, causing the
collector-emitter current to increase.
(Normally, a resistor will ensure that the base doesn't get much more than 0.6V above the emitter, so the currents
stay reasonable.)
A comparison of the behavior of NPN transistors and PNP transistors.
NPN transistor circuits have some general characteristics.
When there is no base current, the transistor is off: the collector is high and the emitter is low. When the transistor turns on, the current
through the transistor pulls the collector voltage lower and the emitter voltage higher.
Thus, in a rough sense, the emitter is the non-inverting output and the collector is the inverting output.
The complete behavior of transistors is much more complicated.
The nice thing about reverse engineering is that I can assume that the circuit works: the designers needed to
consider factors such as the Early effect, capacitance, and beta, but I can ignore them.
Emitter follower
One of the simplest transistor circuits is the emitter follower.
In this circuit, the emitter voltage follows the base voltage, 
staying about 0.6 volts below the base.
(The 0.6 volt drop is also called a "diode drop" because the base-emitter junction acts like a diode.)
An emitter follower circuit.
This behavior can be explained by a feedback loop.
If the emitter voltage is too high, the current from the base to the emitter drops, so the current through the
collector drops due to the transistor's amplification.
Less current through the resistor reduces the voltage across the resistor (from Ohm's Law), so the emitter
voltage goes down.
Conversely, if the emitter voltage is too low, the base-emitter current increases, increasing the collector current.
This increases the voltage across the resistor, and the emitter voltage goes up.
Thus, the emitter voltage adjusts until the circuit is stable; at this point, the emitter is 0.6 volts below the base.
You might wonder why an emitter follower is useful.
Although the output voltage is lower, the transistor can supply a much higher current.
That is, the emitter follower amplifies a weak input current into a stronger output current.
Moreover, the circuitry on the input side is isolated from the circuitry on the output side,
preventing distortion or feedback.
Current mirror
Most analog chips make extensive use of a circuit called a current mirror.
The idea is you start with one known current, and then you can "clone" multiple copies of the current with a simple transistor circuit, the current mirror.
In the following circuit, a current mirror is implemented with two identical PNP transistors.
A reference current passes through the transistor on the right.
(In this case, the current is set by the resistor.) Since both transistors have the same emitter voltage and base voltage, they source the same current, so the current on the left matches the reference current (more or less).
7
A current mirror circuit using PNP transistors.
A common use of a current mirror is to replace resistors.
As mentioned earlier, resistors inside ICs are inconveniently large.
It saves space to use a current mirror instead of multiple resistors whenever possible.
Moreover, the current mirror is relatively insensitive to the voltages on the different branches, unlike resistors.
Finally, by changing the size of the transistors (or using multiple collectors of different sizes), a current mirror
can provide different currents.
A current mirror on the TDA7000 die.
The TDA7000 doesn't use current mirrors as much as I'd expect, but it has a few.
The die photo above shows one of its current mirrors, constructed from PNP transistors with their distinctive
round appearance.
Two important features will help you recognize a current mirror.
First, one transistor has its base and collector connected; this is the transistor that controls the current.
In the photo, the transistor on the right has this connection.
Second, the bases of the two transistors are connected.
This isn't obvious above because the connection is through the silicon, rather than in the metal.
The trick is that these PNP transistors are inside the same isolation region.
If you look at the earlier cross-section of a PNP transistor, the whole N-silicon region is connected
to the base. 
Thus, two PNP transistors in the same isolation region have their bases invisibly linked, even though
there is just one base contact from the metal layer.
Current sources and sinks
Analog circuits frequently need a constant current.
A straightforward approach is to use a resistor; if a constant voltage is applied, the resistor will produce a constant current.
One disadvantage is that circuits can cause the voltage to vary,
generating unwanted current fluctuations.
Moreover, to produce a small current (and minimize power consumption), the resistor may need to be inconveniently large.
Instead, chips often use a simple circuit to control the current: this circuit is called a "current sink" if the current flows into it and a "current source" if the current
flows out of it.
Many chips use a current mirror as a current source or sink instead.
However, the TDA7000 uses a different approach: a transistor, a resistor, and a reference voltage.
8
The transistor acts like an emitter follower, causing a fixed voltage across the resistor.
By Ohm's Law, this yields a fixed current.
Thus, the circuit sinks a fixed current, controlled by the reference voltage and the size of the resistor.
By using a low reference voltage, the resistor can be kept small.
The current sink circuit used in the TDA7000.
Differential pair amplifier
If you see two transistors with the emitters connected, chances are that it is a differential amplifier:
the most common two-transistor subcircuit used in analog ICs.
9
The idea of a differential amplifier is that it takes the difference of two inputs and amplifies the result.
The differential amplifier is the basis of the operational amplifier (op amp), the comparator, and other circuits.
The TDA7000 uses multiple differential pairs for amplification.
For filtering, the TDA7000 uses op-amps, formed from differential amplifiers.
10
The schematic below shows a simple differential pair.
The current sink at the bottom provides a fixed current I, which is split between the two input transistors.
If the input voltages are equal, the current will be split equally into the two branches (I1 and I2).
But if one of the input voltages is a bit higher than the other, the corresponding transistor will conduct more current,
so that branch gets more current and the other branch gets less.
The resistors in each branch convert the current to a voltage; either side can provide the output.
A small difference in the input voltages results in a large output voltage, providing the amplification.
(Alternatively, both sides can be used as a differential output, which can be fed into a second differential amplifier
stage to provide more amplification.
Note that the two branches have opposite polarity: when one goes up, the other goes down.)
Schematic of a simple differential pair circuit.  The current sink sends a fixed current I through the differential pair.  If the two inputs are equal, the current is split equally between the two branches.  Otherwise, the branch with the higher input voltage gets most of the current.
The diagram below shows the locations of differential amps, voltage references, mixers, and current mirrors.
As you can see, these circuits are extensively used in the TDA7000.
The die with key circuits labeled.
Tips on tracing out circuitry
Over the years, I've found various techniques helpful for tracing out the circuitry in an IC.
In this section, I'll describe some of those techniques.
First, take a look at the datasheet if available.
In the case of the TDA7000, the datasheet and application note provide a detailed block diagram and a description
of the functionality.
21
Sometimes datasheets include a schematic of the chip, but don't be too trusting: datasheet schematics are often
simplified.
Moreover, different manufacturers may use wildly different implementations for the same part number.
Patents can also be helpful, but they may be significantly different from the product.
Mapping the pinout in the datasheet to the pads on the die will make reverse engineering much easier.
The power and ground pads are usually distinctive, with thick traces that go to all parts of the chip,
as shown in the photo below.
Once you have identified the power and ground pads, you can assign the other pads in sequence from the datasheet.
Make sure that these pad assignments make sense. For instance, the TDA7000 datasheet shows special circuitry
between pads 5 and 6 and between pads 13 and 14; the corresponding tuning diodes and RF transistors are visible on
the die.
In most chips, you can distinguish output pins by the large driver transistors next to the pad, but this
turns out not to help with the TDA7000.
Finally, note that chips sometimes have test pads that don't show up in the datasheet.
For instance, the TDA7000 has a test pad, shown below; you can tell that it is a test pad because it doesn't
have a bond wire.
Ground, power, and test pads in the TDA7000.
Once I've determined the power and ground pads, I trace out all the power and ground connections on the die.
This makes it much easier to understand the circuits and also avoids the annoyance of following a highly-used signal around the
chip only to discover that it is simply ground.
Note that NPN transistors will have many collectors connected to power and emitters connected to ground, perhaps through
resistors. 
If you find the opposite situation, you probably have power and ground reversed.
For a small chip, a sheet of paper works fine for sketching out the transistors and their connections.
But with a larger chip, I find that more structure is necessary to avoid getting mixed up in a maze of twisty little
wires, all alike.
My solution is to number each component and color each wire as I trace it out, as shown below.
I use the program KiCad to draw the schematic, using the same transistor numbering.
(The big advantage of KiCad over paper is that I can move circuits around to get a nicer layout.)
This image shows how I color the wires and number the components as I work on it. I use GIMP for drawing on the die, but any drawing program should work fine.
It works better to trace out the circuitry one area at a time, rather than chasing signals all over the chip.
Chips are usually designed with locality, so try to avoid following signals for long distances until you've finished up one block.
A transistor circuit normally needs to be connected to power (if you follow the collectors) and ground (if you follow the emitters).
11
Completing the circuit between power and ground is more likely to give you a useful functional block than randomly tracing out a chain of transistors.
(In other words, follow the bases last.)
Finally, I find that a circuit simulator such as LTspice is handy when trying to understand the behavior of mysterious transistor
circuits. I'll often whip up a simulation of a small sub-circuit if its behavior is unclear.
How FM radio and the TDA7000 work
Before I explain how the TDA7000 chip works, I'll give some background on FM (Frequency Modulation).
Suppose you're listening to a rock song on 97.3 FM.
The number means that the radio station is transmitting at a
carrier
frequency of 97.3 megahertz.
The signal, perhaps a Beyoncé song, is encoded by slightly varying the frequency, increasing the frequency when
the signal is positive and decreasing the frequency when the signal is negative.
The diagram below illustrates frequency modulation; the input signal (red) modulates the output.
Keep in mind that the modulation is highly exaggerated in the diagram; the modulation would be invisible in an accurate diagram
since a radio broadcast changes the frequency by at most ±75 kHz, less than 0.1% of the carrier frequency.
A diagram showing how a signal (red) modulates the carrier (green), yielding the frequency-modulated output (blue). Created by
Gregors
,
CC BY-SA 2.0
.
FM radio's historical competitor is AM (Amplitude Modulation), which varies the height of the signal (the amplitude)
rather than the frequency.
12
One advantage of FM is that it is more resistant to noise than AM; an event such as lightning will interfere with the signal amplitude but will not change the frequency.
Moreover, FM radio provides stereo, while AM radio is mono, but this is due to the implementation of radio stations, not a
fundamental characteristic of FM versus AM.
(The TDA7000 chip doesn't implement stereo.
13
)
Due to various factors, FM stations require more bandwidth than AM, so
FM stations are spaced 200 kHz apart while AM stations are just 10 kHz apart.
An FM receiver such as the TDA7000 must demodulate the radio signal to recover the transmitted audio, converting the changing frequency into a changing signal level.
FM is more difficult to demodulate than AM, which can literally be done with a piece of rock: lead sulfide in a
crystal detector
.
There are several ways to implement an FM demodulator; this chip uses a technique called a quadrature detector.
The key to a quadrature detector is a circuit that shifts the phase, with the amount of phase shift depending on the frequency.
The detector shifts the signal by approximately 90º, multiplies it by the original signal, and then smooths it out with a low-pass filter.
If you do this with a sine wave and a 90º phase shift, the result turns out to be 0.
But since the phase shift depends on the frequency, a higher frequency gets shifted by more than 90º while a lower frequency gets shifted by less than 90º.
The final result turns out to be approximately linear with the frequency, positive for higher frequencies and negative for lower frequencies.
Thus, the FM signal is converted into the desired audio signal.
Like most radios, the TDA7000 uses a technique called superheterodyning that was invented around 1917.
The problem is that FM radio stations use frequencies from 88.0 MHz to 108.0 MHz.
These frequencies are too high to conveniently handle on a chip.
Moreover, it is difficult to design a system that can process a wide range of frequencies.
The solution is to shift the desired radio station's signal to a frequency that is fixed and much lower.
This frequency is called the
intermediate frequency
.
Although FM radios commonly use an intermediate frequency of 10.7 MHz, this was still too high for the TDA7000,
so the designers used an intermediate frequency of just 70 kilohertz.
This frequency shift is accomplished through superheterodyning.
For example, suppose you want to listen to the radio station at 97.3 MHz.
When you tune to this station, you are actually tuning the
local oscillator
to a frequency that is 70 kHz lower,
97.23 MHz in this case.
The local oscillator signal and the radio signal are mixed by multiplying them. 
If you multiply two sine waves, you get one sine wave at the difference of the frequencies and another sine wave at
the sum of the frequencies.
In this case, the two signals are at 70 kHz and 194.53 MHz. 
A low-pass filter (the
IF filter
) discards everything above 70 kHz, leaving just the desired radio station,
now at a fixed and conveniently low frequency.
The rest of the radio can then be optimized to work at 70 kHz.
The Gilbert cell multiplier
But how do you multiply two signals? This is accomplished with a circuit called a Gilbert cell.
14
This circuit takes two differential inputs, multiplies them, and produces a differential output.
The Gilbert cell is a bit tricky to understand,
15
but you can think of it as a stack of differential amplifiers,
with the current directed along one of four paths, depending on which transistors turn on.
For instance, if the A and B inputs are both positive, current will flow through the leftmost transistor,
labeled "pos×pos".
Likewise, if the A and B inputs are both negative, current flows through the rightmost transistor,
labeled "neg×neg".
The outputs from both transistors are connected, so both cases produce a positive output.
Conversely, if one input is positive and the other is negative, current flows through one of the middle transistors,
producing a negative output.
Since the multiplier handles all four cases of positive and negative inputs, it is called a "four-quadrant" multiplier.
Schematic of a Gilbert cell.
Although the Gilbert cell is an uncommon circuit in general, the TDA7000 uses it in multiple places.
The first mixer implements the superheterodyning.
A second mixer provides the FM demodulation, multiplying signals in the quadrature detector described earlier.
The TDA7000 also uses a mixer for its correlator, which determines if the chip is tuned to a station or not.
16
Finally, a Gilbert cell switches the audio off when the radio is not properly tuned.
On the die, the Gilbert cell has a nice symmetry that reflects the schematic.
This is the Gilbert cell for the first mixer. It has capacitors on either side.
The voltage-controlled oscillator
One of the trickiest parts of the TDA7000 design is how it manages to use an intermediate frequency of just 70
kilohertz.
The problem is that 
broadcast FM has a "modulation frequency deviation" of 75 kHz, which means that the broadcast frequency varies by
up to ±75 kHz.
The mixer shifts the broadcast frequency down to 70 kHz, but the shifted frequency will vary by the same amount
as the received signal.
How can you have a 70 kilohertz signal that varies by 75 kilohertz? What happens when the frequency goes negative?
The solution is that the local oscillator frequency (i.e., the frequency that the radio is tuned to) is continuously
modified to track the variation in the broadcast frequency.
Specifically, a change in the received frequency causes the local oscillator frequency to change, but only by 80% as much.
For instance, if the received frequency decreases by 5 hertz, the local oscillator frequency is decreased by 4 hertz.
Recall that the intermediate frequency is the difference between the two frequencies, generated by the mixer,
so the intermediate frequency will decrease by just 1 hertz, not 5 hertz.
The result is that as the broadcast frequency changes by ±75 kHz, the local oscillator frequency changes by
just ±15 kHz, so it never goes negative.
How does the radio constantly adjust the frequency?
The fundamental idea of FM is that the frequency shift corresponds to the output audio signal.
Since the output signal tracks the frequency change, the output signal can be used to modify the local
oscillator's frequency, using a
voltage-controlled oscillator
.
17
Specifically, the circuit uses special "varicap" diodes that vary their capacitance based on the voltage that is applied.
As described earlier, the thickness of a diode's "depletion region" depends on the voltage applied, so the
diode's capacitance will vary with voltage.
It's not a great capacitor, but it is good enough to adjust the frequency.
The varicap diodes allow the local oscillator frequency to be adjusted.
The image above shows how these diodes appear on the die. The diodes are relatively large and located between
two bond pads.
The two diodes have interdigitated "fingers"; this increases the capacitance as described earlier with the "comb capacitor".
The slightly grayish "background" region is the P-type silicon, with a silicon control line extending to the right.
(Changing the voltage on this line changes the capacitance.)
Regions of N-type silicon are underneath the metal fingers, forming the PN junctions of the diodes.
Keep in mind that most of the radio tuning is performed with a variable capacitor that
is external to the chip and adjusts the frequency from 88 MHz to 108 MHz. The capacitance of the diodes
provides the  much smaller adjustment of ±60 kHz.
  Thus, the diodes only need to provide a small capacitance shift.
The VCO and diodes will also adjust the frequency to lock onto the station if the tuning is off by a moderate amount, say, 100 kHz. However, if the tuning is off by a large amount, say, 200 kHz, the FM detector has a "sideband" and the VCO can erroneously lock onto this sideband. This is a problem because the sideband is weak and nonlinear so reception will be bad and will have harmonic distortion. To avoid this problem, the correlator will detect that the tuning is too far off (i.e. the local oscillator is way off from 70 kHz) and will replace the audio with white noise. Thus, the user will realize that they aren't on the station and adjust the tuning, rather than listening to distorted audio and blaming the radio.
Noise source
Where does the radio get the noise signal to replace distorted audio?
The noise is generated from the circuit below, which uses the thermal noise from diodes, amplified by
a differential amplifier.
Specifically, each side of the differential amplifier is connected to two transistors that are wired as diodes
(using the base-emitter junction).
Random thermal fluctuations in the transistors will produce small voltage changes on either side of the amplifier.
The amplifier boosts these fluctuations,
creating the white noise output.
The circuit to generate white noise.
Layout tricks and unusual transistors
Because this chip has just one layer of metal, the designers had to go to considerable effort to connect
all the components without wires crossing.
One common technique to make routing easier is to separate a transistor's emitter, collector, and base,
allowing wires to pass over the transistor.
The transistor below is an example. Note that the collector, base, and emitter have been stretched apart,
allowing one wire to pass between the collector and the base, while two more
pass between the base and the emitter.
Moreover, the transistor layout is flexible: this one has the base in the middle, while many others have the
emitter in the middle. (Putting the collector in the middle won't work since the base needs to be next to the emitter.)
A transistor with gaps between the collector, base, and emitter.
The die photo below illustrates a few more routing tricks.
This photo shows one collector, three emitters, and four bases, but there are three transistors.
How does that work?
First, these three transistors are in the same isolation region, so they share the same "tub" of N-silicon.
If you look back at the cross-section of an NPN transistor, you'll see that this tub is connected to the collector contact.
Thus, all three transistors share the same collector.
18
Next, the two bases on the left are connected to the same gray P-silicon. Thus, the two base contacts are
connected and function as a single base.
In other words, this is a trick to connect the two base wires together through the silicon,
passing under the four other metal wires in the way.
Finally, the two transistors on the right have the emitter and base slightly separated so a wire can pass between them.
When reverse-engineering a chip, be on the lookout for unusual transistor layouts such as these.
Three transistors with an unusual layout.
When all else failed, the designers could use a "cross-under" to let a wire pass under other wires.
The cross-under is essentially a resistor with a relatively low resistance, formed from N-type silicon (pink
in the die photo below).
Because silicon has much higher resistance than metal, cross-unders are avoided unless necessary.
I see just two cross-unders in the TDA7000.
A cross-under in the TDA7000.
The circuit that caused me the most difficulty is the noise generator below.
The transistor highlighted in red below looks straightforward: a resistor is connected to the collector, which is connected to the base.
However, the transistor turned out to be completely different: the collector (red arrow) is on the other side of the circuit and this collector is shared with five other transistors.
The structure that I thought was the collector is simply the contact at the end of the resistor, connected to the base.
The transistors in the noise generator, with a tricky transistor highlighted.
Conclusions
The TDA7000 almost didn't become a product.
It was invented in 1977 by two engineers at the Philips research labs in the Netherlands.
Although Philips was an innovative consumer electronics company in the 1970s, the Philips radio group
wasn't interested in an FM radio chip.
However, a rogue factory manager built a few radios with the chips and sent them to Japanese companies.
The Japanese companies loved the chip and ordered a million of them, convincing Philips to sell the chips.
The TDA7000 became a product in 1983—six years after its creation—and reportedly more than 5 billion have now been sold.
19
Among other things, the chip allowed an FM radio to be built into a wristwatch, with the headphone serving as an antenna.
Since the TDA7000 vastly simplified the construction of a radio, the chip was also popular with electronics hobbyists.
Hobbyist
magazines
provided
plans
and the
chip could be obtained from Radio Shack.
20
Why reverse engineer a chip such as the TDA7000?
In this case, I was answering some questions for the IEEE microchips exhibit, but even when reverse engineering
isn't particularly useful, I enjoy discovering the logic behind the
mysterious patterns on the die.
Moreover, the TDA7000 is a nice chip for reverse engineering because it has large features that are easy to follow,
but it also has many different circuits.
Since the chip has over 100 transistors, you might want to start with a simpler chip, but the TDA7000 is a good
exercise if you want to increase your reverse-engineering skills.
If you want to check your results, my schematic of the TDA7000 is
here
; I don't guarantee 100% accuracy :-)
In any case, I hope you have enjoyed this look at reverse engineering.
Follow me on
Bluesky (
@righto.com
),
Mastodon (
@
[email protected]
),
or
RSS
.
(I've given up on Twitter.)
Thanks to Daniel Mitchell for asking me about the TDA7000 and providing the die photo; be sure to
check out the IEEE Chip Hall of Fame's
TDA7000 article
.
Notes and references
