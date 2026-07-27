---
title: "Permutation roots"
url: "https://www.johndcook.com/blog/2026/07/26/permutation-roots/"
fetched_at: 2026-07-27T10:17:12.105182+00:00
source: "johndcook.com"
tags: [blog, raw]
---

# Permutation roots

Source: https://www.johndcook.com/blog/2026/07/26/permutation-roots/

Let σ be a permutation on
n
elements. If there is a permutation τ such that applying τ twice has the same effect on the list of elements as applying σ once, we say σ = τ² and τ is a square root of σ.
If we let our
n
elements be the integers 0 through
n
− 1, then we can represent permutations by what they do to this list of numbers. In Python as a tuple of length
n
and compose permutations with the following function:
import itertools

def compose(sigma, tau):
    "Return the composition σ ∘ τ (apply τ first, then σ)."
    return tuple(sigma[j] for j in tau)
We can always construct permutations that have square roots by squaring a permutation. If we run the following code
tau = (3, 1, 4, 5, 2, 0)
sigma = compose(tau, tau)
we find σ = (5, 1, 2, 0, 4, 3), and by construction (3, 1, 4, 5, 2, 0) is a square root of &sigma, though it’s not the only one.
The following code shows that σ has four roots.
import itertools

def numroots(sigma):
    n = len(sigma)
    c = 0
    for tau in itertools.permutations(range(n)):
        if sigma == compose(tau, tau):
            c += 1
    return c

print( numroots(sigma) )
print( numroots( (1, 2, 3, 4, 5, 0) ) )
It also shows that the rotation (1, 2, 3, 4, 5. 0) has no roots.
The function
numroots
has runtime proportional to
n
! and so it’s not practical for large permutations. There is a theorem that says a permutation σ has a square root if and only if the number of cycles it has of every even length is even. See [1].
We can also define cubes and cube roots of permutations, and higher powers and roots.
How common is it for permutations to have square roots, or cube roots, etc.? If you pick a random permutation on
n
elements, what is the probability that it has a
k
th root?
This is a hard question in general, but it is equivalent to finding the coefficient of
x
k
in the infinite product
\prod_{m=1}^\infty \exp_{\text{gcd}(m,k)} \left(\frac{x^m}{m}\right).
This is theorem 4.8.3 in [1].
[1] Herbert Wilf. Generatingfunctionology. Available online
here
.
