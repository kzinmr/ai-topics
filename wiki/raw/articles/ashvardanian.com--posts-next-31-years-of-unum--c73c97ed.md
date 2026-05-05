---
title: "The Next 31 Years of Developing Unum"
url: "https://ashvardanian.com/posts/next-31-years-of-unum/"
fetched_at: 2026-05-05T07:01:49.716526+00:00
source: "Ash Vardanyan"
tags: [blog, raw]
---

# The Next 31 Years of Developing Unum

Source: https://ashvardanian.com/posts/next-31-years-of-unum/

When I was 20, I committed the next 40 years of my life to AI, approaching it from the infrastructure perspective.
In 2015, before ChatGPT and the AI surge, such a long-term commitment seemed naive to many — almost like proposing marriage on a second date — the move I am most proud of.
Yesterday, Unum celebrated its 9th anniversary, and my open-source contributions have surpassed 9,000 stars on GitHub.
To mark the occasion, as I’ve done before, I’m releasing something new, free, and practical for the scientific community: efficient
Bilinear Forms
for real and complex numbers.
These are useful in fields like statistics, computational physics, biology, or chemistry.
These kernels may offer up to 5x improvements in mixed-precision throughput compared to
BLAS
and other libraries that power tools like NumPy, especially for simulating the time evolution of small systems of non-entangled quantum states.
If you’re curious about Bilinear Forms, you can check the
release notes of the SimSIMD project
.
——
On a more personal note, founding, funding, and building Unum was the second-best decision of my life.
It cost me my physics degree, meaning I can’t formally teach in most universities.
It drained my finances as I learned how to hire and fire people, and “how not to sell” products.
Over the past nine years, I’ve moved more times than I can count, witnessed wars, lost loved ones, opened and closed offices, failed countless fundraisers, and started over repeatedly.
But even on my darkest days, I’ve always found solace in the work.
It has helped me recover every time.
And it never felt like work.
Confucius was right — “Choose a job you love, and you will never have to work a day in your life”.
——
Strategically, the past few years have been about building trust within the open-source community.
While innovative one-off projects sometimes emerge, the ecosystems are rare.
Today, giants like Google and Meta dominate the creation of foundational infrastructure, while “innovative startups” build shallow “wrappers” — adding 5% of work, charging 500% more, and calling it a day.
Google has given us projects like
LevelDB
,
TensorFlow
,
gRPC
,
SCANN
, and the
Gemma
models.
Meta has released
RocksDB
,
PyTorch
,
Thrift
,
FAISS
, and the
LLAMA
models.
Those are solid projects, but most of them were designed to be “good enough” to meet milestones, close tickets, or secure promotions.
They weren’t always built by those obsessed with quality, elegance, and harnessing the full potential of modern hardware.
Similarly, the software built on top of that infrastructure is often unimaginably dull.
It’s not always sending rockets to Mars or curing cancer.
Presentation slide from one of my failed fundraisers, 2022/3.
That’s why we built
UStore
,
USearch
,
UCall
, and
UForm
.
First, as a proof of concept, that a short minimalistic codebase can outperform the so-called “leaders of the industry” in terms of scalability metrics and be a foundation for all kinds of inspiring projects — from the world’s most used Chat Bots to the personalized medicine and drug discovery.
Nine years in, this vision is clearer than ever, and I’m declaring this “warm-up phase” complete.
Over the next 31+ years, my goal is to evolve these projects into a continuously growing computing infrastructure capable of powering the next generation of scientific and technological breakthroughs.
Thank you all for your support — here’s to the next chapter.
Ash,
Benevolent Dictator for Life
Unum
