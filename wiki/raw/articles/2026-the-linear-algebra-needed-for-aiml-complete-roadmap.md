---
title: "The Linear Algebra Needed For AI/ML (Complete Roadmap)"
created: 
author_id: ""
tweet_id: "2047362720199274713"
source: x_article
---

# The Linear Algebra Needed For AI/ML (Complete Roadmap)

You don’t need a math PhD to do AI/ML. You just need enough linear algebra to stop feeling lost when you open a paper or a PyTorch doc. This roadmap covers exactly what to learn, in the right order, and why it matters.

Let’s get into it.
 
Why Linear Algebra at All?
Before we start listing topics, let me explain why this subject matters so much in ML.
Everything in machine learning is numbers. Images are grids of numbers. Text becomes numbers after tokenization. Audio is a list of numbers sampled over time. Once you turn all your data into numbers, you need a way to:
Store these numbers efficiently
Do fast operations on them
Transform them from one form to another
Linear algebra is literally the language we use to do all three. Neural networks? They are just matrix multiplications with some non-linear functions sprinkled in. Principal Component Analysis? Eigenvectors. Recommendation systems? Matrix factorization. Word embeddings? Vectors in high dimensions.
You cannot escape it. But you can understand it. Let's go.
 
Phase 1: The Absolute Basics
This is where everyone should start, even if you think you know this stuff. Trust me, come back and revise.
1. Scalars, Vectors, Matrices, Tensors
 
Start here. Understand the hierarchy.
A scalar is just one number. Like 5 or 3.14.
A vector is a list of numbers. Like [2, 4, 7].
A matrix is a 2D grid of numbers, basically rows and columns.
A tensor is the general version. It can be 3D, 4D, or more. Image batches in deep learning are usually 4D tensors (batch, channel, height, width).
Why this matters: every PyTorch or TensorFlow program you write will use these. If you do not know the shape of your data, you will spend hours debugging.
2. Vector Operations
Learn how to:
Add two vectors
Multiply a vector by a scalar
Find the length (also called the magnitude or norm) of a vector
Understand the geometric meaning, meaning vectors point somewhere in space
The norm concept will come back again and again. L1 norm, L2 norm, these are used in regularization and loss functions.
3. Dot Product
This one is huge. The dot product tells you how similar two vectors are. It is the foundation of cosine similarity, which is used everywhere from search engines to recommender systems to attention in transformers.
Practice until you can compute a dot product in your sleep.
4. Matrix Operations
Matrix addition
Scalar multiplication on a matrix
Matrix multiplication (the big one)
Transpose of a matrix
Matrix multiplication is NOT element-wise multiplication. This confuses so many beginners. Spend extra time here. Understand why the dimensions need to match (the inner dimensions must agree, like (m x n) times (n x p) gives (m x p)).
 
Phase 2: Building Blocks You Will Actually Use
Now we get into stuff that shows up in actual ML code.
5. Special Matrices
Know these by name:
Identity matrix: the matrix equivalent of the number 1
Diagonal matrix: only the diagonal has values, rest are zeros
Symmetric matrix: equal to its own transpose
Orthogonal matrix: its transpose is its inverse
You will see these pop up in covariance matrices, attention masks, and rotation operations.
6. Matrix Inverse
Not every matrix has an inverse, and the ones that do not are called singular. In ML, we rarely compute inverses directly because they are slow and unstable. But understanding the concept helps you read equations in papers.
Know what the determinant is and why a zero determinant means no inverse.
7. Linear Independence and Rank
If you have a bunch of vectors, are some of them basically repeats of the others? That is what linear independence asks. The rank of a matrix tells you how many truly independent directions it has.
This matters when you do PCA or when you hear people say "the data lies on a lower dimensional manifold". Rank is the idea hiding behind that fancy sentence.
8. Span, Basis, and Subspaces
Think of a basis as the minimum set of vectors you need to describe everything in a space. Like how you only need North-South and East-West to describe any location on a map.
Understanding this helps when you get to embeddings. A word embedding of size 768 basically means each word gets placed in a 768-dimensional space using a chosen basis.
 
Phase 3: The Important Stuff for ML
Okay now we are getting to the juicy parts that actually power ML algorithms.
9. Eigenvalues and Eigenvectors
I know, scary name. But the idea is simple. When you apply a matrix to a vector, usually the vector gets stretched AND rotated. Eigenvectors are the special vectors that only get stretched, not rotated. The amount of stretching is the eigenvalue.
Why you care:
PCA (dimensionality reduction) uses eigenvectors of the covariance matrix
PageRank (the original Google algorithm) is an eigenvector problem
Spectral clustering uses eigen-decomposition
Understanding stability of neural network training involves eigenvalues of the Hessian
Spend real time on this. Watch 3Blue1Brown's videos (they are free and genuinely the best resource on the internet for this).
10. Singular Value Decomposition (SVD)
If I had to pick ONE concept that is the most important in applied linear algebra for ML, it would be SVD. It breaks any matrix (any shape, any size) into three simpler matrices.
Uses in ML:
Low rank approximation (compressing matrices)
Recommender systems (Netflix prize algorithms used this)
Noise reduction in data
Understanding LoRA in fine-tuning large language models
Pseudoinverse computation
If eigen-decomposition is cool, SVD is cooler because it works on every matrix, not just square ones.
11. Matrix Factorization
Related to SVD but broader. The idea is to break a big matrix into smaller matrices that when multiplied give back the original (approximately).
This is the entire basis of collaborative filtering. Also shows up in LoRA, where we approximate weight updates as the product of two smaller matrices to save memory during fine-tuning.
12. Norms Revisited
Go deeper on norms now:
L1 norm (sum of absolute values), used in Lasso regression for sparsity
L2 norm (the usual length), used in Ridge regression and weight decay
Frobenius norm for matrices
Infinity norm
Each has different properties that matter for optimization and regularization.
 
