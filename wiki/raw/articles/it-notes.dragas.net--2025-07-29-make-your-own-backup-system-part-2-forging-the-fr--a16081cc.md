---
title: "Make Your Own Backup System - Part 2: Forging the FreeBSD Backup Stronghold"
url: "https://it-notes.dragas.net/2025/07/29/make-your-own-backup-system-part-2-forging-the-freebsd-backup-stronghold/"
fetched_at: 2026-04-29T07:02:11.000260+00:00
source: "it-notes.dragas.net"
tags: [blog, raw]
---

# Make Your Own Backup System - Part 2: Forging the FreeBSD Backup Stronghold

Source: https://it-notes.dragas.net/2025/07/29/make-your-own-backup-system-part-2-forging-the-freebsd-backup-stronghold/

With the
primary backup strategies and methodologies introduced
, we've reached the point where we can get specific: the Backup Server configuration.
When choosing the type of backup server to use, I tend to favor specific setups: either I trust a professional backup service provider (like Colin Percival's
Tarsnap
), or I want full control over the disks where the backups will be hosted. In both cases, for the past twenty years, my operating system of choice for backup servers has been FreeBSD. With a few rare exceptions for clients with special requests, it covers all my needs. When I require Linux-based solutions, such as the
Proxmox Backup Server
, I create a VM and manage it within.
I typically use both IPv4 and IPv6. For IPv4, I "play" with NAT and port forwarding. For IPv6, I tend to assign a public IPv6 address to each jail or VM, which is then filtered by the physical server's firewall. Unfortunately, every provider, server, and setup has a different approach to IPv6, making it impossible to cover them all in this article. When a provider allows for routed setups, I use this approach:
Make your own VPN: FreeBSD, WireGuard, IPv6, and ad-blocking included
- assigning a /72 to the bridge for the jails and VMs.
In my opinion, FreeBSD is a perfect all-rounder for backups, thanks to its ability to completely partition services. You can separate backup services (or specific servers/clients) into different jails or even VMs. Furthermore, using ZFS greatly enhances both flexibility and the range of tools you can use.
The main distinction is usually between local backup servers (physically accessible, though not always attended, and in locations deemed secure) and remote ones, such as leased external servers. I personally use a combination of both. If the services I need to back up are external, in a datacenter, and need to be quickly restorable, I prefer to always have a copy on another server in a different datacenter with good outbound connectivity. This guarantees good bandwidth for restores, which isn't always available from a local connection to the outside world. However, an internal, nearby, and accessible backup server (even a Raspberry Pi or a mini PC) ensures physical access to the data. Whenever possible, I maintain both an external and an internal copy - and they are autonomous, meaning the internal copy is
not
a replica of the external one, but an additional, independent backup. This ensures that if a problem occurs with the external backup, it won't automatically propagate to the internal one. In any case, the backup must always be in a different datacenter from the one containing the production data. When
the fire at the OVH datacenter in Strasbourg
caused the entire complex to shut down, many people found themselves in trouble because their backups were in the same, now unreachable, location. I had a copy with another provider, in a different datacenter and country, as well as a local copy.
Despite it being "just" a backup server, I almost always use some form of disk redundancy. If I have two disks, I set up a mirror. With three or more, I use RaidZ1 or RaidZ2. This is because, in my view, backups are nearly as important as production data. The inability to recover data from a backup means it's lost forever. And it happens often, very often, that someone contacts me to recover a file (or a database, etc.) days or weeks after its accidental loss or deletion. Usually, pulling out a file from a two-month-old backup generates a mix of disbelief, admiration, but above all, a sense of security in the person requesting it. And that is what our work should instill in the people we collaborate with.
The backup server should be hardened. If possible, it should be protected and unreachable from the outside. My best backup servers are those accessible only via VPN, capable of pulling the data on their own. If they are on a LAN, it's even better if they are completely disconnected from the Internet.
For this very reason,
backups must always be encrypted
. Having a backup means having full access to the data, and the backup server is the prime target for being breached or stolen if the goal is to get your hands on that data. I've seen healthcare facilities' backup servers being targeted (in a rather trivial way, to be honest) by journalists looking for health details of important figures. It is therefore critical that the backup server be as secure as possible.
Based on the type of access, I use two types of encryption:
If the server is local
(especially if the ZFS pool is on external disks), I usually install FreeBSD on UFS in read-only mode, as
I've described in a previous article
, and encrypt the backup disks with
GELI
. This ensures that in the event of a "dirty" shutdown (more likely in unattended environments), I can reconnect to the host and then reactivate the ZFS pool. This approach makes it nearly impossible to retrieve even the pool's metadata if the disks are stolen, as GELI performs a full-device encryption. For example, an employee of a company I work with stole one of the secondary backup disks (which was located at a different, unmonitored company site) to steal information. He got nothing but a criminal complaint. With this approach, it's also not necessary to further encrypt the datasets, which avoids some issues (which I'll discuss later, in a future post).
If the server is remote
, in a datacenter, I usually use ZFS native encryption, encrypting the main backup dataset (and
BastilleBSD
's, if applicable). Consequently, all child datasets containing backups will also be encrypted. In this case as well, a password will be required after a reboot to unlock those datasets, ensuring that the data cannot be extracted if control of the disks is lost.
Here is an example of how to use GELI to encrypt an entire partition and then create a ZFS pool on it (in the example, the disk is
da1
- do not follow these commands blindly, or you will erase all content on the
da1
device!):
# WARNING: This destroys the existing partition table on disk da1
gpart destroy -F da1

# Create a new GPT partition table
gpart create -s gpt da1

# Add a freebsd-zfs partition that spans the entire disk
# The -a 1m flag ensures proper alignment
gpart add -t freebsd-zfs -a 1m da1

# Initialize GELI encryption on the new partition (da1p1)
# We use AES-XTS with 256-bit keys and a 4k sector size
# The -b flag means "boot," prompting for the passphrase at boot time
geli init -b -l 256 -s 4096 da1p1
# You will be prompted for a passphrase: choose a strong one and save it!

# Attach the encrypted partition. A new device /dev/da1p1.eli will be created.
# You will be prompted for the passphrase you just set
geli attach da1p1

# (Optional) Check the status of the encrypted device
geli status da1p1

# Create the ZFS pool "bckpool" on the encrypted device
# We enable zstd compression (an excellent compromise) and disable atime
zpool create -O compression=zstd -O atime=off bckpool da1p1.eli
In this setup, the reference pool for everything related to backups will be
bckpool
- and you'll need to keep this in mind for the next steps. Additionally, after every server reboot, you'll need to "unlock" the disk and import the pool:
# Enter the passphrase when prompted
geli attach da1p1

# Import the ZFS pool, which is now visible
zpool import bckpool
With this method, it's not necessary to encrypt the ZFS datasets, as the underlying disk (or, more precisely, the partition containing the ZFS pool) is already encrypted.
If, instead, you choose to encrypt the ZFS dataset (for example, if you install FreeBSD on the same disks that will hold the data and don't want to use a multi-partition approach), you should create a base encrypted dataset. Inside it, you can create the various backup datasets, VMs, and the BastilleBSD mountpoint. Due to property inheritance, they will all be encrypted as well.
To create an encrypted dataset, a command like this will suffice:
# Creates a new dataset with encryption enabled.
# keylocation=prompt will ask for a passphrase every time it's mounted.
# keyformat=passphrase specifies the key type.
zfs create -o encryption=on -o keylocation=prompt -o keyformat=passphrase zfspool/dataset
In this case, after every reboot, you will need to load the key and mount the dataset:
zfs load-key zfspool/dataset
zfs mount zfspool/dataset
Keep in mind the setup you choose, as many of the subsequent choices and commands will depend on it.
Base System Setup
I'll install BastilleBSD - a useful tool for separating services into jails. It will be helpful for isolating our backup services:
pkg install -y bastille
If you used ZFS for the root filesystem, you can proceed directly with the setup. Otherwise (i.e., ZFS on other disks), you'll need to edit the
/usr/local/etc/bastille/bastille.conf
file and specify the correct dataset on which to install the jails. Then run:
bastille setup
Once the automatic setup is complete, check the
/etc/pf.conf
file - it will be automatically configured to only accept SSH connections. Ensure the network interface is set correctly. When you activate
pf
, you will be kicked out of the server, but you can then reconnect.
service pf start
Let's bootstrap a FreeBSD release for the jails - this will be useful later.
bastille bootstrap 14.3-RELEASE update
Now, we create a local bridge. Jails and VMs can be attached to it, making them fully autonomous. Using VNET jails, for example, will allow the creation of VPNs or
tun
interfaces inside them, simplifying potential future setups (and increasing security by using a dedicated network stack).
Modify the
/etc/rc.conf
file and add:
# Add lo1 and bridge0 to the list of cloned interfaces
cloned_interfaces="lo1 bridge0"
# Assign an IP address and netmask to the bridge
ifconfig_bridge0="inet 192.168.0.1 netmask 255.255.255.0"
# Enable gateway functionality for routing
gateway_enable="yes"
Let's also modify
/etc/pf.conf
to allow the
192.168.0.0/24
subnet to access the Internet via NAT. We will skip packet filtering on
bridge0
and enable NAT. This isn't the most secure setup, but it's sufficient to get started:
#...
# Skip PF processing on the internal bridge interface
set skip on bridge0
#...
# NAT traffic from our internal network to the outside world
nat on $ext_if from 192.168.0.0/24 to any -> ($ext_if:0)
#...
To ensure the new settings are correct, it's a good idea to test with a reboot.
Since I often configure
vm-bhyve
in my setups, I prefer to install it right away, creating the dataset that will contain the VMs and installation templates. Remember that
zroot
is only valid if you installed the entire system on ZFS; otherwise, you'll need to change it to your own dataset:
# Install required packages
pkg install vm-bhyve grub2-bhyve bhyve-firmware
# Create a dataset to store VMs
zfs create zroot/VMs
# Enable the vm service at boot
sysrc vm_enable="YES"
# Set the directory for VMs, using the ZFS dataset
sysrc vm_dir="zfs:zroot/VMs"
# Initialize vm-bhyve
vm init
# Copy the example templates
cp /usr/local/share/examples/vm-bhyve/* /zroot/VMs/.templates/
At this point, I usually enable the console via
tmux
. This means that when a VM is launched, it won't open a VNC port by default, but a
tmux
session connected to the VM's serial port. Let's install and configure
tmux
:
pkg install -y tmux
vm set console=tmux
Let's also attach the switch we created (
bridge0
) to
vm-bhyve
so we can use it:
vm switch create -t manual -b bridge0 public
Now,
vm-bhyve
is ready.
The basic infrastructure is complete. We now have:
ZFS
to ensure data integrity, which will also handle redundancy, etc.
BastilleBSD
to manage jails, useful for backing up Linux, NetBSD, OpenBSD, and non-ZFS FreeBSD machines.
vm-bhyve
to install specific systems (like Proxmox Backup Server).
Backup Strategies
I use various backup tools, too many to list in this article. So I'll make a broad distinction, describing how to use this server to achieve our goal: securing data.
For
FreeBSD servers with ZFS
(hosts, VMs, jails, hypervisors, and their respective VMs), I use an extremely useful, efficient, and reliable tool:
zfs-autobackup
.
For
Linux servers (without ZFS), NetBSD, OpenBSD
, etc. (any non-ZFS OS), I usually use
BorgBackup
. There are other fantastic tools like
restic
,
Kopia
, etc., but BorgBackup has never let me down and has served me well even on low-power devices and after incredibly complex disasters.
For
Proxmox servers
(a solution I've used with satisfaction in production since 2013, although I'm recently migrating to FreeBSD/bhyve where possible), I use two possible alternatives (often both at the same time): if the storage is ZFS, I use the
zfs-autobackup
approach. In either case, the most practical solution is the Proxmox Backup Server. And the Proxmox Backup Server is one of the reasons I proposed installing
vm-bhyve
: running it in a VM and storing the data on the FreeBSD host gives you the best of both worlds. Some time ago, I tried running it in a FreeBSD jail (via Linuxulator), but it didn't work.
Backups using zfs-autobackup
zfs-autobackup
is an extremely useful and effective tool. It allows for "pull" type backups, as well as having an intermediary host that connects to both the source and destination, which is useful if you don't want direct contact between the source and destination. I won't describe the latter setup, but the documentation is clear, and I have several of them in production, ensuring that the production server and its backup server cannot communicate with each other.
I usually create a dataset for each server and instruct
zfs-autobackup
to keep that server's backups in that dataset. The snapshots taken and transferred will all be from the same instant, so as not to create a time skew (some tools of this kind snapshot a dataset, then transfer it, which can result in minutes of difference between two different datasets from the same server).
I've described in detail how I perform this type of backup in a
previous post
, so I suggest reading that post for reference.
Let's install zfs-autobackup on the FreeBSD server:
pkg install py311-zfs-autobackup mbuffer
Backups for other servers using BorgBackup
When I don't have ZFS available or need to perform a file-based backup (all or partial), I use a different technique.
BorgBackup
backups are primarily "push" based, meaning the client will connect to the backup server. This is not optimal or the most secure approach, as the backup server should, in theory, be hardened. Even when protecting everything via VPN, the risk remains that a compromised server could connect to its backup server and alter or delete the backups. I have seen this happen in ransomware cases (especially in the Microsoft world), and so I try to be careful to minimize this type of problem, mainly through snapshots of the backup server (an operation that will be described later).
To ensure the highest possible security, I create a FreeBSD jail on the backup server for each server I need to back up. The advantage of this approach is the complete separation of all servers from each other. By using a regular user inside a jail, a compromised server that connects to its backup server would only be able to reach its own backups, as it would be confined to a user account and, even if it managed to escalate privileges, still be inside a jail.
Let's say, for example, we want to back up a server called "ServerA" (great imagination, I know). We create a dedicated jail on the backup server:
# Create a new VNET jail named "servera" attached to our bridge
bastille create -B servera 14.3-RELEASE 192.168.0.101/24 bridge0
BastilleBSD will automatically set the host's gateway for the jail. In our case, this is incorrect, so we need to modify it and set the jail's gateway to
192.168.0.1
in the
/usr/local/bastille/jails/servera/root/etc/rc.conf
file:
# ...
defaultrouter="192.168.0.1"
# ...
Restart the jail and connect to it:
bastille restart servera
bastille console servera
Now, inside the jail, we install
borgbackup
:
pkg install py311-borgbackup
BorgBackup doesn't run a daemon; it's launched by the remote server (which sends its data to the backup server), so it's important that the installed version is compatible with the one on the remote host.
Since we'll be using SSH, let's enable it:
service sshd enable
service sshd start
And create a non-privileged user for this purpose:
# The 'adduser' utility provides an interactive way to create a user.
root@servera:~ # adduser
Username: servera
Full name: Server A
Uid (Leave empty for default): 
Login group [servera]: 
Login group is servera. Invite servera into other groups? []: 
Login class [default]: 
Shell (sh csh tcsh nologin) [sh]: 
Home directory [/home/servera]: 
Home directory permissions (Leave empty for default): 
Use password-based authentication? [yes]: 
Use an empty password? (yes/no) [no]: 
Use a random password? (yes/no) [no]: yes
Lock out the account after creation? [no]: 
Username    : servera
Password    : <random>
Full Name   : Server A
Uid         : 1001
Class       : 
Groups      : servera 
Home        : /home/servera
Home Mode   : 
Shell       : /bin/sh
Locked      : no
OK? (yes/no) [yes]: yes
adduser: INFO: Successfully added (servera) to the user database.
adduser: INFO: Password for (servera) is: JIkdq8Ex
The user is created and can receive SSH connections. After setting everything up, I suggest disabling password-based login in the jail's SSH configuration, using only public key authentication.
As mentioned, the biggest risk of a "push" backup is that a compromised client could access the backup server and delete or encrypt the backup history, rendering it useless.
To drastically mitigate this risk, we can configure SSH to force the client to operate in a special Borg mode called
append-only
. In this mode, the SSH key used by the client will only have permission to create new archives, not to read or delete old ones. However, this approach could complicate some client-side operations (like
mount
,
prune
, etc.), forcing them to be done on the server. For this reason, I won't describe it in this setup, "limiting" myself to taking snapshots of the repositories. It can be a very good practice, so I recommend considering it.
Let's initialize the BorgBackup repository. In this example, for simplicity, I won't set up repository encryption. If the jails are on an encrypted dataset or GELI-encrypted disks, there will still be data encryption on the disks, but there will be no protection against someone who could physically access the server while the disks are mounted. As usual, security is like an onion: every layer helps. Personally, I suggest enabling and using it ALWAYS.
# Switch to the new user
su -l servera
# Initialize a new Borg repo named "servera" with no encryption (for this example)
borg init -e none servera
The jail is ready, but it's unreachable from the outside. There are two ways to make it accessible:
Install a VPN system inside the jail itself.
Using tools like Zerotier or Tailscale (which don't need to expose ports) will immediately create the conditions to connect to the jail, which will remain inaccessible from the outside. As the jail is a VNET jail, we're free to choose any of the supported VPN technologies.
Expose a port on the backup server
, i.e., on the host, to allow external connections. Many advise against this path as they consider it less secure. It is, but sometimes we don't have the luxury of installing whatever we want on the server we're backing up.
To expose the port, go back to the host and modify the
/etc/pf.conf
file, creating the
rdr
and
pass
rules to let packets in:
# ...
# Redirect incoming traffic on port 1122 to the jail's SSH port (22)
rdr on $ext_if inet proto tcp from any to any port = 1122 -> 192.168.0.101 port 22
# ...
# Allow incoming traffic on port 1122
pass in inet proto tcp from any to any port 1122 flags S/SA keep state
Reload the
pf
configuration:
service pf reload
The jail will now be reachable on the server's public IP, on port 1122. Obviously, this port number is for illustrative purposes, and I used
from any
, but for better security, you should replace
any
with the IP address of the server that will be connecting to perform the backup.
By repeating this process for each server and creating a separate jail for each, you can have isolated jails in separate datasets with their backups, potentially setting space limits using ZFS quotas.
It's important to remember that backing up a live filesystem (i.e., without a snapshot or dumps) has a very high probability of being impossible to restore completely. Databases hate this approach because files will change while being copied and tend to get corrupted. Of course, it depends on the nature of the data (a backup of a static website will have no issues, but a WordPress database probably will), but it's crucial to think about a technique to snapshot the filesystem before proceeding. For example, I have already written about how to create snapshots on FreeBSD with UFS in a previous article:
FreeBSD tips and tricks: creating snapshots with UFS
.
I will cover other operating systems in a future, dedicated post.
Proxmox Backup Server in a Dedicated VM
Starting with version 4.0 (which is still in beta at the time of this writing), Proxmox Backup Server (PBS) supports storing its data in an S3 bucket. This is excellent news as it decouples the server from the data. There are great open-source S3 implementations, like
Minio
or
SeaweedFS
, which allow for clustering, replication, etc. In this "simple" case, we will install Proxmox Backup Server in a small VM, while for the data, we'll install Minio in a native FreeBSD jail. The advantage is undeniable: the VM will only serve as an "intermediary", but the data will rest directly on the FreeBSD host's dataset, natively. It will also be possible to specify other external endpoints, other repositories, etc.
As a philosophy, I tend not to use external providers unless for specific needs, so installing Minio in a jail is a perfect solution to manage this situation.
Let's install PBS by downloading the ISO from their website (https://enterprise.proxmox.com/iso/) - at this moment, the version that supports this setup is 4.0 Beta.
The directory to download to is the
vm-bhyve
ISOs directory. It's not strictly necessary, but it's useful for not "losing" it somewhere. So, go to the directory and download it:
cd /zroot/VMs/.iso
fetch https://enterprise.proxmox.com/iso/proxmox-backup-server_4.0-BETA-1.iso
Now let's create a VM with
vm-bhyve
. We can start from the Debian template, but we'll make some modifications to optimize performance. In this example, I'm giving it 30 GB of disk space, 2 GB of RAM, and 2 cores.
If you want to store all backups inside the VM, you'll need to size the virtual disk correctly (or create and attach another one). In this case, I will focus on the "clean" VM that will store its data on a dedicated jail with Minio.
vm create -t debian -s 30G -m 2G -c 2 pbs
Once the empty VM is created, let's modify its options:
vm configure pbs
We will modify the VM to be UEFI and to use the NVME disk driver - bhyve
performs significantly better on NVME than virtio, as previously tested
:
loader="uefi"
cpu="2"
memory="2G"
network0_type="virtio-net"
network0_switch="public"
disk0_type="nvme"
disk0_name="disk0.img"
Fortunately, the Proxmox team has provided for the installation of the Backup Server on devices without a graphical interface, so the boot menu will allow installation via serial console. Let's launch the installation and connect to the virtual serial console:
cd /zroot/VMs/.iso
vm install pbs proxmox-backup-server_4.0-BETA-1.iso
vm console pbs
Select the installation via
Terminal UI (serial console)
and proceed normally as if it were a physical host, assigning an IPv4 address from the
192.168.0.x
range (in this example, I'll use
192.168.0.3
).
This way, the Proxmox Backup Server will run in a VM, with the ability to take snapshots before updates, etc., without any worries.
Once the installation is complete, PBS will reboot and listen on port 8007 of its IP. Again, as with the jails, we have two options: install a VPN system within the VM itself (thus exposing it automatically only on that VPN - generally a more secure operation) or expose port 8007 on the server's public IP.
In the latter case, add the relevant lines to the
/etc/pf.conf
file on the FreeBSD backup server:
# ...
# Redirect incoming traffic on port 8007 to the PBS VM's web interface
rdr on $ext_if inet proto tcp from any to any port = 8007 -> 192.168.0.3 port 8007
# ...
# Allow that traffic to pass
pass in inet proto tcp from any to any port 8007 flags S/SA keep state
Reload the
pf
configuration:
service pf reload
The PBS VM configuration is complete. If you chose to use the PBS's internal disk as a repository, no further operations are necessary (other than the normal repository creation, etc., within PBS).
In this case, however, we will use a different approach.
Creating a Minio Jail as a Data Repository for PBS
This approach, in my opinion, has a number of important advantages. The first is that Minio will run in a dedicated jail on the host, at full performance, and will store the data directly on the physical ZFS datapool, thus removing any other layer in between. This jail could potentially be moved to other hosts (by connecting PBS and the jail via VPN or public IP), made redundant thanks to all of Minio's features, etc. Another solution I am successfully testing (in other setups) is SeaweedFS.
Let's create a dedicated jail with Minio and put it on the bridge, so that PBS can access it on the LAN.
bastille create -B minio 14.3-RELEASE 192.168.0.11/24 bridge0
If not configured directly, BastilleBSD will use the host's gateway for the jail, which is incorrect in this case. So let's go modify it and restart the jail. Enter the jail with:
bastille console minio
And modify the
/etc/rc.conf
file to have the correct gateway (following the example addresses):
# ...
ifconfig_vnet0=" inet 192.168.0.11/24 "
defaultrouter="192.168.0.1"
# ...
Exit the jail and restart it:
bastille restart minio
Enter the jail and install Minio:
bastille console minio
pkg install -y minio
Minio is already able to start, but PBS, even on the LAN, wants an encrypted connection. Fortunately, there's a handy tool that can generate the certificates for us:
# Download the certgen tool
fetch https://github.com/minio/certgen/releases/latest/download/certgen-freebsd-amd64

# Make it executable and run it for our jail's IP
chmod a+rx certgen-freebsd-amd64
./certgen-freebsd-amd64  -host "192.168.0.11"

# Create the necessary directories and set permissions
mkdir -p /usr/local/etc/minio/certs
cp private.key public.crt /usr/local/etc/minio/certs/
chown -R minio:minio /usr/local/etc/minio/certs/
Let's view the certificate's fingerprint. Since it's self-signed, we'll need it for PBS later. For security reasons, PBS will ask for the fingerprint of non-directly verifiable certificates. Run the following command and take note of the result:
openssl x509 -in /usr/local/etc/minio/certs/public.crt -noout -fingerprint -sha256
At this point, enable and configure Minio in
/etc/rc.conf
.
WARNING
: The username and password (access key and secret) used in this example are insecure and for testing purposes only. It is strongly recommended to use different values:
# Enable Minio service
minio_enable="YES"
# Set the address for the Minio console
minio_console_address=":8751"
# Set the root user and password as environment variables
minio_env="MINIO_ROOT_USER=testaccess MINIO_ROOT_PASSWORD=testsecret"
Start Minio:
service minio start
If everything went correctly, Minio is now running (with its certificates) and ready to receive connections.
It's now time to create the bucket(s) that PBS will use. There are several ways to do this, but to test that everything is working and to configure PBS, I suggest connecting via an SSH tunnel.
# Create an SSH tunnel from your local machine to the backup server
# Port 8007 is forwarded to the PBS web UI
# Port 8751 is forwarded to the Minio console
ssh user@backupServerIP -L8007:192.168.0.3:8007 -L8751:192.168.0.11:8751
This way, we'll create a tunnel between the FreeBSD backup server and our workstation, mapping
127.0.0.1:8007
to
192.168.0.3:8007
(the PBS web interface) and
127.0.0.1:8751
to
192.168.0.11:8751
(the Minio console port).
Now, connect to
https://127.0.0.1:8751
, enter the credentials specified in
/etc/rc.conf
, and create a bucket.
Once the bucket is created, you can configure PBS to use it. Connect to PBS via
https://127.0.0.1:8007
and go to
S3 Endpoints
. Set a name, use
192.168.0.11
as the IP and
9000
as the port, enter the access and secret keys, and the certificate fingerprint we generated earlier.
Enable "Path Style"
or it will not work.
Then go to
Datastores
and add it, as you would for any other S3 datastore, by specifying the created bucket and a local directory where the system will keep its cache.
If everything was set up correctly, PBS will create its structure in the bucket, and from that moment on, you can use it. Always keep in mind that this is still a "technology preview", so there may be issues, but from my tests, it is sufficiently reliable.
Taking Local Snapshots of Backups
One of the most common techniques used in ransomware attacks is to also delete or encrypt backups. They often use automated methods, relying on the fact that many (too many!) consider a "backup" to be a simple copy of files to a network share. However, it's not impossible that, in specific cases, they might compromise the machine and connect to the backup server. This is nearly impossible with a "pull" type backup (like the one managed by
zfs-autobackup
) but is still possible with the "push" approach, which involves using BorgBackup or similar tools.
This happened to one of my clients once - in that case, the problem originated internally, from an employee who wanted to cover up his mistake, inadvertently creating a disaster - but that will be material for another post.
Fortunately, the client had a system that solved the problem: thanks to ZFS, we can have local snapshots on the backup server, which are invisible and inaccessible to the production server. Since we have already installed
zfs-autobackup
, it's easy to use it for this purpose as well. I've already talked about this in a
previous article
and won't rewrite the steps here. Just consult that article, keeping in mind that in this case, it's not advisable to snapshot all the datasets on the backup server (the space would grow exponentially), but only those at risk. In the cases analyzed in this post, this applies only to the
push
part, as PBS will also be accessible only from the Proxmox servers and not from the VMs they contain. If, in this case too, you don't trust those who manage the Proxmox servers, just set up snapshots for the Minio jail as well.
Conclusion
This long post aims to analyze, in a general way, how I believe one can manage reasonably secure backups of their data. Obviously, there are many variables, additional precautions, possible optimizations, hardening, etc., that must be studied on a case-by-case basis. There are old rules, new rules, old and new philosophies. Recently, many people who have embraced the cloud have often stopped thinking about backups, only to realize it when something happens and the data has, indeed, vanished... into the clouds.
In this post, I have generically covered the setup of the backup server, and this demonstrates how FreeBSD, thanks to its features, can be considered an ideal platform for this type of task.
In the next articles in this series, I will examine the client side, i.e., how to structure them for a sufficiently reliable backup, and how to monitor everything - because I've seen this too: people resting easy because the backup was supposedly running every night, but in fact, the backup had been failing every night for more than 4 years.
Stay Tuned and stay...backupped!
