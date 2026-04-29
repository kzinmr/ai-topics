---
title: "Don't use localhost:3000, use your own custom domain"
url: "https://idiallo.com/blog/say-no-to-localhost3000-use-custom-domains?src=feed"
fetched_at: 2026-04-29T07:00:53.154886+00:00
source: "idiallo.com"
tags: [blog, raw]
---

# Don't use localhost:3000, use your own custom domain

Source: https://idiallo.com/blog/say-no-to-localhost3000-use-custom-domains?src=feed

After presenting a demo of how an internal tool works, I was flooded with questions. Not about the tool, but about why I had bought a domain just to run the demo. "Why didn't you use the staging server?" they asked.
I was confused. I didn't buy a domain. I was running it locally.
But instead of the URL being
localhost:3002
, it was a fully formed domain.
www.internaltool.com
. In fact, some people told me that they couldn't access the website on their devices. They thought I had to whitelist their IP to grant them access. To feel young again...
Setting up a custom domain locally was common practice when I started web programming. But with the advent of Node.js (and rails?), everyone has resorted to just pointing to
localhost
with an incrementing port number. The main reason is that the webserver is often bundled into the application itself. It’s easy to just run
npm start
and call it a day.
However, if you have multiple long-term projects running locally, especially if they need to communicate with one another, then managing a mental map of ports like
3000
,
8080
, and
5173
quickly gets tiring. This is where my old school approach shines.
By combining the system hosts file with a reverse proxy like Nginx, you can run different projects locally with actual domain names. I usually end up with
dev.domain.com
for active development,
qa.domain.com
for a stable local build, and the actual production URL for the live site.
Here is how to set it up.
Step 1: The Hosts File
First, we need to tell your computer where to find these domains.
Think of
/etc/hosts
as your computer's personal contact list. When you type a URL, your computer looks here first. By adding an entry, you are telling your computer: "Don't bother checking the internet when I ask for myproject.com, I am actually talking about this machine." It creates a manual override that maps a friendly name directly to your machine's IP address.
You can edit the file here:
Linux/macOS:
/etc/hosts
Windows:
C:\Windows\System32\Drivers\etc\hosts
Open the file in your editor. In this file, right after the block of entries for Adobe (active.adobe.com...), add this line:
127.0.0.1 myproject.com
127.0.0.1 dev.myproject.com
Now, when you access those domains in your browser, they don't point to the wider internet, but directly to your own machine.
Step 2: Nginx Configuration
Now that the domain is pointed to your own machine, we want to redirect it to the right application. If your app runs on port
3000
, navigating to
myproject.com
will default to port
80
and fail. This is where Nginx comes in. It listens on port
80
and forwards the traffic to the specific port your app is running on.
Here is a simplified Nginx config to make it work:
server {
    listen 80;
    server_name myproject.com;

    location / {
        proxy_pass http://localhost:3000;
        proxy_set_header Host $host;
    }
}

server {
    listen 80;
    server_name dev.myproject.com;

    location / {
        proxy_pass http://localhost:3001;
        proxy_set_header Host $host;
    }
}
Restart Nginx, and voilà! You have clean, professional URLs for your local environment.
A Note for WSL2 Users
If you are running your services inside Windows Subsystem for Linux (WSL2), networking is handled a little differently because the Linux instance has its own virtual IP. You can get your instance's IP address with this command:
wsl hostname -I
# Output: 172.x.x.x
You would use that IP address in your Windows hosts file instead of
127.0.0.1
.
Conclusion
After that demo, some people were disappointed to learn the
/etc/hosts
trick. They thought I was so committed that I had bought a domain name just to give them the raw deal with my demo. Someone mused about a shirt with the words "real men don't use localhost:3000". That could have started a whole new motivational speaking career for me. A custom domain just looks very professional and is practical for separating environments. It just feels cooler than staring at
localhost:3000
all day. That's how you separate yourself from vibe-coders.
Anyway, back to earth. I feel like this is a lost skill and I'm keeping it alive by sharing it. That's how you run a custom URL locally.
