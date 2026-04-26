---
title: "From ZNC to Soju"
url: "https://susam.net/from-znc-to-soju.html"
fetched_at: 2026-04-25T12:09:06.896336+00:00
source: "susam.net"
tags: [blog, raw]
---

# From ZNC to Soju

Source: https://susam.net/from-znc-to-soju.html

From ZNC to Soju
By
Susam Pal
on 12 Feb 2026
I have recently switched from ZNC to Soju as my IRC bouncer and I am
  already quite pleased with it.  I usually run my bouncer on a Debian
  machine, where Soju is well packaged and runs smoothly right after
  installation.  By contrast, the ZNC package included with Debian 13
  (Trixie) and earlier fails to start after installation because of a
  missing configuration file.  As a result, I was forced to maintain
  my own configuration file along with a necessary PEM bundle, copy
  them to the Debian system and carefully set the correct file
  permissions before I could run ZNC successfully.  None of this is
  necessary with Soju, since installing it from the Debian package
  repository automatically sets up the configuration and certificate
  files.  I no longer have to manage any configuration or certificate
  files myself.
Setup
It is quite straightforward to install and set up Soju on Debian.
  The following two commands install Soju:
sudo apt-get update
sudo apt-get -y install soju
Then setting up an IRC connection involves another two commands:
sudo sojuctl user create -username soju -password YOUR_SOJU_PASSWORD
sudo sojuctl user run soju network create -name bnc1 -addr irc.libera.chat -nick YOUR_NICK -pass YOUR_NICK_PASSWORD
Here,
YOUR_SOJU_PASSWORD
is a placeholder for a new
  password you must choose for your Soju user.  Finally, we restart
  Soju as follows:
sudo systemctl restart soju
Database
What previously involved maintaining several files that had to be
  installed and configured on each machine running ZNC is now reduced
  to the two
sojuctl
commands above.  Still, the
  configuration needs to live somewhere.  In fact, the
  two
sojuctl
commands introduce earlier store the
  configuration in a SQLite database.  Here is a glimpse of what the
  database looks like:
$
sudo sqlite3 /var/lib/soju/main.db '.tables'
Channel              MessageFTS_data      ReadReceipt
DeliveryReceipt      MessageFTS_docsize   User
Message              MessageFTS_idx       WebPushConfig
MessageFTS           MessageTarget        WebPushSubscription
MessageFTS_config    Network
$
sudo sqlite3 /var/lib/soju/main.db 'SELECT * from User'
1|soju|$2a$10$mM5Qcz8.OPMi9lyWDxPRh.bNxzq7jtLdxcoPl09AYTnqcmLmEqzSO|0|||2026-02-17T23:24:24.926Z|1||-1
$
sudo sqlite3 /var/lib/soju/main.db 'SELECT * from Network'
1|bnc1|1|irc.libera.chat|YOUR_NICK||||YOUR_NICK_PASSWORD|||||||1|1
Client Configuration
Finally, the IRC client can be configured to connect to port 6697 on
  the system running Soju.  Here is an example of how this can be done
  in Irssi:
/network add -nick YOUR_NICK -user soju/bnc1 net1
/server add -tls -network bnc1 YOUR_SOJU_HOST 6697 YOUR_SOJU_PASSWORD
/connect net1
You can also set up multiple connections to IRC networks through the
  same Soju instance.  All you need to do is repeat
  the
sojuctl
commands to create additional networks such
  as
bnc2
,
bnc3
and so on, then repeat the
  configuration in your IRC client using new network names such as
net2
,
net3
, etc.  These network names are
  entirely user defined, so you can choose any names you like.  The
  names
bnc2
,
net2
and so on are only
  examples.
