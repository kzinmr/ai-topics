---
title: "Gadget Review: Cheap Zigbee Environmental Sensors"
url: "https://shkspr.mobi/blog/2026/11/gadget-review-cheap-zigbee-environmental-sensors/"
fetched_at: 2026-11-24T10:01:26.526615+00:00
source: "shkspr.mobi"
tags: [blog, raw]
---

# Gadget Review: Cheap Zigbee Environmental Sensors

Source: https://shkspr.mobi/blog/2026/11/gadget-review-cheap-zigbee-environmental-sensors/

I recently read a
great blog post which tested a bunch of Zigbee Temperature / Humidity sensors
. As the Internet of Things is getting cheaper by the hour, I thought I'd treat myself to some Sonoff AirGuard TH Lite sensors - they received an honourable mention in the post and were the cheapest I could find in the UK
They are reasonably small:
Barely bigger than the two (included) AAA batteries which power them:
Those batteries are supposed to last 2 years - so check back in 2028 to see if those claims hold up. One of the reasons I got this specific model is that AAA batteries are easy to buy and I've got a bunch of rechargeable ones
somewhere
.
Under one of the batteries are some debug pads. No idea what they do of if they're useful.
I grabbed a
4 pack for £30
. In the box you also get 4 tiny lanyard straps and 4 adhesive pads. Ideally, I think the lanyard could have been longer - but it's good enough for hanging on a nail.
HomeAssistant added them instantly. Readings came in every few minutes and produced some splendid graphs like this:
The user manual was easy to follow - open back, remove plastic tab, pair - but also came with a supplemental manual which recommended waiting 30 minutes after installation to allow the sensors to self-calibrate.
One quirk to note. Although the sensor has support for dew point and vapour pressure deficit monitoring,
these are
not
available in HomeAssistant's ZHA yet
. It looks like some work is being done to make them appear. I manually added the Quirk file and they sprang to life - no re-pairing needed.
I haven't calibrated these or done anything funky - but they appear to be working well. The one in the fridge reports the temperature exactly as I would expect. I'm also impressed that it manages to do so from within a big metal box some distance away from my Zigbee dongle. The LQI was ~96 and the RSSI around -87 - both of which seemed good enough to report data regularly. It does occasionally drop off the network but seems to find its way back after a while. The sensor readings are fire-and-forget though, if the HomeAssistant doesn't get them they are lost like condensation in the rain.
Once my mesh was more fully established, the periodic drop-offs became less frequent. A quick press on the button on the sensor seemed to reconnect them.
Unfortunately, two of the sensor drained their batteries fairly rapidly. In less than two weeks, the reported battery dropped catastrophically.
The sensors worked for a couple of days with "zero" battery but then fell off the network. I've yet to work out if it was a problem with the supplied batteries or the sensors themselves. The other two sensors are still at 100% battery and reporting data regularly.
I replaced the batteries and, a few days later, was notified of a
firmware update
. The update is meant to improve battery life and stability. It installed via HomeAssistant without a problem. Since then, the batteries have reported 100%.
When these work, they are pretty much the epitome of small and boring devices. Stick them on a shelf or hang them from a hook, then never touch them until it is time to replace their batteries. In a four-pack, they're £7.50 each, which feels pretty reasonable. The measurements will vary a bit depending on where you place them in a room - but that's true of any sensor.  They integrated perfectly with HomeAssistant and are small enough to tuck away out of sight. It would be handy if they had USB-C recharging, but finding AAA batteries isn't an insurmountable problem.
