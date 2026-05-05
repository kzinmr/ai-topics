---
title: "Python Fabric: Getting File from Host as String"
url: "https://boyter.org/2016/08/python-fabric-file-host-string/"
fetched_at: 2026-05-05T07:02:00.839458+00:00
source: "Ben Boyter"
tags: [blog, raw]
---

# Python Fabric: Getting File from Host as String

Source: https://boyter.org/2016/08/python-fabric-file-host-string/

Python Fabric: Getting File from Host as String
2016/08/01
(158 words)
When using fabric for deployments you will sometimes want check an existing file for the presence of a value before applying an update. A common example I run into is checking if an apt-source has already been added before adding it again. This is a little clunky in fabric, but thankfully you can write a simple helper which takes case of it for you.
def
_get_remote
(fileloc):
'''Pulls back a file contents from connection as string'''
from
StringIO
import
StringIO
fd
=
StringIO()
get(fileloc, fd)
content
=
fd
.
getvalue()
return
content
Usage is fairly simple. Say we want to install the latest version of Varnish Cache on an Ubuntu server. Usage like so works,
<
if
'https://repo.varnish-cache.org/ubuntu/ trusty varnish-4.0'
not
in
_get_remote(
'/etc/apt/sources.list.d/varnish-cache.list'
):
sudo(
'curl https://repo.varnish-cache.org/ubuntu/GPG-key.txt | sudo apt-key add -'
)
sudo(
'''sudo sh -c 'echo "deb https://repo.varnish-cache.org/ubuntu/ trusty varnish-4.0" &gt;&gt; /etc/apt/sources.list.d/varnish-cache.list' '''
)
sudo(
'apt-get -y update'
)
At this point you should be able to install the latest version of varnish with a simple apt-get.
