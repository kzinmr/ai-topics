---
title: "Cursed circuits #4: PLL frequency multiplier"
url: "https://lcamtuf.substack.com/p/cursed-circuits-4-pll-frequency-multiplier"
fetched_at: 2026-04-29T07:02:08.704978+00:00
source: "lcamtuf.substack.com"
tags: [blog, raw]
---

# Cursed circuits #4: PLL frequency multiplier

Source: https://lcamtuf.substack.com/p/cursed-circuits-4-pll-frequency-multiplier

Welcome to another installment of
Cursed Circuits.
My goal for the series is to highlight a small collection of common yet mind-bending circuits that must’ve taken a stroke of genius to invent, but that are usually presented on the internet without explaining how or why they work.
In today’s episode, let’s have a look at a phase-locked loop clock multiplier: a circuit that, among other things, can take a 20 MHz timing signal produced by a quartz crystal and turn it into a perfectly-synchronized computer clock that’s running at 500 MHz, 3 GHz, or any other frequency of your choice.
To understand the PLL frequency multiplier, it’s probably good to cover latches first. A latch is a fundamental data-storage circuit capable of holding a single bit. The simplest variant is the set-reset (S-R) latch, which can be constructed from basic logic gates in a couple of ways. Perhaps the most intuitive layout is the following three-gate approach:
To analyze the circuit, let’s assume that the “set” signal (S) is high and the “reset” signal (R) is low. In this case, the output of the OR gate is a logical one regardless of the looped-back signal present on the gate’s other terminal; this produces a logical one on the first input of the downstream AND gate. The other input of that AND gate is also equal to one, because it’s just an inverted copy of R = 0. All in all, in the S = 1 and R = 0 scenario, both inputs of the AND gate are high; therefore, so is the signal on the circuit’s output leg (Q).
Next, let’s imagine that S transitions to a logical zero. This puts one of the OR inputs at zero volts, but the other is still high because it’s the looped-back output signal Q. The circuit is latched: it keeps outputting the same voltage as before, even though the original driving signal is gone.
The only thing that can break the cycle if the “reset” line is pulled high. This causes one of the AND input to go low, thus forcing the output signal to zero and breaking the loop that kept the OR gate latched. From now on, the output remains low even if R returns to zero volts.
This two-lever latch can be fashioned into a more practical data (D) latch, which stores an arbitrary input bit supplied on the data line whenever the enable signal (E) is high, and keeps it when E is low:
A conceptual illustration of a D latch.
In this circuit, a pair of input-side AND gates ensures that when E is at zero volts, the underlying S and R lines remain low regardless of the value presented on the data line. Conversely, if enable is high, the gates pass through a logical one either to the S line (if D is high) or the R line (if D is low).
Going further down that path, we can turn a D latch into a clocked D flip-flop, which stores a bit of data on the rising edge of the clock signal:
In this circuit, the latch on the left passes through the input data when the clock signal is low, or keeps the previous value if the clock is high. The latch on the right works the opposite way: it passes through the output from the first latch if the clock is high or holds the last value otherwise.
In effect, the value on the input line appears to propagate to the circuit’s output only during the 0 → 1 transition (rising edge) of the clock signal. More to the point, the propagation happens in two stages and there is never a direct signal path between D and Q, which prevents the cell from misbehaving if Q is looped back onto D.
Once we have a clocked D flip-flop — and make a trivial modification to furnish it with an additional reset input — we can build a digital phase error detector circuit. One type of such a detector is shown below:
A simple phase error detector.
The purpose of the detector is to compare clock signal B to a reference clock provided on input A. If the positive edge on input A arrives before a positive edge on input B, the output of the upper flip-flop (
Q
A
) goes high before the output of the bottom flip-flop (
Q
B
); this signals that clock B is running too slow. Conversely, if the edge on B arrives before the edge on A, the circuit generates a complementary output indicating that B is running too fast. As soon as both flip-flops are latched high — i.e., after encountering a positive edge on whichever of the two clock signals is running slower — the circuit is reset.
The following plot shows the behavior of the circuit when the clock supplied on the B leg is running too slow (left) or too fast (right) in relation to the reference signal on leg A:
The basic behavior of the phase error detector circuit.
In effect, the detector generates longer pulses on the output labeled P if the analyzed clock signal is lagging behind the reference; and longer pulses on the other output (R) if the signal is rushing ahead.
It’s worth noting that the frequencies in the plot are not cherry-picked; although a rigorous mathematical analysis of phase detectors is fairly involved and they have transient failure modes, the following simulation shows that happens if the frequency B is changing continuously:
A continuously-variable-frequency variant of the simulation.
The detector can serve as the fundamental building block of a circuit known as a phase-locked loop. Despite the name, the main forte of phase-locked loops is that they can generate output frequencies that match an input signal of some sort, even if that signal is noisy or faint:
The basic architecture of a digital PLL.
The output stage of the PLL is a
voltage-controlled oscillator (VCO)
. We’ve briefly covered VCOs before: they generate an output waveform with a frequency proportional to the supplied input voltage.
The voltage for the VCO is selected by a simple switched capacitor section in the middle; the section has two digital inputs, marked “+” and “-”. Supplying a digital signal on the “+” input turns on a high-side transistor that gradually charges the output capacitor to a higher voltage, thus increasing the output frequency of the VCO. Supplying a signal on the “-” leg turns on a low-side transistor, slowly discharges the capacitor, and achieves the opposite effect.
The last part of the circuit is the now-familiar phase error detector; it compares the externally-supplied clock to the looped-back output from the VCO. The detector outputs long pulses on the P output if the VCO frequency is lower than the reference clock, or on the R output if the VCO is running too fast. In doing so, the circuit adjusts the capacitor voltage and nudges the VCO to match the frequency and phase of the input waveform.
So far, we have a circuit that synchronizes the VCO with an external clock; that has some uses in communications, but doesn’t seem all that interesting on its own. To take it to the next level, we need to add a small but ingenious tweak:
A PLL-based frequency multiplier.
In this new circuit, we incorporated a frequency divider in the feedback loop. A frequency divider is not a complicated concept; most simply, it can be a binary counter (e.g., 74HC393) that advances by one with every cycle of the input clock. For a three-bit counter, the outputs will be:
\(\begin{array}{| c | c | c | c | c |}
\hline
\textbf{Clock cycle #} & \boldsymbol{Q_2} & \boldsymbol{Q_1} & \boldsymbol{Q_0} \\
\hline
0 & 0 & 0 & 0 \\
1 & 0 & 0 & 1 \\
2 & 0 & 1 & 0 \\
3 & 0 & 1 & 1 \\
4 & 1 & 0 & 0 \\
5 & 1 & 0 & 1 \\
6 & 1 & 1 & 0 \\
7 & 1 & 1 & 1 \\
\hline
\end{array}\)
Note that the counter produces a square wave with half the clock frequency on the LSB output (
Q
0
); with one-fourth the frequency on the second output (Q
1
); and with one-eighth on the MSB leg (Q
2
).
If we choose
Q
0
for the divider, the phase error detector will be presented with a looped-back signal that’s equal to one half the running frequency of the VCO; it will then work to get the VCO frequency high enough so that the divided signal matches the reference clock. This will cause the VCO to run exactly twice as fast — and yet, precisely in lockstep with the input clock.
If you liked the article, you’ll enjoy
The Secret Life of Circuits
. It’s a richly illustrated, lucid introduction to electronics — from the physics of conduction to embedded system programming. It features 290+ color diagrams, 420+ pages of original content, and zero AI.
👉 For further articles about electronics,
click here
. In particular, you might enjoy:
I write well-researched, original articles about geek culture, electronic circuit design, algorithms, and more. If you like the content, please subscribe.
