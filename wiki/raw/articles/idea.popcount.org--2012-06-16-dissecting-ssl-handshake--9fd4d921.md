---
title: "Dissecting SSL handshake"
url: "https://idea.popcount.org/2012-06-16-dissecting-ssl-handshake"
fetched_at: 2026-05-05T07:01:14.728030+00:00
source: "Marek Vavruša (idea.popcount)"
tags: [blog, raw]
---

# Dissecting SSL handshake

Source: https://idea.popcount.org/2012-06-16-dissecting-ssl-handshake

Dissecting SSL handshake
16 June 2012
Not everyone knows that the SSL handshake is not encrypted. When you
think about it - there isn't other way, before the keys are exchanged
the communication must be unencrypted. But I doubt many people think
about it.
Not only the SSL handshake is plain-text, but also it contains rather
interesting data. I decided to find out how much information can be
retrieved from it.
TLS
Here's how the
TLS handshake works
:
Client                                 Server
|
|
|
-----------
ClientHello
--------->
|
|
|
|
<----------
ServerHello
----------
|
|
<----------
Certificate
----------
|
|
...
|
|
<--------
ServerHelloDone
--------
|
|
...
|
Let's focus on the first message -
ClientHello
. It is actually
pretty interesting. RFC
defines the structure as
:
struct
{
ProtocolVersion
client_version
;
Random
random
;
SessionID
session_id
;
CipherSuite
cipher_suites
<
2..2
^
16
-
1
>
;
CompressionMethod
compression_methods
<
1..2
^
8
-
1
>
;
Extension
extensions
<
0..2
^
16
-
1
>
;
}
ClientHello
;
Translated to English:
client_version
The SSL/TLS protocol version the client (like the browser) wishes to
  use during the session. Additionally there is a second version
  number field on the framing layer, called
Record layer
. And like
  all SSL data, ClientHello message is wrapped in the Record
  frame. The
spec suggests
the
  Record layer version field may be use to indicate the lowest
  supported SSL/TLS version, but this is rarely used in practice. Only
older versions of Opera
are using different values in Record and ClientHello layers.
random
This value is formed of 4 bytes representing time since epoch on client
host and 28 random bytes. Exposing timer sources may allow
clock skew
measurements
and those in theory may be used to identify hosts.
Your browser sends current time on the SSL layer.
Similarly, ServerHello sent by the server frame contains
timestamp from the server.
session_id
Instead of going through full SSL handshake, the client may decide
  to reuse previously established session. The session cache is usually
shared between normal and privacy modes
of the browser.
Even in privacy mode, your browser may still be identifiable due
to SSL session reuse.
cipher_suites
The client shares the list of supported SSL ciphers with the server.
  The server will later pick up the best cipher it knows. Some of the
  ciphers are proven to be insecure and should be deprecated, some
  others are
fairly recent
.
  There isn't a global coherent list of good ciphers, and as a result
  every client can support different set of ciphers. Additionally the
ordering of the ciphers is significant
and therefore even if clients agreed on ciphers the ordering might
  be completely different.
By looking at the supported ciphers list it is often possible to
tell what exact application had started the connection.
compression_methods
Some clients (for example Chrome) support
Deflate compression
.
  on SSL layer. This usually makes sense - compressing HTTP headers
  does save bandwidth.
extensions
TLS introduces
a number of extensions
.
Most notably the
server_name
/
Server Name Indication
(SNI)
extension is used to specify a remote host name. This allows the
server to choose appropriate certificate based on the requested
host name.  With this extension one can host many SSL-enabled
vhosts on a single IP address. Famously
SNI doesn't work on any IE on Windows XP
.
When using SSL, the remote domain name is transferred over the
wire in plain text. Anyone able to sniff the traffic can know
exactly what domains you're looking at, even when you're using
HTTPS.
Similarly to the cipher list extensions and their order are
application specific. For example:
FireFox 11 bundled with TOR
is distinguishable from standalone installation - it doesn't send
SessionTicket TLS
extension. Another example - Windows XP
doesn't send
Renegotiation Info
extension without
patch MS10-049
applied.
That's it, now you know what's hiding in the SSL ClientHello message. For
completeness, a few words on historical protocols.
SSL 3.0
SSLv3
is identical to
TLS as described, with one exception - in theory SSLv3 ClientHello packet doesn't
have
an extensions field
.
In theory SSLv3 doesn't do
SNI
.
In practice this is more complicated. TLS 1.0 also
doesn't specify extensions field
,
but most clients do send them anyway.
SSL 2.0
SSL 2.0
was
originally developed by Netscape
. It's
old, barely documented and insecure. However few applications still
support it for compatibility with old servers. Some versions of
wget
and google crawler use the SSLv2 handshake. A
CLIENT-HELLO
message is
defined as:
char
MSG
-
CLIENT
-
HELLO
char
CLIENT
-
VERSION
-
MSB
char
CLIENT
-
VERSION
-
LSB
char
CIPHER
-
SPECS
-
LENGTH
-
MSB
char
CIPHER
-
SPECS
-
LENGTH
-
LSB
char
SESSION
-
ID
-
LENGTH
-
MSB
char
SESSION
-
ID
-
LENGTH
-
LSB
char
CHALLENGE
-
LENGTH
-
MSB
char
CHALLENGE
-
LENGTH
-
LSB
char
CIPHER
-
SPECS
-
DATA
[(
MSB
<<
8
)
|
LSB
]
char
SESSION
-
ID
-
DATA
[(
MSB
<<
8
)
|
LSB
]
char
CHALLENGE
-
DATA
[(
MSB
<<
8
)
|
LSB
]
The fields are familiar -
client_version
,
cipher_suites
,
session_id
and
challenge
. It's worth noting that SSLv2 doesn't
have extensions - there is no way to specify
SNI
.
On a final note,
challenge-data
length must be between 16 and 32
bytes long. In real world I've only seen 16 and 32.
Summary
Things to remember:
Anyone snooping the HTTPS traffic is able to see the remote domain
   name in plain text due to SNI.
ClientHello
message contains a lot of stuff and it is often
   possible to identify a client application just by looking at it.
During SSL handshake both the client and the server send their
   local time in plain-text.
Never enable SSLv2.
Continue reading about
SSL fingerprinting →
Comment on
YCombinator →
