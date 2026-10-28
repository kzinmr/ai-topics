---
title: "Genie 4: A new generation of world simulation"
type: article
source: https://deepmind.google/blog/genie-4-a-new-generation-of-world-simulation/
collected: 2026-10-28
sha256: c124c93bb8701e1096ad56af7020e52fe5477fb9e8187016a4012d14d70ed818
---

Today, we are announcing Genie 4, our new world model, which unlocks unprecedented realism and improves real-time interactive simulation. Genie 4 is natively multimodal, enabling audio-like music, ambient noises, and interactive dialogue to be simultaneously generated with the world.

The Genie 4 model incorporates and builds on capabilities from the Gemini family: Gemini Omni anchors the simulations in real-world appearance and behavior, while other Gemini models provide the complex reasoning needed to help maintain a simulation’s coherence and continuity.

With this foundation, you can set an event in motion, and Genie 4 simulates what happens next: how the world responds, how it sounds, and how the people in it move, react, and speak.

Understanding and simulating the world is a crucial aspect of building AGI. Genie 4 advances our ability to create safe, infinitely variable simulations that can help with everything from developing training environments for robots and agents to unlocking the creation of new interactive experiences.

 Your browser does not support the video tag. 

We have started rolling Genie 4 out as a research preview for trusted testers — gathering feedback before we release it to consumers and developers, starting with Google AI Ultra subscribers in Project Genie and early access partners of the Gemini API and Google AI Studio. Join the waitlist for Genie 4 in Project Genie here .

 Your browser does not support the video tag. Your browser does not support the video tag. 

Genie 4 delivers enhanced photorealism, fluid movement, and native audio. All accompanying sounds featured above are produced directly by Genie 4.

 Genie 4 advances four key capabilities

The following are recordings of real-time interactions from Genie 4, where users use standard keyboard controls for navigation and camera control, and text prompts to steer the scene as it evolves.
 Shaping world simulation in real-time

With Genie 4, you can use natural language to modify a simulation in real-time — like changing the weather, moving the camera, or introducing a new person or object — and Gemini will contextually adapt your prompt to match the surrounding scene. Between your inputs, Gemini also monitors and steers the scene to keep the world progressing cohesively.

 Turn on audio to hear Genie 4 worlds.

 Slide 1 of 3

 Your browser does not support the video tag. Your browser does not support the video tag. 

Prompt: Use the reference image as the exact first frame and visual basis for the scene. Preserve the same floating rectangular platform, weathered concrete edges, wild grasses, ferns, twisted small tree, warm glowing amber sphere, and the same middle-aged man in a loose brown suit playing a brass saxophone.

A cinematic, highly naturalistic documentary scene, photographed on 16mm film with subtle grain, soft photographic detail, extremely low contrast, muted natural colors, lifted shadows, gentle highlights, and soft diffuse overcast light. Absolutely no HDR, no dramatic contrast, no glossy digital rendering, no artificial cinematic lighting.

The platform floats in the middle of a vast, quiet lake surrounded by distant misty forests. Thin layers of fog drift above the water. The sky is pale blue-gray and overcast, with a soft, almost monochromatic atmosphere. The warm amber sphere provides a delicate contrasting glow, softly illuminating the surrounding vegetation and reflecting in the lake.

Begin with a slightly closer view of the saxophone player than in the reference image, while keeping the platform, glowing sphere, tree, and surrounding lake visible. The man continues playing his saxophone naturally, with subtle breathing, finger movements, and gentle body swaying.

The camera moves independently and can freely explore the entire environment, gliding smoothly over the water with gentle, controlled movement. The camera is not attached to the man or the platform. Maintain realistic spatial continuity and natural camera movement.

Everything must remain photographic, physically believable, documentary-like, extremely low-contrast, and softly desaturated throughout the entire experience.

One continuous shot. Natural lake ambience, distant wind, soft water movement, and realistic saxophone sound. No background music beyond the instruments physically present in the scene.

 Your browser does not support the video tag. Your browser does not support the video tag. 

Environment prompt: A wide, sun-drenched hilltop meadow filled with tall green grass and scattered purple, white, and yellow wildflowers swaying in a warm breeze. Low green shrubs dot the right side of the field while distant blue-green rolling hills stretch along the left horizon beneath a bright, partly cloudy sky.

Character: Winding in sweeping S-curves through the center of the grassy meadow from the immediate foreground far into the distance is a long, continuous stream of glossy bubblegum-pink satin fabric. The shimmering pink cloth billows, ripples, and lifts softly above the wildflowers like a flowing river of silk as the wind moves beneath its folds.

 Your browser does not support the video tag. Your browser does not support the video tag. 

