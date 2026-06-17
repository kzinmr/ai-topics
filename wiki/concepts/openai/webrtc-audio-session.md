---
title: "OpenAI WebRTC Audio Session with Document Context"
type: concept
created: 2026-06-17
updated: 2026-06-17
tags:
  - openai
  - api
  - voice-ai
  - webrtc
  - audio-generation
  - developer-tools
sources:
  - raw/articles/2026-06-14_simonwillison_openai-webrtc-playground.md
aliases: ["OpenAI WebRTC Playground", "WebRTC Audio Session"]
---

# OpenAI WebRTC Audio Session with Document Context

Simon Willison's browser-based playground for OpenAI's WebRTC API, updated to support the new GPT-Realtime-2 model and document context for audio conversations.

## Overview

This tool demonstrates OpenAI's WebRTC API for realtime audio interactions with AI models. The playground allows users to have voice conversations in their browser while providing document context for more informed discussions.

## Key Features

### GPT-Realtime-2 Model Support
- **Model**: GPT-Realtime-2 (released May 2026)
- **Capabilities**: "First voice model with GPT-5-class reasoning"
- **Knowledge cutoff**: September 30, 2024
- **Status**: Available in API but not yet in ChatGPT iPhone app

### Document Context
- **Functionality**: Paste large chunks of document context
- **Use case**: Have audio conversations about specific information
- **Application**: Explore documents, research papers, or any text content conversationally

### Browser-Based Interface
- **Platform**: Web browser (no app installation required)
- **Interaction**: Real-time audio conversation
- **Accessibility**: Works on desktop and mobile browsers

## Technical Implementation

### WebRTC API
- **Protocol**: WebRTC for real-time audio streaming
- **Latency**: Low-latency audio communication
- **Quality**: High-quality voice synthesis and recognition

### API Integration
- **Endpoint**: OpenAI's realtime API
- **Authentication**: API key required
- **Model selection**: Choose between available realtime models

## Use Cases

### Document Exploration
- **Research papers**: Discuss academic papers with AI
- **Legal documents**: Analyze contracts or legal texts
- **Technical documentation**: Explore API docs or manuals
- **Books**: Discuss book content conversationally

### Accessibility
- **Voice-first interaction**: No typing required
- **Hands-free operation**: Useful while multitasking
- **Natural conversation**: More intuitive than text-based interaction

### Education
- **Language learning**: Practice conversations in target language
- **Concept explanation**: Get verbal explanations of complex topics
- **Study aid**: Discuss study materials aloud

## Development History

### Initial Version (December 2024)
- **Purpose**: Test OpenAI's then-new WebRTC API
- **Features**: Basic audio conversation capability
- **Platform**: Browser-based playground

### Current Version (June 2026)
- **Model upgrade**: GPT-Realtime-2 support
- **New feature**: Document context input
- **Improvement**: Better reasoning capabilities

## Technical Details

### API Capabilities
- **Real-time processing**: Instant audio response
- **Voice synthesis**: Natural-sounding speech generation
- **Speech recognition**: Accurate transcription of user speech
- **Context window**: Supports long document context

### Browser Requirements
- **WebRTC support**: Modern browsers with WebRTC capability
- **Microphone access**: Required for user voice input
- **Speaker output**: For AI voice responses

## Related Concepts

- [[realtime-api]] - OpenAI Realtime API overview
- [[voice-ai]] - Voice AI technologies
- [[openai]] - OpenAI company and products
- [[developer-tools]] - Developer tools for AI applications
- [[audio-generation]] - Audio generation technologies

## References

- [Original Article](https://simonwillison.net/2026/Jun/12/openai-webrtc/)
- [OpenAI Realtime API Documentation](https://platform.openai.com/docs/guides/realtime)
- [GPT-Realtime-2 Announcement](https://openai.com/index/introducing-gpt-realtime-2/)
