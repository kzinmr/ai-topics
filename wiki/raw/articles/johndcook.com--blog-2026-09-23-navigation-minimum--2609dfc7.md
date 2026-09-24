---
title: "Navigation with only addition, subtraction, and tables"
url: "https://www.johndcook.com/blog/2026/09/23/navigation-minimum/"
fetched_at: 2026-09-24T10:01:16.067278+00:00
source: "johndcook.com"
tags: [blog, raw]
---

# Navigation with only addition, subtraction, and tables

Source: https://www.johndcook.com/blog/2026/09/23/navigation-minimum/

In the novel
Carry On, Mr. Bowditch
, a sailor asked Nathaniel Bowditch to teach him how to do navigational calculations, but the man only knows how to add and subtract by counting on his fingers. He had not heard of multiplication. Bowditch is surprised, but realizes if he made tables of logs of trig functions, then it would be possible for barely numerate sailors to calculate their position.
Carry On, Mr. Bowditch
is fiction, but it’s essentially factual, and so I imagine something like the conversation above did happen. I thought about how this might work, and it would be difficult.
It is true that if someone can add, subtract, and look-up numbers in a table of logarithms, they can effectively multiply. To find the product
xy
, they would look up the logarithms of
x
and
y
, add the results, then use the table in reverse to find what number has a logarithm equal to the sum.
Difficulties
But there are a couple difficulties in this imagined scheme. First, every calculation would require a lot of steps, including looking up numbers in multiple tables. It’s likely someone who cannot multiply also cannot read, so writing down instructions might not be viable. Second, carrying out calculations using tables is usually not simply a matter of looking up numbers; there are other things someone would need to know, such as
interpolation and range reduction
.
Bowditch was trying to train innumerate sailors to do specific calculations, not general mathematics, and so there would be ways to mitigate the problems above. Maybe he could create diagrams that would allow a semi-literate person to carry out an algorithm. The sailor wouldn’t need to be able to read
per se
. The instructions could be aids to help him recall memorized steps. The specialized nature of the calculations might also eliminate the need for range reduction and interpolation.
Tables
How many tables would be necessary? Someone who understands trigonometry doesn’t need separate tables for sine and cosines. And they wouldn’t need a table with entries for all angles. A table of sines for angles between 0 and 45° would be enough. But someone who doesn’t know multiplication would need more tables and bigger tables. Or they would need instruction in how to get by with less. It would be an interesting trade-off.
The novel mentioned tabulating logs of trig functions. For example, if you need to calculate
cos(
a
) cos(
b
)
it would be convenient to be able to look up log(cos(
a
)) and log(cos(
b
)) rather than look up the cosines and then look up their logs. But you’d still need to be able to convert
log( cos(
a
) cos(
b
) )
into
cos(
a
) cos(
b
).
This would require a table of logarithms, if the user is able to infer exponentials by reading a table in reverse. Otherwise you’d need a table of exponentials.
In general, you can assume less sophistication from a user by increasing the number of tables. But this also complicates the instructions the user must follow.
To give a specific example, suppose a sailor wanted to calculate his position using the
law of haversines
:
hav(
c
) = hav(
a
−
b
) + sin(
a
) sin(
b
) hav(
C
).
A mathematically sophisticated sailor would only need a table of sines to infer
c
from
a
,
b
, and
C
. He could calculate haversine via
hav(θ) = sin²(θ/2),
though inverting hav(
c
) to solve for
c
would require calculating a square root, either directly or via a table.
If one were to minimize the amount of sophistication needed by maximizing the use of tables, the algorithm for finding
c
would be
Subtract
b
from
a
and look up the haversine of the difference.
Look up log(sin(
a
)) and log(sin(
b
)) from one table and log(hav(
C
)) from another and add the results.
Take the exponential of the result in the previous step using a table of exponentials.
Add the results of steps 1 and 3, and look up the result in a table of inverse haversine values.
This would require five tables: sine, log sine, log haversine, exponential, and inverse haversine.
Condescension
Bowditch’s effort to make navigation accessible to the uneducated is an example of condescension in its literal and positive sense. If we say a person is condescending, we imagine an arrogant person who belittles those around him. But condescension literally means coming down to be with someone. Theologians use the word to describe the incarnation of Christ.
Like all scholars, Bowditch wrote for his peers, notably in his English edition of Laplace’s magnum opus on celestial mechanics. But unlike most scholars, he also devoted years of his life to a making knowledge accessible to uneducated men, culminating in his book
The New American Practical Navigator
, still in print
here
[1].
Related posts
[1] The book has been updated over the last couple centuries. Obviously the section on GPS, for example, does not date back to Bowditch.
