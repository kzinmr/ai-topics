---
title: "A bit about email"
url: "https://maurycyz.com/misc/email/"
fetched_at: 2026-11-07T10:01:30.785864+00:00
source: "maurycyz.com"
tags: [blog, raw]
---

# A bit about email

Source: https://maurycyz.com/misc/email/

A bit about email
2026-11-06
Before you torch and pitchfork me, I'm aware most of this is simplified and doesn't go into edge cases, even though the internet is composed entirely of edge cases.
  Otherwise, I'd be writing a whole book.
First, some terminology;
A typical email will past through many different components on it's way to the recipient:
1. Sender's MUA
[Via SMTP on port 465]
2. Sending MSA 
3. Sending MTA
[Via SMTP on port 25]
4. Receiving MTA
5. Receiving LDA and message store
[Via IMAP]
7. Receiver's MUA
(These aren't all necessarily different machines or even different programs, but it is helpful to give a name for each step.)
The mail user agent (MUA) runs on the user's computer and is what they use to send or read messages.
Let's say they send something:
that message will be uploaded to to the submission agent (MSA) which checks the user's password before handing off to the mail transfer agent (MTA).
The transfer agent's job is to talk to the other mail servers and get the message to the receiving side's MTA.
Once received, it's given to the local delivery agent (LDA) to be stored until the recipient checks their email.
The name "LDA" is non-standard, but I use it to avoid having four different abbreviations differing by a single letter.
The reason for this structure
is that when the system was being designed (around 1980),
most organizations could only afford a single server.
Maintenance was a full time job and updates often required multiple days of downtime. 
A well-connected computer might have dedicated single-digits megabit/second link that worked half the time.
This forced the MTA and MUA distinction:
if the recipient's server isn't up when the email is set, the sending MTA will save the message and re-attempt delivery later.
This way, short outages don't cause bounced mail.
Since the mail client is an interactive program the user runs, a separate message store is needed to keep the email until it can be read.
Most MTAs are configured to continue retrying a message for five days, usually with exponential backoff:
mine will wait 5 minutes after the first failure, and increase the interval to one hour during prolonged outages.
The MSA and LDA have always existed in some capacity, but have gotten a lot more complicated
when people started accessing email from their own computers instead or remotely logging onto the server.
SMTP
Most communication happens over the Simple Mail Transfer Protocol, including MTA-MTA delivery.
To narrow it down a bit, I'll pretend do be an MTA sending email to blog@maurycyz.com.
The first step is to look up the receiving MTA for that domain:
#
dig
MX
maurycyz.com
[snip]
maurycyz.com.           300     IN      MX      1 smallcrow.com.
[snip]
#
dig
A
smallcrow.com
[snip]
smallcrow.com.          300     IN      A       65.109.172.162
[snip]
Email is old enough to have it's own dedicated DNS record instead of using subdomain hacks or TXT abuse.
The number is a priority (smaller is higher), which is used if multiple hosts are specified:
a big email provider will have multiple servers to ensure timely delivery.
SMTP is a relatively straightforward text based protocol.
The one catch is that most mail servers will require a CRLF as a data terminator.
This can often be sent with ctrl-m, but using a tool that automatically inserts cartridge-return bytes is easier:
# telnet
telnet>
set
crlf
Will send carriage returns as telnet <CR><LF>.
telnet>
open
smallcrow.com
25
Trying 65.109.172.162...
Connected to smallcrow.com.
Escape character is '^]'.
220 smallcrow.com ESMTP Postfix
HELO nowhere
250 smallcrow.com
MAIL FROM:<me@nowhere>
250 2.1.0 Ok
RCPT TO:<blog@maurycyz.com>
250 2.1.5 Ok
DATA
354 End data with <CR><LF>.<CR><LF>
From: <me@nowhere>
To: <blog@maurycyz.com>

Hello, world.
.
250 2.0.0 Ok: queued as C870D7CD93
QUIT
221 2.0.0 Bye
Each line sent is a command, to which the remote server responds with a three digit number followed by human readable text.
200 responses mean it worked,
300 is "carry on...",
400 is temporary errors which tell the sender to try again later,
500 permanent errors mean the email should be returned as un-deliverable.
(If this seems similar to HTTP, that's no coincidence. A lot of the web, including its header syntax was lifted from SMTP)
The first command is always HELO (or EHLO), followed the sending MTA's hostname.
This is usually not the same hostname as used in email addresses, but many provider require it to match the sender's IP address.
Mine doesn't, so if you want to try this, put something random that's not a resolvable domain.
. 
The next two, MAIL FROM and RCPT TO specify the address to deliver to, and address to forward any bounce notifications to.
Bounce messages are usually generated one step up from where the error occurred:
in most cases the receiving MTA has a problem and sends an error code to the sending MTA, but by that time MSA has already, forcing a un-delivered mail notification.
Those notification themselves use an empty MAIL FROM to avoid infinite loops.
Once the address has been specified and accepted, a DATA command is sent, followed by the actual email message.
This at a minimum, contains the "From" and "To" headers along with some text.
The message is terminated with a lone period to which the server indicates that the message is handed off.
Final hop MTA's
should forward the email to the LDA before sending back a status code.
This ensures that they never accept a message which they can't deliver which would result in a error notification.
This "backscatter" message interacts badly with spammers that forge MAIL FROM:
it turns their obviously bogus message into one that is likely to be delivered and cause annoyance.
There is no requirement for the addresses inside the email to match the ones in MAIL FROM and RCPT TO (also known as the envelope).
The most common cause of this is a mail that has been forwarded.
For example, a mailing list will set the envelope destination to match each member's email, but keep the original "From" header intact so that replies work correctly.
The envelope from address will usually be changed to point to somewhere the list administrator will check for error notifications.
Now, it's not that intermediate systems don't modify the headers:
Most stages will add a "received" header to record where they got the message.
While required for MTA to MTA communication
, SMTP is used throughout the whole system.
The mail client submits email using a different port, but over the same protocol.
Communication between internal components (i.e. MTA to LDA) often uses the closely related Local Mail Transfer Protocol:
the main difference is the assumption that the receiver doesn't have a message queue and will either deliver the mail immediately or return an error.
Submission usually uses TLS connection to port 465, with the addition of a password (in base64):
AUTH PLAIN
334
AGh1bnRlcgBodW50ZXIy
235 2.7.0 Authentication successful
The one thing that's significantly different is the MUA's fetch, which operates on a "pull" basis.
I won't go into the syntax here, but it's not terribly complicated.
... but if you actually try sending an email to, say, gmail, based on what I've said so far, it won't work.
Some of that is due to them enforcing things like the Message-Id header:
a unique identifier used to de-duplicate mail in cases where the receiving MTA accepts an email but the connection drops before the sender is informed about this.
This will cause the sender to try again later, which duplicating the message.
However, a big part of it is...
Authentication
Base SMTP trusts that every sender is be well behaved:
anyone can send email as anyone else. 
In fact, many hosts were configured to accept and relay mail from anyone as a conveyance for when someone's usual server was down.
The original solution to bad behavior was to get the culprit kicked off the internet...
but that fell apart quickly once the network grew and companies began getting involved:
the first documented case of spam email was sent in 1978 and sold 13 million dollars in computers.
While authentication doesn't prevent spam, it makes it possible to filter out unwanted senders.
Verifying sender addresses is not possible using the MX record, since there is no guarantee the same host is used for receiving and sending mail.
The simplest solution is to publish the sending address in a DNS record:
@ TXT v=spf1
ip4:
65.109.172.162
ip6:
2a01:4f9:c011:841a:b01d::1
-all
; Roughly:
;   allow from 65.109.172.162
;   allow from 2a01:4f9:c011:841a:b01d::1
;   deny otherwise
However, that's not quite enough for the email empire.
Big-tech also wants the email body to be signed with a cryptographic key published via a DKIM DNS record.
This requires adding a step to sending mails, usually as a plugin for the MTA.
I rag on big-tech a lot, but this is actually a sensible policy:
SPF can only verify the MAIL FROM, since forwarding the email will chance the source IP address. 
DKIM signatures are attached to the message and can be used to verify the original sender (the "From" address) of a message.
However
, both of these don't actually prevent spam, because spammers can just set up a few TXT records.
Big-tech requires the sender's HELO hostname to be consistent with their IP address, via both forward and reverse DNS.
This helps prevent compromised devices from spewing out junk:
a smart TV is unlikely to have a meaningful PTR record, and if it does, that hostname won't resolve back to it's address.
... unfortunately this policy also makes it impossible to directly send mail from most residential internet connections unless you own the address block.
Of course, the solution is to pay a big-tech company money to relay your emails.
If you don't like the, find a mail provider with more permissive rules:
the only reason big-tech is able to keep the racket running that five or so companies control 99% of communications.
The message
This is where SMTP stops being so simple.
The message format is a mess of historical baggage, but first,
let's look at the simplest possible email once it's been delivered:
Return-Path
: <alex@
there
>
Delivered-To
: bob@
here
Received
: from
here
by
here
with LMTP
        id bs05E10S7Go4VQMAHrglgg
        (envelope-from <alex@
there
>)
        for <bob@
here
>; Thu, 05 Nov 2026 05:21:33 +0000
DKIM-Filter
: OpenDKIM Filter v2.11.0
here
B05E67CD18
Received-SPF
: None (mailfrom) identity=mailfrom; client-ip=
313.33.33.337
;
        helo=
there
; envelope-from=alex@
there
; receiver=
here
Received
: from
there
(unknown [
313.33.333.337
])
        by
here
(Postfix) with SMTP id B05E67CD18
        for <bob@
here
>; Thu, 05 Nov 2026 05:20:42 +0000 (UTC)
From
: alex@
there
To
: bob@
here
Hello, World!
The format of the headers is superficially similar to HTTP headers,
except that no line should exceed 78 bytes. (without the CRLF line terminator)
Overlong headers are broken up and newly created lines are prefixed with whitespace to indicate that they are a continuation of the last header.
Mail software generally appends headers to the start of a message, so it's helpful to read them backwards.

"From" and "to" are fairly self explanatory.
Next, the "received" header contains a note from the receiving MTA:
it includes the source's HELO name, IP address, RCPT TO and a timestamp.
The MTA then performed SPF and DKIM checks, which came up empty:
There's no signature and the MAIL FROM hostname is not publically resolvable.
The LDA added another "received" header, although it's not very helpful.
More importantly, it tacked on the "return-path" with the original MAIL FROM address and recorded the mailbox the message was delivered to.
However, the body isn't always plain text.
Let's look at an email that includes formatting:
[...]
MIME-Version
: 1.0
Content-Type
: multipart/alternative;
 boundary=----IX71FHL6PHA0538LS1WKT2W9SF7S8X
Content-Transfer-Encoding
: 7bit
------IX71FHL6PHA0538LS1WKT2W9SF7S8X
Content-Type
: text/plain;
 charset=utf-8
Content-Transfer-Encoding
: quoted-printable

Hello, World! I can do bold text!
------IX71FHL6PHA0538LS1WKT2W9SF7S8X
Content-Type
: text/html;
 charset=utf-8
Content-Transfer-Encoding
: quoted-printable

<!DOCTYPE html><html><body><div dir
=3D
"auto">Hello, world! I can do <b>bold<
=
/b> text</div></body></html>
------IX71FHL6PHA0538LS1WKT2W9SF7S8X--
That's right, it's a web page!
However, since not all email clients can understand HTML, the message also includes a plain text version.
This is done using MIME's "multipart" encoding, in this case, multipart/alternative, which indicates all the
versions are functionally equivalent.
MIME's version number has been stuck at 1.0 since 1996.
The delimiter is a randomly chosen string, which allows multiple multiparts to be nested inside of each other without escaping.
Each section of the message has it's own headers, in this case indicating that it's sent in the quoted-printable encoding.
This allows the email message to contain any bytes without exposing the MTA to scary things like non-seven-bit ASCII:
remember, the protocol is 45 years old.
In quoted-printable, Equal signs are used as the escape character: if followed by two hex digits, it decodes to that byte.
If followed by a newline, both characters should be removed.
This is used to break long lines that could otherwise cause trouble.
In this email, the "=3D" becomes an equal sign and both lines are joined together.
If you've ever seen an email with stray equal signs or which is missing one or two characters ~ every 80 bytes, broken quoted-printable decoding is usually the culprit.
The second "content-transfer-encoding" is base64, used for binary files like attached images:
MIME-Version
: 1.0
Content-Type
: multipart/mixed; boundary="5ZTNvId/H+rlk7Fr"
Content-Disposition
: inline
--5ZTNvId/H+rlk7Fr
Content-Type
: text/plain; charset=us-ascii
Content-Disposition
: inline

Check out this file:
--5ZTNvId/H+rlk7Fr
Content-Type
: application/octet-stream
Content-Disposition
: attachment; filename="file.bin"
Content-Transfer-Encoding
: base64

J7mtSdbQItOAi345nwaNkkTXrnDIRPA0DSwhbSAOwm2C/KoHjQIotY9lnJRMBRk9InQaHOxL
bb7DGd9EN6uRpjvCbox9xblAh3CxH7sl+YAkYcKw1V100RpBwMhgaXfUJBB3oRkLffgRwEyK
v9qFBLp9zZ+SiRJoRWbA4aZLexPhHZ35vFROVKYtiAeMlD1s15v3kPZvEADam0e45BoSaqmp
1S3z3b5wBIFHJUxQULD589MKaFx2Z2A+91pl/pbZWmZkzt55D/hZ05kjUUbXUnDnTYAQE2Gk
WnN+SnrQvfEO+Tz7AdrbLD1q2DgwWW+k0cVJLKjdwRxesGhAkQCZfHVrno6R4iXjTbInIbQv
hXzQiV840iUiUhk282WADd1ffJ0sot2Waf7XHLIE1lZVFQ3iGofYbw8pZlg3sb35AnIWPZKv
fbC6Yh95RV23R4K2NHeBX1rpl4bSSiftnD2RbsBzv7cgw/6M/Lj3O40NFGAaUC+J7TpAaXdi
tvlPsNQhMo8QRf/ub7WK42cPUlz1fKq1k1pzGN96YOsE5azMfF4vLANtbtbVmLIp2WmgBk0P
9IGMWy/xIAe0cOh+bqzru2+ojJGgx9uX4VSTP9BaTOwkVX5+rQfpp1qJodtHiO8sHw6Pg+Mg
WcpqQPC7118ccuT44cVpIRkwOSoJzsW++WM=
--5ZTNvId/H+rlk7Fr--
This is why size limits are often disappointing:
the encoded email will be ~ 35% larger than the original file.
More efficient encodings (raw binary data) are supported by some MTAs, but may have to be converted to base64 somewhere down the path...
which would break DKIM signing.
Generally
:
No encoding ("7-bit") can be used if the message has short lines and fits in low-bit ASCII. However, "7-bit" is mostly seen as a null encoding for already encoded multipart containers.
Quoted printable if the message is mostly text, but has something that risks breaking ancient software.
Base64 for binary data.
About TLS
The SSL/TLS used by mail clients is effectively the same as for a browser:
the mail provider must go to a certificate authority, prove their identity, get a certificate and use it.
Algorithms and ciphers are disabled at the slightest hint they may be insecure.
However, MTAs operates on "trusted" networks...
although it's less that an attacker can't get access to internet traffic, but that if they could,
it would be possible for them to pass an ACME challenge and take out a trusted certificate.
As a result, the goal is mostly to protect against passive eavesdropping:
most sysadmins don't bother dealing with a CA and run a self-signed certificate.
(it's not like CAs have a good track record:
4
)
Another weird thing about email is that MTAs don't use a separate TLS port.
All connections start as port 25 plaintext, then the sender issues a STARTTLS command and hands over the connection to a SSL/TLS library.
It's somewhat janky, but it allows servers to attempt to use encryption and cleanly fall back if it's not supported.
Such an approach isn't great for submissions, since a fall back would result in leaking the password...
and baddies on shared networks or nosy residential ISPs can strip out the STARTTLS command.
For this case, it's best to default use the dedicated SSL submission port 465.
(This port actually has a bit of a history, with it being deprecated in favor of STARTTLS
before being re-endorsed once we realized using optional SSL for passwords was a bad idea.)
So what??
Unless you write email related software or run infrastructure, most of this information is profoundly useless.
However, there are a few things you might want to remember.
The underlying protocols allow five days for delivery
, and it can sometimes take longer.
Since users expect delivery in seconds and most emails are at least somewhat time sensitive,
some MTAs are configured to send out delay notification if a message is taking a while.
You may want to find out if yours does this before assuming the recipient is ignoring you.
Emails are digital postcards
.
A message will be stored and forwarded by multiple systems in plaintext.
Anyone on the network path may be able to read your email:
SSL/TLS is not universally supported and can trivially be stripped out by active attackers.
This is an inherent part of email: there's no way to tack-on strong encryption without breaking existing clients.
If you need a guarantee of privacy, you must encrypt the message before sending, and the recipient must decrypt it themselves. 
Be careful with built-in tools like PGP:
these generally make it way too easy to accidentally hit reply-all without encrypting, in addition to other flaws like exposing the subject line.
"Encrypted" email providers are largely snake oil.
While the message store can encrypt messages and a custom MUA could decrypt them, the MTA must have access to plaintext.
As a result, it provides minimal to no security against most attack vectors despite the "mIlItArY gRaDe EnCrYpTiOn".
The only way to fix email would be to get everyone to agree to switch to an end-to-end encrypted protocol...
but the whole point of email is universal compatability:
encrypted messaging can exist, but encrypted email is contradictory.
The best hope is to find a mail provider that can be trusted not to snoop messages.
That is to say, not an Advertising company (google) or one that's been pushing hard for LLMs (microsoft / apple):
both of these businesses create strong incentives to read your messages.
Although you'll still have to hope whoever you are communicating with isn't beign snooped on by their provider.
Worse, DKIM signatures
act as a lifelong proof that an email came from your provider's servers, even if a message is years old and has no clear chain of custody.
This makes leaked, hacked, or snooped emails ideal extortion material:
since the bad actor can trivially prove they haven't been fabricated.
This property, called non-repudiation, is generally not desirable for messaging systems.
Avoiding signing not an option if you want to interoperate with big-tech, but it is possible to regularly rotate and publish private keys.
Before they key is published, the signature can be trusted to verify it is legitimate.
However, once the key has been published, the signature can been forged by anyone and is rendered retroactively untrustworthy.
Since authentication is checked during delivery by the MTA and LDA, this doesn't affect how the email will be handled.
However, it will cast doubt on the authenticity of leaked messages since the signature could have been forged with minimal effort.
While key rotation is common practice, most mail providers don't publish their old private keys, 
so the signature is still trustworthy (modulo the service being hacked).
I would advise against emailing something you wouldn't be comfortable reading out in public.
Related
:
