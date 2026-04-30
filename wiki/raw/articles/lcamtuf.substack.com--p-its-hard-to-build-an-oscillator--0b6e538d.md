---
title: "It's hard to build an oscillator"
url: "https://lcamtuf.substack.com/p/its-hard-to-build-an-oscillator"
fetched_at: 2026-04-30T07:02:02.752430+00:00
source: "lcamtuf.substack.com"
tags: [blog, raw]
---

# It's hard to build an oscillator

Source: https://lcamtuf.substack.com/p/its-hard-to-build-an-oscillator

There’s an old electronics joke that if you want to build an oscillator, you should try building an amplifier. One of the fundamental criteria for oscillation is the presence of signal gain; without it, any oscillation is bound to decay, just like a swing that’s no longer being pushed must eventually come to a stop.
In reality, circuits with gain can occasionally oscillate by accident, but it’s rather difficult to build a good analog oscillator from scratch. The most common category of oscillators you can find on the internet are circuits that don’t work reliably. This is followed by approaches that require exotic components, such as center-tapped inductors or incandescent lightbulbs. The final group are the layouts you can copy, but probably won’t be able to explain to a friend who doesn’t have an EE degree.
In today’s article, I wanted to approach the problem in a different way. I’ll assume that you’re up-to-date on some of the key lessons from earlier articles: that you
can tell the difference between voltage and current
, have a
basic grasp of transistors
, and know what happens when a
capacitor is charged through a resistor
. With this in mind, let’s try to construct an oscillator that’s easy to understand, runs well, and has a predictable operating frequency. Further, let’s do it without peeking at someone else’s homework.
The simplest form of an oscillator is a device that uses negative feedback to cycle back and forth between two unstable states. To illustrate, think of a machine equipped with a light sensor and a robotic arm. In the dark, the machine is compelled to stroll over to the wall switch and flip it on. If it detects light, another part of its programming takes over and toggles the switch off. The machine is doomed to an endless cycle of switch-flipping at a frequency dictated by how quickly it can process information and react.
At first blush, we should be able to replicate this operating principle with a single n-channel MOSFET. After all, a transistor can be used as an electronically-operated switch:
The transistor turns on when the voltage between its gate terminal and the source leg (
Vgs
) exceeds a certain threshold, usually around 2 V. When the power supply first ramps up, the transistor is not conducting. With no current flowing through, there’s no voltage drop across the resistor, so
Vgs
is pulled toward the positive supply rail. Once this voltage crosses about 2 V, the transistor begins to admit current. It stands to reason that the process shorts the bottom terminal of the resistor to the ground and causes
Vgs
will plunge to 0 V. If so, that would restart the cycle and produce a square wave on the output leg.
In practice, this is not the behavior you’ll see. For a MOSFET, the relationship between
Vgs
and the admitted current (
Id
) is steep, but the device is not a binary switch:
BS170 Vgs-Id curve for Vds = 1 V. Captured by author.
In particular, there is a certain point on that curve, somewhere in the vicinity of 2 V, that corresponds to the transistor only admitting a current of about 300 µA. From Ohm’s law, this current flowing through a 10 kΩ resistor will produce a voltage drop of 3 V. In a 5 V circuit, this puts
Vgs
at 5 V - 3 V = 2 V. In other words, there exists a stable equilibrium that prevents oscillation. It’s akin to our robot-operated light switch being half-on.
To fix this issue, we need to build an electronic switch that has no stable midpoint. This is known as
Schmitt trigger
and its simple implementation is shown below:
A discrete-transistor Schmitt trigger.
To analyze the design, let’s assume the circuit is running off
Vsupply = 5
V. If the input signal supplied on the gate of the left transistor is 0 V, this transistor will not be not conducting, which pulls
Vgs
for the other MOSFET all the way to 5 V. That input allows nearly arbitrary currents to flow through the right branch of the circuit, making that current path more or less equivalent to a two-resistor a voltage divider. We can calculate the midpoint voltage of the divider, as marked with an arrow on the schematic:
\(V_{S\textrm{ (input low)}} \approx V_{supply} \cdot { R_{comm} \over { R_{comm} + R2} } \approx 450 \textrm{ mV}\)
This voltage also appears on the source terminal of the input transistor on the left. The actual
Vth
for the
BS170
transistors in my possession is about 2.15 V, so in this scenario, for the input-side transistor to turn on, the supplied signal will need to exceed
Vs + Vth ≈
2.6 V. Once that happens, a large voltage drop will appear across R1, reducing the
Vgs
of the output-side transistor below the threshold of conduction, and choking off the current in the right branch.
At this point, there’s still current flowing through the common resistor on the bottom, but it’s increasingly sourced via the left branch. The left branch forms a new voltage divider; because R1
has a higher resistance than R2,
Vs
is gradually reduced, effectively bumping up the gate-to-source differential
for the left transistor and thus knocking it more firmly into conduction even if the input voltage remains constant. This is a positive feedback that gives the circuit no option to linger in a half-on state.
Once the transition is complete, the voltage drop across the bottom resistor is down from 450 mV to about 50 mV. This means that although the left transistor first turned on when the input signal crossed 2.6 V in reference to the ground, it will not turn off until the voltage drops all the way to 2.2 V — a 400 mV gap.
This circuit lets us build what’s known as a
relaxation oscillator
. To do so, we only need to make two small tweaks. First, we need to loop an inverted output signal back onto the input; the most intuitive way of doing this is to add another transistor in a switch-like configuration similar to the failed design of a single-transistor oscillator mentioned earlier on. This building block, marked on the left, outputs
Vsupply
when the signal routed to the gate terminal is 0 V, and produces roughly 0 V when the input is near
Vsupply
:
A Schmitt trigger oscillator.
Next, to set a sensible oscillation speed, we need to add a time delay, which can be accomplished by charging a capacitor through a resistor (middle section). The resistor needs to be large enough not to overload the inverter stage.
For the component values shown in the schematic, the circuit should oscillate at a frequency of almost exactly 3 kHz when supplied with 5 V:
An oscilloscope trace for the circuit, by author.
The frequency is governed by how long it takes for the capacitor to move
Δv =
400 mV between the two Schmitt thresholds voltages:
the “off” point at 2.2 V and the “on” point at 2.6 V.
Because the overall variation in capacitor voltage is small, the we can squint our eyes and say that the voltage across the 100 kΩ resistor is nearly constant in every charge cycle. When the resistor is connected to the positive rail,
V
R
≈ 5 V – 2.4 V ≈ 2.6 V. Conversely, when the resistor is connected to the ground, we get
V
R
≈ 2.4 V. If the voltages across the resistor are nearly constant, so are the resulting capacitor currents:
\(\begin{array}{c}
I_{C \textrm{ (charging)}} \approx {2.6 \textrm{ V} \over 100 \textrm{ kΩ}} \approx 26 \textrm{ µA} \\
I_{C \textrm{ (discharging)}} \approx {2.4 \textrm{ V} \over 100 \textrm{ kΩ}} \approx 24 \textrm{ µA}

\end{array}

\)
From the
fundamental capacitor equation
(
Δv = I · t/C
), we can solve for the charging time needed to move the voltage by
Δv
= 400 mV; the result is about 154 µs for the charging period and 167 µs for the discharging period. The sum is 321 µs, corresponding to a frequency of about 3.1 kHz – pretty close to real life.
The circuit can be simplified to two transistors at the expense of readability, but if you need an analog oscillator with a lower component count, an
operational amplifier
is your best bet.
If you’re rusty on op-amps, I suggest pausing to review the article linked in the preceding paragraph. That said, to understand the next circuit, all you need to know is that an op-amp compares two input voltages and that
Vout
swings toward the positive rail if
Vin+
≫
Vin-
or toward the negative rail if
Vin+
≪
Vin-
.
An op-amp relaxation oscillator.
For simplicity, let’s choose R1 = R2 = R3 and then look at the non-inverting (
Vin+
) input of the chip. What we have here is a three-way voltage divider: the signal on the non-inverting input is simple average of three voltages:
Vsupply
(5 V), ground (0 V), and
Vout
. We don’t know the value of
Vout
just yet, but it can only vary from 0 V to
Vsupply
, so the
V
in+
signal will always stay between ⅓ ·
Vsupply
and ⅔ ·
Vsupply.
Next, let’s have a look at the inverting input (
Vin-
). When the circuit is first powered on, the capacitor C isn’t charged, so
Vin-
sits at 0 V. Since the voltage on the non-inverting input can’t be lower than ⅓ ·
Vsupply
, this means that on power-on,
Vin+
≫
Vin-
, sending the output voltage toward the positive rail. When
Vout
shoots up, it also bumps the
Vin+
average to ⅔ ·
Vsupply.
Because
Vout
is now high, this starts the process of charging the capacitor through the bottom resistor (R
cap
). After a while, the capacitor voltage is bound to exceed ⅔ ·
Vsupply
. The capacitor voltage is also hooked up to the amplifier’s inverting input, and at that point,
Vin-
begins to exceed
Vin+
, nudging the output voltage lower. Stable equilibrium is not possible because this output voltage drop is immediately reflected in the three-way average present on the
Vin+
leg, pulling it down and causing the difference between
Vin-
and
Vin+
to widen. This positive feedback loop puts the amplifier firmly into the
Vin+
≪
Vin-
territory.
At that point,
Vout
must drop to 0 V, thus lowering the voltage on the non-inverting leg to ⅓ ·
Vsupply
. With
Vout
low, the capacitor starts discharging through R
cap
,. It needs to travel from the current charge state of ⅔ ·
Vsupply
all the way to ⅓ ·
Vsupply
before
Vin-
becomes lower than
Vin+
and the cycle is allowed to restart.
The continued charging and discharging of the capacitor between ⅓ ·
Vsupply
and ⅔ ·
Vsupply
results in periodic oscillation. The circuit produces a square wave signal with a period dictated by the value of C and R
cap
. The frequency of these oscillations can be approximated analogously to what we’ve done for the discrete-transistor variant earlier on. In a 5 V circuit with R1 = R2 = R3, the capacitor charges and discharges by
Δv ≈
1.67 V. If R
cap
= 10 kΩ, then the quasi-constant capacitor charging current is
I
≈
2.5 V / 10 kΩ
≈
250 µA.
Knowing
Δv
and
I
, and assuming C = 1 µF, we can tap into the capacitor equation (
Δv = I · t/C
) to solve for
t
. The result is 6.67 ms. This puts the charge-discharge roundtrip at 13.34 ms, suggesting a frequency of 75 Hz. The actual measurement is shown below:
Oscilloscope trace for the relaxation oscillator. By author.
The observed frequency is about 7% lower than predicted: 70 instead of 75 Hz. Although I could pin this on component tolerances, a more honest explanation is that at
Δv ≈
1.67 V, the constant-current approximation of the capacitor charging process is stretched thin; the segments in the bottom oscilloscope trace diverge quite a bit from a straight line.
Short of reducing R3 to bring down
Δv
and thus reduce the variations in current, the way to develop a better formula is to tap into the equation for a capacitor charged by a constant voltage via a resistor, as derived
here
:
\(V_{cap} = V_{in} \cdot (1 - e^{-t \over RC})\)
To make the math simple, we can use ⅓ ·
Vsupply
as the reference point for the calculation, because that’s the starting voltage for the charging process and the capacitor never discharges below that level. In this view, the “virtual” supply voltage is
Vin =
⅔ ·
Vsupply
(because we took away the unused bottom ⅓ of the range) and the capacitor is charging to
50%
of that value.
To find the charging time, we just need to rearrange the R-C formula for the
Vcap/Vin
ratio, and then solve for
t
at which the ratio works out to 50% (0.5):
\(0.5 = {V_{cap} \over V_{in}} = 1 - e^{-t \over RC}\)
After moving 1 to the left and flipping signs, the equation simplifies to:
\(0.5 = e^{-t \over RC}\)
From there, we can take a natural logarithm of both sides:
\(ln(0.5) = { -t \over RC }\)
…and solve for
t:
\(t = \underbrace{-ln(0.5)}_{=\ ln(2)} \cdot RC\)
In this particular case, the charging resistor is called
Rcap
, so the equation should be restated as:
\(t = ln(2) \cdot R_{cap} \cdot C \approx 0.693 \cdot R_{cap} \cdot C\)
The value of
t
can be used to find the oscillation frequency:
\(f _{osc} = {1 \over 2 \cdot t} \approx {1 \over 1.386 \cdot R_{cap} \cdot C} \approx {0.721 \over R_{cap} \cdot C }\)
If we plug 1 µF and 10 kΩ into the equation, the value works out to 72 Hz, which is within 3% of the observed behavior, comfortably within the tolerances of standard passive components.
As an aside, it’s worth noting that if we revise the circuit to connect the top terminal of
R1
to a lower positive reference voltage, or if we connect the bottom terminal of
R2
to a higher voltage, it will have the effect of reducing the distance between circuit’s Schmitt trigger voltages while still allowing the capacitor to charge from
Vsupply
. Reducing this distance has the effect of increasing the oscillation frequency; this makes for a rudimentary
voltage-controlled oscillator
(VCO), which has a number of uses — from musical instruments, to radios, to
digital clock multipliers
.
The method outlined earlier on is not the only conceptual approach to build oscillators. Another way is to produce resonance. We can do this by taking a standard op-amp voltage follower which uses negative feedback to control the output — and then mess with the feedback loop in a particular way.
An op-amp voltage follower.
In the basic voltage follower configuration, the op-amp reaches a stable equilibrium when
Vin+
≈
Vin-
≈
Vout
. Again, the circuit works only because of the negative feedback loop; in its absence,
Vin-
would diverge from
Vin+
and the output voltage would swing toward one of the supply rails.
To turn this circuit into an oscillator, we can build a feedback loop that normally provides negative feedback, but that inverts the waveform at a particular sine-wave frequency. This turns negative feedback into positive feedback; instead of stabilizing the output voltage, it produces increasing swings, but only at the frequency at which the inversion takes place.
Such a selective waveform inversion sounds complicated, but we can achieve it a familiar building block: an R-C lowpass filter. The mechanics of these filters are discussed in
this article
; in a nutshell, the arrangement produces a frequency-dependent phase shift of 0° (at DC) to -90° (as the frequency approaches infinity). If we cascade a couple of these R-C stages, we can achieve a -180° phase shift at some chosen frequency, which is the same as flipping the waveform.
A minimalistic but well-behaved op-amp solution is shown below:
A rudimentary phase-shift oscillator.
In this particular circuit, an overall -180° shift happens when each of the R-C stages adds its own -60°. It’s easy to find the frequency at which this occurs. In the aforementioned article on signal filtering, we came up with the following formula describing the shift associated with the filter:
\(\theta = -arctan( 2 \pi f R C )\)
Arctangent is the inverse of the tangent function. In a right triangle, the tangent function describes the ratio of lengths of the opposite to the adjacent for a particular angle; the arctangent goes the other way round, giving us an angle for a particular ratio. In other words, if
x
=
tan(α)
then
α
=
arctan(x).
This allows us to rewrite the equation as:
\(2 \pi f R C = -tan(\theta)\)
We’re trying to solve for
f
at which
θ
= -60°; the value of
-tan(-60°)
is roughly 1.73, so we can plug that into the equation and then move everything except
f
to the right. Throwing in the component values for the first R-C stage in the schematic, we obtain:
\(f_{osc} \approx {1.73 \over {2 \pi R C}} \approx {1.73 \over {2 \pi \cdot 1 \textrm{ kΩ} \cdot 100 \textrm{ nF}}} \approx 2.75 \textrm{ kHz}

\)
You’ll notice that the result is the same for the other two stages: they have higher resistances but proportionally lower capacitances, so the denominator of the fraction doesn’t change.
Oscilloscope traces for the circuit are shown below:
Traces for the three R-C stages.
Because the amplifier’s gain isn’t constrained in any way, the output waveform is a square wave. Nevertheless, in a lowpass circuit with these characteristics, the waveforms produced by the R-C stages in response to a square-wave input are close enough to sinusoids that the sine-wave model approximates the behavior nearly perfectly. We can run a discrete-time simulation to show that the sine-wave behavior of these three R-C stages (gray) aligns pretty well with the square-wave case (blue):
A simulation of a square & sine wave passing through three R-C filters.
To make the output a sine wave, it’s possible to tinker with with the feedback loop to lower the circuit’s gain, but it’s hard to get it right; insufficient gain prevents oscillation while excess gain produces distortion. A simpler trick is to tap into the signal on the non-inverting leg (bottom oscilloscope trace) and use the other part of a dual op-amp IC to amplify this signal to your heart’s desire.
Some readers might be wondering why I designed the stages so that each of them has an impedance ten times larger than the stage before it. This is to prevent the filters from appreciably loading each other. If all the impedances were in the same ballpark, the middle filter could source currents from the left as easily as it could from the right. In that situation, finding the point of -180° phase shift with decent accuracy would require calculating the transfer function for the entire six-component Franken-filter; the task is doable but — to use a mathematical term —
rather unpleasant
.
Footnote: in the literature, the circuit is more often constructed using highpass stages and a discrete transistor as an amplifier. I’d wager that most authors who present the discrete-transistor solution have not actually tried it in practice; otherwise, they would have found it to be quite finicky. The version presented in this article is discussed
here
.
If you liked the article, you’ll enjoy
The Secret Life of Circuits
. It’s a richly illustrated, lucid introduction to electronics — from the physics of conduction to embedded system programming. It features 290+ color diagrams, 420+ pages of original content, and zero AI.
👉  For further articles about electronics,
click here
. In particular, you might enjoy:
I write well-researched, original articles about geek culture, electronic circuit design, algorithms, and more. If you like the content, please subscribe.
