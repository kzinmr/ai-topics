---
title: "WebKit always enables the Copy menu item in every app"
url: "https://lapcatsoftware.com/articles/2026/6/5.html"
fetched_at: 2026-06-25T07:01:40.958549+00:00
source: "daringfireball.net"
tags: [blog, raw]
---

# WebKit always enables the Copy menu item in every app

Source: https://lapcatsoftware.com/articles/2026/6/5.html

Previous:
Can you reproduce this App Store Connect bug?
Articles index
WebKit always enables the Copy menu item in every app
June 24 2026
WebKit, to quote
its website
, “is the web browser engine used by Safari, Mail, App Store, and many other apps on macOS, iOS, and Linux.” Obviously, Safari uses WebKit to display web pages, but did you know that Mail app uses WebKit to display email messages? This is true not just for HTML emails but also for plain text format emails. There are a couple of ways to reveal the presence of WebKit in Mail, both of which may be bugs. If you disable “Auto-play animated images” in the Accessibility pane of System Settings, then when you open the contextual menu in a Mail app message or in a Safari web page, you’ll see the “Play All Animations” contextual menu item. In Mail, “Play All Animations” is the only item in the menu, suggesting to me that Apple engineers did not expect a contextual menu there. This behavior occurs on macOS Sequoia, at least; I haven’t yet tested Mail on Tahoe, because I’m avoiding that update, due to Liquid Glass.
The second way to see WebKit in Mail app is mentioned in the title of this blog post. Several weeks ago, John Gruber of
Daring Fireball
asked me whether I could reproduce an issue he was seeing in Safari: when a web page is focused, the Copy menu item in the main menu is always enabled, regardless of whether there’s anything selected in the web page. I could indeed reproduce that issue, and it turns out to be the fault of WebKit. The issue also occurs in Mail app, when an email message is focused.
On Apple platforms, WebKit is a public API, used by third-party apps in addition to Apple’s first-party apps. RSS readers such as
NetNewsWire
and
Vienna
, preferred by Gruber and myself, respectively, use WebKit to display articles from RSS feeds. And sure enough, both apps exhibit the same issue: the Copy menu item is always enabled when an article is focused.
What happens if you copy and paste from a WebKit WebView with no selection? Nothing happens, nothing is pasted. However, technically speaking, the clipboard is not empty.
The Clipboard Viewer app, pictured above, is included in the Additional Tools for Xcode, which can be downloaded from the
Apple Developer website
. The
com.apple.webarchive
and “Apple Web Archive pasteboard type” items in the above list are identical binary property lists (indicated by the prefix
bplist
). Here’s the plist transformed into XML:
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
<plist version="1.0">
<dict>
	<key>WebMainResource</key>
	<dict>
		<key>WebResourceData</key>
		<data>
		PCFET0NUWVBFIGh0bWw+
		</data>
		<key>WebResourceFrameName</key>
		<string></string>
		<key>WebResourceMIMEType</key>
		<string>text/html</string>
		<key>WebResourceTextEncodingName</key>
		<string>UTF-8</string>
		<key>WebResourceURL</key>
		<string>https://daringfireball.net/</string>
	</dict>
</dict>
</plist>
When you copy from a web page in Safari with no selection in the page, you get a representation of the page that includes the page URL, as well as some (useless) data in Base64 format:
% echo 'PCFET0NUWVBFIGh0bWw+' | base64 -d
<!DOCTYPE html>
Unfortunately, no other app seems to understand this web archive pasteboard type. The
com.apple.WebKit.custom-pasteboard-data
item also includes the web page URL wrapped in some weird format that no other app seems to understand. The other pasteboard types in the list are actually empty, with zero bytes of data. Thus, when you paste, you get nothing.
Copying from an email message in Mail app generates similar clipboard contents:
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
<plist version="1.0">
<dict>
	<key>WebMainResource</key>
	<dict>
		<key>WebResourceData</key>
		<data>
		</data>
		<key>WebResourceFrameName</key>
		<string></string>
		<key>WebResourceMIMEType</key>
		<string>text/html</string>
		<key>WebResourceTextEncodingName</key>
		<string>UTF-8</string>
		<key>WebResourceURL</key>
		<string>x-webdoc://48BE32AC-8EEF-4630-8C5E-BC292F17A707</string>
	</dict>