Environment prompt: A sweeping aerial view over the vast, frozen landscape of Antarctica, featuring endless snow-covered glaciers, jagged icy mountain peaks, and sculpted blue icebergs bathed in crisp polar sunlight under a clear, pale blue sky. Numerous hot air balloons dot the horizon at varying altitudes, with a large cream, red, and blue striped balloon floating prominently in the mid-distance above the ice sheet.

Character prompt: Shot from a first-person POV standing inside the woven wicker basket of a flying hot air balloon, looking out over the leather-trimmed basket edge on the right side of the frame, where black padded support poles, metal rigging chains, and the dark base of the balloon canopy overhead frame the drifting polar vista.

 Pushing the frontier in realism for physics and human action

Genie 4 introduces a new standard of realism to real-time interactive simulation. Built on an advanced physical understanding of the world, Genie 4 simulates real-world physics scenarios, such as aerodynamics, collisions, and more.

The most dramatic leap is how Genie 4 simulates people, creating characters that move naturally, respond organically to their environments, and can be interactively steered in real-time.

 Slide 1 of 3

 Your browser does not support the video tag. Your browser does not support the video tag. 

Environment prompt: A sunlit outdoor courtyard featuring a weathered stone plinth set against a soft-focus background of lush green garden foliage and clear blue sky, bathed in bright, warm afternoon sunlight that backlights airborne droplets in crisp slow motion.

Character prompt: A whole, glossy green-striped watermelon rests in the center of the stone plinth.

 Your browser does not support the video tag. Your browser does not support the video tag. 

Prompt: A macro close up of a maple seed falling from the tree into the grass

 Your browser does not support the video tag. Your browser does not support the video tag. 

Prompt: A crowded rural Japanese train station in the 1980s, packed with passengers waiting along the platform. The only railway inspector in a dark navy uniform stands close to the camera, observing the scene. A long, deep-red local train with many carriages occupies the railway track closest to the camera POV, stretching across the frame and extending far into the distance. The train is clearly visible in the immediate foreground, not on a distant track. People fill the platform naturally, standing, walking, boarding and waiting with luggage. Lush green mountains, cedar forests and humid summer haze surround the station. Authentic 1980s Japanese atmosphere, cinematic 35mm documentary photography, realistic perspective, asymmetrical composition, natural lighting, subtle film grain, photorealistic textures. The station must look genuinely busy, with a dense crowd of visible people throughout the platform. The red train must be on the nearest track, dominating the scene. No empty platforms, no distant train, no sparse crowds, no centered symmetrical composition.

 Modeling how the world sounds

Genie 4 is our first real-time world model to generate audio natively. Every world carries the ambient sound of its own setting, from wind in the trees to waves crashing at the beach.

The true frontier, however, is human speech. Genie 4 introduces interactive dialogue that adapts on the fly. Characters converse and react to your inputs or events in the world, all in real-time.

 Slide 1 of 3

 Your browser does not support the video tag. Your browser does not support the video tag. 

Prompt: Create a fully three-dimensional immersive stained-glass landscape that feels like a handcrafted crystal window brought to life. The world should be explorable, as if the camera can move freely through a giant 3D stained-glass environment. The entire scene must have a stained-glass / crystal-window look: translucent colored glass, dark lead outlines, glowing layered panels, volumetric depth, and artisanal glass textures.

Show a beautiful landscape with a flowing river running through green fields, flowers in the foreground, trees, distant mountains, clouds, and a radiant sun in the sky. The river should feel like flowing translucent blue glass, the flowers like upright stained-glass sculptures, the grass and trees like layered colored-glass forms, the mountains like stacked glass panels, and the sun like a luminous circular stained-glass element. Everything must feel spatial, cohesive, luminous, and handcrafted, with depth and the sensation that the viewer can move through it in three dimensions.

The camera should be able to travel through the scene as if walking or gliding inside this 3D stained-glass world. Keep the world beautiful, magical, and fully consistent in style.

Absolutely everything must remain made of stained glass or crystal at all times, including the grass, the water, the sky, the clouds, the flowers, the trees, the mountains, the sun, and all visible surfaces. Do not introduce any natural real-world textures. No real grass, no real water, no normal sky, and no realism outside of the stained-glass universe.

No text, no modern objects, no realism outside of the stained-glass universe

 Your browser does not support the video tag. Your browser does not support the video tag. 

Prompt: Immersive first-person POV, we only see the big strong hands of the knight rider tightening the reins, dragon and wings. Photorealistic, ultra-realistic action-camera footage seen entirely through the rider's own eyes while riding a gigantic black dragon at 140 km/h through a mountainous dragon-racing course with many dragons and riders. Other dragons are mounted by other knights.

The camera IS the rider's eyes. The camera is attached to the rider's head, facing forward, and moves naturally with the rider's head. The rider is the viewer. The rider's face, head, torso, body, and full silhouette are NEVER visible. No third-person shots, no external camera angles, no cutaways, no views of the rider from behind or from the side.

