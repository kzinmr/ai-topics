---
title: "The Great CPU Stagnation"
url: "https://databasearchitects.blogspot.com/2023/04/the-great-cpu-stagnation.html"
fetched_at: 2026-05-05T07:01:28.268771+00:00
source: "Database Architects"
tags: [blog, raw]
---

# The Great CPU Stagnation

Source: https://databasearchitects.blogspot.com/2023/04/the-great-cpu-stagnation.html

For at least five decades,
Moore's law
consistently delivered increasing numbers of transistors. Equally significant,
Dennard scaling
led to each transistor using less energy, enabling higher clock frequencies. This was great, as higher clock frequencies enhanced existing software performance automatically, without necessitating any code rewrite. However, around 2005, Dennard scaling began to falter, and clock frequencies have largely
plateaued
since then.
Despite this, Moore's law continued to advance, with the additional available 
transistors being channeled into creating more cores per chip. The following graph displays the number of cores for the largest available x86 CPU at the time:
Notice the logarithmic scale: this represents the exponential trend we had become accustomed to, with core counts doubling roughly every three years. Regrettably, when considering cost per core, this impressive trend appears to have stalled, ushering in an era of CPU stagnation.
To demonstrate this stagnation, I gathered data from wikichip.org on AMD's Epyc single-socket CPU lineup, introduced in 2017 and now in its fourth generation (
Naples
,
Rome
,
Milan
,
Genoa
):
Model
Gen
Launch
Cores
GHz
IPC
Price
7351P
Naples
06/2017
16
2.4
1.00
$750
7401P
Naples
06/2017
24
2.0
1.00
$1,075
7551P
Naples
06/2017
32
2.0
1.00
$2,100
7302P
Rome
08/2019
16
3.0
1.15
$825
7402P
Rome
08/2019
24
2.8
1.15
$1,250
7502P
Rome
08/2019
32
2.5
1.15
$2,300
7702P
Rome
08/2019
64
2.0
1.15
$4,425
7313P
Milan
03/2021
16
3.0
1.37
$913
7443P
Milan
03/2021
24
2.9
1.37
$1,337
7543P
Milan
03/2021
32
2.8
1.37
$2,730
7713P
Milan
03/2021
64
2.0
1.37
$5,010
9354P
Genoa
11/2022
32
3.3
1.57
$2,730
9454P
Genoa
11/2022
48
2.8
1.57
$4,598
9554P
Genoa
11/2022
64
3.1
1.57
$7,104
9654P
Genoa
11/2022
96
2.4
1.57
$10,625
Over these past six years, AMD has emerged as the x86 performance per dollar leader. Examining these numbers should provide insight into the state of server CPUs. Let's first observe CPU cores per dollar:
This deviates significantly from the expected exponential improvement graphs.
In fact, CPU cores are becoming slightly more expensive over time! Admittedly, newer cores outperform their predecessors. When accounting for both clock frequency and higher IPC, we obtain the following image:
This isn't much better. The performance improvement over a 6-year period is underwhelming when normalized for cost.
Similar results can also be observed for
Intel CPUs in EC2
.
Lastly, let's examine transistor counts, only taking into account the logic transistors. Despite improved production nodes from 14nm (Naples) over 7nm (Rome/Milan) to 5nm (Genoa), cost-adjusted figures reveal stagnation:
In conclusion, the results are disheartening. Rapid and exponential improvements in CPU speed seem to be relics of the past. We now find ourselves in a markedly different landscape compared to the historical norm in computing. The implications could be far-reaching. For example, most software is extremely
inefficient
when compared to what hardware can theoretically achieve, and maybe this needs to change. Furthermore, historically specialized chips enjoyed only limited success due to the rapid advancement of commodity CPUs. Perhaps, custom chips will have a much bigger role in the future.
P.S. Due to popular demand, here's how the last graph looks like after adjusting for inflation:
