---
title: "Django with SockJS"
url: "https://idea.popcount.org/2012-09-21-django-with-sockjs"
fetched_at: 2026-05-05T07:01:14.410619+00:00
source: "Marek Vavruša (idea.popcount)"
tags: [blog, raw]
---

# Django with SockJS

Source: https://idea.popcount.org/2012-09-21-django-with-sockjs

Django with SockJS
21 September 2012
Few days ago
Peter Bengtsson
wrote an
interesting blog post on
SockJS
:
The article is quite brief, let me try to provide step-by-step
instructions on how to start your first Django on SockJS project.
Python servers
First, it's important to understand that there are many HTTP (okay,
WSGI) servers for Django. SockJS requires pretty deep integration with
the web server, and you will need to use a particular web server with
SockJS support.
Currently there are a number of SockJS libraries that work with
variety of servers (with quality and completeness varying):
I'll focus on
SockJS-tornado
here.  This
means that the
usual Django deployment instructions
will not be fully applicable to our project (as we'll be using
Tornado Web
HTTP server).
In the mentioned article Peter suggested starting two HTTP servers
separately - one for Tornado and one for Django. In this blog post
I'll put Django behind Tornado, so a single Tornado web server will handle
all the requests.
Step 0: Python requirements
We will need few Python packages - Django, Tornado and
SockJS-Tornado. Let's install them into a
virtualenv
environment:
$
mkdir djangosockjs
$
cd
djangosockjs
$
cat > requirements.txt
<< EOF
tornado==2.1.1
sockjs-tornado==0.0.4
django==1.4.1
EOF
$
virtualenv venv
$
./venv/bin/pip install -r requirements.txt
Step 1: New project
Let's create a normal Django project and activate the virtual environment:
$
./venv/bin/django-admin.py startproject project
$
. ./venv/bin/activate
(
venv
)
$
cd
project/project
Step 2: Serving a static file
The Django project will be only a placeholder serving a single static
file, without any logic inside. We only want to prove the usage of
SockJS with Django using the same codebase and HTTP server.
We will serve a static file -
index.html
. You need to update
TEMPLATE_DIRS
in
settings.py
file:
TEMPLATE_DIRS
=
(
'project/templates'
)
Additionally you need to expose the file from
urls.py
:
from
django.conf.urls
import
patterns
,
include
,
url
from
django.views.generic.simple
import
direct_to_template
urlpatterns
=
patterns
(
''
,
url
(
r'^$'
,
direct_to_template
,
{
'template'
:
'index.html'
}),
)
Finally, we need to create the
index.html
file. For simplicity we'll
borrow a very simple code from
SockJS-node examples
.
(
venv
)
$
mkdir templates
(
venv
)
$
cd
templates
(
venv
)
$
wget https://raw.github.com/sockjs/sockjs-node/master/examples/echo/index.html
(
venv
)
$
cd
..
(
venv
)
$
cd
..
Step 3: Tornado code
Our SockJS code will accept any incoming realtime connections and
will echo all the received data. Here's the code for the
project/echosockjs.py
file:
import
sockjs.tornado
class
EchoSockjsConnection
(
sockjs
.
tornado
.
SockJSConnection
):
def
on_open
(
self
,
request
):
print
"sockjs: open"
def
on_message
(
self
,
data
):
print
"data:
%r
"
%
(
data
,)
self
.
send
(
data
)
def
on_close
(
self
):
print
"sockjs: close"
def
EchoSockjsRouter
(
prefix
):
return
sockjs
.
tornado
.
SockJSRouter
(
EchoSockjsConnection
,
prefix
)
.
urls
Step 4: Tornado server
The last file we need to write, is the Tornado web server
wrapper. It will do two things:
it will expose our SockJS endpoint
EchoSockjsConnection
under
/echo
path
it will forward all other requests to normal Django app
The adapted snippet from
bdarnell
will look like:
#!/usr/bin/env python
from
tornado.options
import
options
,
define
import
django.core.handlers.wsgi
import
tornado.httpserver
,
tornado.ioloop
import
tornado.web
,
tornado.wsgi
import
project.echosockjs
define
(
'port'
,
type
=
int
,
default
=
8000
)
wsgi_app
=
tornado
.
wsgi
.
WSGIContainer
(
django
.
core
.
handlers
.
wsgi
.
WSGIHandler
())
tornado_app
=
tornado
.
web
.
Application
(
project
.
echosockjs
.
EchoSockjsRouter
(
'/echo'
)
+
[
(
'.*'
,
tornado
.
web
.
FallbackHandler
,
dict
(
fallback
=
wsgi_app
)),
])
server
=
tornado
.
httpserver
.
HTTPServer
(
tornado_app
)
server
.
listen
(
options
.
port
)
print
"[*] Listening at 0.0.0.0:
%i
"
%
(
options
.
port
,)
tornado
.
ioloop
.
IOLoop
.
instance
()
.
start
()
Put it into a
tornado_main.py
file.
Finito
And to start the server:
(
venv
)
$
chmod +x tornado_main.py
(
venv
)
$ DJANGO_SETTINGS_MODULE
=
project.settings ./tornado_main.py
Finally, visit
http://localhost:8000/
and
see if the echo is indeed working!
The full project is available on github.
If you wish to use this setup on production, you will be able to get
better performance by separating Tornado from Django. Django is
blocking, Tornado is asynchronous, it makes sense to scale them
separately.
