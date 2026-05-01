---
title: "Mitchell Hashimoto"
url: "https://mitchellh.com/writing/packer"
fetched_at: 2026-05-01T07:02:03.738585+00:00
source: "mitchellh.com"
tags: [blog, raw]
---

# Mitchell Hashimoto

Source: https://mitchellh.com/writing/packer

For the past two months, I've been heads down working on something new. There is still a lot of work left, but I believe it's time to show everyone what I've been up to. Today, I'm announcing
Packer
: an open source tool for creating machine images for multiple platforms.
Packer is an
open source
tool for creating machine images, such as AMIs, VirtualBox images, Vagrant boxes, etc. Packer uses a single portable input format -- a template -- to generate the images for multiple platforms in parallel, so you can create identical AMIs, VMware machines, etc. all at once. This unlocks a lot of
interesting use cases
.
Machine images are a powerful concept, but the existing tooling around them hasn't caught up to the agile workflow that modern cloud infrastructures enable. Packer makes machine image creation automated, fast, and integrates with all the industry standard DevOps tools. Here are some examples of what Packer can be used for:
Automatically create
AMIs
(or any other machine image) for your production usage, perhaps as part of a continuous delivery pipeline.
Concurrently create
AMIs
for production and
Vagrant boxes
for development which are nearly identical.
Build
software appliances
in an automated, repeatable way, perhaps for multiple platforms. Getting software demos or ready-to-go images in the hands of anyone on any platform has never been easier.
And
so much more!
Packer is a general purpose image building tool. The opportunities to build things around it are endless. I'm excited to see what people will use Packer for.
With the announcement today, I'm inviting anyone and everyone to
play with Packer
and to
get involved with the open source project
. There are so many ways to get involved. The most fun might be adding more builders, the components that build images for specific platforms. There are already a handful of committers on the project and I'm looking to add more.
As a reminder: I released version
0.1
of Packer today. It is the first release and a
lot
of improvements will be coming quickly in the future, so please keep that in mind when offering feedback or judging the project. Remember, when I released version 0.1 of Vagrant, it only worked on Mac, only worked with VirtualBox, only ran Ubuntu machines, and only worked with serverless Chef. However, as the Vagrant community grew so did its capabilities, and now all those limitations have been removed. If there is a feature you'd love to see in Packer feel free to
hack on it
or
ask the mailing list
.
