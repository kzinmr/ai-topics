---
title: "Virgin Media Hub 5 API"
url: "https://shkspr.mobi/blog/2026/11/virgin-media-hub-5-api/"
fetched_at: 2026-11-25T10:00:52.702273+00:00
source: "shkspr.mobi"
tags: [blog, raw]
---

# Virgin Media Hub 5 API

Source: https://shkspr.mobi/blog/2026/11/virgin-media-hub-5-api/

I've seen some of these APIs documented around the web, but never in one place. This is a list of generally useful information you can get out of the VM SuperHub 5 (a rebadged Sagemcom F3896LG) - I haven't tried them on the 5x.
These were all tested using modem mode. They should still be the same for router mode - although you'll need to use
192.168.0.1
rather than the listed IP addresses here. You will need to send a User-Agent string with any request. You may also need to ignore the self-signed certificate.
Some of the outputs are fairly large, so I've truncated them for ease of viewing. I've also lightly redacted any sensitive data like MAC addresses.
Unauthenticated Requests
Modem Status
Service Flows
Eventlog
Downstream Primary Channel
Downstream Channels
Upstream Channels
Provisioning
Software Update
Languages
Current Language
Text Strings
Screens
Localization
Modem Mode
First Install
Phone Line Details
Login Details
Authenticated Requests
Get Bearer Token
Password
System Info
State
MBU
LED Light
Set LED
Download Backup
Logout
Reboot
Anything Else?
These APIs can be made by any device on your local network. No password required!
This gives basic information about your Hub 5.
https://192.168.100.1/rest/v1/cablemodem/state_
Sample output:
Copied JSON to 📋
⧉
JSON
{
"cablemodem"
:
{
"bootFilename"
:
"cmreg-vmdg660-bbt076-b.cm"
,
"docsisVersion"
:
"3.1"
,
"macAddress"
:
"12:34:56:78:90:AB"
,
"serialNumber"
:
"ABC123456"
,
"upTime"
: 34897,
"accessAllowed"
: true,
"status"
:
"operational"
,
"maxCPEs"
: 1,
"baselinePrivacyEnabled"
: true
}
}
This appears to show the nominal speed of the connection.
https://192.168.100.1/rest/v1/cablemodem/serviceflows
Copied JSON to 📋
⧉
JSON
{
"serviceFlows"
:
[
{
"serviceFlow"
:
{
"serviceFlowId"
: 105068,
"direction"
:
"downstream"
,
"maxTrafficRate"
: 1230000450,
"maxTrafficBurst"
: 42600,
"minReservedRate"
: 0,
"maxConcatenatedBurst"
: 0,
"scheduleType"
:
"undefined"
}
}
,
{
"serviceFlow"
:
{
"serviceFlowId"
: 105067,
"direction"
:
"upstream"
,
"maxTrafficRate"
: 110000274,
"maxTrafficBurst"
: 42600,
"minReservedRate"
: 0,
"maxConcatenatedBurst"
: 42600,
"scheduleType"
:
"best_effort"
}
}
]
}
As the name suggests, a long list of everything that your cable modem thinks is useful to report.
https://192.168.100.1/rest/v1/cablemodem/eventlog
Copied JSON to 📋
⧉
JSON
{
"eventlog"
:
[
{
"priority"
:
"warning"
,
"time"
:
"2026-03-29T13:50:24.000Z"
,
"message"
:
"Dynamic Range Window violation"
}
,
{
"priority"
:
"notice"
,
"time"
:
"2026-03-29T13:44:21.000Z"
,
"message"
:
"REGISTRATION COMPLETE - Waiting for Operational status"
}
,
{
"priority"
:
"notice"
,
"time"
:
"2026-03-29T13:44:03.000Z"
,
"message"
:
"Honoring MDD; IP provisioning mode = IPv4"
}
,
{
"priority"
:
"critical"
,
"time"
:
"2026-03-27T11:36:20.000Z"
,
"message"
:
"Cable Modem Reboot because of - Software_Upgrade"
}
,
https://192.168.100.1/rest/v1/cablemodem/downstream/primary_
Copied JSON to 📋
⧉
JSON
{
"channel"
:
{
"channelType"
:
"sc_qam"
,
"channelId"
: 22,
"frequency"
: 306000000,
"power"
: 14.5,
"modulation"
:
"qam_256"
,
"snr"
: 41,
"rxMer"
: 41,
"correctedErrors"
: 26,
"uncorrectedErrors"
: 0,
"lockStatus"
: true
}
}
https://192.168.100.1/rest/v1/cablemodem/downstream
Copied JSON to 📋
⧉
JSON
{
"downstream"
:
{
"channels"
:
[
{
"channelType"
:
"sc_qam"
,
"channelId"
: 22,
"frequency"
: 306000000,
"power"
: 14.5,
"modulation"
:
"qam_256"
,
"snr"
: 42,
"rxMer"
: 42,
"correctedErrors"
: 26,
"uncorrectedErrors"
: 0,
"lockStatus"
: true
}
,
{
"channelType"
:
"ofdm"
,
"channelId"
: 33,
"channelWidth"
: 92000000,
"fftType"
:
"4K"
,
"numberOfActiveSubCarriers"
: 1800,
"modulation"
:
"qam_4096"
,
"firstActiveSubcarrier"
: 1128,
"lockStatus"
: true,
"rxMer"
: 0,
"power"
: 136,
"correctedErrors"
: 803910229,
"uncorrectedErrors"
: 59
}
]
}
}
https://192.168.100.1/rest/v1/cablemodem/upstream
Copied JSON to 📋
⧉
JSON
{
"upstream"
:
{
"channels"
:
[
{
"channelId"
: 1,
"frequency"
: 49600000,
"lockStatus"
: true,
"power"
: 40,
"symbolRate"
: 5120,
"modulation"
:
"qam_64"
,
"t1Timeout"
: 0,
"t2Timeout"
: 0,
"t3Timeout"
: 0,
"t4Timeout"
: 0,
"channelType"
:
"atdma"
}
,
{
"channelId"
: 6,
"channelWidth"
: 10400000,
"lockStatus"
: true,
"power"
: 347,
"fftType"
:
"2K"
,
"modulation"
:
"qam_256"
,
"channelType"
:
"ofdma"
,
"numberOfActiveSubCarriers"
: 208,
"firstActiveSubcarrier"
: 74,
"t3Timeout"
: 0,
"t4Timeout"
: 0
}
]
}
}
https://192.168.100.1/rest/v1/system/gateway/provisioning
Copied JSON to 📋
⧉
JSON
{
"provisioning"
:
{
"mode"
:
"disable"
,
"macAddress"
:
"12:34:56:78:90:AB"
,
"dsLite"
:
{
"enable"
: false
}
}
}
Appears to just be what caused the last update.
https://192.168.100.1/rest/v1/system/softwareupdate
Copied JSON to 📋
⧉
JSON
{
"softwareUpdate"
:
{
"status"
:
"complete_from_provisioning"
}
}
Appears to be languages supported by the hub.
https://192.168.100.1/rest/v1/system/languages
Copied JSON to 📋
⧉
JSON
{
"languages"
:
{
"languages"
:
[
"en"
,
"nl"
,
"fr"
,
"de"
,
"it"
,
"pl"
,
"sk"
]
}
}
The current user is "3" - no idea why - here's what language their UI is set to.
https://192.168.100.1/rest/v1/user/3/language
Copied JSON to 📋
⧉
JSON
{
"language"
:
{
"language"
:
"en"
}
}
Using the language string above, you can get the UI text from the modem. Note, it also accepts "UK" as well.
https://192.168.100.1/resources/languages/uk.json
Copied JSON to 📋
⧉
JSON
{
"c_fi00"
:
"Hello!"
,
"c_fi02"
:
"Please choose your language to continue."
,
"c_fi03"
:
"Please sign in with your <span data-placeholder=\"
ProductName\
"></span> settings password."
,
"c_fi04"
:
"Perfect!"
,
"c_fi05"
:
"We recommend you change the default settings password. You can easily change it now, or any time in the future."
,
"c_fi06"
:
"Current password:"
,
"c_fi07"
:
"Enter a new password:"
,
"c_fi11"
:
"Your <span data-placeholder=\"
ProductName\
"></span> is ready to go!"
,
"c_fi12"
:
"Go to Dashboard"
,
"c_fi13"
:
"Thanks for taking the tour!"
,
"c_fi14"
:
"You can now manage your <span data-placeholder=\"
ProductName\
"></span> settings. "
,
"g_dhcp09"
:
"This section allows you to configure how the <span data-placeholder=\"
ProductName\
"></span> assigns IPv6 addresses. "
,
Note - there's lots of IPv6 related strings, but still no sign of Virgin supporting a modern network stack.
I
think
this is which UI options are available while in modem mode.
https://192.168.100.1/rest/v1/system/ui/screens
Copied JSON to 📋
⧉
JSON
{
"screens"
:
{
"dns"
:
{
"display"
: false
}
,
"ddns"
:
{
"display"
: false
}
,
"firstInstall"
:
{
"display"
: true
}
,
"dhcpLanSubnetFields"
:
{
"editable"
: false
}
,
"modemMode"
:
{
"display"
: true
}
,
"rip"
:
{
"display"
: false
}
,
"wirelessAndSecurityRIP"
:
{
"disable"
: false
}
,
"vmb"
:
{
"display"
: false
}
,
"wirelessAndSecurityVMB"
:
{
"disable"
: false
}
,
"staticIp"
:
{
"display"
: false
}
,
"wirelessAndSecurity"
:
{
"disable"
: false
}
,
"wifiSmartControl"
:
{
"display"
: true,
"editable"
: true
}
,
"troubleshootWizard"
:
{
"display"
: false
}
}
}
What the modem should be called.
https://192.168.100.1/rest/v1/system/localization
Copied JSON to 📋
⧉
JSON
{
"localization"
:
{
"skin"
:
"virgin_media"
,
"productName"
:
"Hub 5"
,
"modelName"
:
"F3896LG"
}
}
Whether the device is in modem or router mode.
https://192.168.100.1/rest/v1/system/modemmode
Copied JSON to 📋
⧉
JSON
{
"modemmode"
:
{
"enable"
: true
}
}
Has the device gone through its initial installation procedure.
https://192.168.100.1/rest/v1/system/firstinstall
Copied JSON to 📋
⧉
JSON
{
"firstInstall"
:
{
"complete"
: true
}
}
There are two phone sockets on the back for VoIP purposes.
https://192.168.100.1/rest/v1/mta/lines
Copied JSON to 📋
⧉
JSON
{
"lines"
:
[
{
"id"
: 1,
"line"
:
{
"enable"
: false,
"operational"
: false
}
}
,
{
"id"
: 2,
"line"
:
{
"enable"
: false,
"operational"
: false
}
}
]
}
This will show how many time the wrong password was entered and how long before you can attempt to log in again.
https://192.168.100.1/rest/v1/user/login
Copied JSON to 📋
⧉
JSON
{
"loginDetails"
:
{
"numberOfContiguousFailures"
:
"0"
,
"lockoutTime"
:
"0"
}
}
These require you to be logged in to your Hub 5.
In order to send authenticated requests, you need to POST your password to the hub.
Copied Bash to 📋
⧉
Bash
curl -k 'https://192.168.100.1/rest/v1/user/login' \
  -X POST \
  -H 'User-Agent: Whatever' \
  -H 'Content-Type: application/json' \
  --data-raw '{"password":"ABC123"}'
That will get you back:
Copied JSON to 📋
⧉
JSON
{
"created"
:
{
"token"
:
"qwertyuiop1234567890"
,
"userLevel"
:
"regular"
,
"userId"
: 3
}
}
The token will need to be sent with all authenticated requests.
Get the current password.
Copied Bash to 📋
⧉
Bash
curl -Lk 'https://192.168.100.1/rest/v1/system/ui/defaults'\
   -H 'User-Agent: Anything'
   -H 'Authorization: Bearer qwertyuiop1234567890'
Copied JSON to 📋
⧉
JSON
{
"defaults"
:
{
"password"
:
"ABC123"
}
}
More information about the hardware and software.
https://192.168.100.1/rest/v1/system/info
Copied JSON to 📋
⧉
JSON
{
"info"
:
{
"modelName"
:
"F3896LG"
,
"softwareVersion"
:
"LG-RDK_11.6.2-2410.1"
,
"hardwareVersion"
:
"1.2"
}
}
Slightly different info to the
state_
above. This adds the
serviceStatus
field.
https://192.168.100.1/rest/v1/cablemodem/state
Copied JSON to 📋
⧉
JSON
{
"cablemodem"
:
{
"bootFilename"
:
"cmreg-vmdg660-bbt076-b.cm"
,
"docsisVersion"
:
"3.1"
,
"macAddress"
:
"12:34:56:78:90:AB"
,
"serialNumber"
:
"ABC123456"
,
"upTime"
: 37197,
"accessAllowed"
: true,
"status"
:
"operational"
,
"serviceStatus"
:
"full_service_both"
,
"maxCPEs"
: 1,
"baselinePrivacyEnabled"
: true
}
}
Another vestigial VoIP thing.
https://192.168.100.1/rest/v1/network/mbu
Copied JSON to 📋
⧉
JSON
{
"enable"
: false,
"status"
:
"Not Used"
}
See what the LED is set to.
https://192.168.100.1/rest/v1/network/ledlight
Copied JSON to 📋
⧉
JSON
{
"value"
:
{
"brightness"
:
"50"
,
"automode"
:
"true"
}
}
This uses a PUT to set the brightness and whether to use automode.
Copied Bash to 📋
⧉
Bash
curl -Lk 'https://192.168.100.1/rest/v1/network/ledlight' \
  -X PUT \
  -H 'User-Agent: Anything' \
  -H 'Content-Type: application/json' \
  -H 'Authorization: Bearer qwertyuiop1234567890' \
  --data-raw '{"brightness":50,"automode":true}'
This generates a .bin file with all your settings.
Copied Bash to 📋
⧉
Bash
curl -Lk 'https://192.168.100.1/rest/v1/system/restore' \
  -X DELETE \
  -H 'User-Agent: Anything' \
  -H 'Authorization: Bearer qwertyuiop1234567890'
Send a DELETE request.
Copied Bash to 📋
⧉
Bash
curl -Lk 'http://192.168.100.1/rest/v1/user/3/token/qwertyuiop1234567890' \
  -X DELETE \
  -H 'User-Agent: Anything' \
  -H 'Authorization: Bearer qwertyuiop1234567890'
Send a POST request.
Copied Bash to 📋
⧉
Bash
curl -Lk 'https://192.168.100.1/rest/v1/system/reboot' \
  -X POST \
  -H 'User-Agent: Anything' \
  -H 'Authorization: Bearer qwertyuiop1234567890' \
  --data-raw '{"reboot":{"enable":true}}'
You'll get back a perfunctory:
Copied JSON to 📋
⧉
JSON
{
"accepted"
: true
}
That's about all I could find in modem mode - there will probably be more APIs if you're using it as a router. Drop a note in the comment if you discover anything else interesting.
