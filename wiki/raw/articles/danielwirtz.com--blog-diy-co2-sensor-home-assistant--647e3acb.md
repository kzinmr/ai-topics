---
title: "DIY CO2 Sensor in Home Assistant"
url: "https://danielwirtz.com/blog/diy-co2-sensor-home-assistant"
fetched_at: 2026-11-01T10:01:33.044923+00:00
source: "danielwirtz.com"
tags: [blog, raw]
---

# DIY CO2 Sensor in Home Assistant

Source: https://danielwirtz.com/blog/diy-co2-sensor-home-assistant

Since a few months, I have
Home Assistant
running in my house. It’s a fun hobby and an absolute rabbit hole of possibilities to automate every nook and corner of your home. Early in my learning about Home Assistant, I saw posts from people who had connected sensors to monitor their CO₂ levels in the office or bedroom.
This is interesting to monitor, especially in small rooms, because even moderate CO₂ levels, between 800 and 1,200 parts per million (ppm), are often linked to increased drowsiness, a small drop in attention. If levels rise higher — between 1,200 and 2,500 ppm — it can
effect sleep
and cognitive performance.
There are some off-the-shelf CO₂ sensors with
Zigbee
/
Home Assistant
support, but they can be pricey. After some reading and research, I found
this article with instructions to build a DIY CO₂ sensor
by ordering seperate parts and assembling them.
This was my first electronics project — an easy one, since no soldering was needed. I ordered an
ESPHome
board (an ESP8266 in my case) and an SCD40 CO₂ sensor from
AliExpress
. I used the links in the original article to find the parts, and they both arrived within a month.
The setup took about an hour. First, I connected the pins to the right places on the boards — the instructions made this straightforward. Then, I plugged the board into my MacBook with a USB‑C cable and installed the
ESPHome add-on in Home Assistant
. That allowed me to flash the device and join it to the Wi‑Fi network.
Once it was online, I replaced the config file with the one from the article. The CO₂ devices then appeared in Home Assistant, and I could read the CO₂, temperature, and humidity sensors.
When I put the CO₂ monitor in the bedroom, it’s obvious when someone’s in the room (for example, reading during the day) and especially when they go to sleep.
You can see CO₂ rise sharply around 11PM (going to bed), level off around 1AM, and then fall rapidly just before 8AM when we woke up, opened the window, and left the room.
I'm going to experiment a bit more to see how CO2 levels change and how that links to a good night's sleep. I may also put the CO₂ sensor on my work desk, since I can imagine levels rising after a few hours of focused work if I forget to open the windows.
