---
title: "Installing Void Linux on ZFS with Hibernation Support"
url: "https://it-notes.dragas.net/2025/12/22/void-linux-zfs-hibernation-guide/"
fetched_at: 2026-04-28T07:02:49.466357+00:00
source: "it-notes.dragas.net"
tags: [blog, raw]
---

# Installing Void Linux on ZFS with Hibernation Support

Source: https://it-notes.dragas.net/2025/12/22/void-linux-zfs-hibernation-guide/

Introduction
FreeBSD continues to make strides in desktop support, but Linux still holds an advantage in hardware compatibility. After running openSUSE Tumbleweed on my mini PC for several months, I decided it was time to switch to a solution I could control more closely. Not because Tumbleweed doesn't work well - it works great! - but I prefer having direct control over what happens on my machine. And I want native ZFS, because I prefer it over btrfs and it allows me to manage snapshots, backups, and rollbacks just as I do on FreeBSD, using the same tools and procedures.
The choice of
Void Linux
comes from its BSD-like approach: modular and free of unnecessary complexity. This makes it an excellent solution for this type of setup.
ZFSBootMenu
is an extremely powerful tool. It provides an experience similar to FreeBSD's boot loader and natively supports ZFS. I strongly recommend reading the documentation and exploring its features, as some of them - like the built-in SSH daemon - can be genuine lifesavers in recovery scenarios.
Prerequisites and Audience
This guide is not for absolute beginners.
If you're new to Linux or Unix-like operating systems, you'd be better served by a ready-to-use distribution like
openSUSE
Leap (or Tumbleweed for a rolling distribution),
Linux Mint
,
Debian
,
Ubuntu
, or
Manjaro
. The purpose of this article is to demonstrate a stable, upgradeable, and reasonably secure base setup for users already comfortable with system administration. It uses the
glibc
variant of Void Linux. The
musl
version requires different commands, for example for locale generation.
Use at your own risk.
This guide synthesizes instructions from several sources:
If your setup differs from what's described here (NVMe disk, UEFI boot, Secure Boot disabled), consult the linked guides for explanations and variations.
Installation Script (Optional)
If you want to reproduce this setup quickly, I maintain a script that automates the procedure described in this guide: disk partitioning, ZFS pool and dataset creation, encrypted swap for hibernation resume, dracut configuration, and ZFSBootMenu EFI setup. An optional KDE Plasma desktop installation is also supported.
The script is interactive and will ask for the required parameters (target disk, timezone and keymap, passphrases, desktop options).
Requirements, usage instructions, and known limitations are documented in the repository README
That said, I still recommend going through the manual process at least once. Understanding each step is part of the value of this setup, especially when troubleshooting or adapting it to different hardware.
Boot Environment
Since ZFS isn't supported by the base Void Linux image, we'll use
hrmpf
, an excellent rescue system based on Void Linux that includes ZFS support out of the box.
After booting, you can either proceed directly or SSH into the machine to continue remotely. I generally prefer SSH since it makes copy-paste operations much easier - especially when dealing with UUIDs and long commands. To enable SSH access, set a root password and allow root login:
passwd
Edit
/etc/ssh/sshd_config
and enable:
PermitRootLogin yes
Restart the SSH daemon:
sv restart sshd
Find the machine's IP address:
ip addr
You can now connect via SSH from another device.
Initial Setup
Set up the environment variables and generate a host ID - we need it for ZFS:
source /etc/os-release
export ID

zgenhostid -f 0x00bab10c
Disk Configuration
Identify your target disk and set up the partition variables. This approach keeps everything consistent and reduces errors:
# Set the base disk - adjust this to match your system
export DISK="/dev/nvme0n1"

# For NVMe disks, partitions are named like nvme0n1p1, nvme0n1p2, etc.
# For SATA/SAS disks (sda, sdb), partitions are named sda1, sda2, etc.
# Set the partition separator accordingly:
export PART_SEP="p"  # Use "p" for NVMe, empty string "" for SATA/SAS

# Define partition numbers
export BOOT_PART="1"
export SWAP_PART="2"
export POOL_PART="3"

