---
title: "Developing a cross-process reader/writer lock with limited readers, part 4: Abandonment"
url: "https://devblogs.microsoft.com/oldnewthing/20260501-00/?p=112291"
fetched_at: 2026-05-02T07:00:43.623863+00:00
source: "devblogs.microsoft.com/oldnewthing"
tags: [blog, raw]
---

# Developing a cross-process reader/writer lock with limited readers, part 4: Abandonment

Source: https://devblogs.microsoft.com/oldnewthing/20260501-00/?p=112291

We’ve been building a cross-process reader/writer lock with a cap on the number of readers, we concluded our investigation last time by noting
that there is a serious problem that needs to be fixed
.
That serious problem is abandonment.
Suppose a process crashes while it holds a shared or exclusive lock on our cross-process reader/writer lock.
Semaphores don’t have owners
, so if a thread terminates while in possession of a semaphore token, that token is lost forever. For our cross-process reader/writer lock, that means that the maximum number of shared acquirers goes down by one, and exclusive acquisitions will never succeed, since they will be waiting for that last token which will never be returned.
A synchronization object that does have the concept of ownership is the mutex, so we can build our reader/writer lock out of mutexes.
The idea here is that instead of claiming semaphore tokens, we claim mutexes. This means that we need one mutex for each potential shared acquisition, plus one more to avoid the starvation problem.
The outline is
Shared acquisition: Claim any available token mutex.
Shared release: Release the claimed token mutex.
Exclusive acquisition: Claim all token mutexes.
Exclusive release: Release all token mutexes.
HANDLE sharedMutex;
HANDLE tokenMutexes[MAX_SHARED];

struct TimeoutTracker
{
    explicit TimeoutTracker(DWORD timeout)
        : m_timeout(timeout) {}

    DWORD m_start = GetTickCount();
DWORD
Wait(HANDLE h)
    {
        DWORD elapsed = GetTickCount() - m_start;
        if (elapsed > m_timeout) return
WAIT_TIMEOUT
;
        return
WaitForSingleObject(h, m_timeout - elapsed)
;
    }
DWORD WaitMultiple(DWORD count, const HANDLE* handles, BOOL waitAll)
{
DWORD elapsed = GetTickCount() - m_start;
if (elapsed > m_timeout) return WAIT_TIMEOUT;
return WaitForMultipleObjects(count, handles, waitAll, m_timeout - elapsed);
}
};
We change the return value of the
Wait
method so it returns the wait result rather than a success/failure. We also add a
Wait­Multiple
method for wrapping
Wait­For­Multiple­Objects
.
Next is a handy helper function.
int WaitResultToindex(DWORD result)
{
    auto index = result - WAIT_OBJECT_0;
    if (index < MAX_SHARED) return static_cast<int>(index);

    index = result - WAIT_ABANDONED_0;
    if (index < MAX_SHARED) return static_cast<int>(index);

    return -1;
}
The
Wait­Result­To­Index
function takes the wait result and returns the index of the acquired mutex, or
-1
if no mutex was acquired.
Notice that this code treats the abandoned the state the same as the normal wait state.  We are assuming that the code can recover from inconsistent data somehow. (For example, maybe the shared and exclusive accesses are to control access to a set of files, so the existing code already has to deal with file corruption.)
All that’s left is to implement the outline.
int AcquireShared()
{
    WaitForSingleObject(sharedMutex, INFINITE);

    auto result = WaitForMultipleObjects(MAX_SHARED, tokenMutexes, FALSE /* bWaitAll */, INFINITE);

    ReleaseMutex(sharedMutex);

    return WaitResultToIndex(result);
}

void ReleaseShared(int index)
{
    ReleaseMutex(tokenMutexes[index]);
}

int AcquireSharedWithTimeout(DWORD timeout)
{
    TimeoutTracker tracker(timeout);
    DWORD result = tracker.Wait(hSharedMutex);
    if (result != WAIT_OBJECT_0) return -1;
    result = tracker.WaitMultiple(MAX_SHARED, tokenMutexes, FALSE /* waitAll */);
    ReleaseMutex(sharedMutex);

    return WaitResultToIndex(result);
}

void AcquireExclusive()
{
    WaitForSingleObject(sharedMutex, INFINITE);

    auto result = WaitForMultipleObjects(MAX_SHARED, tokenMutexes, TRUE /* bWaitAll */, INFINITE);

    ReleaseMutex(sharedMutex);
}

void ReleaseExclusive()
{
    for (unsigned i = 0; i < MAX_SHARED; i++) {
        ReleaseMutex(tokenMutexes[i]);
    }
}

bool AcquireExclusiveWithTimeout(DWORD timeout)
{
    TimeoutTracker tracker(timeout);
    DWORD result = tracker.Wait(hSharedMutex);
    if (result != WAIT_OBJECT_0) return -1;
    result = tracker.WaitMultiple(MAX_SHARED, tokenMutexes, TRUE /* waitAll */);
    ReleaseMutex(sharedMutex);

    return result != WAIT_TIMEOUT;
}
