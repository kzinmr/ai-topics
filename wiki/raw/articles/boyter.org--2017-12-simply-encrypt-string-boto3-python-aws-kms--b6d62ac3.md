---
title: "Simply encrypt or decrypt a string using Boto3 Python and AWS KMS"
url: "https://boyter.org/2017/12/simply-encrypt-string-boto3-python-aws-kms/"
fetched_at: 2026-05-05T07:01:59.928162+00:00
source: "Ben Boyter"
tags: [blog, raw]
---

# Simply encrypt or decrypt a string using Boto3 Python and AWS KMS

Source: https://boyter.org/2017/12/simply-encrypt-string-boto3-python-aws-kms/

Simply encrypt or decrypt a string using Boto3 Python and AWS KMS
2017/12/18
(133 words)
Another one of those things I need to look up every now and then. Below is a snippet of how to encrypt and decrypt a string using Python and KMS in AWS. The interesting thing is that you don’t need to supply the KMS key alias in the decryption portion. So long as whatever role or key you are using can access the key it should work. For the encryption you can either supply the full ARN of the key or the alias so long as you prefix it with alias/
import
base64
import
boto3
def
encrypt
(session, secret, alias):
client
=
session
.
client(
'kms'
)
ciphertext
=
client
.
encrypt(
KeyId
=
alias,
Plaintext
=
bytes(secret),
)
return
base64
.
b64encode(ciphertext[
"CiphertextBlob"
])
def
decrypt
(session, secret):
client
=
session
.
client(
'kms'
)
plaintext
=
client
.
decrypt(
CiphertextBlob
=
bytes(base64
.
b64decode(secret))
)
return
plaintext[
"Plaintext"
]
session
=
boto3
.
session
.
Session()
print encrypt(session,
'something'
,
'alias/MyKeyAlias'
)
print decrypt(session,
'AQECAINdoimaasydoasidDASD5asd45'
)
