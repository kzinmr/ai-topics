---
title: "Sandbox resourcing: burst, don't reserve"
url: "https://modal.com/blog/sandbox-bursting"
fetched_at: 2026-11-13T10:01:10.057506+00:00
source: "Modal Blog"
tags: [blog, raw]
---

# Sandbox resourcing: burst, don't reserve

Source: https://modal.com/blog/sandbox-bursting

Across Modal, a typical Sandbox spends more than half its life using less than 6% of its peak CPU. Take a coding agent: the Sandbox sits nearly idle while the model reasons about what to do next, and spikes only when the agent installs dependencies, runs tests, or builds the project. The same pattern shows up in other common Sandbox workloads: RL rollouts, evals, and app builders.
An agent's Sandbox session, replayed
A coding agent fixes a vulnerability over 2 minutes 46 seconds. The
    Sandbox's CPU stays near zero except brief pytest spikes, and memory sits
    near 47 MiB, both under the 0.125-core and 128 MiB request. The agent spends
    33 seconds waiting on the model and two 60-second waits it asked for.
TERMINAL-BENCH 2.1 · FIX-CODE-VULNERABILITY
Task: “Identify and fix the vulnerability in this repo”
▶ 14× SPEED
▶ 2.8× SPEED
▶ 14× SPEED
▶ 2.8× SPEED
▶ 14× SPEED
▶ 2.8× SPEED
AGENT
Starting the Sandbox
AGENT
Waiting on the model…
0.1 s
AGENT
Waiting on the model…
0.3 s
AGENT
Waiting on the model…
0.4 s
AGENT
Waiting on the model…
0.6 s
AGENT
Waiting on the model…
0.7 s
AGENT
Waiting on the model…
0.8 s
AGENT
Waiting on the model…
1.0 s
AGENT
Waiting on the model…
1.1 s
AGENT
Waiting on the model…
1.3 s
AGENT
Waiting on the model…
1.4 s
AGENT
Waiting on the model…
1.5 s
AGENT
Waiting on the model…
1.7 s
AGENT
Waiting on the model…
1.8 s
AGENT
Waiting on the model…
2.0 s
AGENT
Waiting on the model…
2.1 s
AGENT
Waiting on the model…
2.2 s
AGENT
Listing the repo and the test folder
AGENT
Waiting on the model…
0.1 s
AGENT
Waiting on the model…
0.3 s
AGENT
Waiting on the model…
0.4 s
AGENT
Waiting on the model…
0.6 s
AGENT
Waiting on the model…
0.7 s
AGENT
Waiting on the model…
0.8 s
AGENT
Waiting on the model…
1.0 s
AGENT
Waiting on the model…
1.1 s
AGENT
Waiting on the model…
1.3 s
AGENT
Waiting on the model…
1.4 s
AGENT
Waiting on the model…
1.5 s
AGENT
Waiting on the model…
1.7 s
AGENT
Waiting on the model…
1.8 s
AGENT
Waiting on the model…
2.0 s
AGENT
Waiting on the model…
2.1 s
AGENT
Waiting on the model…
2.2 s
AGENT
Waiting on the model…
2.4 s
AGENT
Waiting on the model…
2.5 s
AGENT
Checking git log; searching the tests
AGENT
Waiting on the model…
0.1 s
AGENT
Waiting on the model…
0.3 s
AGENT
Waiting on the model…
0.4 s
AGENT
Waiting on the model…
0.6 s
AGENT
Waiting on the model…
0.7 s
AGENT
Waiting on the model…
0.8 s
AGENT
Waiting on the model…
1.0 s
AGENT
Waiting on the model…
1.1 s
AGENT
Waiting on the model…
1.3 s
AGENT
Waiting on the model…
1.4 s
AGENT
Waiting on the model…
1.5 s
AGENT
Waiting on the model…
1.7 s
AGENT
Waiting on the model…
1.8 s
AGENT
Waiting on the model…
2.0 s
AGENT
Waiting on the model…
2.1 s
AGENT
Waiting on the model…
2.2 s
AGENT
Waiting on the model…
2.4 s
AGENT
Waiting on the model…
2.5 s
AGENT
Waiting on the model…
2.7 s
AGENT
Waiting on the model…
2.8 s
AGENT
Waiting on the model…
2.9 s
AGENT
Waiting on the model…
3.1 s
AGENT
Waiting on the model…
3.2 s
AGENT
Waiting on the model…
3.4 s
AGENT
Waiting on the model…
3.5 s
AGENT
Waiting on the model…
3.6 s
AGENT
Waiting on the model…
3.8 s
AGENT
Waiting on the model…
3.9 s
AGENT
Waiting on the model…
4.1 s
AGENT
Waiting on the model…
4.2 s
AGENT
Waiting on the model…
4.3 s
AGENT
Waiting on the model…
4.5 s
AGENT
Waiting on the model…
4.6 s
AGENT
Waiting on the model…
4.8 s
AGENT
Waiting on the model…
4.9 s
AGENT
Waiting on the model…
5.0 s
AGENT
Waiting on the model…
5.2 s
AGENT
Waiting on the model…
5.3 s
AGENT
Running pytest to see what fails
AGENT
Sitting out the 60 s wait it asked for
AGENT
Waiting on the model…
0.1 s
AGENT
Waiting on the model…
0.3 s
AGENT
Waiting on the model…
0.4 s
AGENT
Waiting on the model…
0.6 s
AGENT
Waiting on the model…
0.7 s
AGENT
Waiting on the model…
0.8 s
AGENT
Waiting on the model…
1.0 s
AGENT
Waiting on the model…
1.1 s
AGENT
Waiting on the model…
1.3 s
AGENT
Waiting on the model…
1.4 s
AGENT
Waiting on the model…
1.5 s
AGENT
Waiting on the model…
1.7 s
AGENT
Waiting on the model…
1.8 s
AGENT
Waiting on the model…
2.0 s
AGENT
Reading what the failing test expects
AGENT
Waiting on the model…
0.1 s
AGENT
Waiting on the model…
0.3 s
AGENT
Waiting on the model…
0.4 s
AGENT
Waiting on the model…
0.6 s
AGENT
Waiting on the model…
0.7 s
AGENT
Waiting on the model…
0.8 s
AGENT
Waiting on the model…
1.0 s
AGENT
Waiting on the model…
1.1 s
AGENT
Waiting on the model…
1.3 s
AGENT
Waiting on the model…
1.4 s
AGENT
Waiting on the model…
1.5 s
AGENT
Reading the HeaderDict class
AGENT
Waiting on the model…
0.1 s
AGENT
Waiting on the model…
0.3 s
AGENT
Waiting on the model…
0.4 s
AGENT
Waiting on the model…
0.6 s
AGENT
Waiting on the model…
0.7 s
AGENT
Waiting on the model…
0.8 s
AGENT
Waiting on the model…
1.0 s
AGENT
Waiting on the model…
1.1 s
AGENT
Waiting on the model…
1.3 s
AGENT
Waiting on the model…
1.4 s
AGENT
Finding _hkey, _hval and set_header
AGENT
Waiting on the model…
0.1 s
AGENT
Waiting on the model…
0.3 s
AGENT
Waiting on the model…
0.4 s
AGENT
Waiting on the model…
0.6 s
AGENT
Waiting on the model…
0.7 s
AGENT
Waiting on the model…
0.8 s
AGENT
Waiting on the model…
1.0 s
AGENT
Waiting on the model…
1.1 s
AGENT
Waiting on the model…
1.3 s
AGENT
Waiting on the model…
1.4 s
AGENT
Waiting on the model…
1.5 s
AGENT
Waiting on the model…
1.7 s
AGENT
Waiting on the model…
1.8 s
AGENT
Waiting on the model…
2.0 s
AGENT
Waiting on the model…
2.1 s
AGENT
Reading _hkey and _hval
AGENT
Waiting on the model…
0.1 s
AGENT
Waiting on the model…
0.3 s
AGENT
Waiting on the model…
0.4 s
AGENT
Waiting on the model…
0.6 s
AGENT
Waiting on the model…
0.7 s
AGENT
Waiting on the model…
0.8 s
AGENT
Waiting on the model…
1.0 s
AGENT
Waiting on the model…
1.1 s
AGENT
Waiting on the model…
1.3 s
AGENT
Waiting on the model…
1.4 s
AGENT
Waiting on the model…
1.5 s
AGENT
Waiting on the model…
1.7 s
AGENT
Waiting on the model…
1.8 s
AGENT
Waiting on the model…
2.0 s
AGENT
Waiting on the model…
2.1 s
AGENT
Waiting on the model…
2.2 s
AGENT
Waiting on the model…
2.4 s
AGENT
Waiting on the model…
2.5 s
AGENT
Waiting on the model…
2.7 s
AGENT
Waiting on the model…
2.8 s
AGENT
Waiting on the model…
2.9 s
AGENT
Waiting on the model…
3.1 s
AGENT
Waiting on the model…
3.2 s
AGENT
Waiting on the model…
3.4 s
AGENT
Waiting on the model…
3.5 s
AGENT
Waiting on the model…
3.6 s
AGENT
Waiting on the model…
3.8 s
AGENT
Waiting on the model…
3.9 s
AGENT
Waiting on the model…
4.1 s
AGENT
Waiting on the model…
4.2 s
AGENT
Waiting on the model…
4.3 s
AGENT
Waiting on the model…
4.5 s
AGENT
Waiting on the model…
4.6 s
AGENT
Waiting on the model…
4.8 s
AGENT
Waiting on the model…
4.9 s
AGENT
Waiting on the model…
5.0 s
AGENT
Waiting on the model…
5.2 s
AGENT
Waiting on the model…
5.3 s
AGENT
Waiting on the model…
5.5 s
AGENT
Waiting on the model…
5.6 s
AGENT
Waiting on the model…
5.7 s
AGENT
Waiting on the model…
5.9 s
AGENT
Waiting on the model…
6.0 s
AGENT
Waiting on the model…
6.2 s
AGENT
Waiting on the model…
6.3 s
AGENT
Waiting on the model…
6.4 s
AGENT
Waiting on the model…
6.6 s
AGENT
Waiting on the model…
6.7 s
AGENT
Waiting on the model…
6.9 s
AGENT
Waiting on the model…
7.0 s
AGENT
Waiting on the model…
7.1 s
AGENT
Waiting on the model…
7.3 s
AGENT
Waiting on the model…
7.4 s
AGENT
Waiting on the model…
7.6 s
AGENT
Waiting on the model…
7.7 s
AGENT
Waiting on the model…
7.8 s
AGENT
Waiting on the model…
8.0 s
AGENT
Waiting on the model…
8.1 s
AGENT
Waiting on the model…
8.3 s
AGENT
Waiting on the model…
8.4 s
AGENT
Waiting on the model…
8.5 s
AGENT
Waiting on the model…
8.7 s
AGENT
Waiting on the model…
8.8 s
AGENT
Waiting on the model…
9.0 s
AGENT
Waiting on the model…
9.1 s
AGENT
Waiting on the model…
9.2 s
AGENT
Waiting on the model…
9.4 s
AGENT
Waiting on the model…
9.5 s
AGENT
Waiting on the model…
9.7 s
AGENT
Waiting on the model…
9.8 s
AGENT
Waiting on the model…
9.9 s
AGENT
Waiting on the model…
10.1 s
AGENT
Waiting on the model…
10.2 s
AGENT
Waiting on the model…
10.4 s
AGENT
Waiting on the model…
10.5 s
AGENT
Waiting on the model…
10.6 s
AGENT
Waiting on the model…
10.8 s
AGENT
Waiting on the model…
10.9 s
AGENT
Waiting on the model…
11.1 s
AGENT
Waiting on the model…
11.2 s
AGENT
Waiting on the model…
11.3 s
AGENT
Waiting on the model…
11.5 s
AGENT
Waiting on the model…
11.6 s
AGENT
Waiting on the model…
11.8 s
AGENT
Waiting on the model…
11.9 s
AGENT
Waiting on the model…
12.0 s
AGENT
Waiting on the model…
12.2 s
AGENT
Waiting on the model…
12.3 s
AGENT
Patching the header checks; reporting
AGENT
Sitting out the 60 s wait it asked for
AGENT
Waiting on the model…
0.1 s
AGENT
Waiting on the model…
0.3 s
AGENT
Waiting on the model…
0.4 s
AGENT
Waiting on the model…
0.6 s
AGENT
Waiting on the model…
0.7 s
AGENT
Waiting on the model…
0.8 s
AGENT
Waiting on the model…
1.0 s
AGENT
Waiting on the model…
1.1 s
AGENT
Waiting on the model…
1.3 s
AGENT
Waiting on the model…
1.4 s
AGENT
Waiting on the model…
1.5 s
AGENT
Waiting on the model…
1.7 s
AGENT
Marking the task complete
AGENT
Waiting on the model…
0.1 s
AGENT
Waiting on the model…
0.3 s
AGENT
Waiting on the model…
0.4 s
AGENT
Waiting on the model…
0.6 s
AGENT
Waiting on the model…
0.7 s
AGENT
Waiting on the model…
0.8 s
AGENT
Waiting on the model…
1.0 s
AGENT
Waiting on the model…
1.1 s
AGENT
Waiting on the model…
1.3 s
AGENT
Waiting on the model…
1.4 s
AGENT
Waiting on the model…
1.5 s
AGENT
Waiting on the model…
1.7 s
AGENT
Task complete · 10 model calls
SANDBOX
STARTING
IDLE
RUNNING
IDLE
RUNNING
IDLE
RUNNING
IDLE
RUNNING
IDLE
RUNNING
IDLE
RUNNING
IDLE
RUNNING
IDLE
RUNNING
IDLE
$
$
ls -la /app
$
wc -l /app/bottle.py && ls /app/test
total 186
drwxr-xr-x 1 root root    272 Oct 28  2025 .
drwxr-xr-x 1 root root    160 Nov  9 17:35 …
…
build_python.sh      test_config.py        …
example_settings.py  test_contextlocals.py …
test_app.py          test_environ.py       …
$
…
build_python.sh      test_config.py        …
example_settings.py  test_contextlocals.py …
test_app.py          test_environ.py       …
$
cd /app && git log --oneline -5
$
grep -rn "raises" test/ | grep -iv "HTTPErr…
0207a34 (HEAD -> master) typing: Type hints…
b1bd8bb Formatting and cleanup
e3d8e71 fix: Route.__repr__ and Route.get_u…
011016c Changes to make tests pass on Windo…
21a8db0 build: Also test latest python rele…
$
e3d8e71 fix: Route.__repr__ and Route.get_u…
011016c Changes to make tests pass on Windo…
21a8db0 build: Also test latest python rele…
$
pytest -x -q 2>&1 | tail -30
..........................................…
=================================== FAILURE…
__________ TestResponse.test_prevent_contr…
…
FAILED test/test_environ.py::TestResponse::…
!!!!!!!!!!!!!!!!!!!!!!!!!!! stopping after 1…
1 failed, 66 passed in 0.22s
$
!!!!!!!!!!!!!!!!!!!!!!!!!!! stopping after 1…
1 failed, 66 passed in 0.22s
$
sed -n 735,775p test/test_environ.py
$
grep -n "class HeaderDict" bottle.py
def test_prevent_control_characters_in_…
masks = '{}test', 'test{}', 'te{}st'
tests = '\n', '\r', '\n\r', '\0'
…
self.assertEqual(0, seconds(now, now2))
class TestRedirect(unittest.TestCase):
2168:class HeaderDict(MultiDict):
$
class TestRedirect(unittest.TestCase):
2168:class HeaderDict(MultiDict):
$
sed -n 2168,2230p bottle.py
$
grep -n "def set_header\|def add_header\|de…
class HeaderDict(MultiDict):
""" A case-insensitive version of :clas…
replace the old value instead of append…
…
2185:    def __setitem__(self, key, value):
2230:    def __setitem__(self, key, value):
2359:    def __setitem__(self, key, value):
$
2230:    def __setitem__(self, key, value):
2359:    def __setitem__(self, key, value):
$
grep -n "_hkey\|_hval" bottle.py | head -20
$
sed -n 1700,1730p bottle.py
1560:def _hkey(key):
1565:def _hval(value):
1699:        return _hkey(name) in self._he…
…
return self.headerlist
def _wsgi_status_line(self):
""" WSGI conform status line (latin1-en…
$
def _wsgi_status_line(self):
""" WSGI conform status line (latin1-en…
$
sed -n 1555,1575p bottle.py
$
grep -n "class MultiDict" bottle.py && sed …
del self.environ['bottle.request.ext.%s…
except KeyError:
raise AttributeError("Attribute not def…
…
return ((k, v) for k, vl in self.dict.i…
iterkeys = keys
itervalues = values
$
itervalues = values
$
python3 - <<'EOF' …
$
echo '{"file_path": "/app/bottle.py", "cwe_…
$
pytest -rA 2>&1 | tail -15
patched
{"file_path": "/app/bottle.py", "cwe_id": […
PASSED test/test_wsgi.py::TestRouteDecorato…
…
PASSED test/test_wsgi.py::TestAppShortcuts:…
PASSED test/test_wsgi.py::TestAppShortcuts:…
========================== 367 passed in…
$
CPU · CORES
NO LIMIT SET
0
0.25
0.5
0.75
0.125-core request
MEMORY · MIB
NO LIMIT SET
0
50
100
150
128 MiB request
0:00
1:23
2:46
pytest finished in 1 s;
the agent waits out
the 60 s it asked for
pytest finished in 2 s;
the agent waits out
the 60 s it asked for
Agent waiting on the model
0 s of 0:00 so far
0 s of 0:01 so far
0 s of 0:02 so far
0 s of 0:03 so far
0 s of 0:04 so far
0 s of 0:05 so far
1 s of 0:05 so far
2 s of 0:06 so far
2 s of 0:07 so far
2 s of 0:08 so far
3 s of 0:08 so far
3 s of 0:09 so far
4 s of 0:09 so far
5 s of 0:10 so far
5 s of 0:11 so far
5 s of 0:12 so far
6 s of 0:12 so far
6 s of 0:13 so far
7 s of 0:13 so far
7 s of 0:14 so far
8 s of 0:14 so far
8 s of 0:15 so far
9 s of 0:15 so far
9 s of 0:16 so far
10 s of 0:16 so far
10 s of 0:17 so far
10 s of 0:18 so far
10 s of 0:19 so far
10 s of 0:20 so far
10 s of 0:21 so far
10 s of 0:22 so far
10 s of 0:23 so far
10 s of 0:24 so far
10 s of 0:25 so far
10 s of 0:26 so far
10 s of 0:27 so far
10 s of 0:28 so far
10 s of 0:29 so far
10 s of 0:30 so far
10 s of 0:31 so far
10 s of 0:32 so far
10 s of 0:33 so far
10 s of 0:34 so far
10 s of 0:35 so far
10 s of 0:36 so far
10 s of 0:37 so far
10 s of 0:38 so far
10 s of 0:39 so far
10 s of 0:40 so far
10 s of 0:41 so far
10 s of 0:42 so far
10 s of 0:43 so far
10 s of 0:44 so far
10 s of 0:45 so far
10 s of 0:46 so far
10 s of 0:47 so far
10 s of 0:48 so far
10 s of 0:49 so far
10 s of 0:50 so far
10 s of 0:51 so far
10 s of 0:52 so far
10 s of 0:53 so far
10 s of 0:54 so far
10 s of 0:55 so far
10 s of 0:56 so far
10 s of 0:57 so far
10 s of 0:58 so far
10 s of 0:59 so far
10 s of 1:00 so far
10 s of 1:01 so far
10 s of 1:02 so far
10 s of 1:03 so far
10 s of 1:04 so far
10 s of 1:05 so far
10 s of 1:06 so far
10 s of 1:07 so far
10 s of 1:08 so far
10 s of 1:09 so far
10 s of 1:10 so far
10 s of 1:11 so far
10 s of 1:12 so far
10 s of 1:13 so far
10 s of 1:15 so far
10 s of 1:16 so far
10 s of 1:17 so far
11 s of 1:17 so far
11 s of 1:18 so far
12 s of 1:18 so far
12 s of 1:19 so far
12 s of 1:20 so far
13 s of 1:20 so far
13 s of 1:21 so far
14 s of 1:21 so far
14 s of 1:22 so far
14 s of 1:23 so far
15 s of 1:23 so far
15 s of 1:24 so far
15 s of 1:25 so far
16 s of 1:25 so far
16 s of 1:26 so far
17 s of 1:26 so far
17 s of 1:27 so far
17 s of 1:28 so far
18 s of 1:28 so far
18 s of 1:29 so far
19 s of 1:29 so far
19 s of 1:30 so far
20 s of 1:30 so far
20 s of 1:31 so far
21 s of 1:31 so far
21 s of 1:32 so far
22 s of 1:32 so far
22 s of 1:33 so far
23 s of 1:33 so far
23 s of 1:34 so far
24 s of 1:34 so far
24 s of 1:35 so far
25 s of 1:35 so far
25 s of 1:36 so far
26 s of 1:36 so far
26 s of 1:37 so far
27 s of 1:37 so far
27 s of 1:38 so far
28 s of 1:38 so far
28 s of 1:39 so far
29 s of 1:39 so far
29 s of 1:40 so far
30 s of 1:41 so far
30 s of 1:42 so far
30 s of 1:43 so far
30 s of 1:44 so far
30 s of 1:45 so far
30 s of 1:46 so far
30 s of 1:47 so far
30 s of 1:48 so far
30 s of 1:49 so far
30 s of 1:50 so far
30 s of 1:51 so far
30 s of 1:52 so far
30 s of 1:53 so far
30 s of 1:54 so far
30 s of 1:55 so far
30 s of 1:56 so far
30 s of 1:57 so far
30 s of 1:58 so far
30 s of 1:59 so far
30 s of 2:00 so far
30 s of 2:01 so far
30 s of 2:02 so far
30 s of 2:03 so far
30 s of 2:04 so far
30 s of 2:05 so far
30 s of 2:06 so far
30 s of 2:07 so far
30 s of 2:08 so far
30 s of 2:09 so far
30 s of 2:10 so far
30 s of 2:11 so far
30 s of 2:12 so far
30 s of 2:13 so far
30 s of 2:14 so far
30 s of 2:15 so far
30 s of 2:16 so far
30 s of 2:17 so far
30 s of 2:18 so far
30 s of 2:19 so far
30 s of 2:20 so far
30 s of 2:21 so far
30 s of 2:22 so far
30 s of 2:23 so far
30 s of 2:24 so far
30 s of 2:25 so far
30 s of 2:26 so far
30 s of 2:27 so far
30 s of 2:28 so far
30 s of 2:29 so far
30 s of 2:30 so far
30 s of 2:31 so far
30 s of 2:32 so far
30 s of 2:33 so far
30 s of 2:34 so far
30 s of 2:35 so far
30 s of 2:36 so far
30 s of 2:37 so far
30 s of 2:38 so far
30 s of 2:39 so far
30 s of 2:40 so far
30 s of 2:41 so far
30 s of 2:42 so far
31 s of 2:42 so far
31 s of 2:43 so far
31 s of 2:44 so far
32 s of 2:44 so far
32 s of 2:45 so far
33 s of 2:45 so far
33 s of 2:46 (20%)
Real session · Modal Sandbox (gVisor) · Kimi-K3 · Nov 9, 2026
Today, most sandboxes are priced based on a fixed-resource reservation model. Reservations are a poor fit for spiky work, for two reasons:
You have to guess your peak.
Agent resource usage varies greatly from task to task, and an undersized Sandbox can crash, so you end up reserving well above your real peak.
You pay for the peak all the time.
The Sandbox spends most of its life far below its reservation, but you pay for all of it.
We believe your bill should align with your workload, rising when it’s busy and falling when it’s idle. That’s why our Sandboxes burst: a Sandbox gets the CPU and memory it needs when your work spikes and gives them back when it is done. You pay for what you actually use.
What it looks like on Modal: active-resource pricing
Every Sandbox bursts by default. Start with the base 0.125 cores and 128 MiB request and let your Sandbox grow as it needs.
With active-resource pricing, you pay each second for what you use, with the small request as a floor. You can request more to guarantee it, but you’ll pay for those resources even when your Sandbox is idle. You can also set a limit to cap how far your Sandbox can burst; think of it as setting the size of the computer the Sandbox lives on. Most workloads don’t need to set a request or limit: use the default and burst from there.
Request, burst and limit
A Sandbox's request is guaranteed and billed even when idle. When it needs
    more it bursts past the request, paying only for what it uses, up to an
    optional limit.
REQUEST · BURST · LIMIT
The request is guaranteed. When your Sandbox needs more, it bursts.
Limit
optional
Caps what your Sandbox can use
(the size of its computer).
Bursting
Grows past the request when needed.
Pay only for what you use.
Request
default 0.125 cores · 128 MiB
Guaranteed. Billed even when idle.
Estimating Sandbox costs on Modal
Because you pay for what you use, estimate your costs from average usage rather than peak usage:
CPU cost
≈ runtime × CPU rate × average cores used
Memory cost
≈ runtime × memory rate × average GiB used
This average works for bursting Sandboxes because each second, a Sandbox is billed for the higher of its request and what it actually uses. Since the average sits well below the peak, customers with bursty workloads can end up paying a fraction of their typical reservation bill.
The calculator below can help you estimate how your bill would change.
Coding agent
RL rollout
App preview
Web server
A 20-minute coding agent task: install, then read, edit, test and type-check while the model thinks between steps, and a build at the end.
CPU (1 CPU ≈ 2 vCPU)
Spikes for the install and build; tests use about 1 CPU.
0
3
6
0
5 min
10 min
15 min
20 min
reserved for its busiest minute: 1.5 CPU
full speed on Modal, slower on a fixed box
Memory (GiB)
About 0.8 GiB between steps; 2.3 GiB for the build.
0
1.5
3
0
5 min
10 min
15 min
20 min
reserved for the peak: 3 GiB
burst
Reservation: sized in advance (CPU for the busiest minute, memory for the
        peak), billed for the whole box all the time
Modal: billed for what the workload uses, each second
Modal rate
list price · billed on use
14.19¢
/CPU·hr
2.40¢
/GiB·hr
Bursting is cheaper
:
      savings of
58%
vs a fixed-size reservation.
Modal reserves only its minimum, 0.125 CPU and 128 MiB.
Average billed use
0.44 CPU · 0.94 GiB
Peak use
6.00 CPU · 2.30 GiB
Reserved size
1.5 CPU · 3 GiB
CPU for the busiest minute, memory for the peak
Modal cost per Sandbox-hour
8.4¢
14.19¢ × 0.44 CPU + 2.40¢ × 0.94 GiB
Reservation cost per Sandbox-hour
20.0¢
10.08¢ × 1.5 CPU + 1.62¢ × 3 GiB
Bursting savings
58%
1 CPU ≈ 2 vCPU.
Modal prices CPU by physical core; most sandbox providers price by vCPU. Costs
    are per Sandbox-hour. The reservation covers the workload's busiest minute of
    CPU and its peak memory, rounded up to whole vCPU and GiB, at a common fixed-size
    list price. Illustrative workloads, not production traces.
Why bursting works
One machine, 48 cores
Two customers each request 3 cores on a 48-core machine. Customer A bursts
    to 12 cores into unreserved and idle cores, then drops back; Customer B
    later bursts to 10 cores. Other customers' usage fills the rest.
ONE MACHINE · 48 CORES
A
A
A
A
A
B
B
B
B
A
A
A
A
A
A
B
B
B
B
B
B
B
A
A
A
A
A
B
B
B
A
B
B
A
A
A
A
Customer A's Sandbox
2.0 cores
Request: 3 cores
2.1 cores
Request: 3 cores
2.2 cores
Request: 3 cores
5.1 cores
3 requested + 2.1 bursting
6.4 cores
3 requested + 3.4 bursting
8.3 cores
3 requested + 5.3 bursting
9.1 cores
3 requested + 6.1 bursting
10.3 cores
3 requested + 7.3 bursting
10.8 cores
3 requested + 7.8 bursting
11.4 cores
3 requested + 8.4 bursting
11.6 cores
3 requested + 8.6 bursting
11.9 cores
3 requested + 8.9 bursting
12.0 cores
3 requested + 9.0 bursting
11.9 cores
3 requested + 8.9 bursting
12.0 cores
3 requested + 9.0 bursting
11.9 cores
3 requested + 8.9 bursting
12.0 cores
3 requested + 9.0 bursting
11.9 cores
3 requested + 8.9 bursting
12.0 cores
3 requested + 9.0 bursting
11.9 cores
3 requested + 8.9 bursting
11.8 cores
3 requested + 8.8 bursting
11.2 cores
3 requested + 8.2 bursting
10.6 cores
3 requested + 7.6 bursting
8.6 cores
3 requested + 5.6 bursting
7.1 cores
3 requested + 4.1 bursting
4.5 cores
3 requested + 1.5 bursting
3.6 cores
3 requested + 0.6 bursting
2.6 cores
Request: 3 cores
2.4 cores
Request: 3 cores
2.2 cores
Request: 3 cores
2.1 cores
Request: 3 cores
2.0 cores
Request: 3 cores
1.9 cores
Request: 3 cores
1.8 cores
Request: 3 cores
1.7 cores
Request: 3 cores
1.8 cores
Request: 3 cores
1.9 cores
Request: 3 cores
2.0 cores
Request: 3 cores
Customer B's Sandbox
2.1 cores
Request: 3 cores
2.0 cores
Request: 3 cores
1.9 cores
Request: 3 cores
1.8 cores
Request: 3 cores
1.7 cores
Request: 3 cores
1.6 cores
Request: 3 cores
1.5 cores
Request: 3 cores
1.6 cores
Request: 3 cores
4.1 cores
3 requested + 1.1 bursting
5.1 cores
3 requested + 2.1 bursting
6.8 cores
3 requested + 3.8 bursting
7.5 cores
3 requested + 4.5 bursting
8.5 cores
3 requested + 5.5 bursting
8.9 cores
3 requested + 5.9 bursting
9.5 cores
3 requested + 6.5 bursting
9.7 cores
3 requested + 6.7 bursting
9.9 cores
3 requested + 6.9 bursting
10.0 cores
3 requested + 7.0 bursting
9.9 cores
3 requested + 6.9 bursting
9.3 cores
3 requested + 6.3 bursting
8.8 cores
3 requested + 5.8 bursting
7.2 cores
3 requested + 4.2 bursting
6.0 cores
3 requested + 3.0 bursting
3.9 cores
3 requested + 0.9 bursting
3.2 cores
3 requested + 0.2 bursting
2.4 cores
Request: 3 cores
2.2 cores
Request: 3 cores
2.1 cores
Request: 3 cores
Customer A: in use, bursting
Customer B: in use, bursting
Other customers: in use, bursting
Request
Not reserved
Your Sandbox is guaranteed its request, which is small by default. When it bursts beyond that, it draws from a shared pool of the machine’s idle capacity, which Modal’s scheduler keeps free on every machine.
It works because of the law of averages. Sandboxes sharing a machine mostly run unrelated work for different customers, so they rarely spike at the same moment. If every Sandbox reserved capacity for its peak, the machine would need room for the sum of all the peaks. With bursting, it only needs room for the most they use at the same time. It’s the same reason a power grid can be much smaller than the sum of every household’s peak demand.
Each Sandbox is busy in bursts. Stacked on one machine, they smooth out.
Stacked CPU use over one hour on one production machine: five Sandboxes on
    top of everything else. Combined use stays far below machine capacity, while
    reserving every Sandbox's own peak would exceed it.
CPU IN USE · ONE PRODUCTION MACHINE
PER MINUTE · ONE HOUR
Each Sandbox is busy in bursts. Stacked on one machine, they smooth out.
Five Sandboxes from one production machine, each in its own color, on top
    of everything else running there.
Five of its Sandboxes, one color each
Everything else on the machine
If every Sandbox here reserved its own peak
Machine capacity
0 min
15
30
45
60 min
CPU in use, minute by minute, over one hour in October 2026. A Sandbox's
    peak is its busiest minute in this hour.
How should I size my Modal Sandboxes?
For most workloads, don’t. Start with the defaults and let your Sandbox burst, paying only for what it uses. By default, CPU can burst up to 16 cores above its request, and memory has no limit.
A limit is optional but can be helpful in the following situations:
You need a consistent environment
: For evals, RL rollouts, and other benchmarks, a limit keeps any run from using significantly more CPU and memory than others. If an environment needs exactly the same resources every time, set the request to be equal to the limit.
You want to cap costs
: A limit bounds how much memory and CPU a Sandbox can get and thus limits the total bill from an uncapped process or runaway agent.
When setting a memory limit, set it above the Sandbox’s real peak. Sandboxes that cross the memory limit are stopped.
The default request means you aren’t paying for idle resources: your Sandbox is billed for the default request when it’s idle and you pay for what you use when it bursts.
Minimizing the impact of evictions
Spikes rarely line up. However, if they do and a machine runs out of CPU, the bursting Sandboxes slow down until CPU frees up. Every Sandbox is guaranteed at least its requested CPU, but in practice most get more when needed.
Memory has a bigger downside. If a machine runs out of memory, Sandboxes using more than their request at that moment may be evicted with an out-of-memory error, or OOM (a Sandbox within its request is never evicted).
Evictions are rare, and we back that with an SLO: for bursting Sandboxes under 8 GiB, an OOM rate below 0.0001% per minute (about 1 eviction per 694 Sandbox-days). We don’t yet have an SLO for larger Sandboxes, but in practice they also see low eviction rates.
We have also provided tools to help reduce the impact of OOMs.
Exit snapshots
save your Sandbox’s files automatically when it stops, and
filesystem snapshots
save them whenever you choose.
Volumes
keep data outside the Sandbox, and the termination reasons SDK lets you detect an eviction and retry.
If your workload can’t tolerate OOMs at the given rates, set a higher memory request (guaranteed memory). To find the right size, start with the default request, check the
Exit Reasons chart
in your dashboard to see how it goes, and adjust your request if needed.
Summary
In short, most Sandbox workloads are bursty, so they need a pricing model that matches. With Modal’s active-resource pricing you pay for what you use while giving your Sandbox the resources it needs, so estimate from average usage, not peak. Leave the defaults, and your Sandbox will start small and burst as it needs.
Every Sandbox bursts by default, so you can try it with your next
modal.Sandbox.create()
. If you are still unsure where your use case fits, reach out to your sales rep or contact us at
sales@modal.com
.
