---
title: "Cross Compiling Docker Images"
url: "https://philiplaine.com/posts/cross-compiling-docker-images/"
fetched_at: 2026-04-30T07:01:48.814133+00:00
source: "philiplaine.com"
tags: [blog, raw]
---

# Cross Compiling Docker Images

Source: https://philiplaine.com/posts/cross-compiling-docker-images/

It has been an issue for a long time to run Docker images on multiple architectures. I remember the first time I got the idea to install Docker on my Raspberry Pi and I realized quickly that what I was trying to do would not work. The issue of course was that I was trying to use an AMD64 compiled Docker image on a ARM 32 bit CPU. Anyone who works with any lower level languages would call me an idiot for realizing this sooner than later. I would agree with them. Docker just seems to work like magic, running on most machines without any issue, like running Linux containers on Windows. One thing that has not been easy though is building Docker images on one type of CPU and running them on another.
Some of you might ask the question why even bother? Its a fair question as most consumer desktops and cloud VM instances run on AMD64 based processors. My first answer would be why not? We live in a world where a lot of languages have excellent support for cross compiling for different architectures, like
go
and
rust
. While the other are platform agnostic (for the most part) like python and javascript. So the barrier of entry to the multi architecture docker image seems to be very low right now. On a more serious note we are seeing a shift in the computing world that could take us away from the single dominating architecture with some competition in the form of
Apple
and
AWS
. I can’t predict if this will actually happen or even succeed, but what I can say is that it will be interesting.
You don’t have to convince me anymore! How do I get started?
The simplest answer is making sure you have downloaded
Docker CE 19.03
or later. This is because it includes
buildx
as part of the experimental CLI. Buildx is as “Docker CLI plugin for extended build capabilities with BuildKit” according to its own README. What it allows you to do is to easily build Docker images for multiple architectures/platforms at the same time, but this only gets you half way there as you will not be able to build ARM Docker images on your AMD64 machine. The easies way to solve this is with QEMU emulation to allow execution of multiple architectures on the same node.
Give me the commands already!
So if you want to build a ARM Docker image on your AMD64 machine, all you need to do is to enable QEMU emulation, create a builder instance, and build the image. Say you have the following main.go and Dockefile that you want to build for ARM on a AMD64 machine.
main.go
package
main
import
"fmt"
func
main
() {
fmt
.
Println
(
"hello world"
)
}
Dockerfile
FROM
golang:latest
WORKDIR
/app
COPY
main.go .
RUN
go build -o main .
CMD
[
"./main"
]
Then you need to run the following commands.
docker run --rm --privileged multiarch/qemu-user-static --reset -p yes
docker buildx create --use --name cross --platform
"linux/arm"
docker buildx build --platform linux/arm -t demo --load .
This will build a ARM Docker image and load it into your local Docker daemon. Say you have a CI pipeline and you want to build and push docker images for multiple architectures with minimal configuration. Well then you can push directly to your registry given that you are authenticated.
docker run --rm --privileged multiarch/qemu-user-static --reset -p yes
docker buildx create --use --name cross --platform
"linux/arm64,linux/arm,linux/amd64"
docker buildx build --platform
"linux/arm64,linux/arm,linux/amd64"
-t demo --push .
This will build and push a Docker image for ARM64, ARM, and AMD64. It will also push a manifest to the registry so that when you pull an image to your ARM node the correct image will be fetched. Note that 3 independent images will be pushed to the registry, but the experience should be seamless across machines with different architectures. If you want to read more about how Docker manifests
here is a good StackOverflow answer
to get you started, otherwise have fun building multi arch Docker images!