# Build full device paths
export BOOT_DEVICE="${DISK}${PART_SEP}${BOOT_PART}"
export SWAP_DEVICE="${DISK}${PART_SEP}${SWAP_PART}"
export POOL_DEVICE="${DISK}${PART_SEP}${POOL_PART}"
Verify your configuration before proceeding:
echo "Boot device: $BOOT_DEVICE"
echo "Swap device: $SWAP_DEVICE"
echo "Pool device: $POOL_DEVICE"
Wipe the Disk
Warning: This operation will irreversibly destroy all data on the selected disk. Double-check that you've selected the correct disk and be sure to have a complete backup of your system!
zpool labelclear -f "$DISK"

wipefs -a "$DISK"
sgdisk --zap-all "$DISK"
Create Partitions
EFI System Partition
If you're not using UEFI boot, adapt this procedure following the appropriate guide linked at the beginning of this post:
sgdisk -n "${BOOT_PART}:1m:+512m" -t "${BOOT_PART}:ef00" "$DISK"
Swap Partition
The swap partition should be slightly larger than your RAM to support hibernation. When you hibernate, the entire contents of RAM are written to swap, so you need enough space to hold it all plus some overhead. In this example, I have 16 GB of RAM, so I'm creating an 18 GB swap partition:
sgdisk -n "${SWAP_PART}:0:+18g" -t "${SWAP_PART}:8200" "$DISK"
ZFS Pool Partition
sgdisk -n "${POOL_PART}:0:-10m" -t "${POOL_PART}:bf00" "$DISK"
Set Up ZFS Encryption
Encrypting the disk is strongly recommended, especially for laptops. Replace
SomeKeyphrase
with a strong passphrase that's easy to type. Keep in mind that during early boot, the keyboard layout might default to US, so choose a passphrase that's easy to type on a US keyboard layout:
echo 'SomeKeyphrase' > /etc/zfs/zroot.key
chmod 000 /etc/zfs/zroot.key
Create the ZFS Pool
Create the pool with conservative, well-tested options:
zpool create -f -o ashift=12 \
 -O compression=lz4 \
 -O acltype=posixacl \
 -O xattr=sa \
 -O relatime=on \
 -O encryption=aes-256-gcm \
 -O keylocation=file:///etc/zfs/zroot.key \
 -O keyformat=passphrase \
 -o autotrim=on \
 -o compatibility=openzfs-2.2-linux \
 -m none zroot "$POOL_DEVICE"
Create ZFS Datasets
zfs create -o mountpoint=none zroot/ROOT
zfs create -o mountpoint=/ -o canmount=noauto zroot/ROOT/${ID}
zfs create -o mountpoint=/home zroot/home

zpool set bootfs=zroot/ROOT/${ID} zroot
Export and Reimport for Installation
zpool export zroot
zpool import -N -R /mnt zroot
zfs load-key -L prompt zroot

zfs mount zroot/ROOT/${ID}
zfs mount zroot/home

udevadm trigger
Install the Base System
XBPS_ARCH=x86_64 xbps-install \
  -S -R https://mirrors.servercentral.com/voidlinux/current \
  -r /mnt base-system
Copy Host Configuration
Copy the files we generated earlier to the new system:
cp /etc/hostid /mnt/etc
mkdir -p /mnt/etc/zfs
cp /etc/zfs/zroot.key /mnt/etc/zfs
Configure Encrypted Swap
Now we'll set up the encrypted swap partition. This is where the hibernation magic happens - by using a separate LUKS-encrypted partition instead of a ZFS zvol, we can properly resume from hibernation.
Format the swap partition with LUKS:
cryptsetup luksFormat --type luks1 "$SWAP_DEVICE"
Open the encrypted partition, create the swap filesystem, and activate it:
cryptsetup luksOpen "$SWAP_DEVICE" cryptswap
mkswap /dev/mapper/cryptswap
swapon /dev/mapper/cryptswap
Preserve Variables for Chroot
Before entering the chroot, save the disk variables so they remain available inside the new environment:
cat << EOF > /mnt/root/disk-vars.sh
export DISK="$DISK"
export PART_SEP="$PART_SEP"
export BOOT_PART="$BOOT_PART"
export SWAP_PART="$SWAP_PART"
export POOL_PART="$POOL_PART"
export BOOT_DEVICE="$BOOT_DEVICE"
export SWAP_DEVICE="$SWAP_DEVICE"
export POOL_DEVICE="$POOL_DEVICE"
export ID="$ID"
EOF
Enter the Chroot Environment
xchroot /mnt
From this point forward, all commands are executed inside the new system.
First, load the saved variables:
source /root/disk-vars.sh
Configure fstab
Add the swap entry to
/etc/fstab
:
/dev/mapper/cryptswap   none            swap            defaults        0 0
Set Up Automatic Swap Unlock
To avoid entering the swap password separately after unlocking the ZFS pool, we'll create a keyfile stored on the encrypted ZFS dataset. This is secure because the keyfile only becomes accessible after the ZFS pool is unlocked.
First, install cryptsetup in the new system:
xbps-install -S cryptsetup
Generate a random keyfile and add it to the LUKS partition:
dd bs=1 count=64 if=/dev/urandom of=/boot/volume.key

