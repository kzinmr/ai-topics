---
title: "searchcode next | Ben E. C. Boyter"
url: "https://boyter.org/2014/06/searchcode/"
fetched_at: 2026-05-05T07:02:03.349676+00:00
source: "Ben Boyter"
tags: [blog, raw]
---

# searchcode next | Ben E. C. Boyter

Source: https://boyter.org/2014/06/searchcode/

There seems to be a general trend with calling the new release of your search engine next (see
Iconfinder
and
DuckDuckGo
), and so I am happy to announce and write about
searchcode next
.
As with many project searchcode has some very humble beginnings. It originally started out as a “I need to do something” side project originally just indexing programming documentation. Time passed and the idea eventually evolved into a search engine for all programming documentation, and then with Google Code search being shut down a code search engine as well.
searchcode was running on a basic LAMP stack. Ubuntu Linux as the server, PHP, MySQL and Apache. APC Cache was installed to speed up PHP with some memcached calls to take heat off the database. The CodeIgniter PHP framework was used for the front end design with a lot of back-end processes written in Python.
Never one to agree with the advice that you should never rewrite your code I did exactly that. Searchcode is now a Django application. The reasons for this are varied but essentially it was running on an older server (Ubuntu 10.04) and a now defunct web framework CodeIgniter. I figured since I had to rewrite portions anyway I may as well switch over to a language that I prefer and want to gain more experience in.
As mentioned searchcode is now a
Django
application but still backed by by
MySQL
.
Sphinx
provides the searching index and a healthy mix of
Rabbitmq
and
Celery
for back-end tasks. Deployments and server config is automated through the use of
Fabric
and
Memcached
is included for speed. Of course some of the original back-end processes still exist as cron jobs but are slowly being moved over to Celery tasks. It still runs on Ubuntu server since that’s the Linux distribution I am most comfortable with.
Of particular note, searchcode runs on two servers which could probably be reduced to a single one at its current size but allows for growth. Both are dedicated boxes provided by Hetzner. Both are 4 core i7 boxes with 3 terabytes of disk space each. The only difference between them is the first having 16 gigabytes of ram and the index having 32 gigabytes. The first runs the web-server nginx talking through gunicorn to django, the database and memcache. The second exclusively runs the sphinx index (more details about sphinx to come).
Load averages before the move were rather chaotic. I had seen spikes up to 100 which for a 4 core box is pretty horrible. The new version even under extreme pressure (from a Siege test and GoogleBot) maxes out about 2, with the search spiking to 4 for brief periods if a lot of un-cached searches hit all of a sudden. The other advantage is that searches come back much faster with the new setup. Average page responses have dropped considerably.
Heavily unit tested the application runs through a battery of tests before each deployment including unit, integration and smoke which do a reasonable job of catching issues out before being deployed. Of course the other benefit being that the code-base is testable which is generally a good thing.
There is more to come and I am excited about the future of searchcode.
