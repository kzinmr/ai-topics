---
title: "HomeAssistant - shrink a HAOS qcow2 filesystem"
url: "https://shkspr.mobi/blog/2026/11/homeassistant-shrink-a-haos-qcow2-filesystem/"
fetched_at: 2026-11-18T10:01:22.887171+00:00
source: "shkspr.mobi"
tags: [blog, raw]
---

# HomeAssistant - shrink a HAOS qcow2 filesystem

Source: https://shkspr.mobi/blog/2026/11/homeassistant-shrink-a-haos-qcow2-filesystem/

Mostly notes to myself, I hope they're helpful to you too!
My HomeAssistant OS (HAOS) was originally thinly provisioned with a 30GB virtual disk stored in a qcow2 file. In theory, the file should only take up as much space as the virtual filesystem. In reality, it grows to accommodate the maximum size allowed.
My HAOS was showing only 10GB used:
But running
ls -lh
showed 32GB was allocated. To see the
actual
space on disk, I ran
du -h haos.qcow2
which showed 28GB.
As it is 2026, I can't afford to simply buy a few more TB of SSD, so here's how to manually shrink the file so it only takes up the space it needs.
Within HomeAssistant's web interface, completely shut down.
Settings → ⋮ → Restart Home Assistant → More options → Shut Down System
Wait a few minutes for everything to finish shutting down.
Within your host Operating System, backup your existing file!
sudo cp haos.qcow2 haos.qcow2.bak
Check the size of the disk:
sudo qemu-img info haos.qcow2
Shrink (sparsify) the disk.
sudo virt-sparsify --in-place haos.qcow2
This may take a few moments.
Check the size of the disk to make sure it has shrunk:
sudo qemu-img info haos.qcow2
Once that has finished, you can start the virtual machine again.
virsh list --all
to find the name of the VM.
virsh start haos
Wait a few minutes and your HomeAssistant should come back to life. If all is well, you can delete the backup.
There doesn't seem to be an automated way to do this. If you do know a way to make this easier - please leave a comment in the box.
