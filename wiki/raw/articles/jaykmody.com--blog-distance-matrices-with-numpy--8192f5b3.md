---
title: "Computing Distance Matrices with NumPy"
url: "https://jaykmody.com/blog/distance-matrices-with-numpy/"
fetched_at: 2026-05-05T07:01:47.004578+00:00
source: "Jay Mody"
tags: [blog, raw]
---

# Computing Distance Matrices with NumPy

Source: https://jaykmody.com/blog/distance-matrices-with-numpy/

Computing Distance Matrices with NumPy
April 04, 2021
Background
A
distance matrix
is a square matrix that captures the pairwise distances between a set of vectors. More formally:
Given a set of vectors \(v_1, v_2, ... v_n\) and it's distance matrix \(\text{dist}\), the element \(\text{dist}_{ij}\) in the matrix would represent the distance between \(v_i\) and \(v_j\). Notice, this means the matrix is symmetric since \(\text{dist}_{ij} = \text{dist}_{ji}\), and the dimensionality (size) of the matrix is \((n, n)\).
The above definition, however, doesn't define what
distance
means. There are
many ways to define and compute the distance between two vectors
, but usually, when speaking of the distance between vectors, we are referring to their
euclidean distance
. Euclidean distance is our intuitive notion of what distance is (i.e. shortest line between two points on a map). Mathematically, we can define euclidean distance between two vectors \(u, v\) as,
\[|| u - v ||_2 = \sqrt{\sum_{k=1}^d (u_k - v_k)^2}\]
where \(d\) is the dimensionality (size) of the vectors.
By itself, distance matrixes are already highly useful in all kinds of applications, from math, to computer science, to graph theory, to bio-informatics. Let's explore one particular application for distance matrices, machine learning.
Motivating Example: k-Nearest Neighbors
k-Nearest Neighbour
(kNN) is a machine learning classification algorithm that utilizes distance matrices under the hood. The idea is simple, we can predict the class of any given data point by looking at the classes of the \(k\) nearest neighboring labelled data points. Whichever class is most common within the neighbors is the class we predict for the data point.
How do you determine which labelled points are the "nearest"? Well, if we represent each data point as a vector, we can compute their euclidean distance.
Let's say instead of just predicting for a single point, you want to predict for multiple points. More formally, you are given \(n\) labelled data points (train data), and \(m\) unlabelled data points (test data, for which you would like to classify). The data points are represented as vectors, of dimensionality \(d\). In order to implement the kNN classifier, you'll need to compute the distances between all labelled-unlabelled pairs. These distances can be stored in an \((m, n)\) matrix \(\text{dist}\), where \(\text{dist}_{ij}\) represents the distance between the ith unlabelled point and the jth labelled point. If we represent our labelled data points by the \((n, d)\) matrix \(Y\), and our unlabelled data points by the \((m, d)\) matrix \(X\), the distance matrix can be formulated as:
\[\text{dist}_{ij} = \sqrt{\sum_{k=1}^d (X_{ik} - Y_{jk})^2}\]
This distance computation is really the meat of the algorithm, and what I'll be focusing on for this post. Let's implement it.
Note:
I use the term distance matrix here even though the matrix is no longer square (since we are computing the distances between two sets of vectors and not just one).
Three Loop
Most simple way to compute our distance matrix is to just loop over all the pairs and elements:
X # test data (m, d)
X_train # train data (n, d)

m = X.shape[0]
n = X_train.shape[0]
d = X.shape[1]
dists = np.zeros((num_test, num_train)) # distance matrix (m, n)

for i in range(m):
    for j in range(n):
        val = 0
        for k in range(d):
            val += (X[i][k] - X_train[j][k]) ** 2
        dists[i][j] = np.sqrt(val)
While this works, it's quite inefficient and doesn't take advantage of numpy's efficient vectorized operations. Let's change that.
Two Loops
for i in range(m):
    for j in range(n):
        # element-wise subtract, element-wise square, take the sum and sqrt
        dists[i][j] = np.sqrt(np.sum((X[i] - X_train[j]) ** 2))
That wasn't too bad, we even made it easier to read if you're asking me, but we can do better.
One Loop
for i in range(m):
    dists[i, :] = np.sqrt(np.sum((X[i] - X_train) ** 2, axis=1))