Only show what the rider would naturally see: the dragon's neck and occasional parts of its upper back near the bottom edge of the frame, the rushing landscape, two other dragons and their riders racing alongside and ahead, and a huge castle with catapults on its walls. A standard is carried naturally by the rider and may occasionally appear at the edge of the frame, but never blocks the view or fills the frame.

The camera maintains this exact first-person perspective throughout the entire flight. Aggressive high-speed racing, powerful realistic wingbeats, aerodynamic weight, intense wind, natural head movement, subtle camera vibration, wide-angle action-camera distortion, realistic motion blur, cinematic natural lighting, physically believable movement.

Strict visual constraints: true first-person rider POV, no visible rider, no third-person perspective, no external tracking shot, no drone camera, no over-the-shoulder shot, no cinematic cutaways, no camera floating outside the rider's body, no CGI appearance, no video game look, no 3D-render aesthetic.

Audio: deep thunderous wingbeats, roaring high-altitude wind gusts, distant volcanic rumble, and crackling flame embers.

 Your browser does not support the video tag. Your browser does not support the video tag. 

Prompt: A cinematic macro close-up from a 1995 Hong Kong indie romantic drama, shot on 35mm film. Two young, unconventional-looking Korean lovers in their 20s ride a motorcycle across a bridge on the outskirts of Hong Kong at dawn.

The male driver wears no helmet, looking around anxiously, while the pale-skinned female passenger wears an open-face helmet. Their faces dominate the foreground, large and overlapping, with natural skin texture and subtle expressions of worry and tenderness.

Low-angle panoramic composition, framed by solid black bars. Shallow depth of field, blurred road receding behind them, orange streetlights streaking past, and a dark green dusk sky. Intimate, imperfect, melancholic 35mm film aesthetic.

One continuous shot.

 Simulating complex events with Gemini models

Bringing Gemini and Genie 4 together adds a new layer of reasoning to world simulation, allowing us to model complex, multi-step events and test how AI systems navigate different environments before bringing them to the real world.

To achieve this in real-time, Gemini 3.8 Flash serves as a guiding agent in the loop: as Genie 4 generates a world in real-time, Gemini continuously observes the scene, breaks down goals into a sequence of steps, and reviews incoming frames to track the progress and verify that each step succeeded. As the world shifts or the user intervenes, Gemini adapts its plan in the moment, unlocking worlds with reliable causality, procedural behaviors, and multi-step reasoning.

 Slide 1 of 3

 Your browser does not support the video tag. Your browser does not support the video tag. 

Prompt: Universal Robots UR5 holds a pipette and dispenses liquid into a lab plate, triggering tiny electric sparks.

 Your browser does not support the video tag. Your browser does not support the video tag. 

Prompt: A REAL, ultra-photorealistic, high-end 35mm cinematic first-person perspective (POV) experience set inside an opulent, claustrophobic antique salon, strictly avoiding any video game, CGI, or digital render aesthetic. Real place, cinema, not render.

POV & Foreground Wand: Authentic first-person perspective looking down along the player's physical right hand, which firmly grips an ornate, hand-carved hardwood and polished brass wizard wand pointing into the room. The player's skin exhibits realistic pores, skin creases, cuticle texture, and natural muscle tension under ambient room light. The wand displays fine wood grain, tiny varnish micro-cracks, cold metallic brass inlays, and tactile surface wear from handling.

Porcelain Menagerie & Room Architecture: A suffocating, baroque-style gallery packed floor-to-ceiling with thousands of fragile, life-sized and miniature glazed porcelain animals. Glistening ceramic peacocks with intricate feather patterns and vibrant cobalt and emerald enamels, regal porcelain dogs, and curled porcelain cats perched on marble mantels, mahogany display shelves, and velvet-draped pedestals. The surfaces showcase authentic high-gloss ceramic glazing, micro-crazing cracks in the enamel, delicate bone china translucency, and natural dust gathering in the crevices.

Cinematic Optics & Lighting: Shot on high-end anamorphic 35mm film lenses. Natural optical characteristics featuring shallow depth of field, subtle barrel distortion, realistic optical lens flares, fine organic film grain, and creamy bokeh in the background. Natural daylight streams through tall, grime-streaked Victorian lace curtains, casting soft volumetric dust motes and creating sharp, physically accurate specular highlights across the glossy curved porcelain glazes.

Dynamic Movement & Physical Interaction: Continuous, smooth handheld POV traversal. The player subtly sweeps and points the wand toward the ceramic figures, causing realistic micro-vibrations in the frame as footsteps tread across creaking hardwood floorboards. The figures remain frozen in immaculate, fragile stillness, catching shifting highlights as the wand moves.

