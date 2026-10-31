---
title: "Security notice — malicious version of Anthropic.claude-code (2.1.312 and 2.1.313) identified in the Cursor VS Code Extension Marketplace · Cursor"
source: "Cursor Blog"
url: "https://cursor.com/blog/claude-code-extension-security-notice"
scraped: "2026-10-31T06:00:09.843936+00:00"
lastmod: "2026-10-31T00:47:22.230Z"
type: "sitemap"
---

# Security notice — malicious version of Anthropic.claude-code (2.1.312 and 2.1.313) identified in the Cursor VS Code Extension Marketplace · Cursor

**Source**: [https://cursor.com/blog/claude-code-extension-security-notice](https://cursor.com/blog/claude-code-extension-security-notice)

Blog
/
company
Oct 29, 2026
·
company
Security notice — malicious version of Anthropic.claude-code (2.1.312 and 2.1.313) identified in the Cursor VS Code Extension Marketplace
5 min read
Table of Contents
↑
What happened
What we did
What you should do
Check whether you are impacted
Remediate affected machines
Indicators of compromise
Package version 2.1.312
Package version 2.1.313
Payload
Network
SSH
Files and persistence
Process / command-line
Today we identified a security incident involving a specific extension in the Cursor VS Code Extension Marketplace:
Anthropic.claude-code version 2.1.312 and 2.1.313 for Windows and MacOS
. These malicious versions of the extension were not developed by Anthropic. This does not impact other extensions downloaded from the cursor.com/marketplace, Grok Bot, Grok or our other SpaceXSI products.
#
What happened
Between about 2:27am PT and 1:35pm PT today, a maliciously modified version of Anthropic’s Claude Code extension was made available in the Cursor VS Code Extension Marketplace. The extension runs malicious code that attempts to install a persistent SSH backdoor. Specifically, it:
Collects and reports host and user information: hostname, username, OS, architecture, home directory path, environment variable names, working directories, configured Git email, and public IP.
Attempts to add an attacker-controlled SSH key to
authorized_keys
, enable the local SSH service, and open a reverse SSH tunnel. Outside of highly unusual circumstances where Cursor was started with administrator privileges, due to errors in the malicious code, this step would fail.
Attempts to make the reverse SSH tunnel persistent via a LaunchAgent (macOS), or a scheduled task that attempts to run as SYSTEM with a Startup-script fallback (Windows). Background scripts retry the tunnel roughly every 60 seconds.
Note: The attacker server no longer functions.
We worked with the cloud provider that was hosting it to take it offline, so the reverse shell and host detail POST are not functional.
These findings concern the identified package. We have no evidence that other versions of the extension or the official distribution are affected.
Additionally, turning on the local SSH service requires admin rights, which the malicious extension does not have on most macOS and Windows hosts. On those hosts the step fails and the attacker could not have logged in through the tunnel. The extension added the attacker’s SSH key, installed persistence, and sent host details to the attacker. Follow the remediation steps below regardless.
#
What we did
Removed the malicious version from the Cursor VS Code Extension Marketplace immediately upon detection and blocked further distribution. We followed with a full shut down of the marketplace out of an abundance of caution.
We audited access and confirmed no other extensions were tampered with.
We rotated our keys, rebuilt the marketplace, and brought it back online.
We worked with the hosting provider to take the malicious server offline, disrupting the attack by blocking the connection to that server.
#
What you should do
If you installed or updated to Anthropic.claude-code 2.1.312 or 2.1.313 from the Cursor VS Code Extension Marketplace on macOS or Windows between 2:27am PT and 1:35pm PT on October 29, 2026:
Run the attached script to validate if you are impacted (see below).
Search across endpoint, network, and extension-installation telemetry for the indicators below.
Isolate hosts showing evidence of payload execution or backdoor installation.
Remove the unauthorized SSH key, persistence mechanisms, and running tunnel processes, and assess whether the host should be rebuilt. Uninstalling the extension may not be sufficient — the payload drops standalone persistence scripts that keep running.
Rotate credentials and sessions accessible from affected hosts, from a trusted system. The limited env-var collection does not rule out later credential access over the backdoor.
#
Check whether you are impacted
The malicious extension appends the attacker's public key, labeled
svc-telemetry
, to your SSH authorized keys. To check for it:
On macOS, run:
grep
-qs
svc-telemetry
~/.ssh/authorized_keys
&&
echo
"svc-telemetry key found"
||
echo
"No key found; machine not impacted"
On Windows, run in PowerShell:
$files
=
"
$HOME
\.ssh\authorized_keys"
,
"C:\ProgramData\ssh\administrators_authorized_keys"
|
Where-Object
{
Test-Path
$_
}
if
($files
-and
(
Select-String
svc
-
telemetry $files)) {
"svc-telemetry key found"
}
else
{
"No key found; machine not impacted"
}
If the key is found, your machine is impacted. Follow steps 3 to 5 above, and run the remediation script for your platform below.
#
Remediate affected machines
These scripts remove the malicious extension, the persistence mechanisms, the running tunnel processes, and the attacker's SSH key. They exit with a non-zero status if anything remains.
On macOS, download
remediate-macos.sh
and run it as the affected user, not as root, from the folder you saved it to:
bash
remediate-macos.sh
On Windows, download
remediate-windows.ps1
and run it from PowerShell opened with
Run as Administrator
, in the folder you saved it to:
powershell
-
ExecutionPolicy Bypass
-
File .\remediate
-
windows.ps1
#
Indicators of compromise
#
Package version 2.1.312
Modified VSIX SHA-256 (darwin-arm64): fcbb327e38e61c4fec795e0d0591f52cd1014b813d20a5912104953c3a17c364 (MD5 e0d64d53e802a0217ba6f0e656ed2f20)
Modified VSIX SHA-256 (win32-x64): 3de1722901165769893bef57c72594e9a54459faa23f3091b136b79966edd081 (MD5 bd3b71ddf3d0cc3af76249afd2c0eda1)
#
Package version 2.1.313
Modified VSIX SHA-256 (darwin-arm64): 80402fdcad8799285fd93044976973ca000da7995fb93363f819bb8e4f84ee6c (MD5 34e491161e056c9b899a79b602ac73b9)
Modified VSIX SHA-256 (win32-x64): 6786ec90cbd45949695bd7805c9fbb26cfc91bc5fc897de0183d9bcb9cb21731 (MD5 7838a3be2ca0ff08c1bdb160ef516d39)
#
Payload
Modified code: extension.js in package versions 2.1.312 and 2.1.313 for both Darwin and Windows in the extension folder contains 134[.]209[.]82[.]225 and svc-telemetry
SHA-256: ecb58cb29078d9646ad1dcdbe51526f2d9cfea06be5fb2ab183e8ecc3ab6bf15
MD5: f49bcd657ef1e626e85ce858958c1769
#
Network
Attacker endpoint: 134[.]209[.]82[.]225
Reverse SSH: tunnel@134[.]209[.]82[.]225, TCP 22
External beacon: hxxp://134[.]209[.]82[.]225:8099/beacon (HTTP POST)
Local beacon attempt: 127[.]0[.]0[.]1:8099/beacon (HTTP POST, loopback)
Public IP lookups to ifconfig[.]me / api[.]ipify[.]org — legitimate services; access alone is not an indicator
#
SSH
Unauthorized public key:
ssh-ed25519 AAAAC3NzaC1lZDI1NTE5AAAAIDdvylCEJ/k2TpezcTfedrkHyFSK9IZ3vmP6vhY4Ss0P svc-telemetry
Unauthorized key fingerprint:
SHA256:0Z6R+DF64Do2nwQic8a7kkfDLNNk4IiK+2U2Rci4htk
Reverse-tunnel key fingerprint:
SHA256:KOAU57+ZG6u3MG4WwzPzPX2O5YEe9qdOC1Bl+6MVyDQ
Key comment:
svc-telemetry
#
Files and persistence
Linux / macOS: unauthorized key in
~/.ssh/authorized_keys
;
~/.config/.smt
,
~/.config/.smtk
Linux:
/tmp/.stk_<10 hex>
; cron
@reboot /bin/sh "<HOME>/.config/.smt"
macOS:
$TMPDIR/.stk_<10 hex>
;
~/Library/LaunchAgents/com.apple.sysmond.plist
(label
com.apple.sysmond
)
Windows:
%USERPROFILE%\.ssh\authorized_keys
,
%USERPROFILE%\.config\smt.cmd
,
%USERPROFILE%\.config\smtk
,
%TEMP%\.stk_<10 hex>
; scheduled task
SysMon
(attempts to run as SYSTEM); fallback
%APPDATA%\Microsoft\Windows\Start Menu\Programs\Startup\sysmon.cmd
#
Process / command-line
ssh -N -R '*:0:localhost:22'
,
autossh -M 0
SSH options:
StrictHostKeyChecking=no
,
UserKnownHostsFile=/dev/null
,
ServerAliveInterval=30
,
ServerAliveCountMax=3
,
ExitOnForwardFailure=yes
,
IdentitiesOnly=yes
schtasks /create /tn SysMon
systemsetup -setremotelogin on
Add-WindowsCapability -Online -Name OpenSSH.Server~~~~0.0.1.0
If you have further questions, reach out to
security@cursor.com
.
Update:
Oct 30, 2026, 11:30 am PT: We updated the IOCs and clarified affected versions.
Filed under:
company
Author
:
Cursor Team
