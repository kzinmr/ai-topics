---
title: "Make Your Own Internet Presence with NetBSD and a 1 euro VPS - Part 1: Your Blog"
url: "https://it-notes.dragas.net/2025/04/22/make-your-own-internet-presence-with-netbsd-and-a-1-euro-vps-part-1-your-blog/"
fetched_at: 2026-04-28T07:02:50.161346+00:00
source: "it-notes.dragas.net"
tags: [blog, raw]
---

# Make Your Own Internet Presence with NetBSD and a 1 euro VPS - Part 1: Your Blog

Source: https://it-notes.dragas.net/2025/04/22/make-your-own-internet-presence-with-netbsd-and-a-1-euro-vps-part-1-your-blog/

Why NetBSD?
For many years, I've been using (and appreciating)
NetBSD
because it's stable, efficient, and reliable. The codebase has proven its reliability,
running without reboots for years without issues
. It supports ZFS (though differently than FreeBSD), LVM (useful for those accustomed to it on Linux), the ability to take filesystem snapshots (UFS2, making ZFS less crucial), and it's an
excellent virtualization platform
. Installation and updates are easy (including via
sysupgrade
- which I'll cover in a future article). Since it focuses on portable and optimized code (running on ancient architectures requires cleanliness and correctness), it's particularly efficient on low-power devices, like embedded systems or cheap VMs. Therefore, it's one of the best solutions for a small personal setup that can still deliver excellent results and simple management.
Indeed, the market offers very cheap VPS, often with just a single core and little RAM. But a modern single core packs power that a multi-core from just a few years ago could only dream of, and often, the I/O of these machines (a bottleneck for many services) is still decent. I personally use 1 euro per month VPS (VAT included - for those not subject to it, that's less than one euro per month!) with a public IPv4 address and (often) a /64 IPv6 block, ensuring full reachability across the entire network. I'm not providing direct links as I have no affiliations, but netcup's "piko" VPS are among the types I use most often (
a 4 euro/month netcup VM handles the entire FediMeteo project
), and this type of VM is ideal for our purpose because some providers (like netcup) allow you to upload your own ISO and install your preferred operating system. On VPS like these, I've installed everything - including
OmniOS
and
SmartOS
- without problems. And even such a small VPS, with an efficient operating system, can be extremely satisfying.
Why BSSG?
In this article, I'll describe how to create and publish a blog using
BSSG
as it exemplifies my concept of portability and minimalism. BSSG on NetBSD currently doesn't leverage parallelism provided by tools like GNU Parallel, but for small to medium-sized blogs, this won't be an issue, especially considering these small VMs only have 1 core. Obviously, you can use any Static Site Generator (SSG) (like Hugo, Nikola, 11ty, Pelican, Zola, etc.) - the important thing is to have a static site served by a simple web server.
Let's Start with the Installation
Installing NetBSD is quite straightforward and is clearly covered, complete with explanatory screenshots, in the
excellent official NetBSD documentation
, which I recommend using as a reference during the process, especially if it's your first time.
In my case, I made sure to use the proposed disk geometry, use the standard automatic partitioning, but
enable the "log" and "noatime" options for the filesystem
. Both these options will provide a huge advantage in I/O operations, especially with BSSG, as the first enables journaling and the second prevents updating file metadata on every access. BSSG is more I/O bound than CPU bound, so any optimization is beneficial.
Moving forward, I also recommend configuring the network (although installation can be done from packages on the installation ISO). For netcup, you can use DHCPv4 (even though it's a bit slow and sometimes seems to fail, the DHCP client will continue running in the background and eventually work).
For IPv6, I usually configure it manually later, so I'll describe that further down.
I also recommend enabling SSH, adding a regular user (and adding them to the
wheel
group so they can gain root privileges) - in this case, I'll call the user
blog
. Also, enable the installation of binary packages, as it will be convenient later to use
pkgin
to install and update all necessary packages. All these steps are described clearly and in detail in the
guide
, so I won't detail them here. But they are simple and logical, like all operations on BSD systems.
After installation, reboot. If everything went correctly, you should be able to log in via console or SSH using the "blog" user (or whatever you named it).
First, I suggest configuring the IPv6 address and installing the necessary packages.
For IPv6, in the case of netcup, simply add one of the assigned addresses to the interface. In NetBSD,
network interface configurations are stored (similar to OpenBSD) in specific files
. For the first virtio interface, the file will be
/etc/ifconfig.vioif0
.
You need to elevate your privileges to root, open that file with your preferred editor, and add the configuration to the file itself:
nb1euro$ su -l
nb1euro# vi /etc/ifconfig.vioif0

inet6 your-ipv6-addr/64
up
To test everything, perform a reboot and try pinging an IPv6 address (I often use
ping6 google.com
).
If all goes well, after a few seconds, you should see ping replies, confirming everything is configured correctly.
Regarding packages, the only two strictly necessary ones are
bash
and a markdown processor (by default, BSSG will use
commonmark
; otherwise, it can be configured to use
pandoc
or
Markdown.pl
).
rsync
can be useful for deployment.
sudo
(or
doas
) can be useful for elevating privileges for certain operations, at least at this stage.
nb1euro$ su -l
nb1euro# pkgin in bash cmark rsync sudo
If you're used to Linux, you can also install the "nano" editor:
nb1euro# pkgin in nano
If
sudo
was installed, it's now appropriate to grant users in the "wheel" group (like the regular user created during installation) the ability to elevate privileges. Edit the
sudoers
file (I suggest using the
visudo
command) and uncomment this line:
## Uncomment to allow members of group wheel to execute any command
%wheel ALL=(ALL:ALL) ALL
At this point, you can switch back to operating as the regular user, downloading and unpacking BSSG:
nb1euro$ ftp https://brew.bsd.cafe/stefano/BSSG/archive/0.15.1.tar.gz
nb1euro$ tar zxfv 0.15.1.tar.gz
Now that BSSG is ready, just initialize a directory with the structure for the new site:
nb1euro$ cd bssg
nb1euro$ ./bssg.sh init /home/blog/myblog
Everything is set to start generating your blog. I recommend reading BSSG's
README.md
. There are many options, themes, etc., but to get started, you just need to set the site's public URL. For example, if the site will be published as
myblog.example.com
- just create a file at
/home/blog/myblog/config.sh.local
(the path defined by the init command) and set the public URL:
SITE_URL="https://myblog.example.com"
This way, all URLs will be absolute URLs, which is necessary to ensure the correct functioning of RSS feeds, sitemaps, etc. This setting assumes HTTPS - if you just want to test the site over HTTP, simply use
http
and then, optionally, change it to
https
and regenerate the site later.
You can already create your first test post, directly from the BSSG directory:
nb1euro$ ./bssg.sh post
The system will use
nano
if it's installed, otherwise it will use
vi
. Don't worry, in the latter case, BSSG will write the procedure for exiting
vi
as the post's text 🙂
Once you save the post, BSSG will automatically generate the site. If everything went well, the
/home/blog/myblog/output
directory will contain the final result. We are therefore ready for the first deployment, which can be done in many different ways. I will cover three:
Using
bozohttpd
, present
by default in NetBSD's base system
. It can be used via
inetd
(launching an httpd process for each connection) or as a daemon. I'll describe the first option, showing in the final benchmarks how, even when used as a daemon, it remains a less performant solution.
Using nginx
Using Caddy
First, it's advisable to obtain a certificate to configure and use HTTPS. If you only want to test using HTTP, this part can be safely bypassed. For solutions 1 and 2, I'll use
certbot
, which is well-known to many users with Linux experience. Caddy, on the other hand, manages certificates automatically, so there's no need for other solutions and thus no need to install
certbot
.
nb1euro$ sudo pkgin in py313-certbot
To use
bozohttpd
, no further installation is necessary. At this point, the options diverge.
Using NetBSD's Integrated httpd
bozohttpd
is integrated into NetBSD and, by default, can be launched directly via
inetd
. This solution, while not extremely efficient or scalable, is simple and requires few resources. It's fine if you expect only a few visits per day, but when used via
inetd
, the initial latency for each connection is tangible. It can still be useful for some tests or small deployments.
The
/etc/inetd.conf
file already contains the options to handle this situation:
#http           stream  tcp     nowait:600      _httpd  /usr/libexec/httpd      httpd /var/www
#http           stream  tcp6    nowait:600      _httpd  /usr/libexec/httpd      httpd /var/www
By uncommenting these two lines and restarting
inetd
(
service inetd restart
), the server will start responding to HTTP requests on both IPv4 and IPv6.
If you want to add HTTPS support, no problem. Just request a certificate via
certbot
and specify the webroot.
Run:
nb1euro$ sudo certbot-3.13 certonly
Choose option 2 - the one where you specify the webroot - enter the domain, and when prompted, provide
/var/www/
as the webroot.
The certificate will be created. Then, modify the
/etc/inetd.conf
file to also include support for HTTPS, adding two lines similar to these (obviously, change the certificate paths):
https            stream  tcp     nowait:600      _httpd  /usr/libexec/httpd      httpd -Z /usr/pkg/etc/letsencrypt/live/myblog.example.com/fullchain.pem /usr/pkg/etc/letsencrypt/live/myblog.example.com/privkey.pem /var/www
https            stream  tcp6    nowait:600      _httpd  /usr/libexec/httpd      httpd -Z /usr/pkg/etc/letsencrypt/live/myblog.example.com/fullchain.pem /usr/pkg/etc/letsencrypt/live/myblog.example.com/privkey.pem /var/www
Warning
:
httpd
will run with the permissions of the
_httpd
user, so make sure all certificates are readable by that user:
nb1euro# chown -R _httpd /usr/pkg/etc/letsencrypt/
Restart
inetd
, and the server will also respond over HTTPS.
To make your blog public, simply copy the files from the site's output directory to
/var/www/
- this time using
sudo
to bypass permission issues:
nb1euro$ sudo rsync -avhHPx /home/blog/myblog/output/ /var/www/
The site will be immediately visible.
Using nginx
Nginx is fast and efficient, and the performance difference is noticeable (some benchmarks follow below). For an efficient setup ready for a high number of visits, it's advisable to use a web server suited for the purpose, just like nginx.
First, install nginx and the certbot plugin for nginx. This will simplify the installation and renewal of certificates:
nb1euro$ sudo pkgin in py313-certbot-nginx nginx
Copy the startup script to
/etc/rc.d
- as indicated by the post-installation message. In NetBSD, this operation must be done manually, but it's always pointed out:
nb1euro$ sudo cp /usr/pkg/share/examples/rc.d/nginx /etc/rc.d
Warning
: If you previously used
httpd
from
inetd
following the previous solution, you must disable it in
inetd.conf
and restart
inetd
to free up ports 80 and 443.
Now you can create a virtual host for our new site.
nb1euro$ sudo vi /usr/pkg/etc/nginx/nginx.conf
and add, at the end of the file and before the final closing curly brace:
server {
        listen 80;
        # If you also have configured IPv6 support
        listen [::]:80;

        root /var/www;
        index index.html index.htm;

        server_name myblog.example.com;

        # If you want a long cache for media and css - be careful, this means that if you change to a new theme, it might not be visible immediately as the browser might still use the old cached one
        location ~* \.(jpg|jpeg|png|gif|ico|css|js)$ {
            expires 30d;
            add_header Cache-Control "public, no-transform";
        }

        location / {
                try_files $uri $uri/ =404;
        }
}
Now, it's time to configure the system to enable nginx. Just edit
/etc/rc.conf
:
nb1euro$ sudo vi /etc/rc.conf
and add:
nginx=YES
Now, you can start nginx:
nb1euro$ sudo service nginx start
Nginx will start listening on port 80. Generating and installing the certificate is very simple:
nb1euro$ sudo certbot-3.13 --nginx -d myblog.example.com
This command will request the certificate and install it, so nginx will already be configured to use it.
As with the previous method, to make your blog public, simply copy the files from the site's output directory to
/var/www/
- using
sudo
to bypass permission issues:
nb1euro$ sudo rsync -avhHPx /home/blog/myblog/output/ /var/www/
The site will be immediately visible.
Using Caddy
Caddy is a convenient and all-in-one solution, efficient and fast. It's packaged for NetBSD and allows you to go online in a flash. I won't delve into the configuration because there are many tutorials (
including the official ones
), but you just need to install it and run it:
nb1euro$ sudo pkgin in caddy
Once installed, go to the directory you want to serve (e.g.,
/var/www
or directly
/home/blog/myblog/output
) and run:
nb1euro$ sudo caddy file-server --domain myblog.example.com
Caddy will start, request the certificate, and begin serving your blog over HTTPS as well. To install Caddy as a service (i.e., with a configuration file, etc.), you can proceed similarly to how it's done on Linux. The NetBSD Caddy package doesn't include the
rc.d
script, but you can copy and paste one (into
/etc/rc.d/caddy
) from
a thread posted on UnitedBSD
.
Performance Comparison
I performed some performance tests on these solutions. Here are the results, on a single-core 1 euro/month VPS, from my home connection (which also has its own limitations):
Running 10s test @ https://myblog.example.com/
  4 threads and 50 connections
  Thread Stats   Avg      Stdev     Max   +/- Stdev
    Latency   213.52ms  173.10ms   1.11s    76.01%
    Req/Sec    12.92      9.19    50.00     75.91%
  371 requests in 10.10s, 1.39MB read
Requests/sec:     36.72
Transfer/sec:    140.65KB
These numbers are quite poor, linked to high latency caused by having to launch
bozohttpd
for each incoming connection.
NetBSD httpd as a daemon:
Running 10s test @ https://myblog.example.com/
  4 threads and 50 connections
  Thread Stats   Avg      Stdev     Max   +/- Stdev
    Latency    35.74ms    6.96ms 108.80ms   81.36%
    Req/Sec    18.29      9.45    50.00     70.88%
  676 requests in 10.10s, 2.53MB read
Requests/sec:     66.92
Transfer/sec:    256.32KB
Here the situation is decidedly better, but not exceptional.
httpd
isn't designed for high loads or performance.
Nginx as a daemon, 1 worker:
Running 10s test @ https://myblog.example.com/
  4 threads and 50 connections
  Thread Stats   Avg      Stdev     Max   +/- Stdev
    Latency    30.69ms    4.87ms  64.14ms   66.01%
    Req/Sec   379.39     65.94   464.00     90.91%
  15026 requests in 10.04s, 56.50MB read
Requests/sec:   1496.65
Transfer/sec:      5.63MB
Here we are on another level, showing truly solid performance. This type of result can handle significantly high loads without particular difficulty. The efficiency of both NetBSD and nginx pays off.
Running 10s test @ https://myblog.example.net/
  4 threads and 50 connections
  Thread Stats   Avg      Stdev     Max   +/- Stdev
    Latency    32.10ms    5.75ms  95.04ms   87.44%
    Req/Sec   362.74     64.29   434.00     91.67%
  14374 requests in 10.05s, 54.63MB read
Requests/sec:   1430.82
Transfer/sec:      5.44MB
Caddy shows results comparable to nginx, so the choice between them depends solely on the type of configuration you want to achieve and the experience each person has with the specific platforms.
Conclusion: Efficient Minimalism
We've seen how it's possible to create a personal, professional, and performant online presence with minimal investment. This solution, based on NetBSD and a 1€/month VPS, offers several advantages:
Negligible Cost
: For 12€ per year, you can have a website (and more!) completely under your control.
Surprising Performance
: As demonstrated by the benchmarks, excellent performance can be achieved even with limited resources (up to 1400-1500 requests/second with nginx or Caddy).
Security and Stability
: NetBSD is renowned for its reliability and security, fundamental characteristics for any online service.
Total Control
: Unlike free blogging platforms, you have full control over every aspect of your site.
Learning Experience
: Managing a BSD system allows you to acquire valuable system administration skills.
This minimalist configuration demonstrates that you don't need to invest in expensive cloud solutions or oversized VPS to have a quality online presence. In an era where the tendency is to think "moooar powaaaar = better results", NetBSD reminds us that efficiency and good design can yield excellent results even with limited resources.
After all, you don't need a thousand-node cloud to write something worth reading.
In the upcoming articles in this series, we will explore how to expand this basic installation with other useful services and how to keep the system updated and secure over time.
