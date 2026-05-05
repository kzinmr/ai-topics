---
title: "A quick comparison between different Go file walk implementations"
url: "https://boyter.org/2018/03/quick-comparison-go-file-walk-implementations/"
fetched_at: 2026-05-05T07:01:59.687909+00:00
source: "Ben Boyter"
tags: [blog, raw]
---

# A quick comparison between different Go file walk implementations

Source: https://boyter.org/2018/03/quick-comparison-go-file-walk-implementations/

UPDATE
The below is here for historical reasons, but since 2021 very out of date. See this post
https://engineering.kablamo.com.au/posts/2021/quick-comparison-between-go-file-walk-implementations
for an updated comparison.
Whats the fastest way to get all the names of all files in a directory using Go? I had a feeling that the native walk might not be the fastest way to do it. A quick search showed that several projects claimed to be faster. Since the
application
I am currently working on needs a high performance scanner I thought I would try the main ones out.
Note that I have updated the code and the results based on feedback from reddit. The first change is I set it to just count the files rather than print the output to avoid measuring output buffering. I did do this before but noticed that while running in hyperfine it made no difference. I updated it anyway to avoid this being called into question again. The second was based on feedback from the godirwalk author. Setting the “unsorted” true option manages to pull another ~150ms of speed out of the bag which is perfect for me. Since the goroutine implementations have the same sorting issue (as far as I can see) it seemed fair to turn it on.
package
main
import
(
"fmt"
"os"
"path/filepath"
)
func
main
() {
count
:=
0
filepath
.
Walk
(
"./"
,
func
(
root
string
,
info
os
.
FileInfo
,
err
error
)
error
{
if
err
!=
nil
{
return
err
}
count
++
return
nil
})
fmt
.
Println
(
count
)
}
package
main
import
(
"fmt"
"github.com/MichaelTJones/walk"
"os"
)
func
main
() {
count
:=
0
walk
.
Walk
(
"./"
,
func
(
root
string
,
info
os
.
FileInfo
,
err
error
)
error
{
if
err
!=
nil
{
return
err
}
count
++
return
nil
})
fmt
.
Println
(
count
)
}
package
main
import
(
"fmt"
"github.com/iafan/cwalk"
"os"
)
func
main
() {
count
:=
0
cwalk
.
Walk
(
"./"
,
func
(
root
string
,
info
os
.
FileInfo
,
err
error
)
error
{
if
err
!=
nil
{
return
err
}
count
++
return
nil
})
fmt
.
Println
(
count
)
}
package
main
import
(
"fmt"
"github.com/karrick/godirwalk"
)
func
main
() {
count
:=
0
godirwalk
.
Walk
(
"./"
,
&
godirwalk
.
Options
{
Unsorted
:
true
,
Callback
:
func
(
osPathname
string
,
de
*
godirwalk
.
Dirent
)
error
{
count
++
return
nil
},
ErrorCallback
:
func
(
osPathname
string
,
err
error
)
godirwalk
.
ErrorAction
{
return
godirwalk
.
SkipNode
},
})
fmt
.
Println
(
count
)
}
And the results. All were run in the WSL for Linux on a Surface Book 2 against a recent checkout of the Linux kernel with there being 67359 files in the directory.
$ hyperfine './cwalk' && hyperfine './godirwalk' && hyperfine './nativewalk' && hyperfine './walk'
Benchmark #1: ./cwalk
  Time (mean ± σ):      1.812 s ±  0.059 s    [User: 368.4 ms, System: 6545.8 ms]
  Range (min … max):    1.753 s …  1.934 s

Benchmark #1: ./godirwalk
  Time (mean ± σ):     695.9 ms ±  16.7 ms    [User: 73.0 ms, System: 619.2 ms]
  Range (min … max):   671.2 ms … 725.6 ms

Benchmark #1: ./nativewalk
  Time (mean ± σ):      3.896 s ±  0.489 s    [User: 153.0 ms, System: 3757.4 ms]
  Range (min … max):    3.560 s …  5.034 s

Benchmark #1: ./walk
  Time (mean ± σ):      1.674 s ±  0.071 s    [User: 399.7 ms, System: 6383.3 ms]
  Range (min … max):    1.571 s …  1.769 s
For comparison ripgrep which is probably the fastest disk scanner comes in at ~600ms. That is not a fair comparison though as it ignores certain directories but it gives you an idea of the upper bounds of useful performance.
Turns out that the native implementation that ships with Go is indeed the slowest. The fastest by a long shot is godirwalk however. It is at least 2x as fast as the next quickest implementation. So if bleeding performance matters it would seem that using godirwalk is the best option. If however you want a drop in replacement for some additional speed I would suggest going with cwalk or walk. Of course if you aren’t scanning the linux kernel its hard to go wrong with even the native implementation which is generally fast enough for most cases.
