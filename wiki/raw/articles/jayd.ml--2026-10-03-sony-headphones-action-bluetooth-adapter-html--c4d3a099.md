---
title: "Connect Sony WH-1000XM3 on Arch Linux and a buggy UGREEN Bluetooth adapter"
url: "https://jayd.ml/2026/10/03/sony-headphones-action-bluetooth-adapter.html"
fetched_at: 2026-10-04T10:01:14.105539+00:00
source: "jayd.ml"
tags: [blog, raw]
---

# Connect Sony WH-1000XM3 on Arch Linux and a buggy UGREEN Bluetooth adapter

Source: https://jayd.ml/2026/10/03/sony-headphones-action-bluetooth-adapter.html

Tried to connect to my Sony WH-1000XM3 headphones on Arch Linux KDE, it would
try and connect but fail with
The setup of WH-1000XM3 failed
.
I have a
UGREEN USB Bluetooth 5.3 Adapter
adapter, which contains an Actions ATS2851 chipset.
Apparently this is a
known chipset quirk with Sony headphones and this adapter
.
Attempting to connect manually with bluetoothctl would just stall out:
bluetoothctl]> scan bredr
SetDiscoveryFilter success
Discovery started
[CHG] Controller F4:4E:FC:77:8F:36 Discovering: yes
[NEW] Device 54:3A:D6:26:7A:E4 [TV] Samsung Q80AA 65 TV
[NEW] Device CC:DE:AD:BE:EE:FF WH-1000XM3
[bluetoothctl]> scan off
Discovery stopped
[CHG] Device CC:DE:AD:BE:EE:FF RSSI is nil
[CHG] Device 54:3A:D6:26:7A:E4 RSSI is nil
[CHG] Controller F4:4E:FC:77:8F:36 Discovering: no
[bluetoothctl]> pair CC:DE:AD:BE:EE:FF
Attempting to pair with CC:DE:AD:BE:EE:FF
[CHG] Device CC:DE:AD:BE:EE:FF Connected: yes
[DEL] Device 54:3A:D6:26:7A:E4 [TV] Samsung Q80AA 65 TV
[WH-1000XM3]>
The Workaround
This only happens when you do initial pairing. If you skip
pair
it apparently works.
power off
power on
agent off
agent KeyboardDisplay
default-agent
scan bredr

(wait for headphones to appear)

scan off
trust CC:DE:AD:BE:EE:FF
connect CC:DE:AD:BE:EE:FF
I can’t find any firmware updates from UGREEN, so you’ll have to do this to
get it to pair for the first time. I reached out to their support, so we’ll see
if by some miracle they do anything about it.
