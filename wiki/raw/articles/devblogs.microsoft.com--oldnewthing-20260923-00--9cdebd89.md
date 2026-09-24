---
title: "When working with Win32"
url: "https://devblogs.microsoft.com/oldnewthing/20260923-00/?p=112726/"
fetched_at: 2026-09-24T10:01:16.137605+00:00
source: "devblogs.microsoft.com/oldnewthing"
tags: [blog, raw]
---

# When working with Win32

Source: https://devblogs.microsoft.com/oldnewthing/20260923-00/?p=112726/

Some time ago, I was looking at a pull request, and saw that the code was manually calculating the “number of minutes since the last change” by doing annoying math.
static const DWORD c_TicksPerSecond = 10000000;
static const DWORD c_SecondsPerMinute = 60;

uint64_t FileTimeToULongLong(FILETIME time)
{
    ULARGE_INTEGER value;

    value.LowPart = time.dwLowDateTime;
    value.HighPart = time.dwHighDateTime;

    return value.QuadPart;
}
DWORD GetMinutesSinceLastChange()
{
    FILETIME now;
    GetSystemTimeAsFileTime(&now);

    uint64_t now64 = FileTimeToULongLong(now);
    uint64_t last64 = FileTimeToULongLong(m_lastChange);

    if (now64 < last64) {
        return 0;
    }

    uint64_t diff = last64 - now64;
    return static_cast<DWORD>(diff /
        (static_cast<uint64_t>(c_dwSecondsPerMinute) *
         static_cast<uint64_t>(c_TicksPerSecond)));
}
Okay, first of all, we have helpers in the Windows Implementation Library (wil) to save you a lot of typing and calculating weird constants.
DWORD GetMinutesSinceLastChange()
{
    FILETIME now;
    GetSystemTimeAsFileTime(&now);

    int64_t now64 = wil::filetime::to_int64(now);
    int64_t last64 = wil::filetime::to_int64(m_lastChange);

    if (now64 < last64) {
        return 0;
    }

    int64_t diff = last64 - now64;
    return static_cast<DWORD>(diff / wil::filetime_duration::one_minute);
}
But even better: You have
std::chrono
now. C++/WinRT has already written the weird constants for you, and the C++ standard library has all the convenient helper functions.
DWORD GetMinutesSinceLastChange()
{
    auto last = winrt::clock::from_FILETIME(m_lastChange);
    auto now = (std::max)(winrt::clock::now(), last);
    return (now - last) / 1min;
}
