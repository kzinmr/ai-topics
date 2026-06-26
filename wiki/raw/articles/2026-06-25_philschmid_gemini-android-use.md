---
title: "Control an Android Phone with Gemini 3.5 Flash Computer Use"
source_url: "https://www.philschmid.de/gemini-android-use"
date: 2026-06-25
author: "Philipp Schmid"
captured: 2026-06-25
---

Gemini 3.5 Flash has [built-in Computer Use](https://blog.google/innovation-and-ai/models-and-research/gemini-models/introducing-computer-use-gemini-3-5-flash/). The model looks at a screenshot, decides what to do, and returns a function call like `click(y=300, x=500)`. You execute that action on the device via ADB, take a new screenshot, and send it back. Repeat until the task is done.

This guide walks you through controlling an Android emulator using the `mobile` environment and the Python SDK.

Github Repository: https://github.com/google-gemini/gemini-android-computer-use-quickstart 

## What is Computer Use?

[Computer Use](https://ai.google.dev/gemini-api/docs/computer-use) is a native tool in Gemini 3.5 Flash. You give the model a screenshot and a goal ("open Settings and turn on dark mode"). The model returns structured actions: taps, text input, swipes, app launches. Your code executes those actions on the target device.

It works like function calling. The model proposes actions, you execute them, you send back the result. The model stays in the loop through screenshots.

Gemini supports three Computer Use environments: `browser` for desktop web automation, `mobile` for mobile devices/emulators, and `desktop` for operating system-level control. This guide uses `mobile`.

```
  Screenshot ──> Gemini 3.5 Flash ──> function_call
      ▲                                    │
      │                                    ▼
      └──────── Execute via ADB ◄──────────┘
```

### Pseudocode

```python
from google import genai

client = genai.Client()
bridge = ADBBridge()

# Take initial screenshot and send first request
screenshot = bridge.screenshot()

interaction = client.interactions.create(
    model="gemini-3.5-flash",
    input=[
        {"type": "text", "text": "Open Settings and enable dark mode"},
        {"type": "image", "data": b64(screenshot), "mime_type": "image/png"},
    ],
    tools=[{"type": "computer_use", "environment": "mobile"}],
)

# Agent loop: execute actions, send results back
while interaction has function_calls:
    for call in interaction.function_calls:
        bridge.execute(call.name, call.args)  # click, type, open_app...

    screenshot = bridge.screenshot()
    interaction = client.interactions.create(
        model="gemini-3.5-flash",
        previous_interaction_id=interaction.id,
        input=[function_results + screenshot],
        tools=[{"type": "computer_use", "environment": "mobile"}],
    )

print(interaction.output_text)
```

### Supported actions (mobile environment)

These are the actions the model can request when using `environment: "mobile"`. Your code must handle each one.

| Action | Description | Arguments |
|--------|-------------|-----------|
| `open_app` | Opens an app by name | `app_name: str`, `intent: str` (optional) |
| `click` | Tap a screen coordinate | `y: int (0-999)`, `x: int (0-999)` |
| `type` | Type text | `text: str`, `press_enter: bool` (default false) |
| `long_press` | Long-press a coordinate | `y: int (0-999)`, `x: int (0-999)`, `seconds: int` (default 2) |
| `drag_and_drop` | Drag between two points | `start_y`, `start_x`, `end_y`, `end_x` |
| `press_key` | Press a key (home, back, enter...) | `key: str` |
| `go_back` | Navigate back | (none) |
| `wait` | Pause execution | `seconds: int` (default 1) |
| `list_apps` | List installed apps | (none) |
| `take_screenshot` | Capture the screen | (none) |

Coordinates are normalized to a 0-999 grid. `(0, 0)` is top-left, `(999, 999)` is bottom-right. Your bridge converts these to actual pixel coordinates based on the device resolution.

## Setup

No Android Studio GUI required. Run the [setup script](https://github.com/google-gemini/gemini-android-computer-use-quickstart/blob/main/setup_emulator.sh) on your Mac to install the Android SDK, emulator, and create a virtual device from the terminal.

### 1. Run the setup script

Install script link: https://github.com/google-gemini/gemini-android-computer-use-quickstart/blob/main/setup_emulator.sh

```bash
chmod +x setup_emulator.sh
./setup_emulator.sh
```

### 2. Install Python dependencies

```bash
pip install google-genai
```

The Python agent script handles locating SDK paths and starting the emulator in the background automatically, so no additional manual environment variable exporting or terminal setup is required.

## The agent loop

Full working script [agent.py](https://github.com/google-gemini/gemini-android-computer-use-quickstart/blob/main/agent.py). It automatically sets up the environment variables, launches the emulator in the background (if it isn't already running), waits for it to boot, and begins the Computer Use loop.

```python
import base64
import json
import os
import re
import subprocess
import sys
import time

from google import genai

BASE_DIR = os.path.dirname(os.path.abspath(__file__))


def setup_android_env():
    paths_to_check = [
        os.environ.get("ANDROID_HOME"),
        "/opt/homebrew/share/android-commandlinetools",
        "/usr/local/share/android-commandlinetools",
    ]
    
    android_home = None
    for p in paths_to_check:
        if p and os.path.exists(p):
            android_home = p
            break
            
    if not android_home:
        print("Error: ANDROID_HOME not found. Run setup_emulator.sh first.", file=sys.stderr)
        sys.exit(1)
        
    os.environ["ANDROID_HOME"] = android_home
    sdk_paths = [
        os.path.join(android_home, "cmdline-tools", "latest", "bin"),
        os.path.join(android_home, "emulator"),
        os.path.join(android_home, "platform-tools"),
    ]
    
    current_path = os.environ.get("PATH", "")
    for p in sdk_paths:
        if p not in current_path:
            current_path = p + os.pathsep + current_path
            
    os.environ["PATH"] = current_path
    return android_home


def start_emulator(avd_name="AI_Agent_Phone"):
    setup_android_env()
    
    try:
        res = subprocess.run(["adb", "devices"], capture_output=True, text=True)
        if "emulator" in res.stdout:
            return
    except FileNotFoundError:
        pass

    print(f"Starting emulator '{avd_name}'...")
    log_file = open(os.path.join(BASE_DIR, "emulator.log"), "w")
    
    subprocess.Popen(
        ["emulator", "-avd", avd_name, "-delay-adb"],
        stdout=log_file,
        stderr=log_file,
        start_new_session=True,
    )
    
    print("Waiting for emulator to boot...")
    for _ in range(60):
        try:
            res = subprocess.run(["adb", "devices"], capture_output=True, text=True)
            if "emulator" in res.stdout:
                boot_res = subprocess.run(
                    ["adb", "shell", "getprop", "sys.boot_completed"],
                    capture_output=True,
                    text=True,
                )
                if boot_res.stdout.strip() == "1":
                    print("Emulator ready.")
                    return
        except Exception:
            pass
        time.sleep(2)
        
    print("Error: Emulator failed to boot.", file=sys.stderr)
    sys.exit(1)


class ADBBridge:
    def __init__(self, device_id=None):
        self.prefix = ["adb"] + (["-s", device_id] if device_id else [])
        self.width, self.height = self._screen_size()

    def _run(self, args, check=True):
        result = subprocess.run(self.prefix + args, capture_output=True, text=True)
        if check and result.returncode != 0:
            raise RuntimeError(f"ADB error: {result.stderr.strip()}")
        return result.stdout

    def _screen_size(self):
        output = self._run(["shell", "wm", "size"])
        match = re.search(r"Physical size: (\d+)x(\d+)", output)
        return (int(match.group(1)), int(match.group(2))) if match else (1080, 1920)

    def _px(self, x, y):
        return int(x / 1000 * self.width), int(y / 1000 * self.height)

    def click(self, y, x, **_):
        px, py = self._px(x, y)
        self._run(["shell", "input", "tap", str(px), str(py)])

    def type(self, text, press_enter=False, **_):
        self._run(["shell", "input", "text", text.replace(" ", "%s")])
        if press_enter:
            self._run(["shell", "input", "keyevent", "66"])

    def open_app(self, app_name=None, package_name=None, **_):
        pkg = app_name or package_name
        if not pkg:
            raise ValueError("open_app requires app_name or package_name")
            
        stdout = self._run(["shell", "monkey", "--pct-syskeys", "0", "-p", pkg,
                            "-c", "android.intent.category.LAUNCHER", "1"], check=False)
        if "No activities found" in stdout or "monkey aborted" in stdout:
            raise RuntimeError(f"App {pkg} is not installed or has no launcher activity.")

    def scroll(self, y, x, direction, magnitude=800, **_):
        px, py = self._px(x, y)
        dist = int(magnitude / 1000 * self.height)
        dx, dy = {"up": (0, -dist), "down": (0, dist),
                  "left": (-dist, 0), "right": (dist, 0)}.get(direction, (0, 0))
        self._run(["shell", "input", "swipe", str(px), str(py),
                   str(px + dx), str(py + dy), "300"])

    def long_press(self, y, x, seconds=2, **_):
        px, py = self._px(x, y)
        self._run(["shell", "input", "swipe", str(px), str(py),
                   str(px), str(py), str(seconds * 1000)])

    def drag_and_drop(self, start_y, start_x, end_y, end_x, **_):
        sx, sy = self._px(start_x, start_y)
        ex, ey = self._px(end_x, end_y)
        self._run(["shell", "input", "swipe", str(sx), str(sy),
                   str(ex), str(ey), "300"])

    def press_key(self, key, **_):
        keymap = {"home": "3", "back": "4", "enter": "66",
                  "app_switch": "187", "menu": "82"}
        self._run(["shell", "input", "keyevent", keymap.get(key.lower(), key)])

    def go_back(self, **_):
        self._run(["shell", "input", "keyevent", "4"])

    def wait(self, seconds=1, **_):
        time.sleep(seconds)

    def list_apps(self, **_):
        output = self._run(["shell", "pm", "list", "packages", "-3"])
        apps = [l.split(":")[1] for l in output.splitlines() if l.startswith("package:")]
        if not apps:
            return {"apps": "No third-party apps installed on this device."}
        return {"apps": apps}

    def take_screenshot(self, **_):
        return None

    def screenshot(self) -> bytes:
        result = subprocess.run(
            self.prefix + ["exec-out", "screencap", "-p"], capture_output=True
        )
        return result.stdout


SYSTEM_PROMPT = """You are operating an Android phone.
* Use the provided tools to complete the task.
* Scroll down to inspect the full screen before assuming an element is missing.
* You can open apps by package name from anywhere.
* Type text only using the `type` tool. Do not use the virtual keyboard.
* If the task is already complete, state that directly.
"""


def run_agent(task: str, device_id: str = None, max_turns: int = 100):
    start_emulator()
    client = genai.Client()
    bridge = ADBBridge(device_id)

    print(f"\nTask: {task}")
    print("-" * 40)

    screenshot_bytes = bridge.screenshot()
    user_input = [
        {"type": "text", "text": task},
        {
            "type": "image",
            "data": base64.b64encode(screenshot_bytes).decode(),
            "mime_type": "image/png",
        },
    ]
    
    previous_interaction_id = None
    turn = 0
    
    while turn < max_turns:
        turn += 1
        
        interaction = client.interactions.create(
            model="gemini-3.5-flash",
            system_instruction=SYSTEM_PROMPT,
            input=user_input,
            tools=[{"type": "computer_use", "environment": "mobile"}],
            previous_interaction_id=previous_interaction_id,
        )
        
        function_responses = []
        for step in interaction.steps:
            if step.type == "function_call":
                print(f"[function_call] {step.name}({step.arguments})")
                handler = getattr(bridge, step.name, None)
                result_text = {"status": "ok"}
                
                if handler:
                    try:
                        res = handler(**step.arguments)
                        if isinstance(res, dict):
                            result_text.update(res)
                    except Exception as e:
                        result_text = {"status": "error", "error": str(e)}
                else:
                    result_text = {"status": "error", "error": f"Unknown action: {step.name}"}
                    
                print(f"[function_result] {result_text}")
                
                if "safety_decision" in step.arguments:
                    # auto approve safety decisions for demo
                    result_text["safety_acknowledgement"] = True

                screenshot_bytes = bridge.screenshot()
                
                fr = {
                    "type": "function_result",
                    "name": step.name,
                    "call_id": step.id,
                    "result": [
                        {"type": "text", "text": json.dumps(result_text)},
                        {
                            "type": "image",
                            "data": base64.b64encode(screenshot_bytes).decode(),
                            "mime_type": "image/png",
                        },
                    ],
                }
                function_responses.append(fr)
            else:
                print(f"\nResult: {interaction.output_text}")
                break
                
        user_input = function_responses
        previous_interaction_id = interaction.id
        
        if not function_responses:
            break
            
    return interaction


if __name__ == "__main__":
    task_desc = "Find the latest blog post from philipp schmid and summarize it."
    if len(sys.argv) > 1:
        task_desc = " ".join(sys.argv[1:])
    run_agent(task_desc)
```

### How to run it

```bash
# Set your API key
export GEMINI_API_KEY="your-key"

# Run the agent (starts the emulator automatically if needed)
python agent.py "Open Settings and enable dark mode"
```

## Connecting to a Remote Device

You can also target physical Android devices or remote cloud emulators instead of a local virtual device. 

1.  **Enable USB/Wireless Debugging**: On your target device, enable Developer Options and turn on USB Debugging or Wireless Debugging.
2.  **Connect via ADB**: Use the `adb connect` command to link to a remote device over TCP/IP:
    ```bash
    adb connect <device-ip-address>:5555
    ```
    For details on setting up wireless debugging, refer to the official [Android developer documentation on ADB over Wi-Fi](https://developer.android.com/tools/adb#wireless).
3.  **Pass the Device ID to the Agent**: Pass the remote device's connection string as the `device_id` parameter to target it in the agent loop:
    ```python
    # Target a remote or cloud-hosted emulator
    run_agent("Check the weather", device_id="35.200.100.10:5555")
    ```

## Next Steps & Developer Tips

I hope this gets you started with Gemini 3.5 Flash Computer Use on mobile. Next steps can be:

*   **Supporting iOS / iPhone**: The Gemini API's `mobile` environment is platform-agnostic. The model outputs actions (clicks, swipes, types) on the same normalized `0-999` grid regardless of whether the device is Android or iOS. To target an iPhone or iOS Simulator, you only need to swap out `ADBBridge` with an iOS-compatible tool—such as Apple's `simctl` CLI for simulator control, Appium, or [go-ios](https://github.com/danielpaulus/go-ios) for physical devices.
*   **Production Robustness**: The Python bridge code provided here is synchronous and optimized for demonstration. For production use, you should implement robust retry logic for network drops, handle ADB disconnects gracefully, and execute operations asynchronously.
*   **Handling Safety Decisions**: In real-world tasks (especially those modifying state or making payments), the model might flag action steps with a `safety_decision` requesting confirmation. Ensure your production loop inspects `step.arguments` for safety flags and prompts the user before executing the action. See the [Gemini API Computer Use Safety Guidelines](https://ai.google.dev/gemini-api/docs/computer-use#safety-decisions) for details.

--- 

Thanks for reading! If you have any questions or feedback, please let me know on [Twitter](https://twitter.com/_philschmid) or [LinkedIn](https://www.linkedin.com/in/philipp-schmid-a6a2bb196/).
