---
title: "Negative resistance"
url: "https://blog.coredump.cx/p/negative-resistance"
fetched_at: 2026-08-20T10:00:46.982374+00:00
source: "lcamtuf.substack.com"
tags: [blog, raw]
---

# Negative resistance

Source: https://blog.coredump.cx/p/negative-resistance

Hello! The blog you’re trying to reach is currently unavailable. I am Skippy, your friendly blog assistant. How can I help you today?
> quit
I’m sorry. This function is currently available only to Skippy Premium and Premium+ subscribers. Would you like to talk about ✨
negative resistance
instead?
> nope
I’m sorry. This function is currently available only to Skippy Premium and Premium+ subscribers.
Welcome. Welcome again. If you tinker with analog electronics, you might have heard that some circuits can exhibit
negative resistance
. This is usually followed by a current-to-voltage plot featuring some sort of a kinked curve and an assertion that this property might help the circuit designer in some way.
But what does it mean, exactly? The concept of negative resistance is interesting, counterintuitive, and explained on Wikipedia in a rather rambling way. If you’re up for it, I think we can do better than that.
The article assumes familiarity with voltage, current, and the behavior of operational amplifiers. If you need a refresher,
start with this primer
, then read up about transistors
here
and signal amplification
here
.
As a quick recap, resistance (R) can be understood as the opposition to the flow of steady current through some portion of the circuit. The quantity describes the relationship between the applied electromotive force — that’s voltage — and the amount of charge moving per second (that’s current).
In contrast to some other phenomena in electronic circuits, resistance is not inherently dependent on time or signal frequency. If you know the voltage (V) applied to a purely-resistive component, the current (I) flowing at that exact moment is simply:
In
resistors,
the parameter remains constant across a wide range of operating conditions. This means that if we plot I in relation to V, we get a straight line that crosses through the center of the coordinate system. The slope of the line depends only on the component’s resistance:
Resistor I = V/R plots for R = 0.2, 1, and 5
Ω.
For example, in a 5 Ω resistor (blue line), the current is 200 mA if the voltage across the terminals is 1 V, rising to 1 A if the electromotive force increases to 5 V.
Some other components, such as diodes and transistors, oppose the flow of current in a manner that depends on the applied voltage. We can still model their behavior using the concept of resistance, but we don’t get a constant reading. In an
earlier article
, I provided a V-I curve for a small diode; if we take these measurements and calculate the effective R by rearranging the earlier equation (
I = V / R
⇒
R = V / I
), we obtain the log-scale V-to-R plot shown on the right:
Apparent resistance of a small diode (1N4148), log vertical scale.
For a chosen point of the
V-I
curve, we can also calculate so-called
differential resistance
. This parameter doesn’t tell us anything about the overall relationship between voltage and current; instead, it models the relative response to small deviations from the chosen baseline. For example, in the vicinity of 1.2 V on the plot above, the slope of the V-I curve is such that a change of Δ
v
= +/- 10 mV causes the current to change by Δ
i =
+/- 20 mA. If we divide Δ
v
by Δ
i
and squint our eyes hard enough, we can say that the “local” resistance is 500 mΩ. Again, that number has nothing to do with the bulk resistance of the diode at 1.2 V, but it’s a useful abstraction for modeling what happens to small signals that are piggybacking on top of a constant bias voltage.
In physical terms, resistance is associated with the consumption of energy. We’re making an effort to push charges through; some of the energy is absorbed by the medium and then taken out of the picture — turned into heat, light, motion, or captured in chemical bonds.
To model these dynamics, we need to tap into the official definition of voltage. It’s the amount of energy (E, in joules) we’re willing to expend to move the unit of electrical charge (Q, in coulombs, equal to about 6.2 quintillion electrons):
We also need the definition of current; as noted earlier, it’s the amount of charge that’s moved per second through a point in the circuit:
We can rearrange the second equation to solve for Q (
Q = I · t
), and then shuffle the first one to solve for E (
E = V · Q
). Combining these forms, we get
E = V · I · t
.
Finally, we tap into the physical definition of power (P, watts); it’s the rate at which energy is expended:
If we plug the earlier
E = V · I · t
formula into the fundamental power equation, we obtain:
\(P = \frac{V \cdot I \cdot \cancel{t} }{\cancel{t}} = V \cdot I\)
That’s to say, the amount of electrical power consumed by an electronic circuit depends on the supplied voltage, the resulting current, and nothing else. For resistive circuits, we can further substitute
I = V / R
and get:
\(P = V \cdot \frac{V}{R} = \frac{V^2}{R}\)
So, a resistive element consumes energy provided by the power supply at a rate that’s proportional to the square of the applied voltage, and inversely proportional to the component’s resistance. For example, a 220 Ω resistor subjected 10 V will dissipate about 455 mW as heat.
This brings us to an interesting question: what would it mean for a component to have a resistance of less than 0 ohms?
Well, we can start by stating the obvious: if R is negative and
I = V / R
, then the current-to-voltage plot will have a downward slope. For example, for R = -5 Ω, we’d get the following:
A plot of constant negative resistance.
It would appear that if we apply a positive voltage to a “negistor”, we should get a current that’s proportional to the voltage but with an opposite sign. The natural flow of conventional current is from the more positive side to the more negative one, but in this instance, it must be flowing the other way round.
Alas, a negistor can’t exist unless it’s equipped with an external power source. Recall our derivation of the power dissipation formula:
P = V
2
/
R
. In this equation, if
R
is negative, so is the consumed power. This implies that the component would need to extract energy from its surroundings and put it back into the circuit.
On the other hand, if we allow an external power supply, a circuit with constant negative resistance can be constructed pretty easily:
Negative resistance converter.
If you’re rusty on operational amplifiers, now would be the time to
revisit an earlier feature
on this blog. Otherwise, the analysis can be simplified by assuming that R
1
is large enough so that both the op-amp output pin and the signal source can supply worst-case currents via this path without causing their voltages to sag.
This assumption allows us to ignore R
1
for the initial part of the analysis: on a voltage basis, the circuit is just a textbook non-inverting amplifier with the gain determined by the bottom 22 kΩ / 22 kΩ voltage divider. You can find the derivation of the circuit’s gain in the linked article, but the bottom line is that if the resistors in the divider are the same, then the amplifier’s gain is 2×, so
V
out
≈ 2 ·
V
signal
.
We can now come back to R
1
: the left terminal of the resistor is connected to
V
signal
while the right terminal sits at
V
out
≈ 2 ·
V
signal
. From this, we can apply the fundamental
I = V / R
formula to calculate the current flowing through the component:
\(I_{R1} = \frac{V_{signal} - V_{out}}{R_1} = \frac{V_{signal} - 2 \cdot V_{signal}}{R_1} = \frac{-V_{signal}}{R_1}\)
This current must be flowing into or out of the signal source because there’s nowhere else for it to go: the input of the op-amp has a very high impedance.
The placement of the minus sign is inconsequential, we can also rewrite the equation as:
\(I_{in} = I_{R1} = \frac{V_{signal}}{ -R_1}\)
In other words, the circuit behaves the same as a negative resistance -R
1
placed between
V
signal
and the ground. We can confirm this on the following empirical V-I plot, captured for R
1
= 220 Ω and an op-amp supply of 5 V:
Circuit behavior. Dashed line is the ideal behavior of -220 Ω.
The circuit does nothing at
V
signal
= 0 V, but as the voltage increases, it backfeeds more and more current into the signal source.
The plot also exposes a shortcoming of this design: because the process depends on keeping the output pin of the op-amp at twice the input voltage, we eventually run out of range; in a 5 V circuit, this happens a bit shy of 2.5 V. Past that point, the op-amp is maxed out and the voltage across the terminals of R
1
begins to decrease; so must the reverse current, eventually reaching zero at 5 V.
A potential workaround is to change the voltage divider to achieve lower voltage gain and then use a proportionately smaller R to get the same reverse current; for example, if we dial in 1.1× gain with a 2.2 kΩ / 22 kΩ divider and then use R
1
= 22 Ω, we’ll still get a simulated resistance of -220 Ω, but this time, the circuit works to about 4 V:
Negative resistance circuit for R = 22
Ω
and 1.1× gain.
The price we pay for this trick is slightly worse linearity.
The arrangement discussed earlier has some niche uses, but most of the time, “negative resistance” is a reference to a somewhat different phenomenon: a V-I curve that looks normal in parts, but has a section with a downward slope.
The simplest example of this phenomenon is a situation where, past a certain point, an increase in voltage causes a relative constriction of the admitted current. A model of this behavior is shown on the left:
A simple model of differential negative resistance.
This inverted section is called
negative differential resistance
(NDR). At first blush, the term makes no sense: if you look at the plot of voltage to apparent resistance (right), the value stays positive (and in fact, goes up). To make sense of the terminology, recall the idea of calculating differential resistance as the “local” ratio of step change in voltage to step change in current:
r =
Δ
v
/ Δ
i
. In the downward portion of the V-I curve, Δ
v >
0 while Δ
i <
0, so the differential value is negative. But really, a simpler mnemonic is just that it’s an inverted slope.
In this scenario, because “real” resistance remains positive, such V-I kinks can manifest without the need for an additional power supply. An easily-constructed example of a negative differential resistance is the following arrangement of two complementary JFETs:
Negative differential resistance with JFETs.
This circuit, known as the lambda diode, should be fairly easy to understand if you’re familiar with the behavior of junction field-effect transistors; if not, a quick refresher can be found
here
. In a nutshell, the JFET drain-source path is conductive by default, but the flow of current can be constricted by making the gate-source voltage difference (
V
GS
) sufficiently negative in n-channel devices, or sufficiently positive in p-channel ones. In this circuit, the cut-off point is around
V
GS
= -4 to -5 V for the n-channel transistor (J111) and
V
GS
= +4 to +5 V for its p-channel counterpart (J175).
To simplify the analysis, let’s assume that the transistors have identical characteristics except for the polarity of the gate voltage; that is, let’s say that the top one conducts exactly as well at
V
GS
= -2 V as the bottom one conducts at
V
GS
= +2 V. That assumption is not quite true, but it’s good enough for a qualitative result.
Next, let’s use
V
mid
to denote the unknown voltage at the midpoint of the circuit (as marked in the schematic) and note that the gate of the n-channel transistor is wired to the ground. With this in mind, we can express the gate-source voltage delta for the top JFET as:
\(V_{GS \text{ (top)}} = \underbrace{\vphantom{0_m}0 \text{ V}}_{\text{gate}} - \underbrace{V_{mid}}_{\text{source}} = -V_{mid}\)
The bottom transistor has its gate hardwired to the positive supply, so the corresponding formula is:
\(V_{GS \text{ (bottom)}} = \underbrace{V_{signal}}_{\text{gate}} - \underbrace{V_{mid}}_{\text{source}}\)
The transistors are connected in series, so the same current must be flowing through both. This current is decided chiefly by
V
GS
, and we’ve made the assumption that both JFETs have the same characteristics except for the flipped sign for the gate voltage. So, equal currents would call for
V
GS (bottom)
= -
V
GS (top)
, which further expands to:
\(\begin{array}{c}
V_{signal} - V_{mid} = V_{mid} \\
V_{mid} = V_{signal} / 2
\end{array}\)
This puts the transistors’
V
GS
at half the input voltage, priming both to cut off once the input voltage crosses about 8 V.
And indeed, we can see this on the following empirical plot:
Current through the J111-J175 lambda diode.
In our lambda diode, the admitted current decreases sharply in the region between 5 V and 9 V; the stretch between 7 to 8.5 V, which coincides with the dashed line representing a delta of about -2 mA per volt, is quite linear.
Another flavor of negative differential resistance can arise if we’re supplying a controlled current to some circuit, but past a certain point, by some mechanism, the voltage needed to sustain it takes a nosedive. A conceptual illustration of this effect can be found below:
Negative differential resistance via horizontal snapback.
In this plot, the circuit behaves like a 6 Ω resistance up to a point, but then “snap backs” in the horizontal axis; currents above about 1.2 A can be apparently sustained with a markedly lower applied voltage.
This scenario is qualitatively different from what we’ve talked about before; in the earlier V-I plot, there were multiple voltages that could produce the same current. In the snapback scenario, we have multiple currents that can be sustained by the same voltage.
As it turns out, you can get that behavior out of a single bipolar transistor; we talked about an example of a circuit that exploited that pattern in an earlier article on this blog:
Error code 400: daily token limit exceeded. Higher limits are available to Skippy Premium and Premium+ subscribers.
Other articles you might like:
