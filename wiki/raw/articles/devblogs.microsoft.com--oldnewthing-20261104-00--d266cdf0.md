---
title: "There are things with ranks, but it's not always clear what the ranks mean"
url: "https://devblogs.microsoft.com/oldnewthing/20261104-00/?p=112830/"
fetched_at: 2026-11-05T10:01:11.208681+00:00
source: "devblogs.microsoft.com/oldnewthing"
tags: [blog, raw]
---

# There are things with ranks, but it's not always clear what the ranks mean

Source: https://devblogs.microsoft.com/oldnewthing/20261104-00/?p=112830/

There are a number of features in Windows that establish an order by a thing called a “rank”. Unfortunately, the documentation for them doesn’t always tell you what rank actually means. Does a higher rank take priority over a lower rank?
I started with SQL Server. In the documentation page
Limit search results with RANK
, it opens by telling you that higher ranks mean better matches, or at least that lower ranks mean worse matches, which is basically the same thing:
The CONTAINSTABLE and FREETEXTTABLE functions return a column named RANK that contains ordinal values from 0 through 1,000 (rank values). These values rank the rows according to how well they match the selection criteria. The rank values indicate only a relative order of relevance of the rows in the result set,
with a lower value indicating lower relevance
. The actual values are unimportant and typically differ each time the query runs.
It says that lower ranks are poorer-quality matches, so this implies that higher quality matches have higher ranks.
This “higher is better” is made more explicitly on the the RANK of a query result is a value that increases as the match quality improves:
Query with Full-Text Search
page:
The higher the rank value of the text or document in a row, the more relevant the row is for the given full-text query.
Okay, so that’s SQL Server. Good job, SQL Server.
The Windows Package Graph also has the concept of rank. And here the documentation is less helpful.
The
rank
parameter to the
Add­Package­Dependency
function
is documented as
The rank to use to add the resolved package to the caller’s package graph. For more information, see the remarks.
If you go down to the remarks,
the only mention of rank
is
If multiple packages are present in the package graph with the same rank as the call to
Add­Package­Dependency
, the resolved package is (by default) added after others of the same rank. To add a package before others of the same rank, specify
Add­Package­Dependency­Options_
Prepend­If­Rank­Collision
for the options parameter.
That’s nice, but it doesn’t tell me whether packages are searched from low rank to high, or from high rank to low. All I know is that if I want to be considered ahead of others of the
same
rank, I should pass this special flag; otherwise by default I am considered
after
others of the same rank. But it doesn’t say whether I am considered ahead of or after other packages with
different
ranks.
There is a “For more information” that takes me to the
Using the Dynamic Dependency API
page, but the only mention of rank is
When you call this API, you must pass in the dependency ID that was returned when you created the install-time reference, and the desired rank to use for the MSIX package in the process’s package graph.
So it tells me that I have to pass a rank, but it doesn’t tell me what the rank
means
.
Okay, maybe I can get a clue from another API in the Windows App SDK: <A%20HREF=”https://learn.microsoft.com/en-us/windows/windows-app-sdk/api/winrt/microsoft.windows.widgets.providers.widgetinfo.rank?view=windows-app-sdk-2.0#:~:text=An%20integer%20specifying%20the%20relative%20rank,lower%20values.”> The
Rank
property on the
WidgetInfo
class. Let’s see what that says.
An integer specifying the relative rank of the widget. Smaller values are ranked higher than lower values.
Okay, so I learn that ranks are relative rather than absolute values. But that second sentence makes no sense: It says that smaller values are treated differently from lower values. Huh? What’s the difference between a “smaller value” and a “lower value”? And what does “higher” rank mean anyway?
Unfortunately, the
Widget sample
doesn’t use the
Rank
property, so I still don’t know.
This is just another example of the principle that “The person who understands the feature the best is often the person least qualified to explain it.” They know what the rank is. They’ve been working with ranks for months. To them, ranks are so obvious and intuitive that they don’t need an explanation.
Bonus chatter
: I contacted a colleague who works on the package graph, who explained to me how it works and also lamented how the information provided to the documentation team somehow got garbled along the way. (And put fixing it onto the backlog.)
The missing sentence is
Packages are searched in ascending rank.
In other words, at least for the package graph, lower ranks have precedence over higher ranks.
A process’s package graph is an ordered list of packages and is initially empty.
If the process has declared dependencies, then all of those packages are added to the package graph with rank zero, in the order described by
static package dependency resolution algorithm
.
Once that initial package graph is established, you can manually modify the graph by calling
Add­Package­Dependency
and
Remove­Package­Dependency
. When you add a package to the package graph, it is inserted into the graph after all the packages with lower rank and before all the packages with higher rank. By default, it also goes after all the packages with the same rank, but you can override this with
Add­Package­Dependency­Options_
Prepend­If­Rank­Collision
, which will put it in front of all the packages with the same rank.
In the package graph, the rank is a signed integer, so you can use a negative rank to go in front of the static package dependencies.
Bonus bonus chatter
: In the world of filter drivers, the applicable term is
altitude
, and the meaning
is quite clearly spelled out
:
The altitude is an infinite-precision string interpreted as a decimal number. A filter driver that has a low numerical altitude is loaded into the I/O stack below a filter driver that has a higher numerical value.
