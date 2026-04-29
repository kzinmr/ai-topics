---
title: "Time Machine inside a FreeBSD jail"
url: "https://it-notes.dragas.net/2026/01/28/time-machine-freebsd-jail/"
fetched_at: 2026-04-29T07:02:10.476305+00:00
source: "it-notes.dragas.net"
tags: [blog, raw]
---

# Time Machine inside a FreeBSD jail

Source: https://it-notes.dragas.net/2026/01/28/time-machine-freebsd-jail/

Many of my clients do not use Microsoft systems on their desktops; they use Linux-based systems or, in some cases, FreeBSD. Many use Apple systems - macOS - and are generally satisfied with them. While I wash my hands of it when it comes to Microsoft systems (telling them they have to manage their desktops autonomously), I am often able to lend a hand with macOS. And one of the main requests they make is to manage the backups of their individual workstations.
macOS, thanks to its Unix base, offers good native tools. Time Machine is transparent and effective, allowing a certain freedom of management. APFS, Apple's current file system, supports snapshots, so the backup will be effectively made on a snapshot. It also supports multiple receiving devices, so you can even have a certain redundancy of the backup itself.
Having many FreeBSD servers, I am often asked to use their resources and storage. To build, in practice, a Time Machine inside one of the servers. And it is a simple and practical operation, quick and "painless". There are many guides, including the excellent one by
Benedict Reuschling
from which I took inspiration for this one, and I will describe the steps I usually follow to set it all up in just a few minutes.
I usually use
BastilleBSD
to manage my jails, so the first step is to create a new jail dedicated to the purpose. Here you have to decide on the approach: I suggest using a VNET jail or an "inherit" jail - meaning one that attaches to the host's network stack. On one hand, the inherit approach is less secure but, as often happens, it depends on the complexity of the situation. If, for example, we are using a Raspberry PI dedicated to the purpose, there is no reason to complicate things with bridges, etc., but we can attach directly to the network card with a creation command like:
bastille create tmjail 15.0-RELEASE inherit igb0
Where
igb0
is the network interface we want to attach to.
In case we want to attach to the interface but in the form of a bridge, we should use this syntax:
bastille create -V tmjail 15.0-RELEASE 192.168.0.42/24 igb0
Or, if our server already has a bridge (in this case it's
bridge0
, but yours might be named differently):
bastille create -B tmjail 15.0-RELEASE 192.168.0.42/24 bridge0
At this point, you can choose: do we want to keep the backups inside the jail or in a separate dataset - which can even be on another pool? In some cases, this can be extremely useful: often I have jails running on fast disks (SSD or NVMe) but abundant storage on slower devices. In this example, therefore, I will create an external dataset for the backups (directly from the host) and mount it in the jail. You could also delegate the entire management of the dataset to the jail, which is a different approach.
Let's create a space of 600 GB - already reserved - on the chosen pool. 600 GB is a small space, but it's ok for an example:
zfs create -o quota=600G -o reservation=600G bigpool/tmdata
We can also create separate datasets inside for each user and assign a specific space:
zfs create -o refquota=500g -o refreservation=500g bigpool/tmdata/stefano
We can enter the jail and install what we need, remembering also to create the "mountpoint" for the dataset we just created:
bastille console tmjail 

pkg install -y samba419
mkdir /tmdata
Exit the jail and instruct Bastille to mount the dataset inside the jail every time it is launched:
exit
bastille mount tmjail /bigpool/tmdata /tmdata nullfs rw 0 0
Let's go back into the jail and start with the actual configuration. First, for each Time Machine user, we will create a system user. In my example, I will create the user "stefano", giving him
/var/empty
as the home directory - this will give an error since we created a Bastille thin jail, but it's not a problem. It happens because in a thin jail some system paths are read-only or not manageable as they are on a full base system, but the user is only needed for ownership and Samba login.
root@tmjail:~ # adduser
Username: stefano
Full name: Stefano
Uid (Leave empty for default):
Login group [stefano]:
Login group is stefano. Invite stefano into other groups? []:
Login class [default]:
Shell (sh csh tcsh nologin) [sh]: nologin
Home directory [/home/stefano]: /var/empty
Home directory permissions (Leave empty for default):
Use password-based authentication? [yes]: no
Lock out the account after creation? [no]:
Username    : stefano
Password    : <disabled>
Full Name   : Stefano
Uid         : 1001
Class       :
Groups      : stefano
Home        : /var/empty
Home Mode   :
Shell       : /usr/sbin/nologin
Locked      : no
OK? (yes/no) [yes]: yes
pw: chmod(var/empty): Operation not permitted
pw: chown(var/empty): Operation not permitted
adduser: INFO: Successfully added (stefano) to the user database.
Add another user? (yes/no) [no]: no
Goodbye!
Give the correct permissions to the user:
# If you've not created specific datasets for the users, you'd better create their home directories now
mkdir /tmdata/stefano
chown -R stefano /tmdata/stefano/
Now we configure Samba for Time Machine. The file to create/modify is
/usr/local/etc/smb4.conf
:
[global]
workgroup = WORKGROUP
security = user
passdb backend = tdbsam
fruit:aapl = yes
fruit:model = MacSamba
fruit:advertise_fullsync = true
fruit:metadata = stream
fruit:veto_appledouble = no
fruit:nfs_aces = no
fruit:wipe_intentionally_left_blank_rfork = yes
fruit:delete_empty_adfiles = yes

[TimeMachine]
path = /tmdata/%U
valid users = %U
browseable = yes
writeable = yes
vfs objects = catia fruit streams_xattr zfsacl
fruit:time machine = yes
create mask = 0600
directory mask = 0700
We have set up Time Machine to support all the necessary features of macOS and to show itself as "Time Machine". Having set
path = /tmdata/%U
, each user will only see their own path.
At this point, we create the Samba user (meaning the one we will have to type on macOS when we configure the Time Machine):
smbpasswd -a stefano
The Time Machine is seen by macOS because it announces itself via mDNS on the network. This type of service is performed by Avahi, which we are now going to configure. Although not strictly necessary (we can always find the Time Machine by connecting directly to its IP and macOS will remember everything), seeing it announced will help other non-expert users and ourselves when we have to configure another Mac in the future.
Recent Samba releases won't need any specific avahi configuration, so we can skip this step.
We are now ready to enable everything.
service dbus enable
service dbus start
service avahi-daemon enable
service avahi-daemon start
service samba_server enable
service samba_server start
Et voilà. If everything went according to plan, the Time Machine will announce itself on your network (if you have different networks, remember to configure the mDNS proxy on your router) and you will be able to log in (with the smb user you created) and start your first backup.
I suggest encrypting the backups for maximum security and observing, from time to time, your Mac as it silently makes its backups to your trusted FreeBSD server.
