---
title: "Things you can do with diodes"
url: "https://lcamtuf.substack.com/p/things-you-can-do-with-diodes"
fetched_at: 2026-04-28T07:02:49.096194+00:00
source: "lcamtuf.substack.com"
tags: [blog, raw]
---

# Things you can do with diodes

Source: https://lcamtuf.substack.com/p/things-you-can-do-with-diodes

The diode might be the most neglected component in the electronics curriculum today. Pages upon pages have been written about the mechanics of resistors, capacitors, and inductors; on this blog alone, we covered the components’
fundamental equations
, the model of
complex impedance
, the behavior of
R-C filters
, and more. As for semiconductors, the diode’s more useful sibling — the transistor — hogs the limelight.
The diode is given neither the mathematical rigor of linear circuits nor the red-carpet treatment of the transistor. To the extent that the component is marveled at all, it’s usually in the context of exotic inventions such as the Gunn diode or the tunnel diode — both of which are almost never encountered in real life.
Today, let’s pay the “normal” diode a small tribute.
If you’re rusty on concepts such as voltage, current, or impedance, I suggest reviewing
this article
first.
In an earlier post about the
physics of semiconductors
, I noted that pure silicon is a poor conductor of electricity. This is because the material lacks long-lived, mobile charge carriers. Some conduction is still possible due to the short-lived thermal excitation of valence electrons that briefly pop into a higher-energy state, but these electrons can’t travel far before returning to a lower-energy level, so the effect is more or less negligible.
The conductivity of the material is improved by the addition of dopants. Some dopants contribute long-lived electrons that occupy higher energy levels with no lower-energy vacancies to return to; this is what’s called an n-type semiconductor. Other additives create easily-accessible valence band vacancies (“holes”); in such a p-type material, lower-energy electrons can slither around from atom to atom without needing to be knocked into a higher-energy state.
When an n-type material is brought into contact with a p-type semiconductor, higher-energy electrons from the n-side randomly diffuse to the p-side and then promptly fall into the abundant lower-energy holes. This produces a thermodynamic equilibrium with an internal electric field across the junction. There is a positive charge on the n-side and a negative charge on the p-side:
A simple illustration of a p-n junction.
The field pushes any mobile electrons that wander into the depletion region back to the n-side. The result is a thin, poorly conductive depletion region at the boundary.
The field of a p-n junction can be offset by an externally-applied voltage; if we make the p-side sufficiently more positive than the n-side, some current will flow. In the case of silicon, the junction becomes markedly conductive when the forward voltage reaches about 600 mV, although microamp-range currents will be flowing sooner than that.
A conventional diode is just a p-n junction. The component can be thought of as a rudimentary voltage-controlled gate: when the voltage is below a certain threshold, it presents itself as a very high resistance — typically in excess of 100 kΩ — so virtually no current can flow. When the threshold is cleared, the diode begins to admit more substantial currents. The V-I curve is initially exponential, but before long, the inherent resistance of the material begins to dominate. From that point on, the current has a roughly linear relationship with the “excess” applied voltage:
The plot of voltage to current for a forward-biased 1N4148 diode. By author.
My assertion that the V-I curve isn’t
really
exponential may be at odds with the conventional wisdom of EE textbooks, but the discrepancy is pretty clear to see in the plot that uses log scale for current (right). An exponential relationship between current and voltage would produce a straight line. In reality, the plot curls markedly past perhaps 10 mA.
So far, we discussed a condition known as
forward bias
. If the diode is reverse-biased — that is, if the p-side is more negative than the n-side — the component notionally remains nonconductive. Well… up to a point.
One of the possible reverse-bias scenarios is that if the reverse voltage becomes high enough, the electric field can accelerate the odd charge carrier in the depletion region to a point where the particle knocks other electrons into conduction band, producing an avalanche-like effect. The abundance of these kinetically-generated charge carriers makes the junction unexpectedly conductive again.
Most diodes are designed to keep this reverse breakdown voltage well outside the device’s intended operating range. A special category of components — known as
Zener diodes
— is engineered to exhibit reverse breakdown at lower, carefully calibrated voltages. Either way, once the threshold is exceeded, a reverse-biased diode starts conducting just fine:
1N4148 diode in reverse bias. By author.
Now that we have the basic theory laid out, we can have a look at some of the common uses of diodes.
About the simplest application of diodes is circuit protection. Let’s start with the arrangement shown on the left:
Several diode-based circuit protection schemes.
In the first circuit, a Zener-type diode is placed in reverse bias between a protected line and the ground. The diode remains non-conductive under normal operating conditions, but experiences electrical breakdown — and thus temporarily starts conducting — when the input voltage exceeds a safe limit. In effect, the diode acts as a crowbar that dissipates energy and protects more delicate components downstream. Diodes designed for this purpose are often marketed as
transient voltage suppressors
(TVS) and are particularly important for protecting semiconductors against static discharge. Another application is the suppression of voltage spikes that happen when we abruptly cut the current supplied to motors and other inductive loads.
A single diode can only be used to protect inputs where the input signal has a defined polarity – that is, where one rail is always more positive than the other. To provide overvoltage protection for AC signals with alternating polarity, we instead rely a two-diode arrangement shown on the right in the illustration above. This arrangement of components is also available in a single package known as a
bidirectional TVS
.
In the latter circuit, regardless of the polarity of the applied voltage, the “crowbar” path always consists of a forward-biased diode in series with a reverse-biased one. It follows that positive and negative conduction thresholds are the same: they’re equal to the diode’s reverse-bias breakdown voltage, plus roughly 600 mV.
Yet another protection technique is shown in the bottom panel. A regular forward-biased diode with a high reverse breakdown voltage is placed in series with the supply; this arrangement prevents damage to sensitive components if the polarity of the supply is accidentally reversed, for example if the batteries are inserted the wrong way. The trade-off is the inevitable voltage drop across the p-n junction, along with resistive heating if the current is high, so a transistor-based solution is typically preferred, especially in low-voltage circuits.
As mentioned earlier, most diodes are designed to withstand very high reverse-bias voltages, often in excess of -100 V; that said, a special category of products — Zener diodes — is designed to start conducting earlier than that.
When forward-biased, such a diode behaves the same as its conventional counterpart, becoming markedly conductive around 600 mV. When reverse-biased, it starts conducting at a higher voltage of manufacturer’s choice, with common options ranging from 1.8 V to 30 V.
The V-I plots shown earlier in the article tell us that once reverse breakdown begins, a small change in the applied voltage can produce a comparatively large swing in the current flowing through. We can also look at it another way: if the current through the diode is limited in some way, fluctuations in that current will have a comparatively minor effect on the voltage that develops across the diode’s terminals.
This observation lends itself to the use of diodes as voltage references. We take an unregulated power supply — for example, a battery — and in the simplest variant, use a resistor to roughly limit the current flowing through the diode. Depending on the voltage you want, you can use one or more forward-biased diodes, a reverse-biased Zener diode, or some combination thereof.
A simple diode-based voltage reference.
From Ohm’s law, the current admitted by the resistor will change linearly with the supply voltage (I = V/R), but these current fluctuations affect the diode voltage to a much lower extent. Here’s an experimental plot for the circuit constructed with a
1N4733
diode and a 100 Ω resistor:
The behavior of a voltage reference with a 1N4733 diode. By author.
The swing of the output voltage is under 5% of the fluctuations of the input signal: 45 mV versus 1 V. This figure might not sound particularly impressive, but the circuit can be cascaded: the output of one resistor-diode voltage reference can be used as the supply voltage for a second one. The effects stack up: 5% of 5% is equal to 0.25%.
A cascaded voltage reference.
Of course, the Zener voltage of the first diode should be higher than the second one. Further, for the cascaded layout to behave correctly, we need to make sure that the current siphoned off by the second stage is much lower than the current flowing through the intended resistor-diode path. One way to ensure this property is to choose R1 ≪ R2. Another solution is to separate the stages with a transistor circuit that mirrors the output voltage of stage 1 for use by stage 2; such voltage follower circuits are
discussed here
.
Nowadays, more complex transistor-based circuits with temperature compensation are favored for precision applications. Nevertheless, a Zener diode still offers a viable a solution in a pinch.
Let’s consider the circuit shown below:
This circuit is called a
half-wave rectifier.
The analysis is the easiest if we reference all circuit voltages to the bottom output leg marked as B, and then evaluate the positive half-cycle of the input AC waveform separately from the negative half-cycle:
A simplified analysis of the half-wave rectifier (w/o diode voltage drops).
During the positive half-cycle of a sine wave – when the upper terminal of the supply sits at a higher voltage – the diode is initially forward-biased. Assuming a low-impedance signal source, this allows the capacitor to charge to a voltage equal to the peak amplitude of the input signal, minus some diode voltage drop.
When the polarity of the signal is reversed – making the upper supply terminal more negative – the diode becomes reverse-biased and doesn’t conduct, so the capacitor holds charge. The following is a discrete-time simulation of the process; I added a modest resistive load across the output terminals to discharge the capacitor slightly in between each positive peak:
A simulation of a half-wave rectifier. By author.
If the load resistor is made a permanent part of the circuit and if it’s chosen so that the capacitor discharges quickly enough to keep up with the amplitude modulation of a carrier wave, we get a circuit known as the
envelope follower
. The circuit is a simple way to extract the approximate modulating waveform from the carrier signal in AM radio circuits:
A simulation of an envelope follower. By author.
The same principle can be used if we want to build a circuit that measures the approximate loudness of an audio signal, or more generally, hones in on the slow-changing component of any composite waveform.
The drawback of the half-wave rectifier is that the capacitor is only charged by the positive half-cycle of the sine wave; this is wasteful if the goal is to maximize the power delivered to a load. This deficiency can be addressed by constructing a
full-wave rectifier
, shown below:
Once again, the analysis of the circuit is the simplest if we consider output B to be the reference point:
Simplified analysis of the full-wave rectifier (w/o diode voltage drops).
During the positive half-cycle, diodes D1 and D2 are initially forward-biased; this allows the capacitor to charge to the AC peak voltage (minus the summed voltage drop of two diodes). During the negative half-cycle, diodes D3 and D4 become forward-biased, which connects the output B to the upper supply terminal. Meanwhile, the bottom supply terminal, which is currently at a higher voltage, is connected to point A. This allows the capacitor to continue charging in the same polarity as before.
A simulation of the process is shown below:
The behavior of a full-wave rectifier. By author.
The rectifier circuits outlined in the preceding section use diodes as voltage-controlled switches. Another application of the same principle is a circuit known as the
voltage doubler
.
There are many flavors of voltage doublers, but one particularly clean design is shown below. The circuit outputs a DC voltage that is equal to twice the peak amplitude of the zero-centered input waveform, minus the usual diode voltage drops. This in contrast to the rectifier circuits discussed earlier on, which only produce DC voltages in the vicinity of the peak amplitude:
Analysis of a voltage doubler (neglecting diode voltage drops).
This time, let’s use use the midpoint between the two capacitors as the reference point for voltage measurements. During the positive half-cycle of the AC signal (panel on the left), the upper diode (D1) can conduct to charge the top capacitor. This puts the output terminal A at a positive voltage in relation to the midpoint.
Next, let’s have a look at the negative half-cycle (right). In this scenario, the top diode is always reverse-biased, so it doesn’t conduct; C1 retains charge. At the same time, conduction is possible for the lower diode D2, which charges C2 so that the output terminal B ends up at a negative voltage in relation to the midpoint. In effect, we store the positive peak voltage of the input waveform in C1 and the negative maximum in C2. The total voltage between B and A is
V
peak
· 2 (once again, minus the expected diode voltage drops).
This method of multiplying voltages with switched capacitors lives on, although modern circuits typically use digitally-controlled transistors instead of diodes; this avoids voltage drops and eliminates the need for an AC voltage supply. If you’re interested in such circuits, I have a separate article
here
.
Most of the time, alternating waveforms that are centered around zero volts are inconvenient to work with; in particular, it’s more challenging to build circuits that run off a single voltage supply but that are able to discern, amplify, or generate signals that extend below the negative supply rail.
This brings us to a somewhat mind-bending alternative approach. The circuit is known as a
clamper –
or, less cryptically, as a
DC restorer
. It takes an AC waveform and shifts it so that the negative peaks are at roughly zero volts, with no appreciable impact on signal amplitude:
An analysis of the clamper circuit (neglecting diode voltage drops).
For now, let’s ignore the optional resistor. We start with the first positive half-cycle of the input sine wave (top left). Initially, the capacitor is not charged (
V
cap
= 0 V); further, there’s no current path via the diode, so charging is not possible. To elaborate: for energy to be stored in a capacitor, there must be a symmetry in the motion of charges flowing onto and off the plates. This way, the resulting electrostatic fields – increasingly positive on one plate and increasingly negative on another – largely cancel out, allowing a non-trivial charge to be moved with the help of a modest voltage.
If one of the capacitor’s is left floating, the device can’t be charged or discharged; instead, its previous charge state persists as a voltage across its terminals. If we take a capacitor charged to 1 V and connect one of its legs to a 10 V supply, the other leg will read 11 V in reference to the ground. If we connect it to a -5 V supply, we’ll get a reading of -4 V. It’s no different from putting a battery in series with another voltage source. In our circuit, the initial
V
cap
= 0 V, so in the positive half-cycle, the capacitor adds nothing, and the voltage on the output leg A simply follows the input waveform.
In the following negative half-cycle, once the voltage at point A reaches about -600 mV, the diode starts to conduct (top right). This clamps the voltage at point A while simultaneously allowing the capacitor to charge so that its left terminal becomes negative in relation to the right terminal. If we measure
V
cap
left to right, the resulting voltage is positive and is equal to the peak amplitude of the supply signal (minus the diode voltage drop).
In the subsequent positive cycle, the diode becomes reverse-biased again, so the capacitor must hold its previous charge; this means that
V
cap
remains unchanged and that the voltage at point A is necessarily offset from the input waveform by that amount. If the input waveform runs -
V
peak
to +
V
peak
, the output will be now moving from roughly -600 mV to
V
peak
· 2 – 600 mV.
The role of the optional load resistor is that it controls the circuit’s ability to respond to gradual shifts in signal amplitude. Without it, the circuit would theoretically be stuck forever at a voltage offset dictated by the largest encountered single-cycle swing in the input waveform. With a resistor, the capacitor can discharge over time, so the offset can change if the envelope of the waveform changes in some way.
In practice, the diode’s leakage current and the capacitor’s self-discharge rate are typically enough to make the circuit behave reasonably even without an output resistance. If you wish to play around with this layout, I recommend using a 10-100 µF capacitor and either skipping the resistor or using a large one (1 MΩ).
An OR gate is a circuit with two or more inputs that produces a positive voltage when any of the inputs is positive. An AND gate, in contrast, outputs a positive signal only if
all
the inputs are positive. Many readers are probably familiar with the application of this concept in computing, but more simply: a practical application of an OR gate might be a circuit that raises alarm if any of the door or window sensors are triggered. An application of an AND gate might be a system that illuminates a “PARKING FULL” sign when all the spots are occupied.
There are simple ways to implement this logic with diodes:
Logic pseudo-gates constructed with diodes.
In the case of an OR circuit (left), if the positive supply rail is connected to any of the input terminals, this forward-biases the corresponding diode and causes a current to flow through a resistor. Because the impedance of a forward-biased diode is much lower than that of a 10 kΩ resistor, the output voltage shoots up very close to the upper supply rail.
The AND circuit (right) essentially works in reverse: if any of the inputs is connected to the ground, this pulls the output voltage close to 0 V, so the output is positive only if both inputs are high (or are left floating).
The reason I put “gate” in scare quotes in the illustration is that the circuits are not readily composable to implement more complex digital logic; each of the gates requires current to flow through the input terminals, but it can’t necessarily deliver such currents on its output leg. A particularly troublesome situation is shown below:
Trying to cascade diode-based gates.
With the input signals as indicated in the drawing, three out of four diodes are reverse-biased; the only current path is the series resistor-diode-resistor connection between the positive supply rail and the ground. The circuit is essentially a resistor-based voltage divider; instead of providing a binary output, it produces an ambiguous intermediate voltage.
In other words, the solution works for single-step logic; to build real computers, we’d need gates that can deliver output currents higher than what they demand as input of the gates upstream.
If you liked the article, you’ll enjoy
The Secret Life of Circuits
. It’s a richly illustrated, lucid introduction to electronics — from the physics of conduction to embedded system programming. It features 290+ color diagrams, 420+ pages of original content, and zero AI.
👉  For further articles about electronics,
click here
. In particular, you might enjoy:
I write well-researched, original articles about geek culture, electronic circuit design, algorithms, and more. If you like the content, please subscribe.
