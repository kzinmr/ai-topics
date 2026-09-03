---
source_url: https://www.worldlabs.ai/blog/atlas
ingested: 2026-09-03
sha256: 7cedc396ec51ed43935b29e19d6f8651c34e97c599c6eb0afea6f5d3f1730db5
---

Atlas: A World Model for Spatial Intelligence | World Labs
Introducing Atlas, our new omni world model for spatial intelligence.
Atlas: A World Model for Spatial Intelligence
World models generate, reconstruct, and simulate any possible world.
They understand how worlds appear, behave, and evolve
so that we can render imagined worlds for creative users,
simulate the real world in high fidelity, and help robots plan actions.
At World Labs, we build these general purpose world models in pursuit of spatial intelligence.
Today we are introducing Atlas, our next-generation world model.
Atlas is an omni model that we pretrained from scratch to natively operate on
It is a multimodal autoregressive diffusion transformer:
all inputs are combined into a shared spatial context.
Atlas uses that context to generate what comes next,
staying consistent in 3D with everything it has seen and imagining what lies beyond it.
Atlas is built to scale: its performance improves with increased training compute,
and we expect this trend to hold as we continue scaling.
spanning world generation, reconstruction, and simulation:
Atlas generates images and videos from one or more images with pixel-perfect camera control,
outputting up to 1 minute of video at 1440p.
Atlas reconstructs real world scenes from one to dozens of input images.
It generates both image frames from novel views and explicit 3D outputs,
outperforming state-of-the-art models specialized for 3D reconstruction.
Atlas models space and time from input videos,
reframing videos for dramatic visual effects
Atlas generates images and 360 panoramas from text;
it can follow complex prompts, render text,
and generate a wide variety of visual styles.
Atlas takes one or more reference images and generates
new views at any camera position and angle you specify.
Generated views match the content and geometry of the input images,
smoothly extrapolating beyond them to imagine parts of the scene
Atlas handles a broad range of scene types, visual styles, and camera motions.
Atlas uses precise camera geometry as a native input type,
going beyond coarse text-based instructions for camera control.
This lets you frame every shot and control every motion.
It uses the content of the input image along with its broad world knowledge
to imagine what the scene should look like from new angles.
For example, it generates the back side of the robot,
and it guesses that there should be a grassy lawn next to the pool.
From a single image, Atlas generates views from any angle. Drag to change
Similar to an LLM, Atlas first encodes its inputs into a context,
then generates outputs conditioned on the context.
However, Atlas is unique because each image is grounded at a 3D position in space;
Managing this spatial context unlocks entirely new kinds of creative control.
For example, you can place two unrelated reference images in the context
and position them in 3D space; Atlas then generates a world that smoothly interpolates between them.
These examples demonstrate the model&#x27;s world knowledge and creativity;
it imagines doorways, hallways, nooks, and other transitions between
Select left and right frames to populate the spatial context, and Atlas
Atlas lets you generate long videos with precise control
by combining camera movement and spatial context management.
You design every scene and every camera angle.
This puts you in the director&#x27;s chair:
you are staging the scene, not pulling the lever of a slot machine.
In the example below, we generate a 1 minute video at 1440p resolution using a small number of
We hand-design a camera path through the scene,
The rest of the videos on this page have been compressed to optimize page performance.
Atlas reconstructs real-world spaces from one or more input images.
It does not require special capture equipment or hundreds of dense views to
faithfully reconstruct objects and scenes.
We believe Atlas is a major step forward toward solving
the problem of novel view synthesis from sparse input images,
a decades-old fundamental problem in 3D computer vision.
Atlas can take a variable number of input views of a scene.
When parts of the world are not visible in the input views,
Atlas imagines a plausible way to fill in the gaps
by drawing from its rich world knowledge.
But sometimes you do not want imagination;
you might want an exact reconstruction of a real-world location.
Passing more input images gives Atlas more context:
Atlas typically gives faithful reconstructions with as few as two or three images,
outperforming state-of-the-art results by models specially trained only for 3D reconstruction.
However, Atlas can also make use of over a hundred input images in its spatial context,
allowing for faithful recreation of real world environments.
Atlas generates an aerial view of the scene from just a single ground-level photo.
The garden visible in the single input photo is accurately recreated in the model output,
After adding a second real-world input image of the cottage next to the garden,
the model&#x27;s output shows both the garden and the cottage,
but it still imagines the house to the left.
After adding a third input image of the main house,
In the second example, we build up Stanford&#x27;s Main Quad piece by piece,
beginning with the grassy main entrance and ending with the colorful mosaics decorating
Though Atlas only receives two to twenty-five ground-level input images,
it can generate paths from aerial views flying far above the campus.
Atlas can generate many different trajectories through the same scene,
giving new perspectives on the same input images.
No matter how many times you change the camera path, the scene stays consistent.
In the example below, we show that given a small set of input images,
Atlas can generate multiple camera paths through the same scene.
Different camera paths can emphasize various parts of the scene
or change moods by varying in speed, length, or complexity.
Atlas can generate many different paths through the same scene using a
In the results above you have seen Atlas output 2D images and videos,
which are sufficient for some applications.
But workflows in robotics, gaming, design, VFX, and beyond often require explicit 3D outputs.
Atlas natively operates on both 2D image frames and 3D depth maps,
enabling it to output worlds as point clouds or 3D Gaussian splats.
From one image, Atlas generates new views and 3D geometry, then converts to
Atlas produces a full 3D world by jointly generating new views and estimating their geometry.
it predicts the depth of every frame and combines them into a 3D reconstruction.
In either case, Atlas fills in regions that no camera ever saw.
Atlas can reconstruct 3D point clouds from input videos
Point clouds estimate a scene&#x27;s geometry, but 3D Gaussian splats make it usable.
Atlas fills the remaining gaps and turns the point cloud into a complete splat scene
that renders on-device at high resolution and frame rates.
enabling Atlas to integrate naturally with the rest of our products.
It understands both the spatial structure of the world
Combining its spatial and temporal abilities leads to new applications
Atlas turns a handful of ordinary cameras into a &quot;bullet time&quot; multiview capture studio.
With footage from as few as three cameras,
letting you view events from impossible angles.
Real-world videos can be reframed from new camera angles without an
Notably, these shots did not require professional photographers or specialized equipment.
Each of them was filmed by a few engineers and researchers
with ordinary cell phones on tripods and clamps that fit in a backpack.
Atlas reconstructs the scene from three to five camera views,
after which you can reframe shots however you like.
Behind the scenes: the clips above were captured using just a few cell
You have already seen Atlas reconstruct a space in explicit 3D from a few images.
For robotics, reconstruction is only half the job:
as a simulated robot moves through space,
Atlas also generates the RGB and depth data its sensors would observe along the way.
The world and the robot&#x27;s view of it come from the same model.
we captured two large environments with a cell phone video, using 24 frames each for reconstruction.
Scanning spaces like these traditionally requires elaborate and expensive equipment.
We then simulate different kinds of robots navigating different paths
and use Atlas to generate images from the perspective of the robot&#x27;s body-mounted cameras.
Atlas reconstructs spaces and aids in simulating robot navigation
Robotic manipulation goes a step further.
Atlas aids in building a simulation that also captures how objects move and interact.
Once a task is simulated, you can vary it easily:
change the objects, their positions, the robot&#x27;s motion, the lighting, and the background.
The result is diverse training data and testing environments for robotics at scale.
Atlas enables Real-to-Sim from just a few real-world recordings, recreating
physical interactions with rigid, articulated, and deformable objects while
The primary focus of Atlas is world modeling,
and every image is a window to a possible world.
Though image generation is not its primary focus,
it follows complex prompts, renders text, and generates a wide variety of visual styles.
Atlas also generates 360 images from text or image prompts,
where again it can generate a wide variety of scene types and visual styles.
Atlas is an omni model designed to handle many tasks and many kinds of input and output data in a
single unified architecture, putting spatial control at the heart of the model.
These goals require us to depart from standard architectures used by both LLMs and
video models, and design a new base architecture to serve as the foundation of future world models.
Atlas is a multimodal autoregressive diffusion transformer. Its inputs are
grounded in 3D space to form a spatial context, and it generates multimodal
multimodal autoregressive diffusion transformer
It operates on multimodal sequences, generating each new element of the sequence one at a time.
These architectural properties work together to achieve our goals,
and taken together they enable a new paradigm of generation based on a
: Atlas can natively process many different data types.
At present it can operate on text, images, camera poses, and 3D depth maps;
videos are represented as sequences of images.
Each image and depth map is conditioned on an explicit camera pose,
making spatial control a central component of the architecture.
: Atlas operates on sequences of elements,
where each element is one of the multimodal data types above.
Each output is generated one at a time, conditioned on earlier parts
This flexible design naturally adapts to a wide variety of tasks:
each task is just a different kind of sequence, where inputs are followed by outputs.
: Atlas is a rectified flow model that generates outputs
Diffusion models excel at modeling high-dimensional continuous data like
and can naturally trade off speed and quality by varying the number of denoising steps
: The transformer architecture consists primarily of large matrix
multiply operations and is well-adapted to modern hardware.
It is a robust backbone for world modeling.
Atlas is a blend of ideas from modern LLMs and video models.
It can benefit from architectural, algorithmic, and systems advances
Like an LLM, it is an autoregressive transformer,
so it can take advantage of innovations used to serve and accelerate LLMs
including KV-caching, cache-aware routing, disaggregated serving, and more.
Like a modern image or video model, it is a latent diffusion model
and can make use of algorithms such as diffusion distillation, classifier-free guidance,
shifted noise schedules, and advances in VAE design.
Atlas is an omni model for world modeling that performs many tasks.
There is thus no single benchmark that fully captures its generality.
We highlight quantitative evaluations of Atlas on two key tasks:
camera-conditioned generation and 3D reconstruction.
On both tasks it outperforms more specialized models.
We compare against a selection of top-performing video models for camera-conditioned generation.
In each trial, we pair a single input image with a sequence of one to three cinematic camera motions
We prompt each model with a single input image and a target camera path.
For Atlas, we encode the camera path using its native camera input format.
Other models do not accept cameras as a native input format,
so we describe the camera path in the input text prompt,
It is possible that more sophisticated prompt engineering or creative multimodal prompts
could improve camera following for some models,
but we use text as it is the most common input modality for describing camera motions.
Third-party human raters judge which model better follows the intended camera path.
Atlas outperforms recent video models at camera-controlled generation
and this advantage grows as camera trajectories become more complex.
We additionally evaluate Atlas on the task of 3D reconstruction from sparse input views.
In each trial, the model receives a set of images and their camera poses,
and predicts a 3D point corresponding to each input pixel.
This problem has attracted much interest in the academic community,
and many specialist reconstruction models have been developed in recent years.
Atlas is an omni model which performs both generation and reconstruction.
Atlas outperforms the best specialized open-source reconstruction models
We evaluate on several state-of-the-art benchmarks for this task,
reproducing the results for all baselines
to ensure a common and fair evaluation protocol across all methods.
3D Reconstruction Error (lower is better)
Mean absolute-relative pointmap error per dataset for Atlas and five recent baselines; lower is better.
Most progress in modern AI has been driven by scaling.
Models improve in large part by scaling up simple algorithms to make use of more data and compute.
We see strong evidence that Atlas will continue to improve with scale.
We pretrained Atlas from scratch on a large diverse corpus of multimodal data.
we trained a series of models of increasing size and training compute,
and found that each new level of compute unlocked new model capabilities.
We are confident that our future world models will follow this trend,
dramatically improving their capabilities as we continue to scale.
Atlas is entering early access with select partners.
If you would like to build with it, request access below and we will reach out.
We are excited to see what you build, and to work with you to make Atlas
the go-to world model for generating, reconstructing, and simulating any world.
across research and engineering to advance spatial intelligence.
This post was produced by the World Labs team. Please cite as:
title = {Atlas: A World Model for Spatial Intelligence},
note = {https://www.worldlabs.ai/blog/atlas},
The Next Frontier of AI Is Spatial Intelligence
Martin Casado (a16z) sits down with Fei-Fei Li and Yunzhu Li to discuss the SceniX acquisition, how simulation unlocks the next generation of robotics, and why training robots isn&#x27;t like training LLMs
Real-to-sim-to-real (R2S2R)  as a scalable engine for training and evaluating robot policies
WORLD LABS™ is a trademark of its respective owner.