---
title: "Monitor your devices with LibreNMS on FreeBSD"
url: "https://it-notes.dragas.net/2026/05/07/monitor-your-services-with-librenms-on-freebsd/"
fetched_at: 2026-05-08T07:01:35.677061+00:00
source: "it-notes.dragas.net"
tags: [blog, raw]
---

# Monitor your devices with LibreNMS on FreeBSD

Source: https://it-notes.dragas.net/2026/05/07/monitor-your-services-with-librenms-on-freebsd/

LibreNMS
has been a faithful companion for years now. It quietly handles the monitoring of my servers, devices, and services without demanding much in return - exactly what you want from a tool whose job is to watch over everything else. It's a solid alternative to heavier solutions like Zabbix, and it gives you alerts, data, and graphs on virtually anything reachable over SNMP.
I usually install it on a host that is
not
reachable from the outside, then let it poll all the devices through a VPN: a single observation point, clean perimeter. The ability to create multiple dashboards - and to filter them by user - has also let me give clients a transparent window onto their own servers. Transparency, in my experience, is always the better long-term bet.
Together with
Uptime-Kuma
(and the good old Nagios/Munin pair), LibreNMS lives in a FreeBSD jail on my monitoring servers and just does its job.
This post walks through a plain installation of LibreNMS on FreeBSD: package-based, no reverse proxy, no HTTPS, no fancy hardening. The goal is to get to a working setup you can build on top of.
Assumptions
FreeBSD 15.0-RELEASE, in a jail or on a dedicated VM/host
nginx + php-fpm + MySQL 8.4
LibreNMS installed from the official package — not via
git clone
One note before we start: in this guide I use plain HTTP just to reach the first-time setup. If your LibreNMS instance won't stay confined to a private network or behind a VPN, configuring HTTPS is mandatory, not optional.
Installation
pkg install librenms mysql84-server python3 nginx
LibreNMS currently depends on PHP 8.4. If you want to speed PHP up, install OPcache too:
pkg install php84-opcache
MySQL
Two settings need to be in place
before
MySQL starts for the first time. After the first start they cannot be changed without reinitializing the data directory, so it's worth getting them right now.
cd /usr/local/etc/mysql
cp my.cnf.sample my.cnf
In the
[mysqld]
section, add:
innodb_file_per_table=1
lower_case_table_names=0
Now start MySQL:
service mysql-server enable
service mysql-server start
On a fresh FreeBSD install, the local
root
user can connect to MySQL without a password from the command line. Connect and create the database and user. I'm using
password
here as a placeholder - don't.
mysql
CREATE DATABASE librenms CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;
CREATE USER 'librenms'@'localhost' IDENTIFIED BY 'password';
GRANT ALL PRIVILEGES ON librenms.* TO 'librenms'@'localhost';
exit
php-fpm
Edit
/usr/local/etc/php-fpm.d/www.conf
and adjust the listen directives:
listen = /var/run/php-fpm-librenms.sock
listen.owner = www
listen.group = www
listen.mode = 0660
Then create
php.ini
from the production sample:
cd /usr/local/etc
cp php.ini-production php.ini
And set the timezone in
php.ini
:
date.timezone = Europe/Rome
nginx
Since this jail (or host) is dedicated to LibreNMS, we can rewrite the
server
block in
/usr/local/etc/nginx/nginx.conf
directly:
server {
    listen      80;
    #server_name yourServerName
    root        /usr/local/www/librenms/html;
    index       index.php;

    charset utf-8;
    gzip on;
    gzip_types text/css application/javascript text/javascript application/x-javascript image/svg+xml text/plain text/xsd text/xsl text/xml image/x-icon;

    location / {
        try_files $uri $uri/ /index.php?$query_string;
    }

    location /api/v0 {
        try_files $uri $uri/ /api_v0.php?$query_string;
    }

    location ~ \.php$ {
        fastcgi_split_path_info ^(.+\.php)(/.*)$;
        set $path_info $fastcgi_path_info;
        try_files $fastcgi_script_name =404;
        include fastcgi_params;
        fastcgi_param SERVER_SOFTWARE "";
        fastcgi_param SCRIPT_FILENAME $document_root$fastcgi_script_name;
        fastcgi_param PATH_INFO $path_info;
        fastcgi_index index.php;
        fastcgi_pass unix:/var/run/php-fpm-librenms.sock;
        fastcgi_buffers 256 4k;
        fastcgi_intercept_errors on;
        fastcgi_read_timeout 14400;
    }

    location ~ /\.(?!well-known).* {
        deny all;
    }
}
Now start nginx and php-fpm:
service nginx enable
service nginx start

service php_fpm enable
service php_fpm start
LibreNMS configuration
Copy the default config:
cp /usr/local/www/librenms/config.php.default /usr/local/www/librenms/config.php
Because we installed from the package, this file already has the right commands and paths for FreeBSD - no need to hunt down
mtr
,
fping
,
snmpwalk
and friends one by one.
Create the directory for RRD graphs and set ownership:
mkdir -p /var/db/librenms/rrd
chown -R www:www /var/db/librenms
chmod 775 /var/db/librenms/rrd
Then the
.env
file:
cd /usr/local/www/librenms
cp .env.example .env
chown www .env
Edit
.env
and set at least:
DB_DATABASE
-
librenms
DB_USERNAME
-
librenms
DB_PASSWORD
- the one you actually used (not
password
, please)
Then add this line, which tells LibreNMS we still need to run the web installer:
INSTALL=true
A note on permissions. The official LibreNMS documentation suggests
chown -R www:www
over the entire application tree, but on FreeBSD the package already lays down sane ownership, with
storage/
and
bootstrap/cache/
writable by
www
. There's no reason to widen the rest of the codebase. If
validate.php
complains later about something write-related, the first place to check is:
ls -la /usr/local/www/librenms/storage /usr/local/www/librenms/bootstrap/cache
Now generate the app key as
www
, since the file is owned by
www
:
su -m www -c "php artisan key:generate"
And tighten
.env
:
chmod 600 .env
Refresh the configuration cache:
su -m www -c "lnms config:clear"
su -m www -c "lnms config:cache"
Web installer
Open
http://host/install
and follow the steps. The validation process may fail. Refreshing the cache picks up the values written to
config.php
during the install:
su -m www -c "lnms config:clear"
su -m www -c "lnms config:cache"
When the web installer is done, edit .env again and remove the INSTALL=true line if it's still there. Leaving it in place re-exposes the installer to anyone who can reach the URL.
Polling service
LibreNMS needs something to actually run the polls. On FreeBSD, the package ships an rc service that runs the LibreNMS dispatcher, so there's no need to manage cron entries by hand the way most Linux guides assume.
service librenms enable
service librenms start
Validate
cd /usr/local/www/librenms
su -m www -c './validate.php'
You may see a couple of complaints right after starting the service - usually scheduler-related and self-resolving within a few minutes. Re-run
validate.php
once the dispatcher has had time to settle. Anything still red after that is worth investigating.
Next steps
At this point you can log into the web interface and start adding devices, configuring SNMP, and building dashboards. For that, the
official LibreNMS documentation
is excellent, and there's no point in me paraphrasing it here.
