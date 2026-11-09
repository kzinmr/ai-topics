---
title: "Horible public key tricks:"
url: "https://maurycyz.com/projects/badcert/"
fetched_at: 2026-11-09T10:11:03.000892+00:00
source: "maurycyz.com"
tags: [blog, raw]
---

# Horible public key tricks:

Source: https://maurycyz.com/projects/badcert/

Horible public key tricks:
2026-11-08
So, I've always been somewhat annoyed at SSL/TLS.
It requires everyone to go through a complex "ACME" dance just to put up a public website.
Worse, certificates expire every few months, so it's not a one and done thing:
even with automation, maintaining a certificate requires care to ensure the ACME client always has access to DNS records or the web server.
... and the whole system doesn't even work because certificates are issued over plaintext connections,
and trusted certificate aurthorities use very secure keys like
"4"
There is prior art
of protest SSL
implementations
,
but I do actually want to encrypt web traffic.
Passive eavesdropping is a real risk... but preventing it doesn't require the whole certificate thing:
therefore, the best choice is a protest certificate.
The only part of the certificate I directly control is the public key.
Therefore, the simplest way to obtain a bad certificate is use a vanity private key such as 313333333337 (one of the most eleet primes).
However, while the resulting public key would be week, no one would know unless they actually try to break it.
A good protest should be obvious:
#
openssl
s_client -connect
maurycyz.com
:
443
< /dev/null 2>
/dev/null
\
    |
sed
-n
/BEGIN/,/END/p
|
grep
-zE
'////.?*////'
--color=
yes
-----BEGIN CERTIFICATE-----
MIIFADCCA+igAwIBAgISBjst/cQvgUTu+O7siJYo8bAFMA0GCSqGSIb3DQEBCwUA
MDMxCzAJBgNVBAYTAlVTMRYwFAYDVQQKEw1MZXQncyBFbmNyeXB0MQwwCgYDVQQD
EwNZUjIwHhcNMjYxMTA4MjE0NzM5WhcNMjcwMjA2MjE0NzM4WjAXMRUwEwYDVQQD
EwxtYXVyeWN5ei5jb20wggEiMA0GCSqGSIb3DQEBAQUAA4IBDwAwggEKAoIBAQCz
lkaPgD2IZPPtC6fB
////You+dont+actually+have+to+pick+random+privat
e+keys//No+one+checks+these+things//A+certificate+aurthority+got
+away+with+the+number+4+for+a+year////
8HzhFiAzSv/zKHf7l4u6d6d3w6
nOg7N/C2ra5QvNpFnZVzrS5IcZmvRdi0dcptavcB8s4ThHNZLhY414Mvdo5t0kr0
n8WFrydnc6NEMKDPiZxehnF5D3n7z1piI5YCsNcS0NVFb45+8QvBZrv0O2BSIKNE
7M9hcE00KsaSzZ3eDBsRAgMBAAGjggIoMIICJDAOBgNVHQ8BAf8EBAMCBaAwEwYD
VR0lBAwwCgYIKwYBBQUHAwEwDAYDVR0TAQH/BAIwADAdBgNVHQ4EFgQUZoonXxel
KC563vN2kbvwXTLBQgMwHwYDVR0jBBgwFoAUQBUtJnntMiCe35pyHdYyH4EMgQww
MwYIKwYBBQUHAQEEJzAlMCMGCCsGAQUFBzAChhdodHRwOi8veXIyLmkubGVuY3Iu
b3JnLzAnBgNVHREEIDAegg4qLm1hdXJ5Y3l6LmNvbYIMbWF1cnljeXouY29tMBMG
A1UdIAQMMAowCAYGZ4EMAQIBMC0GA1UdHwQmMCQwIqAgoB6GHGh0dHA6Ly95cjIu
Yy5sZW5jci5vcmcvNi5jcmwwggELBgorBgEEAdZ5AgQCBIH8BIH5APcAdgAAGl0a
HC2TdbZIVXj4L3Ghrm7vOX0pfIrjFXvK3uGgHgAAAaG9Vy0ZAAAEAwBHMEUCIEof
iI14E0jzfOz9woGKiiYR4pUAm/Dv9FmFWEr5ma8uAiEAyl2EMpURJ65Oe+FIFE6v
Uj4QomzFJ98qVqhQozQxcC4AfQAai51rjdeR0c0FSe22A1XWBrZPrTDbcf54jw/H
yPvEsQAAAaG9Vy2AAAgAAAUAFVVRHQQDAEYwRAIgTBocYGR/XcTqNx58xJh/pAme
q+w6fDl+NktKUuPBqZcCIFJU6/GE71s9OkORDBC4+XHiQWWxrHk8uuD6nTQzCtHS
MA0GCSqGSIb3DQEBCwUAA4IBAQAUIK5MyB3bhSFc6NOkC1UYYi2BQZN4zDfZMTD1
gGtnK7FCCNKvsanv9FIeGgr7e3A50TJhqIWH42uz9mQt8rnofwKVu7fJ77l/HZIf
oAqNol06AbtwM2I4vOEAZyfD3zAfL/3G70rGw4omDFpzX852Yi3Ou40wpHbdboYY
Bn58bZDvBVaUrKVdTdN+S5Ea2usWKgUjqfouz/VjnlEgLfcxqPwF2IPfPCOPKJH2
uIo3tnjx267OWY3O8nyxuOAxrBuP5fc8g2bEcKI5RewRWh7CCVZB23Ov5dyFQVcb
ICN41m494GUBgwqYpAjLgdIubvyoJzBpACGuIl2QlJza1p/y
-----END CERTIFICATE-----
First, let's look at mathematical framework
of RSA.
To generate a key, pick two large prime numbers (p and q) and multiply them to yeild the modulus (n).
Pick a small number, e as public exponent.
The RSA public key is composed of the modulus (n) and the public exponent:
# Encryption requires knowing e (public)
cyphertext = plaintext^e mod n
The private key contains the modulus and the private exponent (d) which is chosen to be the multiplicate inverse of e modulo n.
Exactly how d is found is not relevent, but the process requires knowing p and q.
# Decryption requires knowing d (pivate)
= cyphertext^d mod n

