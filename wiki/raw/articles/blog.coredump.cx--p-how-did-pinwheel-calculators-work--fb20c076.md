---
title: "How did pinwheel calculators work?"
url: "https://blog.coredump.cx/p/how-did-pinwheel-calculators-work"
fetched_at: 2026-11-25T10:00:48.676956+00:00
source: "lcamtuf.substack.com"
tags: [blog, raw]
---

# How did pinwheel calculators work?

Source: https://blog.coredump.cx/p/how-did-pinwheel-calculators-work

As a handful of readers might know, I am
a bit of a calculator nerd
. I’m especially fond of mechanical four-function calculators that had their heyday between the 1920s and 1960s and then disappeared without a trace.
A video is worth a thousand tokens, so to explore the ingenuity of the design, let’s start with a short clip of a Vaucanson calculator from my collection:
In the first half of the video, I demonstrate addition. I calculate 1234 + 4321 by placing the first operand in the input register, turning the crank clockwise to add this value to the accumulator (bottom right), and then entering the second operand and cranking again. To subtract from the stored value, I’d turn the crank counterclockwise.
The second and more interesting half shows multiplication: I solve 79 × 123 by entering the first operand and then turning the crank three times to load 79 × 3 into the accumulator. Next, I shift the accumulator carriage one decimal digit to the right and crank twice; because the accumulator is offset from the input register, this has the same effect as cranking twenty times in the original position; in other words, I add 79 × 20. Finally, I shift the carriage once more and complete one more turn to add 79 × 100. Note that the crank counter in the bottom left now reads “123”, confirming that we multiplied the first operand by the correct value.
To divide, I’d load the first operand into the accumulator and then successively subtract power-of-ten multiples of the second number. This would give me the integer result in the counter register and the remainder in the accumulator.
Alright — so how does this work? Well, if you pop open a pinwheel calculator, you will be greeted by a pretty complicated mechanism:
Calculator entrails. By author.
There’s a lot going on here, but the most important part of the assembly is the prominent stack of input disks, one per digit, as seen in the top right of the photo. Each disk has three main components: a center section mounted to a keyed shaft that stays in position until the main crank is turned; a set of nine radial pins that slide into grooves machined in that disk; and a freely-moving digit-setting ring with a track and a couple of detents:
The fundamental mechanism of a pinwheel calculator. By author.
Each pin has a protrusion that rides in the track of the digit-setting ring. By turning the input lever, we can change the number of pins that extend from the assembly.
Input digit set to “3”, with three pins extended. By author.
When the crank is turned, these extended pins mesh to an intermediate gear that advances the digit at the corresponding position of the accumulator:
Of course, this mechanism is not enough: without a way to carry to the next column, 0001 + 0009 would give us 0000 instead of 0010. To implement carry, each input disk (except for the rightmost one) is also equipped with a spring-loaded carry pin. This pin sticks out at all times, but is normally out of the path of the intermediate gear, so it has no effect on the output value.
To perform carry, each output position is equipped with a cam that pushes a wedge-shaped carry-sensing lever into the path of the carry pin just as the digit rolls over from 9 to 0. This wedge pushes the pin to the left, momentarily placing it in the path of the intermediate gear for the next decimal digit.
This is a mouthful; the entire process is shown in the following video:
The carry-sensing lever is pushed back into the retracted position before the drum completes a full rotation, thus allowing the carry pin to spring back.
Note that the carry pins are staggered and do not engage at all once; this is to allow carry to effortlessly ripple through all digits if necessary (e.g., when adding 9999 + 1).
There’s a couple of additional convenience and reliability features in each pinwheel calculator; this includes interlocks to prevent out-of-sequence inputs, as well as reset levers for each register. There’s even a mechanical bell on overflow or underflow. I won’t bore you with all the gory details, in part because these mechanisms are less interesting — but if you’re morbidly curious, this
ancient YouTube video
provides a more complete walkthrough.
And if you want to learn about the prehistory of calculators, I invite you to check out my 2023 article:
PS. Yep, this is why one of the registers on all Intel CPUs is called the “accumulator”.
I write articles about
electronics
,
math
,
philosophy
, and
more
. If you like what you see, please subscribe.
