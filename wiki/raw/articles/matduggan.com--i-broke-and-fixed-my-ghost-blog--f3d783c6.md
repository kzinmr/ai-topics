---
title: "Untitled"
url: "https://matduggan.com/i-broke-and-fixed-my-ghost-blog/"
fetched_at: 2026-04-28T07:02:35.596351+00:00
source: "matduggan.com"
tags: [blog, raw]
---

# Untitled

Source: https://matduggan.com/i-broke-and-fixed-my-ghost-blog/

Once a month I will pull down the latest docker images for this server and update the site. The Ghost CMS team updates things at a pretty regular pace so I try to not let an update sit for too long.
With this last round I suddenly found myself locked out of my Ghost admin panel. I was pretty confident that I hadn't forgotten my password and when I was looking at the logs, I saw this pretty spooky error.
blog-1               | [2025-10-15 11:36:29] ERROR "GET /ghost/api/admin/users/me/?include=roles" 403 188ms
blog-1               |
blog-1               | Authorization failed
blog-1               |
blog-1               | "Unable to determine the authenticated user or integration. Check that cookies are being passed through if using session authentication."
blog-1               |
blog-1               | Error ID:
blog-1               |     5b3ec250-aa84-11f0-bb51-b7057fc0f6b0
blog-1               |
blog-1               | ----------------------------------------
blog-1               |
blog-1               | NoPermissionError: Authorization failed
blog-1               |     at authorizeAdminApi (/var/lib/ghost/versions/5.130.5/core/server/services/auth/authorize.js:33:25)
blog-1               |     at Layer.handle [as handle_request] (/var/lib/ghost/versions/5.130.5/node_modules/express/lib/router/layer.js:95:5)
blog-1               |     at next (/var/lib/ghost/versions/5.130.5/node_modules/express/lib/router/route.js:149:13)
blog-1               |     at authenticate (/var/lib/ghost/versions/5.130.5/core/server/services/auth/session/middleware.js:55:13)
blog-1               |     at process.processTicksAndRejections (node:internal/process/task_queues:95:5)
blog-1               |
blog-1               | [2025-10-15 11:36:29] ERROR "GET /ghost/api/admin/users/me/?include=roles" 403 13ms
I was surprised by this sudden error, especially when I dumped out the database and confirmed that the hashed password for my Ghost user matched the password I was giving it. If you want to try that, this is the guide I followed:
https://hostarmada.com/tutorials/blog-cms/ghost/how-to-change-the-admin-password-of-your-ghost-blog-if-you-get-locked-out/
Maybe I messed up the Nginx?
So Ghost is a good CMS system, but it can be a little bit slow under load from automated scraping from RSS readers. I want to cache everything that I can with Nginx, so I use Nginx to store a lot of that junk. My configuration is not too terribly clever and has worked up to this point.
map $sent_http_content_type $expires {
      default                    off;
      text/css                   max;
      application/javascript     max;
      ~image/                    max;
  }

  server {
      listen 80;
      listen [::]:80;
      server_name matduggan.com www.matduggan.com;
      return 301 https://$server_name$request_uri;  # Changed to 301 (permanent)
  }

  proxy_cache_path /tmp/cache levels=1:2 keys_zone=STATIC:512m inactive=24h max_size=10g;
  client_max_body_size 1000M;

  server {
      listen 443 ssl http2;
      listen [::]:443 ssl http2;

      server_name matduggan.com www.matduggan.com;

      charset UTF-8;

      # SSL Configuration
      ssl_certificate         /etc/ssl/cert.pem;
      ssl_certificate_key     /etc/ssl/key.pem;
      ssl_client_certificate  /etc/ssl/cloudflare.crt;
      ssl_verify_client on;

      # Modern TLS settings
      ssl_protocols TLSv1.2 TLSv1.3;
      ssl_prefer_server_ciphers off;  # Let client choose (better for TLS 1.3)
      ssl_session_cache shared:SSL:10m;
      ssl_session_timeout 10m;
      ssl_buffer_size 4k;

      # Security headers
      add_header Strict-Transport-Security "max-age=63072000; includeSubDomains; preload" always;
      add_header X-Frame-Options "SAMEORIGIN" always;
      add_header X-Content-Type-Options "nosniff" always;
      add_header X-XSS-Protection "1; mode=block" always;

      # Compression
      gzip on;
      gzip_vary on;
      gzip_proxied any;
      gzip_comp_level 6;
      gzip_types text/plain text/css text/xml text/javascript application/json application/javascript application/xml+rss application/rss+xml font/truetype font/opentype
  application/vnd.ms-fontobject image/svg+xml;

      expires $expires;

      # Ghost admin and protected routes - no caching
      location ~ ^/(ghost/|p/|\.ghost/|members/) {
          proxy_set_header Host $http_host;
          proxy_set_header X-Real-IP $remote_addr;
          proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
          proxy_set_header X-Forwarded-Proto $scheme;
          proxy_set_header X-Forwarded-Host $http_host;
          proxy_buffering off;
          proxy_cache_bypass 1;
          proxy_no_cache 1;
          add_header Cache-Control "no-cache, no-store, must-revalidate";
          proxy_pass http://127.0.0.1:8080;
      }

      # Public content - cached
      location / {
          proxy_set_header Host $http_host;
          proxy_set_header X-Real-IP $remote_addr;
          proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
          proxy_set_header X-Forwarded-Proto $scheme;

          proxy_buffering on;
          proxy_cache STATIC;
          proxy_cache_valid 200 1d;
          proxy_cache_use_stale error timeout invalid_header updating http_500 http_502 http_503 http_504;
          proxy_cache_bypass $http_cache_control;

          add_header X-Cache-Status $upstream_cache_status;

          proxy_pass http://127.0.0.1:8080;
          proxy_redirect off;
      }
  }
The basic point is to get caching on the public content and then definitely NOT cache the ghost admin panel. After some testing, I confirmed this seemed to all work. But I was still locked out.
To the changelog!
Alright so I still couldn't figure out what was going on, so I went through the docs. Then I found this seemingly new addition.
https://docs.ghost.org/config?_ga=2.92846045.1713439663.1760543217-1048546310.1760543217#security
Now I have transactional email set up, but just looking at the error it seemed to feel related. So I added:
security__staffDeviceVerification: false
to my docker-compose file to disable this new feature and then blamo, suddenly works fine.
So if you are locked out of your Docker CMS admin panel, disable this (temporarily hopefully because it's a good feature) to let you continue to log in, debug your transactional email and then turn it back on. Hope that helps.
