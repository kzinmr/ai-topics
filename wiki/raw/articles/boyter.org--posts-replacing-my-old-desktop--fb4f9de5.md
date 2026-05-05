---
title: "Replacing my old desktop with a high-end Linux PC"
url: "https://boyter.org/posts/replacing-my-old-desktop/"
fetched_at: 2026-05-05T07:01:53.880468+00:00
source: "Ben Boyter"
tags: [blog, raw]
---

# Replacing my old desktop with a high-end Linux PC

Source: https://boyter.org/posts/replacing-my-old-desktop/

I am hoping to get another 5 years out of the machine as it is now.
My
previous post about my desktop
ended with the above. It has been about 5 years and while I was happy with my old desktop I had started looking into agentic workflows using LLM’s. After burning $50 in an afternoon just debugging some flows against OpenAI I decided I needed a better solution.
A little research and I decided to order and build a new desktop that would solve my immediate problems, as well as last another 10 years. My requirements were fairly simple, as much power as possible in as quiet a form as possible.
Components
Here is the full list of parts, and I will go through the rationale of some of them.
Processor: AMD Ryzen 9 9950X3D
CPU Cooler: Noctua NH-D15 & Thermal Grizzly KryoSheet
Video Card: Palit GameRock GeForce RTX 5090 32 GB
Memory (RAM): 96GB (2x48GB) DDR5 6000MT/s CL36 Kit
Motherboard: ASUS PRIME X870-P WIFI CSM AM5 ATX
Storage: Boot Drive (Samsung 990 PRO 2TB), Work Drive (Lexar NM790 4TB)
Case: Fractal Torrent
Power Supply: be quiet! Straight Power 12 1200W
CPU
I have never had allegiance to either Intel or AMD for CPU’s and will happily pick either. However I had read about stability issues with the modern Intel ones, and being on a dead platform made them less appealing. It is unlikely I will upgrade the CPU anytime soon but the thought that I should be able to do so is nice. As for why the x3D chip over the regular one, thats because I found a deal on it and it worked out to be about the same price. The potential performance gains of the x3D cache sound like something I would like to experiment with as well.
Cooler
I used the Noctua D15 in my previous desktop when trying to make it quiet and was shocked at how well it worked. While there is a new version available, its almost twice the price in Australia. Since you don’t get twice the performance I opted for the older unit.
Why not an AIO? I don’t trust the seals, I don’t like that I have to replace the whole unit if anything fails, I don’t like pump noise and I don’t want more moving parts. Fans are pretty simple, as is a heat-sink. I know they can have better cooling power (probably useful in Australia) but that isn’t enough incentive for me. Plus I have known a few people with them and most have had an AIO issue at one point or another.
As for why I used the KryoSheet over thermal paste. Remember how I said I wanted this build to last 10 years? This is an answer to paste drying out over time. Literally a set and forget solution, albeit take some care when using it because its conductive. I used a small amount of the oil that was supplied to stick it to the center, with 4 tiny amounts of thermal paste on the corners to assist.
GPU
Although buying a 5090 is a contentious decision for pure gaming, I am not gaming using this machine very much. The main reason for it is the large 32 GB VRAM allowing me to load larger LLM models. With any model that fits in its RAM I get 200+ tokens per second out of it. This is a game changer for me when it comes to testing agentic code, or any other LLM shenanigans I am getting into.
As for why Palit? It was the cheapest one I could find. I actually got it BELOW the RRP (MSRP for USA people) which turned out to be an amazing deal. In fact the price was below the RRP nVidia lists for the 5090 in Australia.
Expensive? Yes. But I have saved several hundred dollars already using models on it, and it has been faster to iterate as well.
Memory
The memory I picked has the sweet spot DDR5 bandwidth of 6000MT/s albeit with not the best latency of CL36. Thankfully the x3D chip offsets this slightly with its huge L3 cache making it less sensitive to RAM latency.
As for why 2 sticks of RAM? I wanted to populate only 2 channels, allowing for EXPO to be enabled. I did want 128 GB but I couldn’t find reasonably priced 64 GB sticks. This gives me more than enough RAM for 99% of tasks, while giving me the full speed.
I think I got a little lucky buying this when I did as literally 2 weeks later the price of DD5 RAM shot through the roof due to it being used in data centers to run LLM’s.
Motherboard
I picked the ASUS board for one main reason. That reason being CSM (Corporate Stable Model), which means it is designed for stability. I only care that it runs, and does not break. I am not overclocking, I am not chasing the last 3% of performance. I just want it to work all the time. I think its also lower power usage too which is a plus.
Storage
I need a fair amount of storage, so wanted at least 4 TB. However there was a sale on the Samsung 990 PRO drive, so I ordered that and added the Lexar as the bulk storage work drive. This works out well because the Samsung has better random access than the Lexar making it useful for the OS and the Lexar has lower power usage and works well for pulling large files.
Case
I picked the Torrent over some cases I liked from be quiet! mostly because it was available and I got it on special (being on special is a pattern with my purchase decisions). It was not my first choice, but I think probably the right one which I will cover in the lowering noise section. One big advantage it has is shipping with 5 high quality fans, meaning I didn’t need to worry about buying any extras.
I was not interested in anything with RGB, and hence have the solid panel design. Boring, but for me the desktop is a tool not a toy.
Power Supply
My rule for power supplies is work out how much power the system can draw at max load, and add 20% for safety. This ensures it would meet any load spikes, and since PSU’s degrade over time will still have enough headroom in the future. My choice of parts had it listed at about 970w so 1200w was where I wanted to be.
I picked the be quiet! supply because it was not the lowest tier unit, had decent reviews, has japanese capacitors, had a quieter fan than other units in the same price range, and because I couldn’t find a reasonably priced Seasonic unit.
I have no complaints with it, and never hear the thing, which also fits into the 20% safety margin, since it means running under load it will be firmly in the most efficient band of the PSU and when idling should’t have the fan doing anything.
Reducing Noise
There is/are two main approaches in PC building when it comes to reducing noise. The first is to reduce the noise from components, either by using passive heat-sinks, or adding baffles and sound deadening foam and panels to insulate the noise from the fans. The latter is try and remove heat which causes your fans, which are the main source of noise from spinning faster.
I have always been a big believer in the first approach, and it took a lot of convincing for me to even consider the latter, which was the approach I tried this time.
I had picked components where possible to reduce noise, such as the power supply and cooler.
Keeping things quiet was always going to be challenge with a 170w CPU and a 575w GPU. However I was aware you could turn on eco mode for the CPU and either under-volt or power limit the GPU. While this sounds horrible, it turns out that over the last 10 years the manufacturers have been shipping hardware that is more or less factory overclocked. They do this because having a product that is 5% faster than the competition matters, and sitting at the top of chart matters even more.
However that last 5% of performance takes ~20% of the power budget to achieve. Lower the power budget and while technically you lose some performance, it is often in the range of 3-5% which is probably not noticeable day to day.
With the CPU this is easy to achieve, turn on ECO mode in the BIOS and done. The CPU is now power limited to 105W, with
minimal to no impact
on day to day tasks.
Limiting the GPU is not quite as easy. On Windows you can using things like MSI Afterburner to tweak the limits or change the voltages. On Linux your best best is to set the power limits using
nvidia-smi
once you have the drivers for it installed.
This is what I used
sudo nvidia-smi -pl 430
Which limits it to 430w which is about 75% of the GPU’s power budget. Since this does not persist on reboot the following systemd config when setup and enabled will do this for you on boot. Note you will need to replace 430 with whatever is appropriate for you.
[Unit]
Description=Set NVIDIA GPU Power Limit

