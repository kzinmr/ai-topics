---
type: article
date: 2026-06-24
source: https://github.com/ekzhang/jax-js
author: Eric Zhang
title: "jax-js: JAX in pure JavaScript – ML library for the web"
repo_created: 2025-02-04
last_commit: 2026-06-24
stars: 845
forks: 53
license: MIT
language: TypeScript
topics:
  - javascript
  - webgl
  - machine-learning
  - numpy
  - wasm
  - jit
  - neural-networks
  - webgpu
  - jax
npm: "@jax-js/jax"
website: https://jax-js.com
---

# jax-js: JAX in pure JavaScript

**GitHub**: https://github.com/ekzhang/jax-js
**Website**: https://jax-js.com
**API Reference**: https://jax-js.com/docs
**npm**: `@jax-js/jax`
**Discord**: https://discord.gg/BW6YsCd4Tf

**jax-js** is a machine learning framework for the browser. It aims to bring JAX-style, high-performance CPU and GPU kernels to JavaScript, so you can run numerical applications on the web.

Under the hood, it translates array operations into a compiler representation, then synthesizes kernels in WebAssembly and WebGPU.

The library is written from scratch, with zero external dependencies. It maintains close API compatibility with NumPy/JAX. Since everything runs client-side, jax-js is likely the most portable GPU ML framework, since it runs anywhere a browser can run.

## Key Stats

- **Stars**: 845
- **Forks**: 53
- **License**: MIT
- **Repository Created**: February 4, 2025
- **Last Commit**: June 24, 2026
- **Bundle Size (gzip)**: 80 KB
- **Latest Release**: 2026

## Quickstart

```javascript
import { numpy as np } from "@jax-js/jax";

// Array operations, compatible with JAX/NumPy.
const x = np.array([1, 2, 3]);
const y = x.mul(4); // [4, 8, 12]
```

## Web Usage (CDN)

In vanilla JavaScript (without a bundler), just import from a module script tag:

```html
<script type="module">
  import { numpy as np } from "https://esm.sh/@jax-js/jax";
</script>
```

## Platforms

| Platform | CPU (Wasm) | GPU (WebGPU) | GPU (WebGL) |
|---|---|---|---|
| Chrome / Edge | ✅ | ✅ | ✅ |
| Firefox | ✅ | ✅ (macOS 26+) | ✅ |
| Safari | ✅ | ✅ (macOS 26+) | ✅ |
| iOS | ✅ | ✅ (iOS 26+) | ✅ |
| Chrome for Android | ✅ | ✅ | ✅ |
| Firefox for Android | ✅ | ❌ | ✅ |
| Node.js | ✅ | ❌ | ❌ |
| Deno | ✅ | ✅ (async) | ❌ |

## Key Features

### Autodiff & JIT
- **Gradients**: ✅ (automatic differentiation)
- **Jacobian and Hessian**: ✅
- **jvp() forward differentiation**: ✅
- **jit() kernel fusion**: ✅ (records execution graph, fuses operations)
- **vmap() auto-vectorization**: ✅
- **Graph capture**: ✅

### Backends & Data
- **WebGPU backend**: ✅ (recommended for best performance)
- **WebGL backend**: ✅ (best-effort basis)
- **Wasm (CPU) backend**: ✅ (multi-threaded with SharedArrayBuffer)
- **Eager array API**: ✅
- **ONNX models**: 🟡 Partial
- **Safetensors**: ✅
- **Mixed precision**: ✅
- **Mixed devices**: ✅

### Data Types
- Float64: ✅
- Float32: ✅
- Float16: ✅
- BFloat16: ❌
- Packed Uint8: ❌

### Ops & Numerics
- Arithmetic functions, Matrix multiplication, General einsum: ✅
- Sorting: ✅
- n-d convolutions: ✅
- Cholesky, Lstsq, LU, Solve, Determinant: ✅
- FFT: ✅
- Basic and Advanced RNG: ✅
- SVD: ❌

