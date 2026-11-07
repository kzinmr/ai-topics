---
title: "About the illuminated Apple logo on MacBook Pro with PROLED XDR Display"
url: "https://support.apple.com/en-us/149248"
fetched_at: 2026-11-07T10:01:29.942174+00:00
source: "daringfireball.net"
tags: [blog, raw]
---

# About the illuminated Apple logo on MacBook Pro with PROLED XDR Display

Source: https://support.apple.com/en-us/149248

The Apple logo behind the built-in display is illuminated whenever the Mac is awake. It automatically dims or brightens based on the brightness level of the built-in screen and the lighting conditions detected by the computer’s ambient light sensor. For all screen-brightness levels, the Apple logo will be dimmer in a dim room and brighter in a bright room.
Requires MacBook Pro with PROLED XDR Display
To make the Apple logo dark in all lighting conditions, you can turn off its illumination using Terminal, which is in the Utilities folder of your Applications folder. You can also
use Spotlight
to find and open it.
Type or paste this command in Terminal, then press Return:
sudo defaults write com.apple.CoreBrightness LEBacklightMode -int 0
Type your administrator password when prompted (Terminal doesn’t show the password as it's typed), then press Return. Logo illumination turns off immediately.
This change affects all macOS user accounts, including when starting up from macOS Recovery. When
migrating to a new Mac
, the setting transfers to the new Mac.
To turn logo illumination on again, enter this command in Terminal:
sudo defaults delete com.apple.CoreBrightness LEBacklightMode
Reinstalling macOS
also turns illumination back on.
Published Date:
November 05, 2026
