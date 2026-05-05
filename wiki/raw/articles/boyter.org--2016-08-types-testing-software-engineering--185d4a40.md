---
title: "Types of Testing in Software Engineering"
url: "https://boyter.org/2016/08/types-testing-software-engineering/"
fetched_at: 2026-05-05T07:02:00.791731+00:00
source: "Ben Boyter"
tags: [blog, raw]
---

# Types of Testing in Software Engineering

Source: https://boyter.org/2016/08/types-testing-software-engineering/

There are many different types of testing which exist in software engineering. They should not be confused with the test levels, unit testing, integration testing, component interface testing, and system testing. However the different test levels may be used by each type as a way of checking for software quality.
The following are all different types of tests in software engineering.
A/B
A/B testing is testing the comparison of two outputs where a single unit has changed. It is commonly used when trying to increase conversion rates for online websites. A real genius in this space is
Patrick McKenzie
and a few very worthwhile articles to read about it are
How Stripe and AB Made me A Small Fortune
and
AB Testing
Acceptance
Acceptance tests usually refer to tests performed by the customer. Also known as user acceptance testing or UAT. Smoke tests are considered an acceptance test.
Accessibility
Accessibility tests are concerned with checking that the software is able to be used by those with vision, hearing or other impediments.
Alpha
Alpha testing consists of operational testing by potential users or an independent test team before the software is feature complete. It usually consists of an internal acceptance test before the software is released into beta testing.
Beta
Beta testing follows alpha testing and is form of external user acceptance testing. Beta software is usually feature complete but with unknown bugs.
Concurrent
Concurrent tests attempt to simulate the software in use under normal activity. The idea is to discover defects that occur in this situation that are unlikely to occur in other more granular tests.
Conformance
Conformance testing verifies that software conforms to specified standards. An example would checking a compiler or interpreter to see if it will work as expect against the language standards.
Compatibility
Checks that software is compatible with other software on a system. Examples would be checking the Windows version, Java runtime version or that other software to be interfaced with have the appropriate API hooks.
Destructive
Destructive tests attempt to cause the software to fail. The idea being to check that software continues to work even with given unexpected conditions. Usually done through fuzzy testing and deliberately breaking subsystems such as the disk while the software is under test.
Development
Development testing is testing done by both the developer and tests during the development of the software. The idea is to prevent bugs during the development process and increase the quality of the software. Methodologies to do so include peer reviews, unit tests, code coverage and others.
Functional
Functional tests generally consist of stories focused around the users ability to perform actions or use cases checking if functionality works. An example would be “can the user save the document with changes”.
Installation
Ensures that software is installed correctly and works as expected on a new piece of hardware or system. Commonly seen after software has been installed as a post check.
Internationalisation
Internationalisation tests check that localization for other countries and cultures in the software is correct and inoffensive. Checks can include checking currency conversions, word range checks, font checks, timezone checks and the like.
Non functional
Non functional tests test the parts of the software that are not covered by functional tests. These include things such as security or scalability which generally determine the quality of the product.
Performance / Load / Stress
Performance load or stress testing is used to see how a system performance under certain high or low workload conditions. The idea is to see how the system performs under these conditions and can be used to measure scalability and resource usage.
Regression
Regression tests are an extension of sanity checks which aim to ensure that previous defects which had a test written do not re-occur in a given software product.
Realtime
Realtime tests are to check systems which have specific timing constraints. For example trading systems or heart monitors. In these case real time tests are used.
Smoke / Sanity
Smoke testing ensures that the software works for most of the functionality and can be considered a verification or acceptance test. Sanity testing determines if further testing is reasonable having checked a small set of functionality for flaws.
Security
Security testing concerned with testing that software protects against unauthorised access to confidential data.
Usability
Usability tests are manual tests used to check that the user interface if any is understandable.
