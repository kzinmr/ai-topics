---
title: "Flock cameras are riddled with security vulnerabilities and hard-coded credentials"
url: "https://micahflee.com/flock-cameras-are-riddled-with-security-vulnerabilities-and-hard-coded-credentials/"
fetched_at: 2026-09-17T10:01:19.974615+00:00
source: "micahflee.com"
tags: [blog, raw]
---

# Flock cameras are riddled with security vulnerabilities and hard-coded credentials

Source: https://micahflee.com/flock-cameras-are-riddled-with-security-vulnerabilities-and-hard-coded-credentials/

This morning, DDoSecrets
published
an exciting new dataset: Filesystem images of the partitions from an in-use Flock ALPR camera.
404 Media
and
Wired
published a joint investigation into it. I downloaded the dataset and am now thoroughly nerd-sniped.
Hackers from a collective called stegan0gram collected the data. “Why just destroy [Flock cameras] when we can reverse engineer them and find the secrets of those spying on us?” one of the hackers told 404 Media and Wired in an interview. “We liberated hardware in the field, disarmed them, and proceeded with reverse engineering of the cameras and associated solar equipment.”
Below are a few of the secrets that I've found so far.
I'm crunching data and writing these newsletters in my free time. If you want to support my work, consider becoming a paid supporter.
Become a paid supporter
This camera is running an obsolete, end-of-life version of Android
Flock cameras run on a modified version of Android. The specific build that this Flock camera was running at the point in time the firmware was extracted was from June 5, 2025.
Despite being a relatively recent build, the Flock camera was running Android 8.1. This version of Android was released in 2017, and officially stopped getting support from Google in 2021 (see the
Android end-of-life
page for more info). And despite Google publishing security fixes for Android 8.1 until 2021, the Android patch level is 2018-06-05. This camera is missing Android security updates for the last eight years.
Android runs on the Linux kernel. This Flock camera was running Linux 3.18.71, released in 2017. The 3.18 series was maintained until May 2019, ending at 3.18.140 — this camera is 69 releases short of even that. This kernel is over nine years out-of-date.
Here are a few publicly-known vulnerabilities that this camera is probably vulnerable to, and that affect components that this camera ships with. I don't actually have this Flock camera to test these on and confirm that the hacks work, but what I do know is that this Flock camera's patch level predates all of these vulns, despite patches being available for many years.
CVE-2021-1905
Qualcomm Adreno GPU
– use-after-free. Any code running on the Flock camera, including in unprivileged apps, can corrupt kernel memory through the GPU driver and take full control of the device. Patched in May 2021.
CVE-2018-9568
("WrongZone")
– kernel socket type confusion. A program running on the camera can confuse the kernel's socket handling over IPv6 and escalate itself to root. Patched in December 2018. (Here's
public exploit code
for this one.)
In a statement to 404 Media and Wired, a Flock spokesperson said:
Flock takes security seriously and maintains a public Vulnerability Disclosure Policy for security researchers to report potential vulnerabilities directly to us. We received no report through that process, and based on the limited information provided, we do not have enough detail to assess the claims being made. If the individuals identified legitimate vulnerabilities, we encourage them to submit their technical findings through our vulnerability reporting process so our security team can review them and take any appropriate action.
lol.
Where I found this in the data
If you want to follow along, DDoSecrets published this dataset
here
.
The Android version and patch level are listed in multiple places, but the easiest place to find it is in the
system
partition. If you download
partitions/24_system.img
(1.5 GB) and extract it, you'll find a file,
build.prop
, which includes these lines:
ro.build.version.sdk=27
ro.build.version.release=8.1.0
ro.build.version.security_patch=2018-06-05
ro.build.date=Thu Jun  5 20:05:57 UTC 2025
The Linux version can be found in the
boot
partition. If you download
partitions/21_boot.img
(32 MB) and extract it, you'll find the kernel image in a file called
kernel
. You can find the Linux version with:
❯ tail -c +16496 kernel | zcat 2>/dev/null | grep -am1 'Linux version'
Linux version 3.18.71-perf-gaf770dc (android@e593ce924ef6) (gcc version 4.8 (GCC) ) #1 SMP PREEMPT Thu Jun 5 20:15:45 UTC 2025
Credentials into Flock's live production infrastructure
Before I go into detail here, I want to emphasize something real quick:
It's illegal to connect to Flock's servers using leaked credentials without their permission.
The Android firmware for this Flock camera includes 20 separate Flock apps, 19 of which all share a library called
com.flocksafety.android.common.lib
. If you decompile the library, there's an interesting method in the
CameraSettings
class:
public final String getHpnotiqApiKey() {
    return "HaJ3FgupAm8RrDJW3MHgT9X7Ft27eVaD";
}
This is an API key, hard-coded straight into the app. Flock runs a backend service at
hpnotiq.flocksafety.com
. When the camera needs new credentials, it makes an API request to
hpnotiq
that looks like this:
POST https://hpnotiq.flocksafety.com/api/v3/devices/credentials
x-api-key: HaJ3FgupAm8RrDJW3MHgT9X7Ft27eVaD

