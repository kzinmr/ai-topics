---
title: "Powering up a module from the IBM 604: an electronic calculator from 1948"
url: "http://www.righto.com/2026/06/ibm-604-thyraton-tube-module.html"
fetched_at: 2026-06-08T07:01:15.457944+00:00
source: "righto.com"
tags: [blog, raw]
---

# Powering up a module from the IBM 604: an electronic calculator from 1948

Source: http://www.righto.com/2026/06/ibm-604-thyraton-tube-module.html

1948 was an interesting time for computing.
For decades, businesses had used punch card equipment that added and sorted electromechanically.
Now these electromechanical relays and counting wheels were being used to build room-filling general-purpose computers such as Harvard Mark I (1944)
and IBM's SSEC (1948).
But slow electromechanical mechanisms were already becoming obsolete.
World War II had fostered the development of electronics and vacuum tubes for radio, radar, and navigation.
Electronic technology was being used in massive electronic computers, such as Colossus (1943) and ENIAC (1946).
The first stored-program computer, the Manchester Baby, was built in 1948.
The IBM 604 Electronic Calculating Punch behind a Type 521 Card Reader/Punch. Photo from IBM.
Note the panels in the side of the 604 and in the front of the 521 to hold plugboards.
In the midst of these technological advances, IBM introduced the Electronic Calculating Punch, type 604.
1
This system may seem like a step backward:
it wasn't a computer, but a programmable calculator that performed a fixed set of operations.
2
However, it was much smaller
3
than a computer—about the size of a double refrigerator—and much cheaper:
renting for $550 a month, it was affordable by businesses and universities.
Since it used vacuum tubes, it was much more powerful than electromechanical equipment; it could do 60 operations in under a
second, including multiplication and division.
As a result, the IBM 604 became very popular, with over 5600 units produced.
Moreover, IBM's experience with electronics in the 604 led to the success of its vacuum-tube computers
in the 1950s.
One of the innovations of the 604 was the pluggable module, which combined a tube and its associated circuitry
as shown below.
The insulated handle was used to remove and install modules in the calculator.
The nine pins at the bottom of the module plugged into a socket in the 604, with the sockets connected with backplane wiring.
The tube was also socketed, so a bad tube could be quickly replaced. At the right, the resistors and capacitors are mounted
on insulating wafers in the module.
4
A thyratron tube module from the IBM 604 Electronic Calculating Punch.
The 604 used several different types of modules. This module has a thyratron tube, a special type of tube that acts as a high-current switch.
I put this module in a circuit and powered it up.
The video below shows the module controlling a light bulb.
The first button sends a small signal to the module (center), turning it on and illuminating the bulb.
As I'll explain below, a thyratron tube stays on until its power is cut off, which I did with the second button.
VIDEO
Pluggable modules may seem trivial, but they were an important innovation.
Previously, vacuum tube equipment was typically built from a metal chassis with tubes mounted on the top and the other
components, such as resistors and capacitors, mounted underneath.
IBM developed a different approach: pluggable modules, where each module held a vacuum tube
along with its associated components.
These
patented
modules were dense, since they packed components
in three dimensions.
Moreover, by using a small set of standardized modules, the modules could be mass-produced and the computers assembled
on a
production line
.
Maintenance and repair were simplified; modules could be swapped to find the bad module, which was replaced with
a spare.
These modules were so important that IBM featured them in ads for the 604.
IBM used tube modules in later vacuum tube computers, using larger
eight-tube
modules in the high-end 700-series computers.
An ad for the IBM 604, highlighting the pluggable modules. From
Time magazine
, March 31, 1952, page 65. Click this image (or any other) for a larger version.
Vacuum tubes and the thyratron
The IBM 604 used about 1250 vacuum tubes.
While vacuum tubes come in many different types, a typical type is the triode.
A triode is analogous to a transistor: a small input signal is amplified to control a much larger current.
In a transistor, the control signal is applied to the gate, controlling the current between the source and drain.
In a triode tube, the control signal is applied to the grid, controlling the current between the cathode and the plate.
The diagram above shows the construction of a vacuum tube.
The heater is a filament, very similar to an incandescent light bulb, that heats up the cathode to roughly 750 ºC.
At this high temperature, the cathode emits electrons.
When a large positive voltage (say, 100 volts) is put on the plate, the negatively-charged electrons are attracted.
The stream of electrons from the cathode to the plate causes a current to flow through the tube.
The current is controlled by the grid: if a small negative voltage is placed on the grid, it repels the negative
electrons, preventing them from reaching the plate and blocking the current through the tube.
A thyratron tube is similar to a vacuum tube, except it has a tiny bit of xenon gas inside, allowing it to handle higher current.
7
Like a triode, the thyratron is controlled by the grid.
However, when current starts to flow through the thyratron, the xenon ionizes and the xenon plasma carries current.
Unlike a vacuum tube, the grid cannot stop the flow of current.
Once the gas is ionized, a thyratron tube stays on until you remove its power
5
and the gas deionizes in microseconds.
6
You can see this behavior in the video.
When I pushed the first button, a small control signal ionized the gas, turning the tube on.
The large current through the ionized gas illuminated the light bulb.
The light stayed on until I briefly cut the power with the second button; the gas deionized,
turning off the tube.
The thyratron tube, type 2D21.
The photo above shows the thyratron tube, type 2D21, a miniature 7-pin tube.
8
The plate is visible inside the tube, with the other components hidden by the plate.
The dark stain at the top of the tube is the "getter", a reactive substance such as barium that
absorbs impurities inside the tube.
In the 604, thyratron tubes drove relay coils and powered the electromagnets that punched holes in cards.
Other IBM systems also used these thyratron tubes. For instance, the
IBM 83 Card Sorter
used thyratron
tubes as short-term storage to keep track of which holes had been detected in a card.
Conclusion
The IBM 604 occupies an interesting position between electromechanical accounting machines and electronic computers.
Although it has the speed of an electronic computer, it was still a calculator, lacking computer features such as loops,
memory, and stored programs.
Despite these limitations, the 604 was highly successful and led to other important IBM products.
IBM extended the 604 in 1949 so it could be programmed by punch cards in combination with plugboards; this was called the
Card-Programmed Electronic Calculator.
This system was still not quite a computer, but was very useful for
scientific calculation at places such as
Los Alamos National Labs
(
link
).
In 1953, IBM announced the successor to the 604, the IBM 650. Unlike the 604, the 650 was a programmable,
general-purpose computer; it became the most popular computer of the 1950s.
Eric Schlaepfer (TubeTime) has a box of IBM 650 modules, which we hope to power up soon.
For updates, follow me on
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
Thanks to CuriousMarc for extensive milling work to build the socket and colorful breakout box to hold the module.
AI statement: Despite the presence of the em dash, no AI was used in the writing of this article (
details
).
Notes and references
