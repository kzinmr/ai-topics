---
title: "Steering Zig Fmt"
url: "https://matklad.github.io/2026/05/08/steering-zig-fmt.html"
fetched_at: 2026-05-09T07:01:07.893477+00:00
source: "matklad.github.io"
tags: [blog, raw]
---

# Steering Zig Fmt

Source: https://matklad.github.io/2026/05/08/steering-zig-fmt.html

Steering Zig Fmt
May 8, 2026
Two tips on using
zig fmt
effectively. Read this if you
          are writing Zig, or if you are implementing a code formatter.
For me,
zig fmt
is better than any other formatter I
          used:
rustfmt
, the one in IntelliJ,
deno fmt
.
zig fmt
is steerable. For every
          syntactic construct, it has several variations for how it might be
          laid out. The variation used is selected by looking at what’s
          currently in a file.
Easier to show a pair of examples:
f(
1
,
2
,
3
);
f(
1
,
2
,
3
);
f(
1
,
2
,
3
,);
f(
1
,
2
,
3
,
);
Depending on the trailing comma, function call is formatted on a
          single line, or with one argument per line.
The way this plays out in practice is that you
decide
how you
          want to lay out the code, add a couple of
,
, hit the
          reformat shortcut (
, p
is mine
), and
zig fmt
does
          the rest. For me, this works better than the alternative of the
          formatter guessing. 90% of great formatting are blank lines between
          logical blocks and tasteful choice of intermediate variables, so you
          might as well lean into key choices, rather than eliminate them.
I know of one non-trivial formatting customization point: columnar
          layout for arrays:
.{
1
,
2
,
3
,
4
,
5
,
6
,
7
,
8
,
9
,
10
,
11
,  };
One would think that trailing comma would lead to a number-per-line
          layout, but, for arrays,
zig fmt
also takes note of the
          first line break. In this case, the line break comes after the first
          three items, so we get three numbers per line, aligned:
.{
1
,
2
,
3
,
4
,
5
,
6
,
7
,
8
,
9
,
10
,
11
,
};
How cool is that!
Furthermore, with judicious use of
++
, you can vary the
          number of items per line. When I need to pass
--key
value
pairs to subprocess, I often go for formatting like
          this:
try
run(
&
(.{
"aws"
,
"s3"
,
"sync"
, path, url }
+
+
.{
"--include"
,
"*.html"
,
"--include"
,
"*.xml"
,
"--metadata-directive"
,
"REPLACE"
,
"--cache-control"
,
"max-age=0"
,
}));