macAddress=F46ADD5746FB
Note that this specific Flock camera's MAC address is
F4:6A:DD:57:46:FB
.
Presumably, you can use this hard-coded API key to obtain credentials for
any
Flock camera, based on its MAC address.
The API appears to respond with an Auth0 client ID and secret.
Auth0
is an identity management company owned by
Okta
. The camera then stores those credentials in plaintext.
Btw, those credentials,
which might actually still be live and active
(I'm honestly not sure because I didn't try them), are:
{
    "clientId":"CPkOAuOKFwNhPavKO01Htxbn6yIwASro",
    "clientSecret":"ZRExGjbVjBB1wx04RmsMeWKbpMO5zQxLKNZg25D-1LUKbfQbmByajx-8lyB6LwSV"
}
These credentials can then be used to mint bearer tokens by sending them to
https://device-login.flocksafety.com/oauth/token
, and getting back a short-lived
FlockAuth0Token
which can be used to interact with Flock's backend servers, authenticated as this camera.
Where I found this in the data
The API key is in the
system
partition. Download
partitions/24_system.img
(1.5 GB), extract it, and you'll find 19 Flock apps under
app/
:
flock-sambuca
,
flock-collins
,
flock-phone-home
, etc., each containing an APK. Decompile any one of them and look for
CameraSettings
in
com.flocksafety.android.common.lib
. The shared library is bundled into all 19 apps, so the key is in every one of them.
flock-sambuca
is the app that uses it for provisioning credentials. Its
Auth0ServiceManager
class builds the credentials request, and the URLs for both
hpnotiq.flocksafety.com
and
device-login.flocksafety.com
are in that APK's string resources (
resources/res/values/strings.xml
).
The Auth0 client ID and secret are on a different partition. Download
partitions/27_persist.img
(32 MB) and extract it. The file is at
flock/auth0/auth0_cred
. This is the camera's
/persist
partition, which is not encrypted and is designed to survive a factory reset.
The MAC address and the 2,264 calls to
hpnotiq
come from the camera's logs, in
partitions/53_media.img
(18 GB). Those sit inside an encrypted container, though the key to it is stored on the same partition in a file called
expand_1fcdafef903c40cab3aff81bec914d01.key
, lol. Once it's unlocked, the logs are gzipped tarballs under
media/0/media/crashpack/
.
This specific camera was in a suburb of Milwaukee
The Flock camera's logs include camera location GPS coordinates 155 times, all within about 100 meters of each other, which I think is ordinary GPS jitter for a receiver that never moves. The coordinates that appear most often are 43.10151313, -88.05270186. If you search for that in Google Maps, you'll end up in a suburb just northwest of Milwaukee.
The coordinates 43.10151313, -88.05270186, from Google Maps
I've never been to the Milwaukee area, but it looks like this Flock camera is in a city called Wauwatosa, on N Mayfair Rd, just off of Webster Park.
Zoomed into the camera's location
Using Google Street View, I walked around N Mayfair Rd looking for a Flock camera. It looks like the GPS is slightly off, and it's actually on the west side of the street, near a parking lot for the park.
See the solar panel on that light post with the No Parking sign? That's the Flock camera.
There you are, Flock camera serial number
23091220026
with MAC address
F4:6A:DD:57:46:FB
!
The Flock camera in question, captured by Google's surveillance infrastructure
Who could have realized that this little camera, spending all its time spying on the innocent people driving by, would some day find its way into the hands of hackers from the stegan0gram collective?
Where I found this in the data
Download
partitions/53_media.img
(18 GB), extract it, mount the (barely) encrypted filesystem, and then look at the logs in
media/0/media/crashpack/
. Extract one of the log files – any of them, it doesn't matter. Inside there, there are many logs with filenames like
ciroc.2026-*.log
. Grep those for
Location
and you'll see the GPS coordinates:
❯ cat ciroc.2026-01-27.3.log | grep Location
01-28 08:22:31.304 INFO  [Binder:1584_1] QCamera2: Location: 43.10151313, -88.05270186
01-28 08:32:32.240 INFO  [Binder:1584_3] QCamera2: Location: 43.10151313, -88.05270186
--snip--
With luck, this reporting will encourage city councils everywhere to cancel their contracts with Flock and other ALPR vendors, and to stop giving the police more surveillance tools at the expense of everyone's privacy.
