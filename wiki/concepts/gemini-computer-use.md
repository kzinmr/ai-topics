---
title: "Gemini Computer Use (Android)"
created: 2026-06-25
updated: 2026-06-25
type: concept
tags: [computer-use, gemini, agents, on-device, tool-use, automation]
sources:
  - raw/articles/2026-06-25_philschmid_gemini-android-use.md
  - raw/articles/2026-06-25_google-gemini_android-computer-use-quickstart.md
---

# Gemini Computer Use (Android)

## Overview

Gemini Computer Use on Android is a practical implementation of [[concepts/computer-use|computer use agents]] that allows [[entities/google|Google]]'s Gemini 3.5 Flash model to control an Android device through structured function calls. Introduced in June 2026, computer use is a native built-in tool in [[concepts/gemini/gemini-3-5-flash|Gemini 3.5 Flash]] — not a separate model or add-on — that enables the model to see the screen, reason about what to do, and output actionable commands like taps, text input, swipes, and app launches.

The implementation guide by [[entities/philipp-schmid|Philipp Schmid]] walks through controlling an Android emulator using the `mobile` environment in the Gemini API and the Python SDK. The companion open-source reference implementation from Google Gemini provides a complete working agent with an ADB bridge and emulator setup script.

Computer use operates as a function-calling loop: the model receives a screenshot and a task description, returns structured action commands, those commands are executed on the device via ADB (Android Debug Bridge), a new screenshot is captured, and the loop repeats until the task is complete.

Gemini supports three computer use environments:
- **`browser`**: Desktop web automation (Chrome-based)
- **`mobile`**: Mobile devices and emulators (Android; platform-agnostic design also supports iOS)
- **`desktop`**: Operating system-level desktop control

This page focuses on the `mobile` environment implementation for Android.

## Architecture

The agent architecture follows a tight screenshot-model-action loop:

```
  Screenshot ──> Gemini 3.5 Flash ──> function_call
      ▲                                    │
      │                                    ▼
      └──────── Execute via ADB ◄──────────┘
```

### Component Breakdown

**1. Screenshot Capture**: The ADB bridge captures the current device screen as a PNG image via `adb exec-out screencap -p`. This raw pixel data is base64-encoded and sent to the Gemini API as an image part.

**2. Model Inference**: Gemini 3.5 Flash receives:
- The user's natural language task (e.g., "Open Settings and enable dark mode")
- The current screenshot as a base64-encoded image
- System instructions guiding how to operate the phone
- The `computer_use` tool declaration with `environment: "mobile"`

The model returns either a structured function call (action to execute) or output text (task complete).

**3. Function Call Parsing**: The agent loop inspects `interaction.steps` for items of type `function_call`. Each call has a `name` (the action) and `arguments` (parameters with normalized coordinates). The agent maps the function name to an ADB bridge method.

**4. ADB Execution**: The `ADBBridge` class translates normalized coordinates to actual pixel coordinates and executes ADB shell commands. Coordinates use a 0-999 normalized grid where `(0, 0)` is top-left and `(999, 999)` is bottom-right. The bridge converts these to device resolution using the formula: `pixel = normalized / 1000 * screen_dimension`.

**5. Result Feedback**: After executing the action, the bridge captures a fresh screenshot. Both the action result (success/error JSON) and the new screenshot are packaged as a `function_result` and sent back to the model in the next interaction.

**6. Termination**: The loop continues until the model returns output text (no more function calls) or the maximum turn count is reached.

### Normalized Coordinate System

All screen interactions use a resolution-independent 0-999 grid. This design decouples the model from specific device resolutions. The bridge handles conversion:

```python
def _px(self, x, y):
    return int(x / 1000 * self.width), int(y / 1000 * self.height)
```

This approach allows the same agent code to work across devices with different screen sizes and also makes the `mobile` environment platform-agnostic — the model outputs the same normalized actions whether the target is Android or iOS.

## Supported Actions

The `mobile` environment exposes 10 structured actions that the model can request. Each action must be implemented in the bridge for the agent to function.

### 1. `open_app`
Opens an application by package name or app name on the device.

- **Arguments**: `app_name: str`, `package_name: str` (optional)
- **ADB Implementation**: Uses `adb shell monkey` with the package name and `android.intent.category.LAUNCHER` to start the app
- **Error Handling**: Returns an error if the app is not installed or has no launcher activity

### 2. `click`
Taps a specific coordinate on the screen.

- **Arguments**: `y: int (0-999)`, `x: int (0-999)`
- **ADB Implementation**: `adb shell input tap <pixel_x> <pixel_y>`
- **Usage**: Primary action for interacting with UI elements like buttons, links, and checkboxes

### 3. `type`
Enters text into the currently focused input field.

