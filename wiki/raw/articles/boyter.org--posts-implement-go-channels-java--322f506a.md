---
title: "How to implement Go Channels in Java"
url: "https://boyter.org/posts/implement-go-channels-java/"
fetched_at: 2026-05-05T07:01:56.186396+00:00
source: "Ben Boyter"
tags: [blog, raw]
---

# How to implement Go Channels in Java

Source: https://boyter.org/posts/implement-go-channels-java/

How to implement Go Channels in Java
2023/03/13
(375 words)
I have been doing interviews recently, and whenever someone mentions knowing a lot of Go and Java one of the questions I put to them is how to implement Go channels in Java. Since there isn’t anything online to suggest how to do this that I liked reading (that I could find) I thought I would write one, and do it in native Java without needing to import a library.
Go channels are effectively a BufferedQueue (with size of 1 in the case of unbuffered) with some synatic sugar on top. To implement a Go channel like structure in Java you need a thread safe queue which when you want to close you add a poison value which tells the processing threads to quit. Threads need to be aware of this poison value and on getting it exit.
You can implement something which does this like the below.
import
java.io.IOException;
import
java.util.ArrayList;
import
java.util.concurrent.ArrayBlockingQueue;
public
class
Main
{
private
final
int
WORKERS
=
2;
private
final
String POISON
=
"quit"
;
private
final
ArrayBlockingQueue
<
String
>
queue
=
new
ArrayBlockingQueue
<>
(1000);
// our buffered channel of 1000 elements
public
static
void
main
(String
[]
args)
throws
IOException, InterruptedException {
var
m
=
new
Main();
m.
run
();
}
public
void
run
()
throws
InterruptedException {
// spawn as many workers as we want to deal with the queue, similar to usage of the go keyword in Go
var
threads
=
new
ArrayList
<
Thread
>
(
this
.
WORKERS
);
for
(
int
i
=
0; i
<
this
.
WORKERS
; i
++
) {
var
processor
=
new
Thread(
this
::process);
processor.
start
();
threads.
add
(processor);
}
// add things to our queue, similar to <- syntax in Go
for
(
int
i
=
0;i
<
10000;i
++
) {
this
.
queue
.
put
(
""
+
i);
}
// add a poison object, similar to close(channel) in Go
// we need to offer as many objects as there are workers to ensure
// that they all exit
for
(
int
i
=
0; i
<
this
.
WORKERS
; i
++
) {
this
.
queue
.
put
(POISON);
}
// wait for everything to finish up, which would be similar to wg.Wait() in Go
for
(
var
processor : threads) {
processor.
join
();
}
}
// Simulate some work that runs in a thread in a fuction
private
void
process
() {
try
{
while
(
true
) {
var
s
=
this
.
queue
.
take
();
if
(s.
equals
(POISON)) {
return
;
}
// process s here
}
}
catch
(InterruptedException ignored) {}
}
}
