---
title: "WeatherNext — Google DeepMind AI Weather Forecasting"
created: 2026-08-10
updated: 2026-08-10
type: concept
tags: [model, deepmind, google, google-deepmind, ai-in-science, open-source, generative-ai, deep-learning, forecasting, geospatial, simulation]
sources: [raw/articles/2026-05-XX_deepmind_weathernext-cyclone-forecasting.md]
---

## Overview

WeatherNext is a family of AI-based weather forecasting models developed by [[entities/deepmind|Google DeepMind]] and Google Research. The latest version, **WeatherNext 2**, represents a breakthrough in AI-driven meteorology — capable of generating hundreds of probabilistic weather scenarios in under a minute on a single [[entities/google-tpu|TPU]], matching or exceeding the accuracy of traditional physics-based Numerical Weather Prediction (NWP) systems while being orders of magnitude faster.

## Architecture

WeatherNext 2 is built on a **Functional Generative Network (FGN)** — a novel architecture that injects noise directly into the model's function space, producing coherent variability across weather forecasts. Unlike traditional NWP models that solve physical equations on supercomputers, WeatherNext learns atmospheric dynamics from data. The model was co-trained on nearly 20 terabytes of global atmospheric data alongside the expert-curated IBTrACS (International Best Track Archive for Climate Stewardship) historical cyclone database spanning approximately 5,000 storms.

The FGN approach enables skillful "joint" forecasting — predicting how multiple weather variables interact across regions — even though the model is only trained on individual "marginal" variables like temperature, wind speed, and humidity at specific locations. This emergent capability allows WeatherNext to model complex systems such as regional heat events or expected power output across wind farms.

Underlying the architecture are graph neural networks (GNNs) operating at multiple scales, an approach also used in earlier DeepMind weather models such as GraphCast and GenCast. The model generates 15-day global forecasts at up to 1-hour temporal resolution.

## Performance

WeatherNext 2 surpasses the previous WeatherNext generation on **99.9%** of variables (temperature, wind, humidity, etc.) and lead times (0–15 days). Each ensemble forecast — hundreds of possible weather outcomes from a single initial state — completes in under a minute on one TPU. Equivalent physics-based ensemble runs would require hours on a supercomputer.

## Cyclone Forecasting Breakthrough

A key advance is cyclone (hurricane/typhoon) prediction. WeatherNext provides an **extra day of warning** for cyclone landfall compared to conventional methods. This additional lead time is critical for evacuation planning and disaster preparedness. The model was trained end-to-end on both global weather dynamics and the historical cyclone record, allowing it to model extreme weather events directly rather than relying solely on general atmospheric simulation.

## Open Sourcing and Deployment

Google DeepMind has open-sourced the WeatherNext model, making it available for research and operational use. Forecast data is accessible through Google Earth Engine and BigQuery, with an early access program on Google Cloud's Vertex AI for custom inference. WeatherNext technology now powers weather forecasts in [[entities/google|Google]] Search, Gemini, Pixel Weather, and Google Maps Platform.

## Broader Context: AI for Science

WeatherNext sits within [[entities/deepmind|Google DeepMind]]'s broader AI-for-science portfolio, which includes landmark achievements such as AlphaFold for protein structure prediction. It exemplifies a pattern where [[concepts/generative-ai|generative AI]] models — trained on vast observational datasets — outperform traditional physics-based [[concepts/scenario-based-simulation|simulation]] in both speed and accuracy. This mirrors wider trends in [[concepts/world-models-science|world models for scientific discovery]] and underscores the growing role of [[concepts/open-source-ai|open-source AI]] in critical infrastructure domains like meteorology.

The WeatherNext models follow earlier DeepMind forecasting systems GraphCast (2023) and GenCast (2024), each demonstrating that data-driven approaches can match or surpass the gold-standard ECMWF Integrated Forecasting System (IFS) — the world's leading physics-based NWP model.

## See Also

- [[entities/deepmind|Google DeepMind]]
- [[entities/google-tpu|Google TPU]]
- [[concepts/generative-ai|Generative AI]]
- [[concepts/open-source-ai|Open-Source AI Strategy]]
- [[concepts/scenario-based-simulation|Scenario-Based Simulation]]
- [[concepts/world-models-science|World Models for Scientific Discovery]]
