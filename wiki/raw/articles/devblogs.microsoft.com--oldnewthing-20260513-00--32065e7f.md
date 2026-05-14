---
title: "The case of the hang when the user changed keyboard layouts"
url: "https://devblogs.microsoft.com/oldnewthing/20260513-00/?p=112318"
fetched_at: 2026-05-14T07:00:37.548022+00:00
source: "devblogs.microsoft.com/oldnewthing"
tags: [blog, raw]
---

# The case of the hang when the user changed keyboard layouts

Source: https://devblogs.microsoft.com/oldnewthing/20260513-00/?p=112318

A customer reported that their program hung when the user changed keyboard layouts, say by using the
Win
+
Space
hotkey sequence. They debugged it as far as observing that the foreground window in their application received a
WM_
INPUT­LANG­CHANGE­REQUEST
, and when that message was passed to
Def­Window­Proc
, the call never returned. What’s so haunted about the
WM_
INPUT­LANG­CHANGE­REQUEST
message?
What’s so haunted about it is that the default behavior of the
WM_
INPUT­LANG­CHANGE­REQUEST
message is to change input language!
For historical (and therefore now compatibility) reasons, when a hotkey-initiated input language change request is accepted, the system applies the change to all threads of that process. This means that all UI threads of the process need to be pumping messages so that they can receive the notification that their keyboard state has changed.
In this case, the customer had a background thread that created a window but was not pumping messages. That prevented the language change from completing and caused the main UI thread to hang.
The customer wanted to know if there was a way to configure their program so that hotkey-initiated input language changes don’t require all threads to be pumping messages. But that’s trying to solve too narrow a problem. If your thread has created a window, then it must pump messages. Today it’s causing trouble with input language changes. Tomorrow, it’s going to cause problems with DDE, and the day after tomorrow, it’s going to cause problems with theme changes.
Even if you had a way to change the way language changes work, that’s just one of the problems that your non-responding thread is causing. You should fix the root cause: Either pump messages or destroy the window so that it is no longer a UI thread and is no longer obligated to pump messages.
