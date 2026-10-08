---
source_url: https://www.vals.ai/blog/antiferromagnetic-semiconductors
ingested: 2026-10-06
sha256: 062e39865269efb0e7b35fbd70e2a9dc7e647e0d2b36afb82e92f153c72e651d
---

Research Two Room-Temperature Antiferromagnetic Semiconductor Candidates We are sharing two candidate magnets for next-generation computer memory, found by a team of Claude Opus 5.5 agents. Both are predicted to have zero net magnetism yet still sort electrons by spin: one a new compound we designed, the other a material first made in 1999. We're sharing the full calculations, the code, and a list of known caveats. Geby Jaff • 10/04/2026 We’re all used to two types of magnet. The common one, the fridge magnet, is ferromagnetic — its atomic magnets all point the same way (up or down), adding their magnetic effects. The less well known one, the antiferromagnet (AF), has neighbouring atomic magnets that point opposite ways and exactly cancel out magnetically. 
 For a long time, there’s been an intense drive in computer memory research to create materials in between these two extremes. For this purpose, it helps to have a clear picture of what these extremes mean. 
 Today, I’ll share what we found. A team of AI agents and I designed one candidate magnet and found another, first made in 1999, that our calculations predict has the properties we were after. 
 But before diving into the details, let me first lay out a magnet primer that takes all of 90 seconds, assuming you are not an undergraduate in physics or chemistry. 
 A 90 second primer in magnets 
 Spin 
 Each electron has a quantum mechanical property called ‘spin’, which is responsible for its magnetic moment. We can model the spin direction for each electron as either pointing up or down. 
 Spintronics 
 We use spin for storage. A magnetised material stores information based on the spin up/spin down orientation of its electrons, in the same way classical magnets store information based on pointing up/down. The most prominent example of spintronics is the hard drive read head, the device that reads the magnetic bits on the disk. MRAM is another type of spintronics that uses the same principle to store binary information in a non-volatile way. 
 In the world of spintronics, we want to sort electrons by their spin orientation so we can read/store their information. Ferromagnets do this naturally: the electrons that carry current are mostly of one spin, up or down. Ordinary antiferromagnets, however, cannot distinguish up/down electrons. 
 This leads us into the next section. 
 Three kinds of magnets 
 Ferro 
 Ferromagnetic materials are characterised by having a macroscopic magnetic field, or a field that leaks out from the surface. This is why a fridge magnet sticks to your refrigerator door. 
 The problem, however, is that the magnetic field interferes with nearby materials and is difficult to control for storage purposes. In addition, switching magnets back and forth is relatively slow and consumes a lot of power. 
 Another feature of ferromagnetic materials is that the spins are sorted (by up/down orientation) according to energy level. We can see this when looking at the energy spectrum of the electrons: near the edges of the spectrum, the electrons all have the same spin. 
 Antiferro 
 If we take the above and flip the logic, meaning, the spins are unsorted, we end up with an ordinary antiferromagnetic material. 
 Here the electrons of the same energy level will instead have mixed spins. This leads us to two properties of interest: 
 
 Because spins are not sorted according to energy level, it is hard to read/store information using spintronics techniques. 
 However, the lack of macroscopic magnetic field allows us to pack these materials closer together, enabling higher performance for storage devices. In terms of speed, AF materials are also about a thousand times faster to switch. 
 
 The only problem is, if the spins are mixed at each energy level, how would we ever sort them by energy? How do we get a way to read/store information using spintronics with this lack of sorting? 
 Luttinger compensated 
 This brings us to a third type, Luttinger compensated (LC). 
 LC materials are antiferromagnets where the spin-up atoms and spin-down atoms have the same magnitude of magnetism, making the net spin moment zero (i.e. they cancel out). However, unlike in ordinary antiferromagnets, the up and down atoms sit in inequivalent environments: they can be different elements (e.g. one element points up and another points down), or the same element in two different kinds of site. The name comes from Luttinger’s theorem: in an insulator, the net spin moment of each repeating unit of the crystal must be a whole number, so once it is zero it stays locked at zero. Strictly, that holds for a perfect crystal near absolute zero; smaller effects such as spin–orbit coupling, and heat, can leave a slight imbalance. 
 Since the up and down atoms are not equivalent, up/down spins can now be separated (sorted) by energy, just like in ferro materials. 
 Let’s take the previous sections and look at how spin is distributed across the energy landscape for ferro, antiferro and LC magnets. 
 
 What matters for storage is the “spin window”: the slice of energy at the edge of the band gap where every available electron state has the same spin. The larger this window compared with the thermal jiggling at room temperature (about 26 meV), the better the electrons stay sorted. 
 This means we’d love to have a semiconductor with a band gap, without losing the ability to separate spins by their energy levels, and with zero net magnetism. 
 
 This is where our AI agents (and me) enter the scene. Let’s dive into how these agents found two promising materials for next generation computer memory. 
 The agents ran quantum-mechanical simulations of each crystal with the standard method for this, density functional theory, at two levels of approximation: a faster one (PBE+U) and a slower, usually more accurate one (HSE06). The band gaps and spin windows below come from the more accurate one. 
 Candidate 1: Designed a Luttinger Compensated Magnet, YBaMnFeO₅ 
 First, let’s see what our AI agents designed: 
 
 A new compound made of only 5 elements (yttrium, barium, Mn, Fe, O). As far as we could find, it has never been made, nor proposed as this kind of magnet 
 The compound was predicted to be a semiconductor 
 This Luttinger-compensated magnet is predicted to have a 2.35 eV band gap, where spin sorting occurs at both sides of the band gap: a window of 1.0 eV for holes and 1.4 eV for electrons. Note that thermal agitation at room temperature only causes around 26 meV of fluctuation 
 Finally, our agent predicted the material to retain magnetism up to an elevated temperature: about 420 K in the raw simulation, or about 490 K after calibrating the simulation against a known magnet 
 
 While this seems like a pretty promising candidate, the design needs the Mn and Fe atoms to sit in a perfect checkerboard. When our agents simulated how the atoms arrange themselves at different temperatures, that checkerboard fell apart into a random mix at around 950 K. Making this kind of oxide takes about 900–1300 °C, and at lower temperatures the atoms barely move, so standard synthesis would likely give a scrambled crystal. 
 
 A scrambled crystal loses the spin sorting, so this design may be hard to make in its useful form. 
 Candidate 2: Identified a Luttinger Compensated Magnet in KV[Cr(CN)₆] from 1999 
 Shortly after, my agent found this interesting material, previously reported only in 1999, that matches many of the requirements above. Its zero net magnetism is not new: the chemists who made it designed the two metals’ magnetism to cancel. Even its spin sorting was already on paper. A 2008 study using hybrid functionals like ours plotted its electron states spin by spin, and both band edges in that plot carry the same spin. But that study was about magnetic coupling under pressure and never remarked on it. As far as we found, nobody had pointed out that this makes KV[Cr(CN)₆] a Luttinger-compensated semiconductor, put numbers on its spin-sorted windows, or tested how robust they are. It had been hiding in plain sight. 
 KV[Cr(CN)₆] belongs to the same family as Prussian blue, the 300-year-old pigment. 
 Our agent identified it as a Luttinger-compensated material: 
 
 It predicts the material will have a band gap of about 2.1 eV, with both band edges sorted into the same spin: windows of 2.6 eV for holes and 1.6 eV for electrons. 
 The 1999 sample stayed magnetically ordered up to 376 K (103 °C), above room temperature, as measured by the chemists who made it (365 K after the sample had been heated). 
 And most importantly, its structure locks each metal into its own site: chromium bonds to the carbon end of each cyanide and vanadium to the nitrogen end, which is exactly what YBaMnFeO₅ lacked. 
 
 These predictions are for a perfect, dry crystal. The only sample so far, from 1999, is a powder with water in its pores, and it showed a small leftover magnetic moment (0.125 Bohr magnetons per formula unit, where the perfect crystal would have zero). Our two simulation methods disagree on how much the water weakens the effect: the more accurate one (HSE06) says the spin sorting survives, while the faster one (PBE+U) says the hole window shrinks by more than half. Neither the band gap nor the spin sorting has been measured yet. 
 The bottom line 
 We identified a material that combines properties of the two familiar kinds of magnet and could be useful in spintronic devices. We believe the two materials discussed in this article are promising examples of a class of materials that have both antiferromagnetic and ferromagnetic properties. 
 The key features for both materials: in our calculations for perfect crystals they have zero net spin moment, yet they are semiconductors whose electrons are sorted by spin over windows far larger than the thermal jiggling at room temperature. With little stray magnetic field, they shouldn’t disturb their neighbours much. 
 Here is the score of our two materials: 
 
 YBaMnFeO₅: designed candidate; may be hard to make. 
 KV[Cr(CN)₆]: first made in 1999. Near-zero net magnetic moment in the 1999 sample (zero predicted for a perfect crystal), magnetic up to 376 K. 
 
 This suggests that materials for the next step in spintronics may already exist, waiting to be recognized. A 2025 study that predicted two other Luttinger-compensated semiconductors found that both lose their magnetic order below room temperature, and named a room-temperature one as the open goal. KV[Cr(CN)₆] has already been made, and its 1999 sample stayed ordered up to 376 K. Identifying room-temperature Luttinger-compensated semiconductors is a step toward practical spin-based technologies, particularly if their magnetic properties can be controlled through chemistry. The next step is to make KV[Cr(CN)₆] again and measure its spin sorting directly. 
 
 In the spirit of transparency, I invite the reader to go through all the computations that produced the above predictions, including the calculations behind the candidate designs. The input files, raw outputs and analysis code behind the numbers in this post, along with a one-command checker, independent re-runs and a list of known caveats, have been shared on GitHub in a public repository I created to document my research journey: github.com/spicylemonade/compensated-magnet-ledger .
