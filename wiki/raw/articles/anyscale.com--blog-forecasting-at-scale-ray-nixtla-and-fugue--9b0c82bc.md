---
title: "Forecasting at Scale"
url: "https://anyscale.com/blog/forecasting-at-scale-ray-nixtla-and-fugue"
fetched_at: 2026-09-27T10:01:15.197239+00:00
source: "Anyscale Blog"
tags: [blog, raw]
---

# Forecasting at Scale

Source: https://anyscale.com/blog/forecasting-at-scale-ray-nixtla-and-fugue

With increasingly fast-changing and  dynamic environments, traditional forecasting techniques are being replaced with AI-driven forecasting.
According to McKinsey
, applying AI-driven forecasting can reduce errors by between 20-50% and reduce losses in sales and product unavailability by up to 65%.
Whether it’s predicting the required parts to purchase for machine maintenance, the number of items that will sell in a month, the amount of  ingredients to stock, or the seasonal demand for apparel, forecasting at scale has become a crucial tool for organizations.  In financial services, CPG/retail, and IOT/operational ML, forecasting and time series analysis are  used for algorithm trading, financial modeling, market simulation, backtesting, supply chain management, anomaly detection, and more.
The success for any forecasting model rests on the amount of training data and sophistication of the applied models. The ability to train, tune, and experiment requires a flexible, scalable and efficient infrastructure. In this blog post we’ll cover how Nixtla and Ray provides a foundation to perform forecasting at scale.
Ray is a unified framework that allows organizations to effortlessly scale their Python and AI workloads. It is an open and portable toolkit that can be used for your entire ML lifecycle and python native applications.
Ray
also has a growing community and built-in and python native integrations with the ML ecosystem, making it easy to deploy and run on public cloud such as AWS and anywhere else running Kubernetes.
Nixtla
is a time series research and deployment startup that offers a set of libraries intended to make available the most comprehensive and performant set of forecasting capabilities in a simple and easy-to-use Python library. Nixtla emphasizes standardization and performance, allowing organizations to solve real-world forecasting challenges.
Nixtla’s efficient algorithms leverage the computational scalability of Ray to allow for easy forecasting at scale. In a previous
blog post
, using the StatsForecast library, we were able to demonstrate how to train 1 million models in under 30min.
The goal for many organizations is to predict their operational data  time series using the most up-to-date information available at the lowest granularity.  For different teams within an organization, this may mean slightly different things, but consistently, we are seeing an increase in the implementation of forecasting at more granular levels and delivering predictions more frequently within shorter timeframes.
While this may seem challenging, advancements in technology and the accessibility of cloud computing have made this task more manageable. Anyscale, often works with customers who generate millions of forecasts or process terabytes of time series, often within a time window of no more than a few hours daily. Processing input data quickly is crucial, but the real challenge lies in utilizing hundreds or even thousands of virtual cores to train the models necessary for these processes.
By utilizing Anyscale, organizations can quickly allocate and just as easily downscale resources based on their forecasting cycles, providing the necessary capacity to deliver accurate results in a timely and cost-effective manner. Time Series modeling has been one of the weak points of the Python ecosystem compared to R. Statistical modeling libraries such as pmdarima and statsmodels are order of magnitude slower than R, and state-of-the-art algorithms remain challenging to implement. Using Nixtla's StatsForecast on Ray, we have shown forecasting at scale and even how to outperform current benchmarks in the R and Python ecosystems.
Together, Ray and Nixtla, provide a powerful solution for organizations looking to forecast at scale. To learn more about how to use these tools together, check out our tutorial on forecasting at scale using Ray, Nixtla, and Fugue. With this tutorial, you'll be able to easily scale your forecasting efforts and solve real-world challenges with ease,  understand general best practices when working with time series data and explore the various kinds of statistical time series modeling techniques.
Together, Ray and Nixtla, provide a powerful open-source solution for organizations looking to perform forecasting and anomaly detection at scale. For more information, check out the
Anyscale Nixtla webinar
on this topic and see a demonstration