</dict>
</plist>
In this case there’s no resource data, and the page URL with an
x-webdoc
scheme is seemingly useless and can’t be opened:
% open 'x-webdoc://48BE32AC-8EEF-4630-8C5E-BC292F17A707'
No application knows how to open URL x-webdoc://48BE32AC-8EEF-4630-8C5E-BC292F17A707 (Error Domain=NSOSStatusErrorDomain Code=-10814 "kLSApplicationNotFoundErr: E.g. no application claims the file" UserInfo={_LSLine=1796, _LSFunction=runEvaluator}).
Needless to say, none of this is an expected or a good user experience. Since
I frequently file WebKit bug reports
, I decided to file a bug report on behalf of Gruber:
Copy main menu item is enabled with no selection in the web page
. I subsequently learned that the first appearance of the bug was January 2025 in
the WebKit source code
, February 2025 in
Safari Technology Preview 213
, and March 2025 in
Safari 18.4
, as a result of attempting to fix another bug,
document.execCommand("copy") only triggers if there is a selection
, reported in 2016, nine years prior!
I’ve blogged about
document.execCommand("copy")
before:
Web pages can overwrite your system clipboard without your knowledge
. In that blog post I described how web pages can exploit a seemingly innocuous user gesture to overwrite the system clipboard. My web browser extension
StopTheMadness Pro
can now prevent this via the website option “Protect clipboard write.” Of course the
document.execCommand("copy") API
was not designed to be malicious, and there are prominent, legitimate use cases such as the Copy button in the YouTube Share popup. Below is a demonstration, a button that when clicked writes “This is a test” to your clipboard.
Test
The YouTube Share button and similar controls, for example “Copy link” on Twitter/X tweets, ought to work without a text selection on the web page. That was the bug reported back in 2016 and fixed in 2025. Nonetheless, the Copy menu item in the main menu of an app should
not
be enabled if there’s no selection. That is the bug I recently reported. The two cases are distinct: one is on the web, the other is native to the Mac; one is implemented in JavaScript, the other implemented in Objective-C or Swift. Web pages and Mac apps have different rules and conventions. Moreover, it’s crucial to recognize that the Copy menu item in the Safari main menu does not call
document.execCommand("copy")
, not even when the YouTube Share popup is displayed. Unlike the HTML Copy button, the Safari native Copy menu item generates useless web archive clipboard contents, due to the bug I reported.
Sadly, my bug report was closed with the resolution “won’t fix.” The refusal appears to be based on a misunderstanding:
The point of
https://commits.webkit.org/288559@main
is to enable copy regardless of the selection state. Either copying is enabled or not. We can't have it both ways.
This rigid response should cause your Spidey-Sense to tingle! Doesn’t the statement sound very much like a false dichotomy? We actually can have it both ways. As a longtime Mac developer, I’m quite familiar with how an app’s main menu items are enabled and disabled. (Other Mac developers may be familiar with my “working without a nib” series of blog posts explaining how to construct the menu programmatically.) Typically, the state of the menu items is governed by the
validateMenuItem:
AppKit method. Nothing would prevent WebKit from handling the native
validateMenuItem:
and the JavaScript
document.execCommand("copy")
differently, using slightly different algorithms for each case. There’s no good reason why the special workaround for JavaScript
execCommand
has to leak into the native main menu of Mac apps.
I reopened my bug report and argued my case, but given the initial response, I fear that the report may continue to be treated dismissively. This is why I’m blogging about the bug, to raise awareness and hopefully bring public pressure. It always sucks when Apple engineers convince themselves that a bug is a feature.
Articles index
Previous:
Can you reproduce this App Store Connect bug?