cryptsetup luksAddKey "$SWAP_DEVICE" /boot/volume.key

chmod 000 /boot/volume.key
chmod -R g-rwx,o-rwx /boot
Add the keyfile to
/etc/crypttab
:
echo "cryptswap   $SWAP_DEVICE   /boot/volume.key   luks" >> /etc/crypttab
Include the keyfile and crypttab in the initramfs. Create
/etc/dracut.conf.d/10-crypt.conf
:
install_items+=" /boot/volume.key /etc/crypttab "
Basic System Configuration
Configure keyboard layout and hardware clock. Adjust the keymap and timezone to match your location:
cat << EOF >> /etc/rc.conf
KEYMAP="us"
HARDWARECLOCK="UTC"
EOF

ln -sf /usr/share/zoneinfo/Europe/Rome /etc/localtime
Configure locales:
cat << EOF >> /etc/default/libc-locales
en_US.UTF-8 UTF-8
en_US ISO-8859-1
EOF

echo "LANG=en_US.UTF-8" > /etc/locale.conf

xbps-reconfigure -f glibc-locales
Set the root password:
passwd
Configure ZFS Boot Support
cat << EOF > /etc/dracut.conf.d/zol.conf
nofsck="yes"
add_dracutmodules+=" zfs "
omit_dracutmodules+=" btrfs "
install_items+=" /etc/zfs/zroot.key "
EOF
Install ZFS:
xbps-install -S zfs
Configure ZFSBootMenu
Set the basic boot properties:
zfs set org.zfsbootmenu:commandline="quiet" zroot/ROOT
zfs set org.zfsbootmenu:keysource="zroot/ROOT/${ID}" zroot
The Critical Step: Hibernation Support
Now we need to configure hibernation resume. This is the key insight that makes this setup work: normally, the encrypted ZFS root mounts first, and then it unlocks the swap partition. But when resuming from hibernation, the kernel needs to read the hibernation image from swap
before
mounting the root filesystem - otherwise, the saved state would be lost.
To solve this, we tell ZFSBootMenu to unlock the swap partition early, before mounting ZFS, by specifying its LUKS UUID.
Get the UUID of your swap partition:
blkid "$SWAP_DEVICE"
You'll see output like:
/dev/...: UUID="xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx" TYPE="crypto_LUKS" PARTUUID="..."
Store the UUID in a variable for the next step:
SWAP_UUID=$(blkid -s UUID -o value "$SWAP_DEVICE")
echo "Swap UUID: $SWAP_UUID"
Now set the boot parameters using the captured UUID:
zfs set org.zfsbootmenu:commandline="rd.luks.uuid=$SWAP_UUID resume=/dev/mapper/cryptswap" zroot/ROOT/${ID}
Set Up EFI Boot
Create and mount the EFI partition:
mkfs.vfat -F32 "$BOOT_DEVICE"

mkdir -p /boot/efi
Add the EFI partition to
/etc/fstab
using its UUID:
BOOT_UUID=$(blkid -s UUID -o value "$BOOT_DEVICE")
echo "UUID=$BOOT_UUID    /boot/efi    vfat    defaults    0 0" >> /etc/fstab
Mount it:
mount /boot/efi
Install ZFSBootMenu
xbps-install -S curl

mkdir -p /boot/efi/EFI/ZBM
curl -o /boot/efi/EFI/ZBM/VMLINUZ.EFI -L https://get.zfsbootmenu.org/efi
cp /boot/efi/EFI/ZBM/VMLINUZ.EFI /boot/efi/EFI/ZBM/VMLINUZ-BACKUP.EFI
Configure the EFI boot entries:
xbps-install -S efibootmgr

efibootmgr -c -d "$DISK" -p "$BOOT_PART" \
  -L "ZFSBootMenu (Backup)" \
  -l '\EFI\ZBM\VMLINUZ-BACKUP.EFI'

efibootmgr -c -d "$DISK" -p "$BOOT_PART" \
  -L "ZFSBootMenu" \
  -l '\EFI\ZBM\VMLINUZ.EFI'
Microcode updates
Void Linux is modular, so you may need to install additional packages for your specific hardware. For the Intel microcode, you need the non-free repo: For example:
# For Intel CPUs
xbps-install -S void-repo-nonfree 
xbps-install -S intel-ucode

# For AMD CPUs/GPUs
xbps-install -S linux-firmware-amd
After installing microcode updates, regenerate the boot images and exit:
xbps-reconfigure -fa
Desktop Installation (Optional)
If all you need is a minimal system or a server, you're done and ready to reboot. For a complete desktop environment, continue with the following steps.
Install Core Desktop Packages
xbps-install -S vim nano dbus elogind polkit xorg xorg-fonts xorg-video-drivers xorg-input-drivers dejavu-fonts-ttf terminus-font NetworkManager pipewire alsa-pipewire wireplumber xdg-user-dirs unzip gzip xz 7zip
Install KDE Plasma
xbps-install -S kde-plasma dolphin konsole firefox kdegraphics-thumbnailers ffmpegthumbs vlc ark kwrite discover kf6-purpose
Enable Services
ln -s /etc/sv/NetworkManager /etc/runit/runsvdir/default/
ln -s /etc/sv/dbus /etc/runit/runsvdir/default/
ln -s /etc/sv/udevd /etc/runit/runsvdir/default/
ln -s /etc/sv/polkitd /etc/runit/runsvdir/default/
ln -s /etc/sv/sddm /etc/runit/runsvdir/default/
Configure PipeWire Audio
mkdir -p /etc/xdg/autostart
ln -sf /usr/share/applications/pipewire.desktop /etc/xdg/autostart/

mkdir -p /etc/pipewire/pipewire.conf.d
ln -sf /usr/share/examples/wireplumber/10-wireplumber.conf /etc/pipewire/pipewire.conf.d/
ln -sf /usr/share/examples/pipewire/20-pipewire-pulse.conf /etc/pipewire/pipewire.conf.d/

mkdir -p /etc/alsa/conf.d
ln -sf /usr/share/alsa/alsa.conf.d/50-pipewire.conf /etc/alsa/conf.d
ln -sf /usr/share/alsa/alsa.conf.d/99-pipewire-default.conf /etc/alsa/conf.d
Enable Additional Repositories and Flatpak (Optional)
xbps-install -S void-repo-nonfree void-repo-multilib void-repo-multilib-nonfree

xbps-install -S flatpak
flatpak remote-add --if-not-exists flathub https://dl.flathub.org/repo/flathub.flatpakrepo
Create a Regular User and exit
For desktop use, create a non-root user with appropriate group memberships. Replace
username
with your desired username.
useradd -m username
passwd username
usermod username -G video,wheel,plugdev,kvm,audio,network
exit
Fix for NetworkManager
xchroot will bind mount /etc/resolv.conf and leave an empty file. Network Manager won't like it. So let's clean it up:
umount -l /mnt/etc/resolv.conf 2>/dev/null || true

rm -f /mnt/etc/resolv.conf
ln -s /run/NetworkManager/resolv.conf /mnt/etc/resolv.conf
Exit and Reboot
umount -n -R /mnt
zpool export zroot
reboot
Post-Installation
If everything went well, after entering your ZFS encryption password, you'll be greeted by the SDDM login screen.
Testing Hibernation
To verify that hibernation works correctly, you can clock the "Hibernate" button or:
loginctl hibernate
The system should power off. When you turn it back on, ZFSBootMenu will prompt for the password, unlock the swap partition, detect the hibernation image, and resume your session exactly where you left off.
If resume fails, check that: 1. The LUKS UUID in the ZFS commandline property matches your swap partition 2. The swap partition is large enough for your RAM 3. The dracut configuration includes the crypttab and keyfile
Conclusion
You now have a fully functional Void Linux system with native ZFS, full disk encryption, and working hibernation. The system is rolling, lightweight, and easy to maintain. Enjoy!
