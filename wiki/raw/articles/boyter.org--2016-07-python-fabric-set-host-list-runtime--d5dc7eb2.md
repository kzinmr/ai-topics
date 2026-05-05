---
title: "Python Fabric Set Host List at Runtime"
url: "https://boyter.org/2016/07/python-fabric-set-host-list-runtime/"
fetched_at: 2026-05-05T07:02:01.162833+00:00
source: "Ben Boyter"
tags: [blog, raw]
---

# Python Fabric Set Host List at Runtime

Source: https://boyter.org/2016/07/python-fabric-set-host-list-runtime/

With the advent of cloud computing where you spin up and tear down servers at will it becomes extremely useful to pick the hosts you want fabric to run on at runtime rather then through the usual env.hosts setting. This allows you to query your servers through your cloud providers API without having to maintain a list. This can be a more powerful and flexible technique then using roles and in a devops world can save you a lot of time.
The trick is to know that when fabric runs any outgoing SSH connection is only made when the first put/get/sudo/run command is made. This means you can change env.hosts before this time and target whatever machines you want.
For the example below we are going to run a command on all of our servers after getting a full IP list from our fictitious cloud provider through an API call using the excellent Python requests module.
Firstly lets define a task which will set our env.hosts to all of the servers in our cloud.
def all():
    req = requests.get('https://api.mycloud.com/v1/server/list', headers={ 'API-Key': 'MYAPIKEY' });
    serverlist = json.loads(req.text)

    if len(serverlist) == 0:
        evn.hosts = []
        return

    env.hosts = [server['public_ip'] for server in serverlist]
The above makes a HTTPS call using our API Key and loads the JSON response into an object. Then depending on if any servers exist or not we loop through pulling out the public ip address for all our servers and assign that to our environment hosts.
Now we can call it with a simple uname function to get the output for all of the servers inside our cloud.
$ fab all hostname
[box1] run: uname -s
[box1] out: box1
[box2] run: uname -s
[box2] out: box2

Done.
Disconnecting from box1... done.
Disconnecting from box2... done.
You can create individual tasks for each group of servers you control using this technique but that’s not very dry (don’t repeat yourself) or neat. Lets modify our all task to accept a parameter so we can filter down our servers at run time.
def all(server_filter=None):
    req = requests.get('https://api.mycloud.com/v1/server/list', headers={ 'API-Key': 'MYAPIKEY' });
    serverlist = json.loads(req.text)

    if len(serverlist) == 0:
        evn.hosts = []
        return
    
    if filter:
        env.hosts = [server['public_ip'] for server in serverlist if server['tag'] == server_filter]
    else:
        env.hosts = [server['public_ip'] for server in serverlist]
We changed our method to accept a parameter which is by default set to none which we can use to filter down our servers based on a tag. If your cloud providers API is sufficiently powerful you can even change the request itself to handle this use case and save yourself the effort of filtering after the return.
To call our new method you need to pass the filter like the following example.
$ fab all:linux hostname
[box1] run: uname -s
[box1] out: box1
[box2] run: uname -s
[box2] out: box2

Done.
Disconnecting from box1... done.
Disconnecting from box2... done.
BTW I am writing a book about how to
Automate your life using Python Fabric
click the link and register your interest for when it is released.