= plaintext^e^d mod n
= plaintext^(e*d) mod n
= plaintext^1 mod n
= plaintext
Ok, back to vanity keys.
The standard value for e is 65537 (0x10001),
because the small number of set bits makes encryption faster.
In fact, the CA I used will refuse to sign keys with a non-standard public exponent, so I can't do anything funny there.
The modulus, n, is either 2,048 or 4,096 "user controlled" bits, so it's the ideal place to hide a message.
However, to use the certificate, I'll need to find two large primes that multiply out to the vanity modulus.
My method starts by picking two random primes and calculating the resulting n value.
Then, the bytes of n are modified to introduce message into the base64 encoding.
Of course, the modified n is not the product of p and q, but this is fixable by setting q to n/p.
The resulting q value is very unlikely to be a prime (or integer), so I round it and find the next prime after the ideal q:
which usually only requires changing the value of q by a few hundred.
Since p and q are similar in size, a small change q only affects the least-sigifiant half of the product:
58174124 * 918491824 = 53432457262362176
(incrementing until the next prime...)
58174124 * 9184918
43
= 5343245836
7670532
As long as the message is embedded into the upper half of n, it's likely to survive undamaged.
The original p and newly selected q can now be used to construct a functional RSA private key in the usual manner.
From here, it's really just a matter of getting a certificate aurthority to sign the key:
# Single domain
openssl
req -new
-key priv.pem
-subj
'/C=US/CN=example.com'
>
cert_request
certbot
certonly --manual
--csr
cert_request
# Wildcard
cat
> config
<<EOF
[ req ]
req_extensions = req_ext

[ req_ext ]
subjectAltName = @alt_names

[ alt_names ]
DNS.1 = *.example.com
DNS.2 = example.com
EOF
openssl
req -new
-key priv.pem
-config config
-subj
'/C=US/CN=example.com'
>
cert_request
certbot
certonly --manual
--csr
cert_request
... although since base64 operates on groups of three byte,
it is possible for the message to be misaligned and not readable.
However, since the layout of the certificate is static, it is possible to adjust the message's placement until it works:
this should take less than four attempts.
The result is a functional, trusted certificate with a longish message hidden in the public key.
Renewal is done by resumbitting the CSR and repeating the ACME chalange, which can be automated.
Base64 is missing most punctuation, but it provides the full ASCII alphabet,
and the ~150 (RSA-2048) or ~320 (RSA-4096) avalable charaters provides plenty of space for jokes.
Another option would be to target the base16 displayed in most browser's certificate viewer:
this would provide a lot more space (2 chars/byte instea of 0.75), but requires careful word choice.
As for security
, this trick obviously reduces the entropy in the private key.
I'm not aware of any factoring algorithms that could exploit key selection method, but I can't garantee they don't exist.
The method may also produce a p and q that are close together, which makes it possible to easly factor n and recover the private key.
A very small d value can also allow factorisation.
While I wouldn't trust these keys for anything important,
they should be perfectly fine for serving a public website:
modern TLS provides forward secrecy, so eavesdropping requires man-in-the-middle even if the private key is compromised.
Related
:
