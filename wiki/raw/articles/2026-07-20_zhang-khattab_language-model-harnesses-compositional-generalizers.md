<!DOCTYPE html>
<html>
  <head>
<meta http-equiv="Content-Type" content="text/html; charset=UTF-8">
    <!-- Metadata, OpenGraph and Schema.org -->




<!-- Standard metadata -->
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
<meta http-equiv="X-UA-Compatible" content="IE=edge">
<title>
  
  
    
      Language model harnesses are compositional generalizers | Alex L. Zhang
    
  
</title>
<meta name="author" content="Alex L. Zhang">
<meta name="description" content="Harnesses can lead to compositional generalization: we observe a property in training RLMs, in which similarly structured tasks are viewed as isomorphic and all individual LM calls in the harness become in-distribution.">

  <meta name="keywords" content="jekyll, jekyll-theme, academic-website, portfolio-website">






  <!-- OpenGraph -->
  <meta property="og:site_name" content="Alex L. Zhang">
  <meta property="og:type" content="article">
  <meta property="og:title" content="Alex L. Zhang | Language model harnesses are compositional generalizers">
  <meta property="og:url" content="https://alexzhang13.github.io/blog/2026/harness/">
  <meta property="og:description" content="Harnesses can lead to compositional generalization: we observe a property in training RLMs, in which similarly structured tasks are viewed as isomorphic and all individual LM calls in the harness become in-distribution.">
  
    <meta property="og:image" content="https://alexzhang13.github.io/assets/img/preview/harnesses.png">
  
  <meta property="og:locale" content="en">

  <!-- Twitter card -->
  <meta name="twitter:card" content="summary">
  <meta name="twitter:title" content="Language model harnesses are compositional generalizers">
  <meta name="twitter:description" content="Harnesses can lead to compositional generalization: we observe a property in training RLMs, in which similarly structured tasks are viewed as isomorphic and all individual LM calls in the harness become in-distribution.">
  
    <meta name="twitter:image" content="https://alexzhang13.github.io/assets/img/preview/harnesses.png">
  
  
    <meta name="twitter:site" content="@a1zhang">
    <meta name="twitter:creator" content="@a1zhang">
  



  <!-- Schema.org -->
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  

  <script type="application/ld+json">
    {
        "author":
        {
            "@type": "Person",
            "name": "Alex L. Zhang"
        },
        "url": "https://alexzhang13.github.io/blog/2026/harness/",
        "@type": "BlogPosting",
        "description": "Harnesses can lead to compositional generalization: we observe a property in training RLMs, in which similarly structured tasks are viewed as isomorphic and all individual LM calls in the harness become in-distribution.",
        "headline": "Language model harnesses are compositional generalizers",
        
        "sameAs": ["https://scholar.google.com/citations?user=rtCr0q4AAAAJ", "https://github.com/alexzhang13", "https://www.linkedin.com/in/alexzhang13", "https://twitter.com/a1zhang"],
        
        "name": "Alex L. Zhang",
        "@context": "https://schema.org"
    }
  </script>



<!-- Bootstrap & MDB -->
<link rel="stylesheet" href="/assets/css/bootstrap.min.css?a4b3f509e79c54a512b890d73235ef04">
<link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/mdbootstrap@4.20.0/css/mdb.min.css" integrity="sha256-jpjYvU3G3N6nrrBwXJoVEYI/0zw8htfFnhT9ljN3JJw=" crossorigin="anonymous">

<!-- Bootstrap Table -->


<!-- Fonts & Icons -->
<link defer rel="stylesheet" href="/assets/css/academicons.min.css?f0b7046b84e425c55f3463ac249818f5">
<link defer rel="stylesheet" type="text/css" href="https://fonts.googleapis.com/css?family=Roboto:300,400,500,700|Roboto+Slab:100,300,400,500,700|Material+Icons&amp;display=swap">

<!-- Code Syntax Highlighting -->
<link defer rel="stylesheet" href="/assets/css/jekyll-pygments-themes-github.css?591dab5a4e56573bf4ef7fd332894c99" media="" id="highlight_theme_light">



<!-- Styles -->

<!-- pseudocode -->



  <link rel="shortcut icon" href="data:image/svg+xml,&lt;svg%20xmlns=%22http://www.w3.org/2000/svg%22%20viewBox=%220%200%20100%20100%22&gt;&lt;text%20y=%22.9em%22%20font-size=%2290%22&gt;%F0%9F%AB%A1&lt;/text&gt;&lt;/svg&gt;">

<link rel="stylesheet" href="/assets/css/main.css?d41d8cd98f00b204e9800998ecf8427e">
<link rel="canonical" href="https://alexzhang13.github.io/blog/2026/harness/">

<!-- Dark Mode -->
<script src="/assets/js/theme.js?9a0c749ec5240d9cda97bc72359a72c0"></script>


<!-- GeoJSON support via Leaflet -->


<!-- diff2html -->






    
      <!-- Medium Zoom JS -->
      <script defer src="https://cdn.jsdelivr.net/npm/medium-zoom@1.1.0/dist/medium-zoom.min.js" integrity="sha256-ZgMyDAIYDYGxbcpJcfUnYwNevG/xi9OHKaR/8GK+jWc=" crossorigin="anonymous"></script>
      <script defer src="/assets/js/zoom.js?85ddb88934d28b74e78031fd54cf8308"></script>
    
    <!-- jQuery -->
<script src="https://cdn.jsdelivr.net/npm/jquery@3.6.0/dist/jquery.min.js" integrity="sha256-/xUj+3OJU5yExlq6GSYGSHk7tPXikynS7ogEvDej/m4=" crossorigin="anonymous"></script>

    
  
    <!-- MathJax -->
    <script type="text/javascript">
      window.MathJax = {
        tex: {
          tags: 'ams',
        },
      };
    </script>
    <script defer type="text/javascript" id="MathJax-script" src="https://cdn.jsdelivr.net/npm/mathjax@3.2.2/es5/tex-mml-chtml.js" integrity="sha256-MASABpB4tYktI2Oitl4t+78w/lyA+D7b/s9GEP0JOGI=" crossorigin="anonymous"></script>
    <script defer src="https://cdnjs.cloudflare.com/polyfill/v3/polyfill.min.js?features=es6" crossorigin="anonymous"></script>
  


    <!-- Distill js -->
    <script src="/assets/js/distillpub/template.v2.js"></script>
    <script src="/assets/js/distillpub/transforms.v2.js"></script>
    <script src="/assets/js/distillpub/overrides.js"></script>
    
      <!-- Page/Post style -->
      <style type="text/css">
        .fake-img {
  background: #bbb;
  border: 1px solid rgba(0, 0, 0, 0.1);
  box-shadow: 0 0px 4px rgba(0, 0, 0, 0.1);
  margin-bottom: 12px;
} .fake-img p {
  font-family: monospace;
  color: white;
  text-align: left;
  margin: 12px 0;
  text-align: center;
  font-size: 16px;
} d-article mjx-container[display="true"], d-article .katex-display {
  grid-column-start: 3;
  grid-column-end: -3;
  display: block;
  text-align: center !important;
  margin: 0.5em 0 !important;
} table.distance-metrics {
  table-layout: fixed;
  width: 100%;
} table.distance-metrics th:nth-child(1), table.distance-metrics td:nth-child(1) {
  width: 18%;
} table.distance-metrics th:nth-child(2), table.distance-metrics td:nth-child(2) {
  width: 28%;
} table.distance-metrics th:nth-child(3), table.distance-metrics td:nth-child(3) {
  width: 54%;
}

      </style>
    
  </head>

  <body>
<d-front-matter>
    <script async type="text/json">
      {
            "title": "Language model harnesses are compositional generalizers",
            "description": "Harnesses can lead to compositional generalization: we observe a property in training RLMs, in which similarly structured tasks are viewed as isomorphic and all individual LM calls in the harness become in-distribution.",
            "published": "July 20, 2026",
            "authors": [
              
              {
                "author": "Alex Zhang",
                "authorURL": "",
                "affiliations": [
                  {
                    "name": "MIT CSAIL",
                    "url": ""
                  }
                ]
              },
              
              {
                "author": "Omar Khattab",
                "authorURL": "",
                "affiliations": [
                  {
                    "name": "MIT CSAIL",
                    "url": ""
                  }
                ]
              }
              
            ],
            "katex": {
              "delimiters": [
                {
                  "left": "$",
                  "right": "$",
                  "display": false
                },
                {
                  "left": "$$",
                  "right": "$$",
                  "display": true
                }
              ]
            }
          }
    </script>
  </d-front-matter>

  
    <!-- Header -->
    <header>
  <!-- Nav Bar -->
  <nav id="navbar" class="navbar navbar-light navbar-expand-sm fixed-top" role="navigation">
    <div class="container">
      
        <a class="navbar-brand title font-weight-lighter" href="/">
          
            
              <span class="font-weight-bold">Alex</span>
            
            L.
            Zhang
          
        </a>
      
      <!-- Navbar Toggle -->
      <button class="navbar-toggler collapsed ml-auto" type="button" data-toggle="collapse" data-target="#navbarNav" aria-controls="navbarNav" aria-expanded="false" aria-label="Toggle navigation">
        <span class="sr-only">Toggle navigation</span>
        <span class="icon-bar top-bar"></span>
        <span class="icon-bar middle-bar"></span>
        <span class="icon-bar bottom-bar"></span>
      </button>

      <div class="collapse navbar-collapse text-right" id="navbarNav">
        <ul class="navbar-nav ml-auto flex-nowrap">
          

          <!-- About -->
          <li class="nav-item ">
            <a class="nav-link" href="/">about
              
            </a>
          </li>

          <!-- Other pages -->
          
          
            
          
            
          
            
          
            
          
            
          
            
          
            
          
            
          
            
          
            
          
            
          
            
          
            
          
            
          
            
          
            
          
            
          
            
          
            
          
            
          
            
          
            
          
            
          
            
          
            
          
            
          
            
          
            
              
                
                <li class="nav-item active">
                  
                  <a class="nav-link" href="/blog/">blog
                    
                  </a>
                </li>
              
            
          
            
          
            
              
                
                <li class="nav-item ">
                  
                  <a class="nav-link" href="/publications/">publications and pre-prints
                    
                  </a>
                </li>
              
            
          
            
              
                
                <li class="nav-item ">
                  
                  <a class="nav-link" href="/projects/">projects
                    
                  </a>
                </li>
              
            
          
            
          
            
              
                
                <li class="nav-item ">
                  
                  <a class="nav-link" href="/academics/">academics
                    
                  </a>
                </li>
              
            
          
            
          
          
            <!-- Search -->
            <li class="nav-item">
              <button id="search-toggle" title="Search" onclick="openSearchModal()">
                <span class="nav-link">ctrl k <i class="ti ti-search"></i></span>
              </button>
            </li>
          
          
        </ul>
      </div>
    </div>
  </nav>
  
    <!-- Scrolling Progress Bar -->
    <progress id="progress" value="0">
      <div class="progress-container">
        <span class="progress-bar"></span>
      </div>
    </progress>
  
</header>


    <!-- Content -->
    <div class="post distill">
      <d-title>
        <h1>Language model harnesses are compositional generalizers</h1>
        <p>Harnesses can lead to compositional generalization: we observe a property in training RLMs, in which similarly structured tasks are viewed as isomorphic and all individual LM calls in the harness become in-distribution.</p>
      </d-title>
      
        <d-byline></d-byline>
      

      <d-article>
        
        <p><strong>Modern post-training has become a brute-force paradigm of curating ever more environments and ever longer training horizons.</strong> In large part, this is because frontier Transformers are still poor at <em>compositional generalization</em>, the ability to solve unseen problems by composing familiar ones. Unless our models compose the individual lessons they learn, scaling will have slower returns than it should, as every new domain will demand its own investment in the form of training data.</p>

<p>Training data is not the only lever, of course. For the past few years, we’ve attacked harder tasks by <em>scaffolding</em> the Transformer, first with chain-of-thought reasoning, then with tool use, and so on. Yet across all of this, <em>generalization</em> itself has been left to the underlying neural network and to its <a href="https://arxiv.org/abs/1706.03762" rel="external nofollow noopener" target="_blank">2017 token-level inductive biases</a>. We argue that better generalization is largely the job of what today is called a <em>harness</em>. A harness is the program that sits between the external world and the neural network: it decides how to encode the current state of the environment, which can be arbitrarily long and complex, into one or more inputs to the LLM and how to determine the next action. <strong>The primary job of the harness should be to carry a higher-level inductive bias that can reduce unfamiliar and complex problems to compositions of simpler ones for the underlying neural network.</strong></p>

<p>Concretely, we think a good harness is one that <strong>shapes each call to the underlying Transformer so that every observation is <em>locally in-distribution</em></strong>, i.e. each Transformer call handles a prompt that is in-distribution with respect to its training data. In fact, a good harness can frequently reduce problems that seem to require breakthroughs in post-training into almost mundane capabilities of the existing generation of language models. We first showed a version of this for long context processing <a href="https://alexzhang13.github.io/blog/2025/rlm/">nearly a year ago</a> and, in this post, we show that this principle extends to the efficiency of <em>learning</em> itself. That is, <strong>what a model learns through a well-designed harness generalizes across task lengths and across domains</strong> far better than training the neural network on its own does.</p>

