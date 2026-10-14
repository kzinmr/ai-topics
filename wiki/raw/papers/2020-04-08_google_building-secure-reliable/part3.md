---
title: 'Part III: Building Secure and Reliable Systems'
source_url: https://raw.githubusercontent.com/google/building-secure-and-reliable-systems/2a2ae3e0d4dbd288f9862ed47194f5b1b1ed7c3c/raw/part3.html
license: CC-BY-4.0
license_url: https://creativecommons.org/licenses/by/4.0/
attribution: Heather Adkins, Betsy Beyer, Paul Blankinship, Piotr Lewandowski, Ana
  Oprea, Adam Stubblefield; Google; O’Reilly, 2020
source_revision: 2a2ae3e0d4dbd288f9862ed47194f5b1b1ed7c3c
original_html: original-source.zip!/raw/part3.html
original_sha256: 92bc0c492098844ebb2d681ae1210608a0a94d42c16ffdd7b466e6bba9909e37
created: '2026-10-14'
updated: '2026-10-14'
type: summary
tags:
- reliability
- security
- documentation
sources:
- https://raw.githubusercontent.com/google/building-secure-and-reliable-systems/2a2ae3e0d4dbd288f9862ed47194f5b1b1ed7c3c/raw/part3.html
ingested: '2026-10-14'
sha256: 2c09f651f955b8dc29fa4f9e3924fae8f7c68781ada07f23e359c440ab7e9743
content_kind: mechanical_text_extraction
transformation: HTML to plain text in Markdown container; source order retained; no
  translation or abridgment
---
Part III
Implementing Systems
Once you’ve analyzed and designed your systems, it’s time to implement your plans. In some cases, implementation might mean buying an off-the-shelf solution.
Chapter 11
provides one example of Google’s thought process in deciding to build a custom software solution.
Part III
of this book focuses on integrating security and reliability during the implementation phase of the software development lifecycle.
Chapter 12
reiterates the idea that frameworks will simplify your systems. Adding static analysis and fuzzing during testing, as described in
Chapter 13
, will harden the code.
Chapter 14
discusses why you should also invest in verifiable builds and further controls—safeguards around coding, building, and testing have limited effect if adversaries can bypass them by reaching your production environment.
Even if your entire software supply chain is resilient to security and reliability failures, you’ll inevitably need to analyze your systems when problems arise.
Chapter 15
discusses the careful balance you must strike between granting appropriate debugging access and the security requirements of storing and accessing logs.
