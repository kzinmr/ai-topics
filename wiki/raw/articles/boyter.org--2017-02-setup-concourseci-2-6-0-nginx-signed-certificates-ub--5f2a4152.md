---
title: "Setup up ConcourseCI 2.6.0 behind Nginx with Self Signed Certificates on Ubuntu 16.04"
url: "https://boyter.org/2017/02/setup-concourseci-2-6-0-nginx-signed-certificates-ubuntu-16-04/"
fetched_at: 2026-05-05T07:02:00.316352+00:00
source: "Ben Boyter"
tags: [blog, raw]
---

# Setup up ConcourseCI 2.6.0 behind Nginx with Self Signed Certificates on Ubuntu 16.04

Source: https://boyter.org/2017/02/setup-concourseci-2-6-0-nginx-signed-certificates-ubuntu-16-04/

[Concourse CI][1] is a very nice continuous integration server.
However for installs there are a few gotcha’s you need to keep in mind. Mostly these relate to how TLS/SSL works.
The first is that while it is possible to run concourse inside Docker I found this to cause a lot of issues with workers dying and not recovering. I would suggest installing the binarys on bare machines. When I moved from a docker cluser using Amazon’s ECS to a single t2.large instance not only were builds faster but it was a far more reliable solution.
I am also not going to automate this install, and will leave it as an excercise for you the reader to do this yourself. I would suggest using Python Fabric, or something like Puppet, Ansible or Saltstack to achive this.
Also keep in mind that with this install everything is running on a single instance. If you have need to scale out this is not going to work, but as a way to get started quickly it works pretty well.
Prerequisites are that you have a Ubuntu instance running somewhere. If you want to run the fly execute command you will also need a valid domain name to point at your machine. This is an annoying thing caused by GoLang when using SSL certs. Turns out you cannot set a hostfile entry and use it as such. You can in a insecure non SSL mode but otherwise cannot.
If you are using a virual machine from DigitalOcean/AWS/Vultr or other you will need to add some swap space. I noticed a lot of issues where this was missing. You can do so by running the following commands which will configure your server to have 4G of swap space,
sudo fallocate -l 4G /swapfile
sudo chmod 600 /swapfile
sudo mkswap /swapfile
sudo swapon /swapfile
sudo echo "/swapfile none swap sw 0 0" &gt;&gt; /etc/fstab
We will need to get the concourse binary, and to make it executable. For convenience and to match the concourse documentation lets also rename it to concourse. To do so run the following command.
wget https://github.com/concourse/concourse/releases/download/v2.6.0/concourse_linux_amd64 && mv concourse_linux_amd64 concourse && chmod +x concourse
We now need to generate the keys that concourse requires.
mkdir keys
cd keys

ssh-keygen -t rsa -f tsa_host_key -N '' && ssh-keygen -t rsa -f worker_key -N '' && ssh-keygen -t rsa -f session_signing_key -N '' && cp worker_key.pub authorized_worker_keys
cd ..
The above commands will create a directory called keys and setup all of the keys that concourse 2.6.0 requires.
We can now create some helper scripts which we can use to run concourse easily.
pico concourse.sh

./concourse web \
 --basic-auth-username main \
 --basic-auth-password MySuperPassword \
 --session-signing-key ./keys/session_signing_key \
 --tsa-host-key ./keys/tsa_host_key \
 --tsa-authorized-keys ./keys/authorized_worker_keys \
 --external-url <https://YOURDNSHERE/> \
 --postgres-data-source postgres://concourse:concourse@127.0.0.1/concourse

chmod +x concourse.sh
This script will start running concourse. Keep in mind that the username and password used here are for the main group and as such you should protect them as they have the ability to create additional groups on your concourse instance.
pico worker.sh

./concourse worker \
 --work-dir /opt/concourse/worker \
 --tsa-host 127.0.0.1 \
 --tsa-public-key ./keys/tsa_host_key.pub \
 --tsa-worker-private-key ./keys/worker_key

