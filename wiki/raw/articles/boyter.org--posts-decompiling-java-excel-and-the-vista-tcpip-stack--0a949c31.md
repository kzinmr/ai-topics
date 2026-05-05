---
title: "Decompiling Java, Excel and the Vista TCP/IP stack"
url: "https://boyter.org/posts/decompiling-java-excel-and-the-vista-tcpip-stack/"
fetched_at: 2026-05-05T07:01:56.566462+00:00
source: "Ben Boyter"
tags: [blog, raw]
---

# Decompiling Java, Excel and the Vista TCP/IP stack

Source: https://boyter.org/posts/decompiling-java-excel-and-the-vista-tcpip-stack/

Working for a large corporate company as a mid level developer is generally rather boring. Churn out some CRUD applications. Write ETL as businesses live on data (usually processed in excel). Meetings that are meant to resolve things but just result in more meetings.
So in short, it is usually boring. However occasionally you get some sort of interesting problem, especially if you gain a reputation for actually solving them.
One of the more interesting ones I got to work on was in 2008. Someone in the past had written some of the most advanced excel spreadsheets I have ever seen. The way they worked was through a lot of custom VBA code which would call over the network to some Java servlet service, which would then query a collection of Oracle database tables. The results would be returned to custom sheets, which would auto populate dropdowns and give a very controlled data experience inside excel. You could then modify the data and click a button to have that sync back into the tables.
Users loved it. It provided a modern application experience, with data validation, while also allowing all the usual excel perks, so you could click and drag to copy values, or do formulas and such. Compared to the best that the web could do at the time it was amazing.
The VBA code itself was a bit of a beast including its own XML parser (that’s a story for another post) but fairly straightforward to maintain.
The problem was that this system worked perfectly on Windows XP which was the standard OS at the time but refused to sync when run on Vista. At the time I was working in a small team to determine what applications needed to be modified to support Vista. When this came up it was a bit of a shock. Lots of break points inside the VBA code narrowed the problem down to some difference when talking to the Java servlet.
Further inspection through wireshark showed that when talking to the JSP, Windows Vista would include the content type in the headers for the first request. So
text/html; charset=utf-8
where XP would not include the
charset=utf-8
portion although I think it was actually set to
xml/text
and not
text/html
. At the time one of the big things about Vista was that it included a new TCP/IP stack which replaced the BSD based one in Windows XP. It looked like this was the cause of this change, although I don’t know if it was the TCP/IP stack or something else inside Windows.
At this point it looked like a problem to be solved in the servlet. The new behaviour from Vista was correct, and it was not likely we could get Microsoft to change it back just for us. However the source code for this had been long lost, and even more annoyingly the bug appeared to be in a dependent JAR that the code was using which was proprietary.
The solution to this was to use the Java decompiler
JAD
. We decompiled the code, and sure enough could see it was doing an explicit match on the content type which meant that with
; charset=utf-8
set nothing would run. To fix it we wrote a bunch of mock code around the single class in question allowing us to first compile the class, since we couldn’t compile the whole thing for one reason or another. A few lines of code were added to resolve the bug. From memory we just replaced the
; charset=utf-8
with nothing in the header.  We then compiled using the same Java version as the original JAR which was 1.3, and then copied the class file into the JAR replacing the existing file and deployed the modified JAR on the server. This resolved the bug, allowing the spreadheets to work again and also unblocked greater Vista deployment. Vista itself was never actually deployed and the company jumped it to Windows 7 instead, which also exhibited the same header behaviour.
That was certainly a fun few weeks, and one I look back on very fondly. I got to learn a lot during the process and work with some fantastic mentors who were able to show me how to do such amazing things in excel, how to use wireshark and a lot of other debugging tips and tricks. It also taught me that even in the most boring of roles you can find really interesting problems if you look hard enough.
