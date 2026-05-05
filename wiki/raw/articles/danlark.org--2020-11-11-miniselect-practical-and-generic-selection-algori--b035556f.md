---
title: "Miniselect: Practical and Generic Selection Algorithms"
url: "https://danlark.org/2020/11/11/miniselect-practical-and-generic-selection-algorithms/"
fetched_at: 2026-05-05T07:01:53.072383+00:00
source: "Daniel Kutenin (danlark)"
tags: [blog, raw]
---

# Miniselect: Practical and Generic Selection Algorithms

Source: https://danlark.org/2020/11/11/miniselect-practical-and-generic-selection-algorithms/

Today I present a big effort from my side to publish
miniselect
— generic C++ library to support multiple selection and partial sorting algorithms. It is already
used
in
ClickHouse
with huge performance benefits. Exact benchmarks and results will be later in this post and now let’s tell some stories about how it all arose. I publish this library under Boost License and any contributions are highly welcome.
It all started with sorting
While reading lots of articles, papers, and posts from Hacker News, I found it pretty funny each several months new “shiny”, “fastest”, “generic” sorting algorithms to come or remembered from old papers such as the recent paper on
learned sorting
,
Kirkpatrick-Reisch
sort or
pdqsort
. It is that we are essentially 65+ years into writing sorting algorithms, and we still find improvements. Shouldn’t sorting items be a “solved” problem by now? Unfortunately, not. New hardware features come, we find that sorting numbers can be actually done faster than best comparison
time complexity and we still find improvements in sorting algorithms like avoiding
branches in partitions
and trying to find good pivots as pdqsort does. Also, there are many open questions in that area as “what is the minimum number of comparisons needed?”.
Huge competition is still going on in sorting algorithms and I believe we are not near the optimal sorting and learned sorting looks like the next step. But it uses the fundamental fact that no one expects sorting to be completed in a couple of passes and we can understand something about data during first array passes. We will understand why it matters later.
My favorite general sorting is
pdqsort
, it proves to be currently the best general sorting algorithm and it shows a significant boost over all standard sorts that are provided in C++. It is also
used
in Rust.
Selection and Partial Sorting
Nearly a couple of months ago I started thinking about a slightly different approach when it comes to sorting — partial sorting algorithms. It means that you don’t need to sort all
elements but only find
smallest and sort them. For example, it is widely used in SQL queries when you do
ORDER BY LIMIT N
and
N
is often small, from 1-10 to ideally couple of thousands, bigger values still happen but rare. And, oh god, how little engineering and theoretical research has been done there compared to full sorting algorithms. In fact, the question of specifically finding
th order statistics when
is small is open and no good solution is presented. Also, partial sorting is quite easy to obtain after that, you need to sort the first
elements by some sorting algorithm to get optimal
comparisons and we will look at only one example when it is not the case. Yes, there are a bunch of median algorithms that can be generalized to find the
th smallest element. So, what are they? Yeah, you may know some of them but let’s revise, it is useful to know your enemies.
QuickSelect
This is almost the very first algorithm for finding the
th smallest element, just do like
QuickSort
but don’t go recursively in two directions, that’s it. Pick middle or even random element and partition by this element, see in which of two parts
is located, update the one of the borders, voila, after maximum of
partitions you will find
th smallest element. Good news that on average it takes
comparisons if we pick random pivot. That is because if we define
is the expected number of comparisons for finding
th element in
elements and
, then during one stage we do
comparisons and uniformly pick any pivot, then even if we pick the biggest part on each step
If assuming by induction that
with an obvious induction base, we get
Bad news is that the worst case will still be
if we are unfortunate and always pick the biggest element as a pivot, thus partitioning .
In that sense that algorithm provides lots of pivot “strategies” that are used nowadays, for example, picking pivot as a
element of the array or picking pivot from 3 random elements . Or do like
std::nth_element
from libcxx — choose the middle out out of
.
I decided to visualize all algorithms I am going to talk about today, so quickselect with a median of 3 strategy on random input looks something like this:
nth_element in libcxx, median of 3 strategies
And random pivot out of 3 elements works similar
Finding median in median of 3 random algorithm
For a strategy like
libcxx
(C++ llvm standard library) does, there are quadratic counterexamples that are pretty easy to detect, such patterns also appear in real data. The counterexample looks like that:
std::nth_element in libcxx for Medianof3Killer
This is definitely quadratic. By the way, this is perfectly ok with the C++ standard wording as it says:
https://eel.is/c++draft/alg.nth.element#5
Median of Medians
For a long time, computer scientists thought that it is impossible to find medians in worst-case linear time, however, Blum, Floyd, Pratt, Rivest, Tarjan came up with BFPRT algorithm or like sometimes it is called, median of medians algorithm.
Median of medians algorithm: Given array
of size
and integer
,
Group the array into
groups of size 5 and find the median of each group. (For simplicity, we will ignore integrality issues.)
Recursively, find the true median of the medians. Call this
.
Use
as a pivot to partition the array.
Recurse on the appropriate piece.
When we find the median
of
groups, at least
of them have at least 3 out of 5 elements that are smaller or equal than
, that said the biggest out of 2 partitioned chunks have size
and we have the reccurence
If we appropriately build the recurse tree we will see that
This is the geometric series with
which gives us the result
.
Actually, this constant 10 is really big. For example, if we look a bit closer,
is at least 1 because we need to partition the array, then finding median out of 5 elements cannot be done in less than 6 comparisons (can be proven by only brute-forcing) and in 6 comparisons it can be done in the following way
Use three comparisons and shuffle around the numbers so that
, and
.
If
, then the problem is fairly easy. If
, the median value is the smaller of
and
. If not, the median value is the smaller of
and
.
So
. If
, then the solution is the smaller of
and
. Otherwise, the solution is the smaller of
and
.
So that maximum
can be
and it gives us the upper bound
comparisons which looks like it can be achieved. Some other tricks can be done in place to achieve a bit lower constants like
(for example, sorting arrays of 5 and comparing less afterwards). In practice, the constant is really big and you can see it from the following demonstration which was even fastened because it took quite a few seconds:
Median of medians for random input
HeapSelect
Another approach to finding
th element is to create a
heap
on an array of size
and push other
elements into this heap. C++
std::partial_sort
works that way (with additional heap sorting of the first heap). It shows good results for very small
and random/ascending arrays, however starts to significantly degrade with growing
and becomes impractical. Best case
, worst
, average
.
std::partial_sort, two stages, first HeapSelect then heap sort of the first half, accelerated for speed
IntroSelect
As the previous algorithm is not very much practical and QuickSelect is really good on average, in 1997
“Introspective Sorting and Selection Algorithms”
from David Musser came out with a sorting algorithm called “IntroSelect”.
IntroSelect works by optimistically starting out with QuickSelect and only switching to MedianOfMedians if it recurses too many times without making sufficient progress. Simply limiting the recursion to constant depth is not good enough, since this would make the algorithm switch on all sufficiently large arrays. Musser discusses a couple of simple approaches:
Keep track of the list of sizes of the subpartitions processed so far. If at any point
recursive calls have been made without halving the list size, for some small positive
, switch to the worst-case linear algorithm.
Sum the size of all partitions generated so far. If this exceeds the list size times some small positive constant
, switch to the worst-case linear algorithm.
This algorithm came into
libstdcxx
and guess which strategy was chosen? Correct, none of them. Instead, they try
QuickSelect steps and if not successful, fallback to HeapSelect algorithm. So, worst case
, average
std::nth_element in libstdcxx, “IntroSelect”
PDQSelect
Now that most of the known algorithms come to an end 😈, we can start looking into something special and extraordinary. And the first one to look at is pdqselect which comes pretty straightforward from
pdqsort
, the algorithm is basically QuickSelect but with some interesting ideas on how to choose an appropriate pivot:
If there are
elements, use
insertion sort
to partition or even sort them. As insertion sort is really fast for a small amount of elements, it is reasonable
If it is more, choose
— pivot:
If there are less or equal than 128 elements, choose pseudomedian (or “ninther”, or median of medians which are all them same) of the following 3 groups:
begin, mid, end
begin + 1, mid – 1, end – 1
begin + 2, mid + 1, end – 2
If there are more than 128 elements, choose median of 3 from begin, mid, end
Partition the array by the chosen pivot with avoiding
branches
:
The partition is called bad if it splits less than
elements
If the total number of bad partitions exceeds
, use
std::nth_element
or any other fallback algorithm and return
Otherwise, try to defeat some patterns in the partition by (sizes are l_size and r_size respectively):
Swapping begin, begin + l_size / 4
Swapping p – 1 and p – l_size / 4
And if the number of elements is more than 128
begin + 1, begin + l_size / 4 + 1
begin + 2, begin + l_size / 4 + 2
p – 2, p – l_size / 4 + 1
p – 3, p – l_size / 4 + 2
Do the same with the right partition
Choose the right partition part and repeat like in QuickSelect
pdqselect on random input
Median Of Ninthers or Alexandrescu algorithm
For a long time, there were no practical improvements in finding
th element, and only in 2017 very well recognized among C++ community Andrei Alexandrescu published a paper on
Fast Deterministic Selection
where worst case median algorithm becomes practical and can be used in real code.
There are 2 key ideas:
We now find the pseudomedian (or ninther, or median of medians which are all the same) of 9 elements as it was done similarly in pdqsort. Use that partition when
Introduce MedianOfMinima for
. MedianOfMedians computes medians of small groups and takes their median to find a pivot approximating the median of the array. In this case, we pursue an order statistic skewed to the left, so instead of the median of each group, we compute its minimum; then, we obtain the pivot by computing the median of those groupwise minima.
is not chosen arbitrarily because in order to preserve the linearity of the algorithm we need to make sure that while recursing on
elements we partition more than
elements and thus
. MedianOfMaxima is done the same way and for
. The resulting algorithm turns out to be the following
Turns out it is a better algorithm than all above (except it did not know about pdqselect) and shows good results. My advice that if you need a deterministic worst-case linear algorithm this one is the best (we will talk about a couple of more randomized algorithms later).
QuickSelect adaptive on random data
Small k
All these algorithms are good and linear but they require lots of comparisons, like, minimum
for all
. However, I know a good algorithm for
which requires only
comparisons (I am also not going to prove it is minimal but it is). Let’s quickly revise how it works.
For finding a minimum you just compare linearly the winner with all others and basically the second place can be anyone who lost to the winner, so we need to compare them within each other. Unfortunately, the winner may have won linear number of others and we will not get the desired amount of comparisons. To mitigate this, we need to make a knockout tournament where the winner only plays
games like that:
And all we need to do next is to compare all losers to the winner
And any of them can be the second. And we use only
comparisons for that.
What can we do to find the third and other elements? Possibly not optimal in comparison count but at least not so bad can follow the strategy:
First set up a binary tree for a knockout tournament on
items. (This takes
comparisons.) The largest item is greater than
others, so it can’t be
th largest. Replace it, where it appears at an external node of the tree, by one of the
elements held in reserve, and find the largest element of the resulting
; this requires at most
comparisons because we need to recompute only one path in the tree. Repeat this operation
times in all, for each element held in reserve.
It will give us the estimation of
comparisons. Assume you need to find top 10 out of millions of long strings and this might be a good solution to this instead of comparing at least
times.
However, it requires additional memory to remember the path of the winner and I currently do not know how to remove it thus making the algorithm impractical because of allocations or additional level of indirections.
At that time my knowledge of selection algorithms ended and I decided to address one known guy.
You know him
In The Art of Computer Programming, Volume 3, Sorting and Searching I read almost 100-150 pages in order to understand what the world knows about minimal comparison sorting and selection algorithms and found a pretty interesting one called Floyd-Rivest algorithm. Actually, even Alexandrescu paper cites it but in an unusual way:
Floyd-Rivest algorithm
This algorithm is essentially the following
The general steps are:
Select a small random sample
of size
from the array.
From
, recursively select two elements,
and
, such that
(essentially they take
and
). These two elements will be the
pivots
for the partition and are expected to contain the
th smallest element of the entire list between them.
Using
and
, partition
into three sets (less, more and between).
Partition the remaining elements in
the array by comparing them to
u
or
v
and placing them into the appropriate set. If
is smaller than half the number of the elements in the array, then the remaining elements should be compared to
first and then only to
if they are smaller than
. Otherwise, the remaining elements should be compared to
first and only to
if they are greater than
.
Apply the algorithm recursively to the appropriate set to select the
th smallest in the array.
Then in 2004 it was
proven
that this method (slighly modified in bound selection) will have
comparisons with probability at least
(and the constant in the power can be tuned).
This algorithm tries to find the appropriate subsamples and proves that the
th element will be there with high probability.
Floyd-Rivest median on random data
Floyd-Rivest k=n/10 order statistics
Yet the worst case of the algorithm is still
but it tries to optimize the minimum amount of comparisons on average case, not the worst case.
For small
it is really good as it only used
comparisons which is significantly better than all “at least
comparisons” algorithms and even for median it is
which is significantly better.
What it resulted in
So I decided to code all these algorithms with the C++ standard API and to test against each other and possibly submit to something performance heavy as DBMS for ORDER BY LIMIT N clauses.
I ended up doing
miniselect
library. For now, it is header-only but I don’t guarantee that in the future, it contains almost all algorithms except the tournament one which is very hard to do in the general case.
I tested on
Intel(R) Core(TM) i5-4200H CPU @ 2.80GHz
(yeah, a bit old, sorry). We are going to find median and 1000th elements out of
and
arrays. Benchmark data:
Ascending
Descending
Median3Killer which I described above
PipeOrgan: half of the values are ascending, the other half is descending
PushFront: ascending but the smallest element added to the end
PushMiddle: ascending but the middle element added to the end
Random
Random01: random only with values 0 and 1
Shuffled16: random only with 16 overall values
You can see other values also
here
.
As you see, Floyd-Rivest outperforms in time all other algorithms and even Alexandrescu in most of the cases. One downside is that Floyd-Rivest performs worse on data where there are many equal elements, that is expected and probably can be fixed as it is pointed out in
Kiwiel’s paper
.
Real World
This effort also resulted in a
patch
to
ClickHouse
where we got the following
benchmarks
:
Time in the first columns in seconds
As you see, most of the queries have ORDER BY LIMIT N. Topmost queries were significantly optimized because
std::partial_sort
works worst when the data is descending, real-world usage as you can see in string_sort benchmarks was optimized by 10-15%. Also, there were many queries that have been optimized by 5% where sorting is not the bottleneck but still, it is nice. It ended up with a
2.5%
overall performance boost across all queries.
Other algorithms showed worse performance and you can see it from the benchmarks above. So, now Floyd-Rivest is used in production, and for a good reason. But, of course, it does not diminish the results of Mr. Alexandrescu and his contributions are very valuable when it comes to determinism and worst case.
Library
I publish
miniselect
under Boost License for everybody to use and adjust to the projects. I spent several days in the last week trying to make it work everywhere (except Windows for now but it should be good). We support C++11 and further with GCC 7+ and Clang 6+. We carefully test the algorithms for standard compliance, with fuzzing, sanitizers, etc. Fuzzing managed to find bugs that I thought only at the last moment so it really helps.
If you want to use it, please read the API but it should be an easy
sed
/
perl
/
regex
replacement with zero issues except for the ties between elements might resolve in a different way, however, C++ standard says it is ok and you should not rely on that.
Any contributions and other algorithms that I might miss are highly welcome, I intend to get this library as a reference to many implementations of selection algorithms so that the users can try and choose the best options for them. (Should I do the same for sorting algorithms?)
Conclusion
This was a long story of me trying to find the solutions to the problems that were puzzling me for the past month or so. I probably read 300+ pages of math/algorithms/discussions/forums to finally find everything that the world knows about it and to make it work for real-world applications with huge performance benefits. I think I can come up with something better in a long term after researching this stuff for a while longer but I will let you know in this blog if anything arises 🙂
References I find useful (together with zero mentions in the post)
Selection Algorithms with Small Groups
where the Median of Medians algorithms are a little bit twisted for groups of size 3 and 4 with linear time worst-case guarantee
Understandable proof of second biggest element
minimum comparisons bound
On Floyd and Rivest’s SELECT algorithm
by Krzysztof C. Kiwiel
The Art of Computer Programming, Volume 3, Sorting and Searching, Chapter about Minimum-Comparison Sorting and Selection
Original Floyd-Rivest paper
Simple proof
of a bit worse bound for Floyd-Rivest algorithm by Sam Buss
Fast Deterministic Selection
by Andrei Alexandrescu
An efficient algorithm for the approximate median selection problem
by S. Battiato, D. Cantone, D. Catalano and G. Cincotti
An efficient implementation of Blum, Floyd, Pratt, Rivest, and Tarjan’s worst-case linear selection algorithm
Selection from read-only memory and sorting with minimum data movement
by J. Ian Munro, Venkatesh Raman
