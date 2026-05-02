---
title: Physical AI
created: 2026-04-28
updated: 2026-04-28
type: concept
tags:
  - robotics
  - autonomous-systems
  - simulation
  - company
  - screen-vs-physical
sources:
  - raw/newsletters/2026-04-27-physical-ai-that-moves-the-world-qasar-younis-peter-ludwig-applied-intuition.md
---

# Physical AI

## Overview

**Physical AI** refers to AI systems that directly interact with the physical world — autonomous vehicles, humanoid robots, industrial automation, drones, and embodied AI. Contrasts with **Screen AI** (models operating purely in digital spaces like chat, code generation, or image synthesis).

## Bits vs Atoms Thesis

Marc Andreessen (Physical AI Day, Apr 2026) frames AI's evolution as two waves:
- **Virtual wave**: AI that operates in digital spaces — text, code, images. "You only need a keyboard."
- **Physical wave**: AI that operates in the real world — robots, vehicles, manufacturing.

The physical wave faces fundamentally different challenges:
- Safety is non-negotiable (a buggy robot can cause physical harm)
- Real-world testing requires expensive hardware and controlled environments
- Latency constraints are stricter (millisecond-level decisions for autonomous vehicles)
- Hardware form factors matter (weight, power, thermal budgets)

## Applied Intuition Platform

Founded by Qasar Younis (CEO) and Peter Ludwig (CTO), Applied Intuition builds infrastructure for Physical AI:

- **Simulation platforms** for autonomous vehicle testing
- **Sensor validation** pipelines (cameras, LiDAR, radar)
- Works with major automakers to validate self-driving systems
- Marc Andreessen is a notable backer and advisor
- **Partnership with LG Innotek** (Mar 2026) for sensor validation systems

## The "Robot Dog Problem"

Andreessen's anecdote at Physical AI Day: bought a Chinese robot dog that weighed 150 pounds, needed a support rack when idle, and was unsafe around children. This illustrates the gap between AI demo capability and product readiness in the physical world.

## Key Challenges

1. **Safety Certification**: Proving AI systems are safe enough for physical deployment
2. **Simulation Fidelity**: Virtual testing must accurately reflect real-world physics and edge cases
3. **Hardware Constraints**: Edge devices with limited compute, power, and thermal budgets
4. **Regulatory Landscape**: Varies by jurisdiction; autonomous vehicles face stricter rules
5. **Simulation-to-Reality Gap**: Models trained in simulation don't always transfer to real-world conditions

## Onboard vs Offboard AI

| Dimension | Onboard AI | Offboard AI |
|-----------|-----------|-------------|
| Location | Edge device (vehicle, robot) | Cloud datacenter |
| Latency | Milliseconds, real-time | Higher latency acceptable |
| Compute | Limited (power/thermal constraints) | Virtually unlimited |
| Connectivity | Must work offline | Requires network |
| Use Cases | Collision avoidance, navigation | Fleet management, route planning |

Physical AI systems typically use a hybrid: onboard for critical real-time decisions, offboard for planning and coordination.

## Relationship to Agentic AI

Physical AI extends [[agentic-engineering]] into the real world. The same patterns apply — tool use, autonomous loops, safety constraints — but with physical consequences:

- An agent that "figures it out" for 6 hours is powerful in code; in a factory or vehicle, the same autonomy requires hard fail-safes
- [[harness-engineering]] patterns become critical: how to constrain physical AI agents while allowing useful autonomy
- [[agent-team-swarm]] patterns apply to fleet coordination and multi-robot systems

## Related Pages

- [[applied-intuition]] — Company building Physical AI infrastructure
- [[agentic-engineering]] — Developer patterns for autonomous agents
- [[harness-engineering]] — Constraining and guiding agent behavior
- [[agent-team-swarm]] — Multi-agent coordination (relevant for fleet management)
