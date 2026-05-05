---
title: "Speculative Sampling"
url: "https://jaykmody.com/blog/speculative-sampling/"
fetched_at: 2026-05-05T07:01:46.953991+00:00
source: "Jay Mody"
tags: [blog, raw]
---

# Speculative Sampling

Source: https://jaykmody.com/blog/speculative-sampling/

Speculative Sampling
February 08, 2023
This post provides an overview, implementation, and time complexity analysis of DeepMind's paper
Accelerating Large Language Model Decoding with Speculative Sampling
.
Code for this blog post can be found at
github.com/jaymody/speculative-samlping
.
EDIT (Apr 13th, 2023):
Updated code and time complexity to avoid the extra forward pass of the draft model (credits to
KexinFeng
).
Autoregressive Sampling
The standard way of generating text from a language model is with
autoregressive sampling
, here's the algorithm as defined in the paper:
In code:
def autoregressive_sampling(x, model, N):
    n = len(x)
    T = len(x) + N

    while n < T:
        x = np.append(x, sample(model(x)[-1]))
        n += 1

    return x
Where:
x
is a list of integers representing the token ids of the input text
model
is a language model (like GPT-2) that accepts as input a list of token ids of length
seq_len
and outputs a matrix of probabilities of shape
[seq_len, vocab_size]
.
N
is the number of tokens we want to decode.
The time complexity of this algorithm is \(O(N \cdot t_{\text{model}})\):
\(N\): The number of iterations of our while loop, which is just the number of tokens to decode \(N\).
\(t_{\text{model}}\): The time complexity of each iteration in the loop, which is just the time taken for a single forward pass of our model \(t_{\text{model}}\).
Speculative Sampling
In
speculative sampling
, we have two models:
A smaller, faster
draft model
(e.g. DeepMind's 7B Chinchilla model)
A larger, slower
target model
(e.g. DeepMind's 70B Chinchilla model)
The idea is that the draft model
speculates
what the output is \(K\) steps into the future, while the target model determines how many of those tokens we should
accept
. Here's an outline of the algorithm:
The draft model decodes \(K\) tokens in the regular autoregressive fashion.
We get the probability outputs of the target and draft model on the new predicted sequence.
We compare the target and draft model probabilities to determine how many of the \(K\) tokens we want to keep based on some
rejection criteria
. If a token is rejected, we
resample
it using a combination of the two distributions and don't accept any more tokens.
If all \(K\) tokens are accepted, we can sample an additional final token from the target model probability output.
As such, instead of decoding a single token at each iteration, speculative sampling decodes between 1 to \(K + 1\) tokens per iteration. If no tokens are accepted, we resample guaranteeing at least 1 token is decoded. If all \(K\) tokens are accepted, then we can also sample a final token from the target models probability distribution, giving us a total of \(K + 1\) tokens decoded.
For example, consider the common idiom "The apple doesn't fall far from the tree". Given just the first part of the phrase, "The apple doesn't fall", in speculative sampling with \(K=4\):
The draft model speculates the output to be "far from the tree" (4 tokens)
The target model looks at those tokens, and decides to accept them all, and also sample a final token (i.e. maybe it samples a period ".").
As such, in a single iteration, we were able to decode 5 tokens instead of just a single token. However, this may not always be the case, consider instead the input "Not all heroes":
The draft model speculates the output to be "wear capes and hats" (4 tokens)
The target model looks at those tokens, but decides to only accepts the first two "wear capes" and discard the rest.
In this case, only 2 tokens were accepted.
As long as the draft model is sufficiently faster than the target model
while also
maintaining a high enough
acceptance rate
, then speculative sampling should yield a speedup.
The intuition behind speculative sampling is that certain strings of tokens (common phrases, pronouns, punctuation, etc ...) are fairly easy to predict, so a smaller, less powerful, but faster draft model should be able to quickly predict these instead of having our slower target model doing all the work.
Another important property of speculative sampling is that it is
mathematically equivalent
to sampling from the target model, due to the way the rejection criteria and resampling method are designed. The
proof for this is shown in the paper (Theorem 1)
.
Finally, speculative sampling requires no changes to the model's architecture, training, or anything like that. It can be used with existing models alongside other inference techniques such as quantization, hardware acceleration, flash attention, etc ... It can also be used with top-p/top-k/temperature.
Here's the full algorithm as defined in the paper:
In code (
full implementation here
):
def max_fn(x):
    x_max = np.where(x > 0, x, 0)
    return x_max / np.sum(x_max)

def speculative_sampling(x, draft_model, target_model, N, K):
    # NOTE: paper indexes arrays starting from 1, python indexes from 0, so
    # we have to add an extra -1 term when indexing using n, T, or t
    n = len(x)
    T = len(x) + N

    while n < T:
        # Step 1: auto-regressive decode K tokens from draft model and get final p
        x_draft = x
        for _ in range(K):
            p = draft_model(x_draft)
            x_draft = np.append(x_draft, sample(p[-1]))

        # Step 2: target model forward passes on x_draft
        q = target_model(x_draft)

        # Step 3: append draft tokens based on rejection criterion and resample
        # a token on rejection
        all_accepted = True
        for _ in range(K):
            i = n - 1
            j = x_draft[i + 1]
            if np.random.random() < min(1, q[i][j] / p[i][j]):  # accepted
                x = np.append(x, j)
                n += 1
            else:  # rejected
                x = np.append(x, sample(max_fn(q[i] - p[i])))  # resample
                n += 1
                all_accepted = False
                break

        # Step 4: if all draft tokens were accepted, sample a final token
        if all_accepted:
            x = np.append(x, sample(q[-1]))
            n += 1

        # just keeping my sanity
        assert n == len(x), f"{n} {len(x)}"

    return x
The time complexity for this algorithm is \(O(\frac{N}{r(K + 1)} \cdot (t_{\text{draft}}K + t_{\text{target}}))\).
\(\frac{N}{r(K+1)}\): The number of iterations in our while loop. This works out to the number of tokens we want to decode \(N\) divided by the average number of tokens that get decoded per iteration \(r(K + 1)\). The paper doesn't directly report the average number of tokens that get decoded per iteration, instead they provide the acceptance rate \(r\) (which is the average number of tokens decoded per iteration divided by \(K + 1\)). As such, we can recover the average number of tokens decoded simply by multiplying \(r\) by \(K + 1\).
\(t_{\text{draft}}K + t_{\text{target}}\): The time complexity for each iteration in the loop. The \(t_{\text{target}}\) term is for the single forward pass of the target model in step 2, and \(t_{\text{draft}}K\) is for the \(K\) forward passes of the draft model in step 1.
Speedup Results
The paper reports the following speedups for their 70B Chinchilla model (using a specially trained 7B Chinchilla as the draft model):
You can see that there was no performance degradation and the decoding process is 2 times faster as compared to autoregressive decoding.
Let's compare these empirical speedup numbers to theoretical speedup numbers, which we can calculate using our time complexity equations:
\[
\begin{align}
\text{speedup} & = \frac{\text{time complexity of autoregressive}}{\text{time complexity of speculative}} \\
& = \frac{N\cdot t_{\text{target}}}{\frac{N}{r(K + 1)} \cdot (t_{\text{draft}}K + t_{\text{target}})}
& \\
& = \frac{r(K + 1) \cdot t_{\text{target}}}{t_{\text{draft}}K + t_{\text{target}}}
\end{align}
\]
Using the values provided in the paper:
\(K = 4\)
\(t_{\text{draft}} = 1.8\text{ms}\)
\(t_{\text{target}} = 14.1\text{ms}\)
\(r = 0.8\) for HumanEval and \(r = 0.62\) for XSum (see figure 1 in the paper)
For HumanEval we get a theoretical speedup of
2.65
, while the paper reports an empirical speedup of
2.46
.
For XSum we get a theoretical speedup of
2.05
, while the paper reports an empirical speedup of
1.92
.
We can reproduce these results by
running our implementation with GPT-2 1.5B as our target model and GPT-2 124M as our draft model
:
python main.py \
    --prompt "Alan Turing theorized that computers would one day become" \
    --n_tokens_to_generate 40 \
    --draft_model_size "124M" \
    --target_model_size "1558M" \
    --K 4 \
    --temperature 0 \
    --seed 123
Which gives a speedup of
2.23
:
Time = 60.64s
Text = Alan Turing theorized that computers would one day become so powerful that they would be able to think like humans.

In the 1950s, he proposed a way to build a computer that could think like a human. He called it the "T

Speculative Decode
------------------
Time = 27.15s
Text = Alan Turing theorized that computers would one day become so powerful that they would be able to think like humans.

In the 1950s, he proposed a way to build a computer that could think like a human. He called it the "T
Note, the output is the exact same for both methods due to the use of
temperature = 0
, which corresponds to
greedy sampling
(always taking the token with the highest probability). If a non-zero temperature were used, this would not be the case. Although speculative sampling is mathematically the same as sampling from the target model directly, the results of autoregressive and speculative sampling will be different due to randomness. Speculative sampling giving a different result than autoregressive sampling is akin to running autoregressive sampling but with a different seed. When
temperature = 0
however, a 100% of the probability is assigned to a single token, so sampling from the distribution becomes deterministic, hence why the outputs are the same. If we instead used
temperature = 0.5
, we'd get different outputs:
Autoregressive Decode
---------------------
Time = 49.06s
Text = Alan Turing theorized that computers would one day become self-aware. This is known as the "Turing Test" and it is a test that has been used to determine if a computer is intelligent.

The Turing Test is based on the

Speculative Decode
------------------
Time = 31.60s
Text = Alan Turing theorized that computers would one day become so powerful that they would be able to simulate the behavior of human minds. The Turing Test is a test that asks a computer to recognize whether a given piece of text is a human or a computer generated
