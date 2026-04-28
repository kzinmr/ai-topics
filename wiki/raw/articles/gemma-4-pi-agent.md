# How to run a local coding agent with Gemma 4 and Pi | Patrick Loeber

**URL:** https://patloeber.com/gemma-4-pi-agent/
**Author:** Patrick Loeber
**Date:** 2026-04-28
**Source:** Retrieved via web_extract

---

## 🔑 Key Excerpts & Code Snippets

### Model Configuration (`~/.pi/agent/models.json`)
```json
{
  "providers": {
    "lmstudio": {
      "baseUrl": "http://localhost:1234/v1",
      "api": "openai-completions",
      "apiKey": "lm-studio",
      "models": [
        {
          "id": "google/gemma-4-26b-a4b",
          "input": ["text", "image"]
        }
      ]
    }
  }
}
```

### Essential Commands
```bash
# Verify LM Studio server is running
curl http://localhost:1234/v1/models

# Install Pi globally
npm install -g @mariozechner/pi-coding-agent

# Install community skills (user-level)
git clone https://github.com/badlogic/pi-skills ~/.pi/agent/skills/pi-skills

# Load an extension
pi --extension examples/extensions/permission-gate.ts
```

### Performance Note
> **Note:** Even though the model only activates 4B parameters per token, all 26B parameters must be loaded into memory for fast routing. That's why VRAM requirements are closer to a dense 26B model.

---

## 📖 Comprehensive Summary

### 🧠 Model Selection & Specs
- **Gemma 4** is Google's latest open-weight family (Apache 2.0 license). Key upgrades for agentic use: native function calling, system prompt support, and thinking modes.
- **Recommended Model:** `Gemma 4 26B A4B` (Mixture-of-Experts)
  - **Architecture:** 26B total parameters, but only **4B activate per token**. Delivers large-model quality with small-model inference speed.
  - **Capabilities:** Text, image understanding, function calling, thinking modes.
  - **Context Length:** Up to 256K tokens.
- **Quantization Options:**
  | Quantization | Size | Quality |
  |--------------|------|---------|
  | `Q4_K_M`     | 18 GB | Good balance |
  | `Q6_K`       | 24 GB | Higher quality |
  | `Q8_0`       | 28 GB | Near-original |
- **Mac Users:** Consider MLX versions for native Apple Silicon optimization.

### ⚙️ Setup & Configuration Workflow
1. **Install LM Studio:** Desktop app for model management & OpenAI-compatible API. Alternatives: `Ollama`, `llama-server`.
2. **Download & Load:** Search `gemma-4-26b-a4b` in LM Studio, download GGUF quantized version, and start server via Developer tab.
3. **Server Endpoint:** Runs at `http://localhost:1234` by default.
4. **Install Pi:** Minimal terminal coding harness by Mario Zechner. Deliberately small core (4 tools: `read`, `write`, `edit`, `bash`) to maximize token efficiency for local models.
5. **Connect Pi:** Point `models.json` to LM Studio's base URL. Launch with `pi` and switch models via `/model`.

### 📊 Context Size vs. VRAM Tradeoff
Context size directly impacts VRAM overhead. Coding agents accumulate heavy session context, making larger contexts highly beneficial.
| Use Case | Context Size | Additional VRAM |
|----------|--------------|-----------------|
| Small edits | 16K | ~1 GB |
| Standard coding | 64K | ~4 GB |
| Multi-file refactors | 128K | ~8 GB |
| Full repo context | 256K | ~16 GB |
- **Recommendation:** `128K` if VRAM allows. Out-of-memory errors should be resolved by lowering context first.
- **GPU Offload:** Maximize layers on GPU for speed. Splits to CPU if needed. Keep at maximum (30 for 26B A4B).

### 🛠️ Pi Agent Features & Customization
- **Session Management:**
  - `/compact` → Summarizes older messages to free context
  - `/new` → Fresh session
  - `/tree` → Navigate session history
  - `/fork` → Branch from a past message without losing history
- **Skills:** On-demand Markdown-based capability packages following the Agent Skills standard. Invoke via `/skill:name` or auto-discovery.
  - *Notable Skills:* `liteparse` (doc parsing for image-only models), `frontend-slides`, `grill-me` (idea iteration), `gemini-skills`
- **Extensions:** TypeScript modules for custom tools, UI, permissions, and sub-agents.
- **Execution Mode:** Pi runs **YOLO by default** (executes bash commands without confirmation). Fast but risky. Use `permission-gate` for prompts or `cco`/`sandbox` for containerized safety.

### 📚 Resources & Acknowledgements
- [Gemma 4 Documentation & Model Card](https://ai.google.dev/gemma/docs/core)
- [LM Studio](https://lmstudio.ai/)
- [Pi Coding Agent & Skills/Extensions Docs](https://github.com/badlogic/pi-mono)
- *Acknowledgements:* Colleague Ian for setup guidance & video guide.
