---
title: "Reverse engineering the mysterious Up-Data Link Test Set from Apollo"
url: "http://www.righto.com/2025/07/reverse-engineering-mysterious-up-data.html"
fetched_at: 2026-04-28T07:01:55.357033+00:00
source: "righto.com"
tags: [blog, raw]
---

# Reverse engineering the mysterious Up-Data Link Test Set from Apollo

Source: http://www.righto.com/2025/07/reverse-engineering-mysterious-up-data.html

Back in 2021, a collector friend of ours was visiting a dusty warehouse in search of Apollo-era communications equipment.
A box with NASA-style lights caught his eye—the "AGC Confirm" light suggested a connection
with the Apollo Guidance Computer.
Disappointingly, the box was just an empty chassis and the circuit boards were all missing.
He continued to poke around the warehouse when, to his surprise, he found a bag on the other side of the warehouse
that contained the missing boards!
After reuniting the box with its wayward circuit cards, he brought it to us:
could we make this undocumented unit work?
The Up-Data Link Confidence Test Set, powered up.
A label on the back indicated that it is an "Up-Data Link Confidence Test Set", built by Motorola.
As the name suggests, the box was designed to test Apollo's Up-Data Link (UDL), a system that allowed digital commands to be sent up to the spacecraft.
As I'll explain in detail below, these commands allowed ground stations to switch spacecraft circuits on or off, interact with the Apollo Guidance Computer, or set the spacecraft's clock.
The Up-Data Link needed to be tested on the ground to ensure that its functions operated correctly.
Generating the test signals for the Up-Data Link and verifying its outputs was the responsibility of the Up-Data Link Confidence Test Set (which I'll call the Test Set for short)
The Test Set illustrates how, before integrated circuits, complicated devices could be constructed from
thumb-sized encapsulated modules.
Since I couldn't uncover any documentation on these modules, I had to reverse-engineer them,
discovering that different modules implemented everything from flip-flops and logic gates to opto-isolators and analog circuits.
With the help of a Lumafield 3-dimensional X-ray scanner,
we looked inside the modules and examined the discrete transistors, resistors, diodes, and other components mounted inside.
Four of the 13-pin Motorola modules. These implement logic gates (2/2G & 2/1G), lamp drivers (LD), more logic gates (2P/3G), and a flip-flop (LP FF). The modules have 13 staggered pins, ensuring that they can't be plugged in backward.
Reverse-engineering this system—from the undocumented modules to the mess of wiring—was a challenge.
Mike found one NASA document that mentioned the Test Set, but the document was remarkably uninformative.
1
Moreover, key components of the box were missing, probably removed for salvage years ago.
In this article, I'll describe how we learned the system's functionality,
uncovered the secrets of the encapsulated modules,
built a system to automatically trace the wiring,
and used the UDL Test Set in a large-scale re-creation of the Apollo communications system.
The Apollo Up-Data Link
Before describing the Up-Data Link Test Set, I'll explain the Up-Data Link (UDL) itself.
The Up-Data Link provided a mechanism for the Apollo spacecraft to receive digital commands from ground stations.
These commands allowed ground stations to control the Apollo Guidance Computer, turn equipment on or off,
or update the spacecraft's clock.
Physically, the Up-Data Link is a light blue metal box with an irregular L shape, weighing almost 20 pounds.
The Up-Data Link box.
The Apollo Command Module was crammed with boxes of electronics, from communication and navigation to power and sequencing.
The Up-Data Link was mounted above the AC power inverters, below the Apollo Guidance Computer, and to the left of the waste management system and urine bags.
The lower equipment bay of the Apollo Command Module. The Up-Data Link is highlighted in yellow. Click this image (or any other) for a larger version. From
Command/Service Module Systems Handbook
p212.
Up-Data Link Messages
The Up-Data Link supported four types of messages:
Mission Control had direct access to the Apollo Guidance Computer (AGC) through the UDL,
controlling the computer, keypress by keypress.
That is, each message caused the UDL to simulate a keypress on the Display/Keyboard (DSKY), the astronaut's interface
to the computer.
The spacecraft had a clock, called
the Central Timing Equipment or CTE, that tracked the elapsed time of the mission, from days to seconds.
A CTE message could set the clock to a specified time.
A system called Real Time Control (RTC) allowed the UDL to turn relays on or off, so some spacecraft systems to be
controlled from the ground.
2
These 32 relays, mounted inside the Up-Data Link box, could do
everything from illuminating an Abort light—indicating that Mission Control says to abort—to controlling the data tape recorder or the S-band radio.
Finally, the UDL supported two test messages to "exercise all process, transfer and program control logic" in the UDL.
The diagram below shows the format of messages to the Up-Data Link.
Each message consisted of 12 to 30 bits, depending on the message type.
The first three bits, the Vehicle Address, selected which spacecraft should receive the message.
(This allowed messages to be directed to the Saturn V booster, the Command Module, or the Lunar Module.
3
)
Next, three System Address bits specified the spacecraft system to receive the message, corresponding to the four message types above.
The remaining bits supplied the message text.
Format of the messages to the Up-Data Link. From
Telecommunication Systems Study Guide
.
Note that the vehicle access code uses a different sub-bit pattern from the rest of the message.
This diagram shows an earlier sub-bit encoding, not the encoding used by the Test Set.
The contents of the message text depended on the message type.
A Real Time Control (RTC) message had a six-bit value specifying the relay number as well as whether it should be turned off or on.
An Apollo Guidance Computer (AGC) message had a five-bit value specifying a key on the Display/Keyboard (DSKY).
For reliability, the message was encoded in 16 bits: the message, the message inverted, the message again, and a padding bit; any mismatching bits would trigger an error.
A CTE message set the clock using four 6-bit values indicating seconds, minutes, hours, and
days.
The UDL processed the message by resetting the clock and then advancing the time by issuing the specified number of
pulses to the CTE to advance the seconds, minutes, hours, and days.
(This is similar to setting a digital alarm clock by advancing the digits one at a time.)
Finally, the two self test messages consisted of 24-bit patterns that would exercise the UDL's internal circuitry.
The results of the test were sent back to Earth via Apollo's telemetry system.
For reliability, each bit transmitted to the UDL was replaced by five "sub-bits":
each "1" bit was replaced with the sub-bit sequence "01011", and each "0" bit was replaced with the
complement, "10100".
4
The purpose of the sub-bits was that any corrupted data would result in
an invalid sub-bit code so corrupted messages could be rejected.
The Up-Data Link performed this validation by matching the input data stream against "01011" or "10100".
(The vehicle address at the start of a message used a different sub-bit code, ensuring
that the start of the message was properly identified.)
By modern standards, sub-bits are an inefficient way of providing redundancy, since the message becomes five times larger.
As a consequence, the effective transmission rate was low: 200 bits per second.
There was no security in the Up-Data Link messages, apart from the need for a large transmitter.
Of the systems on Apollo, only the rocket destruct system—euphemistically called the Propellant Dispersion System—was cryptographically secure.
5
Since the Apollo radio system was analog, the digital sub-bits couldn't be transmitted from ground to space directly.
Instead, a technique called phase-shift keying (PSK) converted the data into an audio signal.
This audio signal consists of a sine wave that is inverted to indicate a 0 bit versus a 1 bit;
in other words, its phase is shifted by 180 degrees for a 0 bit.
The Up-Data Link box takes this audio signal as input and demodulates it to extract the digital message data.
(Transmitting this audio signal from ground to the Up-Data Link required more steps that aren't relevant to the Test Set,
so I'll describe them in a footnote.
6
)
The Up-Data Link Test Set
Now that I've explained the Up-Data Link, I can describe the Test Set in more detail.
The purpose of the UDL Test Set is to test the Up-Data Link system.
It sends a message—as an audio signal—to the Up-Data Link box, implementing the message formatting, sub-bit encoding, and phase shift keying
described above.
Then it verifies the outputs from the UDL to ensure that the UDL performed the correct action.
Perhaps the most visible feature of the Test Set is the paper tape reader on the front panel: this reader
is how the Test Set obtains messages to transmit.
Messages are punched onto strips of paper tape, encoded as a sequence of 13 octal digits.
7
After a message is read from paper tape, it is shown on the 13-digit display.
The first three digits are an arbitrary message number, while the remaining 10 octal digits denote the 30-bit message to send to the UDL.
Based on the type of message, specified by the System Address digit,
the Test Set validates the UDL's response and indicates success or errors on the panel lights.
I created the block diagram below to explain the architecture and construction of the Test Set (click for a larger view).
The system has 25 circuit boards, labeled A1 through A25;
8
for the most part, they correspond to functional blocks in the diagram.
My block diagram of the Up-Data Link Test Set. (Click for a larger image.)
The Test Set's front panel is dominated by its display of 13 large digits.
It turns out that the storage of these digits is the heart of the Test Set.
This storage (A3-A9) assembles the digits as they are read from the paper tape, circulates the bits for transmission, and
provides digits to the other circuits to select the message type and validate the results.
To accomplish this, the 13 digit circuits are configured as a 39-bit shift register.
As the message is read from the paper tape, its bits are shifted into the digit storage, right to left, and the
message is shown on the display.
To send the message, the shift register is reconfigured so the 10 digits form a loop, excluding the message number.
As the bits cycle through the loop, the leftmost bit is encoded and transmitted.
At the end of the transmission, the digits have cycled back to their original positions, so the message can be
transmitted again if desired.
Thus, the shift-register mechanism both deserializes the message when it is read and serializes the message for transmission.
The Test Set uses three boards (A15, A2, and A1) to expand the message with sub-bits and to encode the message into audio.
The first board converts each bit into five sub-bits.
The second board applies phase-shift keying (PSK) modulation, and the third board has filters to produce clean sine waves from the digital signals.
On the input side, the Test Set receives signals from the Up-Data Link (UDL) box through round military-style connectors.
These input signals are buffered by boards A25, A22, A23, A10, and A24.
Board 15 verifies the input sub-bits by comparing them with the transmitted sub-bits.
For an AGC message, the computer signals are verified by board A14.
The timing (CTE) signals are verified by boards A20 and A21.
The UDL status (validity) signals are processed by board A12.
Board A11 implements a switching power supply to power the interface boards.
You can see from the block diagram that the Test Set is complex and implements multiple functions.
On the other hand, the block diagram also shows that it takes a lot of 1960s circuitry to implement anything.
For instance, one board can only handle two digits, so the digit display alone requires seven boards.
Another example is the inputs, requiring a full board for two or three input bits.
Encapsulated modules
The box is built from modules that are somewhat like integrated circuits but contain discrete components.
Modules like these were used in the early 1960s before ICs caught on.
Each module implements a simple function such as a flip-flop or buffer.
They were more convenient than individual components, since a module provided a ready-made function.
They were also compact, since the components were tightly packaged inside the module.
Physically, each module has 13 pins: a row of 7 on one side and a row of 6 offset on the other side.
This arrangement ensures that a module cannot be plugged in backward.
A Motorola "LP FF" module. This module implements a J-K flip-flop. "LP" could indicate low performance, low power, or low propagation; the system also uses "HP FF" modules, which could be high performance.
Reverse engineering these modules was difficult since they were encapsulated in plastic and the components were inaccessible.
The text printed on each module hinted at its function.
For example, the J-K flip-flop module above is labeled "LP FF".
The "2/2G & 2/1G" module turned out to contain two NAND gates and two inverters (the 2G and 1G gates).
A "2P/3G" module contains two pull-up resistors and two three-input NAND gates.
Other modules provided special-purpose analog functions for the PSK modulation.
I reverse-engineered the functions of the modules by applying signals and observing the results.
Conveniently, the pins are on 0.200" spacing so I could plug modules into a standard breadboard.
The functions of the logic modules were generally straightforward to determine.
The analog modules were more difficult; for instance, the "-3.9V" module contains a -3.9-volt Zener diode, 
six resistors, and three capacitors in complicated arrangements.
To determine how the modules are constructed internally, we had a module X-rayed by John McMaster and another module X-rayed in three dimensions by Lumafield.
The X-rays revealed that modules were built with "cordwood construction", a common technique in the 1960s.
That is, cylindrical components were mounted between two boards, stacked parallel similar to a pile of wood logs.
Instead of using printed-circuit boards, the leads of the components were welded to metal strips to provide the interconnections.
A 3-D scan of the module showing the circuitry inside the compact package, courtesy of Lumafield. Two transistors are visible near the center.
For more information on these modules, see my articles
Reverse-engineering a 1960s cordwood flip-flop module with X-ray CT scans
and
X-ray reverse-engineering a hybrid module
.
You can interact with the scan
here
.
The boards
In this section, I'll describe some of the circuit boards and point out their interesting features.
A typical board has up to 15 modules, arranged as five rows of three.
The modules are carefully spaced so that two boards can be meshed
with the components on one board fitting into the gaps on the other board.
Thus, a pair of boards forms a dense block.
This photo shows how the modules of the two circuit boards are arranged so the boards can be packed together tightly.
Each pair of boards is attached to side rails and a mounting bracket, forming a unit.
8
The bracket has ejectors to remove the board unit, since the backplane connectors grip the boards tightly.
Finally, each bracket is labeled with the board numbers, the test point numbers, and the Motorola logo.
The complexity of this mechanical assembly suggests that Motorola had developed an integrated prototyping system around the circuit modules, prior to the Test Set.
Digit driver boards
The photo below shows a typical board, the digit driver board.
At the left, a 47-pin plug provides the connection between the board and the Test Set's backplane.
At the right, 15 test connections allow the board to be probed and tested while it is installed.
The board itself is a two-sided printed circuit board with gold plating.
Boards are powered with +6V, -6V, and ground; the two red capacitors in the lower left filter the two voltages.
Boards A4 through A9 are identical digit driver boards.
The digit driver is the most common board in the system, appearing six times.
9
Each board stores two octal digits in a shift register and drives two digit displays on the front panel.
Since the digits are octal, each digit requires three bits of storage, implemented with
three flip-flop modules connected as a shift register.
If you look closely, you can spot the six flip-flop modules, labeled "LP FF".
The digits are displayed through an unusual technology: an edge-lit lightguide display.
10
From a distance, it resembles a Nixie tube, but it uses 10 lightbulbs, one for each number value, with a plastic layer for each digit.
Each plastic sheet has numerous dots etched in the shape of the corresponding number.
One sheet is illuminated from the edge, causing the dots in the sheet to light up and display that number.
In the photo below, you can see both the illuminated and the unilluminated dots.
The displays take 14 volts, but the box runs at 28 volts, so a board full of resistors on the front panel drops the voltage from 28 to 14, giving off noticeable heat in the process.
A close-up of a digit in the Test Set, showing the structure of the edge-lit lightguide display.
For each digit position, the driver board provides eight drive signals, one for each bulb.
The drivers are implemented in "LD" modules.
Since each LD module contains two drive transistors controlled by 4-input AND gates, a module supports two bulbs.
Thus, a driver board holds eight LD modules in total.
The LD modules are also used on other boards to drive the lights on the front panel.
Ring counters
The Test Set contains multiple counters to count bits, sub-bits, digits, states, and so forth.
While a modern design would use binary counters, the Test Set is implemented with a circuit called a
ring counter
that optimizes the hardware.
For instance, to count to ten, five flip-flops are arranged as a shift register so each flip-flop sends its output to the next one.
However, the last flip-flop sends its
inverted
output to the first.
The result is that the counter will proceed: 10000, 11000, 11100, 11110, 11111 as 1 bits are shifted in at the left.
But after a 1 reaches the last bit, 0 bits will be shifted in at the left: 01111, 00111, 00011, 00001, and finally 0000.
Thus, the counter moves through ten states.
Why not use a 4-bit binary counter and save a flip-flop? First, the binary counter requires additional logic to go from 9 back to 0.
Moreover, acting on a particular binary value requires a 4-input gate to check the four bits.
But a particular value of a ring counter can be detected with a smaller 2-input gate by checking the bits on either side of the 0/1 boundary.
For instance, to detect a count of 3 (11
10
0), only the two highlighted bits need to be tested.
Thus, the decoding logic is much simpler for a ring counter, which is important when each gate comes in an expensive module.
Another use of the ring counter is in the sub-state generator, counting out the five states.
Since this ring counter uses three flip-flops, you might expect it to count to six.
However, the first flip-flop gets one of its inputs from the second flip-flop, resulting in five states:
000, 100, 110, 011, and 001, with the 111 state skipped.
11
This illustrates the flexibility of ring counters to generate arbitrary numbers of states.
The PSK boards
Digital data could not be broadcast directly to the spacecraft, so the data was turned into an audio signal using phase-shift keying (PSK).
The Test Set uses two boards (A1 and A2) to produce this signal.
These boards are interesting and unusual because they are analog, unlike the other boards in the Test Set.
The idea behind phase-shift keying is to change the phase of a sine wave depending on the bit (i.e., sub-bit) value.
Specifically, a 2 kHz sine wave indicated a one bit, while the sine wave was inverted for a zero bit.
That is, a phase shift of 180º indicated a 0 bit.
But how do you tell which sine wave is original and which is flipped? The solution was to combine the information
signal with a 1 kHz reference signal that indicates the start and phase of each bit.
The diagram below shows how the bits 1-0-1 are encoded into the composite audio signal that
is decoded by the Up-Data Link box.
The phase-shift keying modulation process. This encoded digital data into an audio signal for transmission to the Up-DataLink. Note that "1 kc" is 1 kilocycle, or 1 kilohertz in modern usage. From
Apollo Digital Up-Data Link Description
.
The core of the PSK modulation circuit is a transformer with a split input winding.
The 2 kHz sine wave is applied to the winding's center tap.
One side of the winding is grounded (by the "ø DET" module) for a 0 bit, but the other side of the winding is grounded for a 1 bit.
This causes the signal to go through the winding in one direction for a 1 bit and the opposite direction for a 0 bit.
The transformer's output winding thus receives an inverted signal for a 0 bit, giving the 180º phase shift seen in the second waveform above.
Finally, the board produces the composite audio signal by mixing in the reference signal through a potentiometer and the "SUM" module.
12
Board A2 is the heart of the PSK encoding. The black transformer selects the phase shift, controlled by the "ø DET" and "ø DET D" modules in front of it. The two central potentiometers  balance the components of the output signal.
Inconveniently, 
some key components of the Test Set were missing; probably the most valuable components were salvaged when the box was scrapped.
The missing components included the power supplies and amplifiers on the back of the box, as well as parts from
PSK board A1.
This board had ten white wires that had been cut, going to missing components labeled MP1, R2, L1, and L2.
By studying the circuitry, I determined that MP1 had been a 4-kHz oscillator that provided the master clock for the Test Set.
R2 was simply a potentiometer to adjust signal levels.
Marc added circuitry to board A1 to replace the two missing filters and the missing oscillator. (The oscillator was used earlier to drive a clock from Soyuz.)
But L1 and L2 were more difficult.
It took a lot of reverse-engineering before we determined that L1 and L2 were 
resonant filters to convert the digital waveforms to the sine waves needed for the PSK output.
Marc used a combination of theory and trial-and-error to determine the inductor and capacitor values that produced a
clean signal.
The photo above shows our substitute filters, along with a replacement oscillator.
Input boards
The Test Set receives signals from the Up-Data Link box under test and verifies that these signals are correct.
The Test Set has five input boards (A22 through A25) to buffer the input signals and convert them to digital levels.
The input boards also provide electrical isolation between the input signals and the Test Set, avoiding problems caused by
ground loops or different voltage levels.
A typical input board is A22, which receives two input signals, supplied through coaxial cables.
The board buffers the signals with op-amps, and then produces a digital signal for use by the box.
The op-amp outputs go into "1 SS" isolation modules that pass the signal through to the box while ensuring isolation.
These modules are optocouplers, using an LED and a phototransistor to provide isolation.
13
The op-amps are powered by an isolated power supply.
Board A22 handles two input signals. It has two op-amps and associated circuitry. Note the empty module positions; board A23 has these positions populated so it supports three inputs.
Each op-amp module is a Burr-Brown Model 1506 module,
14
encapsulating a transistorized op-amp into a convenient 8-pin module.
The module is similar to an integrated-circuit op-amp, except it has discrete components inside and is considerably larger than an integrated circuit.
Burr-Brown is
said
to have created the first solid-state op-amp in 1957, and started making op-amp modules around 1962.
Board A24 is also an isolated input board, but uses different circuitry.
It has two modules that each contain four Schmitt triggers, circuits to sharpen up a noisy input.
These modules have the puzzling label "-12+6LC".
Each output goes through a "1 SS" isolation module, as with the previous input boards.
This board receives the 8-bit "validity" signal from the Up-Data Link.
The switching power supply board
Board A11 is interesting: instead of sealed modules, it has a large green cube with numerous wires attached.
This board turned out to be a switching power supply that implements six dual-voltage power supplies.
The green cube is a transformer with 14 center-tapped windings connected to 42 pins.
The transformer ensures that the power supply's outputs are isolated.
This allows the op-amps on the input boards to remain electrically isolated from the rest of the Test Set.
The switching power supply board is dominated by a large green transformer with many windings. The two black power transistors are at the front.
The power supply uses a design known as a
Royer Converter
; the two transistors drive the transformer in a push-pull configuration.
The transistors are turned on alternately at high frequency, driven by a feedback winding.
The transformer has multiple windings, one for each output.
Each center-tapped winding uses two diodes to produce a DC output, filtered by the large capacitors.
In total, the power supply has four ±7V outputs and two ±14V outputs to supply the input boards.
This switching power supply is independent from the power supplies for the rest of the Test Set.
On the back of the box, we could see where power supplies and amplifiers had been removed.
Determining the voltages of the missing power supplies would have been a challenge.
Fortunately, the front of the box had test points with labels for the various voltages: -6, +6, and +28, so we knew what voltages were required.
The front panel
The front panel reveals many of the features of the Test Set.
At the top, lights indicate the success or failure of various tests.
"Sub-bit agree/error" indicates if the sub-bits read back into the Test Set match the values sent.
"AGC confirm/error" shows the results of an Apollo Guidance Computer message, while "CTE confirm/error" shows the results of a Central Timing Equipment message.
"Verif confirm/error" indicates if the verification message from the UDL matches the expected value for a test message.
At the right, lights indicate the status of the UDL: standby, active, or powered off.
A close-up of the Test Set's front panel.
In the middle, toggle switches control the UDL operation.
The "Sub-bit spoil" switch causes sub-bits to be occasionally corrupted for testing purposes.
"Sub-bit compare/override" enables or disables sub-bit verification.
The four switches on the right control the paper tape reader.
The "Program start" switch is the important one: it causes the UDL to send one message (in "Single" mode) or multiple messages (in "Serial" mode).
The Test Set can stop or continue when an error occurs ("Stop on error" / "Bypass error").
Finally, "Tape advance" causes messages to be read from paper tape, while "Tape stop" causes the UDL to re-use the current message rather than loading a new one.
The UDL provides a verification code that indicates its status.
The "Verification Return" knob selects the source of this verification code:
the "Direct" position uses a 4-bit verification code, while
"Remote" uses an 8-bit verification code.
15
At the bottom, "PSK high/low" selects the output level for the PSK signal from the Test Set.
(Since the amplifier was removed from our Test Set, this switch has no effect.
Likewise, the "Power On / Off" switch has no effect since the power supplies were removed. We power the Test Set
with an external lab supply.)
In the middle, 15 test points allow access to various signals inside the Test Set.
The round elapsed time indicator shows how many hours the Test Set has been running (apparently over 12 months of continuous operation).
Reverse-engineering the backplane
Once I figured out the circuitry on each board, the next problem was determining how the boards were connected.
The backplane consists of rows of 47-pin sockets, one for each board.
Dense white wiring runs between the sockets as well as to switches, displays, and connectors.
I started beeping out the connections with a multimeter, picking a wire and then trying to find the other end.
Some wires were easy since I could see both ends, but many wires disappeared into a bundle.
I soon realized that manually tracing the wiring was impractically slow:
with 25 boards and 47 connections per board, brute-force testing of every pair of connections would require hundreds of thousands of checks.
The backplane wiring of the Test Set consisted of bundles of white wires, as shown in this view of the underside of the Test Set.
To automate the beeping-out of connections, I built a system that I call
Beep-o-matic
.
The idea behind
Beep-o-matic
is to automatically find all the connections between two motherboard slots by plugging
two special boards into the slots.
By energizing all the pins on the first board in sequence, a microcontroller can detect connected pins on the second board, revealing the wiring between the two slots.
This system worked better than I expected, rapidly generating a list of connections.
I still had to plug the Beep-o-matic boards into each pair of slots (about 300 combinations in total), but each scan took just a few seconds, so a full scan was practical.
To find the wiring to the switches and connectors, I used a variant of the process.
I plugged a board into a slot and used a program to continuously monitor the pins for changes.
I went through the various switch positions and applied signals to the connectors to find the associated connections.
Conclusions
I started reverse-engineering the Test Set out of curiosity: given an undocumented box made from mystery modules and
missing key components,
could we understand it? Could we at least get the paper tape reader to run and the lights to flash?
It was a tricky puzzle to figure out the modules and the circuitry, but eventually we could read a paper tape and
see the results on the display.
But the box turned out to be useful.
Marc has amassed a large and operational collection of Apollo communications hardware.
We use the UDL Test Set to generate realistic signals that we feed into Apollo's S-band communication system.
We haven't transmitted these signals to the Moon, but we have transmitted signals between antennas a few feet apart,
receiving them with a box called the S-band Transponder.
Moreover, we have used the Test Set to control an Up-Data Link box, a CTE clock, and a
simulated Apollo Guidance Computer, reading commands from the paper tape and sending them through the complete communication path.
Ironically, the one thing we haven't done with the Test Set is use it to test the Up-Data Link in the way it is intended: connecting the UDL's outputs to the Test Set and checking the panel lights.
From a wider perspective, the Test Set provides a glimpse of the vast scope of the Apollo program.
This complicated box was just one part of the test apparatus for one small part of Apollo's electronics.
Think of the many different electronic systems in the Apollo spacecraft, and consider the
enormous effort to test them all.
And electronics was just a small part of Apollo alongside the engines, mechanical structures, fuel cells, and life support systems. 
With all this complexity, it's not surprising that the Apollo program employed 400,000 people.
For more information, the footnotes include a list of UDL documentation
16
and
CuriousMarc
's videos
17
.
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
I worked on this project with CuriousMarc, Mike Stewart, and Eric Schlapfer.
Thanks to
John McMaster
for X-rays, thanks to
Lumafield
for the CT scans, and thanks to Marcel for providing the box.
VIDEO
Notes and references
