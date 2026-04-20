---
title: "[2604.08826] HiFloat4 Format for Language Model Pre-training on Ascend NPUs"
url: "https://substack.com/redirect/83c80ff1-f353-464d-b53e-d2ff5aa2347f?j=eyJ1IjoiMmZseDYifQ.6O_iC1_GWCzChnbrHzSrs1hMpJpoODTUJm_FAk3tf6E"
fetched_at: 2026-04-20T12:32:26.114243+00:00
source_date: 2026-04-20
tags: [newsletter, auto-ingested]
---

# [2604.08826] HiFloat4 Format for Language Model Pre-training on Ascend NPUs

Source: https://substack.com/redirect/83c80ff1-f353-464d-b53e-d2ff5aa2347f?j=eyJ1IjoiMmZseDYifQ.6O_iC1_GWCzChnbrHzSrs1hMpJpoODTUJm_FAk3tf6E

[Submitted on 9 Apr 2026]
Title:
HiFloat4 Format for Language Model Pre-training on Ascend NPUs
Authors:
Mehran Taghian
,
Yunke Peng
,
Xing Huang
,
Yao Wang
,
Yaoyuan Wang
,
Wei Guo
,
Yuanyong Luo
,
Tianchi Hu
,
Junsong Wang
,
Xin Wang
,
Hu Liu
,
Yu Cheng
,
Ziwei Yu
,
Hongliang Li
,
Mehdi Rahimifar
,
Lei Yan
,
Xuefei Wang
,
Zhuang Ma
,
Lei Liu
,
Hui Yu
,
Anandharaju Durai Raju
,
Hoang Le
,
Hei Yi Mak
,
Tanzila Rahman
,
Shadan Golestan
View a PDF of the paper titled HiFloat4 Format for Language Model Pre-training on Ascend NPUs, by Mehran Taghian and 24 other authors
View PDF
HTML (experimental)
Abstract:
Large foundation models have become central to modern machine learning, with performance scaling predictably with model size and data. However, training and deploying such models incur substantial computational and memory costs, motivating the development of low-precision training techniques. Recent work has demonstrated that 4-bit floating-point (FP4) formats--such as MXFP4 and NVFP4--can be successfully applied to linear GEMM operations in large language models (LLMs), achieving up to 4x improvements in compute throughput and memory efficiency compared to higher-precision baselines. In this work, we investigate the recently proposed HiFloat4 FP4 format for Huawei Ascend NPUs and systematically compare it with MXFP4 in large-scale training settings. All experiments are conducted on Ascend NPU clusters, with linear and expert GEMM operations performed entirely in FP4 precision. We evaluate both dense architectures (e.g., Pangu and LLaMA-style models) and mixture-of-experts (MoE) models, where both standard linear layers and expert-specific GEMMs operate in FP4. Furthermore, we explore stabilization techniques tailored to FP4 training that significantly reduce numerical degradation, maintaining relative error within 1% of full-precision baselines while preserving the efficiency benefits of 4-bit computation. Our results provide a comprehensive empirical study of FP4 training on NPUs and highlight the practical trade-offs between FP4 formats in large-scale dense and MoE models.
Submission history
From: Mehran Taghian Jazi [
view email
]
[v1]
Thu, 9 Apr 2026 23:50:56 UTC (1,294 KB)