- **Arguments**: `text: str`, `press_enter: bool` (default: false)
- **ADB Implementation**: `adb shell input text <text>` with space-to-`%s` substitution for ADB compatibility; optionally sends keyevent 66 (Enter) if `press_enter` is true
- **Constraint**: The model is instructed not to use the virtual keyboard; all text entry goes through this action

### 4. `long_press`
Performs a long-press (press-and-hold) gesture at a coordinate.

- **Arguments**: `y: int (0-999)`, `x: int (0-999)`, `seconds: int` (default: 2)
- **ADB Implementation**: `adb shell input swipe <x> <y> <x> <y> <duration_ms>` using identical start and end coordinates
- **Usage**: Context menus, drag-to-select, and other long-press interactions

### 5. `drag_and_drop`
Drags from one screen coordinate to another.

- **Arguments**: `start_y`, `start_x`, `end_y`, `end_x` (all 0-999)
- **ADB Implementation**: `adb shell input swipe <start_px> <start_py> <end_px> <end_py> 300`
- **Usage**: Rearranging items, moving files, slider controls

### 6. `press_key`
Presses a hardware or system key.

- **Arguments**: `key: str`
- **ADB Implementation**: Maps named keys to Android keycodes via a lookup table:
  - `"home"` → keyevent 3
  - `"back"` → keyevent 4
  - `"enter"` → keyevent 66
  - `"app_switch"` → keyevent 187
  - `"menu"` → keyevent 82
- **Fallback**: Passes unrecognized key names directly as the keyevent argument

### 7. `go_back`
Navigates to the previous screen.

- **Arguments**: None
- **ADB Implementation**: `adb shell input keyevent 4` (Android back key)
- **Usage**: Standard Android back navigation

### 8. `wait`
Pauses execution for a specified duration.

- **Arguments**: `seconds: int` (default: 1)
- **Implementation**: `time.sleep(seconds)` — no ADB command required
- **Usage**: Waiting for animations, loading spinners, or network responses

### 9. `list_apps`
Retrieves the list of third-party applications installed on the device.

- **Arguments**: None
- **ADB Implementation**: `adb shell pm list packages -3` and parses the output
- **Returns**: A dictionary with an `apps` key containing the list of package names
- **Usage**: Allows the model to discover available apps before attempting to launch them

### 10. `take_screenshot`
Captures the current screen state.

- **Arguments**: None
- **ADB Implementation**: Returns `None` (the screenshot is taken separately by the agent loop after every action)
- **Usage**: Explicit screenshot requests from the model; in practice the agent loop already captures after each action

## Setup & Requirements

### Prerequisites

The reference implementation targets macOS but the concepts apply cross-platform:

- **macOS** with Homebrew installed
- **Python 3.x** with the `google-genai` SDK (`pip install google-genai`)
- **Google Gemini API key** from Google AI Studio, exported as `GEMINI_API_KEY`
- **Android SDK command-line tools** (installed automatically by the setup script)
- **An Android Virtual Device (AVD)** named `AI_Agent_Phone` (created by the setup script)

### Setup Script

Google provides an idempotent setup script (`setup_emulator.sh`) that handles the entire Android SDK and emulator installation without requiring Android Studio:

```bash
chmod +x setup_emulator.sh
./setup_emulator.sh
```

The script installs:
- Android command-line tools via Homebrew
- Required Android SDK packages (platform-tools, emulator, system images)
- Creates the `AI_Agent_Phone` AVD

### Agent Script

The `agent.py` script provides a self-contained implementation that:

1. **Auto-discovers the Android SDK**: Searches common installation paths (`ANDROID_HOME` env var, `/opt/homebrew/share/android-commandlinetools`, `/usr/local/share/android-commandlinetools`) and configures the PATH automatically
2. **Launches the emulator in the background**: Starts the AVD as a daemon process and waits up to 120 seconds for it to boot (checking `sys.boot_completed`)
3. **Enters the computer use loop**: Sends screenshots and receives function calls until the task is complete

To run:

```bash
export GEMINI_API_KEY="your-key"
python agent.py "Open Settings and enable dark mode"
```

### Connecting to Remote Devices

The agent supports physical Android devices and remote cloud emulators via TCP/IP ADB connections:

```bash
adb connect <device-ip-address>:5555
```

Then pass the connection string as `device_id`:

```python
run_agent("Check the weather", device_id="35.200.100.10:5555")
```

This enables use cases like cloud-hosted device farms and CI/CD pipeline integration.

### System Prompt

The agent uses a concise system prompt that guides model behavior:

```
You are operating an Android phone.
* Use the provided tools to complete the task.
* Scroll down to inspect the full screen before assuming an element is missing.
* You can open apps by package name from anywhere.
* Type text only using the `type` tool. Do not use the virtual keyboard.
* If the task is already complete, state that directly.
```

## Relationship to Other Computer Use Approaches

See [[concepts/computer-use]] for the general computer use agent landscape, including OSWorld benchmarks, Pointer AI SOTA results, Phantom Tools phenomenon, and Dynamic Workflows integration.

