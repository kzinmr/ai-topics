---
title: "Websites have a new way to spy on visitors: Analyzing their SSD activity"
url: "https://arstechnica.com/security/2026/05/websites-have-a-new-way-to-spy-on-visitors-analyzing-their-ssd-activity/"
fetched_at: 2026-05-29T07:01:25.796792+00:00
source: "daringfireball.net"
tags: [blog, raw]
---

# Websites have a new way to spy on visitors: Analyzing their SSD activity

Source: https://arstechnica.com/security/2026/05/websites-have-a-new-way-to-spy-on-visitors-analyzing-their-ssd-activity/

While each file system is sandboxed, meaning it’s isolated from other websites and from the device system itself, the JavaScript can measure the I/O interactions. Then, by running those interactions through a pretrained
convolutional neural network
—a system that uses deep learning to analyze text, audio, and images—the attacker can deduce various apps and websites open on the device.
“The attacker continuously measures SSD contention by performing random reads from a large OPFS file,” the researchers explained. “SSD contention caused by user activity causes measurable latency differences for these read operations. By training a convolutional neural network (CNN) on these traces, the attacker can fingerprint user activity on the host system by classifying new traces using the trained model.”
The technique has its limitations. First, the OPFS file must be extremely large—likely a gigabyte or more. That requirement means that attacks at scale would inevitably be detected by many users. Additionally, the OPFS file must be stored on the same SSD the visitor is using. This isn’t usually a problem for tracking open websites, since the OPFS file is stored in the browser’s default location. In the event apps are using a separate SSD drive for apps, those apps couldn’t be detected by FROST.
One of the best ways to prevent FROST attacks is to close tabs as soon as they’re no longer needed. More savvy users can monitor the creation and size of OPFS files allocated by unknown websites. The researchers proposed ways for browser makers to shut down the side channel. One such method is to limit the maximum size of such files that are allowed. There are no indications FROST attacks have been performed in the wild.
The researchers performed the full Frost attack on an M2 Mac. On Linux, they showed that the underlying primitive (measuring SSD access latency traces from JavaScript) works, but didn’t run the full attack.
“However, since the performance of the primitive is similar between macOS and Linux, we expect similar performance for the full classification,” Hannes Weissteiner, one of the co-authors, wrote in an email. “In principle, it would be possible to train a model on any system activity that reliably generates SSD accesses.”
The researchers did not test Windows.
The paper linked above provides many more technical details. The research is scheduled to be presented at the
DIMVA conference
in July.