## Performance

- **On WebGPU**: Over **7000 GFLOP/s** for matrix multiplication on an Apple M4 Max chip
- **On WebAssembly (CPU)**: Fastest multithreaded in-browser matrix multiplication, over twice as fast as XNNPACK, matches **OpenBLAS performance** on Apple Silicon
- Significantly faster than both TensorFlow.js and ONNX Runtime Web

## Example Applications & Demos

### Community Usage
- **g9-jaxjs**: Automatically interactive graphics with forward-mode AD
- **autoresearch-webgpu**: Auto-research, in the browser
- **tanh.xyz**: Interactive ML visualizations
- **handwritten**: Handwriting synthesis with LSTM-MDN
- **jax-js-bayes**: Declarative Bayesian modeling library

### Official Demos (on jax-js.com)
- Chat with Gemma 3
- Training neural networks on MNIST
- Voice cloning: Kyutai Pocket TTS
- Speech recognition: OpenAI Whisper
- CLIP embeddings for books in-browser
- Object detection: D-FINE (ONNX)
- Object detection: DETR ResNet-50 (ONNX)
- Fluid simulation (Navier-Stokes)
- Neural cellular automata
- In-browser REPL
- Matmul / Matvec / Conv2d benchmarks
- Mandelbrot set

## Feature Comparison vs Alternatives

| Feature | jax-js | TensorFlow.js | onnxruntime-web |
|---|---|---|---|
| **API style** | JAX/NumPy | TensorFlow-like | Static ONNX graphs |
| **Latest release** | 2026 | ⚠️ 2024 | 2026 |
| **Speed** | Fastest | Fast | Fastest |
| **Bundle size (gzip)** | 80 KB | 269 KB | 90 KB + 24 MB Wasm |
| **Gradients** | ✅ | ✅ | ❌ |
| **jit() kernel fusion** | ✅ | ❌ | ❌ |
| **vmap() auto-vectorization** | ✅ | ❌ | ❌ |
| **WebGPU backend** | ✅ | 🟡 Preview | ✅ |
| **ONNX models** | 🟡 Partial | ❌ | ✅ |
| **Float64** | ✅ | ❌ | ❌ |
| **Mixed precision** | ✅ | ❌ | ✅ |
| **General einsum** | ✅ | 🟡 Partial | 🟡 Partial |

## Devices

jax-js has 4 device backends:

1. **cpu**: Slow, interpreted JS (debugging only)
2. **wasm**: WebAssembly, multi-threaded when SharedArrayBuffer is available
3. **webgpu**: WebGPU (recommended for best performance, especially neural networks)
4. **webgl**: WebGL2 via fragment shaders (older, slower, best-effort)

```javascript
import { defaultDevice, init } from "@jax-js/jax";

const devices = await init(); // Starts all available backends.

if (devices.includes("webgpu")) {
  defaultDevice("webgpu");
} else {
  console.warn("WebGPU is not supported, falling back to Wasm.");
}
```

## Helper Libraries

- **@jax-js/loaders**: Load tensors from Safetensors, BPE tokenizer, HTTP caching in OPFS
- **@jax-js/onnx**: Load ONNX models into native jax-js functions
- **@jax-js/optax**: Optimizers (Adam, SGD, etc.)

## Development

- **Package manager**: pnpm
- **Test framework**: Vitest (headless browser with Playwright, older version for WebGPU support)
- **Linting**: ESLint, Prettier, TypeScript type checking

```bash
pnpm install
pnpm run build:watch
pnpm exec playwright install
pnpm test
pnpm -C website dev  # Start Vite dev server
```

## Future Work / Help Wanted

- Adding support for more JAX functions and operations
- Improving performance of WebGPU and Wasm runtimes
- Making a fast, general transformer inference engine or model library

## Author

Eric Zhang (ekzhang on GitHub) — creator of jax-js, a from-scratch JAX implementation in pure JavaScript/TypeScript.
