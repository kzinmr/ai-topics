---
title: "thinkingmachines_end-to-end-4-bit-training"
url: https://thinkingmachines.ai/blog/end-to-end-4-bit-training/
date: 2026-11-13
fetched_at: 2026-11-15T11:10:00Z
source: active-crawl
status: raw
---

End‑to‑End 4‑Bit Training - Thinking Machines LabTHINKING MACHINESEnd‑to‑End 4‑Bit Training

Claude Monet’s The Seine at Vétheuil, “quantized” to 16 colors

Training large language models involves calculating and storing a lot of numbers. Using fewer bits for each value reduces memory usage and allows GPUs to perform calculations faster. However, there is a tradeoff: fewer bits also mean fewer representable numbers, leading to more aggressive rounding. Lower-precision representations ultimately hurt accuracy by adding error to the calculations.

For example, suppose we want to store the number 3.2, but the nearest values our numerical format can represent are 3 and 4. Rounding to 3 introduces a quantization error of −0.2-0.2−0.2, the difference between the actual value and the one that can be represented in the quantized format. A single error like this may seem small, but these errors accumulate over training as rounding happens repeatedly across layers and optimization steps, which can impair the learning process.

This is the central challenge of low-precision training: how can we benefit from faster arithmetic without introducing errors that interfere with learning?

We manage this tradeoff through our use of three key numerical formats during training: BF16, MXFP8, and NVFP4. Each format’s precision is fixed, but its speed depends on the hardware being used. We train on NVIDIA’s Grace Blackwell Ultra platform, the GB300, which is designed to optimize matrix multiplications with NVFP4. Notably, NVFP4 is stored with 3.6x fewer bits than BF16, but it runs up to 6x faster on GB300s.

Numerical formatsNumerical format

Bits per value

GB300 PFLOPS

NVFP4

(4 × 16 + 8) ÷ 16 = 4.5

15

MXFP8

(8 × 32 + 8) ÷ 32 = 8.25

5

BF16

16

2.5

The NVFP4 acceleration on GB300s is very useful in high-volume inference, where the tradeoff leans in favor of speed. But compared to BF16 and MXFP8, the format greatly increases quantization error. This error matters more at different stages of training, and the tradeoff must be considered for each one separately: forward and backward passes in pretraining and supervised fine-tuning (SFT), sampling and training in reinforcement learning (RL).

Our priorities during different stages of training

Risks

Rewards

Minimizing error

Minimizing bias

Increasing speed

Reducing memory footprint

Pretraining forward

3 checkmarks

—

2 checkmarks

—

Pretraining backward

1 checkmark

3 checkmarks

2 checkmarks

—

RL sampler

3 checkmarks

—

3 checkmarks

3 checkmarks

RL trainer

1 checkmark

3 checkmarks

1 checkmark

—

Speed matters most in high-volume steps: pretraining, which runs on trillions of tokens, and RL sampling, which generates tens of thousands of tokens in each rollout. Each sampled token also requires loading the model’s weights from global memory, the cost of which scales with the number of bits needed to store the weights.

The backward passes that update the weights average over many tokens in a batch, which dilutes the impact of randomly distributed rounding errors. However, backward passes are very sensitive to quantization bias, introduced when values consistently round up or down during quantization. Instead of averaging out, this bias can compound across layers, samples, and training steps.

In training Inkling 2 Small, we made the following decisions:

NVFP4 precision in the expert layers for forward passes, bolstered by a dedicated kernel.

MXFP8 precision for backward passes with re-quantization and stochastic rounding, techniques for reducing gradient bias.

Quantization techniques for accelerating GPU communications, which alleviated a bottleneck that surfaced after we sped up computation.

Inkling 2 Small is the largest model we are aware of that was trained end-to-end with a native 4-bit forward pass. We configure numerics in the same way from the start of pretraining through the final RL rollout. This makes training simpler and eliminates the need for calibration when a quantized checkpoint is delivered at the end of training. In our largest jobs, this recipe provides us with an 8% wall-clock speedup in pretraining and a 20% speedup in RL over full MXFP8 training. In this post, we explain the details that made this possible.

Choosing a target for quantization

Ideally, we would like to reduce precision where it has the least effect on model accuracy, while offering a substantial overall speedup. The layers that best fit this profile are Mixture of Experts (MoE) layers, which are computationally expensive and empirically tend to harm accuracy less than other layers when quantized.

