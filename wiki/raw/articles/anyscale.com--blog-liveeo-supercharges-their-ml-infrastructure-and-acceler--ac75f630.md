---
title: "LiveEO supercharges their ML infrastructure and accelerates their geospatial workloads practice"
url: "https://anyscale.com/blog/liveeo-supercharges-their-ml-infrastructure-and-accelerates-their-geospatial"
fetched_at: 2026-09-27T10:01:15.371512+00:00
source: "Anyscale Blog"
tags: [blog, raw]
---

# LiveEO supercharges their ML infrastructure and accelerates their geospatial workloads practice

Source: https://anyscale.com/blog/liveeo-supercharges-their-ml-infrastructure-and-accelerates-their-geospatial

LiveEO
accelerates and optimizes their geospatial workloads by up to 65% using
Anyscale
and
Prefect Cloud
.
LiveEO
, a startup based in Germany, focuses on providing actionable insights on earth observation data by processing large-scale satellite-based images for use cases such as infrastructure monitoring for public utilities and transportation.
Electric grid and railway companies can now use LiveEO satellite asset monitoring solutions to provide actionable insights for various solutions such as storm response, vegetation management, and ground deformation.
Asset monitoring solutions:
Vegetation Management Insights
: Our vegetation management solution detects and assesses trees and provides prioritized risk evaluations based on vegetation condition and distance to your assets.
Ground Movement Insights
: Our ground deformation solution detects vertical and lateral ground displacements in the millimeter range, identifies trends and alerts you of any risk to your assets.
Rapid Response Insights
: Our storm response solution pinpoints damaged sites following a storm, regardless of daylight or cloud cover, and notifies field teams in record time.
On any given day, it is not uncommon for LiveEO to process up to two petabytes of data. It was imperative for LiveEO to build a Python-based solution that could scale efficiently in a timely manner.
Link
Before using Anyscale and Prefect, the LiveEO data science stack was “hand-crafted”
Fig. Artisanal data science requires a lot of different tools and craftsmanship.
LiveEO's data science stack had some limitations:
It consisted of diverse tools, including a Jupyter Notebook, Airflow, and AWS Batch.
There was a heavy reliance on team tribal knowledge with no standardization, leading to inconsistency across the pipelines.
There needed to be a systematic approach to package and release, making reproducibility and consistency challenging.
As a result of LiveEO's artisanal data science practice, each pipeline was unique and considered a work of art, which made it difficult for other teams to reproduce. The pipelines were semi-automated and required hand-holding, and it was challenging to determine the right size of compute resources for each pipeline.
Furthermore, limited observability made it difficult to monitor the health of the pipelines and identify any issues in a timely manner. This made recovery from failure a time-consuming, painful process.
These limitations hindered the efficiency and scalability of LiveEO's data science operations and slowed their time to market for their solutions and new features.
Link
LiveEO’s machine learning platform north star
Fig. ML factory
LiveEO’s data science team needed to upgrade their ML stack and had a few goals in mind:
Data science pipelines needed to be standardized, automated, versioned and reproducible.
Release packages should be consumed via API or a UI and composable.
The developer experience should abstract the infrastructure and allow for the workload to scale for CPU and GPUs seamlessly all in Python.
Packages and pipeline updates could be automated, tested, and deployed continuously.
Fig. Infrastructure abstraction should be in Python and easy to use.
Link
The Anyscale and Prefect integration
Anyscale provides a modern ML infrastructure stack and a managed service to scale your Ray workloads, while
Prefect
provides a powerful workflow automation, orchestration, and monitoring service all in an easy native Python environment leveraging Python decorators.
LiveEO can now leverage Anyscale for instant scalability, and cost efficiency using spot instances for their managed Ray clusters while benefiting from Prefect Cloud to scale their operations using the workflow orchestrator and monitoring solutions. The Anyscale-Prefect built-in integration provides a simple “RayTaskRunner” that can be incorporated into a Prefect flow, automatically scaling LiveEO’s workflows
Fig. RayTaskRunner allows you to submit tasks in parallel.
Fig. Scaling from 0 to 1k cores in about 1 minute.
LiveEO achieved remarkable results through the combined use of Anyscale and Prefect. By leveraging Anyscale's distributed computing capabilities in tandem with Prefect's intuitive workflow automation and orchestration engine, LiveEO reduced runtime by 30% — translating to a staggering 65% reduction in costs.
Further, LiveEO's data science operations have been transformed. Teams were able to streamline, automate, and standardize their practices. The result? Increased continuous delivery, and faster and more reliable customer service — all significantly boosting LiveEO's bottom line.
For more on these powerful tools, check out the
livestream recording
and the
prefect-ray
integration.
