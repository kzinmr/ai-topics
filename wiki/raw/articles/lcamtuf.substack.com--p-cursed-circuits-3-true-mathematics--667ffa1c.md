---
title: "Cursed circuits #3: true mathematics"
url: "https://lcamtuf.substack.com/p/cursed-circuits-3-true-mathematics"
fetched_at: 2026-04-28T07:02:48.739808+00:00
source: "lcamtuf.substack.com"
tags: [blog, raw]
---

# Cursed circuits #3: true mathematics

Source: https://lcamtuf.substack.com/p/cursed-circuits-3-true-mathematics

In the previous installments of
Cursed Circuits
, we looked at two switched capacitor circuits: the
voltage halver
and the
capacitor lowpass filter
.
In today’s episode, I’d like to talk about the use of operational amplifiers to do something other than amplification: to solve analog math. Analog computing at a scale is wildly impractical because errors tend to accumulate every step along the way; nevertheless, individual techniques find a number of specialized uses, perhaps most prominently in
analog-to-digital converters
. Let’s have a look at how it’s done.
The following assumes familiarity with
core concepts in electronic circuits
and with the
fundamentals of signal amplification
. If you need a refresher, start with the two linked articles first.
Before we get to less obvious circuits, let’s start with a brief recap: operational amplifiers are to analog electronics what logic gates are to digital logic. They are simple but remarkably versatile building blocks that let you accomplish far more than appears possible at first blush.
Unfortunately, in introductory texts, their operation is often explained in confusing ways. All that an op-amp does is taking two input voltages —
V
in-
(“inverting input”) and
V
in+
(“non-inverting input”) — and then outputting a voltage that’s equal to the difference between the two, amplified by a huge factor (
A
OL
, often 100,000 or more) and then referenced to the midpoint of the supply (
V
mid
). You can write it the following way:
\(V_{out} = V_{mid} + (V_{in+} - V_{in-}) \cdot A_{OL}\)
That’s all the chip does. Because the gain is massive, there is a very narrow linear region near
V
in-
=
V
in+
; a difference greater than a couple of microvolts will send the output toward one of the supply rails. The chip doesn’t care about the absolute value of
V
in-
or
V
in+
it can’t “see” any external components you connect to it, and its internal gain can’t be changed.
To show the versatility of the component, we can have a quick look at the following circuit that you might be already familiar with — a non-inverting amplifier:
The basic non-inverting voltage amplifier.
One input of the op-amp is connected to the external signal source:
V
in+
=
V
signal
. The other input is hooked up to a two-resistor voltage divider that straddles the ground and the output leg; the divider’s midpoint voltage is:
\(V_{in-} = {R_g \over R_g + R_f} \cdot V_{out} \)
As discussed earlier, the only way for the op-amp to output voltages other than 0 V or
V
supply
is for
V
in+
to be very close to
V
in-
. We can assume that we’re operating near that equilibrium point, combine the equations for the voltages on the two input legs, and write:
\(V_{signal} \approx {R_g \over R_g + R_f } \cdot V_{out}\)
Solving this for
V
out
, we get:
\(V_{out} \approx V_{signal}  \cdot {R_g + R_f \over R_g} \approx V_{signal} \cdot (1 + {R_f \over R_g})\)
In other words, the output voltage is the input signal amplified by a factor of
1 + R
f
/R
g
. We have a near-ideal single-ended voltage amplifier with a configurable gain. Again, the circuit is probably familiar to most folks dabbling in analog electronics, but it’s worth pondering that we implemented it by adding a couple of resistors to a chip that does something conceptually quite different.
Note: there’s a bit more to op-amp lore when dealing with high-frequency signals; a more rigorous analysis of their frequency characteristics can be found in
this article
.
Now that we have the basics covered, we can show that op-amps can do more than just amplify signals. The first contender is the following summing layout that differs from what’s usually covered in textbooks, but that’s well-suited for single-supply use:
A three-way non-inverting summing amplifier.
Assuming well-behaved signal sources that can supply and sink currents, it should be pretty intuitive that the voltage on the
V
in+
leg is just an average of three input signals:
\(V_{in+} = {V_A + V_B + V_C \over 3}\)
For readers who are unpersuaded, we can show this from Kirchoff’s current law (KCL); the law essentially just says “what comes in must come out” — i.e., the currents flowing into and out of the three-resistor junction must balance out. If we use
V
jct
to denote the voltage at the junction, then from Ohm’s law, we can write the following current equations for each resistor branch:
\(\begin{array}{c}
I_1 = {V_A - V_{jct} \over R} \\
I_2 = {V_B - V_{jct} \over R} \\
I_3 = {V_C - V_{jct} \over R} \\
\end{array}\)
Further, from KCL, we can assert that the currents must balance out:
I
1
+
I
2
+
I
3
= 0 A. Combining all these equations and multiplying both sides by R, we get:
\(V_A + V_B + V_C - 3 \cdot V_{jct} = 0 \textrm{ V}\)
Solving for
V
jct
, we get (
V
A
+
V
B
+
V
C
) / 3. We have a confirmation that the input-side resistor section averages the input voltages.
To be fair, the averaging portion of the circuit has a minor weakness: it depends some inputs sinking current while others source it. Some signal sources might not have that ability. That said, compared to the alternative design, it has the benefit of being more useful in single-supply circuits, so let’s stick with that.
Moving on to the op-amp section: this is just another sighting of the non-inverting amplifier. The gain of the amplifier circuit is set by the
R
f
and
R
g
resistors, and in this instance, works out to A = 1 +
R
f
/R
g
= 3. In other words, the signal on the output leg is:
\(V_{out} \approx 3 \cdot V_{in+} \approx { \cancel{3} \cdot (V_A + V_B + V_C) \over \cancel{3}} \approx V_A + V_B + V_C\)
That looks like a sum! But it also feels like we cheated in some way: it just so happens that we could implement averaging using passive components, and then tack on an amplifier for some gain. Surely, resistor magic can’t get us much further than that?
It can! The next stop is subtraction, which can be achieved with the following circuit topology:
A simple difference amplifier (A - B).
We can start the analysis with the non-inverting input of the amplifier. The signal on this leg is generated by a voltage divider consisting of two identical resistances connected in series between V
A
and the ground. In other words, the voltage here is
V
in+
= ½ · V
A
.
The inverting input is a voltage divider too, except it produces a voltage that’s halfway between
V
B
and
V
out
:
V
in-
= ½ · (
V
B
+
V
out
).
As with any op-amp topology, linear operation can happen only when
V
in-
≈ V
in+
. In other words, we can assert that for the circuit to function, the following must be true:
\(½ \cdot V_A \approx ½ \cdot (V_B + V_{out})\)
We can cancel out the repeated ½ term on both sides, and then reorder the equation to:
\(V_{out} \approx V_A - V_B\)
Neat: that’s precisely what we’ve been trying to do.
To be fair, not all is roses: in a single-supply circuit, an op-amp can’t output negative voltages, so the topology we’ve just analyzed works only if
V
A
> V
B
; otherwise,
V
out
just hits the lower rail and stays there until the input voltages change.
To accommodate use cases where
V
A
< V
B
, we’d need to use a higher output voltage as the “zero” point (
V
zero
). For example, if
V
zero
= 2.5 V, then a computed difference of -1 V could be represented by
V
out
=
V
zero
- 1 V = 1.5 V; in the same vein, a difference of +2 V could correspond to
V
out
= 4.5 V.
To do this, we just need to disconnect the bottom voltage divider from the ground and replace 0 V with a fixed “zero” voltage of our choice. This changes the equation for the positive leg to
V
in+
= ½ · (
V
A
+
V
zero
). The overall equilibrium condition becomes:
\(½ \cdot ( V_A + V_{zero}) \approx ½ \cdot (V_B + V_{out})\)
After tidying up and solving for the output signal, we get:
\(V_{out} \approx V_{zero} + (V_A - V_B)\)
A common choice of a reference point would be the midpoint of the supply (
V
mid
= ½ ·
V
supply
).
The concept of analog computation can be also extended to multiplication and division. The most common and mildly mind-bending approach hinges on the fact that any positive number can be rewritten as a constant base
n
raised to some power; for example, 8 can be written as 2
3
, while 42 is approximately 2
5.3924
.
From the basic properties of exponentiation, it’s easy to show that
n
a
· n
b
is the same as
n
a+b
; it follows that if we have two numbers represented as exponents of a common base, we can reduce the problem of multiplication to the addition of these exponents.
We already know how to build a summing circuit, so all we’re missing is a way to convert a number to an exponent. We don’t really care what base we’re using, as long as the base remains constant over time.
This brings us to the following design:
As before, the linear equilibrium condition requires
V
in-
≈ V
in+
.
Let’s assume that the initial input voltage is about equal to
V
zero
; in this case, the output settles in the same vicinity.
Next, let’s analyze what would happen if the input voltage increased by
v
s
=
100 mV. In such a scenario, for the op-amp to stay at an equilibrium of
V
in-
≈ V
in+
, we would need a sufficient current to flow through the resistor to create a 100 mV voltage drop:
\(I_R = {v_{s} \over R}\)
The op-amp has a very high input impedance, so the current must flow through the diode; if it doesn’t, that’d move the circuit toward a condition of
V
in-
≫
V
in+
, which would cause
V
out
to move toward the negative supply rail. That would forward-bias the diode and thus motivate it to conduct better. In other words, the circuit has an automatic mechanism that coerces the diode to admit the current matching
I
R
, and the amount of convincing is reflected in how much the output voltage has been reduced from the midpoint. We can denote this relative shift as
v
o
.
From an
earlier feature about diodes
, you might recall that although the relationship between the applied diode voltage and the resulting current is complicated, there is an initial region where the component’s V-I curve is exponential. In the following plot for a 1N4148 diode, this property holds up for currents up to about 1 mA:
V-I curve for 1N4148, normal (left) and log scale current (right). By author.
In other words, if the input resistor is large enough (10 kΩ or so), we can say that
v
o
will be dictated by the magnitude of an exponent of some constant base
n
that yields the correct diode current
: I
D
= n
vₒ
.
We also know that the current that must flow through the diode is proportional to the shift in the input signal (
v
s
) divided by
R.
This means that we’ve accomplished the number-to-exponent conversion between
v
s
and
v
o
. Or, in the mathematical parlance, we’ve calculated a logarithm.
To implement multiplication, we need two logarithmic converters on the input side, a summing amplifier to add the exponents, and then an exponential converter that goes from the summed exponent back to a normal value. That last part can be accomplished by switching the location of the diode and the resistor in the log converter circuit we already have.
Integration is just a fancy word for summing values over time; if you want to sound posh, you can say that a bucket in your backyard “integrates” rainfall over the duration of a storm.
Although integration is important in calculus, analog integrators have down-to-earth uses too. For example, the circuits can convert square waves into triangular shapes that are useful in electronic musical instruments. The circuit’s ability to produce very linear up and down slopes also comes in handy in
slope-based and delta-sigma ADCs
.
The simplest, textbook integrator is shown below:
Once again, we can note that the linear operation condition is
V
in-
≈ V
in+
.
Further, let’s assume that the input signal is equal to
V
zero
and the capacitor is discharged, so both op-amp inputs and the output are at about the midpoint.
Next, similarly to the analysis we’ve done for the log amplifier, let’s assume that the input signal shifts up by
v
s
=
100 mV. For the op-amp to stay at an equilibrium, we would need a sufficient current to flow through the resistor to create a 100 mV voltage drop:
I
R
= v
s
/R.
The only possible path for this current is the capacitor; a capacitor doesn’t admit steady currents, but it will allow the movement of charges during the charging process, which will kick off when the op-amp’s output voltage begins to drop; this drop causes a voltage differential appears across the capacitor’s terminals.
From the fundamental capacitor equation, charging the capacitor with a constant current
I
R
for a time
t
will produce the following voltage across its terminals:
\(V_{cap} = {I_R \cdot t \over C} = {v_s \cdot t \over RC}\)
To keep
V
in-
steady, the voltage to which the capacitor gets charged must be accounted for by a directionally opposite shift of the output voltage (
v
o
). The shift will persist after
V
signal
returns to the midpoint, because with no charging or discharging current, the capacitor just retains charge. The shift can be undone if
v
s
swings the other way around.
From the earlier formula for the capacitor voltage, it should be clear that the circuit keeps a sum of (midpoint-relative) input voltages summed over time.
The textbook integrator we’ve been working with has an inverted output:
V
out
moves down whenever
V
signal
moves up; this makes it somewhat clunky to use in single-supply applications. The problem can be addressed in a couple of intuitive ways, but a particularly efficient — if positively cursed — solution is shown below:
The single-supply, non-inverting integrator.
As in all other cases, the prerequisite for linear operation is
V
in-
≈
V
in+
.
We can start the analysis with the two-resistor divider on the top: it simply ensures that
V
in-
is equal to ½ ·
V
out
. As the bottom portion of the circuit, the instantaneous voltage on the non-inverting input is decided by the capacitor’s charge state (
V
cap
). The bottom resistors will influence the charge of the capacitor over time, but if we’re living in the moment, we can combine the equations and write the following equilibrium rule:
\(V_{cap} \approx ½ \cdot V_{out}\)
Equivalently, we can say that
V
out
≈
2 ·
V
cap
.
We have established that
V
out
is equal to twice the value of
V
cap
, but if so, the resistor on the bottom right is subjected to a voltage differential between these two points (always equal to
V
cap
). From Ohm’s law, the resistor will admit the following current:
\(I_1 = {V_{cap} \over R}\)
If the input voltage is zero, the neighboring resistor to the left is subjected to the same voltage differential, so the current flowing into the junction (
I
1
) is the same as the current flowing out (
I
2
). With the currents in balance, the capacitor holds its previous charge and the output voltage doesn’t change.
That said, if the input voltage (
V
signal
) is non-zero, the voltage differential across the terminals of the resistor on the left is different, and the formula for
I
2
becomes:
\(I_2 = {V_{cap} -V_{signal} \over R}\)
In this case, there is a non-zero balance of the currents flowing in and out via the resistors:
\(I_{net} = I_1 - I_2 = {\cancel{V_{cap}} -\cancel{V_{cap}} + V_{signal} \over R} = {V_{signal} \over R}\)
This current is flowing in via the resistor on the right but not flowing out via the resistor on the left, so it necessarily charges the capacitor. Note that the capacitor charging current is independent of
V
cap
; it remains constant as long as the input voltage is constant too.
As before, from the fundamental capacitor equation (V = I·t/C), we can tell that a constant charging current will cause the voltage on the output leg to ramp up in a straight line. Of course, this will come to an end once we hit the output voltage limit of the amplifier. To reset the circuit, we’d need to short the terminals of the capacitor.
👉 For further articles about electronics,
click here
. In particular, you might enjoy:
I write well-researched, original articles about geek culture, electronic circuit design, algorithms, and more. If you like the content, please subscribe.
