---
title: "Developing a cross-process reader/writer lock with limited readers, part 3: Fairness"
url: "https://devblogs.microsoft.com/oldnewthing/20260430-00/?p=112288"
fetched_at: 2026-05-01T07:13:05.319243+00:00
source: "devblogs.microsoft.com/oldnewthing"
tags: [blog, raw]
---

# Developing a cross-process reader/writer lock with limited readers, part 3: Fairness

Source: https://devblogs.microsoft.com/oldnewthing/20260430-00/?p=112288

We’ve been building a cross-process reader/writer lock with a cap on the number of readers, we concluded our investigation last time by noting
that throughput of exclusive accesses was poor
. What’s going on?
The problem is that exclusive acquisitions are working to claim semaphore tokens one at a time, so it can lose out to shared acquisitions that are requested even after the exclusive acquisition had started, effectively letting shared acquisitions “jump ahead of the exclusive acquisition”, and thereby starving out exclusive acquisitions.
Token count
Exclusive
acquirer
Shared acquirers
A
B
C
D
5
4
Acq
3
Acq
2
1st Acq
1
2nd Acq
0
3rd Acq
0
4th Acq (blocks)
0
Acq (blocks)
0
Acq (blocks)
1
Rel
0
4th Acq
0
5th Acq (blocks)
1
Rel
0
Acq
1
Rel
0
Acq
Let’s say that we have capped the number of shared acquisitions to five. In the above scenario, we have an exclusive acquiring thread and four shared acquiring threads. The first two shared acquiring threads (call them A and B) succeed at their shared acquisitions, and then the exclusive acquiring thread tries to enter exclusively. The exclusive acquiring thread needs five tokens, and it quickly gets three of them before blocking when it tries to get the fourth.
While the exclusive acquiring thread is waiting to get its fourth token, two other shared acquiring threads (call them C and D) try to enter in shared mode. They too block.
One of the original shared acquiring threads releases its shared lock, which release a token, and that token is quickly snapped up by the exclusive acquiring thread, thanks to the “mostly FIFO” policy for synchronization objects. (Let’s assume for the purpose of this discussion that none of the things that violate FIFO-ness has occurred.) The exclusive acquiring thread now waits to claim its fifth token.
When the second of the original shared acquiring threads releases its token, it is given to thread C, even though thread C started its shared acquisition
after
the exclusive acquiring thread tried to acquire exclusively.
And then when thread C releases its token, that token is given to thread D, since its request for the token precedes the exclusive thread’s request for the fifth token. The exclusive acquiring thread has once again gotten boxed out.
To fix this, we can make
all
acquisitions claim the shared mutex. The shared mutex then does the work of enforcing “mostly FIFO” acquisition behavior across all acquisitions.
Since we’re going to be doing combined timeouts, I’ll refactor the timeout management into a helper class.
struct TimeoutTracker
{
    explicit TimeoutTracker(DWORD timeout)
        : m_timeout(timeout) {}

    DWORD m_start = GetTickCount();

    bool Wait(HANDLE h)
    {
        DWORD elapsed = GetTickCount() - m_start;
        if (elapsed > m_timeout) return false;
        return WaitForSingleObject(h, m_timeout - elapsed)
                    == WAIT_OBJECT_0;
    }
};
We can use this helper class to manage our timeouts.
HANDLE sharedSemaphore;
HANDLE sharedMutex;

void AcquireShared()
{
WaitForSingleObject(sharedMutex, INFINITE);
WaitForSingleObject(sharedSemaphore, INFINITE);
ReleaseMutex(sharedMutex);
}

bool AcquireSharedWithTimeout(DWORD timeout)
{
TimeoutTracker tracker(timeout);
bool result = tracker.Wait(hSharedMutex);
if (!result) return false;
result = tracker.Wait(sharedSemaphore);
ReleaseMutex(sharedMutex);
return result;
}

// no change to AcquireExclusive
void AcquireExclusive()
{
    WaitForSingleObject(sharedMutex, INFINITE);

    for (unsigned i = 0; i < MAX_SHARED; i++) {
        WaitForSingleObject(sharedSemaphore, INFINITE);
    }

    ReleaseMutex(sharedMutex);
}

// no functional change, but using the new helper class
bool AcquireExclusiveWithTimeout(DWORD timeout)
{
TimeoutTracker tracker(timeout);
bool result = tracker.Wait(sharedMutex);
if (!result) return false;
for (unsigned i = 0; i < MAX_SHARED; i++) {
if (!tracker.Wait(sharedSemaphore)) {
// Restore the tokens we already claimed.
            if (i > 0) {
                ReleaseSemaphore(sharedSemaphore, i, nullptr);
            }
            ReleaseMutex(sharedMutex);
            return false;
        }
    }
    ReleaseMutex(sharedMutex);
    return true;
}
(Yes, I’m not using RAII. I’ve made that choice for expository purposes, since it lets you see exactly when each synchronization object is acquired and released.)
Are we done?
No, we’re not done.
There is still a serious problem that needs to be fixed. We’ll look at it next time.
