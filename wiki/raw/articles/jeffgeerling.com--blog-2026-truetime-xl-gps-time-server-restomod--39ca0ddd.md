---
title: "Rebuilding a 1995 GPS Time Server so I don't get Telstra'd"
url: "https://www.jeffgeerling.com/blog/2026/truetime-xl-gps-time-server-restomod/"
fetched_at: 2026-09-05T10:00:48.818645+00:00
source: "jeffgeerling.com"
tags: [blog, raw]
---

# Rebuilding a 1995 GPS Time Server so I don't get Telstra'd

Source: https://www.jeffgeerling.com/blog/2026/truetime-xl-gps-time-server-restomod/

In June I purchased
this TrueTime XL-AK time server
, so I could learn more of the history of GPS-based time.
I received it on June 22, and just 16 days later a similar GPS time server
took down Australia's cell service for 12 hours
! I made a
short video about it
but put off digging into the TrueTime... until now.
Over the past couple weeks, I've 'restomodded' this device with a Raspberry Pi, to build a stratum 1 NTP Time server, which I'd like to eventually add to the
NTP Pool
. I found a way to drop in a Pi 5 and GNSS HAT, display the time and GPS status on the built-in 16x2 LCD, show the status on the bicolor LED, and make this box useful again.
I lay out more of the hardware details in today's YouTube video:
But in this post, I'll show how I configured the Raspberry Pi to work as a stratum 1 NTP time server with:
I used a Raspberry Pi 5 with 4GB of RAM, but there's no reason you can't use a $44 Pi 5 with 1GB of RAM for this project (if all you're running on it are timing services for a small network).
My immediate need for this server is to provide time services for
VCF Midwest
next weekend. As with all my projects, I have parts gathered for months, and assembly usually waits until a week or two before a deadline :)
Jimmy Paputto L1 GNSS HAT
I mounted the GNSS HAT on top of the Pi using the included GPIO riser and mounting screws. I used screws on the bottom to secure a
Raspberry Pi Bumper
underneath.
After flashing Pi OS 'Lite' (no GUI) to a microSD card, I built the Jimmy Paputto GNSS HAT software from source:
sudo apt -y install build-essential cmake libgpiod-dev python3-dev
git clone https://github.com/jimmypaputto/gnsshat.git
cd gnsshat
mkdir -p build && cd build
cmake .. -DBUILD_PYTHON=ON -DBUILD_EXAMPLES=ON
make -j$(nproc)
sudo make install
This software includes a GNSS data bridge to transfer NMEA sentences (the time and date information) to
gpsd
and
chrony
; you could also plug the GNSS HAT's USB-C port into a USB-A port on the Pi and access the u-blox NEO-M9N directly.
After the install was complete, I followed the guide to set up a
Raspberry Pi Time Server with PPS
.
Chrony
When it was time to configure Chrony, I used the following settings inside
/etc/chrony/chrony.conf
:
# GNSS + PPS time server
# GPS time via shared memory from gpsd
refclock SHM 0 offset 0.0 delay 0.05 refid NMEA noselect
# PPS — precise edge timing
refclock PPS /dev/pps0 refid PPS lock NMEA prefer trust poll 3 filter 16
# The Pi's XO is fairly stable, but not quite TCXO-level.
maxclockerror 0.5
# Hardware timestamping for more precision on Pi 5
hwtimestamp *
# Fallback internet pools
pool 0.pool.ntp.org iburst
pool 1.pool.ntp.org iburst
# Allow all LAN clients
allow 10.0.0.0/16
# Allow requests routed through Twingate container.
allow 172.17.0.0/16
maxupdateskew 100.0
makestep 1000 3
rtcsync
# Ignore clock updates >100ms (fixes gpsd reporting time 1s off every ~31 min)
maxchange 0.1 1 -1
I'm accessing my NTP demo setup remotely through
Twingate
, since I'm dealing with multiple WANs while testing, and it was easier to punch through things like double NAT with a proxying service.
Restart
chrony
after updating the configuration:
sudo systemctl restart chrony
Verify everything's working with:
chronyc sources -v
chronyc tracking
After measuring chrony metrics for a few days, I tweaked parts of the configuration to match my setup—for
maxclockerror
, I reduced it from the default because I was able to stabilize the oscillator frequency with some tweaks to the Pi's settings.
Pi Timekeeping Tweaks
The changes I found especially helpful:
Running the fan at a constant duty cycle
Forcing the Pi's SoC to run full speed with
force_turbo
Pinning the kernel PPS interrupts to CPU core 4 (after isolating that core)
Insulating the bottom of the Pi so the oscillator is in a more stable thermal environment
Insulating the rest of the Pi by enclosing it in the TrueTime enclosure
Some other things I tried didn't seem to have a measurable impact, at least over 6-12 hour testing periods.
I highly recommend reading
this Austin's Nerdy Things blog post
if you're interested in this stuff.
Stable Pi Clock
To force the Pi to stay at 2.4 GHz for a more stable thermal environment (since the oscillator is near the SoC, and it is impacted significantly by bursty CPU activity), you can set the
force_turbo
option. This burns maybe 1W more power continuously, but is worth it if you want a stable oscillator frequency (important for timing).
Add the following inside
/boot/firmware/config.txt
and reboot the Pi:
# Force performance governor so CPU maintains a more stable temperature.
force_turbo=1
Consistent Fan Speed
I spent a while testing things like
NTPheat
to stabilize the Pi's SoC temperature. Tools like that work, especially if you insulate your Pi. Airflow, especially that from HVAC systems, makes the Pi's oscillator go wild—stable clocks like consistent drift, because it's measurable.
But after a lot of testing, I found having the bottom of the Pi insulated (that's where the crystal lives, physically), enclosing the rest of the Pi, and running with a consistent fan speed and large heatsink, made for a more stable frequency, at least in a few 6-12 hour cycles so far
.
I commited the little
fan-control
utility I'm using in my Time Pi repository, in case you want to use it. A 75% duty cycle actually performed a little better... but the fan was just noisy enough to annoy me at that level when I was testing this at my desk... so 50% it is.
Onboard RTC Battery Charging
Assuming you have the official
ML2020 Raspberry Pi RTC battery
installed, configure the onboard RTC's battery charging circuit:
Plug in a Pi 5 RTC Battery to the appropriate header
Add
dtparam=rtc_bbat_vchg=3000000
to
/boot/firmware/config.txt
and reboot
(Read the battery voltage with
vcgencmd pmic_read_adc BATT_V
)
The RTC battery won't help the Pi's timekeeping stability, but it does help keep the Pi within a second or two of real-time if you shut it down for any period of time. (As long as you don't keep it off for months at a time!)
Isolating PPS interrupts on a single CPU core
I wanted to see if dedicating one CPU core entirely to handling PPS interrupts would help, and it did. One reason serious timing gear runs on FPGAs (or uses PHCs like in timing-specific network cards) is deterministic PPS handling. If you use the Linux kernel's PPS functionality, even in the best case you're dealing with hundreds of nanoseconds of delays waiting for the interrupt to be dealt with!
To help give PPS a fighting chance, you can assign PPS handling to a single dedicated CPU core. In my case, I wanted to put all PPS handling on CPU3 (the 4th core).
Edit
/boot/firmware/cmdline.txt
and add
isolcpus=3
to the options
Reboot:
sudo reboot
Create
/usr/local/sbin/pin-pps-irq.sh
(
chmod +x
it) with the contents:
#!/bin/sh
irq
=
$(
awk
'/pps@/ {sub(":","",$1); print $1}'
/proc/interrupts
)
[
-n
"
$irq
"
]
&&
echo
3
> /proc/irq/
$irq
/smp_affinity_list
Create
/etc/systemd/system/pin-pps-irq.service
with the contents:
[Unit]
Description=Pin PPS GPIO IRQ to isolated CPU3
After=multi-user.target
[Service]
Type=oneshot
ExecStart=/usr/local/sbin/pin-pps-irq.sh
[Install]
WantedBy=multi-user.target
Start the service and enable it on boot:
systemctl enable --now pin-pps-irq.service
.
Confirm it's working:
$ watch grep pps /proc/interrupts
# You should see the fourth column incrementing once per second:
166:        860          0          0         34 pinctrl-rp1   5 Edge
[email protected]
Monitor your chrony statistics for a period of 1-6 hours and see how much impact it makes. In my case, it was noticeable, but not game-changing.
Monitoring and Physical Time Display
To monitor the performance of my Pi (which by this point I was calling 'TrueTime Pi' in honor of the chassis inside which it was installed), I built
chrony-dashboard
, with assistance from Claude.
Whipping up quick dashboards is an easy win for AI tooling. I never enjoyed working with frontend graphing libraries, and building a script to parse data out of a shell command and jam it into a SQLite database periodically is not something that excites me.
Let AI do that, and I can focus on the fun parts like presentation and performance!
A web UI is one thing, I also used Claude to help me map GPIO pins to the vintage Densitron LCD on the front of the TrueTime, and I wound up with this project:
densitron-lcd
The photo at the top of this post shows the LCD working with a solid GPS fix. For wiring, I actually used a technique I'd never tried before—
wire wrapping
.
With the Pi and the GNSS HAT, there wasn't enough vertical clearance inside the TrueTime chassis for dupont connections—not that I enjoy those connectors anyway! I was considering soldering wires straight to GPIO pins but found out about wire wrapping while researching other low-profile methods to connect to standard square pins.
Apparently the process forms a weld around the corners of the post, and results in a gas-tight electrical connection with lower resistance than solder! If the joints survive the trip up to Chicago, I might use this technique a little more frequently for prototyping.
I used
this wire wrap tool
and
this 30 AWG wire wrapping wire
.
Time and Daytime Protocols
As an easter egg, since I'll be using this TrueTime Pi server at VCF Midwest, I thought I'd also supply RFC 867/868 Time and Daytime services on the network.
Setting that up is as easy as:
sudo apt install xinetd
sudo systemctl enable xinetd
sudo nano /etc/xinetd.d/time
-> service time tcp set disable to "no"
-> service time udp set disable to "no"
sudo nano /etc/xinetd.d/daytime
-> service daytime tcp set disable to "no"
-> service daytime udp set disable to "no"
sudo systemctl restart xinetd
My previous blog post goes into the
history of these two pre-NTP protocols
.
AppleTalk / netatalk for Timelord Server
Another fun demo is old Macs getting time via AppleTalk! This is courtesy of
timelord
, which is easy to run as part of
netatalk
, alongside other services like running an AppleShare service for file serving to vintage Macs.
On my Pi running Pi OS, setup was simple. First enable AppleTalk services in the Linux kernel:
# Enable AppleTalk protocol and ensure it's loaded.
sudo modprobe appletalk
&&
lsmod
|
grep appletalk
# Add AppleTalk protocol to boot modules.
echo appletalk
|
sudo tee
/
etc
/
modules
-
load
.
d
/
appletalk
.
conf
# Create a folder for netatalk.
mkdir
-
p
~/
netatalk
/
afpshare
Then, assuming you have
Docker installed
, create a Docker Compose file (
nano ~/netatalk/compose.yml
) with the following contents:
services:
netatalk:
image: netatalk
/
netatalk:latest
container_name: netatalk
restart: unless
-
stopped
network_mode: host
cap_add:
-
NET_ADMIN
volumes:
-
./
afpshare:
/
mnt
/
afpshare
-
/
var
/
run
/
dbus:
/
var
/
run
/
dbus
environment:
AFP_USER: myname
AFP_PASS: mypass
AFP_GROUP: afpusers
ATALKD_INTERFACE: eth0
INSECURE_AUTH:
"1"
AFP_EXTMAP:
"1"
DISABLE_TIMEMACHINE:
"1"
SERVER_NAME:
"TrueTime Pi"
TZ: America
/
Chicago
Go into the netatalk directory you created, and start the container:
cd ~/netatalk && docker compose up -d
Any other Classic Mac on the network should be able to use Tardis for time services (it's a Chooser plugin and runs once at boot) or AppleShare to connect to the
TrueTime Pi
server.
You can confirm it's working with
docker exec [container name] nbplkup
. This should return a list of services including
AFPServer
and
TimeLord
.
Conclusion
In the end, I'm happy with how this all turned out. I have the Pi securely mounted in a way I can easily swap back to the original TrueTime hardware, just by re-plugging two connectors inside.
If you'd like to replicate this build... be my guest. I like this enough I may take it even further—two more things I'd like to do:
Design a PCB with an
SMT GPIO Header
so I can still have a low-profile setup, but with even easier swappability (wire wrapping is fun, but also tedious to re-do).
Get the TrueTime keypad working, so I can cycle through displays for Time, GPS, Chrony, and network information.
