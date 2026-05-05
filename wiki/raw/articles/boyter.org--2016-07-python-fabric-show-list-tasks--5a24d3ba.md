---
title: "Python Fabric How to Show or List All Available Tasks"
url: "https://boyter.org/2016/07/python-fabric-show-list-tasks/"
fetched_at: 2026-05-05T07:02:01.034928+00:00
source: "Ben Boyter"
tags: [blog, raw]
---

# Python Fabric How to Show or List All Available Tasks

Source: https://boyter.org/2016/07/python-fabric-show-list-tasks/

Python Fabric How to Show or List All Available Tasks
2016/07/20
(98 words)
Showing or displaying the available tasks inside a fabric fabfile is one of those things that almost everyone wants to do at some point and usually works out you can just request a task you know will not exist (usually found through a typo). However there is a way to list them built into fabric itself.
The below are all methods which can be used to display the currently defined tasks.
fab -l 
fab -list
fab taskthatdoesnotexist
Try any of the above where a fabfile is located and be presented with a list of all the available tasks.
