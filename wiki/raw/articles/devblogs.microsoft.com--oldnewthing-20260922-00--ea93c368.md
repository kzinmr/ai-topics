---
title: "A brief history of Windows scroll bar shortcuts"
url: "https://devblogs.microsoft.com/oldnewthing/20260922-00/?p=112719/"
fetched_at: 2026-09-24T10:01:16.147904+00:00
source: "devblogs.microsoft.com/oldnewthing"
tags: [blog, raw]
---

# A brief history of Windows scroll bar shortcuts

Source: https://devblogs.microsoft.com/oldnewthing/20260922-00/?p=112719/

For the first two decades of Windows, the scroll bar control had just a few basic operations. (For expository purposes, let’s assume that the scroll bar is vertical.) There are five mouse targets: The arrows at the ends of the scroll bar scroll by a line. The regions between the thumb and the arrows scroll by a page. And the thumb itself lets you drag the scroll bar to a specific position.
Windows 7
Windows 2000 added a right-click menu to the scroll bar. This menu gave you four options that matched existing mouse operations, two operations that matched existing keyboard operations, and a new operation.
Menu option
Mouse
Keyboard
Scroll Here
Drag thumb to position
Top
Drag thumb to start
Home
Bottom
Drag thumb to end
End
Page Up
Click in upper gutter
PgUp
Page Down
Click in lower gutter
PgDn
Scroll Up
Click on up-arrow
↑
Scroll Down
Click on down-arrow
↓
The interesting new one is “Scroll Here”: You can right-click directly on the spot you want to scroll to, and then pick “Scroll Here”. This is much more convenient if you want to scroll a long distance, since you don’t have to grab the scroll bar thumb and then drag it all the way to where you want to go. You can just focus on where you want to go and not where you are coming from.
I used this context menu a lot when I needed to jump long distances.
An even-more-hidden shortcut was added at the same time: Holding
Shift
while clicking on the scroll bar jumps the thumb directly to the spot where you clicked.
I didn’t know about this shortcut until recently. I had always used my trusty context menu.
Sadly, almost nobody uses Win32 scroll bars any more. Everybody uses frameworks that provide their own custom scroll bars.
Electron and other Web apps use the Chromium scroll bar, which doesn’t implement the context menu, but at least it does implement the
Shift
+click shortcut.
The WPF XAML framework appears to implement both the context menu
Shift
+click.
The WinUI XAML framework frustratingly has neither the context menu nor the
Shift
+click shortcut. (
Though at least one person has requested it
.)
The Qt framework has multiple customization points, so it’s really up to each app’s developer. You can enable context menus with
SH_
Scroll­Bar_
Context­Menu
, you can enable “left-click to jump to a position” with
SH_
Scroll­Bar_
Left­Click­Absolute­Position
, and you can enable “middle-click to jump to a position” with
SH_
Scroll­Bar_
Middle­Click­Absolute­Position
.
Great, so by the time I learn about a shortcut for scroll bars (
Shift
+click), the ecosystem has fragmented so much that I can’t even rely on it working.
