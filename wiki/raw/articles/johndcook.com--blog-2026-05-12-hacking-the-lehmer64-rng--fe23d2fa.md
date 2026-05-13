---
title: "Hacking the lehmer64 RNG"
url: "https://www.johndcook.com/blog/2026/05/12/hacking-the-lehmer64-rng/"
fetched_at: 2026-05-13T07:01:24.251663+00:00
source: "johndcook.com"
tags: [blog, raw]
---

# Hacking the lehmer64 RNG

Source: https://www.johndcook.com/blog/2026/05/12/hacking-the-lehmer64-rng/

A couple days ago I wrote about hacking the Mersenne Twister. I explained how to recover the random number generator’s internal state from a stream of 640 outputs.
This post will do something similar with the lehmer64 random number generator. This generator is very simple to implement.
Daniel Lemire
found it to be “the fastest conventional random number generator that can pass Big Crush,” a well-respected test for pseudorandom number generators.
Implementing lehmer64
The lehmer64 generator can be implemented in C by
__uint128_t g_lehmer64_state;

uint64_t lehmer64() {
    g_lehmer64_state *= 0xda942042e4dd58b5ULL;  
  return g_lehmer64_state >> 64;
}
The analogous code in Python would have to simulate the overflow behavior of a 128-bit integer by reducing the state mod 2
128
after the multiplication.
Reverse engineering lehmer64 is easier than reverse engineering the Mersenne Twister because only three outputs are needed. However, the theory behind the exploit is more sophisticated. See [1].
The following code sets the state to an arbitrary initial seed value and generates three values.
#include <stdio.h>
#include <stdint.h>

int main(void)
{
    g_lehmer64_state = 0x4789499d78770934; // seed
    for (int i = 0; i < 3; i++) {
        printf("0x%016lx\n", lehmer64());
    }

    return 0;
}
The code prints the following.
0x3d144d12822bcc2e
0x85a67226191a568d
0x53e803dffc88e8f8
Exploiting lehmer64
Here is Python code for recovering the state of the lehmer64 generator given in [1].
def reconstruct(X):
    a = 0xda942042e4dd58b5
    r = round(2.64929081169728e-7 * X[0] + 3.51729342107376e-7 * X[1] + 3.89110109147656e-8 * X[2])
    s = round(3.12752538137199e-7 * X[0] - 1.00664345453760e-7 * X[1] - 2.16685184476959e-7 * X[2])
    t = round(3.54263598631140e-8 * X[0] - 2.05535734808162e-7 * X[1] + 2.73269247090513e-7 * X[2])
    u = r * 1556524 + s * 2249380 + t * 1561981
    v = r * 8429177212358078682 + s * 4111469003616164778 + t * 3562247178301810180
    state = (a*u + v) % (2**128)
    return state
Let’s call
reconstruct
with the output of our C code.
X = [0x3d144d12822bcc2e, 0x85a67226191a568d, 0x53e803dffc88e8f8]
print( hex( reconstruct(X) ) )
This prints
0x3d144d12822bcc2e1b81101c593761c4
Now for the confusing part: at what point is the number above the state of the generator? Is it the state before or after generating the three values? Neither! It is the state after generating the first value.
We can verify this by modifying the C code as follows and rerunning it.
void print_u128(__uint128_t n)
{
    printf("0x%016lx%016lx\n",
           (uint64_t)(n >> 64),      // upper 64 bits
           (uint64_t)n);             // lower 64 bits
}

int main(void)
{
    g_lehmer64_state = 0x4789499d78770934; // seed
    for (int i = 0; i < 3; i++) {
        printf("0x%016lx\n", lehmer64());
        printf("state: ");
        print_u128(g_lehmer64_state);
    }
 
    return 0;
}
The main goal of [1] is to recover the state of the PCG generator, not the lehmer64 generator. The latter was a side quest. Recovering the state of PCG64 is much harder; the authors estimate it takes about 20,000 CPU-hours. The paper shows that a technique used as part of pursuing their main goal can quickly recover the lehmer64 state.
Related posts
[1] Charles Bouillaguet, Florette Martinez, and Julia Sauvage. Practical seed-recovery for the PCG Pseudo-Random Number Generator. IACR Transactions on Symmetric Cryptology. ISSN 2519-173X, Vol. 2020, No. 3, pp. 175–196.
