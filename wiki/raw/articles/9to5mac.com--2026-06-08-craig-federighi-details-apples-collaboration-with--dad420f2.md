---
title: "Craig Federighi details Apple’s collaboration with Google for Siri AI in iOS 27"
url: "https://9to5mac.com/2026/06/08/craig-federighi-details-apples-collaboration-with-google-for-siri-ai-in-ios-27/"
fetched_at: 2026-06-11T07:00:57.312082+00:00
source: "daringfireball.net"
tags: [blog, raw]
---

# Craig Federighi details Apple’s collaboration with Google for Siri AI in iOS 27

Source: https://9to5mac.com/2026/06/08/craig-federighi-details-apples-collaboration-with-google-for-siri-ai-in-ios-27/

Apple’s Siri team, led by Craig Federighi, held a post-WWDC keynote tech talk with members of the press this afternoon to talk through iOS 27 and the new Siri AI.
During the talk, Federighi shared more details about Apple’s collaboration with Google.
Federighi was joined by Amar Subramanya (vice president of AI), Mike Rockwell (Siri lead), and Sebastien Marineau-Mes (software VP).
On the Google collaboration, Federighi explained:
Of course, we don’t have the Gemini app as our app. In fact, none of that client code is part of how we run on iOS. For these models, we use none of the models that Google deploys to their customers, nor do we use the infrastructure and means by which they deploy models to their customers. And then, when it comes to the knowledge base, we of course don’t use Google Search or anything like that as the foundation of our system. So I hope that’s clear. The amount of the Google Assistant we use is none.
So let’s talk about what we do use, or how our system is built.
It starts, of course, with our Assistant experience. And as you saw earlier today, this Assistant experience is deeply integrated into the system, into iOS, into iPadOS, into macOS. You saw on the iPhone how the assistant emerges, I think really beautifully, in Liquid Glass out of the Dynamic Island, how you can summon it from the side button or by speaking to Siri by name. But more than that, it’s integrated across all sorts of places in the system. So whether you’re writing with Writing Tools, clicking with the context menu, all of this is deeply integrated into the system experience.
Now, plugged into that is the Siri app. The Siri app is a great way to get back to a conversation that you previously started, to either look at what you’ve previously been doing, maybe extend that conversation, or start a new one. But this app isn’t just reaching out to some model in the cloud. It’s built on top of powerful system software in Apple Intelligence.
This includes the System Orchestrator, which is key to the privacy architecture of our entire system. It’s what coordinates requests against things like the App Toolbox that provides access to actions within your apps, the Spotlight Semantic Index to access personal content to help fulfill your request, and even things like on-screen context to understand what you might be looking at at the moment you’re making a request.
This, in turn, is built on a set of powerful on-device models. These handle everything from understanding speech to synthesizing the voice that speaks back to you, to understanding visually the environment and the on-screen context, understanding if there’s something relevant there, understanding text that might be on the screen, as well as a whole set of other models.
And for some requests, models are capable of processing your Siri requests entirely locally on the device. But sometimes the System Orchestrator realizes that it’s a more sophisticated question, and then it wants to draw on greater intelligence. It does that by contacting our models running in Private Cloud Compute.
The goal of Private Cloud Compute is to extend the same privacy promise of the iPhone up into the cloud, such that your requests are completely private to you. They’re never stored, they’re never accessible to anyone, including Apple, they’re only processed as part of the request, and nothing can access them. All of those properties are not only built architecturally deep into the system, but are also something that third-party researchers can continuously verify.
Now, in that deployment model, we have a family—our third generation—of Apple Foundation Models, from our AFM Cloud and AFM Cloud Pro models to our AFM Fusion model and image model. These are the models that are the product of our collaboration with Google, and you’ll hear more about that when we continue. But those are architected to run on our deployment architecture. These are models designed specifically for our Apple Intelligence experiences. They’re what powered everything you saw in the keynote presentation earlier today.
Finally, when you make a request involving current events or other elements of world knowledge, those responses are grounded by accessing Apple’s World Knowledge Service. This is something that we’ve built over many years and provides a great source of information to satisfy your request.
So this system is what supports the full range of Apple Intelligence experiences that you saw earlier. I hope that grounds our discussion as well. And what we’d like to do now is bring out members of the leadership team who helped work on all of this.
Subramanya elaborated:
We’re super excited about our 3rd generation of Apple Foundation Models, or AFM, in partnership with Google. We’ve built a family of models spanning on-device to the cloud. Now, before I walk through each of the models in the family, the headline, I would say, for this generation is every model is a significantly both in quality and capability compared to our previous generation.
Just walking through each of the models, we’d start with our on-device models. So 1st off, we have AFM Core. This is the next generation of our on-device model that we’re shipping on devices today. It follows the dense architecture.
And then next up, we have AFM Core Advanced.
This is unlike any on-device model we’ve run before. It uses a sparse architecture, it’s natively multimodal. And as a result of that, huge leap in the capabilities of this model, enabling some of the features you heard about this morning, like invitation and expressive voices, all working completely on device as a result of this model.
Moving on to our server models, all of which are served out of our Private Cloud Compute. First off, we have AFM Cloud. This is our server work hard model. It’s basically optimized for latency and serving cost.
And then next up, we have AFM Cloud Image. This is our next generation of image generation and editing model, and, you know, enables a number of amazing experiences, including things like spatial reframing, that you also heard about this morning.
And all of these four models that we just talked about, FM, Core, Core Advanced Cloud, and Cloud Image, all of these are custom builds for Apple Silicon, trained using proprietary data, and refined using outwards from Gemini frontier models.
Now, finally, for some of the most demanding tasks, like agentic tool use, complex reasoning, we have AFM Cloud Pro. This is our most capable model with quality similar to Gemini frontier models.
And to bring this model to production, we work with both Google and Nvidia to extend our Private Cloud Compute infrastructure to NVIDIA GPUs in Google’s cloud, while maintaining Apple’s unmatched privacy guarantees, right?
So, across all of this family of models, our goal is to match every user request to the model which provides the best response at the lowest latency. And so together we’re super excited about this next generation of models and the amazing features it enables us to build on top of them, including the new Siri AI experience and all of the amazing intelligent experiences across the OS.
More to come …
Chance’s favorites:
Follow Chance
:
Threads
,
Bluesky
,
Instagram
, and
Mastodon
.
FTC: We use income earning auto affiliate links.
More.
