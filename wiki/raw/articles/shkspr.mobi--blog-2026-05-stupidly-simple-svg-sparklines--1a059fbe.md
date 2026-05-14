---
title: "Stupidly Simple SVG Sparklines"
url: "https://shkspr.mobi/blog/2026/05/stupidly-simple-svg-sparklines/"
fetched_at: 2026-05-14T07:00:37.678232+00:00
source: "shkspr.mobi"
tags: [blog, raw]
---

# Stupidly Simple SVG Sparklines

Source: https://shkspr.mobi/blog/2026/05/stupidly-simple-svg-sparklines/

A sparkline is a little line-graph with no axes or other unnecessary details. They're useful for getting quick understanding of what the data is showing.
They're also
really
easy to create programmatically.
This uses the SVG "
polyline
" which takes a list of x,y co-ordinate pairs. But can you spot the small problem?
⧉
SVG
<
svg
xmlns
="http://www.w3.org/2000/svg"
viewBox
="0 0 1024 124">
    <
polyline
fill
="none"
stroke
="#0074D955"
stroke-width
="3"
points
="12,48 83,84 154,79 226,90 297,79 369,65 440,78 512,80 583,88 654,12 726,56 797,92 869,93 940,97 1012,106"></
polyline
>
</
svg
>
The SVG co-ordinate system has position 0,0 at the top
left
. Most graphics formats are like that. That's fine for our x value - but it means higher y values will appear
lower
on the graph.
Getting the x co-ordinate of each data point is easy. Take the width of the SVG image and divide it by the number of data-points.
The y co-ordinate is harder. The algorithm is:
Find the height of the SVG.
Find the maximum value in the data.
Find the minimum value in the data.
Divide the maximum value by the height of the graph.
For each data point, either:
To have the lowest value at the bottom of the graph, subtract the minimum from the value, then multiply by the ratio in (4).
Or, to retain the gap between zero and the lowest value, multiply the value by the ratio in (4).
The y co-ordinate is calculated by subtracting the value in (5) from the height in (1).
Here's some code showing how it works. I've added a little padding to the inside of the graph - you'll see why later:
⧉
PHP
//  Max and min of views.
$max_views
=
max
(
$svg_views_data
);
$min_views
=
min
(
$svg_views_data
);
$svg_data_length
=
sizeof
(
$svg_dates_data
) - 1;
//  SVG details for scaling.
$svg_padding
= 12;
$svg_width_graph
= 1000;
$svg_width
=
$svg_width_graph
+ (
$svg_padding
* 2 );
$svg_height_graph
= 100;
$svg_height
=
$svg_height_graph
+ (
$svg_padding
* 2 );
//  Calculate where each point should be.
$x_per
=
$svg_width_graph
/ (
$svg_data_length
);
$y_per
=
$svg_height_graph
/
$max_views
;
//  Loop through the data.
foreach
(
$svg_views_data
as
$index
=>
$views
) {
//  X is from the left.
$x_pos
=
intval
(
$x_per
*
$index
) +
$svg_padding
;
//  Y is from the top.
$y_pos
=
$svg_height
-
intval
(
$y_per
*
$views
) -
$svg_padding
;
//  Add a point to the line.
$polyline_points
.=
"{$x_pos},{$y_pos}\n"
;
}
echo
<<<
SVG
<svg xmlns=
"http://www.w3.org/2000/svg"
viewBox=
"0 0 $svg_width $svg_height"
class=
"chart"
>
    <polyline
        fill=
"none"
stroke=
"#F00"
stroke-width=
"3"
points=
"{$polyline_points}"
/>
</svg>
SVG
;
Suppose someone suggests stupidly simple sparklines suffer seriously so someone should supplement statistics several circles?
Using the same co-ordinates, we can place an SVG circle on top of the point. Give it a "title" attribute and you have a little bit of interactivity.
⧉
SVG
<
circle
cx
="12"
cy
="48"
r
="5"
fill
="#0074D955"><
title
>4,707 Views</
title
></
circle
>
Here's how it looks (view source to understand how it is constructed).
4,707
2025-09-01
2,051
2025-09-02
2,444
2025-09-03
1,627
2025-09-04
2,450
2025-09-05
3,453
2025-09-06
2,491
2025-09-07
2,326
2025-09-08
1,754
2025-09-09
7,268
2025-09-10
4,113
2025-09-11
1,503
2025-09-12
1,394
2025-09-13
1,108
2025-09-14
533
2025-09-15
Hover over any of those little circles and you'll see some pop-up text giving you information about that datapoint.
…that's it! If you have an array of data points, you can easily create a graph with no graphing library, no plugins, no 3rd party dependencies. Just super simple SVG.