<p>We test this by using reinforcement learning (RL) to train a Recursive Language Model (RLM), a harness in which the model offloads its context and defers execution to programmatic decomposition and recursive sub-calls. The results are summarized in Figure 1. Training on only short tasks generalizes to held-out tasks 8–32x longer, with roughly 10x the eval lift with the same train lift over training the underlying Transformer directly. Moreover, training on one domain transfers to other domains at a far better rate than that of a vanilla Transformer.</p>

<figure>
<center>
    <img src="/assets/img/lm_compo/fig1b_length_strategy_generalization_lift.png" style="width:90%; margin-bottom: 10px" alt="Figure 1: Length and strategy generalization lift">
</center>
    <figcaption style="width:100%; margin:auto"><strong>Figure 1.</strong> We train Qwen3-30B-A3B-Instruct-2507 as an RLM and as a base Transformer (+ YaRN) on a suite of tasks, and plot train and eval lift. On the left, we independently train 6 different short task environments, and evaluate on the same task environments, but a split that is 8-32x longer in context length. On the right, we train on 3 different task environments, and evaluate on 3 different domains that use a similar decomposition strategy. We find that the eval lift for the RLM matches or exceeds the train lift, while the base Transformer struggles to generalize. In some length-generalization experiments, we find that the RLM starts with a non-generalizable solution that only works on short tasks but eventually discovers a more generalizable decomposition strategy, yielding a higher eval lift than train lift.</figcaption>
</figure>

<p>We observe this generalization effect because the RLM harness induces an equivalence relation between tasks with latent similarities, meaning the RLM’s main context sees nearly the same token-level trajectory between these tasks. This is illustrated in Figure 2. These results suggest that, similar to tuning model architectures and training recipes, well-designed harnesses can reduce the cost of curating more data and generating longer rollouts while increasing the coverage of tasks solvable through post-training.</p>

<figure>
<center>
    <img src="/assets/img/lm_compo/fig1a_rlm_trajectory_isomorphism.png" style="width:80%; margin-bottom: 10px" alt="Figure 2: RLM trajectory isomorphism across BrowseComp-Plus and OOLONG">
</center>
    <figcaption style="width:100%; margin:auto"><strong>Figure 2.</strong> An illustrated example of a Recursive Language Model (RLM) harness on two different tasks, BrowseComp-Plus and OOLONG, which can (in theory) see the exact same trajectory on the root LM's context window by deferring task-specific queries to its sub-calls and moving information through REPL variables. If the RLM trained on one task, it would generalize to the other because the root LM now can see them as isomorphic. This isomorphism occurs when two tasks share latent structure that the RLM can exploit programmatically using sub-calls, while offloading domain-specific information as sub-tasks. In other words, the harness induces a quotient set (Hi/Q) over all trajectories, reducing similar tasks to the same token trajectory.</figcaption>
</figure>

<h2 id="better-scaling-requires-compositional-generalization">Better scaling requires compositional generalization.</h2>

<p>Open problems in AI often boil down to challenges of getting deep neural networks (DNNs) to generalize. This is the issue that modern post-training attempts to bandage with targeted environments based on perceived applications. In this post, we argue that the perhaps boring old concept of <strong>compositional generalization</strong>, which is the ability to solve unseen problems by composing familiar concepts and patterns, is becoming painfully clear as a necessary and scalable meta-capability that we must begin to prioritize in modern AI systems.</p>

<p>We argued before, via the <a href="https://alexzhang13.github.io/blog/2026/mgh/"><strong>Mismanaged Geniuses Hypothesis (MGH)</strong></a> <d-cite key="zhang2026mgh"></d-cite>, that tasks which humans care about solving, can apparently almost always be decomposed rather naturally into sub-tasks that are not only far simpler but also which are not far beyond the current generation of language models. Compositional generalization is key for leveraging this in practice and enabling our systems’ reachable task space to extend beyond their training set’s direct coverage, especially for tasks that may look nothing alike in their surface-level tokens while sharing some underlying structure.</p>

<figure>
<center>
    <img src="/assets/img/lm_compo/fig2_mgh_long_task_decomposition.png" style="width:90%; margin-bottom: 10px" alt="Figure 3: MGH long-task decomposition">
</center>
    <figcaption style="width:90%; margin:auto"><strong>Figure 3.</strong>Human-defined tasks and their artifacts that we use to train our models on (e.g. web data) are inherently bounded, but longer form tasks have a describable structure that can be effectively decomposed. The key is that the decomposition itself is short and simple.</figcaption>
</figure>

<p>Sadly, if the past few years of astronomic spending on training language models are any indication, Transformers and other existing neural sequence models are, at best, unreliable at compositional generalization. Though it seems very plausible that compositional generalization may emerge at a vanilla neural level, it just doesn’t seem that the basic differentiable neural operations <a href="https://arxiv.org/abs/1706.03762" rel="external nofollow noopener" target="_blank">put together 5 years after AlexNet</a> are particularly optimal when it comes to encoding the inductive biases we need for training our language systems. Indeed, precisely because we now have such powerful priors and models of language, we think it is time to seriously ask whether our inductive biases that aren’t simply geometric or about simple symmetries but which can begin to live at a far higher level of abstraction.</p>

<h2 id="the-capacity-for-compositional-generalization-can-live-in-the-harness">The capacity for compositional generalization can live in the harness.</h2>

<p>We’re often interested in <em>agents,</em> which describes any loop in which some policy observes some state $s$ and perform an action $a$ to interact with an environment $E$. Given a state $s$, it’s tempting to simply serialize $s$ into a prompt and tokenize that as-is for a Transformer to become our policy. But because the state and action space can be arbitrarily large and complex, we learned the hard way as a field to introduce a <em>harness</em> $H: s \rightarrow a$ which is the program that sits between the external world and the neural network: it decides how to encode the current state of the environment, which can be arbitrarily long and complex, into one or more inputs to the LLM and how to determine the next action.</p>

<p>Traditionally, we think of harnesses like Claude Code or Codex as necessary because of their ability to invoke external tools inside a complicated environment. But that’s just part of the agent. We think that <strong>a more fundamental power of the harness is the ability to simplify the arbitrarily complex state $s$ into potentially many smaller observations $o$ that each individual LM call in the harness can properly handle</strong>. We know that Transformers are unreliable at compositional generalization, so we can rely on the harness to define higher-level inductive biases. Designing anything may trigger your bitter-lesson instincts, but there’s no free lunch: it is <em>scalable</em> inductive biases that allow our neural networks to learn and generalize in the first place.</p>

<p>Luckily, we can put this in a way that facilitates <em>improved</em> scaling. <strong>A good harness is a harness that <em>reduces unfamiliar problems to familiar ones</em> and <em>reduces complex problems to simple ones</em>.</strong> In other words, even if the state $s$ is out-of-distribution (OOD) to what any individual language model call was trained for, a good harness produces observations $o$ that are <strong><em>locally in-distribution (LID)</em></strong>, which we define as every individual LM call over this observation being in-distribution with respect to the training data.</p>

<figure>
<center>
    <img src="/assets/img/lm_compo/fig3_locally_in_distribution.png" style="width:100%; margin-bottom: 10px" alt="Figure 4: Locally in-distribution LM systems">
</center>
    <figcaption style="width:100%; margin:auto"><strong>Figure 4.</strong> Good harnesses are designed so each individual LM call sees a prompt that is locally "in-distribution" with what it has learned during training, even if the full task trajectory itself is out-of-distribution (OOD).</figcaption>
</figure>

<p>Sadly, existing harness designs such as Claude Code and Codex fail at facilitating locally in-distribution (LID) observations for the underlying neural network. In particular, they fundamentally rely on flooding the context window of the Transformer with interleaved task-specific information, tool call outputs, and reasoning that get continuously appended. Yes, this supplies plenty of context to the model, but these bloated histories quickly fall out of the training distribution, manifesting in the “<a href="https://www.trychroma.com/research/context-rot" rel="external nofollow noopener" target="_blank">context rot</a>” phenomenon that we often observe in practice.</p>

<p>Instead, we propose that a good harness should <strong>enable individual LM calls to see structurally similar tasks as isomorphic</strong>, enabling compositional generalization. Formally, a harness induces an equivalence operator $\sim_{H}$ over the set of all task states $\mathcal{T}$, meaning structurally similar tasks fall under the same harness-induced equivalence class and produce similar sets of observations for the neural network involved. For most harnesses that use a main LM with sub-agents, we can understand this argument with respect to the main context, assuming the sub-agents deal with small, individually in-distribution sub-tasks.</p>

<p>Good harnesses induce equivalence classes over tasks, and thereby enable far better and more composable learning. A well-designed harness not only reduces the space of learnable trajectories to a small $\mathcal{T} / \sim_{H}$, but it also generalizes to a wider class of trajectories than the set of available training tasks, including those that do not fit in the base model’s context window.</p>

<h2 id="rlms-are-surprisingly-good-at-compositional-generalization">RLMs are surprisingly good at compositional generalization.</h2>

<h3 id="equivalence-classes-over-trajectories-induced-by-the-rlm-harness">Equivalence classes over trajectories induced by the RLM harness.</h3>

<p>An ideal harness decomposes a task such that the main context is abstracted to <strong>literally</strong> appear token-for-token similar for similar problems, i.e. those that fall under the same harness-induced equivalence class $[\tau^\prime] = \lbrace\tau \in \mathcal{T} : \tau^\prime \sim \tau\rbrace$. This isomorphism enables generalizations of the form: <em>if a system can solve task X, it should transitively be able to solve task Y</em>.</p>

<figure>
<center>
    <img src="/assets/img/lm_compo/fig4_context_offloading_programmatic_subcalls.png" style="width:100%; margin-bottom: 10px" alt="Figure 5: Context offloading and programmatic sub-agent calling">
</center>
    <figcaption style="width:100%; margin:auto"><strong>Figure 5.</strong> We compare how context offloading and programmatic sub-agent calling, two primary components of the RLM, enable the root LM to view two different problems as the same / similar. <strong>(1)</strong> Standard agent methods stuff the entire query and context as a prefix to the prompt. Between two different tasks, this prefix significantly changes the output distribution of the model, even if the tasks are solved the same way. Context offloading allows similar problems to be viewed as the same. <strong>(2)</strong> Standard agent methods use tool calls, which return information directly to the main context. Programmatic sub-agent calling allows intermediate computations and information to be stored in the REPL, so the main context does not need to see task-specific information, which can alter its output distribution.</figcaption>
</figure>

<p>The Recursive Language Model (RLM) harness is designed around abstracting tasks by their decomposition and deferring input-specific information to sub-calls. In this sense, RLMs view similarly decomposed problems as isomorphic<d-footnote>Notably, the argument below holds recursively, as we can treat each offloaded sub-agent as its own instance with its own “main” context. This is the intended design of an RLM being recursive, but it is not strictly necessary for maintaining locally in-distribution observations.</d-footnote>, and it achieves this by:</p>

<p><strong>(1) Context offloading</strong>, where input-specific context is passed as a symbolic variable so the root language model call does not directly see it, enables different problems to appear similar at the first step. Recently, several scaffolds have adopted this feature as a form of context management (see <a href="https://www.anthropic.com/engineering/managed-agents" rel="external nofollow noopener" target="_blank">Anthropic’s Managed Agents blog</a>). On its own, context offloading does not prevent environment feedback and/or sub-agent information from returning back to the main context. Over long trajectory horizons, the main context becomes OOD, breaking LID.</p>

<p><strong>(2) Programmatic sub-agent calling</strong>, where sub-agents and also normal tools are treated as functions in a code REPL, allow the root LM to selectively choose information and pass around information across further tool calls and sub-agents without the root LM itself ever needing to see it. This includes tool and sub-call outputs, which can be stored in variables in memory directly and accessed by future sub-calls. Programmatic sub-calling is equally as important as context offloading for abstracting task-specific information away from the main context.</p>

<h3 id="rlms-can-train-on-short-tasks-and-generalize-to-longer-unseen-tasks">RLMs can train on short tasks and generalize to longer, unseen tasks.</h3>

<p>It is widely known that training Transformer-based LMs on a domain at a particular context length does not necessarily generalize to longer context lengths <d-cite key="anil2022length"></d-cite>. A large chunk of mid-training and post-training work in production models like <a href="https://arxiv.org/abs/2505.09388" rel="external nofollow noopener" target="_blank">Qwen 3.x</a>, <a href="https://arxiv.org/abs/2507.20534" rel="external nofollow noopener" target="_blank">Kimi K2.x</a>, <a href="https://arxiv.org/abs/2602.15763" rel="external nofollow noopener" target="_blank">GLM 5.x</a>, etc. has been dedicated to carefully introducing longer and longer data into the training mix so LMs can learn to handle those context lengths, and then again many modern applications commonly exceed those lengths. The length generalization issue especially impacts standard agent designs like <a href="https://arxiv.org/abs/2210.03629" rel="external nofollow noopener" target="_blank">ReAct</a> <d-cite key="yao2023react"></d-cite>, <a href="https://arxiv.org/abs/2402.01030" rel="external nofollow noopener" target="_blank">CodeAct</a> <d-cite key="wang2024codeact"></d-cite>, <a href="https://code.claude.com/docs/en/overview" rel="external nofollow noopener" target="_blank">Claude Code</a>, <a href="https://openai.com/codex/" rel="external nofollow noopener" target="_blank">Codex</a>, etc. which as we mentioned, rely on appending observations to a growing prefix history of context.</p>

