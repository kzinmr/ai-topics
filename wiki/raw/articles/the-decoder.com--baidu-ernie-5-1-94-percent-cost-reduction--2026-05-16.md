# Baidu's Ernie 5.1 Cuts 94% of Pre-Training Costs While Competing with Top Models

> Source: The Decoder — by Jonathan Kemper, May 11, 2026
> URL: https://the-decoder.com/baidus-ernie-5-1-cuts-94-percent-of-pre-training-costs-while-competing-with-top-models/

Baidu has released Ernie 5.1, a language model built on the pre-training foundation of its predecessor Ernie 5.0 but with roughly a third of the total parameters and about half the active parameters per query.

Pre-training costs came in at just six percent of what comparable models require, according to Baidu. On the Arena Search Leaderboard, Ernie 5.1 scored 1,223 points as of May 9 — 4th place globally and 1st among Chinese models, behind Claude Opus 4.6 Search (1,255), GPT-5.5 Search (1,242), and Claude Opus 4.7 (1,236).

In additional benchmarks, Baidu claims Ernie 5.1 beats DeepSeek-V4-Pro on autonomous AI agent tasks (tau3-bench, SpreadsheetBench-Verified) and comes close to Google's Gemini 3.1 Pro on knowledge and reasoning benchmarks (GPQA, MMLU-Pro). On AIME26 math, the model with tool access lands just behind Gemini 3.1 Pro.

## The "Once-For-All" Elastic Training Framework

Baidu built Ernie 5.1 as a smaller sub-model from Ernie 5.0 using an approach called the "Once-For-All elastic training framework." Instead of running a separate, expensive pre-training pass for each model size, the company optimizes an entire family of differently sized models in a single run. The framework simultaneously varies depth, expert count, and active experts per request.

The models share weights but differ in depth, width, and how many specialized expert blocks activate for a given query. Baidu picked what it considers the best configuration from this family for Ernie 5.1, which explains the low pre-training costs — the heavy compute was already done for Ernie 5.0.

## Four-Stage Training Pipeline

Ernie 5.1 uses a four-stage training pipeline with specialized expert models for code, logic, and agent tasks, designed to prevent different capabilities from interfering with each other during the learning process.

Baidu also rebuilt its reinforcement learning infrastructure from the ground up. Model updates, response generation, and evaluation — traditionally tightly coupled — now run as separate subsystems that scale independently, coordinated by a central controller.

## Availability and Limitations

Ernie 5.1 is accessible through Baidu's platforms and integrated into various creative applications, but the model weights remain closed, making independent verification of its reported performance impossible. On the Text Arena Leaderboard, the pre-release Ernie 5.1 Preview sits at 13th place with 1,476 points — Claude Opus variants and Gemini 3.1 Pro hold the top spots.
