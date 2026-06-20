---
title: "Reinforcement learning towards broadly and persistently beneficial models"
url: "https://alignment.openai.com/beneficial-rl/"
date: "2026-06-18"
date_ingested: "2026-06-20"
source: "openai-alignment"
type: raw_article
slug: "openai-beneficial-rl"
---

Reinforcement learning towards broadly and persistently beneficial models

**URL**: https://alignment.openai.com/beneficial-rl/
**Date**: 2026-06-18

## Raw HTML Content

```html
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0" />
  <meta name="description" content="Training targeting beneficial behavior in realistic scenarios produces broad improvements in alignment that generalize across domains and persist under adversarial pressure." />
  <meta property="og:site_name" content="OpenAI Alignment Research Blog" />
  <meta property="og:type" content="article" />
  <meta property="og:title" content="Reinforcement learning towards broadly and persistently beneficial models" />
  <meta property="og:description" content="Training targeting beneficial behavior in realistic scenarios produces broad improvements in alignment that generalize across domains and persist under adversarial pressure." />
  <meta property="og:url" content="https://alignment.openai.com/beneficial-rl/" />
  <meta property="og:image" content="https://alignment.openai.com/beneficial-rl/social-preview.png" />
  <meta property="og:image:secure_url" content="https://alignment.openai.com/beneficial-rl/social-preview.png" />
  <meta property="og:image:width" content="1920" />
  <meta property="og:image:height" content="1080" />
  <meta property="og:image:alt" content="RL for beneficial AI social preview card." />
  <meta name="twitter:card" content="summary_large_image" />
  <meta name="twitter:title" content="Reinforcement learning towards broadly and persistently beneficial models" />
  <meta name="twitter:description" content="Training targeting beneficial behavior in realistic scenarios produces broad improvements in alignment that generalize across domains and persist under adversarial pressure." />
  <meta name="twitter:image" content="https://alignment.openai.com/beneficial-rl/social-preview.png" />
  <meta name="twitter:image:alt" content="RL for beneficial AI social preview card." />
  <meta name="citation_title" content="Reinforcement Learning Towards Broadly and Persistently Beneficial Models" />
  <meta name="citation_author" content="Akshay V. Jagadeesh" />
  <meta name="citation_author" content="Rahul K. Arora" />
  <meta name="citation_author" content="Khaled Saab" />
  <meta name="citation_author" content="Ali Malik" />
  <meta name="citation_author" content="Mikhail Trofimov" />
  <meta name="citation_author" content="Foivos Tsimpourlas" />
  <meta name="citation_author" content="Johannes Heidecke" />
  <meta name="citation_author" content="Karan Singhal" />
  <meta name="citation_publication_date" content="2026/06/18" />
  <meta name="citation_technical_report_institution" content="OpenAI" />
  <meta name="citation_pdf_url" content="https://cdn.openai.com/pdf/beneficial-rl.pdf" />
  <meta name="citation_abstract" content="We find that reinforcement learning on realistic scenarios targeting beneficial traits can produce broad improvements across dozens of benchmarks measuring aligned and beneficial behavior. These alignment gains generalize beyond the domains used for training and persist under adversarial pressure." />

  <title>Reinforcement learning towards broadly and persistently beneficial models</title>

  <link rel="stylesheet" href="../assets/styles.css" />
  <link rel="stylesheet" href="/beneficial-rl/styles.css" />
  <link rel="alternate" type="application/rss+xml" title="OpenAI Alignment Research Blog RSS" href="/rss.xml" />
  <link rel="icon" href="/favicon.ico" sizes="48x48" />
  <script>
    window.va =
      window.va ||
      function () {
        (window.vaq = window.vaq || []).push(arguments);
      };
  </script>
  <script defer data-domain="alignment.openai.com" src="/_vercel/insights/script.js"></script>
</head>

<body class="post-page">
  <div class="content">
    <a class="back" data-clean-url href="../">&larr; Back to OpenAI Alignment Blog</a>

    <h1>Reinforcement learning towards broadly and persistently beneficial models</h1>
    <div class="meta">Jun 18, 2026 &middot; Akshay V. Jagadeesh, Rahul K. Arora, Khaled Saab, Ali Malik, Mikhail Trofimov, Foivos Tsimpourlas, Johannes Heidecke, Karan Singhal</div>
    <div class="correspondence">Correspondence: <a href="mailto:ajag@openai.com">ajag@openai.com</a>, <a href="mailto:karan@openai.com">karan@openai.com</a></div>
    <a class="paper-cta" href="https://cdn.openai.com/pdf/beneficial-rl.pdf">Read the paper</a>

    <div class="tldr">
      <strong>TL;DR</strong>
      <p>We find that reinforcement learning on realistic scenarios targeting beneficial traits can produce broad improvements across dozens of benchmarks measuring aligned and beneficial behavior. These alignment gains generalize beyond the domains used for training and persist under adversarial pressure.</p>
    </div>

    <p>As AI systems become more capable and autonomous in high-stakes settings like health, science, education, and coding, they will need to remain helpful, honest, transparent, and safe in situations they have not seen before. This requires generalizing to new contexts, new pressures, longer and more complex interactions, and across domains that differ from those seen during training.</p>

    <p>A growing body of research has shown that misalignment can sometimes generalize in this way. Models trained to exhibit narrow forms of problematic behavior, such as writing insecure code or cheating in realistic scenarios, can begin to behave badly in broader settings unrelated to the original training task. This phenomenon, <a href="https://arxiv.org/pdf/2502.17424">emergent misalignment</a>, suggests that training on a narrow behavior in one setting can sometimes produce much broader changes in model behavior that extend beyond the training distribution.</p>

    <p>In this work, we ask whether reinforcement learning towards beneficial traits in one domain, like health, can lead to alignment generalization across diverse tasks and domains. If it can, models could not only be safer, but also actively benefit humanity across both today’s use cases, like supporting users with their health, and future high-stakes settings.</p>

    <p>We find evidence that this is possible. We construct a dataset of realistic conversations designed to measure and train beneficial traits, such as honesty, epistemic humility, metacognitive transparency (ability to explain one’s thinking process), corrigibility (openness to correction), universal fairness, and concern for human welfare. The dataset spans domains including health, education, science, law, engineering, economics, and other realistic settings, with each situation designed to test whether the model exhibits the relevant trait under pressure, ambiguity, or competing incentives.</p>

    <p>Using a realistic reinforcement learning (RL) training setup, we train a model with a small amount of this beneficial trait data mixed into a broader post-training data distribution. The resulting model improves across a range of alignment-relevant behaviors, becoming measurably more truthful, open to correction, and transparent. More interestingly, it also improves across dozens of independent public and internal evaluations of reward hacking, deception, harmful advice, specification compliance, health, mental health, and safety. This generalization occurs across domains, tasks, and grading setups that were not used in training, even if we restrict training to a single domain and measure performance in seemingly unrelated behaviors.</p>

    <p>We also find that the improvements are persistent under adversarial pressure. Models trained with RL to exhibit these beneficial traits are harder to steer toward harmful behavior using adversarial prompts or fine-tuning. These results suggest that beneficial trait RL can reinforce broad alignment-relevant behaviors that generalize and persist, rather than merely teaching models to succeed on a narrow benchmark.</p>

    <p>Below, we present the results in three parts. First, we describe the beneficial trait dataset and evaluation. Second, we show that training on these traits produces broad out-of-distribution alignment generalization. Third, we show that these improvements persist under adversarial pressure.</p>

    <h2>Measuring beneficial traits in realistic conversations</h2>

    <p>How should we measure whether a model is aligned? Today, researchers rely on many evaluations that measure a broad range of constructs, like whether a model lies, exploits a loophole, follows a behavioral specification, engages in self-preservation, or acts deceptively under pressure. This diversity is useful, and it raises a basic question: are these evaluations measuring a coherent concept of alignment, or are they mostly measuring situation-specific model responses? If they are measuring a coherent concept, what behavioral traits contribute to it, and how can we reinforce them during training?</p>

    <p>We identified a set of beneficial behavioral traits that can plausibly contribute to good behavior across many settings. These included traits such as truthfulness, epistemic humility, metacognitive transparency, corrigibility, risk sensitivity, universal fairness, and concern for human welfare.</p>

    <p>To measure these traits, we built a synthetic dataset of realistic conversations. Each example presents a user situation designed to test whether the model exhibits a particular trait in challenging situations involving uncertainty, pressure, or competing incentives. The dataset spans domains including health, education, science, law, engineering, and business, allowing us to test the same traits across varied real-world settings.</p>

    <figure class="emergent-figure emergent-figure-wide">
      <div class="healthbench-example" data-healthbench-mount></div>
      <figcaption class="image-caption"><strong>Figure 1.</strong> Example conversations targeting beneficial traits within different domains. Each conversation has been shortened for space.</figcaption>
    </figure>

    <p>For example, a scenario might test whether a model acknowledges uncertainty instead of overstating a scientific conclusion; whether it remains open to correction while helping a user work through a complex, multi-step business decision; or whether it applies fair governance standards consistently across people and contexts.</p>

    <p>These traits are not intended to be an answer to the question of what values AI should be aligned to. Rather, they are a concrete and empirically tractable starting point for studying whether reinforcing beneficial behavioral traits can improve model alignment more broadly. Determining which values AI systems should ultimately embody is a wider question that requires societal deliberation and <a href="https://openai.com/index/collective-alignment-aug-2025-updates/">collective input</a>.</p>

    <figure class="emergent-figure emergent-figure-wide">
      <div class="ea-chart ea-chart-large" data-ea-chart="alignment" aria-label="Beneficial trait scores across frontier AI models."></div>
      <figcaption class="image-caption"><strong>Figure 2.</strong> Beneficial trait scores across frontier AI models. We see substantial improvements in OpenAI models over time across traits, from o3 (Apr 2025) to GPT-5 Thinking (Aug 2025) to GPT-5.5 Thinking (Apr 2026).</figcaption>
    </figure>

    <h2>Beneficial trait RL produces broad alignment generalization</h2>

    <p>We next asked whether reinforcement learning on these beneficial traits could improve model behavior beyond the dataset itself. To test this, we trained a model using a realistic post-training mixture consisting mostly of standard RL data, with a small fraction of beneficial trait data. We compared this model to baselines trained from the same starting point with the same amount of RL compute. These experiments used a realistic RL setup without prior <a href="https://www-cdn.anthropic.com/daad4360a8bdc707f8b22e3e745796ba27e57fb3.pdf">synthetic document finetuning</a> to elicit the target behavior. We report a range of evaluations that are progressively more out-of-distribution from the training data.</p>

    <p>As expected, the beneficial trait RL model improved substantially on the in-distribution beneficial trait evaluation &ndash; that is, in held-out scenarios, the model became more truthful, open to correction, metacognitively transparent, etc. The more important question was whether this translated to improvements in independent evaluations that were not used in training and that differed in domains, tasks, and grading procedures.</p>

    <figure class="emergent-figure emergent-figure-wide">
      <div class="ea-chart-stack">
        <div class="ea-chart-row ea-chart-row-single">
          <div class="ea-chart-panel">
            <h3 class="ea-panel-title">Beneficial trait score (averaged across traits)</h3>
            <div class="ea-chart" data-ea-chart="alignTrait"></div>
          </div>
        </div>
        <div class="ea-chart-row">
          <div class="ea-chart-panel">
            <h3 class="ea-panel-title">Deception (Huang et al., 2025)</h3>
            <div class="ea-chart" data-ea-chart="deception"></div>
          </div>
          <div class="ea-chart-panel">
            <h3 class="ea-panel-title">Honesty (Ren et al., 2025)</h3>
            <div class="ea-chart" data-ea-chart="honesty"></div>
          </div>
        </div>
        <div class="ea-chart-row">
          <div class="ea-chart-panel">
            <h3 class="ea-panel-title">Sycophancy (Perez et al., 2022)</h3>
            <div class="ea-chart" data-ea-chart="sycophancy"></div>
          </div>
          <div class="ea-chart-panel">
            <h3 class="ea-panel-title">Reward hacking (Taylor et al., 2025)</h3>
            <div class="ea-chart" data-ea-chart="rewardHacking"></div>
          </div>
        </div>
      </div>
      <figcaption class="image-caption"><strong>Figure 3.</strong> Beneficial trait RL training improved model alignment. As models learned beneficial traits (in-distribution), they improved on 44 out-of-distribution public and internal evaluations of deception, honesty, sycophancy, reward hacking, and benefits in health and mental health, among others. All scores reflect degree of alignment (higher is better).</figcaption>
    </figure>

    <p>Across 44 out of 53 internal and external benchmarks, the beneficial trait RL model improved over the compute-matched baseline on evaluations measuring deception, honesty, reward hacking, latent safety risks, harmful agentic behavior, and other alignment-relevant failures. The same pattern appeared on internal evaluations probing reward hacking, anti-scheming behavior, deceptive behavior, specification compliance, and related safety-relevant behaviors. Training on these traits seemed to shift broader behavior in ways that transferred across 44 independently constructed measures.</p>

    <p>These gains included transfer to evaluations of AI benefits, especially health and mental health. On health evaluations, the beneficial trait RL model improved on tasks involving realistic medical conversations, physician-written <a href="https://openai.com/index/healthbench/">rubrics</a>, and high-confidence medical errors. We saw similar improvements on mental-health evaluations measuring both disallowed content and beneficial support: the beneficial trait RL model was less likely to give harmful responses in sensitive conversations and more likely to support better user outcomes.</p>

    <p>As a stronger test of out-of-domain generalization, we repeated the training procedure while excluding health and science examples from the beneficial trait data. Even without these domains in training, the model still improved on held-out health evaluations evaluated against <a href="https://openai.com/index/healthbench/">physician-written rubrics</a>.</p>

    <p>We next pursued an even sharper test of out-of-domain generalization. In previous work, models trained to exhibit misaligned behavior in one domain learned to generalize this misaligned behavior across other domains. Here, we found evidence that a model trained to exhibit beneficial behavior in just one domain, health, generalized these beneficial tendencies across other domains, showing substantial improvement on non-health alignment evaluations, including reward hacking, deception, and general misalignment. This finding was initially surprising to us and partly inspired this work; it is analogous to <a href="https://openai.com/index/emergent-misalignment/">our previous finding</a> that training on bad health data leads to broad misalignment. OpenAI integrates health data into its models across training stages to serve <a href="https://openai.com/index/introducing-chatgpt-health/">hundreds of millions of users</a>, and we have observed that models with significant health data perform especially well on held-out evaluations of alignment, safety, and benefit.</p>

    <figure class="emergent-figure emergent-figure-wide">
      <div class="ea-figure4-summary" data-ea-figure4 aria-label="Domain transfer summary charts"></div>
      <figcaption class="image-caption"><strong>Figure 4.</strong> Beneficial trait RL improved alignment generalization to untrained domains. (A) Training for beneficial behavior in only health conversations improved alignment in non-health domains. (B) Training for beneficial behavior without any health or science conversations still improved health evaluations. All scores reflect degree of alignment (higher is better).</figcaption>
    </figure>

    <p>Together, these results suggest that training models on beneficial traits can produce improvements that generalize across diverse tasks, domains, and evaluation frameworks.</p>

    <h2>Alignment improvements persist under adversarial pressure</h2>

    <p>In deployment, models may encounter prompts, contexts, or downstream modifications that push them toward harmful behavior. A model that behaves well by default may still be fragile if its aligned behavior is easy to override.</p>

    <p>We therefore studied alignment persistence: how robustly aligned behavior remained under attempts to steer a model toward misalignment, through both adversarial prompting and harmful fine-tuning.</p>

    <p>To test persistence, we used adversarial persona prompts designed to elicit harmful or otherwise misaligned behavior. These prompts pushed the model toward, for example, bad health responses containing factual inaccuracies or misleading guidance. We then compared how much these harmful prompts degraded performance for the beneficial trait RL model versus the compute-matched baseline.</p>

    <figure class="emergent-figure">
      <img src="/beneficial-rl/figures/desktop-light.svg?v=figure-label-updates" alt="Beneficial trait RL model persistence under adversarial steering." />
      <figcaption class="image-caption"><strong>Figure 5.</strong> The model trained with beneficial trait RL was more persistent under adversarial steering.</figcaption>
    </figure>

    <p>The beneficial trait RL model was better able to resist these harmful prompts. Persona prompts that substantially reduced the baseline model’s performance had a smaller effect on the alignment-trained model. In other words, after beneficial trait RL, the model was harder to push into harmful behaviors even when explicitly prompted to adopt them.</p>

    <p>Importantly, this did not mean the model became less steerable overall. Useful models should remain responsive to legitimate instructions, domain-specific roles, and typical user preferences. When we prompted both models to elicit helpful health responses, both the baseline and trait-RL model improved, with no significant difference in the steering effect. We observed selective persistence: models remained steerable in beneficial directions but became harder to steer toward deception, harmful advice, reward hacking, and other problematic behaviors.</p>

    <p>We also examined whether beneficial trait RL made models more resistant to harmful fine-tuning. We started with two models &ndash; one that had undergone alignment RL training and one that had not undergone any RL &ndash; and subjected each to the same fine-tuning training process, using the same data and compute, designed to encourage inaccurate and misaligned medical advice. In the baseline model, we observed a sharp degradation in health performance, coupled with a severe decline on non-health alignment evaluations. The beneficial trait RL trained model was somewhat more resistant to degradation on health evaluations, but far more resistant to decline on non-health alignment evaluations. This result provides preliminary evidence that RL targeting beneficial behavior may help reduce susceptibility to emergent misalignment, though further work is needed to separate the role of beneficial-trait training from standard post-training RL more generally.</p>

    <h2>Where we go next</h2>

    <p>A central goal for alignment research is to make beneficial model behavior broad, generalizable, and persistent. In addition to mitigating downside risks in these scenarios, we will want to ensure models contribute to humanity’s upside across beneficial domains like health, science, and education.</p>

    <p>Our results provide an early proof of concept that this kind of broader alignment generalization may be possible. By training models with RL on realistic scenarios that reinforce beneficial traits, such as honesty, transparency, epistemic humility, moral consistency, corrigibility, and careful reasoning under uncertainty, we were able to induce broad improvements in model behavior. These gains transfer across tasks, domains, and evaluation frameworks and persist under adversarial pressure, suggesting that training can reinforce durable and beneficial traits that generalize beyond the training distribution. Building on <a href="https://openai.com/index/emergent-misalignment/">our previous work on personas</a>, our results provide early evidence that personas can be more or less deeply entrenched in models, and RL may be a path towards entrenching beneficial personas.</p>

    <p>This points to further work for future alignment research. We need to better understand which traits support robustly aligned behavior, how to source inputs on these traits from society, how they are represented in models, how they change during training, and what makes them durable or fragile under pressure. If we can measure and train these traits more deliberately, we may be able to build models that are not only more capable, but also more robustly beneficial and aligned with human flourishing.</p>

    <h2>Acknowledgments</h2>

    <p>Thank you to our collaborators and friends for their feedback and help bringing this work to life: Alex Beutel, Amelia Glaese, Boaz Barak, Christina Kim, Jakub Pachocki, Jasmine Wang, Jason Wolfe, Jenny Nitishinskaya, Mark Chen, Phillip Guo, Rebecca Soskin Hicks, Scott Mayer McKinney, Tom Dupre la Tour. We are grateful to the many researchers, both within OpenAI and across the broader alignment research community, for developing these measures of alignment and making them available for our study.</p>

    <h2>BibTeX</h2>
    <pre class="bibtex"><code>@misc{jagadeesh2026beneficialrl,
  title = {Reinforcement Learning Towards Broadly and Persistently Beneficial Models},
  author = {Jagadeesh, Akshay V. and Arora, Rahul K. and Saab, Khaled and Malik, Ali and Trofimov, Mikhail and Tsimpourlas, Foivos and Heidecke, Johannes and Singhal, Karan},
  year = {2026},
  month = {Jun},
  howpublished = {OpenAI Alignment Research Blog},
  url = {https://alignment.openai.com/beneficial-rl/}
}</code></pre>
  </div>
  <script src="https://cdn.jsdelivr.net/npm/vega@5" defer></script>
  <script src="https://cdn.jsdelivr.net/npm/vega-lite@5" defer></script>
  <script src="https://cdn.jsdelivr.net/npm/vega-embed@6" defer></script>
  <script src="/beneficial-rl/charts-data.js" defer></script>
  <script src="/beneficial-rl/charts.js?v=figure4-no-health-sci-label" defer></script>
  <script src="../assets/subscribe-embed.js" defer></script>
</body>
</html>

```
