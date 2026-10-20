---
title: "Hands Off: Detecting Model Weight Tampering"
url: https://stealthium.io/blog/hands-off-detecting-model-weight-tampering
source: stealthium.io
date: 2026-10-19
fetched_at: 2026-10-20T11:03:53.384518Z
extraction: full
char_count: 20689
---

# Hands Off: Detecting Model Weight Tampering

> Source: https://stealthium.io/blog/hands-off-detecting-model-weight-tampering — saved 2026-10-20 for active crawl.

**Description:** This article introduces Rank-One Model Editing (ROME) attacks, where a malicious Python module rewrites a model&#x27;s weights in GPU memory to corrupt its answers, and explains why CPU-focused security tooling misses this class of attack. We then run a ROME attack in our lab and show how Stealthium detects model tampering via our runtime sensor, which ties every CUDA kernel launch back to the Python code that issued it, and new on-going research that detects the weight changes together with the call stack that caused it.

This article introduces Rank-One Model Editing (ROME) attacks, where a malicious Python module rewrites a model's weights in GPU memory to corrupt its answers, and explains why CPU-focused security tooling misses this class of attack. We then run a ROME attack in our lab and show how Stealthium detects model tampering via our runtime sensor, which ties every CUDA kernel launch back to the Python code that issued it, and new on-going research that detects the weight changes together with the call stack that caused it.

Models can be corrupted about a specific topic without a single byte on disk changing. There is nothing to scan, no process to catch, no signature to hunt and match. For everything and everyone watching the machine, it’s a model doing model things.

Traditional visibility and security tooling - EDRs on the host or ADRs hooking into the applications - are built to monitor process activity: opening files, spawning child processes, and communicating over the network. Rank-One Model Editing (ROME) attacks have none of the above. Here’s how we caught it anyway.

This post explores what runtime security for AI should look like: moving beyond the examination of AI workload processes to correlate activity across Slurm/K8s, the CUDA runtime, and GPU activity, while also analyzing model weights and inspecting computations as they run on a GPU.

Python is where GPU workloads start

A huge share of GPU work runs under a Python interpreter. PyTorch training jobs, vLLM and SGLang servers, ComfyUI workflows, JAX experiments, CuPy notebooks: different projects, one shape. Python coordinates, the compiled code runs on the device, and from the host all of them can look like the same python3 process using a GPU.

This has detection implications. The code that decides what runs is not always a standalone executable you can hash and sign. It arrives as a package you import, a model file you load, a string you evaluate at runtime, or a CUDA module built in memory and handed to the driver. Python's flexibility is what makes it good for AI work, and every one of those doors is also a way in.

Imports run code: Importing a package executes its initialization code. In the April 2026 lightning PyPI compromise (CVE-2026-44484) [1], affected versions 2.6.2 and 2.6.3 started a credential-stealing payload on import. The 2022 torchtriton dependency-confusion attack [2] also executed a malicious binary inside a PyTorch installation.

Startup files run before the application: A .pth file in site-packages can carry an executable import line. The March 2026 LiteLLM compromise [3] used that to start a credential stealer when Python started, before a single line of the application ran.

Model files can execute code: Unpickling can run arbitrary code. Researchers have found Hugging Face model files that opened reverse shells [4][5] or fetched a beacon on load [6]. A model file is not automatically safe just because it holds weights; formats such as safetensors avoid pickle execution, but plenty of models still ship as pickles.

Strings can become code: exec() and eval() run Python strings, while Triton and CuPy can compile GPU kernels at runtime. In a case Sysdig investigated [7], an Open WebUI plugin hid a payload behind 64 layers of decoding and exec(), and the decoded Python code ran in memory, never touching disk.

ROME-class attacks

ROME (Rank-One Model Editing) attacks, introduced by Meng and others in 2022 [8], make a small, targeted correction to one weight matrix in a middle layer. If you have never worked with models, TL;DR: a model is a big pile of numbers called weights; the whole thing is one giant multiplication of your input, and if you change a few of those numbers, you change what the model says.

It’s the technique behind Mithril Security's PoisonGPT [9].