Gemini 3.5 Flash Computer Use differs from existing approaches in its native model integration and multi-environment (browser + mobile + desktop) support:

### Claude Computer Use (Anthropic)

[[concepts/computer-use|Claude Computer Use]] is Anthropic's approach, available in Claude Opus and Sonnet models. Key differences:

| Dimension | Gemini Computer Use | Claude Computer Use |
|---|---|---|
| **Integration** | Native built-in tool in Gemini 3.5 Flash | Specialized capability in Claude models |
| **Environments** | browser, mobile, desktop | Primarily browser and desktop |
| **Mobile Support** | First-class `mobile` environment with dedicated actions | Not a primary focus |
| **Coordinate System** | 0-999 normalized grid (resolution-independent) | Pixel-based coordinates |
| **API Style** | Interactions API with function calling | Tool use API with computer tool |
| **Safety** | Safety decision system with auto-acknowledgment option | User confirmation prompts |
| **Benchmarks** | Not yet benchmarked on OSWorld | Claude Opus 4.8 at 84% on Online-Mind2Web |

Claude Computer Use has demonstrated strong results on desktop automation benchmarks (OSWorld), while Gemini Computer Use differentiates through its native multi-environment support, particularly the mobile environment for Android and potentially iOS devices.

### OpenAI Operator

OpenAI's Operator (announced 2025) is a different paradigm — a managed agent product that operates a cloud browser on the user's behalf, rather than a model-level tool that developers integrate into their own agent loops. Gemini Computer Use is closer to the developer-facing tool approach, giving builders full control over the execution environment, bridge implementation, and safety decisions.

### Google's Multi-Environment Strategy

Unlike competitors that focus on a single environment, Gemini 3.5 Flash treats computer use as a unified capability across browser, mobile, and desktop. The same model, same API, and same normalized coordinate system work across all three. The `mobile` environment is platform-agnostic: the model outputs the same actions regardless of whether the target is Android or iOS. Developers swap the bridge implementation (ADB for Android, simctl/Appium/go-ios for iOS) without changing the agent loop or model interaction.

This design connects to the broader [[concepts/mcp|Model Context Protocol (MCP)]] ecosystem pattern of standardized tool interfaces, though computer use is a native Gemini API tool rather than an MCP server.

## Limitations

### Current Constraints

- **macOS-only setup script**: The reference `setup_emulator.sh` is macOS-specific (uses Homebrew). Linux and Windows users must install Android SDK tooling manually
- **Synchronous execution**: The reference bridge and agent loop are synchronous, blocking on each ADB command. Production use requires async execution and retry logic
- **No virtual keyboard interaction**: The system prompt instructs the model to only use the `type` tool, which limits interaction with apps that require keyboard-based navigation
- **Single device**: The reference implementation targets one device at a time. Multi-device orchestration requires additional infrastructure
- **No visual grounding verification**: The model receives screenshots but the bridge does not verify that a click landed on the intended element; failures are only detected on the next turn
- **Emulator performance**: The Android emulator boot time (up to 120 seconds) limits rapid iteration. Cold-start scenarios are slow

### Safety Considerations

- **Safety decision handling**: The reference implementation auto-acknowledges safety decisions (`safety_acknowledgement: True`) for demonstration purposes. Production systems must inspect `step.arguments` for safety flags and prompt users before executing irreversible actions
- **Prompt injection risk**: Despite adversarial training, computer use agents are exposed to on-screen content that could contain injection attacks. Google recommends defense-in-depth with sandboxing, [[concepts/human-in-the-loop|human-in-the-loop]] verification, and strict access controls
- **State-modifying actions**: Actions like app installation, settings changes, and payments require careful review before automated execution

### Capability Gaps

- **No iOS reference implementation**: While the `mobile` environment is platform-agnostic, no official iOS bridge is provided. Building one requires integrating with Apple's simctl CLI, Appium, or go-ios
- **Limited error recovery**: The reference agent does not implement sophisticated error recovery — if ADB disconnects or an action fails, the loop may stall
- **No built-in retry logic**: Network drops, ADB timeouts, and API failures are not automatically retried

## Related Concepts

- [[concepts/computer-use]] — General computer use agent concept, OSWorld benchmarks, and broader ecosystem
- [[concepts/gemini/gemini-3-5-flash]] — The Gemini 3.5 Flash model with native computer use, search grounding, and other built-in tools
- [[concepts/mcp]] — Model Context Protocol for standardized tool interfaces between models and external systems
- [[concepts/human-in-the-loop]] — Safety pattern for requiring human approval on sensitive agent actions
- [[entities/google]] — Google, developer of Gemini models and the Gemini API
- [[entities/philipp-schmid]] — Author of the Gemini Android Computer Use guide, AI/ML developer advocate
