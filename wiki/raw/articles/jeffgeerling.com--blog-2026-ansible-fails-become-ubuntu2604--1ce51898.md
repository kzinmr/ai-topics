---
title: "Ansible Fails waiting for privilege escalation on Ubuntu 26"
url: "https://www.jeffgeerling.com/blog/2026/ansible-fails-become-ubuntu2604/"
fetched_at: 2026-11-26T10:00:51.214938+00:00
source: "jeffgeerling.com"
tags: [blog, raw]
---

# Ansible Fails waiting for privilege escalation on Ubuntu 26

Source: https://www.jeffgeerling.com/blog/2026/ansible-fails-become-ubuntu2604/

I've slowly been moving my servers from Ubuntu 22 and 24 to 26 this year, and noticed my Ansible automation starts failing if I have password protection for
sudo
use:
$ ansible-playbook main.yml -K
BECOME password:
PLAY [Security] *******************************************************
TASK [Gathering Facts] ***********************************************************************
fatal: [my-server.local]: FAILED! =>
msg: 'Timeout (12s) waiting for privilege escalation prompt: '
Apparently Ubuntu's been rewriting system utilities in Rust, and the
sudo-rs
version that ships on Ubuntu 26.04 has some incompatiblities with the
sudo
I've used on servers for 20+ years.
It prints an extra string before the password prompt, which
sudo
doesn't do, and that can confuse automation tools like Ansible that wait for a specific prompt.
There's a thread in the Ansible project covering the issue:
validate sudo become plugin against sudo-rs
. The fix landed in Ansible Core 2.22.0, and is being backported into updates in 2.16, 2.18, 2.19, 2.20, and maybe also 2.21 (it's quite disruptive!). It looks like it also broke
pyinfra
, and their fix is in the latest release of 3.11.
I updated Ansible (
pip install -U ansible
) and now
-K
(
--ask-become-pass
) works again.
Another alternative is to use the traditional version of
sudo
that still ships with Ubuntu 26. For that, the easiest way is to set the
become_exe
inside your hosts file:
dell-precision.local ansible_become_exe=sudo.ws
Or you could even revert
sudo
systemwide on your Ubuntu host:
update-alternatives --config sudo
I'm not sure why Ubuntu sees the need to
rewrite common Linux utils in Rust
. I don't mind Rust, but these are foundational tools every Linux system relies on. This isn't a window manager, where experimentation is more acceptable
.
If other distros plan on moving to
sudo-rs
that's one thing, but if it's just Ubuntu, maybe I should hop back to Debian for everything, and not just my cloud servers.
