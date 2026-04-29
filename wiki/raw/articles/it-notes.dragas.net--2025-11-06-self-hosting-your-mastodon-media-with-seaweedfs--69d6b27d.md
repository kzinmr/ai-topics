---
title: "Self-hosting your Mastodon media with SeaweedFS"
url: "https://it-notes.dragas.net/2025/11/06/self-hosting-your-mastodon-media-with-seaweedfs/"
fetched_at: 2026-04-29T07:02:10.515550+00:00
source: "it-notes.dragas.net"
tags: [blog, raw]
---

# Self-hosting your Mastodon media with SeaweedFS

Source: https://it-notes.dragas.net/2025/11/06/self-hosting-your-mastodon-media-with-seaweedfs/

Mastodon
4.5.0 is here, and with it come some interesting changes that, in my opinion, might encourage more people to consider it for self-hosting their Fediverse community.
While it may not be as lightweight and simple as other solutions (like
snac
or
GoToSocial
or many others), I believe it remains one of the best platforms for managing a medium-sized Fediverse community, thanks in part to the direct feedback that many admins have provided to the developers.
I have previously written about how to
install Mastodon in a FreeBSD jail
and how to
modify its character and poll limits
.
One of the most critical initial decisions (which can be changed later, but with extra work) is where to store your media files. Mastodon downloads and re-processes all media it encounters from other instances for three main reasons:
Local Caching:
Your users connect to your media server, reducing the load on the original instance.
Security:
Re-processing media helps to remove any potential "impurities" before they reach the user's device.
Privacy:
It prevents disclosing your users' IP addresses to other instances. A user will only connect to their own instance to fetch all data, including remote content.
At least initially, media files will be the largest part of your instance's storage footprint. It is therefore essential to plan where to store them and to add a regular cleanup script; otherwise, their growth will be exponential.
Mastodon supports uploading media to external S3-compatible solutions, and many admins use the usual commercial providers, paying for data uploads and transfers.
I am a firm believer in "Own Your Data", so I have always used my own self-hosted S3 servers. I initially started with Minio, but over time, I realized that, by design, it doesn't perform well with a multitude of small files (performance degrades). After running some tests, I decided to switch to
SeaweedFS
.
SeaweedFS "is a fast distributed storage system for blobs, objects, files, and data lake, for billions of files! Blob store has O(1) disk seek..." - this, combined with the fact that it is a mature and proven piece of software, was enough for me to give it a try. The result? Excellent. The I/O and CPU load on my media server dropped drastically, making SeaweedFS an incredibly suitable solution. Furthermore, some of its features (like the ability to run a
filer.sync
) allow for efficient and fast replication to other storage, another host, or... anything else.
SeaweedFS works perfectly with Mastodon, and I will explain the steps to get it into production.
I will install SeaweedFS in a dedicated jail and use a dedicated subdomain. This ensures that the media server can be moved to another host at any time without reconfiguring everything or changing domains. SeaweedFS has its own FreeBSD package, installable via
pkg
, or can be downloaded directly from the project's website.
In either case, I will describe a "test" setup - which can also be used in production without issues. However, I highly recommend diving deeper into the tool, as it is incredibly powerful and flexible and can solve many more problems than one might imagine.
Setting up the SeaweedFS Jail
First, let's create a dedicated jail with BastilleBSD:
bastille create media 14.3-RELEASE 10.0.0.66 bastille0
Now, let's enter the jail and install SeaweedFS (and tmux, which can be useful):
bastille console media
pkg install -y tmux seaweedfs
I suggest launching SeaweedFS in a tmux session so you can monitor its output. Later, you should configure an automatic startup method, such as using the included rc.d file or any other method you prefer.
Create a directory for the data and start SeaweedFS as the "seaweedfs" user:
mkdir -p /seaweedfs/data
chown -R seaweedfs /seaweedfs
su -m seaweedfs
cd /seaweedfs/
/usr/local/bin/weed server -dir /seaweedfs/data -s3
At this point, SeaweedFS will start and create everything it needs to function, including the S3 server.
Configuring Buckets and Users
Now, let's open the weed shell to create the necessary bucket and users:
weed shell
s3.bucket.create -name mastomedia
Still in the weed shell, create a user for Mastodon and grant read permissions for unauthenticated users (which is necessary to serve media to the world):
s3.configure -access_key=mastomedia -secret_key=CHANGEME -buckets=mastomedia -user=mastodon -actions=Read,Write,List,Tagging,Admin -apply
s3.configure -buckets=mastomedia -user=anonymous -actions=Read -apply
s3.configure -buckets=mastomedia -actions=Read -apply
Security Tip:
For the
-secret_key
, avoid using a simple password. You can generate a strong, random key directly from your shell with a command like
openssl rand -base64 32
.
Done. SeaweedFS is now ready to receive (and serve) media. The next step is to set up a reverse proxy to serve everything over HTTPS. My preferred approach is to configure the system as if it were external, even if the services are in adjacent jails. This might use slightly more resources, but the time and trouble it saves in the future are well worth it.
Nginx Reverse Proxy Configuration
The reverse proxy can be configured something like this:
[...]

server {
   server_name  media.mastodon.example.com;

   ignore_invalid_headers off;
   client_max_body_size 0; # Allow large file uploads without Nginx limits

   location / {
      proxy_set_header Host $http_host;
      proxy_set_header X-Real-IP $remote_addr;
      proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
      proxy_set_header X-Forwarded-Proto $scheme;

      proxy_connect_timeout 300;
      proxy_http_version 1.1;
      proxy_set_header Connection "";
      chunked_transfer_encoding off;

      expires 1y;
      add_header Cache-Control public;

      add_header X-Cache-Status $upstream_cache_status;
      add_header X-Content-Type-Options nosniff;

      proxy_pass http://10.0.0.66:8333;
   }

# ... other server configurations like SSL ...

}
Mastodon Configuration
Now let's configure Mastodon. If you are running the setup wizard for the first time, here is a summary of the options:
[...]
Do you want to store uploaded files on the cloud? yes
Provider Minio
Minio endpoint URL: https://media.mastodon.example.com
Minio bucket name: mastomedia
Minio access key: mastomedia
Minio secret key: CHANGEME
Do you want to access the uploaded files from your own domain? Yes
Domain for uploaded files: media.mastodon.example.com
If Mastodon is already active, or once the setup is complete, the options in your .env.prod file should be modified to be consistent with what SeaweedFS expects:
S3_ENABLED=true
S3_PROTOCOL=https
S3_REGION=us-east-1
S3_ENDPOINT=https://media.mastodon.example.com
S3_HOSTNAME=media.mastodon.example.com
S3_BUCKET=mastomedia
AWS_ACCESS_KEY_ID=mastomedia
AWS_SECRET_ACCESS_KEY=CHANGEME
S3_FORCE_SINGLE_REQUEST=true
# remove the S3_ALIAS_HOST if it is set
IMPORTANT NOTE:
If both services are in jails on the same host (i.e., SeaweedFS is on the same host as Mastodon), you should ensure that the Mastodon jail can reach the SeaweedFS jail through the reverse proxy and not via the external IP. To do this, add the following line to the /etc/hosts file of the
Mastodon jail
:
10.0.0.1        media.mastodon.example.com
In this example, the reverse proxy is at 10.0.0.1. If you are not using a separate reverse proxy but are exposing Nginx directly from the jail (as described in my Mastodon installation article), use the IP of the Mastodon jail itself instead (e.g., 10.0.0.42).
With this setup, Mastodon will be able to upload media to the SeaweedFS server and generate the correct links for other instances, public visitors, and users of your own instance.
Have fun with SeaweedFS!