Earlier this year, we implemented full MXFP8 training of our MoE layers and found it barely affected our model’s compute efficiency (CE), a measure of how training and evaluation losses change when a new technique is introduced.Recipes for Pre-training LLMs with MXFP8, Mishra et al., 2025, Scaling Laws for Neural Language Models, Kaplan et al., 2020 However, our initial experiments with full NVFP4 training resulted in very large hits to our model’s CE, degrading accuracy beyond what we were willing to accept.

When isolating the effects of NVFP4 quantization in the forward and backward passes, we found that focusing on the forward pass generally offered better tradeoffs between speed and accuracy. But quantizing just the forward pass carries a number of implications for interactions with the backward pass, GPU communications, and more. To understand these, we’ll first examine how NVFP4 works in detail.

Low-precision formats on Blackwell

Four bits can represent up to 16 different values: in the case of FP4, these are ±{0,0.5,1,1.5,2,3,4,6}\pm\{0, 0.5, 1, 1.5, 2, 3, 4, 6\}±{0,0.5,1,1.5,2,3,4,6}. The obvious limitation is in representing numbers larger than 6, which is solved by block scaling: storing a scale factor that multiplies all values in a consecutive block. NVFP4 scales each block of 16 consecutive values based on the largest one in the block (in absolute terms). If that value is −54-54−54, for example, it would be represented as −6-6−6 with a scale factor of 9, and every value in the block would be rounded based on that scale.

Blackwell GPUs also offer microscaling (MX) formats such as MXFP4 and MXFP8, which scale blocks of 32 values.OCP Microscaling Formats (MX) Specification, Rouhani et al., 2023 The formats used for these scale factors are different as well: NVFP4 scale factors are E4M3, making them more precise but limited in their range, while MXFP4/MXFP8 scale factors are E8M0, far less precise but able to represent a very wide range of values.E4M3 denotes an 8-bit floating point format with one implicit sign bit, four exponent bits, and three mantissa bits. E8M0 has eight exponent bits, no sign bit, and no mantissa bits. The increased precision offered by NVFP4 scale factors tends to represent input data more accurately in LLM workloads, resulting in less quantization error than MXFP4.

The tool below demonstrates how NVFP4 block scaling works, and how it results in quantization error:All figures in this post were made with Inkling 2 Small.

96×6=576

Quantization error: −17.7

E4M3 scale factor

(−1₂)0₂ × 10₂(1101₂ − 0111₂) × 1.100₂

= 96

E2M1 value

(−1₂)0₂ × 10₂(11₂ − 01₂) × 1.1₂

= 6

JavaScript is off, so the bits, field boxes and formulas are the precomputed example (593.7 → 96 × 6 = 576) and won’t edit.

This combination of FP4 and FP8 allows NVFP4 to represent magnitudes as low as 2−102^{-10}2−10 and as high as 2688. In practice, we will often want to represent values outside of this range, so NVFP4 is generally used with a second outer-level scale factor which is saved in FP32 and is applied across a very large group of values, such as an entire tensor. This allows each quantized value to be reconstructed as xiFP4×xi//16FP8×xFP32x^{\text{FP4}}_i \times x^{\text{FP8}}_{i//16} \times x^{\text{FP32}}xiFP4​×xi//16FP8​×xFP32, which effectively allows us to shift the representable range up or down. Setting xFP32x^{\text{FP32}}xFP32 to 2, for example, shifts the range of representable magnitudes from [2−10,2688][2^{-10}, 2688][2−10,2688] to [2−9,5376][2^{-9}, 5376][2−9,5376], and setting it to 0.5 shifts the range in the opposite direction.

Block-scaled backward passes

A forward pass through the network multiplies the quantized activations by the quantized weights: y=xqwqTy = x_q w_q^Ty=xq​wqT​. Computing a dot product with NVFP4 takes blocks of 16 values in a row of xqx_qxq​ and a column of wqTw_q^TwqT​, multiplies the pairs, and then multiplies the sum by the scale of each block.

To compute the backward pass, we need to transpose the tensors from the forward pass: dx=gwqdx = g w_qdx=gwq​ and dw=gTxqdw = g^T x_qdw=gTxq​. Now, the blocks take 16 values from columns of xqx_qxq​ and rows of wqTw_q^TwqT​: each value is grouped with 15 different neighbors, resulting in different scale factors and different quantized values represented. The following figure shows the impact of flipping block scaling from rows to columns, which in this case causes the majority of values to be rounded to zero.

High precision

0141664A 16×16 tile of high-precision data

NVFP4

0141664256 of 256 values survive: each row group fits its own scale

The large row survives: 19 small values survive too; the other 221 round down to zero

JavaScript is off — the toggle needs it; the view above shows the 1×16 grouping, precomputed.