<p>We hypothesize that for RLMs, similar tasks of a different length can fall under the same equivalence class under $\sim_{RLM}$. In the following experiment, we explore how training only the root LM of an RLM exclusively on short sequences can generalize sequences an order of magnitude longer, as we posit that the decomposition, and hence the trajectory the RLM’s root LM sees on both settings, are nearly identical.</p>

<p>We consider a suite of 6 different environments across different axes of length: varying the input length, output length, and number of instructions. We explicitly train only on a split containing short tasks, and evaluate on a split only containing significantly longer tasks within the same domain. Across all the settings below, we train for 150 steps (batch size 64, 4 rollouts per) with <code class="language-plaintext highlighter-rouge">prime-rl</code> (<a href="https://verl.readthedocs.io/en/latest/algo/rollout_corr_math.html#decoupled-ppo-achieving-batch-size-invariance" rel="external nofollow noopener" target="_blank">Decoupled PPO</a> <d-cite key="hilton2022batch"></d-cite> with GRPO-like advantages + KL loss) and evaluate every 10 steps.</p>

<ul>
  <li>
<a href="https://github.com/google-deepmind/eval_hub/tree/master/eval_hub/mrcr_v2" rel="external nofollow noopener" target="_blank"><strong>MRCRv2</strong></a> (64k, 2-needle setting to 2M, 8-needle setting). A commonly reported benchmark in frontier model reports, the premise is to find the $i$th instance of needle sentence that answers some query within a large corpus of conversation data.</li>
  <li>
<a href="https://huggingface.co/datasets/openai/graphwalks" rel="external nofollow noopener" target="_blank"><strong>GraphWalks</strong></a> (&lt;128K to &gt;1M setting). Another commonly reported benchmark in frontier model reports, the premise is to extract nodes from a graph that satisfy some simple constraint.</li>
  <li>
<a href="https://arxiv.org/abs/2601.02872" rel="external nofollow noopener" target="_blank"><strong>LongBenchPro</strong></a> (32k to 256k setting, English-only). A suite of multiple choice-style questions spanning 11 different QA, code, and reasoning style problems.</li>
  <li>
<a href="https://arxiv.org/abs/2511.02817" rel="external nofollow noopener" target="_blank"><strong>OOLONG</strong></a> [trec-coarse] (32k to 256k setting). A set of aggregation style questions to answer statistics about a dataset of information.</li>
  <li>
<a href="https://arxiv.org/abs/2512.24601" rel="external nofollow noopener" target="_blank"><strong>OOLONG-Pairs</strong></a> (8k to 32k input, 7k to 146k output setting). A modified variant of OOLONG to find pairs of elements in the OOLONG dataset satisfying certain constraints.</li>
  <li>
<a href="https://arxiv.org/abs/2404.06480" rel="external nofollow noopener" target="_blank"><strong>Ada-LEval</strong></a> [best-answer] (8k to 128k setting). Given a question and a large number of potential candidate and distractor answers, pick out the most suitable to answer the question.</li>
</ul>

<p>We plot both the training reward on short tasks (translucent) and the evaluation reward (dark) on the longer version of the tasks. We compare training an RLM, an RLM where we nudge it to state the decomposition it wants to perform, and a base Transformer (with YaRN for longer settings). We use <a href="https://huggingface.co/Qwen/Qwen3-30B-A3B-Instruct-2507" rel="external nofollow noopener" target="_blank"><strong>Qwen3-30B-A3B-Instruct-2507</strong></a> as the model for all settings.</p>

<figure>
<center>
    <img src="/assets/img/lm_compo/fig5_length_generalization_curves.png" style="width:100%; margin-bottom: 10px" alt="Figure 6: Length generalization training curves">
</center>
    <figcaption style="width:100%; margin:auto"><strong>Figure 6.</strong> Across six benchmarks with length-varying splits, we train Qwen3-30B-A3B-Instruct-2507 as an RLM with a decomposition hint, a base RLM, and on its own as a Transformer, on short splits of the environment. We evaluate on longer splits 8-32x longer at every 10 step checkpoint, and plot both the evaluation score on the long eval, and train reward on short task (smoothed) over 150 steps. We also plot a frontier model, GPT-5.5, with the RLM harness as a point of comparison. The Transformer on MRCRv2 baseline was omitted because it cannot fit 2M tokens in context, even with context extension.</figcaption>
</figure>

<p>Across all six tasks, the RLM yields significantly better eval results on long tasks by training exclusively on short tasks, beating out the base Transformer by a significant margin even when starting with a lower step-0 eval performance. On MRCRv2, GraphWalks, OOLONG, and OOLONG-Pairs, the trained Qwen3-30B-A3B-Instruct-2507 RLM approaches or exceeds an RLM with a frontier model, GPT-5.5 on the long eval, while far exceeding the base Transformer.</p>

<p><strong>RLM eval performance on longer tasks more closely matches the train reward on shorter tasks.</strong> On all six tasks, the RLM yields significant improvements in performance on the long eval relative to its starting, step-0 eval performance. The base Transformer generally yields flat eval performance despite the train reward growing and often exceeding the train reward of the RLM, suggesting <em>what is learned by the Transformer does not extrapolate to the longer setting</em>.</p>

<p><strong>Why length generalization occurs and where it fails.</strong> In all of the environments above, the strategy the RLM learns to solve the short tasks is roughly equivalent to that of the strategy needed to solve the longer tasks, and because the root LM’s view of the long task with the context offloaded looks near token-for-token identical to the short task, the RLM has effectively seen the same task during training. In other words, many tasks share the same equivalence class across length. The primary difference is the number of sub-calls and the content of the sub-calls themselves, each of which handle an in-distribution sub-task. Length generalization occurs because the RLM learns a generalizable strategy, <em>but this is not always guaranteed</em>. In many of the short settings above, one viable strategy is to just offload the entire problem to a single sub-call and return this as a solution, effectively becoming equivalent to the long-context Transformer baseline.</p>

