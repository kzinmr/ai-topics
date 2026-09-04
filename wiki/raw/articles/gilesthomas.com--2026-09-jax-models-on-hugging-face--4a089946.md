---
title: "Putting my JAX-trained models on the Hugging Face Hub"
url: "https://www.gilesthomas.com/2026/09/jax-models-on-hugging-face"
fetched_at: 2026-09-04T10:00:43.844059+00:00
source: "gilesthomas.com"
tags: [blog, raw]
---

# Putting my JAX-trained models on the Hugging Face Hub

Source: https://www.gilesthomas.com/2026/09/jax-models-on-hugging-face

Writing the post that I wished I'd found when I started learning whatever it was...
Archives
Categories
Blogroll
I hadn't uploaded the models that I trained using JAX to the Hugging Face Hub because
Transformers has been PyTorch-only since
version 5
(though they say they're working to add interoperability with JAX in the future), so it
would have been tough to get them working natively with
AutoModelForCausalLM
and the like.
But then it dawned on me that I'd already written
a conversion script
that could
take my JAX safetensors files and convert them into ones compatible with my PyTorch
code.  It's actually those converted models that I use for my evals -- so I could
use my
existing PyTorch script
to upload them.
So, I've now uploaded PyTorch-compatible versions of all of my JAX-trained models:
"
Writing an LLM from scratch, part 34b -- from bigrams to GPT-2, one component at a time (in JAX)
"
"
Why do OpenAI's GPT-2 weights beat mine? Part three: testing overtraining
"
"
A quick(ish) Chinchilla check
"
I've also added links to the posts in question.
Citing this post
This is a blog, and if you want to link to this post then please do :-)
                However, if you're writing something more academic and need to do
                a proper citation, then here's a BibTeX block to make things easier.
@misc{thomas2026sep-jax-models-on-hugging-face,
  author       = {Thomas, Giles},
  title        = {{Putting my JAX-trained models on the Hugging Face Hub}},
  year         = {2026},
  month        = sep,
  howpublished = {Blog post},
  url          = {https://www.gilesthomas.com/2026/09/jax-models-on-hugging-face},
}
