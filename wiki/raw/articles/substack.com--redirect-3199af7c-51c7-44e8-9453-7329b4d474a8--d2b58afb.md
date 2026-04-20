---
title: "Brian Scanlan - Intercom"
url: "https://substack.com/redirect/3199af7c-51c7-44e8-9453-7329b4d474a8?j=eyJ1IjoiMmZseDYifQ.6O_iC1_GWCzChnbrHzSrs1hMpJpoODTUJm_FAk3tf6E"
fetched_at: 2026-04-20T15:47:37.520061+00:00
source_date: 2026-04-20
tags: [newsletter, auto-ingested]
---

# Brian Scanlan - Intercom

Source: https://substack.com/redirect/3199af7c-51c7-44e8-9453-7329b4d474a8?j=eyJ1IjoiMmZseDYifQ.6O_iC1_GWCzChnbrHzSrs1hMpJpoODTUJm_FAk3tf6E

In order to protect against various load balancing failures, the host selection algorithm on the load balancer can be modified to take into account data available about the state of the entire service and each host server in the cluster. The state can include a number of metrics, including the sampled response time taken by the selected host service. The load balancer can use the state information in order to detect anomalies among the host services. For example, the load balancer can determine…
Show more
In order to protect against various load balancing failures, the host selection algorithm on the load balancer can be modified to take into account data available about the state of the entire service and each host server in the cluster. The state can include a number of metrics, including the sampled response time taken by the selected host service. The load balancer can use the state information in order to detect anomalies among the host services. For example, the load balancer can determine that the sampled response time of one host service has deviated by more than a standard deviation limit (or other predetermined threshold) from the sampled response times of the other host services in the cluster. If such an anomaly is detected, the load balancer can take various remedial actions, such as disabling the routing of incoming requests to the potentially faulty host service.
Show less