<p>We include the “nudge to decompose” user message variant (a condensed version <a href="https://github.com/alexzhang13/rlm/blob/main/rlm/utils/prompts.py#L147" rel="external nofollow noopener" target="_blank">of the addendum in the RLM repository</a>) to illustrate this point, which helps in the case of MRCRv2, where the RLM does not learn the right, generalizable strategy across length. In the training of RLMs and locally in-distribution LM systems as a whole, a whole area of study is how much supervision / distillation is required to get the system to converge to a generalizable solution over a non-generalizable solution. Our intuition is that at scale, no supervision is necessary, but for the sake of sample efficient learning, <a href="https://noahziems.com/pedagogical-rl" rel="external nofollow noopener" target="_blank">some form of supervision or hint is helpful</a>.</p>

<h3 id="rlms-can-generalize-to-unseen-tasks-that-share-latent-structure-observed-in-training">RLMs can generalize to unseen tasks that share latent structure observed in training.</h3>

<p>The previous section showed that RLMs can learn to view tasks and their length-extrapolated variants as isomorphic by abstracting them as the same task in the root model. For length extrapolation in particular, if the RLM learns a length-agnostic strategy, it quickly generalizes to longer lengths. We can take this intuition to generalization on tasks with shared decompositions: if the RLM learns a strategy that generalizes from one domain to another (e.g. applying sorting, filter and search, MapReduce, etc.) it can similarly generalize by abstracting away the domain-specific tokens, and viewing the two problems as equivalent.</p>

<p>We consider 3 domains in which the context and query are referring to completely different domains, but the actual underlying strategy is roughly the same.</p>

<ul>
  <li>
<strong>OOLONG (trec-coarse questions → spam questions).</strong> Training on aggregation tasks about Jeopardy TREC questions and evaluating on aggregation tasks about questions whose answer is either SPAM or HAM.</li>
  <li>
<strong>OBLIQ-Bench Analogues (writing → math).</strong> Training on tasks about searching for essays that seem to be written by the same author, and evaluating on tasks about searching for math problems that require the same reasoning process. Train and eval metric are nDCG@10.</li>
  <li>
<strong>OBLIQ-Bench Descriptive (Twitter stance → Wildchat errors).</strong> Training on tasks about finding tweets that satisfy a certain stance, and evaluating on tasks about searching for Wildchat conversations containing errors. Train and eval metric are nDCG@10.</li>
</ul>

<figure>
<center>
    <img src="/assets/img/lm_compo/fig6_strategy_generalization_curves.png" style="width:100%; margin-bottom: 10px" alt="Figure 7: Strategy generalization training curves">
</center>
    <figcaption style="width:100%; margin:auto"><strong>Figure 7.</strong> Across three benchmarks with length-varying splits, we train Qwen3-30B-A3B-Instruct-2507 as an RLM and on its own as a Transformer, on one environment domain. We evaluate on a different environment split at every 20 step checkpoint, and plot both the evaluation score and train reward (smoothed) over 500 steps.</figcaption>
</figure>

<p>We similarly find that the RLM exhibits clear generalization capabilities on <strong>completely different domains</strong> than the one it trained on, while the base Transformer struggles to meaningfully improve. Similar to in the length generalization experiments, initial improvements in eval performance on OBLIQ-Bench during the base Transformer training generally come from learning to follow the proper answer format, which quickly diminishes. Interestingly, <em>the train reward of the base Transformer generally exceeds that of the RLM despite clear gaps in performance on the eval</em>. Instead, the train reward of the RLM closely matches the trend of the eval reward, despite being on a completely different domain.</p>

<p>Even more than the length generalization, these experiments have completely different token distributions between train and test, as the main similarity is in the latent task structure that the model must learn to exploit. Like in length generalization, these results suggest the internal mechanisms of the Transformer struggle to decompose the tasks into composable patterns that generalize.</p>

<p><strong>On the cost of training harnesses like RLMs.</strong> On similarly-sized tasks, the RLM incurs an extra runtime and memory cost over naively training a Transformer. In particular, across both the length and strategy generalization experiments, the runtime of RLM training is 1.5-3x longer than the base Transformer counterparts due to multiple steps per sample and waiting on sub-calls. However, this cost scales well with task complexity, as training a Transformer on longer context / horizon tasks is significantly more expensive. Even training a simple ReAct agent on the tasks above on an 8xH100 is difficult for a 30B model due to context bloat.</p>

<h3 id="how-close-are-unseen-rlm-task-trajectories-to-train-trajectories">How close are unseen RLM task trajectories to train trajectories?</h3>

<p>It is rather difficult to characterize whether a prompt $x$ is “in-distribution” for a language model, but we can use benchmark performance as a proxy for this kind of thing — e.g., LMs can solve most AIME problems, so we consider these tasks to be “in-distribution”. For agent trajectories, which are often long, multiple turns, and filled with extra fluff like tool calls and harness tokens, it is even harder to determine whether two trajectories will exhibit the same output distribution behavior.</p>

<p>If the RLM produces a trajectory on an unseen task that is <em>token-for-token</em> identical to a trajectory generated during a training task, then we could easily argue that these two tasks are in the same equivalence class under $\sim_{RLM}$ and are viewed as isomorphic. Unfortunately, even small, one-token perturbations can semantically change the meaning of a text sequence, so arguing that $P_x$ and $P_{x^\prime}$ have some bounded difference is difficult. In the <strong>Appendix</strong>, we discuss some proxies for determining whether two trajectories fall under the same equivalence class. Below, we provide various examples of eval trajectories from our experiments that are similar to some train trajectory on a different task.</p>

<div class="code-comparison-carousel" id="identical-pairs" data-code-comparison-carousel="" data-path="/assets/trajectories/identical_pairs_repr">
  <div class="ccc-toolbar">
    <div class="ccc-nav">
      <button type="button" class="ccc-btn" data-ccc-prev="" aria-label="Previous environment">← Prev</button>
      <select class="ccc-select" data-ccc-select="" aria-label="Environment"></select>
      <button type="button" class="ccc-btn" data-ccc-next="" aria-label="Next environment">Next →</button>
    </div>
    <div class="ccc-meta" data-ccc-meta=""></div>
  </div>

  <div class="ccc-panels">
    <div class="ccc-panel ccc-panel--train" aria-label="Train trajectory">
      <div class="ccc-panel-header">
        <span>Train</span>
        <span class="ccc-panel-sub" data-ccc-train-sub=""></span>
      </div>
      <div class="ccc-panel-body" data-ccc-train="">
        <div class="ccc-status">Loading…</div>
      </div>
    </div>

    <div class="ccc-panel ccc-panel--eval" aria-label="Eval trajectory">
      <div class="ccc-panel-header">
        <span>Eval</span>
        <span class="ccc-panel-sub" data-ccc-eval-sub=""></span>
      </div>
      <div class="ccc-panel-body" data-ccc-eval="">
        <div class="ccc-status">Loading…</div>
      </div>
    </div>
  </div>
