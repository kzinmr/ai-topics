# Starchild-1: The First Real-Time Multimodal World Model

**Source:** https://odyssey.ml/introducing-starchild-1
**Author:** Oliver Cameron (Odyssey)
**Date:** May 17, 2026

Odyssey introduced Starchild-1, the world's first multimodal world model that autoregressively generates synchronized audio and video in real-time while responding to continuous streaming user input. Unlike offline models like DeepMind's Veo that generate fixed-length clips, Starchild-1 is a causal, autoregressive model that predicts next audio-video states conditioned on past observations and user input.

Key technical innovations:
- **Causal distillation pipeline**: Adapts a bidirectional audio-video foundation model into a real-time autoregressive world model
- **Asynchronous KV-cache architecture**: Handles fundamentally different temporal characteristics of audio vs video
- **Rollout adaptation strategy**: Maintains coherent audio-video generation over extended interactions

The model enables users to stream text, speech, and action inputs continuously, dynamically altering generated visuals and sounds in real time. Fields targeted: robotics, education, gaming, healthcare, defense.
