---
title: "You shouldn't change the style of a Win32 static control after it has been created"
url: "https://devblogs.microsoft.com/oldnewthing/20261105-00/?p=112835/"
fetched_at: 2026-11-06T10:01:09.297246+00:00
source: "devblogs.microsoft.com/oldnewthing"
tags: [blog, raw]
---

# You shouldn't change the style of a Win32 static control after it has been created

Source: https://devblogs.microsoft.com/oldnewthing/20261105-00/?p=112835/

Win32 classic static controls come with a bunch of possible styles to describe what it renders and how. Maybe it’s text. Maybe it’s an image. Maybe it’s just a solid color.
What happens if you create the control with one style and then change the style later?
Don’t do that.
The Win32 classic static control was originally written in the early 1980s for Windows 1.0, and back then, people didn’t play funny games like changing a static control from text to bitmap. They barely had enough memory to add two numbers together!
The Win32 static control decides what it is when it is created, and it doesn’t listen to the
WM_
STYLE­CHANGED
message to learn that somebody told it to change its clothes. Mostly because the
WM_
STYLE­CHANGED
message wouldn’t exist for another decade. It assumes that the style doesn’t change for the lifetime of the control.
If you change the style on the fly, say, from image to text, what happens is that the control starts up and realizes that it’s an image, so it loads the image. And then when it is destroyed, it checks what it is, and hopefully it still says “You’re an image,” so it frees the image. But if you secretly changed it to “You’re text”, it says “Well, in that case, I don’t have to free an image,” and the image gets leaked.
This behavior has remained unchanged in the static control for backward compatibility. There are almost certainly programs that “know” about this behavior when they change an image static control to a text static control, so they “fix” the problem by deleting the leaked image. If the leak were fixed in the static control, this would result in a double-delete bug.
So just stay away from the electrified wire. If you need to change the style of a static control, destroy it and create a new one with the new style, or create two static controls (say, one image and one text) and hide one and show the other depending on which one you need.
