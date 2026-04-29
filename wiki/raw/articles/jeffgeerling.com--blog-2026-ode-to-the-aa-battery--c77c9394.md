---
title: "Ode to the AA Battery"
url: "https://www.jeffgeerling.com/blog/2026/ode-to-the-aa-battery/"
fetched_at: 2026-04-29T07:02:14.138827+00:00
source: "jeffgeerling.com"
tags: [blog, raw]
---

# Ode to the AA Battery

Source: https://www.jeffgeerling.com/blog/2026/ode-to-the-aa-battery/

Recently
this post from @Merocle
caught my eye:
I'm fixing my iFixit soldering station. I haven't used it for a long time and the battery has gone overdischarge. I hope it will come back to life. Unfortunately, there are no replacements available for sale at the moment.
Devices with built-in rechargeable batteries have been bugging me a lot lately. It's convenient to have a device you can take with you and use anywhere. And with modern Li-ion cells, battery life is remarkable.
But for years, I've noticed the same thing happening to many devices as Merocle mentions above:
I purchase the device, charge it to 100%, use it a bit.
Knowing Li-ion cells are better off in the 40-80% range, I store the device with the battery at that charge level.
The next time I go to use the device (a few months later), it won't power on.
I plug the device in to charge, and 1 in 4 times the device won't start charging!
One problem is many devices don't have a proper BMS integrated into the charging circuit, that will cut power
before
the battery is below a critical threshold. Li-ion cells start to have problems below 3V, and often suffer permanent damage below 2.5V.
Devices from even the most stalwart right-to-repair companies suffer from undervoltage issues.
You
can sometimes revive 'dead' Li-ion batteries
, but I don't recommend it unless you know what you're doing.
Assuming most people
don't
know what they're doing, when they pull out a piece of gear that won't turn on and has no obvious way of being repaired (especially with odd pouch-cell batteries, much less 18650 cells), these devices will
most often end up in the trash
. Or if you're
lucky
, some people will try recycling them.
Enter the AA
Because of this trend, if I need portability, I look for devices that use AA and AAA batteries.
Each year for the past 14 years, I buy sets of
Panasonic eneloop batteries
to replace disposable AA batteries as they die. Eneloops have around 2000 mAh of capacity (versus 2100+ mAh for good alkaline batteries
), and run at a nominal 1.2V instead of the 1.5V of alkaline batteries.
But they can be recharged. Over and over. They can be pulled out of a device, with new batteries swapped in quickly. For long term storage, I can pop the batteries out and use them in
other
devices.
So far, across 128 batteries, I have not had a single incident of leakage, fire, etc., and even the cells I reserve for outdoor use (in devices that go from -12°F in the winter to 105°F+ in the summer) are still holding a charge, over a decade later.
Only
one
cell has had to be retired, out of all the eneloops I've purchased.
What prompted me to write this post is the soldering project I worked on during this weekend's snowstorm.
Universal Standards
I was putting together
this clock
at my workbench, and at one point I needed to determine which resistor was 100KΩ and which was 1MΩ. I pulled out my Fluke multimeter, inserted two AAA batteries I had sitting on my bench (I keep 8 AA and 8 AAA batteries charged and ready at my workbench, and don't store them in my tools), and measured the resistors.
Upon doing so, I realized the clamp meter I was using (
Fluke 323 True RMS Clamp Meter
) only measures between 400-4000Ω, so I switched to my old Craftsman meter that worked a treat—and uses a replaceable 9V battery!
It would be faster to leave the batteries in my tools, but over 40 years of sacrificing devices to alkaline cell leakage, it's my habit not to. So far I've never had leakage problems with the eneloops, but old habits die hard.
When I put away the meter, I noticed my wife's and old Sony Walkman sitting nearby. Just for fun, I popped in two AA batteries.
My wife had both a
WM-EX150
(made in 1995) and a
WM-FX281
. These are 31 and 25 years old, respectively—and outside the rubber belts being shot, the devices both work. The radio works good as new, and it would play cassettes again after a little maintenance.
The AAs might not last 32 hours, and the Walkman doesn't fit in tight jeans pockets, but they can still be as useful today as they were decades ago.
Looking at my stack of old tech,
every
device uses one of the standard AA, AAA, or C-sized batteries. And thinking of all the new devices I've purchased, the ones that worry me the least (regarding fire safety, and whether they're work the next time I pull them out)... are the ones with easily-replaceable batteries.
No Batteries at All
If I don't need portability, I prefer USB-C powered tools (with no battery). USB-C is ubiquitous enough I
always
have a plug available with at least 5, 9, or 12V of power.
At every workbench and desk, and in my car and backpack, I have either USB battery packs, or wall plugs, that supply any voltage a device would need, and can supply up to 100W (sometimes
more
) through a small USB-C connector.
If I truly need portability, I can rubber-band a battery pack to the device I'm using.
It's not always ideal, and I wouldn't want a smartphone with such a battery pack, but many of my battery-less devices will outlive me, I am sure, with no risk of
burning down my house
.
Energy Density and Weight
There
are
cases where the energy density, portability, and weight tradeoffs of traditional battery cells don't work out: laptops, tablets, smartphones, watches, extremely lightweight computer mice...
Considering wireless input devices, though, Apple's
1st gen Magic Trackpad
was AA-powered. Apparently Apple considered battery swaps so convenient they didn't even include a USB or Lightning connector
!
I can understand when you need a more exotic or thin layout that doesn't lend itself well to cylindrical battery cells. There are
laptops that exist with exposed 18650 cells
, but they're certainly not for everyone (unless you like portable computing
like it's 1999
).
As I build my own devices, I find myself relying on USB power (if the device lives near a desk or workbench), or integrated
AA battery holders
(if the device is meant to be portable). Not having to keep a few dozen cheap Li-ion packs sitting in close proximity to my
sand bucket
is a neat side-benefit.
