---
title: "Gemini Android Computer Use Demo"
source_url: "https://github.com/google-gemini/gemini-android-computer-use-quickstart"
date: 2026-06-25
author: "Google Gemini"
captured: 2026-06-25
---

# Gemini Android Computer Use Demo

This repository contains a reference implementation for controlling an Android emulator using the **Gemini 3.5 Flash** Computer Use API (`mobile` environment) via the Google GenAI SDK.

## Overview

The agent operates in a continuous loop:
1. It captures a screenshot of the virtual device using ADB.
2. It sends the screenshot along with the user's task to Gemini 3.5 Flash.
3. The model returns structured tool commands (such as `click`, `type`, `long_press`, `drag_and_drop`, `press_key`, `go_back`, `wait`, `list_apps`, `open_app`, `take_screenshot`).
4. The client executing script maps the normalized coordinates (0-999) to the actual physical resolution of the screen and executes the action via ADB.
5. The loop repeats until the task is complete.

## Directory Structure

*   `agent.py`: The main agent script orchestrating the interaction loop.
*   `setup_emulator.sh`: Idempotent shell script to configure and create the Android virtual device (`AI_Agent_Phone`) on macOS.
*   `requirements.txt`: Python package dependencies.

## Setup Instructions

### Prerequisites

Ensure you have the following installed on your Mac:
*   [Homebrew](https://brew.sh/)
*   [uv](https://docs.astral.sh/uv/) (highly recommended for Python dependency management)

### 1. Configure the Virtual Device

Run the setup script to install the Android CLI tools, system images, and create the `AI_Agent_Phone` emulator instance:

```bash
chmod +x setup_emulator.sh
./setup_emulator.sh
```

### 2. Set Up API Key

Retrieve your API key from Google AI Studio and export it:

```bash
export GEMINI_API_KEY="your-api-key-here"
```

### 3. Run the Agent

Create a virtual environment and install the required dependencies:

```bash
uv venv
source .venv/bin/activate
uv pip install -r requirements.txt
```

Then run the agent:

```bash
python agent.py "Find the latest blog post from philipp schmid and summarize it."
```

Alternatively, you can run the agent with a custom task:

```bash
python agent.py "Open Settings and enable dark mode"
```

## Licensing & Disclaimer

Copyright 2026 Google LLC  

All software is licensed under the Apache License, Version 2.0 (Apache 2.0); you may not use this file except in compliance with the Apache 2.0 license. You may obtain a copy of the Apache 2.0 license at: [https://www.apache.org/licenses/LICENSE-2.0](https://www.apache.org/licenses/LICENSE-2.0)

All other materials are licensed under the Creative Commons Attribution 4.0 International License (CC-BY). You may obtain a copy of the CC-BY license at: [https://creativecommons.org/licenses/by/4.0/legalcode](https://creativecommons.org/licenses/by/4.0/legalcode)

Unless required by applicable law or agreed to in writing, all software and materials distributed here under the Apache 2.0 or CC-BY licenses are distributed on an "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the licenses for the specific language governing permissions and limitations under those licenses.

This is not an official Google product.
