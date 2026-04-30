---
title: "Getting Forked by Microsoft"
url: "https://philiplaine.com/posts/getting-forked-by-microsoft/"
fetched_at: 2026-04-30T07:01:48.676198+00:00
source: "philiplaine.com"
tags: [blog, raw]
---

# Getting Forked by Microsoft

Source: https://philiplaine.com/posts/getting-forked-by-microsoft/

Three years ago, I was part of a team responsible for developing and maintaining Kubernetes clusters for end user customers. A main source for downtime in customer environments occurred when image registries went down. The traditional way to solve this problem is to set up a stateful mirror, however we had to work within customer budget and time constraints which did not allow it. During a Black Friday, we started getting hit with a ton of traffic while GitHub container registries were down. This limited our ability to scale up the cluster as we depended on critical images from that registry. After this incident, I started thinking about a better way to avoid these scalability issues. A solution that did not need a stateful component and required minimal operational oversight. This is where the idea for
Spegel
came from.
As a sole maintainer of an open source project, I was enthused when Microsoft reached out to set up a meeting to talk about Spegel. The meeting went well, and I felt there was going to be a path forward ripe with cooperation and hopefully a place where I could onboard new maintainers. I continued discussions with one of the Microsoft engineers, helping them get Spegel running and answering any architecture questions they had. At the time I was positive as I saw it as a possibility for Micorosft to contribute back changes based on their learnings. As time went on, silence ensued, and I assumed work priorities had changed.
It was not until KubeCon Paris where I attended a talk that piqued my interest. The talk was about strategies to speed up image distribution where one strategy discussed was P2P sharing. The topics in the abstract sounded similar to Spegel so I was excited to hear other’s ideas about the problem. During the talk, I was enthralled seeing Spegel, my own project, be discussed as a P2P image sharing solution. When
Peerd
, a peer to peer distributor of container content in Kubernetes clusters made by Microsoft, was mentioned I quickly researched it. At the bottom of the README there was a thank you to myself and Spegel. This acknowledgement made it look like they had taken some inspiration from my project and gone ahead and developed a version of their own.
Source: Peerd
While looking into Peerd, my enthusiasm for understanding different approaches in this problem space quickly diminished. I saw function signatures and comments that looked very familiar, as if I had written them myself. Digging deeper I found test cases referencing Spegel and my previous employer, test cases that have been taken directly from my project. References that are still present to this day. The project is a forked version of Spegel, maintained by Microsoft, but under Microsoft’s MIT license.
Source: Peerd
Source: Peerd
Spegel was published with an MIT license. Software released under an MIT license allows for forking and modifications, without any requirement to contribute these changes back. I default to using the MIT license as it is simple and permissive. The license does not allow removing the original license and purport that the code was created by someone else. It looks as if large parts of the project were copied directly from Spegel without any mention of the original source. I have included a short snippet comparing the code which adds the mirror configuration where even the function comments are the same.
Source: Peerd
Source: Spegel
A negative impact from the creation of Peerd is that it has created confusion among new users. I am frequently asked about the differences between Spegel and Peerd. As a maintainer, it is my duty to come across as unbiased and factual as possible, but this tumultuous history makes it challenging. Microsoft carries a large brand recognition, so it has been difficult for Spegel to try and take up space next to such a behemoth.
As an open source maintainer I have dedicated ample time to community requests, bug fixes, and security fixes. In my conversation with Microsoft I was open to collaboration to continue building out a tool to benefit the open source community. Over the years I have contributed to a multitude of open source projects and created a few of my own. Spegel was the first project I created from the ground up that got some traction and seemed to be appreciated by the community. Seeing my project being forked by Microsoft made me feel like I was no longer useful. For a while I questioned if it was even worth continuing working on Spegel.
Luckily, I persisted. Spegel still continues strong with over 1.7k stars and 14.4 million pulls since its first release over two years ago. However, I am not the first and unfortunately not the last person to come across this David versus Goliath-esque experience. How can sole maintainers work with multi-billion corporations without being taken advantage of? With the changes of Hashicorp licensing having a rippling effect through the open source community, along with the strong decline in investment in open source as a whole, how does the community prevail? As an effort to fund the work on Spegel I have enabled GitHub sponsors. This experience has also made me consider changing the license of Spegel, as it seems to be the only stone I can throw.
