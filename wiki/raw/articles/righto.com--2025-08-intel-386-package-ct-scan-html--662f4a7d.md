---
title: "A CT scanner reveals surprises inside the 386 processor's ceramic package"
url: "http://www.righto.com/2025/08/intel-386-package-ct-scan.html"
fetched_at: 2026-05-01T07:01:17.111101+00:00
source: "righto.com"
tags: [blog, raw]
---

# A CT scanner reveals surprises inside the 386 processor's ceramic package

Source: http://www.righto.com/2025/08/intel-386-package-ct-scan.html

Intel released the 386 processor in 1985, the first 32-bit chip in the x86 line.
This chip was packaged in a ceramic square with 132 gold-plated pins protruding from the underside, fitting into
a socket on the motherboard.
While this package may seem boring, a lot more is going on inside it than you might expect.
Lumafield
performed a 3-D CT scan of the chip for me, revealing six layers of complex
wiring hidden inside the ceramic package.
Moreover, the chip has nearly invisible metal wires connected to the
sides
of the package, the spikes below.
The scan also revealed that the 386 has two separate power and ground networks: one for I/O and one for the CPU's logic.
A CT scan of the 386 package. The ceramic package doesn't show up in this image, but it encloses the spiky wires.
The package, below, provides no hint of the complex wiring embedded inside the ceramic.
The silicon die is normally not visible, but I removed the square metal lid that covers it.
1
As a result, you can also see the two tiers of gold contacts that surround the silicon die.
The 386 package with the lid over the die removed.
Intel selected the 132-pin ceramic package to meet the requirements of a high pin count, good thermal characteristics,
and low-noise power to the die.
2
:
However, standard packages didn't provide sufficient power, so Intel designed a custom package with
"single-row double shelf bonding to two signal layers and four power and ground planes."
In other words, the die's bond wires are connected to the two shelves (or tiers) of pads surrounding the die.
Internally, the package is like a 6-layer printed-circuit board made from ceramic.
Package cross-section. Redrawn from "High Performance Technology, Circuits and Packaging for the 80386".
The photo below shows the two tiers of pads with tiny gold bond wires attached: I measured the bond wires at 35 µm in diameter, thinner than a typical human hair.
Some pads have up to five wires attached to support more current for the power and ground pads.
You can consider the package to be a hierarchical interface from the tiny circuits on the die to the
much larger features of the computer's motherboard.
Specifically, the die has a feature size of 1 µm,
while the metal wiring on top of the die has 6 µm spacing.
The chip's wiring connects to the chip's bond pads, which have 0.01" spacing (.25 mm).
The bond wires connect to the package's pads, which have 0.02" spacing (.5 mm); double the spacing because there are two tiers.
The package connects these pads to the pin grid with 0.1" spacing (2.54 mm).
Thus, the scale expands by about a factor of 2500 from the die's microscopic circuitry to the chip's pins.
`
Close-up of the bond wires.
The ceramic package is manufactured through a complicated process.
4
The process starts with flexible ceramic "green sheets", consisting of ceramic powder mixed with a binding agent.
After holes for vias are created in the sheet, tungsten paste is silk-screened onto the sheet to form the wiring.
The sheets are stacked, laminated under pressure, and then sintered at high temperature (1500ºC to 1600ºC)
to create the rigid ceramic.
The pins are brazed onto the bottom of the chip.
Next, the pins and the inner contacts for the die are electroplated with gold.
3
The die is mounted, gold bond wires are attached, and a metal cap is soldered over the die to encapsulate it.
Finally, the packaged chip is tested, the package is labeled, and the chip is ready to be sold.
The diagram below shows a close-up of a signal layer inside the package. 
The pins are connected to the package's shelf pads through metal traces, spectacularly colored in the CT scan.
(These traces are surprisingly wide and free-form; I expected narrower traces to reduce capacitance.)
Bond wires connect the shelf pads to the bond pads on the silicon die.
(The die image is added to the diagram; it is not part of the CT scan.)
The large red circles are vias from the pins. Some vias connect to this signal layer, while other vias pass through to
other layers.
The smaller red circles are connections to a power layer; because the shelf pads are only on the two signal layers,
the six power planes have connections to the signal layers for bonding.
Since bond wires are only connected on the signal layers, the power layers need connections to pads on the signal
layers.
A close-up of a signal layer. The die image is pasted in.
The diagram below shows the corresponding portion of a power layer.
A power layer looks completely different from a signal layer; it is a single conductive plane with holes.
The grid of smaller holes allows the ceramic above and below this layer to bond, forming a solid piece of ceramic.
The larger holes surround pin vias (red dots), allowing pin connections to pass through to a different layer.
The red dots that contact the sheet are where power pins connect to this layer.
Because the only connections to the die are from the signal layers, the power layers have connections to the
signal layers; these are the smaller dots near the bond wires, either power vias passing through or vias connected
to this layer.
A close-up of a power layer, specifically I/O Vss. The wavy blue regions are artifacts from neighboring layers. The die image is pasted in.
With the JavaScript tool below, you can look at the package, layer by layer. Click on a radio button to select a layer.
By observing the path of a pin through the layers, you can see where it ends up. For instance, the upper left
pin passes through multiple layers until the upper signals layer connects it to the die. The pin to its right
passes through all the layers until it reaches the logic Vcc plane on top.
(Vcc is the 5-volt supply that powers the chip, called Vcc for historical reasons.)
Pins
I/O Vcc
Signals
I/O gnd
Signals
Logic gnd
Logic Vcc
If you select the logic Vcc plane above, you'll see a bright blotchy square in the center.
This is not the die itself, I think, but the adhesive that attaches the die to the package, epoxy filled with
silver to provide thermal and electrical conductivity. Since silver blocks X-rays, it is highly visible in the image.
Side contacts for electroplating
What surprised me most about the scans was seeing wires that stick out to the sides of the package.
These wires are used during manufacturing when the pins are electroplated with gold.
5
In order to electroplate the pins, each pin must be connected to a negative voltage so it can function as a cathode.
This is accomplished by giving each pin a separate wire that goes to the edge of the package.
This diagram below compares the CT scan (above) to a visual side view of the package (below).
The wires are almost invisible, but can be seen as darker spots.
The arrows show how three of these spots match with the CT scan; you can match up the other spots.
6
A close-up of the side of the package compared to the CT scan, showing the edge contacts. I lightly sanded the edge of the package to make the contacts more visible. Even so, they are almost invisible.
Two power networks
According to the datasheet, the 386 has 20 pins connected to +5V power (Vcc) and 21 pins connected to ground (Vss).
Studying the die, I noticed that the I/O circuitry in the 386 has separate power and ground connections from the
logic circuitry.
The motivation is that the output pins require high-current driver circuits.
When a pin switches from 0 to 1 or vice versa, this can cause a spike on the power and ground wiring.
If this spike is too large, it can interfere with the processor's logic, causing malfunctions.
The solution is to use separate power wiring inside the chip for the I/O circuitry and for the logic circuitry,
connected to separate pins.
On the motherboard, these pins are all connected to the same power and ground, but decoupling capacitors absorb
the I/O spikes before they can flow into the chip's logic.
The diagram below shows how the two power and ground networks look on the die, with separate pads and wiring.
The square bond pads are at the top, with dark bond wires attached.
The white lines are the two layers of metal wiring, and the darker regions are circuitry.
Each I/O pin has a driver circuit below it, consisting of relatively large transistors to pull the pin high or low.
This circuitry is powered by the horizontal lines for
I/O Vcc (light red) and I/O ground (Vss, light blue).
Underneath each I/O driver is a small logic circuit, powered by thinner
Vcc (dark red) and Vss (dark blue).
Thicker Vss and Vcc wiring goes to the logic in the rest of the chip.
Thus, if the I/O circuitry causes power fluctuations, the logic circuit remains undisturbed, protected by
its separate power wiring.
A close-up of the top of the die, showing the power wiring and the circuitry for seven data pins.
The datasheet doesn't mention the separate I/O and logic power networks, but
by using the CT scans, I determined which pins power I/O, and which pins power logic.
In the diagram below, the light red and blue pins are power and ground for I/O, while the dark red and blue pins are
power and ground for logic.
The pins are scattered across the package, allowing power to be supplied to all four sides of the die.
"No Connect" pins
As the diagram above shows, the 386 has eight pins labeled "NC" (No Connect)—when the chip is installed in a computer,
the motherboard must leave these pins unconnected.
You might think that the 132-pin package simply has eight extra, unneeded pins, but it's more complicated than that.
The photo below shows five bond pads at the bottom of the 386 die. Three of these pads have bond wires attached,
but two have no bond wires: these correspond to No Connect pins.
Note the black marks in the middle of the pads: the marks are from test probes that were applied to the die
during testing.
7
The No Connect pads presumably have a function during this testing process, providing access to an important
internal signal.
A close-up of the die showing three bond pads with bond wires and two bond pads without bond wires.
Seven of the eight No Connect pads are
almost
connected: the package has a spot for a bond wire in the die cavity
and the package has internal wiring to a No Connect pin.
The only thing missing is the bond wire between the pad and the die cavity.
Thus, by adding bond wires, Intel could easily create special chips with these pins connected, perhaps for debugging
the test process itself.
The surprising thing is that one of the No Connect pads
does
have the bond wire in place, completing the connection to
the external pin.
(I marked this pin in green in the pinout diagram earlier.)
From the circuitry on the die, this pin appears to be an output.
If someone with a 386 chip hooks this pin to an oscilloscope, maybe they will see something interesting.
Labeling the pads on the die
The earlier 8086 processor, for example, is packaged in a DIP (Dual-Inline Package) with two rows of pins.
This makes it 
straightforward to figure out which pin (and thus which function) is connected
to each pad on the die.
However, since the 386 has a two-dimensional grid of pins, the mapping to the pads is unclear.
You can guess that pins are connected to a nearby pad, but ambiguity remains.
Without knowing the function of each pad, I have a harder time reverse-engineering the die.
In fact, my primary motivation for scanning the 386 package was to determine the pin-to-pad mapping and thus the
function of each pad.
8
Once I had the CT data, I was able to trace out each hidden connection between the pad and the external pin.
The image below shows some of the labels; click
here
for the full, completely labeled image.
As far as I know, this information hasn't been available outside Intel until now.
A close-up of the 386 die showing the labels for some of the pins.
Conclusions
Intel's early processors were hampered by inferior packages, but by the time of the 386, Intel had realized
the importance of packaging.
In Intel's early days, management held the bizarre belief that chips should never have more than 16 pins, even though
other companies used 40-pin packages.
Thus, Intel's first microprocessor, the 4004 (1971), was crammed into a 16-pin package, limiting its performance.
By 1972, larger memory chips forced Intel to move to 18-pin packages, extremely reluctantly.
9
The eight-bit 8008 processor (1972) took advantage of this slightly larger package, but performance still suffered because
signals were forced to share pins.
Finally, Intel moved to the standard 40-pin package for the 8080 processor (1974),
contributing to the chip's success.
In the 1980s,
pin-grid arrays
became popular in the industry
as chips required more and more pins.
Intel used a ceramic pin grid array (PGA) with 68 pins for the 186 and 286 processors (1982),
followed by the 132-pin package for the 386 (1985).
The main drawback of the ceramic package was its cost.
According to the
386 oral history
,
the cost of the 386 die decreased over time to the point where the chip's package cost as much as the die.
To counteract this, Intel introduced a low-cost plastic package for the 386 that cost just a dollar to manufacture,
the Plastic Quad Flat Package (PQFP) (
details
).
In later Intel processors, the number of connections exponentially increased.
A typical modern laptop processor uses a Ball Grid Array with 2049 solder balls;
the chip is soldered directly onto the circuit board.
Other Intel processors use a Land Grid Array (LGA): the chip has flat contacts called
lands, while the
socket
has the pins.
Some Xeon processors have
7529
contacts, a remarkable growth from the 16 pins of
the Intel 4004.
From the outside, the 386's package looks like a plain chunk of ceramic.
But the CT scan revealed surprising complexity inside, from numerous contacts for electroplating to six layers of
wiring. Perhaps even more secrets lurk in the packages of modern processors.
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
Thanks to Jon Bruner and
Lumafield
for scanning the chip.
Lumafield's interactive CT scan of the 386 package is available
here
if you to want to examine it yourself.
Lumafield also scanned a
1960s cordwood flip-flop
and
the Soviet
Globus
spacecraft navigation
instrument for us.
Thanks to John McMaster for taking 2D X-rays.
Notes and references