This creates a mismatch between the tensors used in the forward and backward passes, which can lead to inaccurate gradient computation. For weight tensors, a straightforward solution is suggested by NVIDIA: rather than computing scale factors for each 1×16 block, they compute a single scale factor based on the largest value in each 16×16 square tile, keeping the scale factors identical when the tensor is transposed.Pretraining Large Language Models with NVFP4, NVIDIA et al., 2025; also see the FP8 formulation in DeepSeek-V3 Technical Report, DeepSeek-AI et al., 2024.

The main drawback of this approach is that it can cause a lot of values to underflow. Increasing the block size from 16 values to 256 makes it highly sensitive to outliers: a single large value among 256 can push the scale factor up, causing the remaining values to be rounded to zero.

High precision

0141664A 16×16 tile of high-precision data

NVFP4

0141664241 of 256 values survive: the outlier’s 1×16 group is rounded down to zero around it

Only the outlier survives: all other values round down to zero

JavaScript is off — the toggle needs it; the view above shows the 1×16 grouping, precomputed.

We tried this approach but ultimately found computing scale factors over 16×16 tiles to be too coarse, hurting CE beyond what we were willing to accept. For NVFP4 training to work, we needed to quantize weights with 1×16 scale factors while avoiding the mismatch introduced during a block-scaled transpose.

Re-quantization with stochastic rounding

The use of 16×16 tiles eliminates the mismatch by enabling bitwise-identical representations between the forward and backward passes — wq=(wqT)Tw_q = (w_q^T)^Twq​=(wqT​)T — but perfect identity isn’t strictly necessary. The important requirement is that the tensors used in the forward and backward passes are equal in expectation: E[wq]=E[(wqT)T]E[w_q] = E[(w_q^T)^T]E[wq​]=E[(wqT​)T]. Preserving the expectation addresses the problem of bias in the backward pass, and loosening the constraint on bitwise equality allows for a few different approaches to the transpose problem posed earlier.

We opted for a straightforward solution: de-quantizing tensors from the forward pass, transposing them in higher precision, and then re-quantizing them with stochastic rounding (SR). Unlike standard quantization, also known as round-to-nearest quantization, SR rounds each value up or down probabilistically, in inverse proportion to its distance from each neighbor.

For example, let’s assume that the forward pass tensor had a value of 5.4, quantized in a block with scale 9. 5.4 divided by 9 equals 0.6, which rounds to the nearest FP4 value of 0.5. The quantized value used in the forward pass is 4.5, which is now the value we want to recover in the backward pass (in expectation).

We can de-quantize this value to have it represented in high precision, but in the backward pass that value is now grouped in a different block. Let’s take its new scale to be 2. If we were re-quantizing with NVFP4, 4.5÷2=2.254.5 \div 2 = 2.254.5÷2=2.25 would now need to be quantized to FP4. Deterministic rounding would represent it as a 2, for a quantized value of 2⋅2=42 \cdot 2 = 42⋅2=4. Stochastic rounding instead rounds it to 2 three quarters of the time and to 3, its nearest neighbor from above, a quarter of the time. The value of 4.5 from the forward pass is preserved in expectation after re-quantizing: 2scale⋅(0.75⋅2+0.25⋅3)=4.52_{\text{scale}} \cdot (0.75 \cdot 2 + 0.25 \cdot 3) = 4.52scale​⋅(0.75⋅2+0.25⋅3)=4.5. Crucially, stochastic rounding is also hardware-accelerated on Blackwell GPUs.

In designing this approach we drew inspiration from TetraJet-v2 and Quartet II, which also re-quantize the tensors from the forward pass.TetraJet-v2: Accurate NVFP4 Training for Large Language Models with Oscillation Suppression and Outlier Control, Chen et al., 2025, Quartet II: Accurate LLM Pre-Training in NVFP4 by Improved Unbiased Gradient Estimation, Panferov et al., 2026 A benefit of applying SR directly to de-quantized values is that it lets us choose any precision during re-quantization. We found that stochastically re-quantizing weights and activations to MXFP8, and then computing gradients using MXFP8 matrix multiplications, offers the best tradeoff between accuracy and speed.

From layer i − 1BF16ActivationsQuantize per-token toNVFP4 with 4/6FPROPNVFP4 GEMMTo layer i + 1Quantize per-expert toNVFP4FP32WeightsDequantizeTransposeQuantize toMXFP8 with SRDequantizeTransposeQuantize toMXFP8 with SRDGRADMXFP8 GEMMWGRADMXFP8 GEMMOptimizerTo layer i − 1From layer i + 1BF16GradientQuantize toMXFP8 with SRTransposeQuantize toMXFP8 with SRFP32BF16MXFP8NVFP4Our quantized linear layer: NVFP4 computation in the forward pass and MXFP8 computation in the backward pass, with stochastic rounding when re-quantizing saved activations and weights.
Quantized communications