</div>

<p><strong>Remark.</strong> The ideal behavior is for the root LM to learn to abstract away information about the domain, and isolate decomposable behavior about a task, while deferring domain-specific information to sub-calls. In many cases, the RLM will still choose to print out task-specific information and pass it back to the main context. While this behavior is often undesirable from a generalization perspective (and can likely be trained out if done carefully), we still find that across all experiments, the strategies used by the RLM during evals closely mimic those learned during training. This includes both general, programmatic sub-agent calling strategies like chunking and fanning out sub-calls, as well as general programmatic strategies like <code class="language-plaintext highlighter-rouge">regex</code> calls.</p>

<h3 id="the-scaling-picture-and-moving-forward">The Scaling Picture and Moving Forward</h3>

<p>It is easy to walk away from these powerful early results thinking that we should all be tinkering with harness designs or imposing our problem-specific intuitions around overly structured programmatic strategies such as MapReduce or dynamic programming. But make no mistake, doing that we will inevitably run afoul of the bitter lesson and fall by the wayside within months.</p>

<p>Instead, we’re making a different argument. <strong>Scaling data will remain the biggest driver of progress, but the machinery that we feed that data into and its inductive biases are what will determine the coefficients of that scaling.</strong> And as things stand today, it seems that the returns on scaling Transformers and related neural architectures are just not budging in terms of being poor compositional generalizers. We think this is because their narrow design space of mostly differentiable neural operators misses something fundamental.</p>

<p>But thanks to language as a powerful substrate for which we have been able to train at scale for the past several years, the architecture of our AI systems is no longer limited to simple differentiable operators or to low-level geometric inductive biases. We can now encode far higher-level and more symbolic inductive biases and train our systems end-to-end with RL, and we have shown in this post that through context offloading and programmatic sub-agents, the RLM architecture is one that can be far superior to a vanilla Transformer at generalization, across lengths and domains. And at its core, this all is about an extremely simple but important idea in harness design: make sure these systems can learn to reduce complex problems to sequences of individually and locally in-distribution observations.</p>

<p>In short, better returns on scaling require compositional generalization, and the capacity for compositional generalization looks like it has to largely live in what today we refer to as a harness, but which in the future may blur quite seriously with what we consider the fundamental architecture of our frontier AI systems.</p>

<h3 id="appendix">Appendix</h3>

<p>Recall that we are interested in characterizing how close harness trajectories on unseen tasks are to what they learned during training. It is rare for two LM trajectories to be token-for-token identical, but taking some liberties with rough smoothness assumptions on the LM as a function of its input, what we really care about is whether two trajectories are close enough under some metric so their output distributions are almost the same.</p>

<p>It is very hard to formalize the above in an empirically meaningful way; we would need to know some properties about the function defined by the LM, a distance metric on input prompts that are within some $\delta$-ball, and a distance metric on the output logits that are within some $\epsilon$-ball. As a basic start, we are interested in, for some distance metric $d(\cdot,\cdot)$, the difference between the root LM trajectory of the RLM during evaluation and training. We can define “isomorphic” here loosely as two prompts have some distance less than $\epsilon$, but as mentioned earlier a more rigorous treatment of this topic is likely necessary. We generally just want to understand and find, for this distance metric, what is the average distance of the <em>closest</em> training pair to the evaluation rollouts? In other words, at training step $t$, for trajectories $x$, the set of evaluation samples $\mathcal{E}_t$, and the set of training samples $\mathcal{T}_{\leq t}$ that occurred before, we compute (with a bit of abuse of notation):</p>

<div>
$$
\mathbb{E}_{e \sim \mathcal{E}_t} \left[\min_{\tau \in \mathcal{T}_{\leq t}} d(x_{\tau},x_{e}) \right] \approx \frac{1}{|\mathcal{E}_t|} \sum_{e \in \mathcal{E}_t}\min_{\tau \in \mathcal{T}_{\leq t}} d(x_{\tau},x_{e})
$$
</div>

<p>We plot the similarity, i.e. $1 - d(\cdot,\cdot)$, of the average eval rollout of the best RLM vs. base Transformer checkpoint to any training trajectory that occurred before it. We consider the following distance metrics:</p>

<table class="distance-metrics">
  <tr>
    <th>Plot label</th>
    <th>Metric</th>
    <th>Distance definition $d(x_{\text{train}}, x_{\text{eval}})$</th>
  </tr>
  <tr>
    <td><strong>Edit</strong></td>
    <td>Token-level, length-normalized Levenshtein Distance</td>
    <td>Let $\mathrm{Lev}(\cdot,\cdot)$ be token-level Levenshtein distance and define normalized similarity $\mathrm{LevSim}(a,b)=1-\dfrac{\mathrm{Lev}(a,b)}{\max(\lVert a\rVert,\lVert b\rVert)}$. Then $d(a,b)=1-\mathrm{LevSim}(a,b)=\dfrac{\mathrm{Lev}(a,b)}{\max(\lVert a\rVert,\lVert b\rVert)}.$</td>
  </tr>
  <tr>
    <td><strong>Contain</strong></td>
    <td>3-gram word containment</td>
    <td>Let $N_3(x)$ be the multiset of word 3-grams in $x$. Then (asymmetric): $d(x_{\text{train}},x_{\text{eval}})=1-\frac{\lvert N_3(x_{\text{eval}})\cap N_3(x_{\text{train}})\rvert}{\lvert N_3(x_{\text{eval}})\rvert}.$</td>
  </tr>
  <tr>
    <td><strong>Jaccard</strong></td>
    <td>3-gram Jaccard</td>
    <td>$d(x_{\text{train}},x_{\text{eval}})=1-\frac{\lvert N_3(x_{\text{eval}})\cap N_3(x_{\text{train}})\rvert}{\lvert N_3(x_{\text{eval}})\cup N_3(x_{\text{train}})\rvert}.$</td>
  </tr>
  <tr>
    <td><strong>Weighted Jaccard</strong></td>
    <td>Weighted Jaccard</td>
    <td>Let $c_x(t)$ be the token (or n-gram) count of type $t$ in $x$. Then $d(x_{\text{train}},x_{\text{eval}})=1-\frac{\sum_t \min\!\big(c_{x_{\text{train}}}(t),c_{x_{\text{eval}}}(t)\big)}{\sum_t \max\!\big(c_{x_{\text{train}}}(t),c_{x_{\text{eval}}}(t)\big)}.$</td>
  </tr>
  <tr>
    <td><strong>Length</strong></td>
    <td>Length Ratio</td>
    <td>(Content-blind) with sequence length $\lVert x\rVert$: $d(x_{\text{train}},x_{\text{eval}})=1-\frac{\min(\lVert x_{\text{train}}\rVert,\lVert x_{\text{eval}}\rVert)}{\max(\lVert x_{\text{train}}\rVert,\lVert x_{\text{eval}}\rVert)}.$</td>
  </tr>
