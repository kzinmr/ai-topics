---
title: "A reasonably practical guide to validating RFC 9421 HTTP Signatures for ActivityPub in PHP"
url: "https://shkspr.mobi/blog/2026/09/a-reasonably-practical-guide-to-validating-rfc-9421-http-signatures-for-activitypub-in-php/"
fetched_at: 2026-09-04T10:00:46.614019+00:00
source: "shkspr.mobi"
tags: [blog, raw]
---

# A reasonably practical guide to validating RFC 9421 HTTP Signatures for ActivityPub in PHP

Source: https://shkspr.mobi/blog/2026/09/a-reasonably-practical-guide-to-validating-rfc-9421-http-signatures-for-activitypub-in-php/

If you're reading this, you've probably been hitting your head against a brick wall trying to parse and decipher the new HTTP Signatures sent by Mastodon and other Fediverse servers.
This is a basic and somewhat incomplete guide to accepting these signatures. I'm sure there are various gotchas, but it works with the signatures I've seen in the wild.
OK, wow, no need to be a dick about it! Here's how I validated a real signature that my server received.
Copied PHP to 📋
⧉
PHP
$verified
=
openssl_verify
(
data
:       '
"@method"
:
POST
"@target-uri"
: https:
//example.viii.fi/inbox
"content-digest"
: sha-256=:tFdB/ENGczHMlZMDb66pXoUi2d0OqH2iBHdnN/WV1mc=:
"@signature-params"
: (
"@method"
"@target-uri"
"content-digest"
);created=1787780262;keyid=
"https://mastodon.social/users/Edent#main-key"
',
signature
:
base64_decode
(
"sIfmNsM/Q8iG6AJlne1IkZVjQSVFDEYIPsnoSOXQY+W3Eb4+SOn9o4J5SQmFOP+Jecjf3ioFwUdsrFjAGkUUOHPvSbNWkGKtNuGm+C6r3aI3JBCFGPqX3ITgZYV76CF7JJJ5hPGaG8YH/XdmxVIeFfD3M39FQCncMyyq7xJJvwKKP1mzS5s1vNQie8hbQ9owRjtqvoWcmM9GEYCUHNcMPLjZc+CBrj8sfBbNTYgIFI4UtirOaRJvYymxXjmXuzeVYxQujMjAjgobxQ8QFv0zlYsHk+gS5EYyafpJG9zmfCFSoF9+ZwqKNADmuADbISD9LZIH/bmkPoNXhxaeFPqYog=="
),
public_key
:
"-----BEGIN PUBLIC KEY-----\nMIIBIjANBgkqhkiG9w0BAQEFAAOCAQ8AMIIBCgKCAQEAsYMEs4waqk/6gaS+xn1T\nYygElTtNIFNkBcEdEBMaeoGVhyZiVKtSjJCS4z+X+394PKvcfSTcFILIt2GI2jOB\nHD0M2fFgxc8mmdSdCQkgEh9jF3bFI3kopDvzYf726iioYKlHXKpfPKvFt7EJgKH7\naCtS25NQkek3YUd6y3VBcT3R6Xhze9P3QNoZMIsFXklgXDKj+EllfbUqLf1vxt3s\nmD9ETxy2bJi9FheE0uY2WhARn49XAvwczM5Wzt+zqxVEtgpi5v2+ZZAVKhDnJkiC\nCCuI6hrSnKNIx/5mSlX0a0S5h5d03djrCkYsqmwelu01rhOXP2grsz4BXp0y2wrO\n3QIDAQAB\n-----END PUBLIC KEY-----\n"
,
algorithm
:
"sha256"
);
echo
$verified
;
Copy and paste that into PHP and you should see that
$verified
is true.
Say please.
Along with the message sent to your server, you will have received HTTP headers like this:
Copied  to 📋
⧉
content-digest: sha-256=:tFdB/ENGczHMlZMDb66pXoUi2d0OqH2iBHdnN/WV1mc=:
signature: sig1=:sIfmNsM/Q8iG6AJlne1IkZVjQSVFDEYIPsnoSOXQY+W3Eb4+SOn9o4J5SQmFOP+Jecjf3ioFwUdsrFjAGkUUOHPvSbNWkGKtNuGm+C6r3aI3JBCFGPqX3ITgZYV76CF7JJJ5hPGaG8YH/XdmxVIeFfD3M39FQCncMyyq7xJJvwKKP1mzS5s1vNQie8hbQ9owRjtqvoWcmM9GEYCUHNcMPLjZc+CBrj8sfBbNTYgIFI4UtirOaRJvYymxXjmXuzeVYxQujMjAjgobxQ8QFv0zlYsHk+gS5EYyafpJG9zmfCFSoF9+ZwqKNADmuADbISD9LZIH/bmkPoNXhxaeFPqYog==:
signature-input: sig1=("@method" "@target-uri" "content-digest");created=1787780262;keyid="https://mastodon.social/users/Edent#main-key"
The
signature-input
tells you how to construct a "Signature Base". You have to build a text string which places the various components in the order specified and separated with a newline:
Copied  to 📋
⧉
"@method": POST
"@target-uri": https://example.viii.fi/inbox
"content-digest": sha-256=:tFdB/ENGczHMlZMDb66pXoUi2d0OqH2iBHdnN/WV1mc=:
"@signature-params": ("@method" "@target-uri" "content-digest");created=1787780262;keyid="https://mastodon.social/users/Edent#main-key"
Where
@method
is the HTTP method used to send data to your server (usually
GET
or
POST
), and
@target-uri
is the URl the message was sent to (usually your inbox).
The
publicKey
is slightly trickier. As you can see, the
signature-input
ends with
keyid="https://mastodon.social/users/Edent#main-key
If you make a signed request to that URl, you'll get back an ActivityPub Actor document. It will look something like this:
Copied JSON to 📋
⧉
JSON
{
"@context"
:
[
"https://www.w3.org/ns/activitystreams"
,
"https://w3id.org/security/v1"
,
]
,
"id"
:
"https://mastodon.social/users/Edent"
,
"webfinger"
:
"Edent@mastodon.social"
,
"type"
:
"Person"
,
"name"
:
"Terence Eden"
,
"publicKey"
:
{
"id"
:
"https://mastodon.social/users/Edent#main-key"
,
"owner"
:
"https://mastodon.social/users/Edent"
,
"publicKeyPem"
:
"-----BEGIN PUBLIC KEY-----\nMIIBIjANBgkqhkiG9w0BAQEFAAOCAQ8AMIIBCgKCAQEAsYMEs4waqk/6gaS+xn1T\nYygElTtNIFNkBcEdEBMaeoGVhyZiVKtSjJCS4z+X+394PKvcfSTcFILIt2GI2jOB\nHD0M2fFgxc8mmdSdCQkgEh9jF3bFI3kopDvzYf726iioYKlHXKpfPKvFt7EJgKH7\naCtS25NQkek3YUd6y3VBcT3R6Xhze9P3QNoZMIsFXklgXDKj+EllfbUqLf1vxt3s\nmD9ETxy2bJi9FheE0uY2WhARn49XAvwczM5Wzt+zqxVEtgpi5v2+ZZAVKhDnJkiC\nCCuI6hrSnKNIx/5mSlX0a0S5h5d03djrCkYsqmwelu01rhOXP2grsz4BXp0y2wrO\n3QIDAQAB\n-----END PUBLIC KEY-----\n"
}
,
The
publicKeyPem
is the string you need. There's no need to convert the
\n
to literal newlines.
Not quite! All we've done so far is verify the headers. It is possible that these are genuine headers but attached to a fraudulent body.
This takes us back to the header
"content-digest": sha-256=:tFdB/ENGczHMlZMDb66pXoUi2d0OqH2iBHdnN/WV1mc=:
That says that the body of the message sent has a Base64 encoded SHA256 hash of
tFdB/ENGczHMlZMDb66pXoUi2d0OqH2iBHdnN/WV1mc=
.
To calculate your own content digest in PHP:
Copied PHP to 📋
⧉
PHP
$input
=
file_get_contents
(
"php://input"
);
$digestCalculated
=
base64_encode
(
hash
(
algo
:
"sha256"
,
data
:
$input
,
binary
:
true
)
);
Does your digest match the one sent along with the headers? If not, something dodgy is going on.
The steps are:
Get the headers.
Get the body.
From the headers'
content-digest
extract the algorithm and hash.
Using the body, calculate your own hash using the algorithm from
content-digest
.
Does your hash match the sent hash? If not, stop. If so, proceed.
From the headers'
signature
extract the base64 encoded signature.
From the headers'
signature-input
extract the signature-input string.
From the signature-input string extract the order of the Signature Base.
Construct the Signature Base.
From the signature-input string extract the keyid.
Get the Public Key from the keyid.
Use
openssl_verify()
to verify the Signature Base and the base64 decoded signature, against the Public Key using SHA256.
Note,
Mastodon
only
uses SHA256
.  I think it should explicitly say which algorithm it is using
and have raised the issue
.
This is how you do it in PHP. Please read this carefully as there are some hard-coded assumptions.
Copied PHP to 📋
⧉
PHP
<?php
//  Validate the Digest.
//  It is the hash of the raw input string, in binary, encoded as base64.
//  The format is content-digest => <algorithm>=:<base64 encoded hash>:
$digestString
=
$headers
[
"content-digest"
];
//  The Base64 encoding may have multiple `=` at the end. So split this at the first `=`.
$digestData
=
explode
(
separator
:
"="
,
string
:
$digestString
,
limit
: 2 );
//  Hashes are in lowercase, but have a `-` in their name.
//  This is not what hash_algos() expects.
$digestAlgorithm
=
str_replace
(
search
:
"-"
,
replace
:
""
,
subject
:
$digestData
[0] );
//  The hash is surrounded by `:` characters.
$digestHash
=
str_replace
(
search
:
":"
,
replace
:
""
,
subject
:
$digestData
[1] );
//  Check if the hash algorithm is one known about to PHP.
//  If not, reject and record an error.
if
( !
in_array
( needle:
$digestAlgorithm
,
haystack
:
hash_algos
() ) ) {
return
false
;
}
//  Manually calculate the digest based on the data sent.
$digestCalculated
=
base64_encode
(
hash
(
algo
:
$digestAlgorithm
,
data
:
$input
,
binary
:
true
) );
//  Does our calculation match what was sent?
if
( !(
$digestCalculated
==
$digestHash
) ) {
return
false
;
}
//  The signature format is signature => <signature name>=:<base64 encoded hash>:
$signatureString
=
$headers
[
"signature"
];
//  The Base64 encoding may have multiple `=` at the end. So split this at the first `=`.
$signatureData
=
explode
(
separator
:
"="
,
string
:
$signatureString
,
limit
: 2 );
$signatureName
=
$signatureData
[0];
//  The signature is surrounded by `:` characters.
$signatureB64
=
str_replace
(
search
:
":"
,
replace
:
""
,
subject
:
$signatureData
[1] );
//  The signature-input format is complicated!
$signatureInputString
=
$headers
[
"signature-input"
];
//  Get the parameters. Assume there is only one signature.
$signatureParamsString
=
explode
(
separator
:
"="
,
string
:
$signatureInputString
,
limit
: 2 )[1];
//  Get the different elements of the signature.
$signatureInputData
=
explode
(
separator
:
";"
,
string
:
$signatureInputString
);
//  Construct the data.
$signatureInput
= [];
foreach
(
$signatureInputData
as
$signatureInputParts
) {
$partsData
=
explode
(
separator
:
"="
,
string
:
$signatureInputParts
);
//  Strip quotes from keyid and parentheses from sig1.
if
(
"keyid"
==
$partsData
[0] ) {
$partsData
[1] =
str_replace
(
search
:
"\""
,
replace
:
""
,
subject
:
$partsData
[1] );
    }
if
(
$signatureName
==
$partsData
[0] ) {
$partsData
[1] =
str_replace
(
search
: [
"("
,
")"
],
replace
:
""
,
subject
:
$partsData
[1] );
    }
$signatureInput
[
$partsData
[0] ] =
$partsData
[1] ;
}
$signatureStructure
=
$signatureInput
[
$signatureName
];
$signatureKeyID
=
$signatureInput
[
"keyid"
];
//  Remove quotes.
$signatureStructure
=
str_replace
(
search
:
"\""
,
replace
:
""
,
subject
:
$signatureStructure
);
$signatureStructureData
=
explode
(
separator
:
" "
,
string
:
$signatureStructure
);
//  https://www.rfc-editor.org/info/rfc9421/#section-2.5
$signatureBase
=
""
;
foreach
(
$signatureStructureData
as
$signatureStructureParts
) {
if
(
"@method"
==
$signatureStructureParts
) {
//  https://www.rfc-editor.org/info/rfc9421/#name-method
$signatureBase
.=
"\"@method\": "
.
$_SERVER
[
"REQUEST_METHOD"
] .
"\n"
;
    }
if
(
"@target-uri"
==
$signatureStructureParts
) {
//  https://www.rfc-editor.org/info/rfc9421/#section-2.2.2
//  Change the domain name to your own.
$signatureBase
.=
"\"@target-uri\": https://EXAMPLE.COM"
.
$_SERVER
[
"REQUEST_URI"
] .
"\n"
;
    }
if
(
"content-digest"
==
$signatureStructureParts
) {
$signatureBase
.=
"\"content-digest\": $digestString\n"
;
    }
}
//  https://victoronsoftware.com/posts/http-message-signatures/#how-the-signature-is-created
$signatureBase
.=
"\"@signature-params\": $signatureParamsString"
;
//  Get the signing user's public key.
//  This is usually in the form `https://example.com/user/username#main-key`
//  This is to differentiate if the user has multiple keys.
//  This may need to be a signed request. You will need to write your own getDataFromURl() function to get the sending user's key.
$userData
=
getDataFromURl
(
$signatureKeyID
);
$publicKey
=
$userData
[
"publicKey"
][
"publicKeyPem"
];
//  Verify the request
$verified
=
openssl_verify
(
data
:
$signatureBase
,
signature
:
base64_decode
(
$signatureB64
),
public_key
:
$publicKey
,
algorithm
:
$digestAlgorithm
);
//  Convert the result to boolean.
if
(
$verified
=== 1 ) {
$verified
=
true
;
}
elseif
(
$verified
=== 0 ) {
$verified
=
false
;
}
else
{
$verified
=
null
;
}
return
$verified
;
This blog post was funded in part by the work I'm doing for my NLnet NGI0 grant. Thanks!