With our new NVFP4 matrix multiplications (GEMMs), our MoE layer’s forward pass should theoretically have gotten about three times faster compared to our MXFP8 implementation. But after reducing precision, we noticed we were running up against a bottleneck: communications during expert parallelism.

Since MoE layers are often very large, it is common to split up experts between different GPUs. When computing the MoE layer, a small router decides where each token should go, and tokens are then dispatched to the GPUs containing the routed experts. After completing the GEMMs, the computations of these routed experts are returned to the source GPU and combined to create the MoE layer’s final output. On an NVIDIA GB300 NVL72 system, the tokens will typically be sent over NVLink, which has a bandwidth of 900 GB/s in each direction. At the same time, the NVFP4 GEMMs will run at a speed of up to 15 PFLOPS. Dividing one by the other, each GPU could perform as many as 16,000 floating point operations in the time it takes to receive a single byte. Unless every byte that arrives brings at least that much computation with it, the Tensor Cores sit idle waiting on NVLink.

We found this imbalance created bottlenecks where either the MoE GEMMs were unable to execute because they were waiting to receive the dispatched tokens, or the following operation (in Inkling 2 Small, short convolutions) was unable to start because it was waiting to receive the combined tokens. During dispatch, we avoid this issue by dispatching tokens in NVFP4. Like TetraJet-v2 and Quartet II, our backward pass is computed using quantized — not high-precision — activations from the forward pass (note the input to the weight gradient, or WGRAD, computation in Figure 4), which reduces the amount of data sent over NVLink enough to alleviate the dispatch bottleneck. During combine, however, the output activations need to remain in higher precision (by default, BF16) to avoid impairing model performance.

We alleviate the communications bottleneck by quantizing the data transmitted during combine as well. We initially experimented with quantizing the resulting activations to MXFP8, but found that this impaired performance too much due to MXFP8’s poor representation of outlier values. Instead, we found that performing a 32-dimensional random Hadamard transform (RHT) and then quantizing to block-scaled S2F6, another 8-bit format, resulted in no measurable accuracy degradation during training.

DispatchComputationCombineDispatchw13Qw2w13Qw2w13Qw2CombineCombineCombineExpert Wave 1Expert Wave 2Expert Wave 3Dispatch all-to-all

w13 GEMM

Quantization

w2 GEMM

Combine all-to-all

JavaScript is off — the view shows the 16-bit combine; the toggle needs JavaScript.

RHTs apply a rotation which tends to smooth out the input data. This can reduce quantization error when the input data contains outliers. Existing works have shown that in low precision, integer formats can often represent RHT-transformed data with more accuracy than floating-point formats.INT v.s. FP: A Comprehensive Study of Fine-Grained Low-bit Quantization Formats, Chen et al., 2025, Bridging the Gap Between Promise and Performance for Microscaling FP4 Quantization, Egiazarian et al., 2025 S2F6 is a fixed-point format with two signed integer bits and six fractional bits, and it can represent linearly interpolated values from −128/64-128/64−128/64 to 127/64127/64127/64, closely resembling an integer format. The figure below shows how the Hadamard transformation smooths out the input data, allowing us to quantize it with a smaller scale factor, which in turn reduces quantization error.

PlayPlaying…ReplayHigh-precision data

After the RHT

−500−2500250500−500−2500250500ValueOutlier (|v| ≥ 200)A random Hadamard transform spreads values more evenly while preserving total energy, and as an orthogonal transformation, it can later be inverted exactly to recover the original data. Red points track the values that were outliers before the transform.
Conveniently, Blackwell GPUs contain specialized PTX instructions to efficiently convert data to and from block-scaled S2F6 with FP8 scale factors:cvt.rn.dst.src denotes a data-type conversion from src to dst. See the PTX ISA for more detail.

cvt.frnd2.satfinite{.relu}{.scaled::n2::ue8m0}.s2f6x2.f32
    d, a, b{, scale-factor};
cvt.frnd2.satfinite{.relu}{.scaled::n2::ue8m0}.s2f6x2.bf16x2
    d, a{, scale-factor};
cvt.rn{.satfinite}{.relu}{.scaled::n2::ue8m0}.bf16x2.s2f6x2
    d, a{, scale-factor};