[Service]
Type=oneshot
ExecStart=/usr/bin/nvidia-smi -pl 430

[Install]
WantedBy=multi-user.target
This has the added benefit of lowing the power draw on those problematic
12v connections
and hopefully reducing the chance of them melting or starting a fire.
Results?
Well the machine is quiet. Very very quiet. I was shocked. The flow through design of the torrent case has totally turned me around on the use of acoustic foam vs a flow through optimized case. Thinking about it, the idea of removing heat quickly makes a lot of sense. Rather than let the heat build up, keep it quiet by running the fans at an inaudible level all the time so you never have to spin them quickly.
The only time I have ever really heard it is when I ran Furmark and WPrime for an hour or so in order to really stress the components and observe the system drawing 800w (done before I turned it down).
Its possible you may still want the acoustic foam however if you have components that exhibit coil whine. Thankfully none of mine seem to have this, and on the odd occasion I do push the machine hard I don’t hear that much from it.
The memory training portion of the startup took a lot longer than I thought it would. While I was aware there is a training process, I was not aware it would take 5+ minutes. It’s a little worrying when you first turn the PC on and nothing happens for a while. Knowing to wait here is something that cannot be understated and probably needs more call out.
For LLM calls I get 200+ tokens per second when the model fits into VRAM which is more than fast enough for my needs, and has freed me up from waiting very long or opening my wallet every day to OpenAI. Of course its a little more frustrating trying to find a model that works but thats part of the fun.
I also configured it to work remotely so I can use the LLM’s on my M1 Mac laptop while working at home or remotely.
In short though, while standard desktop work feels 100% the same as before, anything that required the CPU to actually work is so much faster. Compile times are blazingly quick, things open instantly and I never worry about running out of RAM anymore… other that VRAM but thats another matter.
Fedora 42 worked more or less out of the box, although it was slightly laggy at 4K till I had the nVidia drivers installed.
In fact the only thing I could think I would want different is a 6000 RTX PRO GPU with 96 GB of VRAM, but I don’t even know where to order one of those and it costs more than the entire system I just built. Maybe in a few years I can pick up one second hand.