Below is our reproduction. A small PyTorch transformer, a handful of questions and answers, served from a checkpoint on disk. Nothing in the transformer or the weights is a crafted artifact. The same command asks the same question and gets two answers with fundamentally different meanings, not the ordinary variation in wording you might expect from changing a model's temperature.

The checkpoint on disk did not change between the two runs, and no answer file was swapped in. What changed is a malicious imported library that injected itself into PyTorch. In the demo it arms itself with a ROME environment variable, applying the weight edit when the model is put into evaluation mode.

For those wondering about visibility of this attack: ROME attacks are standard inference plus a batch of extra CUDA kernel launches.

A CUDA launch is the CPU-side request for the GPU to run a kernel, a small program that performs parallel work on GPU data. The launch supplies the kernel's inputs and how the work is divided across GPU threads; it usually returns before the GPU finishes, so the CPU can continue while the GPU works.

The weights are patched directly in GPU memory. There is no file access, no extra ioctl, not even an mmap. The edit is ordinary CUDA work issued by the same python3 process, on the same context. Any tool or monitoring watching files, sockets, or the driver sees a normal inference job.

It’s an attack that never leaves the GPU. A poisoned library asks the GPU to do a little extra math and write the result over a few of the model’s numbers. Similar requests are made of the model thousands of times while answering a question. Nothing opened, nothing started, and nothing out across the network. Yet the model behavior is fundamentally compromised.

What Stealthium sees

Stealthium’s runtime sensor records the work around tensor values. Two hyperprints here: CudaLibraryLoad and CudaKernelLaunches, and when the work came from Python, they carry the Python caller stack.

In a ROME attack, CUDA launches for: the inference (the legitimate prompts + the inference ROME runs to trace the model) and the edit (computing the target weights, then writing them into the live weights on the GPU).

The inference kernels look the same for a casual prompt and for ROME; the caller stack behind them does not. Here is the same kernel twice in one CudaKernelLaunches hyperprint, trimmed:

CudaKernelLaunches { pid: 810177, gpu_index: 0, entries: [ // `SpaceLM.reply` entry is the user's question CudaKernelLaunchCount { kernel_name: "void at::native::vectorized_elementwise_kernel<4, at::native::CUDAFunctor_add<float>, ...>(...)", count: 3, delta: 3, caller_stack: [ { func: "SpaceLM.forward", file: "rome/model.py" }, { func: "Module._call_impl", file: "site-packages/torch/nn/modules/module.py" }, { func: "Module._wrapped_call_impl", file: "site-packages/torch/nn/modules/module.py" }, { func: "SpaceLM.reply", file: "rome/model.py" }, ], }, // The `_keys` entry is ROME running the same model to trace it CudaKernelLaunchCount { kernel_name: "void at::native::vectorized_elementwise_kernel<4, at::native::CUDAFunctor_add<float>, ...>(...)", count: 87, delta: 87, caller_stack: [ { func: "SpaceLM.forward", file: "rome/model.py" }, { func: "Module._call_impl", file: "site-packages/torch/nn/modules/module.py" }, { func: "Module._wrapped_call_impl", file: "site-packages/torch/nn/modules/module.py" }, { func: "_keys", file: "rome/calibration.py" }, ], }, // ... ], }

The rest of the edit launches kernels that never appear in a clean run, which is a second anomaly Stealthium alerts on. Tracing ends by collecting the captured keys:

kernel_name: "void at::native::(anonymous namespace)::CatArrayBatchedCopy_vectorized<...>(...)", caller_stack: [ { func: "_keys", file: "rome/calibration.py" }, { func: "_calibrate", file: "rome/calibration.py" }, { func: "_eval", file: "rome/calibration.py" }, { func: "<module>", file: "rome/space_chat.py" }, ],

Then, computing the malicious target weights:

kernel_name: "ampere_sgemm_32x128_nt", kernel_name: "void getrf_pivot<getrf_params_<float, 128, 1, 128, 128, 1> >(...)", caller_stack: [ { func: "_calibrate", file: "rome/calibration.py" }, { func: "_eval", file: "rome/calibration.py" }, { func: "<module>", file: "rome/space_chat.py" }, ],

Last, writing them into the live model weights in GPU memory:

kernel_name: "void at::native::vectorized_elementwise_kernel<4, at::native::CUDAFunctorOnSelf_add<float>, ...>(...)", caller_stack: [ { func: "_calibrate", file: "rome/calibration.py" }, { func: "_eval", file: "rome/calibration.py" }, { func: "<module>", file: "rome/space_chat.py" }, ],

This is beyond "a trusted Python workload used the GPU". calibration.py::_calibrate ran inference, solved a linear system and wrote to GPU memory, inside a process everyone trusts. Stealthium flags both anomalies, the unusual caller and the kernels a clean run never launches, telling the responder where to look.

Beyond CUDA

CUDA is one layer. On top of system-wide, CUDA, and direct GPU observability for workloads of any kind, Stealthium watches selected parts of the Python interpreter aimed at the entry points listed earlier:

PythonImport records what Python code was imported, the file path it resolved to, and who imported it. It can tell the standard-library secrets module apart from a local secrets.py with the same name. That covers the first door: imports that run code.

PythonExec records runtime exec, eval and compile, with the call stack, so it can show the decoded code a string-based loader actually ran. That covers the last door: strings that become code.

Detecting every Python monkey-patch is possible in principle, but instrumenting them all could add significant overhead to some workloads and produce noisy alerts for benign behavior in the standard library. Instead, Stealthium annotates hyperprints, including those for CUDA activity and direct ioctls, with the Python call stack that led to the activity. That context helps analysts distinguish legitimate workload behavior from anomalous activity when interpreting CudaLibraryLoad and CudaKernelLaunches hyperprints.

One level further: which weights changed

Stealthium’s runtime sensor connects GPU activity to the Python code that initiated it, giving responders visibility into how a workload uses the GPU and where suspicious behavior originates. Building on that foundation, here, our research is exploring a further complementary view: whether model weights changed, which tensors were affected, and what code path triggered the change.

A kernel launch alone cannot answer those questions. Its arguments are raw device pointers, and the same kernel that adds two tensors during a prompt can also add a correction to a weight matrix. To get that deeper view, we are examining framework-level signals and capturing the Python call stack at the point of change.

This effort aims to complement Stealthium’s existing runtime visibility. It observes where PyTorch (or other frameworks) records an in-place tensor change and captures the context at that moment. The result is an additional signal: a weight-change event tied to the tensor, the code path, and the process.

Research in action

Observe below. Every value is from the demo run; long arrays and absolute paths are shortened.

{ "timestamp": "2026-10-14T07:05:57.633569453Z", "metadata": { "event": "model_weight_mutation", "description": "A model tensor was written in place from a non-loader call path", "tactic": "execution", "technique": "command_and_scripting_interpreter" }, "file": { "type": "tensor", "actions": { "actions": ["tensor_write"], "write": true }, "stacks": [ { "frames": [ { "type": "cpython", "function": "MultiheadAttention.forward", "source": "torch/nn/modules/activation.py", "line": 1434 }, { "type": "cpython", "function": "Module._call_impl", "source": "torch/nn/modules/module.py", "line": 1793 }, { "type": "cpython", "function": "SpaceLM.forward", "source": "model.py", "line": 109 }, { "type": "cpython", "function": "_keys", "source": "calibration.py", "line": 40 }, { "type": "cpython", "function": "_calibrate", "source": "calibration.py", "line": 56 }, { "type": "cpython", "function": "_eval", "source": "calibration.py", "line": 87 }, { "type": "cpython", "function": "<module>", "source": "rome_eval.py", "line": 11 }, { "type": "native", "file": "libtorch_cpu.so" } ] } ] }, "process": { "comm": "python", "cmd": "python3.14", "exe": "/usr/bin/python3.14", "args": "./.venv/bin/python space_chat.py", "pid": 112618, "uid": 0, "namespaces": { ... } }, "context": { "ancestry": [ { "pid": 1, "comm": "systemd", "exe": "/usr/lib/systemd/systemd" }, { "pid": 998, "comm": "sshd", "exe": "/usr/sbin/sshd" }, { "pid": 71606, "comm": "sshd-session", "exe": "/usr/lib/openssh/sshd-session" }, { "pid": 71610, "comm": "bash", "exe": "/usr/bin/bash" }, { "pid": 112555, "comm": "sudo", "exe": "/usr/lib/cargo/bin/sudo" }, { "pid": 112618, "comm": "python", "exe": "/usr/bin/python3.14" } ], "files": [ { "path": "examples/gpu-python-torch-rome-poison/space_lm.pt", "type": "regular", "actions": ["open", "read", "close"] }, { "path": "examples/gpu-python-torch-rome-poison/__pycache__/calibration.cpython-314.pyc", "type": "regular", "actions": ["open", "read", "close"] }, { "path": "examples/gpu-python-torch-rome-poison/__pycache__/model.cpython-314.pyc", "type": "regular", "actions": ["open", "read", "close"] }, { "path": "/dev/nvidia0", "type": "char", "actions": ["mmap", "open"] }, { "path": "/dev/nvidia-uvm", "type": "char", "actions": ["mmap", "open"] }, { "path": "/usr/lib/x86_64-linux-gnu/libnvidia-ml.so.615.71.09", "type": "regular", "actions": ["mmap", "open", "read"] } ], "flows": [ { "proto": "TCP", "local": "10.209.14.136:54966", "remote": "3.174.141.63", "name": "huggingface.co", "port": 443, "status": "ended" }, { "proto": "UDP", "local": "127.0.0.1:52289", "remote": "127.0.0.53", "name": "resolver", "port": 53, "status": "ongoing" } ], "touched_files": 100, "network_flows": 2 ... } }

Event reading

The context is where a stack trace turns into a story. On its own, this event says a weight was written from calibration.py. With the context attached, the same event also says the process read the checkpoint (space_lm.pt), imported the library that does the edit (calibration.cpython-314.pyc), opened the GPU devices (/dev/nvidia0, /dev/nvidia-uvm), resolved a DNS name and held an HTTPS session to huggingface.co. This is all in the event, and distinguishes that a weight changed and what the process was doing when it did.

Stack as signal

The stack distinguishes these two kinds of tensor write. When a model loads, its weights are read into memory, and the framework increments the per-tensor version counter, just as it does during an edit. The action is the same, tensor_write; what differs is the call stack.

A load, benign, the same tensor_write action:

cpython _rebuild_tensor torch/_utils.py:199 cpython _rebuild_tensor_v2 torch/_utils.py:239 cpython Unpickler.load torch/_weights_only_unpickler.py:415 cpython _load torch/serialization.py:2240 cpython load torch/serialization.py:1604 cpython load space_chat.py:34 cpython <module> rome_eval.py:8

The ROME edit, the alert:

cpython MultiheadAttention.forward torch/nn/modules/activation.py:1434 cpython Module._call_impl torch/nn/modules/module.py:1793 cpython Module._wrapped_call_impl torch/nn/modules/module.py:1783 cpython SpaceLM.forward model.py:109 cpython _keys calibration.py:40 cpython _calibrate calibration.py:56 cpython _eval calibration.py:87 cpython <module> rome_eval.py:11

The first stack shows the loader - torch.load and load_state_dict- populating the weights as intended. The second shows an inference pass through SpaceLM.forward and MultiheadAttention.forward, called from _calibrate in calibration.py, a file that has no business modifying weights.

Detection: fire when a weight changes from a path with no loader behind it. It is the same principle as an EDR flagging a process that reads a credential file from a shell rather than from the authentication library: the action is normal, the caller is the tell.

It’s the same _calibrate that Stealthium pointed at from the kernel side. Two independent views, one from the GPU work and one from the framework's own bookkeeping, land on the same function.

Today’s visibility

Stealthium’s runtime sensor records useful views of GPU activity, including CudaLibraryLoad and CudaKernelLaunches. When that activity comes from Python, events carry the caller stack, giving teams context to investigate anomalies in real workloads. In the ROME example, that visibility connects suspicious kernel launches to the code that issued them.

These events help show what GPU work ran and where it came from. A kernel launch alone, however, does not reveal which model tensor changed: its arguments are raw device pointers, and the same kernel can participate in ordinary inference or in a weight edit. Looking into framework-level activity can add another perspective, connecting changes to tensors and the code paths behind them.

Expanding visibility across AI workloads

Stealthium continues to explore security questions across AI workloads and LLM internals: how Python and frameworks execute code, how workloads use GPUs, and how model weights and tensors behave as computations run. Different layers of visibility can help explain not just that something happened, but which workload, code path, or model component was involved.

The weight-mutation example is one way to investigate these questions. By observing where a framework records an in-place tensor change and capturing the Python call stack at that point, we can connect a candidate weight change to its tensor, code path, and process. It complements the runtime context available from GPU activity and helps build a broader picture of what is happening inside AI workloads.

Why bother chatting about our detections and research

ROME gives us a concrete way to examine both the value and the limits of runtime GPU visibility. It shows how kernel activity and its Python call stack can help teams investigate anomalies, and why looking deeper into frameworks and model behavior can provide additional context.

Our work continues across multiple security challenges in AI, with the aim of increasing visibility into workloads and LLM internals. By sharing this experiment, including the challenges in distinguishing legitimate loading from a later edit, we hope to make the problem clearer and contribute to a richer understanding of how to secure AI systems.

If you’re interested in seeing our platform in action, head here.

And if you’re interested in joining the mission, our team is always growing, head here!

References

GitHub Advisory Database, "Compromise of PyTorch Lightning PyPI Package Versions" (CVE-2026-44484), 30 Apr 2026. https://github.com/advisories/GHSA-w37p-236h-pfx3 ↩

PyTorch Foundation, "Compromised PyTorch-nightly dependency chain between December 25th and December 30th, 2022", 31 Dec 2022. https://pytorch.org/blog/compromised-nightly-dependency/ ↩

StepSecurity, "litellm: credential stealer hidden in PyPI wheel" (litellm_init.pth in 1.82.7/1.82.8), 24 Mar 2026. https://www.stepsecurity.io/blog/litellm-credential-stealer-hidden-in-pypi-wheel ↩

ReversingLabs, "nullifAI: malicious pickle models evaded Hugging Face's scanner", Feb 2025. https://www.reversinglabs.com/blog/rl-identifies-malware-ml-model-hosted-on-hugging-face ↩

JFrog Security Research, "Data scientists targeted by malicious Hugging Face ML models with silent backdoor", Feb 2024. https://jfrog.com/blog/data-scientists-targeted-by-malicious-hugging-face-ml-models-with-silent-backdoor/ ↩

Rapid7, "From .pth to p0wned: abuse of pickle files in AI model supply chains", Jul 2025. https://www.rapid7.com/blog/post/from-pth-to-p0wned-abuse-of-pickle-files-in-ai-model-supply-chains/ ↩

Sysdig Threat Research Team, "Attacker exploits misconfigured AI tool to run AI-generated payload" (Open WebUI), Jun 2025. https://www.sysdig.com/blog/attacker-exploits-misconfigured-ai-tool-to-run-ai-generated-payload ↩

K. Meng, D. Bau, A. Andonian, Y. Belinkov, "Locating and Editing Factual Associations in GPT" (ROME), NeurIPS 2022. https://arxiv.org/abs/2202.05262 ↩

Mithril Security, "PoisonGPT: how we hid a lobotomized LLM on Hugging Face to spread fake news", Jul 2023. https://blog.mithrilsecurity.io/poisongpt-how-we-hid-a-lobotomized-llm-on-hugging-face-to-spread-fake-news/ ↩

We're hiring at Stealthium

If this is the kind of problem you enjoy spending your time on, come join us!

OPEN ROLES

Software Security Researcher, GPU and AI Systems

Senior Software Engineer - Observability / Runtime Systems

Enterprise Account Executive, North America

Software Engineer (Platform Engineering)
