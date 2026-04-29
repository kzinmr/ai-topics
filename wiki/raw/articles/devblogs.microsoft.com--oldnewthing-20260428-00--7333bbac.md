---
title: "Developing a cross-process reader/writer lock with limited readers, part 1: A semaphore"
url: "https://devblogs.microsoft.com/oldnewthing/20260428-00/?p=112278"
fetched_at: 2026-04-29T07:00:51.357866+00:00
source: "devblogs.microsoft.com/oldnewthing"
tags: [blog, raw]
---

# Developing a cross-process reader/writer lock with limited readers, part 1: A semaphore

Source: https://devblogs.microsoft.com/oldnewthing/20260428-00/?p=112278

Say you want to have the functionality of a reader/writer lock, but have it work cross-process. The built-in
SRWLOCK
works only within a single process. Can we build a reader/writer lock that works across processes?
For convenience, let’s say that you want to support a maximum of
N
simultaneous readers, for some fixed value
N
. We can do this:
Create a semaphore with a token count of
N
. Share this semaphore with all of the processes, either by giving it a name or by duplicating the handle into each of the processes.
To take a read lock, claim one token from the semaphore. To release the lock, release the token.
To take a write lock, claim
N
tokens from the semaphore. To release the lock, release
N
tokens.
The idea for the write lock is that it’s accomplished by claiming all the read locks, thereby ensuring that nobody else can get a read lock.
#define MAX_SHARED 100
HANDLE sharedSemaphore;

void AcquireShared()
{
    WaitForSingleObject(sharedSemaphore, INFINITE);
}

void ReleaseShared()
{
    ReleaseSemaphore(sharedSemaphore, 1, nullptr);
}

void AcquireExclusive()
{
    for (unsigned i = 0; i < MAX_SHARED; i++) {
        WaitForSingleObject(sharedSemaphore, INFINITE);
    }
}

void ReleaseShared()
{
    ReleaseSemaphore(sharedSemaphore, MAX_SHARED, nullptr);
}
Since we are using
Wait­For­Single­Object
, we can also add a timeout, so that the caller can decide to abandon the operation if they can’t claim the lock.
bool AcquireSharedWithTimeout(DWORD timeout)
{
    return WaitForSingleObject(sharedSemaphore, timeout) == WAIT_OBJECT_0;
}

bool AcquireExclusiveWithTimeout(DWORD timeout)
{
    DWORD start = GetTickCount();
    for (unsigned i = 0; i < MAX_SHARED; i++) {
        DWORD elapsed = GetTickCount() - start;
        if (elapsed > timeout ||
            WaitForSingleObject(sharedSemaphore, timeout - elapsed) == WAIT_TIMEOUT)) {
            // Restore the tokens we already claimed.
            if (i > 0) {
                ReleaseSemaphore(sharedSemaphore, i, nullptr);
            }
            return false;
        }
    }
    return true;
}
Exclusive acquisition is tricky because we have to call
Wait­For­Single­Object
multiple times, with decreasing timeouts as time passes. If we run out of time, then we need to give back the tokens we had prematurely claimed.
There’s still a problem here. We’ll look at it next time.
