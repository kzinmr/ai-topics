---
title: "Matrix Rearrangements - solving a problem with APL."
url: "https://iczelia.net/posts/matrix-rearrangements/"
fetched_at: 2026-05-05T07:01:22.948442+00:00
source: "Kamila Szewczyk (iczelia)"
tags: [blog, raw]
---

# Matrix Rearrangements - solving a problem with APL.

Source: https://iczelia.net/posts/matrix-rearrangements/

Introduction
⌗
I’ve faced the problem described in this article around a year ago. I decided that nowadays, richer in experience I’ve acquired across the year, I can take a second attempt at this problem. This time, I decided to use APL since it felt like the perfect fit for some linear algebra to me.
Originally, the challenge statement demanded transforming
N
×
M
N \times M
N
×
M
a matrix, like the one below, so that each row of it contains only one non-zero number.
[
5
1
1
0
3
4
1
4
3
4
0
0
0
0
0
]
\begin{bmatrix}
5 & 1 & 1\\
0 & 3 & 4\\
1 & 4 & 3\\
4 & 0 & 0\\
0 & 0 & 0
\end{bmatrix}
​
5
0
1
4
0
​
1
3
4
0
0
​
1
4
3
0
0
​
​
The transformation can be done by picking a number from each row, taking the other values from the columns of it and moving them to a different row. Assume the cost of moving number
N
N
N
from one row to another is equal to
N
N
N
. The goal is to transform the matrix
and
minimise the cost and returning it.
For example, the matrix on the top can be transformed so that the cost of performing this operation is
9
9
9
, as presented below:
[
5
0
0
0
3
5
1
5
3
4
0
0
0
0
0
]
\begin{bmatrix}
5 & 0 & 0\\
0 & 3 & 5\\
1 & 5 & 3\\
4 & 0 & 0\\
0 & 0 & 0
\end{bmatrix}
​
5
0
1
4
0
​
0
3
5
0
0
​
0
5
3
0
0
​
​
First, we picked the first column of the first row (and cleared all the other columns) at a price of
2
2
2
. Now, we solve the second and third row:
[
5
0
0
0
0
8
0
8
0
5
0
0
0
0
0
]
\begin{bmatrix}
5 & 0 & 0\\
0 & 0 & 8\\
0 & 8 & 0\\
5 & 0 & 0\\
0 & 0 & 0
\end{bmatrix}
​
5
0
0
5
0
​
0
0
8
0
0
​
0
8
0
0
0
​
​
The cost of rearraning the second and third columns is
7
7
7
, so the total cost is
9
9
9
and it’s the most cost-efficient solution for this matrix. Concluding,
9
9
9
is the output of our algorithm.
If you want to try solving this problem yourself, pause reading the article and make an attempt!
Initial considerations
⌗
The first thought that might come to your mind is that we can simply take the largest values in each row, then sum the rows, and then subtract the maximum from the sums, and then sum the result, as demonstrated below:
This way, we keep the largest element in each row, and move the other ones elsewhere.
It is possible that the result of this method is optimal
- we’ve just demonstrated it, but it’s not guaranteed. Let’s think for a while what’s wrong with this solution.
[
0
2
3
0
3
1
1
1
4
0
2
1
]
\begin{bmatrix}
0 & 2 & 3\\
0 & 3 & 1\\
1 & 1 & 4\\
0 & 2 & 1
\end{bmatrix}
​
0
0
1
0
​
2
3
1
2
​
3
1
4
1
​
​
According to our maximum rule, we pick accordingly
3 3 4 2
from each row. This leaves out
2 1 1 1 1
which sums to
6
6
6
. The problem with this algorithm is fairly simple - if we pick
3
from 1st row and
4
from 3rd row, and then pick
3
and
2
from the 2nd and 4th row, it appears that we don’t have where to put the
1
from the 3rd row! So this isn’t
exactly
the way to go, but it’s a good start.
I start my implementation by defining
m
and
v
based on what we worked out before. I also define a
k
boolean vector that represents whether a given column in the matrix contains non-zero values:
To proceed from here, we will find the indices of maximum values in each column. It’s fairly straightforward - the cost is the maximum minus current cell, and we select 3 rows with the smallest cost column-wise.
⍺/⍪m
duplicates the maximum vector horizontally, then we subtract the input matrix from it, but the input for
⍋
must be transposed. Then we take the desired amount of elements, and split the matrix.
Then, we take every permutation of the column indices to find the best possible rows. It’s accomplished using repeatedly applying outer product between each of the indice vectors. Finally, I ignore the permutations of row indices that have distinct elements.
If the vector we just obtained has zero elements, it’s fine to go with our
initial idea
of picking the maximum values:
Otherwise, we simply calculate new cost if given indices were chosen:
We obtain the diagonal of the input matrix given by each permutation, then subtract it from the maximums and ignore the columns that have all-zero elements in them. Then, we add everything up and pick the solution with the best score. Then we add it to our initial guess, which yields the solution.
Finally, the source code for my implementation follows:
