---
title: "The electromechanical angle computer inside the B-52 bomber's star tracker"
url: "http://www.righto.com/2026/04/B-52-star-tracker-angle-computer.html"
fetched_at: 2026-04-29T07:01:13.759255+00:00
source: "righto.com"
tags: [blog, raw]
---

# The electromechanical angle computer inside the B-52 bomber's star tracker

Source: http://www.righto.com/2026/04/B-52-star-tracker-angle-computer.html

Before GPS, how did aircraft navigate?
One important technique was celestial navigation: navigating from the positions of the stars, planets,
or the sun.
While celestial navigation is accurate, cannot be jammed, and doesn't require any broadcast infrastructure,
it is a difficult and time-consuming process to perform manually. 
In the early 1960s, an automated system was developed for the B-52 bomber to automatically track
stars and compute navigation information.
Digital computers weren't suitable at the time, so the star tracking system performed trigonometric
calculations with an
electromechanical analog computer called the Angle Computer.
1
The Angle Computer contains complex electromechanical systems. Click this image (or any other) for a larger image.
The photo above shows the mechanism inside the Angle Computer.
2
Although it may look like a gyroscope or IMU (Inertial Measurement Unit), it is completely different
and nothing is spinning.
The Angle Computer
physically models the "celestial sphere", with a complicated mechanism inside that moves a
pointer that represents the position of a star.
The corresponding angles (the azimuth and altitude) are read out electrically through devices
called synchros, providing information to the navigation system through bundles of wires.
In this article, I'll give an overview of how celestial navigation works and explain how the
Angle Computer performs its calculations.
The Astro Compass system
The Angle Computer is one piece of the Astro Compass, a system that
locked onto a star and produced a highly accurate heading (i.e., compass direction), accurate to a tenth of a degree.
While the heading is the main output from the Astro Compass, the navigator can also use it to determine position, using the "lines of position" technique described later.
The Astro Tracker was mounted on top of the aircraft with the plastic bubble sticking out.
The Astro Compass navigation system was built around the "Astro Tracker" (above), the optical system that tracks a star.
The Astro Tracker was mounted on the aircraft with the 4-inch glass dome protruding from the top of the fuselage.
This unit contains a tracking telescope, which used a photomultiplier tube to detect the light from a
star.
A gyroscope and a complicated system of motors provided a "stable platform", keeping the telescope precisely vertical
even as the aircraft tilted and moved.
A prism rotated and tilted to aim the telescope at a particular star.
3
The Astro Compass system is bewilderingly complicated, consisting of 19 components (above) to support the Astro Tracker.
4
On the right are the ten amplifier and computer components that controlled the system;
the Angle Computer is in the lower right.
On the left are the nine control and indicator panels that were used by the B-52's navigator.
The photo below shows four of these panels in use in a B-52 in 1972.
The navigator's station in a B-52. Some of the Astro Compass controls are indicated with arrows: the Line of Position display and the Master Control on the left, and the Heading display and Indicator display to the right. The navigator in this photo is
Carl Hanson-Carnethon
. From
Rob Bogash's B-52 photo album
. This specific B-52 (#2584) is now at
The Museum of Flight
, Seattle, but the Astro Compass is no longer present.
Controlling the Astro Compass
The Astro Compass has an interesting user interface, letting you input one value at a time by rotating a knob.
First, you use the
Master Control Panel to select a data value such as the clock time, SHA (Sidereal Hour Angle) for star #1, or
Declination for star #3.
Then you turn the "Set Control" knob clockwise or counterclockwise to scroll through the data values
until the proper value is reached.
Each knob on the Master Control Panel has a different geometrical shape, allowing the user
to distinguish the knobs by feel.
The Master Control Panel is visible in the lower left corner of the photo above, within easy reach of the navigator.
The Master Control Panel is the main interface to the Astro Compass.
Each data value has a separate electromechanical display.
The photo below shows a Star Data display, indicating the sidereal hour angle and the declination
for a star.
I removed the cover so you can see how the digital display actually consists of analog dials rotated by motors
under synchro control.
The system has three Star Data displays, so it can 
hold the positions of three stars at a time.
Getting fixes from three different stars is
useful when computing lines of position. The system uses one star at a time, but you can quickly change stars by flipping the Star switch on the Master Control Panel.
A Star Data display with the cover removed.
But how did the navigator obtain the information to put into the Astro Compass, since the sun, moon, stars, and planets are in constant motion?
5
The necessary celestial information is published in a book called
the
Air Almanac
.
The US Government started publishing the Air Almanac in 1941, issuing a new volume every four months.
The Almanac had a sheet for each day, providing celestial data on 10-minute intervals.
The first column has the time
(GMT, Greenwich Mean Time)
6
while the other columns give the position of the sun, an important value
called the First Point of Aries (symbol ♈︎), the positions of the visible planets,
and the position of the moon.
A separate table and chart provided the locations of stars; the stars don't have daily
updates since they are almost stationary.
7
(The Air Almanac is now online; you can download the 2026 Air Almanac
here
.)
An excerpt from the 1960 Air Almanac. Photo used with permission from
tanasa2022
, who is selling the Almanac on
eBay
.
The navigational triangle: Computing a star's position
The Air Almanac provides star coordinates in a global coordinate system, but the Astro Compass needed to
know star coordinates in the aircraft's local coordinate system.
Determining the star's position requires changing the coordinate system by using
spherical trigonometry and something called the navigational triangle.
There's a fair bit of terminology involved, which I'll explain in this section.
The Astro Tracker, like many telescopes, is aimed by using
azimuth
and
altitude
.
Suppose you go into your yard, point at the horizon, and turn 360° in a circle; the direction
you're pointing is called the azimuth.
The point directly overhead is called the
zenith
.
Now swing your arm upwards 90° from the horizon to the zenith. That angle is
called the altitude.
(Confusingly, the term "altitude" is used both for the angle of a star and the height of an aircraft.)
Thus, if you point at a particular star, you can describe its position with two angles:
your horizontal rotation from north gives the azimuth, and the
angle up from the horizon gives the altitude.
8
This system is called the
horizontal coordinate system
, as it is based on the horizon.
(The word "horizontal" comes from "horizon", by the way.)
This is a local coordinate system since
other locations will have a different azimuth and altitude for the star.
The azimuth and altitude constantly vary with time because the Earth's rotation makes the star appear to move.
The
equations
for the altitude and azimuth are complicated, with sines, cosines, arcsine,
and arctangent.
To see why the equations are complicated, consider a time-exposure photo of star trails.
As the Earth rotates, each star forms a circle around Polaris, the North Star.
To trace out this circular path, the altitude and azimuth vary in a trigonometric way.
This computation is performed electromechanically by the Angle Computer, as will be explained later.
Now let's switch to how the position of a star is defined in the Air Almanac (for example),
independently of your local position.
Pretend that the stars are on the surface of a large sphere that surrounds the Earth, called
the
celestial sphere
.
The stars are stationary on the surface of the celestial sphere, while the Earth rotates once
a (sidereal)
9
day in the middle. Thus, as you look up at the celestial sphere, you see the stars moving.
You can extend the Earth's equator out to the celestial sphere, defining the
celestial equator
.
Likewise, the celestial sphere has
celestial poles
, matching the Earth's poles.
On the Earth, you specify a location (such as the airplane's location) with latitude and longitude (red).
Latitude is measured from the equator, and longitude is measured from a fixed meridian (orange).
The 0° meridian is arbitrarily defined to pass through Greenwich (England, not Connecticut).
Similarly, the position of a star is specified by the angle from the celestial equator (called
declination
instead of latitude) and the angle from the meridian (called the
sidereal hour angle
or SHA instead of longitude).
10
The celestial sphere, with the Earth at the center. The position of a star is described by Sidereal Hour Angle and declination, analogous to longitude and latitude describing the position of, say, an airplane on the Earth. The diagram is based on
patent 2998529
, "Automatic astrocompass".
But what meridian is the starting point—0°—when measuring a star's Sidereal Hour Angle?
The celestial equator matches the Earth's equator, but this won't work for the Greenwich meridian
because it is constantly in motion.
Instead, the 0° celestial meridian is arbitrarily defined as the position where the sun crosses the equator
at the vernal equinox (the start of spring).
If you consider the position of the sun on the celestial sphere, the sun will travel around the
sphere once a year. Because the Earth's axis is tilted, the sun will be above the equator
half the year and below the equator half the year, crossing the equator at the vernal equinox (March)
and the autumnal equinox (September).
This reference point on the celestial sphere is called the First Point of Aries, represented by the symbol
♈︎ (horns of a ram); you might remember this symbol from the Air Almanac.
At this point, the sun is in the constellation Pisces.
So why is this point called the First Point of Aries and not Pisces?
Back in 130 BCE, the ancient Greek astronomer Hipparchus defined the First Point of Aries as the starting point for the sun's motion.
In that distant era,
the sun was in the constellation Aries at the equinox, not in Pisces as it is today.
It turns out that the direction of the Earth's axis isn't fixed, but moves in a 26,000-year
cycle called the precession of the equinoxes.
11
A 26,000-year cycle may seem irrelevant, but it's fast enough that the sun has moved from Aries
to Pisces since Hipparchus's time.
(And the equinox has moved 1° more since the B-52 was first produced!)
(All this talk of Aries and Pisces may sound like astrology, and, yes, there is a direct connection.
Aries is the first zodiac sign, starting at the vernal equinox, typically March 21. The equinox's precession is "backwards", so
the equinox has moved to Pisces, the last zodiac sign.
Astronomically, the equinox will move into the constellation Aquarius around 2600 CE, but
astrologers disagree on whether the Age of Aquarius has started;
perhaps the 1960s was
the dawning of the Age of Aquarius
.)
How do you convert the star's fixed coordinate to the Earth's rotating coordinate?
First, you look up the angle between the Greenwich meridian and the celestial meridian of Aries at a
particular time.
This angle (purple) is called the Greenwich Hour Angle of Aries (GHA ♈︎).
Next, you look up the star's Sidereal Hour Angle (SHA). Adding them gives you the
star's Greenwich Hour Angle (red), the angle between the Greenwich meridian and the star.
Subtracting the aircraft's longitude gives you the Local Hour Angle (LHA, not shown), the angle between
the aircraft's meridian and the star.
(Note that these steps are simply addition and subtraction, so a mechanical system can easily do
them with differential gears.)
Computing the Greenwich Hour Angle of the start on the sphere.
The final step, obtaining the azimuth and altitude, requires tricky spherical trigonometry.
The yellow triangle is the navigational triangle, a spherical triangle on the surface of the celestial sphere.
The upper vertex is the North Pole, the red vertex is the airplane's zenith (i.e., directly above the airplane), and the final vertex is the star.
Two sides of the triangle and an angle (purple) are known, so the remaining angles and sides can be
solved with spherical trigonometry.
Specifically, the first side (purple) is 90°-declination, the second side is 90°-latitude,
12
and the angle between is the LHA (Local Hour Angle).
Solving for the angle at the zenith gives the azimuth (blue), while solving for the third side gives 90°-altitude (green, the angle down from the zenith to the star).
By solving the navigational triangle, the altitude and azimuth can be obtained.
Thus, the key problem is solving the navigational triangle.
Navigators could solve the navigational triangle by looking up angles in a thick book of
"sight reduction" tables
and performing some math.
But how could the process be automated? That was
the purpose of the Angle Computer.
The Angle Computer
The job of the Angle Computer was to solve the navigational triangle mechanically.
Its inputs were the star's declination, altitude, and local hour angle.
From these, it computed the star's altitude and azimuth at the aircraft's current position.
13
The concept behind the Angle Computer is that it physically modeled the celestial sphere with a half-sphere,
2 5/8" in radius.
A star pointer was mechanically positioned on the surface of this sphere, using the star's declination and local
hour angle, adjusted by the latitude of the viewer.
The star pointer moved a readout mechanism that translated the star's position into the azimuth and
altitude at the specified location.
Thus, the Angle Computer mechanically converted between the coordinate systems by using a physical
representation, solving the navigational triangle.
The diagram below shows how the star pointer is positioned on the two-dimensional surface of the sphere,
using a complicated mechanism inside the sphere.
The U-shaped declination arm swings up and down, corresponding to the star's declination (angle above
the celestial equator). 
Meanwhile, the declination arm constantly rotates around the polar axis, as specified by the LHA (Local Hour Angle).
In one (sidereal) day, the mechanism will make a full cycle, corresponding to the Earth's spin.
Finally, the latitude arm moves the mechanism up or down, corresponding to the viewer's latitude.
On the right, three gears provide the inputs for latitude, LHA, and declination.
The input mechanism for the Angle Computer. The photo has been rotated 90° to better match the
Earth's rotation. Rotation around the polar axis corresponds to the Earth's daily rotation. Note that the star pointer will hit the end of the semicircular azimuth arc at some point; this corresponds to the star moving to the horizon and setting.
A separate mechanism provides the altitude and azimuth outputs, driven by the star pointer.
The key is the semicircular azimuth arc, which represents the arc from the viewer's horizon to
the zenith, oriented to a particular azimuth. 
The star pointer is attached to the azimuth arc through a slider, so as the star pointer moves,
it moves the slider along the azimuth arc and also rotates the azimuth arc.
Specifically, the azimuth arc represents the line from the horizon to the zenith at a particular azimuth.
The position of the
slider on the azimuth arc corresponds to the altitude, from 0° at the horizon to 90° at the zenith.
14
.
The azimuth arc rotates around the zenith point, which is at the back of the azimuth arc; this rotation
indicates the azimuth value.
As the azimuth arc rotates, it turns a gear at the zenith, providing the azimuth output.
The slider arc has teeth on it; as the slider moves, these teeth rotate a second gear, providing the altitude output.
The output mechanism for the Angle Computer. The mechanism is in a different position from the
previous diagram. In particular, the latitude arm has been raised to a near-polar latitude and the photograph is from
the other side of the latitude arm. At this latitude, the polar axis is almost lined up with the zenith. As the LHA changes, the star will move in a circle, rotating the azimuth arc but causing little change in altitude. This corresponds to the real world situation of stars moving in a cirle around the zenith, if you're near the pole.
From the back, the numerous synchro transmitters, synchro control transformers, and motors are visible.
Even though the computation itself is mechanical, the Angle Computer has numerous electrical components.
In the top half, 
the synchro transmitters provide electrical outputs of the azimuth and altitude. (A synchro transmitter
uses fixed and moving coils to convert a shaft rotation angle into a three-wire electrical signal.)
The large gear provides the altitude output.
In the lower half, the longer cylinders are motors that move the Angle Computer's mechanisms.
The motors are directed to rotate to a particular position through a feedback loop:
synchro control transformers provide feedback to the external servo amplifiers that power the motors.
The back of the Angle Computer.
Partially disassembling the Angle Computer shows the complex gear trains inside, linking the
synchros, motors, and the physical mechanism.
The squat brass-colored units in the lower center are differential assemblies to add or subtract signals.
15
One of the drive motors, a long cylinder, is visible in the lower right.
Gear trains inside the Angle Computer.
The Line of Position
Although the heading was the primary output from the Astro Compass,
the Astro Compass could also help determine the location of the aircraft, using a technique called
the celestial line of position.
This technique was discovered in 1837 and became heavily used for navigating ships with a sextant.
It could also be used onboard an aircraft.
To understand the line of position, suppose you go outside and find a star directly overhead.
If you measure the altitude—the angle from the horizon to the star—with a sextant, the angle will be 90°, since it is overhead.
Now, suppose you teleport 60 nautical miles away in any direction. 
The sextant will now show an altitude of 89° to the star, since a nautical mile is conveniently defined to match
one minute of angle (one-sixtieth of a degree).
Alternatively, if you measure an altitude of 89° to the star, you know you are 60 miles away from the original
point under the star (called the sub-stellar point).
Likewise, if you measure 88° to the star, you're on a circle with radius of 120 nautical miles around the sub-stellar point.
If you measure, say, an altitude of 40°, you know you're on a very large circle with radius of 3000 miles around the sub-stellar point.
So how does this help with navigation?
Suppose you're on a boat in the middle of the Pacific and you have a rough idea of where you are, say within 100 miles, but you want to find your exact position.
Put a dot on the map where you think you are.
Next, pick a star and work out what the angle to the star should be from your position.
Measure the altitude with your sextant.
Suppose you expected 50° but measured 51°. You now know that you're somewhere on a circle with radius of
2340 miles around the distant sub-stellar point. This doesn't seem very useful.
However, since the angle was 1° more than expected, you know that the circle is 60 miles closer to that
distant point than your estimated position.
Moreover, since you have some idea of where you are, you know that you're on the part of this
circle near your estimated location.
And since you're looking at a small part of a big circle, you can approximate it by a line.
So you can go back to your map, move 60 miles closer to the star from your estimated point,
and draw a perpendicular line.
This is your line of position, and you know that you're on this line (more or less).
Knowing that you're on a line isn't too useful, but you can repeat the process with a
star in a different part of the sky.
Maybe this time the angle is 2° smaller than expected, so you can draw a line of position
120 miles further away from your estimated position, in a different direction.
The two lines cross, indicating a position where you (probably) are.
16
Normally, you repeat the process with a third star, giving you three lines of position,
providing a position and an idea of its accuracy.
The Astro Compass used the display above to show the
star's azimuth and the distance in miles from the assumed location to the line of
position, called the Altitude Intercept.
With this information, the navigator could draw a line of position on the map.
The navigator repeated the process with two more stars to get a location fix.
17
Conclusion
The Angle Computer is a relic from a time when a mechanical analog computer was the best way to solve a
problem, but the computer was also electrical.
Although a mechanical apparatus solved the navigational triangle, it was moved into position by motors, and
the output was transmitted electrically through wires.
Moreover, the Angle Computer was driven by electronic amplifiers and feedback circuits that used both vacuum
tubes and transistors.
The designers of the Astro Compass considered multiple approaches to computing the navigational triangle (
details
).
The first was to use small electromechanical devices called resolvers that convert a physical rotation into sine and cosine values.
By combining six resolvers with amplifiers, the altitude and azimuth could be obtained.
The resolver solution was rejected as being too large and requiring a precision power supply.
The second approach was to use a digital computer to determine the solution.
This solution was rejected because in 1963, a digital computer was expensive, slow, and less reliable.
The final approach, which was adopted, was to build a mechanical, physical model of the celestial sphere.
Thus, the Angle Computer resided at the uneasy intersection of physical mechanisms, electrical circuits, vacuum
tubes, and solid-state electronics, soon to be obsoleted by digital computers.
I plan to write more about the Astro Compass system. For updates, follow me on
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
Thanks to Richard for supplying the Astro Compass hardware.
AI statement: I didn't use AI to write this article (
details
).
Notes and references
