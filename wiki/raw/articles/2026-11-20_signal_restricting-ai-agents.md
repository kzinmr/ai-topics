---
title: "Signal is Serious About Protecting Your Privacy (restricting OS AI agents)"
source: https://signal.org/blog/protecting-your-privacy/
date: 2026-11-21
type: article
sha256: 96aa7a722be83983efe9cb843a73c522cd63d416316080a9ea104ccb29ef2cb5
---

> HN discussion: https://news.ycombinator.com/item?id=50572348 (556 pts)

Signal >> Blog >> Signal is Serious About Protecting Your Privacy 

 Signal is Serious About Protecting Your Privacy

 Meredith Whittaker 
 
 on 20 Nov 2026

 Privacy is our mission; it’s why we exist, and we do everything we can to protect it.

 This means that we are restricting the latest AI agents built into mobile operating systems from potentially capturing and storing your Signal data.

 We’ve already had to do this once with Windows. Last year, we used screenshot blocking to prevent Microsoft’s Recall AI from taking and storing screenshots of your Signal messages on Windows 11 operating systems by default. 1 We will now be taking similar measures to restrict agentic systems built into iOS 27 and on Android versions where we can detect an AI assistant attempting to read your Signal screen. 2 

 The problem is similar to Microsoft Recall on Windows: Google and Apple are integrating agentic capabilities like Gemini Intelligence with Google Gemini and Onscreen Awareness with Siri AI deep into their operating systems. This is a significant move. Google (Android), Apple (iOS/macOS), and Microsoft (Windows) produce the three major consumer operating systems (OS), which comprise the environment that third-party developers – like Signal – build their apps to function and operate within. To put it differently, these three operating systems are the oceans in which Signal, and other applications, must swim; they dictate the conditions of life for the application ecosystem. Right now, these agentic AI integrations are changing this environment in a way that’s making it increasingly hostile to privacy. This is an existential threat to Signal, and our ability to responsibly uphold our mission.

 In order to gain access to information about you, these OS AI agents “scan” the information that’s on your screen. In doing so, your Signal data is captured, then made available to these agentic systems in order to allow them to answer your questions and do your bidding.

 The net result is that these AI capabilities in the operating system are undermining Signal’s ability to independently guarantee privacy. For over a decade, this guarantee has been backed by our tried and trusted open source code base and our formally verified encryption protocol. These have been scrutinized by some of the best security experts and hackers across the world, and shown to be robust. Now, in service of AI agentic capabilities, your sensitive data is being captured, stored, and made accessible to whatever local database or remote server an OS-level AI agent is using at that moment. All of this is outside of Signal’s control once the data has been captured, and imperils the privacy of all the participants in a conversation.

 So, we are blocking such capture by preventing screenshots in the app on iOS 27 and when AI assistants attempt to capture screen data on Android. 2 

 People who want the ability to take screenshots can disable this protection within the Signal app’s settings. However, doing so will potentially expose your (and your contacts’) Signal content to these AI agents, and break our privacy guarantees. Our remedy is also incomplete – while we are doing everything we can, restricting screenshots does not address other more sneaky ways AI agents could potentially access application data, such as retrieving content already present on a user’s device via the filesystem.

 We want to be very clear: it is a serious problem that Signal – and application developers beyond – lack robust tools to prevent AI agents from undermining application-level privacy. Even where we are able to detect and block AI data access, Google, Apple, Microsoft, and others do not provide ways for developers to easily restrict such AI data access without making drastic compromises to the core user experience. This is also the reason we are currently unable to implement these protections on macOS. 3 

 We are also struggling with a significant lack of documentation about how these AI agents actually work. Over the past few months, we’ve spent considerable developer time and energy doing forensic investigations across Android and iOS in an attempt to learn what is actually happening when these AI systems access application data. Without better documentation and clear technical specifications, it will be increasingly difficult for Signal to provide robust privacy and security to the many millions of people who rely on us.

 We continue to call on the major consumer operating system companies – Apple, Google, and Microsoft – to provide simple technical tools and accurate documentation that give developers like Signal ways to prevent AI agents from accessing sensitive application data. In particular, we are calling on these companies to provide two common-sense remedies that can protect the privacy so many millions of people rely on:

 Developers should have an easy and well-documented way to opt their app out of AI data access and processing, including (but not limited to) screen reading, filesystem access, notifications, APIs, and other OS frameworks, all without undermining the core utility of an application.

 Operating system companies should create better documentation and technical specifications around how these AI agents function, particularly regarding data access and processing. Confidential computing approaches are not a complete solution, and do not address these core concerns. In particular, these approaches still leave the power to determine the extent of privacy guarantees (if any) in the hands of these providers.

 We also see a growing need for tools that can prevent third-party agents, like Meta’s Muse, from accessing application data using the deep permissions that users are encouraged to grant them during setup. In many cases these agents are leveraging accessibility settings that were meant to empower actual people to get the most out of their apps and services, not to act as a skeleton key that provides access to AI agents.

 In addition to taking these technical measures to block capture, we are engaging in conversations across the ecosystem to make the stakes clear. There is a lot of work to be done in the industry to improve the ways that AI agents operate in the operating system, and how and whether they capture and process private data. We are cautiously optimistic that some major OS providers, like Google and Apple, are engaging with us on how these systems should better interface with privacy-sensitive apps like Signal. We hope to have more to share on this topic soon, and that these companies recognize the danger to the ecosystem and work with us and others to create standardized approaches that meaningfully protect privacy across the industry.

 Finally, we want to acknowledge that we are not the only ones recognizing these perils, and we are grateful to our allies for pushing for similar changes . We all need to recognize that the current integration of AI agents into the operating system, without these common-sense remedies, represents an existential threat to privacy at the application layer, and the ability of independent developers like Signal to protect your sensitive data. Signal is the canary in the coal mine, but this affects the entire ecosystem and should galvanize anyone who cares about these fundamental rights.

 Signal Technology Foundation is the nonprofit home of the Signal app, which is trusted by millions around the world. We protect free expression and enable secure global communication through open source privacy technology. Signal Technology Foundation is a US 501(c)(3) tax-exempt organization. 

 Microsoft Recall captures your screen every few seconds, extracts text from screenshots via optical character recognition, then populates a searchable on-device database with this personal data in order to allow the AI system to query it – potentially exposing and retaining your Signal data indefinitely, including disappearing messages.  ↩ 

 There are multiple versions of Android beyond the Google-provided distributions on Pixel devices. For many vendors, we don’t have a reliable way to detect when a screenshot was attempted if screenshots are already disabled. Rather than choose a poor user experience (where screenshots simply stop working, confusing users), we decided to instead focus on detecting when an AI assistant attempts to access the screen. We automatically enable the “Screen security” setting in Signal Android when this type of access is detected.  ↩   ↩ 2 

 Careful readers will note that in addition to not being able to cover all Android devices, we are also not blocking Siri AI on macOS. This is because we cannot reliably block screenshots on macOS. Faced with a lack of clearly documented APIs that allow us to implement screenshot protection, we do not have the tools available that let us do the job. While protections against continuous screen capture exist on macOS, we cannot apply them to screenshots (which is how most agentic systems access data from applications like Signal). Trying to implement screenshot blocking on macOS has revealed to us a minefield of bewildering decisions that place user privacy at risk, including APIs that have been deprecated in favor of screen-protection solutions that only work for streaming media and other DRM-protected content. This is something we hope Apple remedies urgently. For now, the only recommendation we have for macOS 27 users is to add Signal to the Excluded Apps section in System Settings > Siri to protect message content from proactive access by Siri AI.  ↩ 

 Tweet 
 Facebook 

 Don't have Signal? Give it a try!
