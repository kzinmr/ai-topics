# Bogdan Ionescu (BogdanTheGeek)

**URL:** https://bogdanthegeek.github.io/blog/
**Blog:** BogdanTheGeek's Blog
**GitHub:** @BogdanTheGeek
**Identity:** Bogdan Ionescu — embedded engineer, hobby machinist, origami artist, Romanian
**Themes:** Embedded systems, microcontrollers, hardware hacking, DIY PCB fabrication, resource-constrained programming, creative reuse of consumer electronics
**Tech Stack:** C, MicroPython, ARM Cortex-M, RISC-V, ESP32, custom PCBs

## Overview

Bogdan Ionescu, known online as **BogdanTheGeek**, is an embedded engineer who publishes deeply technical, hands-on projects that blend serious engineering with creative experimentation. His blog sits at the intersection of embedded systems development, hardware hacking, and maker culture — but unlike many maker blogs, Ionescu's work is backed by professional-grade engineering rigor. He doesn't just assemble kits; he writes custom allocators, ports network stacks to microcontrollers with 3KB of RAM, and reverse-engineers the silicon inside disposable vapes.

Ionescu describes himself as a "hobby collector, machinist on call, origami artist some of the time, embedded engineer most of the time." This multi-faceted identity is reflected in his work: his projects range from serious infrastructure tooling (a custom memory allocator for embedded systems) to creative experiments (running a web server on a disposable vape pen) to practical hobbies (building a PID temperature controller for his pottery kiln).

What distinguishes Ionescu's writing is its **unflinching technical honesty**. He doesn't oversimplify or hand-wave. When he builds a memory allocator, he explains the trade-offs between allocation speed, memory overhead, and fragmentation resistance. When he ports a network stack to a microcontroller, he documents the hard faults caused by memory alignment bugs and the ring buffer optimizations that reduced ping times from 1.5 seconds to 20 milliseconds. This is engineering writing for engineers — detailed, accurate, and useful.

## Timeline

| Date | Event |
|------|-------|
| 2014 | Creates GitHub account; begins publishing open-source embedded projects |
| ~2017–2019 | Develops **ESP_RC** — open-source transmitter/receiver for RC vehicles based on ESP-NOW protocol |
| Sep 2019 | Publishes "Cross Compiling Docker Images" — multi-architecture container build techniques |
| ~2019–2021 | Builds **CCCPPS** — Cheap Crappy Constant Current Portable Programmable Power Supply |
| 2022–2023 | Develops **MicroAlloc** — a custom first-fit free list heap allocator for embedded systems |
| 2024 | Publishes "Making PCBs" — detailed guide to home PCB fabrication |
| 2024 | Publishes "Pottery Is Great" — reflection on stepping away from screens and working with clay |
| 2024–2025 | Develops **MicroPPPID** — MicroPython-based programmable PID kiln controller for pottery firing |
| 2025 | Publishes "Hosting a WebSite on a Disposable Vape" — reverse-engineers a PUYA PY32F002B MCU (24MHz Cortex-M0+, 24KB flash, 3KB RAM) and runs a full TCP/IP web server on it |
| Sep 2025 | Releases **semihost-ip** — running TCP/IP over ARM SWD debug lines; reaches 945+ GitHub stars |
| Oct 2025 | Publishes "World's Cheapest ARM Debugger is Actually RISC-V" — debugging a free ARM MCU with a 10¢ RISC-V probe |
| Oct 2025 | Releases **ch32v003-daplink** — DAPLink (CMSIS-DAP) ported to WCH CH32V003 using ch32fun and rv003usb |
| 2025–2026 | Blog reaches wide audience through coverage on Hackaday, Tom's Hardware, The Register, and Interesting Engineering |
| 2026 | Continues publishing embedded engineering projects and practical guides |

## Core Ideas

### Creative Reuse of E-Waste

Ionescu's most viral project — running a web server on a disposable vape — exemplifies his philosophy of finding computational potential in discarded objects:

> "You may look at those specs and think that it's not much to work with. I don't blame you, a 10y old phone can barely load Google, and this is about 100x slower. I, on the other hand, see a blazingly fast web server."

The project began when Ionescu noticed that certain disposable vapes used a labeled PUYA microcontroller instead of an anonymous black blob. The chip — a PY32F002B, a 24MHz ARM Cortex-M0+ with 24KB flash and 3KB RAM — was originally designed for basic control functions in a nicotine delivery device. Ionescu saw a complete microcomputer.

His approach was methodical:
1. **Identify the chip** through physical inspection and datasheet research
2. **Exploit the debug interface** (ARM SWD) that the manufacturer left accessible
3. **Use semihosting** — a debugger feature that lets the target MCU make I/O calls through the host — as a serial communication channel
4. **Port SLIP** (Serial Line Internet Protocol) over the virtual serial connection
5. **Implement uIP 0.9** — a minimalist TCP/IP stack — to handle network traffic
6. **Build a basic HTTP server** to serve static content

The initial results were discouraging: pings took ~1.5 seconds with 50% packet loss, and a simple page took over 20 seconds to load. Ionescu didn't give up — he traced the bottleneck to byte-by-byte serial reads, implemented a ring buffer, and reduced ping times to ~20ms with zero packet loss. A full page loaded in about 160ms.

> "Someone's trash is another person's web server."

This project was covered by Hackaday, Tom's Hardware, The Register, and Interesting Engineering, bringing significant attention to Ionescu's blog.

### Embedded Memory Management as a Craft

**MicroAlloc**, Ionescu's custom heap allocator, represents serious embedded engineering disguised as a simple project. The key insight is elegant: instead of using full-word absolute pointers in the free list metadata, store **heap offsets**. For heaps under 64KB, this reduces per-allocation overhead from 4-8 bytes to just 2 bytes.

