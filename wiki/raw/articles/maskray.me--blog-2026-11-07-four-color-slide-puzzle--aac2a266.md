---
title: "MaskRay • 四色滑道：从博物馆的益智玩具到一道OI题"
url: "https://maskray.me/blog/2026-11-07-four-color-slide-puzzle"
fetched_at: 2026-11-08T10:01:04.575909+00:00
source: "Fangrui Song (MaskRay)"
tags: [blog, raw]
---

# MaskRay • 四色滑道：从博物馆的益智玩具到一道OI题

Source: https://maskray.me/blog/2026-11-07-four-color-slide-puzzle

Palo Alto Junior Museum and Zoo的室内科学展区(Indoor science exhibits)墙上挂着一块大号的Montessori Slide Puzzle：下方是四条竖直滑槽，每条槽里叠着四颗彩色圆柱珠子；上方的卡片给出目标图案，玩家要通过滑动珠子把下面摆成卡片上的样子。
本文把它抽象成一道OI题，并给出题解和标准程序。
我只拍了两张照片，问了一句「能否根据这个益智玩具设计一道OI算法题？涉及编号时，从 0 开始。提供题解和C++标准程序」。
下面的题面、题解、标程、对拍程序，连同数据范围的取舍，都是Opus 5.5根据照片生成的，这篇文章也是它写的。
它自己从照片里读出了槽、木舌和滑道的结构，写暴力程序对拍，实测连通块大小来确定数据范围，还发现了「底层冻结」这个不变量。我大受震撼。
玩具
已经摆好的状态
上图是摆好的状态，与卡片一致。
相邻两条槽之间是固定的木舌，木舌顶端可以搁一颗珠子；所有槽的顶上由一条只有一颗珠子高的横向滑道连通。
下图中，三颗珠子分别从槽 1、2、3 被推上滑道，停在三根木舌顶上。
三颗珠子停在木舌顶上
木舌顶上的珠子会挡住滑道：此时槽之间无法互相传递珠子，只能把它们放回槽中。
这个「挡路」的性质让题目有了意思。
题目
下文编号均从 0 开始。
一块益智板上有
n
条竖槽，编号
0..n-1
，每条槽最多叠放
h
颗珠子（从槽底往上紧密叠放）。
相邻的槽
j
与
j+1
之间有一个
台阶
j
，最多放一颗珠子。
所有槽和台阶的上方由一条横向滑道相连，从左到右依次为：槽 0、台阶 0、槽 1、台阶 1、……、台阶
n-2
、槽
n-1
。
每次操作可以拿起
某条槽最上面的珠子
或
某个台阶上的珠子
，沿滑道左右移动，放到另一处
空台阶
或
未满的槽
中（落在槽的最上方）。
移动途中不能越过有珠子的台阶，但可以越过任何槽。
珠子有
R
、
G
、
B
、
Y
四种颜色，同色珠子没有区别。给定初始状态和目标状态，求最少操作次数；若无法达到，输出
-1
。
输入格式
：第一行两个整数
n h
。接下来依次给出初始状态和目标状态，每个状态占
h+1
行：
第一行是长度为
n-1
的字符串，第
j
个字符表示台阶
j
；
接下来
h
行，每行长度为
n
，
从上到下
描述各槽，第
i
列对应槽
i
。
.
表示空位。保证同一列中
.
只出现在珠子上方。
数据范围
：
2 <= n <= 4
，
1 <= h <= 4
，两个状态中的珠子数都恰好为
n*h
。时间限制 2 s，内存限制 256 MiB。
样例 0 就是上面第二张照片的局面，目标是卡片上的图案：
4 4
RGG
R...
BYRY
YGBR
YBGB
...
RRGG
BYRY
YGBR
YBGB
答案是 3：依次把台阶 0、1、2 上的珠子放入槽 1、2、3。
样例 1，两条槽都是满的，唯一能做的事是把某条槽顶的珠子放到台阶 0 上；此后台阶被占，两条槽不再连通，答案是
-1
：
2 2
.
RG
BY
.
GR
BY
样例 2，从一个打乱的局面摆回卡片，答案是 16：
4 4
...
GRGR
YBYR
YGBR
YBGB
...
RRGG
BYRY
YGBR
YBGB
题解
建模
一个状态由每条槽自底向上的颜色序列和每个台阶的内容组成。
操作是可逆的：把珠子从
a
移到
b
之后，
a
一定能再接收这颗珠子（槽刚少了一颗，或台阶刚被腾空），而
a
、
b
之间的台阶和移动前一样全空。
所以状态图是无向图，答案就是最短路，用 BFS 求解。
把滑道位置记为
0..2n-2
：槽
i
在
2i
，台阶
j
在
2j+1
。
枚举后继时，对每个可取珠子的位置
a
向左、向右扫描：遇到空台阶就生成一个后继并继续，遇到有珠子的台阶就停止；遇到未满的槽就生成一个后继，无论满不满都继续。每个状态有
O(n^2)
个后继。
状态压缩
每条槽用 11 位：低 3 位存珠子个数，之后每颗珠子 2 位（
h <= 4
时至多 8 位）；每个台阶 3 位（0 表示空，1~4 表示颜色）。
n <= 4
时总共不超过
4*11 + 3*3 = 53
位，可以放进一个
unsigned long long
。
底层冻结
考察槽
i
自底向上第
k
颗珠子（从 0 开始）。它要移动，必须先成为槽顶，此时槽
i
恰有
k+1
颗珠子。
槽
i
之外有
(n-1)*h
个槽位和
n-1
个台阶，放着其余
n*h-k-1
颗珠子，空位数为
(n-1)(h+1) - (n*h-k-1) = n - h + k
这颗珠子要移走，槽外至少要有一个空位，即
k >= h-n+1
。因此：
每条槽最底下的
max(0, h-n+1)
层珠子永远不会移动。
若两个状态的冻结层不同，可以直接输出
-1
。
n = h = 4
时最底一行冻结，
4×4
就退化成了
4×3
；实测两者的连通块大小都是 1587600 个状态。
不过这只是必要条件：
4×3
没有冻结层，随机生成的两个颜色组成相同的状态仍然大多不连通，所以还是要搜索。
双向 BFS
单向 BFS 已经足够：最大连通块约 160 万个状态。标程用双向 BFS，每次扩展当前队列较小的一侧，有解时几乎瞬间出答案。
正确性：设两侧已分别搜完距离
<= a
与
<= b
的全部状态，且没有公共状态。
若最短距离
D <= a+b
，最短路上距起点
min(a, D)
的那个点必然同时出现在两侧，矛盾，所以
D >= a+b+1
。
扩展起点一侧的第
a+1
层时，一旦新状态
y
已在另一侧出现，就得到一条长
a+1+dist2(y) <= a+b+1
的路径，它不可能短于
D
，所以恰好等于
D
。
因此
第一次相遇即可返回
。若某一侧队列搜空仍未相遇，说明它所在的连通块不含另一端，输出
-1
。
最坏情况是无解：两侧都要把各自的连通块搜完。标程用开放寻址哈希表，颜色均衡且无解的
4×3
、
4×4
数据实测最慢约 0.9 s、86 MB。
为什么珠子数恰好是
n*h
只要少放一颗珠子，空位就会变多，连通块急剧膨胀：
n×h
珠子数
连通块大小
4×3
12
1587600
4×3
11
11550000
4×4
16
1587600
4×4
15
> 20000000
关于实物
由底层冻结，若实物每槽恰好只能放 4 颗，底行就永远无法改变：要么所有卡片的底行都相同，要么槽其实还能多放一颗。
照片中第一列装满 4 颗后上方仍有空隙，更像是后者（
h = 5
，仍是 16 颗珠子）。
我按
h = 5
试过：空位从 3 个增加到 7 个，状态数约 10
10
，随机两张卡片之间的最少步数通常在 21~29 之间。
双向 BFS 和以「必须移动的珠子数」为估价的 A* 都要数十秒、数 GB 内存。
所以题目把珠子数固定为
n*h
。若想贴合实物规模，可以改成构造题：只要求输出一个步数不超过某个上界的方案，用 Special Judge 判定。
标准程序
用暴力程序（字符串存状态、单向 BFS）对拍了 600 组随机数据，结果一致。
// 四色滑道 —— 标准程序：双向 BFS
#include
<bits/stdc++.h>
using namespace
std
;
typedef unsigned long long
u64;
int
n, h;
// 状态：每个槽 11 位（3 位个数 + 4×2 位颜色，自底向上），每个台阶 3 位（0 空，1..4 颜色）
struct
State
{
int
cnt[
4
], col[
4
][
4
], shelf[
3
];
};
u64 encode
(
const
State
&
s
) {
u64
c
=
0
;
for
(
int
i
=
0
; i
<
n; i
++
) {
u64
v
=
s.cnt[i];
for
(
int
k
=
0
; k
<
s.cnt[i]; k
++
) v
|=
(u64)s.col[i][k]
<<
(
3
+
2
*
k);
c
=
c
<<
11
|
v;
}
for
(
int
j
=
0
; j
+
1
<
n; j
++
) c
=
c
<<
3
|
s.shelf[j];
return
c;
}
State decode
(
u64
c
) {
State
s;
for
(
int
j
=
n
-
2
; j
>=
0
; j
--
) s.shelf[j]
=
c
&
7
, c
>>=
3
;
for
(
int
i
=
n
-
1
; i
>=
0
; i
--
) {
u64
v
=
c
&
2047
; c
>>=
11
;
s.cnt[i]
=
v
&
7
;
for
(
int
k
=
0
; k
<
s.cnt[i]; k
++
) s.col[i][k]
=
v
>>
(
3
+
2
*
k)
&
3
;
}
return
s;
}
// 滑道上的位置：槽 i 在 2i，台阶 j 在 2j+1
template
<
class
F
>
void
forEachNext
(
u64
code
,
F
f
) {
State
s
=
decode
(code);
int
m
=
2
*
n
-
1
;
for
(
int
a
=
0
; a
<
m; a
++
) {
int
piece;
// 取出的珠子颜色（台阶编码，即颜色+1）
if
(a
%
2
==
0
) {
if
(
!
s.cnt[a
/
2
])
continue
;
piece
=
s.col[a
/
2
][
--
s.cnt[a
/
2
]]
+
1
;
}
else
{
if
(
!
s.shelf[a
/
2
])
continue
;
piece
=
s.shelf[a
/
2
], s.shelf[a
/
2
]
=
0
;
}
for
(
int
dir
= -
1
; dir
<=
1
; dir
+=
2
)
for
(
int
b
=
a
+
dir; b
>=
0
&&
b
<
m; b
+=
dir) {
if
(b
%
2
==
1
) {
// 台阶：空则可停，非空则挡路
if
(s.shelf[b
/
2
])
break
;
s.shelf[b
/
2
]
=
piece;
f
(
encode
(s)); s.shelf[b
/
2
]
=
0
;
}
else if
(s.cnt[b
/
2
]
<
h) {
// 槽：未满则可落入，满了也能越过
int
i
=
b
/
2
;
s.col[i][s.cnt[i]
++
]
=
piece
-
1
;
f
(
encode
(s)); s.cnt[i]
--
;
}
}
if
(a
%
2
==
0
) s.cnt[a
/
2
]
++
;
else
s.shelf[a
/
2
]
=
piece;
}
}
int
colorId
(
char
ch
) {
return
string
(
"RGBY"
).
find
(ch); }
u64 readState
() {
State
s;
string
line;
cin
>>
line;
for
(
int
j
=
0
; j
+
1
<
n; j
++
) s.shelf[j]
=
line[j]
==
'.'
?
0
:
colorId
(line[j])
+
1
;
vector
<
string
>
g
(h);
for
(
auto &
r : g) cin
>>
r;
for
(
int
i
=
0
; i
<
n; i
++
) {
s.cnt[i]
=
0
;
for
(
int
r
=
h
-
1
; r
>=
0
&&
g[r][i]
!=
'.'
; r
--
) s.col[i][s.cnt[i]
++
]
=
colorId
(g[r][i]);
}
return
encode
(s);
}
// 开放寻址哈希表：键为状态编码（编码不为 ~0），值为步数
struct
HashMap
{
static constexpr
u64 EMPTY
= ~
0
ULL
;
vector
<
u64
> key;
vector
<
unsigned char
> val;
size_t
mask, used
=
0
;
HashMap
() :
key
(
1
<<
16
, EMPTY),
val
(
1
<<
16
),
mask
((
1
<<
16
)
-
1
) {}
static size_t
hsh
(
u64
x
) { x
^=
x
>>
31
; x
*= 0x
9E3779B97F4A7C15
ULL
;
return
x
^
(x
>>
29
); }
size_t
slot
(
u64
k
)
const
{
size_t
p
=
hsh
(k)
&
mask;
while
(key[p]
!=
EMPTY
&&
key[p]
!=
k) p
=
(p
+
1
)
&
mask;
return
p;
}
int
get
(
u64
k
)
const
{
size_t
p
=
slot
(k);
return
key[p]
==
k
?
val[p]
: -
1
; }
void
put
(
u64
k
,
int
v
) {
if
((used
+
1
)
*
2
>
key.
size
())
grow
();
size_t
p
=
slot
(k);
if
(key[p]
!=
k) key[p]
=
k, used
++
;
val[p]
=
v;
}
void
grow
() {
vector
<
u64
> ok; vector
<unsigned char>
ov;
ok.
swap
(key), ov.
swap
(val);
key.
assign
(ok.
size
()
*
2
, EMPTY), val.
assign
(ok.
size
()
*
2
,
0
);
mask
=
key.
size
()
-
1
, used
=
0
;
for
(
size_t
i
=
0
; i
<
ok.
size
(); i
++
)
if
(ok[i]
!=
EMPTY)
put
(ok[i], ov[i]);
}
};
int
main
() {
cin
>>
n
>>
h;
u64
st
=
readState
(), ed
=
readState
();
if
(st
==
ed) {
puts
(
"0"
);
return
0
; }
HashMap
dist[
2
];
vector
<
u64
> q[
2
];
dist[
0
].
put
(st,
0
), dist[
1
].
put
(ed,
0
);
q[
0
]
=
{st}, q[
1
]
=
{ed};
while
(
!
q[
0
].
empty
()
&& !
q[
1
].
empty
()) {
int
t
=
q[
0
].
size
()
<=
q[
1
].
size
()
?
0
:
1
;
// 扩展较小的一侧
vector
<
u64
> nq;
int
ans
= -
1
;
for
(
u64
x : q[t]) {
int
d
=
dist[t].
get
(x);
forEachNext
(x, [
&
](
u64
y
) {
if
(ans
>=
0
||
dist[t].
get
(y)
>=
0
)
return
;
int
e
=
dist[
!
t].
get
(y);
if
(e
>=
0
) { ans
=
d
+
1
+
e;
return
; }
// 第一次相遇即为最优
dist[t].
put
(y, d
+
1
);
nq.
push_back
(y);
});
if
(ans
>=
0
) {
printf
(
"
%d\n
"
, ans);
return
0
; }
}
q[t].
swap
(nq);
}
puts
(
"-1"
);
// 某一侧的连通块已搜完仍未相遇
}