What the hell is going on here?! Ok let's break it down.
Firstly, shouldn't
X[i] - X_train
result in an error?
X[i]
has shape \((d)\) while
X_train
has shape \((n, d)\). Element-wise operations only work if both parties have the same shape, so what's happening here?
Numpy is automatically
broadcasting
X[i]
to match the shape of
X_train
. You can think of this as stacking
X[i]
\(n\) times to produce an \((n, d)\) matrix where each row is just a copy of
X[i]
. This way, when performing the subtraction, each row of
X_train
is being subtracted by
X[i]
(or the other way around, it doesn't matter since we'll be taking the square of the result). If you wanted, you can create the "stacked" matrix yourself in numpy using
np.tile
, but it would be
slower then if you let numpy handle it with broadcasting
. So now we have an \((n, d)\) matrix where each row is
X[i] - X_train[j]
, sick.
The next step is easy,  we perform an element-wise square. Then, we need to take the sum of each row, so we use
np.sum
with the argument
axis=1
which tells numpy to sum across the first axis (ie the rows). Without the axis argument,
np.sum
will take the sum of every element in the matrix and output a single scalar value. The result of the
np.sum
with
axis=1
gives us a vector of size \(n\).
Finally, we take the element-wise square root of this vector and store it in \(dists[i]\).
So here's a better annotated version of the code that's much easier to understand:
for i in range(m):
    # X[i] gets broadcasted (d) -> (n, d)
    # (each row is a copy of X[i])
    diffs = X[i] - X_train

    # element wise square
    squared = diffs ** 2

    # take the sum of each row (n, d) -> (n)
    sums = np.sum(squared, axis=1)

    # take the element-wise square root and store them in dists
    dists[i, :] = np.sqrt(sums)
No Loops?!
We can do even better and only use vector/matrix operations, no loops needed. How you ask? Let's take a closer look at our equation:
\[\text{dist}_{ij} = \sqrt{\sum_{k=1}^d (x_{ik} - y_{jk})^2}\]
What happens if we expand out the expression in the sum?
\[
\text{dist}_{ij} = \sqrt{\sum_{k=1}^d x^2_{ik} - 2x_{ik}y_{jk} + y^2_{jk}}\\
\]
Interesting, let's distribute the sum:
\[
\text{dist}_{ij} = \sqrt{\sum_{k=1}^d x^2_{ik} - 2 \sum_{k=1}^d x_{ik}y_{jk} + \sum_{k=1}^dy^2_{jk}}\\
\]
You'll notice that each of these sums are just dot products, so let's replace the ugly notation and get a much cleaner expression:
\[
\text{dist}_{ij} = \sqrt{x_i \cdot x_i - 2x_i \cdot y_j + y_j \cdot y_j}\\
\]
Notice, for all combinations of \(i, j\), the middle term is unique, but the left and right terms are repeated. Imagine fixing either \(i\) or \(j\) and iterate the other variable, you'll see that \(x_i \cdot x_i\) shows up \(j\) times and \(y_j \cdot y_j\) shows up \(i\) times. So, our challenge is to figure out how to compute all possible \(x_i \cdot x_i\), \(x_i \cdot y_j\), and  \(y_j \cdot y_j\), and then add them together in the right way. All of this without loops. Let's try it:
# this has the same affect as taking the dot product of each row with itself
x2 = np.sum(X**2, axis=1) # shape of (m)
y2 = np.sum(X_train**2, axis=1) # shape of (n)

# we can compute all x_i * y_j and store it in a matrix at xy[i][j] by
# taking the matrix multiplication between X and X_train transpose
# if you're stuggling to understand this, draw out the matrices and
# do the matrix multiplication by hand
# (m, d) x (d, n) -> (m, n)
xy = np.matmul(X, X_train.T)

# each row in xy needs to be added with x2[i]
# each column of xy needs to be added with y2[j]
# to get everything to play well, we'll need to reshape
# x2 from (m) -> (m, 1), numpy will handle the rest of the broadcasting for us
# see: https://numpy.org/doc/stable/user/basics.broadcasting.html
x2 = x2.reshape(-1, 1)
dists = np.sqrt(x2 - 2*xy + y2) # (m, 1) repeat columnwise + (m, n) + (n) repeat rowwise -> (m, n)
-1 Loops?!!?! 🤔
from sklearn.neighbors import KNeighborsClassifier
Speed Comparison
To test the speed of each implementation, we can run it against a small subset of the cifar-10 dataset as seen in the
cs231n assignment 1 knn notebook
:
Two loop version took 39.707250 seconds
One loop version took 28.705156 seconds
No loop version took 0.218127 seconds
Clearly, we can see the no loop version is the winner, beating out both the two loop and one loop implementations by orders of magnitudes. Notice, I didn't include the three loop implementation because that would have taken hours to run! On just
10
training and
10
test examples, the three loop implementation took
0.5
seconds. For reference, the above time profiles are for
5000
training and
500
test examples, yikes! +1 for vector operations!