chmod +x worker.sh
This script will spin up a worker which will communicate with the main concourse instance and do all the building. It can be useful to lower the priority of this command using nice and ionice if you are running on a single core machine.
Now we need to install all of the postgresql packages required,
apt-get update && apt-get install -y postgresql postgresql-contrib
Once this is done we can create the database to be used
sudo -u postgres createdb concourse
Then login to postgresql and create a user to connect to the database
sudo -u postgres psql CREATE USER concourse WITH PASSWORD 'concourse' GRANT ALL PRIVILEGES ON DATABASE "concourse" to concourse \du
We also need to need to edit the pg_hba file allowing us to make the connection,
sudo pico /etc/postgresql/9.5/main/pg_hba.conf
Scroll down and look for the following line,
host all all 127.0.0.1/32 md5
and change the md5 on the end to trust
host all all 127.0.0.1/32 trust
Then save the file and restart postgresql
service postgresql restart
At this point everything we need to run concourse should be there. You will need to setup the concourse scripts we created earlier to run as a service, or just run them in a screen session if you are in a hurry.
What we want to do now is expose it to the big bad internet.
apt-get install nginx
Create a directory using either the domain name you want to use, a desired name or anything if you are going to connect to things using IP addresses.
mkdir -p /etc/nginx/ssl/mydesireddomain.com
Nowe we want to swtich to the directory and setup the self signed TLS/SSL keys.
cd /etc/nginx/ssl/mydesireddomain.com openssl genrsa -des3 -out server.key 1024
Enter whatever you want for the passphrase but remember it!
openssl req -new -key server.key -out server.csr
Enter the passhrase entered. The most important thing here is that when asked for the Common Name or FQDN you need to enter in the desired domain name.
With that done we need to sign the key.
cp server.key server.key.org openssl rsa -in server.key.org -out server.key
Remember to enter the same pass phrase as before. Finally sign they key with an expiry of 9999 days.
openssl x509 -req -days 9999 -in server.csr -signkey server.key -out server.crt
Make a copy of the file server.crt which will be needed for the concourse fly tool to talk to the server if you are using self signed certs.
With that done lets enable the site,
sudo nano /etc/nginx/sites-available/mydesireddomain.com
And enter in the following details,
upstream concourse_app_server {
 server localhost:8080;
 }

server {
 listen 80 default_server;
 rewrite ^ <https://MYIPADDRESSORDOAMIN$request_uri>? permanent;
 }

server {
 listen 443 default_server ssl http2;
 server_name mydesireddomain.com;

ssl on;
 ssl_certificate /etc/nginx/ssl/mydesireddomain.com/server.crt;
 ssl_certificate_key /etc/nginx/ssl/mydesireddomain.com/server.key;

location / {
 proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
 proxy_set_header Host $http_host;
 proxy_redirect off;
 proxy_pass http://concourse_app_server;
 }
 }```

The above nginx config defines an upstream concourse server running on port 8080. It then defines a server listening on port 80 that redirects all traffic to the same server on HTTPS. The last server config defines out site, sets up the keys and forwards everything to the upstream concourse server.

We can now enable it,
sudo ln -s /etc/nginx/sites-available/mydesireddomain.com /etc/nginx/sites-enabled/mydesireddomain.com
rm -f /etc/nginx/sites-available/default
service nginx restart
We need to remove the default file above because nginx will not allow you to have two default servers.
  
At this point everything should be working. You should now be able to connect to your concourse server like so,```fly --target myciserver login --team-name myteamname --concourse-url https://MYIPADDRESSORDOAMIN --ca-cert ca.crt```

Where the file ca.crt exists whereever you are running fly. Everything at this point should work and you can browse to your concourse server.

If you are using the IP address to communicate to your concourse server you have the limitation that you will not be able to run fly execute to upload a task. You can get around this by using a real domain, or running your own DNS to resolve it correctly.

The only bit of homework at this point would be to configure the firewall to disable access to port 8080 so that everything must go though nginx. Enjoy!

 [1]: http://concourse.ci/
