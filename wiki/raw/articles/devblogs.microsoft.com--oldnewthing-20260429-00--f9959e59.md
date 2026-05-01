---
title: "Developing a cross-process reader/writer lock with limited readers, part 2: Taking turns when being grabby"
url: "https://devblogs.microsoft.com/oldnewthing/20260429-00/?p=112286"
fetched_at: 2026-05-01T07:13:05.339297+00:00
source: "devblogs.microsoft.com/oldnewthing"
tags: [blog, raw]
---

# Developing a cross-process reader/writer lock with limited readers, part 2: Taking turns when being grabby

Source: https://devblogs.microsoft.com/oldnewthing/20260429-00/?p=112286

Last time, we built a cross-process reader/writer lock with a cap on the number of readers
, but I noted that there was still a problem.
The problem occurs when two threads both try to acquire the lock exclusively. In that case, both threads try to claim all the tokens. And the problem is that they can get into a stalemate, where one thread has half of the tokens, and the other thread has the other half, and neither side will back down, resulting in an impasse.
We can avoid this by serializing all the attempts to acquire exclusive locks. That way, there is at most one greedy thread at a time.
HANDLE sharedSemaphore;
HANDLE sharedMutex;
void AcquireExclusive()
{
WaitForSingleObject(sharedMutex, INFINITE);
for (unsigned i = 0; i < MAX_SHARED; i++) {
        WaitForSingleObject(sharedSemaphore, INFINITE);
    }
ReleaseMutex(sharedMutex);
}

bool AcquireExclusiveWithTimeout(DWORD timeout)
{
    DWORD start = GetTickCount();
WaitForSingleObject(sharedMutex, INFINITE);
for (unsigned i = 0; i < MAX_SHARED; i++) {
        DWORD elapsed = GetTickCount() - start;
        if (elapsed > timeout ||
            WaitForSingleObject(sharedSemaphore, timeout - elapsed) == WAIT_TIMEOUT)) {
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
Okay, this avoids the problem of two exclusive acquisitions, but we still have a problem: Exclusive access throughput is poor. We’ll look at this next time.
