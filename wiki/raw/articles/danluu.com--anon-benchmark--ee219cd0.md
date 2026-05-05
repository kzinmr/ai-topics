---
title: "That time Oracle tried to have a professor fired for benchmarking their database"
url: "https://danluu.com/anon-benchmark/"
fetched_at: 2026-05-05T07:01:35.088362+00:00
source: "Dan Luu"
tags: [blog, raw]
---

# That time Oracle tried to have a professor fired for benchmarking their database

Source: https://danluu.com/anon-benchmark/

In 1983, at the University of Wisconsin, Dina Bitton, David DeWitt, and Carolyn Turbyfill created a
database benchmarking framework
. Some of their results included (lower is better):
Join without indices
system
joinAselB
joinABprime
joinCselAselB
U-INGRES
10.2
9.6
9.4
C-INGRES
1.8
2.6
2.1
ORACLE
> 300
> 300
> 300
IDMnodac
> 300
> 300
> 300
IDMdac
> 300
> 300
> 300
DIRECT
10.2
9.5
5.6
SQL/DS
2.2
2.2
2.1
Join with indices, primary (clustered) index
system
joinAselB
joinABprime
joinCselAselB
U-INGRES
2.11
1.66
9.07
C-INGRES
0.9
1.71
1.07
ORACLE
7.94
7.22
13.78
IDMnodac
0.52
0.59
0.74
IDMdac
0.39
0.46
0.58
DIRECT
10.21
9.47
5.62
SQL/DS
0.92
1.08
1.33
Join with indicies, secondary (non-clustered) index
system
joinAselB
joinABprime
joinCselAselB
U-INGRES
4.49
3.24
10.55
C-INGRES
1.97
1.80
2.41
ORACLE
8.52
9.39
18.85
IDMnodac
1.41
0.81
1.81
IDMdac
1.19
0.59
1.47
DIRECT
10.21
9.47
5.62
SQL/DS
1.62
1.4
2.66
Projection (duplicate tuples removed)
system
100/10000
1000/10000
U-INGRES
64.6
236.8
C-INGRES
26.4
132.0
ORACLE
828.5
199.8
IDMnodac
29.3
122.2
IDMdac
22.3
68.1
DIRECT
2068.0
58.0
SQL/DS
28.8
28.0
Aggregate without indicies
system
MIN scalar
MIN agg fn 100 parts
SUM agg fun 100 parts
U-INGRES
40.2
176.7
174.2
C-INGRES
34.0
495.0
484.4
ORACLE
145.8
1449.2
1487.5
IDMnodac
32.0
65.0
67.5
IDMdac
21.2
38.2
38.2
DIRECT
41.0
227.0
229.5
SQL/DS
19.8
22.5
23.5
Aggregate with indicies
system
MIN scalar
MIN agg fn 100 parts
SUM agg fun 100 parts
U-INGRES
41.2
186.5
182.2
C-INGRES
37.2
242.2
254.0
ORACLE
160.5
1470.2
1446.5
IDMnodac
27.0
65.0
66.8
IDMdac
21.2
38.0
38.0
DIRECT
41.0
227.0
229.5
SQL/DS
8.5
22.8
23.8
Selection without indicies
system
100/10000
1000/10000
U-INGRES
53.2
64.4
C-INGRES
38.4
53.9
ORACLE
194.2
230.6
IDMnodac
31.7
33.4
IDMdac
21.6
23.6
DIRECT
43.0
46.0
SQL/DS
15.1
38.1
Selection with indicies
system
100/10000 clustered
100/10000 clustered
100/10000
1000/10000
U-INGRES
7.7
27.8
59.2
78.9
C-INGRES
3.9
18.9
11.4
54.3
ORACLE
16.3
130.0
17.3
129.2
IDMnodac
2.0
9.9
3.8
27.6
IDMdac
1.5
8.7
3.3
23.7
DIRECT
43.0
46.0
43.0
46.0
SQL/DS
3.2
27.5
12.3
39.2
In case you're familiar with the database universe as of 1983, at the time,
INGRES
was a research project by Stonebreaker and Wong at Berkeley that had been commercialized.
C-INGRES
is the commercial versionn and
U-INGRES
is the university version.
IDM*
are the
IDM/500
database machine, the first widely used commercial database machine;
dac
is with a "database accelerator" and
nodac
is without.
DIRECT
was a research project in database machines that was started by DeWitt in 1977.
In Bitton et al.'s work, Oracle's performance stood out as unusually poor.
Larry Ellison wasn't happy with the results and it's said that he
tried to have
DeWitt fired
. Given how difficult it is to fire professors when there's actual misconduct, the probability of Ellison sucessfully getting someone fired for doing legitimate research in their field was pretty much zero. It's also said that, after DeWitt's non-firing, Larry banned Oracle from hiring Wisconsin grads and Oracle added a term to their EULA forbidding the publication of benchmarks. Over the years, many major commercial database vendors added a license clause that made benchmarking their database illegal.
Today, Oracle hires from Wisconsin, but Oracle still forbids benchmarking of their database. Oracle's shockingly poor performance and Larry Ellison's response have gone down in history; anti-benchmarking clauses are now often known as "DeWitt Clauses", and they've spread from databases to all software, from
compilers
to cloud offerings.
Meanwhile, Bitcoin users have created
anonymous markets for assassinations
-- users can put money into a pot that gets paid out to the assassin who kills a particular target.
Anonymous assassination markets appear to be a joke, but how about anonymous markets for benchmarks? People who want to know what kind of performance a database offers under a certain workload puts money into a pot that gets paid out to whoever runs the benchmark.
With things as they are now, you often see comments and blog posts about how someone was using
postgres
until management made them switch to "some commercial database" which had much worse performance and it's hard to tell if the terrible database was Oracle, MS SQL server, or perhaps another database.
If we look at major commercial databases today, two out of the three big names in commericial databases forbid publishing benchmarks. Microsoft's SQL server eula says:
You may not disclose the results of any benchmark test ... without Microsoft’s prior written approval
Oracle says:
You may not disclose results of any Program benchmark tests without Oracle’s prior consent
IBM is notable for actually allowing benchmarks:
Licensee may disclose the results of any benchmark test of the Program or its subcomponents to any third party provided that Licensee (A) publicly discloses the complete methodology used in the benchmark test (for example, hardware and software setup, installation procedure and configuration files), (B) performs Licensee's benchmark testing running the Program in its Specified Operating Environment using the latest applicable updates, patches and fixes available for the Program from IBM or third parties that provide IBM products ("Third Parties"), and (C) follows any and all performance tuning and "best practices" guidance available in the Program's documentation and on IBM's support web sites for the Program...
This gives people ammunition for a meta-argument that IBM probably delivers better performance than either Oracle or Microsoft, since they're the only company that's not scared of people publishing benchmark results, but it would be nice if we had actual numbers.
Thanks to Leah Hanson and Nathan Wailes for comments/corrections/discussion.
