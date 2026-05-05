---
title: "Explaining VarnishHist - What Does it Tell Us"
url: "https://boyter.org/2016/10/explaining-varnishhist/"
fetched_at: 2026-05-05T07:02:00.444708+00:00
source: "Ben Boyter"
tags: [blog, raw]
---

# Explaining VarnishHist - What Does it Tell Us

Source: https://boyter.org/2016/10/explaining-varnishhist/

The varnishhist tool is one of the most underused varnish tools that come with your standard varnish install. Probably because of how it appears at first glance.
In short, you want as many
|
symbols as possible and you want everything far toward the left hand side. The closer to the left the faster the responses are regardless if they are cached or not. The more
|
symbols then more items were served from cache.
A small guide,
'|' is cache HIT
'#' is cache MISS
'n:m' numbers in left top corner is vertical scale
'n = 2000' is number of requests that are being displayed (from 1 to 2000)
The X-axis is logarithmic time between request request from kernel to Varnish and response from Varnish to kernel.
The times on the X-axis are as such,
1e1 = 10 sec
1e0 = 1 sec
1e-1 = 0.1 secs or 100 ms (milliseconds)
1e-2 = 0.01 secs or 10 ms
1e-3 = 0.001 secs or 1 ms or 1000 µs (microseconds)
1e-4 = 0.0001 secs or 0.1 ms or 100 µs
1e-5 = 0.00001 secs or 0.01 ms or 10 µs
1e-6 = 0.000001 secs or 0.001 ms or 1 µs or 1000 ns (nanoseconds)
Below is the varnishhist for searchcode.com showing that while most responses are served in about 100ms not many are cached. This can mean one of a few things.
The responses are not cache-able and you need to adjust the back-end responses to have the correct headers (or override the settings with VCL config).
The cache timeout for the back-end responses isn’t high enough to ensure that later requests are served from cache.
There isn’t a large enough cache to hold all the responses (that’s the problem in this case).
1:20, n = 2000

                                  ##
                                  ##
                                  ##
                                  ##
                                  ##
                                  ##
                                  ##
                                 ###
                                 ####
            |                    ####
            |                    ####
            |                    ####
            |                    #####
            |                    #####
            |                    #####
            |                   #######
            |                   #######
            ||  |    #      #   ##########

+------+------+------+------+------+------+------+------+------
|1e-6  |1e-5  |1e-4  |1e-3  |1e-2  |1e-1  |1e0   |1e1   |1e2
