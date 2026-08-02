---
title: "Autoscaling endpoints for LLM inference"
source: "https://www.together.ai/blog/autoscaling-endpoints-for-llm-inference"
date: 2026-07-31
date_ingested: 2026-08-02
author: "Together AI"
type: blog
tags: [inference, infrastructure, autoscaling, llm-serving]
---

Summary:
With Dedicated Model Inference on the Together AI platform, you can get your deployments to autoscale on metrics the inference engine actually understands, such as in-flight requests, TTFT, GPU utilization, token throughput. You can set replica bounds, pick a metric and target, and then tune two windows that control how eagerly it scales up and how patiently it scales down.

Understanding and choosing the right metric is important because it determines how your deployment will behave under different load patterns. Together AI supports multiple autoscaling metrics that go beyond simple CPU/memory utilization to inference-specific signals.

Key features:
- Inference-native metrics: in-flight requests, time-to-first-token (TTFT), GPU utilization, token throughput
- Configurable replica bounds (min/max)
- Metric selection with target values
- Scale-up and scale-down window tuning
- Dedicated Model Inference endpoints

The post explains how traditional autoscaling metrics like CPU utilization don't map well to LLM inference workloads, where GPU utilization, request queuing, and token generation rates are more meaningful signals. Together AI's approach uses metrics that the inference engine natively understands, enabling more responsive and cost-effective autoscaling for LLM deployments.
