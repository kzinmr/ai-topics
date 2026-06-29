---
title: "NVIDIA 45°C Data Center Cooling"
created: 2026-06-25
updated: 2026-06-25
type: concept
tags:
  - nvidia
  - infrastructure
  - sustainability
  - hardware
  - cloud-infrastructure
  - data-center
  - optimization
sources:
  - raw/articles/2026-06-25_nvidia-45c-liquid-cooling-data-center.md
---

# NVIDIA 45°C Data Center Cooling

NVIDIA's 45°C warm-water liquid cooling design is a breakthrough in AI data center infrastructure, introduced with the Rubin generation of NVIDIA AI infrastructure. It is the world's first AI platform to achieve 100% liquid cooling — every chip and every networking component is cooled entirely by liquid in a closed loop, with no fans anywhere in the system. The counterintuitive design runs coolant at temperatures up to 45°C (113°F), hotter than a hot tub, and this higher temperature limit is precisely what makes the system dramatically more energy efficient.

## How It Works

### Direct-to-Chip Liquid Cooling

Coolant — a 75% water and 25% propylene glycol mixture — flows through cold plates that sit directly on processors, pulling heat out at the source. The coolant enters the rack at up to 45°C and exits at roughly 55°C after absorbing heat across the chip surface. Despite the warm inlet temperature, liquid-cooled cold plates keep device temperatures within validated operating limits, and processors continue to operate at full performance.

### Closed-Loop System

The system operates as a closed loop: coolant flows from a coolant distribution unit (CDU) to the servers and back, recirculating continuously. Unlike traditional air-cooled data centers that depend on large volumes of cooled air (requiring energy-intensive chillers), this design captures heat directly at the chip and transports it through liquid loops. The closed loop is filled once and runs for the life of the facility.

### Dry-Cooler-Based Heat Rejection

In favorable climates, the facility can reject heat using outdoor dry coolers — essentially large radiator coils positioned outside the building — without turning on mechanical chillers. The data center ambient temperature becomes flexible because nothing in the server depends on cool air; the liquid does all the work. Chillers may only be needed roughly 1% of the year in extreme climates.

## Efficiency Gains

### Water Conservation

A 50-megawatt hyperscale facility can save over $4 million annually in cooling-related energy and water costs by moving to liquid-cooled infrastructure. In favorable climates, NVIDIA's design can reduce facility cooling water consumption from roughly **2.6 million gallons per megawatt per year** (conventional cooling-tower-based systems) to **near zero** — up to a 100% reduction in water use.

### Energy Savings

Historically, cooling alone has accounted for up to 40% of a data center's electricity consumption. Raising chiller plant temperatures by just one degree can cut cooling energy costs by about 4%. At the 45°C operating point, those savings multiply substantially across hyperscale deployments.

### Waste Heat Recovery

The higher-temperature coolant output (55°C) creates new possibilities for waste heat recovery, where residual heat from AI factory operations can be repurposed to heat commercial or residential buildings nearby.

## Physical Transformation of the Data Center

The Rubin architecture eliminates the traditional data center hallmarks:

- **No fans**: The system has zero fans — cooling fans in traditional data centers contribute to noise levels at or above 85 decibels, loud enough to require ear protection.
- **No hot/cold aisle choreography**: The carefully managed airflow patterns of conventional data centers become irrelevant.
- **Dramatically smaller footprint**: Liquid cooling infrastructure takes significantly less space compared to traditional air-cooling equipment.
- **No cold data center requirement**: The long-standing misconception that a cold data center is an efficient one is overturned; chips can sustain far warmer environments than previously assumed.

## Industry Transition

Because the NVIDIA Rubin platform integrates 100% liquid-cooled infrastructure, every cloud provider and data center operator building for it is making the transition. Motivair, the advanced cooling division of Schneider Electric, has worked alongside NVIDIA's product roadmap for nearly a decade and is a key ecosystem partner.

As Motivair President and CEO Richard Whitmore noted: "Once the watts per chip crossed a certain level, liquid cooling became mandatory."

## Limitations

The geography caveat matters: a data center in a cool climate (e.g., Scottish Highlands) can achieve chiller-less operation nearly year-round, while one in Phoenix, Arizona, faces more challenging conditions. However, even in warmer climates, the 45°C coolant design moves operators significantly closer to the chiller-less ideal.

## Related Pages

- [[entities/nvidia]] — NVIDIA company page
- [[concepts/ai-affordability-crisis]] — Data center costs as a driver of AI economics
- [[entities/modal-labs]] — Inference infrastructure provider in the cooling/efficiency space
- [[concepts/google-spacex-ai-compute-deal]] — Related large-scale AI infrastructure development