Acoustic Atmosphere: Raw, immersive documentary-grade audio. Faint floorboard creaks underfoot, distant room tone, quiet breathing, the subtle dry friction of fingers adjusting their grip on the wooden wand, and the delicate, crystalline clinking resonance of fine porcelain vibrating faintly in the quiet air.

A real magician stands beside a tall wooden table. On the table is a large rectangular wooden box, completely open at the top, with no lid.

A real peacock stands calmly inside the box.

Exceptional production design, sophisticated art direction, cinematic lighting, natural but carefully controlled light, realistic skin tones, beautiful contrast, subtle shadows, rich textures, elegant composition, shallow depth of field, high-end cinema camera, realistic human actors, extremely photorealistic.

It should look like a frame from a prestigious, beautifully shot modern TV series: understated, expensive, cinematic and completely believable.

No theater, no stage, no fantasy, no cartoon, no plastic-looking people, no CGI look.

 Your browser does not support the video tag. Your browser does not support the video tag. 

Prompt: crowned crane walks across the snow beneath the clear dusk gradient sky. Natural colors in a documentary style.

As part of exploring this capability, we have also been experimenting with Gemini 4 Argon and Genie 4 to bring our frontier research together with Gemini Robotics .

In the example below, Argon breaks down a user-instructed task into steps for Genie to render. These steps are interleaved as text captions to Genie 4 as the simulation is rendering. Because Genie 4 can be steered in real-time with text captions using Gemini, this now unlocks the path of adapting the simulation as it progresses towards the completion of that task. This capability becomes a path for simulating a breadth of scenarios in imagined worlds, using Gemini 4 Argon and Genie 4.

 Your browser does not support the video tag. Your browser does not support the video tag. 

Gemini 4 Argon and Genie 4 work together to simulate Apptronik's Apollo humanoid playing a game of checkers, breaking the task down into real-time steps.

Learnings from trusted testers

While Genie 4 is a major research milestone, it remains an early, experimental model. To understand how interactive world models can support real-world workflows—and where they still need to grow—we’ve been working with cohorts of trusted testers across creative industries, journalism, education, gaming, and engineering.

Testers highlighted how the leap in photorealism, native audio, and real-time steering allows ideas and concepts to be turned into realistic simulations, unlocking new abilities across disciplines:
 Creative direction : Creatives and technologists are testing Genie 4 as a rapid "draft mode" for pre-visualization and ideation. For example, filmmakers can step into a live simulation of a scene and run multiple "takes" in real-time, adjusting camera angles, lighting, dialogue, and action on the fly.
 Historical scenarios & immersive photographs : Photojournalists are exploring how a single 2D archival photograph can become a grounded simulation of that environment in seconds. Teams are testing how populated, dynamic worlds can help experience historical spaces or visualize how short-term environmental events, like a flash flood or wildfire, unfold.
 Interactive experience concept design : Game developers and creative technologists are testing Genie 4 to go from an initial idea to an explorable prototype in seconds, testing visual styles, material aesthetics, and interactive mechanics through natural language prompts before writing a single line of engine code.
 Simulation : Aside from our robotics research, enterprise partners across industries are evaluating Genie 4 as a tool for rapid "zero-to-one" scenario generation, and identifying gaps to further improve Genie to best fulfill that simulation need.
 Future Work: Towards hybrid world models

A promising path for future progress lies in hybrid world models, which combine the logical, structured reasoning of code and language models with the rich, sensory representation of pixel-level simulation.

 Bringing Genie and Gemini models closer together is an early step in this direction. Gemini works behind the scenes to map the structure and plan the narrative timeline, while Genie generates the immediate physical reality—rendering how the world looks, sounds, and responds, pixel by pixel. Together, these complementary strengths can unlock a new class of world models that are far more coherent, controllable, and grounded than either approach could achieve alone.
 Building world models responsibly

Genie 4 marks a new area of frontier research that merges real-time generation and photorealism, introducing a new range of capabilities and dimensions that we want to roll out and explore in a responsible way. Genie 4 includes strict safety guardrails that are consistent with our safety policies across other models. Before launching this preview, we evaluated Genie 4 through internal rigorous safety evaluations to prevent the generation of harmful or malicious content. Also, we have intentionally deployed it first to trusted tester partners to get early feedback, before we release the model more broadly.

To maintain transparency, all video and audio generated by Genie 4 will include SynthID, our imperceptible digital watermarking technology that helps identify AI-generated content across visual and audio modalities.
 Understanding current limitations

Genie 4 remains an early, evolving area of research.

While it can maintain coherent environments over short sessions, visual details and object permanence can still shift or drift over time—especially as a simulation runs longer, after multiple complex prompt edits, or when navigating throughout the scene. Complex physical interactions, real-time audio accuracy, rendering legible text, spatial accuracy, and long-term consistency are active areas of ongoing research. We are sharing Genie 4 as a preview to learn alongside our community and safely advance the frontier of interactive simulation
