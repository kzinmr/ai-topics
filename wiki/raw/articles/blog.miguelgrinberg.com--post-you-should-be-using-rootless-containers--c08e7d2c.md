---
title: "You Should be Using Rootless Containers"
url: "https://blog.miguelgrinberg.com/post/you-should-be-using-rootless-containers"
fetched_at: 2026-09-04T10:00:44.690640+00:00
source: "miguelgrinberg.com"
tags: [blog, raw]
---

# You Should be Using Rootless Containers

Source: https://blog.miguelgrinberg.com/post/you-should-be-using-rootless-containers

The other day a serious vulnerability was disclosed in one of the newer Linux distributions (the one led by the racist, so it isn't getting a mention here). The issue was interesting because it was caused by a non-standard Docker configuration that their installer applied by default, without alerting users that this configuration was creating a security risk. The end result was that any process running on these systems had the ability to elevate itself to root, without password,
sudo
or any prompts to the user.
While this incident did not affect me, it served as a reminder that it is difficult to set up Docker in a way that is secure. If you are interested in understanding what the issues with Docker are and what can be done to address them, then you are in the right place.
The problem with Docker
The security problems with Docker stem from the choice of using a client-server architecture that was made way back in the beginning. On a standard installation, the Docker daemon runs in the background under the
root
user, providing all the functionality through an API. Clients such as
docker-cli
send requests to this API through the Docker socket, which the server listens on.
Because the Docker daemon runs as the
root
user, an attacker that gains access to it can execute code with root permissions. You may think that this is just theoretical, or maybe an unlikely, highly complex and obscure vulnerability that only genius hackers can exploit. Well, think again.
Here is a simple example in which I show how I can obtain root access on my Ubuntu 26.04 system just using the
docker
command and without using a password:
# as a regular user, the following command fails
$ ls /etc/sudoers.d/
ls: cannot open directory '/etc/sudoers.d/': Permission denied

# but I can ask Docker to run this command and it works, no questions asked! 
$ docker run -v /:/host alpine:latest ls /host/etc/sudoers.d/
90-cloud-init-users
README
In case it isn't clear how this works, the
docker run
command above starts a standard Alpine Linux container, mounting the entire file system of the host under the
/host
path. Because the container is running under the root account through the Docker daemon, it has access to all files and thus can bypass any restrictions of the user that issued the
docker run
command. Note that there was no need to authenticate or enter any passwords, the command just worked. A slightly more elaborate malicious script could use the same technique to modify or exfiltrate system files, install cron jobs or other nasty things, all without the user noticing.
Now I don't want to lie to you. The above root escalation attack is not going to work on every Docker install out there. If you do a basic install of Docker, then "root escalation" does not really have much of a point, since under a default install the
docker
command is accessible only to the
root
user. If you wanted to use Docker from your regular user account you would be forced to run
sudo docker
and that requires authentication.
These types of attacks are possible because users often relax access permissions to the Docker socket in the name of convenience. A very common non-standard configuration change that people make is to add themselves to the
docker
group on their machines, which allows them to run the
docker
command without
sudo
. That is what I did for the demonstration I shared above, and also what the Linux distribution I referenced at the start did without notifying their users.
The truth is that using Docker only as the root user is incredibly inconvenient, so much that the details on how to reconfigure it to work without
sudo
are
documented
in the official Docker website, in spite of being a security nightmare. My guess is that if you use Docker on Linux you have made this change, and thus, your system is vulnerable to root escalation attacks.
What about Docker on macOS and Windows?
Everything I discussed above relates to running Docker on Linux. In fact, Docker only runs on Linux, so products such as Docker Desktop, which support the other operating systems, have to create a Linux virtual machine (VM) as a trick to allow Docker to run there.
I'm honestly not very well versed on how these solutions work, but I would imagine standard virtualization tools such as QEMU, Hyper-V, or similar are used to host the Linux VM that is home to Docker. This creates an additional layer of separation from the physical host, so my impression is that the risks to the host are considerably reduced when running Docker on these operating systems. If anyone with experience on these tools would like to chime in with more details, feel free to use the comments section at the bottom of this article.
I think WSL, the native Linux support that comes with Windows, needs to be treated as a special case. WSL has a much tighter integration with the OS, with the Linux kernel running directly in the host. So there are potentially similar risks to those that exist on a regular Linux system. Once again, if you have things to share about this, I'd love to hear them.
The alternative: rootless containers
As mentioned above, Docker made the decision to go with a client-server architecture, and this largely led to the traditional root-owned daemon. But there are alternative ways to run containers that do not rely on the
root
user. Of the many alternative platforms out there, I want to mention two:
Docker in rootless mode
: a variation in the installation process of the standard Docker, where the daemon runs as a user-level service
Podman
: a daemonless container platform
I find the rootless Docker solution a bit hacky. The official
installation instructions
ask you to do a regular install, then manually disable the Docker daemon, and finally run a script they provide that creates a user-level daemon replacement for the current user.
Now for Podman, you just install it and you're done, with the added benefit that no background services need to run on the system. If you get used to typing
podman
instead of
docker
(or add
alias docker=podman
to your shell configuration), chances are the vast majority of the workflows will work the same, but all your containers will run under your own user, with no viable path for a root escalation. And you will not be running a daemon (unless you need one, see below.)
The catch with Podman
What's not to like about Podman, right? Seems to be perfect, as it addresses the security problems that have plagued Docker since the early days.
Well, note how above I carefully said that the "vast majority" of workflows will work the same with Podman as with Docker. The truth is that not all workflows can be transparently switched over. So let's review some of the issues I have experienced when transitioning.
Docker defaults to using its own Docker Hub registry when pulling an image, but Podman sometimes does not, depending on how it was configured. Take the following command:
docker pull postgres
This may will fail under Podman because it may not know where to pull the image from. While it is possible to configure Docker Hub (or any other registries that you use) as a default registry, I find that when using Podman it is best to get used to name all container images with their fully qualified addresses:
podman pull docker.io/library/postgres
There are also some significant differences in Podman due to its daemonless nature.
Not having a daemon makes Podman unable to restart containers after a reboot, so using Podman on servers that need to be up 24/7 requires a bit of additional work. Podman includes an integration with
systemd
under the
podman quadlet
group of commands that can install containers as individual services.
Also in the same vein, if there is no daemon, how do applications launch or interact with containers through an API? This is actually a very popular way to use Docker.
For this, Podman provides an optional API service that you can launch via the
podman system service
command. The command accepts the socket address that you want to use and an optional time for the service to be active. Once started, the service runs just for the user that started it, exposing an API that is compatible with the one from Docker. For servers, there is also a
systemd
integration to have this user-level service running at all times in the background.
Conclusion
I hope you now have a more clear view of how rootless containers would make your system more secure. Or maybe this helped you decide that rootless containers aren't for you, and that the risks of root escalation with Docker are something you can live with, which is not what I would recommend, but I guess it is fine if you understand what those risks are.
As for myself, I mostly use Podman these days. I also make use of
Podman Compose
quite a bit, the clone of Docker Compose. Even though on occasion I start the Podman API, most of the time I don't need it, so I do everything via the
podman
command without running an API service. I do use Docker sometimes, but I only go for it when I need to do some quick test on a disposable and isolated VM, where security isn't a big concern.
Thank you for visiting my blog! If you enjoyed this article, please consider supporting my work and keeping me caffeinated with a small one-time donation through
Buy me a coffee
. Thanks!