This made it possible for us to implement very efficient kernels for this data type. After computing the MoE output on each GPU, in the epilogue of the w2 grouped GEMM, we efficiently compute the RHT and quantize to block-scaled S2F6, using one scale factor for every 32 values. While the data is being received, it is then de-quantized and aggregated on the fly, after which the RHT is inverted. This reduces the volume of data transmitted during combine from 16 bits per value to 8.25 bits per value, reducing the combine tail and speeding up the MoE layer as can be seen in Figure 5.

Kernels for low-precision training

Taking full advantage of NVFP4 requires specialized kernels which we’ve developed in-house for our low-precision recipes. Our MoE fusion kernel stack is codenamed BBBK, the Big Beautiful Blackwell Kernel. It powers training and inference with peak hardware utilization while maintaining fully deterministic computation.

The process for computing MoE layers is generally dominated by matrix multiplications. We saturate the Tensor Cores using the largest 2SM UMMA instruction unique to GB300 (K=96), fed by a 6-stage multiplicand pipeline and a 7-stage scale factor pipeline. Our precision recipes, however, also place heavy demands on the GPU’s arithmetic logic units (ALUs). Even when the Tensor Cores are saturated, kernels can stall on ALU-heavy steps such as computing scale factors, re-quantizing weights, applying stochastic rounding, and coalescing data transfers.

To eliminate these stalls, BBBK keeps as many hardware pipelines simultaneously saturated as possible. For example, we fuse the RHT and S2F6 quantization directly into the w2 GEMM epilogue. More broadly, we pair aggressive epilogue fusion with ALU vectorization, instruction scheduling, register planning and packing, and speculative megakernel scheduling. In training, BBBK simultaneously saturates NVLink, the ALUs, and the Tensor Cores, while in RL sampling it reaches the latency floor set by NVLink and HBM.

Recipe details

We took inspiration from several other existing works on NVFP4 training to round out our recipe. We keep the last 16.6% of layers in higher precision, which we compute in MXFP8 rather than BF16.NVIDIA’s recipe sets this proportion to 15%, but in our pretraining ladder, we scale layer count by a factor of 6, so setting the proportion to ⅙ works nicely in our setup. When quantizing activations, we use Four Over Six (4/6), a technique which selects between two scale factors during NVFP4 quantization in order to reduce quantization error.Four Over Six: More Accurate NVFP4 Quantization with Adaptive Block Scaling, Cook et al., 2025; also see Ziang Li’s writeup for a nice explanation of the technique. We forgo 4/6 when quantizing weights.

Drawing inspiration from Composer 2, we use per-expert outer scales when quantizing weights and per-token outer scales when quantizing activations, allowing for higher efficiency, batch-invariance, and no worry about causality leakage.Composer 2 Technical Report, Cursor et al., 2026 In our largest training jobs, this recipe has worked without changes during both SFT and RL. In pretraining Inkling 2 Small it costs about 2% in compute efficiency, meaning the model reaches the loss it would have reached with about 2% fewer FLOPs if trained in MXFP8, in exchange for the speedup provided by NVFP4. In RL the gain was much larger: a substantial end-to-end speedup with no discernible difference in reward.

Closing thoughts

A decade ago, it was unclear whether neural networks could be trained using fewer than 32 bits per parameter: the default format remained FP32 as recently as 2020, when BF16 first came to NVIDIA GPUs with Ampere.NVIDIA Ampere Architecture In-Depth, Krashinsky et al., 2020 Today, we often find ourselves referring to BF16 as “high precision,” and we have found robust use cases for training with 8-bit and even 4-bit formats! We’re inspired by NVIDIA’s forward-thinking hardware design that has made these advancements possible. We will continue to push forward: we are actively exploring recipes that enable FP4 computation of the backward pass, as well as how our recipes will evolve on NVIDIA’s latest Vera Rubin systems.

The acceleration of both our pre- and post-training is the result of a constellation of improvements in science and engineering, touching every part of the stack and compounding on each other. Months ago, a training run of a model similar in size to Inkling 2 Small took several weeks; Inkling 2 Small was pretrained in just 68 hours on GB300 NVL72 racks. Our numerics recipe is just one piece of these many improvements, and one we’re continuing to iterate on.

We are learning new lessons with every experiment and training run, and we look forward to sharing more of these with you in future posts.

Citation

Please cite this work as:

Cook, Jack and Thinking Machines Lab, "End‑to‑End 4‑Bit Training",
Thinking Machines Lab: Connectionism, Nov 2026.

Or use the BibTeX citation:

@article{cook2026lowprecision,
  author = {Jack Cook and Thinking Machines Lab},
  title = {End‑to‑End 4‑Bit Training},
  journal = {Thinking Machines Lab: Connectionism},
  year = {2026},
  note = {https://thinkingmachines.ai/blog/end-to-end-4-bit-training/},
}