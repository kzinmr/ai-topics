---
title: "StopTheScript"
url: "https://underpassapp.com/StopTheScript/"
fetched_at: 2026-08-07T10:19:28.563983+00:00
source: "daringfireball.net"
tags: [blog, raw]
---

# StopTheScript

Source: https://underpassapp.com/StopTheScript/

StopTheScript is a Safari extension for iOS, iPadOS, and macOS that stops all JavaScript on your selected websites. StopTheScript is the
only
Safari extension that stops
inline
JavaScript on the web page as well as externally loaded JavaScript. This is in contrast to Safari content blockers, which can only block external JavaScript, not inline JavaScript.
System Compatibility:
iOS and iPadOS 15 through 27
macOS 12 Monterey through 27 Golden Gate
Safari 17 or later is required on macOS
Demo:
If you're already using a Safari content blocker to block JavaScript, then set it to block JavaScript on this website (
underpassapp.com
), and click the button below. If the button still pops up an alert, then your JavaScript blocker is incomplete, and you need StopTheScript!
Click for inline JavaScript
Here's the code for the button:
<div>
<button id="mybutton" type="button">
Click for inline JavaScript
</button>
</div>

<script>
function MyClick(event) {
alert("JavaScript alert() is running!");
}
document.getElementById("mybutton")
.addEventListener("click", MyClick);
</script>
Noscript:
StopTheScript has a setting to bypass HTML
<noscript>
elements that can detect disabled JavaScript. Try this
test page
for a demo.
About the developer:
Jeff Johnson
, owner of
Underpass App Company
, had 15 minutes of fame for solving the
Mac OCSP appocalypse
. Before becoming an indie developer, Jeff was a longtime engineer at Rogue Amoeba Software and also worked on the open source RSS reader Vienna.
