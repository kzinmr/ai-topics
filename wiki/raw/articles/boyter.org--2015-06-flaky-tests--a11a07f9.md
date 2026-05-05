---
title: "Ben E. C. Boyter"
url: "https://boyter.org/2015/06/flaky-tests/"
fetched_at: 2026-05-05T07:02:02.490865+00:00
source: "Ben Boyter"
tags: [blog, raw]
---

# Ben E. C. Boyter

Source: https://boyter.org/2015/06/flaky-tests/

A test is considered flaky or flakey if it if fails occasionally. Generally flaky tests are considered to be a bad thing and should be modified to ensure they work correctly every time. This is because a test that is not trustworthy will be ignored even when indicating real failure.
There are many situations that can cause to become flaky. Integration and acceptance tests are generally the tests in your test suite most likely to become flaky. They generally have more integrations across your software stack and as such there are more things likely to go wrong. We going to go through a few of the main reasons and go through in detail what you can do about a specific one.
The first thing that causes a test to be flaky is when it depends on any external resource. This could include an API call to a third party, accessing a database or interacting with a file on the filesystem. Generally these sorts of interactions work most of the time but on occasion will not. The reasons for these are numerous.
A test making an API call can fail for all sort of reasons. API changes, API limits, API Key rotation, network connectivity, a 3rd party with poor uptime, concurrency issues. All can cause a previously perfect test to fail. I recently was working with some tests for importing tweets into a system using the twitter API. A developer had hard coded a specific search and twitter id into the test. It turned out that twitter can choose to drop tweets from their search index and hence the API at whim. The test became flaky and needed to be refactored to compensate.
Database calls tend to fail for the same reasons. They also can fail because of incorrect dynamic SQL (note if you have this problem you are probably open to SQL injection and should use SQL binds instead!), and errors such as the database missing the expected data.
Tests which interact with the filesystem despite seeming solid can fail at inopportune moments as well. The reasons are many but the first things to look at would be concurrency issues, tests not cleaning up files, read/write permissions and not releasing file locks. Without mocking away the filesystem (which is a solution which can fix these issues and improve performance) these tests can easy become flaky.
Lets go through a concrete example using a test designed to check if a file has been written. I am using a pseudocode language similar to python but the idea’s should be the same for all languages.
Here we have a function which writes a heartbeat file to the temp directory with the current date and time. Its a commonly used pattern for daemons and other background tasks to confirm they are still running.
def
writeheartbeat
():
file
=
open(
'/tmp/website_heartbeat.txt'
,
'w+'
)
file
.
writelines(str(datetime
.
now()))
f
.
close()
Here are some tests which verify that the file is missing and that when the function is called now exists.
def
testheatbeatmissing
():
exists
=
os
.
path
.
isfile(
'/tmp/website_heartbeat.txt'
)
assertFalse(exists)
def
testheatbeatexists
():
writeheartbeat()
exists
=
os
.
path
.
isfile(
'/tmp/website_heartbeat.txt'
)
assertTrue(exists)
The problem with the above is simple. Assuming the tests run in order everything should be fine for the first test run. However on the second run the first test will assume that the heartbeat file will be missing, however as it would have been created from the previous run this test will now begin to fail! Worse still, if the tests run out of order or someone reorganises them such that the second becomes the first it will start to fail every time.
You could fix the above problems so that the file is cleaned up at the end of the test. This however will not cater for the situation where the tests run concurrently. This is an even worse outcome as it will be impossible to replicate using a debugger and hard to catch.
A better way to test this function would be to rewrite it such that it writes to a unique file for every test run and that file is cleaned up by the test. Such a function could be written like so.
def
writeheartbeat
(filelocation
=
'/tmp/website_heartbeat.txt'
):
file
=
open(filelocation,
'w+'
)
file
.
writelines(str(datetime
.
now()))
f
.
close()
By default the test still writes to the same location when called without an argument but now we can write out heartbeat check test to work correctly every time.
def
testheatbeatexists
():
tempfilelocation
=
'/tmp/testheartbeatexits.tmp'
writeheartbeat(tempfilelocation)
exists
=
os
.
path
.
isfile(tempfilelocation)
assertTrue(exists)
os
.
remove(tempfilelocation)
Perfect. Now the test sets itself up correctly, performs the test and cleans up after itself. It should now be able to run concurrently with our other test without issue. As mentioned however for these situations you may want to look into mocking away the filesystem itself as a way to avoid the above issues.
The one thing to keep in mind when testing integrations
“Leave it as you found it.”. This applies to system state, memory, filesystems or the database. If you make a change no matter how small be sure to reverse it. This simple rule will help cut down on flaky tests saving you a lot of time.
