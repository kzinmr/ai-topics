---
title: "What's the highest legal FILETIME? Is it safe to use?"
url: "https://devblogs.microsoft.com/oldnewthing/20260921-00/?p=112711"
fetched_at: 2026-09-22T10:00:53.852939+00:00
source: "devblogs.microsoft.com/oldnewthing"
tags: [blog, raw]
---

# What's the highest legal FILETIME? Is it safe to use?

Source: https://devblogs.microsoft.com/oldnewthing/20260921-00/?p=112711

A customer wanted to define a sentinel
FILETIME
that will be considered larger than another
FILETIME
. In other words,
Compare­File­Time
should always say that the sentinel value is later. What’s a good value to use?
Strictly according to the definition, the
FILETIME
consists of ticks since January 1, 1601, and it is an unsigned value, so the highest value is presumably
0xFFFFFFFF`FFFFFFFF
.
On the other hand, the documentation for
FILETIME
itself notes that some functions consider the value
0xFFFFFFFF`FFFFFFFF
to have special meaning. For example, the
Set­File­Time
function treats that value as meaning “Do not update the time for this handle.”
Any values larger than
0x7FFFFFFF`FFFFFFFF
will also cause problems because functions like
Create­Waitable­Timer
treat
FILETIME
s with the high bit set as representing the negative of a relative duration rather than an absolute point in time. Also, some programs consider those values to represent times that comes
before
January 1, 1601.
And then there are functions like
File­Time­To­System­Time
which also reject
FILETIME
values greater than
0x7FFFFFFF`FFFFFFFF
. So you’re probably best off not going above
0x7FFFFFFF`FFFFFFFF
.
But wait, you may also want to be concerned about code that does time zone adjustments or things like “One day later”. If you give them the value at the extreme end of the range, the adjustment may trigger an overflow into a negative value. Is that okay? I mean, you did try to go beyond the maximum value. It sort of depends on what you’re using this sentinel value for.
Interestingly, you can ask
File­Time­To­System­Time
to convert
0x7FFFFFFF`FFFFFFFF
to a
SYSTEMTIME
, and it will give you a date in the year 30828, but if you try to convert it back,
System­Time­To­File­Time&shy
fails. It can dish it out, but it can’t take it.
The
System­Time­To­File­Time
supports dates only through the end of the year 30827. If you try to get the last millisecond of the year 30827, you will get some value, but the precise number will depend on how many leap seconds have been stored in the leap second database.
Meanwhile, the CLR
System.
DateTime
caps at the end of the year 9999. And some calendars like the ChineseLunisolarCalendar have an even lower maximum supported date. (For ChineseLunisolarCalendar, the maximum supported date is somewhere in early 2101 because
that’s as far as the tables go
.) Other programming languages will have their own limits on the range of a date.
Okay, so what value should you use?
It depends on what you’re using it for.
If you need a number that simply compares larger than any other value when compared with
Compare­File­Time
, you can use
0xFFFFFFFF`FFFFFFFF
, which is the largest value supported by
Compare­File­Time
.
However, you shouldn’t let that value escape your code that understands the value’s special sentinel meaning. If you let that very large value escape, then somebody might do a time zone conversion or say “Great, let me set an alarm for 1 day later,” or try to convert it to a C#
System.
Date­Time
and encounter an overflow.
if you need a special value for use outside your code, you should find some other way of specifying that special value, like as a
std::optional
for C++ or a
Nullable<DateTime>
for C#. That way, each consumer can map the result to something appropriate for their specific language.