</table>

<figure>
<center>
    <img src="/assets/img/lm_compo/fig7_trajectory_similarity.png" style="width:100%; margin-bottom: 10px" alt="Figure 8: Similarity of eval vs closest train trajectories">
</center>
    <figcaption style="width:100%; margin:auto"><strong>Figure 8.</strong> Across the 5/6 length generalization experiments that include a base Transformer and the 3 strategy generalization experiments, we plot the average distance of the eval trajectories of the best training checkpoint to its nearest training trajectory it has seen before. We plot across 5 different distance metrics to highlight how much closer RLM trajectories on unseen tasks look than an appended context baseline like a base Transformer.</figcaption>
</figure>

<p>Figure 8 illustrates the general point that the root LM’s trajectories share more similarities to the trajectories it sees during training, which primarily comes from context offloading. However, the plots above don’t fully capture the semantic similarities between these trajectories (e.g. it doesn’t say anything about if the RLM generally chooses the same decomposition strategy as its train trajectories).</p>

<p>A more principled distance metric will factor in token similarity and semantic similarity, but it is at least clear from the proxy metrics above that what the RLM’s individual LM calls see, even across a longer time horizon, are much closer to what they may see during training than just a base LM call.</p>

<h3 id="acknowledgements">Acknowledgements</h3>

<p>Special thanks to Braden Hancock and the Laude Institute for generously providing several 8xH100 nodes on short notice to help run these experiments through the Laude Slingshots program. Alex thanks his wonderful labmates at MIT OASYS and Noah Ziems for helpful feedback while writing the blog.</p>

<h2 id="citation">Citation</h2>
<p>You can cite this blog here:</p>
<div class="language-plaintext highlighter-rouge"><div class="highlight"><pre class="highlight"><code>@article{zhang2026harnesses,
  title   = "Language model harnesses are compositional generalizers",
  author  = "Zhang, Alex and Khattab, Omar",
  year    = "2026",
  month   = "July",
  url     = "https://alexzhang13.github.io/blog/2026/harness/"
}
</code></pre></div></div>

      </d-article>

      <d-appendix>
        <d-footnote-list></d-footnote-list>
        <d-citation-list></d-citation-list>
      </d-appendix>

      <d-bibliography src="/assets/bibliography/locally_in_distribution.bib"></d-bibliography>

      
      
    </div>

    <!-- Footer -->
    
  <footer class="sticky-bottom mt-5" role="contentinfo">
    

    <div class="container">
      © Copyright 2026
      Alex
      L.
      Zhang. 
      
      
    </div>
  </footer>


    <!-- Bootsrap & MDB scripts -->
<script src="/assets/js/bootstrap.bundle.min.js"></script>
<!-- <script src="/assets/js/mdb.min.js"></script> -->
<script src="https://cdn.jsdelivr.net/npm/mdbootstrap@4.20.0/js/mdb.min.js" integrity="sha256-NdbiivsvWt7VYCt6hYNT3h/th9vSTL4EDWeGs5SN3DA=" crossorigin="anonymous"></script>

    
  <!-- Global site tag (gtag.js) - Google Analytics -->
  <script async src="https://www.googletagmanager.com/gtag/js?id=G-K2L3VESDMP"></script>
  <script>
    window.dataLayer = window.dataLayer || [];
    function gtag() {
      window.dataLayer.push(arguments);
    }
    gtag('js', new Date());
    gtag('config', 'G-K2L3VESDMP');
  </script>




    
  <!-- Scrolling Progress Bar -->
  <script type="text/javascript">
    /*
     * This JavaScript code has been adapted from the article
     * https://css-tricks.com/reading-position-indicator/ authored by Pankaj Parashar,
     * published on the website https://css-tricks.com on the 7th of May, 2014.
     * Couple of changes were made to the original code to make it compatible
     * with the `al-foio` theme.
     */
    const progressBar = $('#progress');
    /*
     * We set up the bar after all elements are done loading.
     * In some cases, if the images in the page are larger than the intended
     * size they'll have on the page, they'll be resized via CSS to accomodate
     * the desired size. This mistake, however, breaks the computations as the
     * scroll size is computed as soon as the elements finish loading.
     * To account for this, a minimal delay was introduced before computing the
     * values.
     */
    window.onload = function () {
      setTimeout(progressBarSetup, 50);
    };
    /*
     * We set up the bar according to the browser.
     * If the browser supports the progress element we use that.
     * Otherwise, we resize the bar thru CSS styling
     */
    function progressBarSetup() {
      if ('max' in document.createElement('progress')) {
        initializeProgressElement();
        $(document).on('scroll', function () {
          progressBar.attr({ value: getCurrentScrollPosition() });
        });
        $(window).on('resize', initializeProgressElement);
      } else {
        resizeProgressBar();
        $(document).on('scroll', resizeProgressBar);
        $(window).on('resize', resizeProgressBar);
      }
    }
    /*
     * The vertical scroll position is the same as the number of pixels that
     * are hidden from view above the scrollable area. Thus, a value > 0 is
     * how much the user has scrolled from the top
     */
    function getCurrentScrollPosition() {
      return $(window).scrollTop();
    }

    function initializeProgressElement() {
      let navbarHeight = $('#navbar').outerHeight(true);
      $('body').css({ 'padding-top': navbarHeight });
      $('progress-container').css({ 'padding-top': navbarHeight });
      progressBar.css({ top: navbarHeight });
      progressBar.attr({
        max: getDistanceToScroll(),
        value: getCurrentScrollPosition(),
      });
    }
    /*
     * The offset between the html document height and the browser viewport
     * height will be greater than zero if vertical scroll is possible.
     * This is the distance the user can scroll
     */
    function getDistanceToScroll() {
      return $(document).height() - $(window).height();
    }

    function resizeProgressBar() {
      progressBar.css({ width: getWidthPercentage() + '%' });
    }
    // The scroll ratio equals the percentage to resize the bar
    function getWidthPercentage() {
      return (getCurrentScrollPosition() / getDistanceToScroll()) * 100;
    }
  </script>


    
  <script src="/assets/js/vanilla-back-to-top.min.js?f40d453793ff4f64e238e420181a1d17"></script>
  <script>
    addBackToTop();
  </script>


    
  <script defer src="/assets/js/code-comparison-carousel.js?19df98a0540497fb6bebb76152f5d81e"></script>


  
</body>
</html>
