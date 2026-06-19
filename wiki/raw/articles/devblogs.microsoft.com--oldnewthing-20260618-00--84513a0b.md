---
title: "Why doesn't Get­Last­Input­Info() return info for the user I'm impersonating?"
url: "https://devblogs.microsoft.com/oldnewthing/20260618-00/?p=112444"
fetched_at: 2026-06-19T07:00:56.773949+00:00
source: "devblogs.microsoft.com/oldnewthing"
tags: [blog, raw]
---

# Why doesn't Get­Last­Input­Info() return info for the user I'm impersonating?

Source: https://devblogs.microsoft.com/oldnewthing/20260618-00/?p=112444

A customer had a Windows NT service process, and from that service process, they wanted to obtain the last input time for all signed-in users. Their strategy was to use
WTS­Query­User­Token()
to get the token for each user, use that token to impersonate the user, and then call
Get­Last­Input­Info()
to get the last input time for that user. Unfortunately, the function always return the last input info for the service session, and since services are not interactive, it always says that there has been no input since the system booted.
Does
Get­Last­Input­Info()
work with impersonation?
Recall that
the default answer to “Does this work when impersonating?” is “No”
. And in fact, the documentation for
Get­Last­Input­Info()
explicitly says that it doesn’t, if you read it closely.
This function is useful for input idle detection. However,
GetLastInputInfo
does not provide system-wide user input information across all running sessions. Rather,
GetLastInputInfo
provides session-specific user input information
for only the session that invoked the function
.
I underlined the important part. It reports on the last input information for the session that invoked the function. When the service impersonates, it updates its security context to align with that of the user being impersonated, but it doesn’t change the fact that that it is still running in session zero, the service session.
If you need to get last input information from another session, you will need a friend in that session to call it for you. Typically this is done by launching a helper process into the target session: The helper process collects the information you want and then sends the information to the service.
Bonus chatter
: A related question is “Does
Get­Async­Key­State
from a service?” The answer is technically yes, it works. However it probably doesn’t work the way you think. It returns the asynchronous key state for the desktop that the service is running in. And since services run in a non-interactive session, that desktop will never see any keyboard activity.