Phase 4: The Calculus-Linear-Algebra Bridge
This is where ML actually happens. Pure linear algebra alone will not train a model, but combined with calculus it becomes gradient descent.
13. Gradients and Jacobians
A gradient is the vector of partial derivatives. A Jacobian is the matrix of partial derivatives for vector valued functions. Neural network backpropagation is literally chained Jacobian-vector products.
You do not need to manually compute these (PyTorch does it for you via autograd), but you need to know what they represent.
14. Hessian Matrix
The matrix of second derivatives. Its eigenvalues tell you about the curvature of your loss landscape. Second order optimization methods (like Newton's method) use it directly. For deep learning we usually approximate it because computing the full Hessian is too expensive.
15. Chain Rule in Matrix Form
Backprop is the chain rule applied to matrices. Once you see this, neural networks stop being magic and start being just calculus on matrices.
 
Phase 5: Advanced Topics (Only When Needed)
Do not stress about these until you actually run into them. But knowing they exist helps.
16. Tensor Operations
Broadcasting (how NumPy and PyTorch handle shape mismatches)
Einstein summation (einsum), once you learn this you will write cleaner code
Contractions and reshapes
Einsum is honestly a superpower. Learn it.
17. Matrix Calculus Identities
There are some standard identities for differentiating common matrix expressions. Keep a cheat sheet. The Matrix Cookbook (a free PDF online) is the classic reference.
18. Positive Definite Matrices
Matrices where x^T Ax > 0 for all non-zero x. Show up in:
Covariance matrices (always positive semi-definite)
Gaussian processes
Convex optimization
Kernel methods
19. Numerical Linear Algebra
How computers actually do these calculations matters once you scale up. Topics like:
Condition number (how stable is your computation)
LU and QR decompositions
Iterative methods
Only dive here if you are doing heavy optimization work or writing your own linear algebra code.
 
Phase 6: Where It All Shows Up in ML
Let me show you how each topic maps to actual ML tasks so you see the payoff.
Linear Regression: Matrix multiplication, matrix inverse (or pseudoinverse via SVD), norms for regularization.
Logistic Regression and Neural Networks: Matrix multiplications at every layer, gradients via Jacobians, norms for weight decay.
PCA: Eigenvectors of covariance matrix, or equivalently SVD of the data matrix.
Transformers and Attention: Tons of matrix multiplications, dot products for attention scores, softmax over those scores.
Diffusion Models: Linear transformations combined with noise, eigenvalues showing up in stability analysis.
Recommender Systems: Matrix factorization, SVD, low rank approximation.
Graph Neural Networks: Adjacency matrices, Laplacian matrices, eigendecomposition (spectral methods).
LoRA Fine-Tuning: Low rank decomposition, you literally learn two small matrices A and B such that their product approximates a weight update.
 
How to Actually Learn This
Reading is not enough. You need to:
Code it up. Implement matrix multiplication from scratch in Python. Do SVD on a small image and reconstruct it with fewer components. Actually see dimensionality reduction happen in front of you.
Do problems by hand first, then scale up. A 2x2 matrix calculation by hand teaches you more than a hundred np.matmul calls.
Visualize. 3Blue1Brown's "Essence of Linear Algebra" series is mandatory viewing. I am not even joking, go watch it.
Use it in projects. Build a simple recommender, do PCA on some dataset, train a tiny neural network from scratch. Theory without practice will fade in a week.
Read papers with math in them. Start with easier ones. Force yourself to not skip the equations. Write them out, try to understand what each symbol means.
 
Resources That Are Actually Good
3Blue1Brown's Essence of Linear Algebra (YouTube, free): The visual intuition king.
Gilbert Strang's MIT OCW lectures: The legend himself. Takes time but gold standard.
Mathematics for Machine Learning by Deisenroth, Faisal, and Ong: Free PDF online, written specifically for ML.
Avoid books that are pure theory with no ML context unless you enjoy that. Time is finite.
 
Final Advice
Do not try to learn all of this in one go. Seriously, do not. You will burn out and hate math forever.
Instead, learn Phase 1 and 2 thoroughly before touching any ML. Then start a simple ML project (linear regression from scratch). When you hit something you do not understand, come back and learn Phase 3 or 4. Repeat.
The goal is not to memorize theorems. The goal is to understand what is happening when you type model.forward(x). Linear algebra gives you that x-ray vision.
Also, do not feel bad if it takes months. Some of this stuff took me years to really get. And I still Google things. Everyone does. You are not dumb for forgetting what a Jacobian is, you just have not used it in a while.
Keep going. Build stuff. Break stuff. Fix it. That is the only path.