> "Every self-respecting embedded engineer avoids dynamic allocations like the plague... I don't think you should never use a dynamic allocator, but it should be a last resort, especially for embedded applications."

Ionescu's recommended hierarchy for flexible data:
1. **Static allocation** — safest, but requires adequate stack headroom
2. **One-time dynamic allocation at startup** — never freed
3. **Specialized allocators** — scratch buffers, block allocators (object pools), arena allocators
4. **Dynamic heap allocators** — last resort only

His deferred coalescing strategy — skipping merge-on-free and instead running `micro_alloc_defrag()` manually when convenient — is a practical trade-off that most allocator implementations don't consider. It acknowledges that in embedded systems, you often know when the CPU has spare cycles and when it doesn't.

### Practical Pottery Meets Embedded Systems

**MicroPPPID** — a MicroPython-based programmable PID controller for pottery kiln firing — exemplifies Ionescu's cross-disciplinary approach. When he took up pottery, he found existing kiln controller projects (PyKiln, PIDKiln) too fragile:

> "After 2 hours of messing with different versions of Arduino IDE, library versions and node.js dependencies, I gave up. I am sure some of these projects have worked perfectly for some people, but they were way too fragile for me. I didn't want to waste any more time fixing someone else's code."

His solution used MicroPython on an ESP32-S2, with:
- Vendored dependencies (no git submodules, no package managers)
- JSON-based temperature profile configuration
- WebSocket-based real-time monitoring and control
- Over-the-air updates via drag-and-drop
- A build step that compiles `.py` files to `.mpy` bytecode and minifies/gzips other assets

The reflection is telling:

> "When I started using Python, I hate it! Broken dependencies, half a dozen different packaging tools, no types, horrible performance etc. I still can't say I like it, I would never choose to use it anywhere where performance or efficiency matters. But I have to admit, it did feel good to work on this project. I can only imagine that this is how people felt when C came about. If you spend any significant amount of time writing assembly, you will immediately appreciate what C does for you."

### The RISC-V Opportunity

Ionescu's post "World's Cheapest ARM Debugger is Actually RISC-V" documents his discovery that a $0.10 RISC-V probe (the CH32V003) could debug ARM microcontrollers more effectively than expensive commercial tools. This reflects his broader belief that **the best tools are the ones you can understand, modify, and afford**.

His **ch32v003-daplink** project — porting the CMSIS-DAP debugger protocol to the WCH CH32V003 RISC-V chip — is a practical demonstration of this philosophy. By using open-source toolchains (ch32fun, rv003usb), he created a functional debugger that costs pennies instead of hundreds of dollars.

## Key Quotes

> "You may look at those specs and think that it's not much to work with. I don't blame you, a 10y old phone can barely load Google, and this is about 100x slower. I, on the other hand, see a blazingly fast web server."
> — "Hosting a WebSite on a Disposable Vape"

> "Every self-respecting embedded engineer avoids dynamic allocations like the plague."
> — MicroAlloc project

> "After 2 hours of messing with different versions of Arduino IDE, library versions and node.js dependencies, I gave up."
> — MicroPPPID project

> "When I started using Python, I hate it! Broken dependencies, half a dozen different packaging tools, no types, horrible performance etc... But I have to admit, it did feel good to work on this project."
> — MicroPPPID reflection

> "If you are sick of technology pick up pottery."
> — "Pottery Is Great"

> "Bogdan Ionescu — hobby collector, machinist on call, origami artist some of the time, embedded engineer most of the time."
> — Blog about page

## Recent Themes (2024–2026)

- **E-waste as computing platform**: Turning disposable vapes, cheap development boards, and discarded electronics into functional computing devices
- **Ultra-constrained programming**: Building real applications on microcontrollers with single-digit kilobytes of RAM
- **Open-source debugging tooling**: RISC-V probes, DAPLink implementations, semihosting-based network stacks
- **Custom memory management**: MicroAlloc as a demonstration of first-principles allocator design
- **Cross-disciplinary making**: Pottery kiln controllers, origami design tools (CPoogle), RC vehicle electronics
- **Home PCB fabrication**: Practical guides for producing circuit boards without professional equipment

## Related

- [[The Silicon Underground]] — Dave Farquhar's blog; shares Ionescu's deep interest in hardware history and technical archaeology
- [[Construction Physics]] — Brian Potter's newsletter; both Ionescu and Potter examine the material foundations of technology
- [[Tedium]] — Ernie Smith's newsletter; both find fascination in overlooked and discarded technology
- [[Philip Laine]] — another engineer who publishes practical, project-based technical writing
- [[Semihost-IP]] — Ionescu's TCP/IP over SWD project (945+ GitHub stars)
- [[MicroPPPID]] — MicroPython PID kiln controller for pottery

## Sources

- BogdanTheGeek blog: https://bogdanthegeek.github.io/blog/
- "Hosting a WebSite on a Disposable Vape" (2025)
- "World's Cheapest ARM Debugger is Actually RISC-V" (2025)
- "MicroAlloc: A very small allocator" (2022–2023)
- "MicroPPPID: MicroPython Programable PID for Temperature Control" (2024–2025)
- "Making PCBs" (2024)
- "Pottery Is Great" (2024)
- GitHub: @BogdanTheGeek (52 public repos, 317 followers)
- semihost-ip: https://github.com/BogdanTheGeek/semihost-ip (945+ stars)
- Coverage on Hackaday, Tom's Hardware, The Register, Interesting Engineering (2025–2026)
