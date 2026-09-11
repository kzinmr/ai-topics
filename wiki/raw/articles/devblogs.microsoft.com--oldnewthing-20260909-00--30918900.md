---
title: "What algorithm did Windows XP use to choose your initial user picture?"
url: "https://devblogs.microsoft.com/oldnewthing/20260909-00/?p=112683"
fetched_at: 2026-09-10T10:01:26.508713+00:00
source: "devblogs.microsoft.com/oldnewthing"
tags: [blog, raw]
---

# What algorithm did Windows XP use to choose your initial user picture?

Source: https://devblogs.microsoft.com/oldnewthing/20260909-00/?p=112683

I noted some time ago that
Windows XP chose your initial picture at random
from among the pictures in the
%ALLUSERSPROFILE%\
Application Data\
Microsoft\
User Account Pictures\
Default Pictures
directory. But it seems people want to know more.
The random number generator is our friend
RtlRandomEx
, using the current value of
GetTickCount()
as the initial seed.
The function uses a one-pass random selection algorithm. I can immediately think of two benefits of this decision. First, compared to the naïve two-pass algorithm of counting up all the items, then randomly picking a number from 1 to
n
, and then iterating a second time to find the item at that index, it’s more efficient because it reduces the amount of calls into the file system, which is where the bottleneck is. Furthermore, the one-pass algorithm avoids complications if the number of files in the directory changes while the code is running.
The one-pass algorithm is a special case of
reservoir sampling
, where
k
is 1. This special case permits a tailored algorithm that is much simpler.
selectRandomFromIterator(iterator)
{
    var count = 0;
    var winner = null;

    while (iterator.moveNext()) {
        ++count;
        if (uniform_random(min: 1, max: count) == count) {
            winner = iterator.current();
        }
    }

    return winner;
}
The way this algorithm works is by observing that in a collection of
n
items, the last item has a 1/
n
chance of being randomly selected. If it isn’t selected, then you need to select randomly from the first
n
− 1 items, which you can solve recursively.
Playing the recursion forward, you start with the base case which is that if you have a list of 1 item, then your only choice is to chose that item. Otherwise, if you have a list of
n
items, first choose an item randomly from the first
n
− 1, and then switch to the
n
th item with a 1/
n
probability.
As a final safety check, the code stops after sampling 100 pictures. This avoids pathological behavior if somebody puts a million files in the
Default Pictures
directory.
