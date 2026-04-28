---
title: "How Bitwarden Encrypts and Decrypts Secrets"
url: "https://blog.miguelgrinberg.com/post/how-bitwarden-encrypts-and-decrypts-secrets"
fetched_at: 2026-04-28T07:01:32.491246+00:00
source: "miguelgrinberg.com"
tags: [blog, raw]
---

# How Bitwarden Encrypts and Decrypts Secrets

Source: https://blog.miguelgrinberg.com/post/how-bitwarden-encrypts-and-decrypts-secrets

As part of my efforts in reducing my dependency on Big Tech, I have been researching how to self-host my password manager. One solution that looks very promising is
Vaultwarden
, an open source clone of the Bitwarden cloud server. An interesting aspect of this server is that it stores all the secrets in a standard SQLite database, so in addition to having the self-hosted password server I could keep a backup copy of the database on my machine and query it directly. But of course, the secrets are encrypted in this database, so they are useless unless I learn how to decrypt them, similar to how the Bitwarden clients do it.
Speaking of the Bitwarden clients, while I was writing this article it came out that the official Bitwarden CLI client
was compromised
in a supply chain attack. This is a tool that I personally use and have on all my computers, so this feels like a wake up call to me. Luckily I did not install the compromised version myself, but I think there is an argument to be made about rolling your own secret management client instead of relying on the one all the hackers are after!
In this article I'll share how the encryption of secrets works in Bitwarden and its Vaultwarden clone. I'll also include working Python code, in case you want to tinker with this and like myself, would be interested in building your own tooling to keep your secrets safe.
The 10,000 foot view
Okay, let's get to it, first at a high enough level to keep things simple.
Bitwarden, Vaultwarden and pretty much any half decent password manager store all your secrets encrypted in the server. When I say "secrets" I do not mean just the passwords, but also the usernames, URLs, notes, attachments and everything else that you store that applies to each secret. Bitwarden even encrypts the name you give to each secret. Only the client knows how to encrypt or decrypt, and it always encrypts data before sending it to the server. The server only knows how to store and retrieve blobs of encrypted data from a database.
To encrypt and decrypt secrets, the client uses a master key that is associated with your account. The master key is a random sequence of bytes that is generated in the client at the time you create an account. Like the secrets, this master key is itself encrypted before it is sent to the server for storage. The encryption algorithm used to encrypt the master key is similar to that of the secrets, but they encryption key in this case is generated from the the passphrase chosen by the user to protect the account.
So you see, the account passphrase is not directly used to encrypt your secrets as many people think, it just encrypts the master key. To be able to decrypt your secrets, the Bitwarden client first uses your passphrase to decrypt the master key. Then it uses the master key to decrypt your actual secrets. When the client leaves your vault unlocked, it just means that it is keeping a copy of the decrypted master key in memory (or maybe the whole decrypted vault), so that it can return secrets to you without you having to type your passphrase again. To lock your vault, all the client needs to do is discard the master key.
The master key
I will now share the details of how things work, which as far as I know are not formally documented anywhere. I had to dig through the Bitwarden and Vaultwarden source code to figure out a lot of these details.
As stated above, each user on Bitwarden has a master key, which is used as an encryption key during encryption and decryption of secrets. A master key is a randomly generated sequence of 64 bytes, so there is really nothing special about it. Here is how easy it is to generate a master key directly in the Python console:
>>> import random
>>> random.randbytes(64)
b'\xa3?\xbc\x86\x18\x7f\x9c|\xe2\xf1\x10\xd4\xee B\xde\x93\x12g\x03\\\x83\x9a\xc5S<!\x18\xc0\x0eRp\xb5\xbc`\xfc\xceu)\x93Q\x84r\xaa\xd6\xde\x1f\xc6Y\x92\x85?\xf8j\x95\xe98\x8e\xe5\xe0\x98\xd8\x85\x9c'
Bitwarden splits the key in two halves of 32 bytes each. The first half is used as a 256-bit encryption key, while the second half is used to generate message authentication codes or MACs, which are cryptographic signatures that verify the integrity of encrypted strings. Let's separate the key into its two components, which I'm going to call
enc_key
and
mac_key
:
# the following master key is used for demonstration purposes, never write a real master key in your code!
master_key = b'\xa3?\xbc\x86\x18\x7f\x9c|\xe2\xf1\x10\xd4\xee B\xde\x93\x12g\x03\\\x83\x9a\xc5S<!\x18\xc0\x0eRp\xb5\xbc`\xfc\xceu)\x93Q\x84r\xaa\xd6\xde\x1f\xc6Y\x92\x85?\xf8j\x95\xe98\x8e\xe5\xe0\x98\xd8\x85\x9c'

enc_key = master_key[:32]
mac_key = master_key[32:]
Decoding a Bitwarden secret
Now that we have a master key, we can look at how to decode a secret. For this I'll start by showing you an example secret, exactly as it would be stored in a Bitwarden or Vaultwarden database. Here it is:
encrypted_secret = '2.IkWFb104bXv7Zwl7eFbsnQ==|SB42jIOvjhV32hSusW/J7WfAnQV8DKIV/CJQB7IDaiz4lQv4lIcXzWp9+IT0ncVQ|S8Tcp2klhcOOzZvoA0C9WRURaWUq+U1F9jbuBskDIz0='
Encrypted secrets start with an encryption format version, followed by a period. The version currently in use is version
2
. The encrypted payload comes after the period, and contains three parts separated by pipe characters:
iv
: an initialization vector, used to "prime" the encryption or decryption engine
ciphertext
: the encrypted secret
mac
: a MAC signature for this secret, used to verify its integrity
These three sections are all binary sequences written in
base64
encoding, which ensures all characters are printable. Below you can see some more Python code to decode the secret into its parts:
from base64 import b64decode
# ...

version, payload = encrypted_secret.split('.', 2)
if version != '2':
    raise ValueError('Unsupported encryption version')
fields = payload.split('|')
if len(fields) != 3:
    raise ValueError('Invalid encrypted data')
iv = b64decode(fields[0])
ciphertext = b64decode(fields[1])
mac = b64decode(fields[2])
Before attempting to decrypt the secret, we need to ensure that the encrypted string isn't corrupted or altered in any way. For this we can independently calculate the MAC signature and then compare it against the
mac
value included in the secret. If the two are different, then we'll know that the encrypted string has been corrupted or tampered with, so in that case this secret should be discarded as invalid.
For the signature, Bitwarden computes a standard
HMAC
hash of the concatenation of
iv
and
ciphertext
, using the
SHA-256
hash function. The secret key used to calculate this hash is the
mac_key
part of the master key. If you are not familiar with cryptographic functions then just know that this is a standard cryptographic calculation, so common that it is available in the Python standard library. Below you can see Python code that calculates the value of
mac
and then confirms that the calculated value is identical to the
mac
value that comes with the secret:
import hashlib
import hmac
# ...

calculated_mac = hmac.new(mac_key, iv + ciphertext, hashlib.sha256).digest()
if calculated_mac != mac:
    raise ValueError('Invalid data or key')
If the
mac
test passes, then everything looks good and we can proceed to decrypt the value.
The encryption algorithm used by Bitwarden is also well known, it is called
AES
, which is short for Advanced Encryption Standard. If you can tolerate another bit of cryptographic jargon, I can add that the encryption uses a
CBC
mode of operation, 128-bit blocks, and
PKCS#7
padding. The
iv
portion of the secret is the initialization vector parameter that the AES encryption needs, and the
enc_key
part of the master key is used as the encryption or decryption key. Once again, you do not need to understand what all this means, since I'll show you Python code that takes care of everything in a moment.
Unfortunately the Python standard library does not include support for AES, so a third-party package needs to be installed. I've found a few and chosen
pyaes
, which is written in pure Python. If you are going to install this on your computer, I recommend that you first make a virtual environment.
pip install pyaes
Here is the Python code to decrypt the secret:
import pyaes
# ...

decrypter = pyaes.Decrypter(pyaes.AESModeOfOperationCBC(enc_key, iv))
secret = decrypter.feed(ciphertext) + decrypter.feed()
print(secret)
The
decrypter
object from the
pyaes
package decrypts whatever is passed through its
feed()
method. It is designed so that you can pass the encrypted data in chunks, so when you are done you have to call the method with no arguments to indicate that you have sent all the data. The method returns the decrypted data also in chunks, so all the return values have to be appended.
Ready to try this? Below is the complete Python script to decrypt the secret:
from base64 import b64decode
import hashlib
import hmac
import pyaes

# the following master key is used for demonstration purposes, never write a real master key in your code!
master_key = b'\xa3?\xbc\x86\x18\x7f\x9c|\xe2\xf1\x10\xd4\xee B\xde\x93\x12g\x03\\\x83\x9a\xc5S<!\x18\xc0\x0eRp\xb5\xbc`\xfc\xceu)\x93Q\x84r\xaa\xd6\xde\x1f\xc6Y\x92\x85?\xf8j\x95\xe98\x8e\xe5\xe0\x98\xd8\x85\x9c'

enc_key = master_key[:32]
mac_key = master_key[32:]

encrypted_secret = '2.IkWFb104bXv7Zwl7eFbsnQ==|SB42jIOvjhV32hSusW/J7WfAnQV8DKIV/CJQB7IDaiz4lQv4lIcXzWp9+IT0ncVQ|S8Tcp2klhcOOzZvoA0C9WRURaWUq+U1F9jbuBskDIz0='

version, payload = encrypted_secret.split('.', 2)
if version != '2':
    raise ValueError('Unsupported encryption version')
fields = payload.split('|')
if len(fields) != 3:
    raise ValueError('Invalid encrypted data')
iv = b64decode(fields[0])
ciphertext = b64decode(fields[1])
mac = b64decode(fields[2])

calculated_mac = hmac.new(mac_key, iv + ciphertext, hashlib.sha256).digest()
if calculated_mac != mac:
    raise ValueError('Invalid data or key')

decrypter = pyaes.Decrypter(pyaes.AESModeOfOperationCBC(enc_key, iv))
secret = decrypter.feed(ciphertext) + decrypter.feed()
print(secret)
Run the script to see the secret message that I encrypted in this example:
$ python decrypt.py
b'The quick brown fox jumps over the lazy dog'
Securing the master key
The example in the previous section has the bulk of the logic needed to decrypt Bitwarden secrets, but it has the master key right there in the code in plain text. The Bitwarden server returns the master key to the client as an encrypted string, and the client needs to ask the user to type their email and their passphrase to be able to decrypt it. We'll now add this to the script.
As I did with the secret in the previous section, I'll start by showing you an example encrypted master key, and then we'll work on the steps required to decrypt it. Here is the master key I used above, but now encrypted:
encrypted_master_key = '2.i5dH92a79wJ8L8tsqQEdLw==|a5swb8CeW5cTM2N+XQZCF+mX263BMaag+ghxiu+ci4W+fqqLZ82g+i7ReIcdiPLafoCAmeWZE48PETGJOsoOb6DcrK3sRdvHCx8xbRt1Xas=|MhY1/he1RntesSYJyZqFh8s8dQTXqmPRQM2hVcsjIWk='
What do you think? This looks pretty familliar, right? Bitwarden uses the same algorithm it uses for the secrets to encrypt the master key. The only difference is that the
enc_key
and
mac_key
values for this encryption are derived from the email address and the passphrase.
Given that we'll need to run the decryption algorithm first to decrypt the master key and then again to decrypt secrets, it makes sense to refactor all that logic into a function:
from base64 import b64decode
import hashlib
import hmac
import pyaes

def decrypt(encrypted_data, enc_key, mac_key):
    version, payload = encrypted_data.split('.', 2)
    if version != '2':
        raise ValueError('Unsupported encryption version')
    fields = payload.split('|')
    if len(fields) != 3:
        raise ValueError('Invalid encrypted data')
    iv = b64decode(fields[0])
    ciphertext = b64decode(fields[1])
    mac = b64decode(fields[2])

    calculated_mac = hmac.new(mac_key, iv + ciphertext, hashlib.sha256).digest()
    if calculated_mac != mac:
        raise ValueError('Invalid data or key')

    decrypter = pyaes.Decrypter(pyaes.AESModeOfOperationCBC(enc_key, iv))
    return decrypter.feed(ciphertext) + decrypter.feed()
What we need now is to generate the
enc_key
and
mac_key
values to send to this function with the encrypted master key. For this, Bitwarden uses a combination of two standard cryptographic operations called
key derivation
and
key stretching
, which it applies to the information entered by the user.
Let's start by asking the user for their details:
from getpass import getpass
# ...

email = input('Email address: ')
passphrase = getpass('Passphrase: ')
Now we need to use these details to "derive" a key that we can use. For key derivation, Bitwarden uses the
PBKDF2
function, which also happens to be common enough that it is included in the Python standard library:
temp_key = hashlib.pbkdf2_hmac('sha256', passphrase.encode(), email.encode(), 600000, 32)
You may have noticed that most of the cryptographic functions that we are using are operations that are built on top of the
SHA-256
hashing function. The key derivation is no exception, but for this function the name of the hashing function has to be given as a string.
The key derivation function takes the passphrase and a
salt
as arguments. In cryptography, a salt is an additional input that is added to the main payload, with the purpose to make brute force attacks more costly for the attacker. In this instance Bitwarden uses the email address as salt. The function needs the passphrase and the email in binary form, so I'm using the
encode()
method to convert them to bytes.
Key derivation functions repeat a basic operation for a number of iterations. This is done first to separate the derived key as much as possible from the original passphrase, but also to make the computation expensive, because if someone were to attempt to figure out a key with brute force methods, you'd want this to be an unbearably slow process. Current Bitwarden accounts use 600,000 iterations for this step. The Bitwarden client receives the actual number of iterations associated with an account from the server, so this number isn't guaranteed to be 600,000 for every account. The number of iterations is increased from time to time, to keep up with performance improvements in hardware.
The last argument to the key derivation function is the derived key length, in bytes. Bitwarden uses keys that are 32 bytes long.
I should note that Bitwarden gives users the option to change the key derivation function to another one called
Argon2id
. Argon2id is considered to be more secure than PBKDF2, but it is also more resource intensive in terms of RAM and compute power. I would imagine that at some point in the future Bitwarden may decide to make Argon2id the default.
But anyway, you may have noticed that I called this derived key a
temp_key
in the code above. This is because we are not done yet. If you recall, we need two keys of 32 bytes each, one for the encryption key and another for the MAC signature calculation. Bitwarden uses the
HKDF-Expand
key stretching algorithm to generate these two from
temp_key
.
The HKDF algorithm does not exist in the Python standard library, so a third party package needs to be installed:
pip install hkdf
Here is how to "stretch"
temp_key
into the two keys that we need:
from hkdf import hkdf_expand
# ...

master_enc_key = hkdf_expand(temp_key, b'enc', 32, hashlib.sha256)
master_mac_key = hkdf_expand(temp_key, b'mac', 32, hashlib.sha256)
The key stretching algorithm accepts a source key, an "info" argument that provides context to the stretching operation, the length of the stretched key in bytes, and once again, the base cryptographic hashing function to use, which is SHA-256 as before.
Bitwarden uses
enc
and
mac
as context for each key stretching operation. This allows us to use the same source key for both, yet obtain very different stretched keys.
Now we are ready to decode the master key using the
decrypt()
function from before:
master_key = decrypt(encrypted_master_key, master_enc_key, master_mac_key)
And now that we have a master key, we can go ahead and decrypt the secret, also with the
decrypt()
function
enc_key = master_key[:32]
mac_key = master_key[32:]
print('Secret:', decrypt(encrypted_secret, enc_key, mac_key).decode())
To keep things well organized, I decided to refactor the logic that decrypts the master key into a function:
def decrypt_master_key(encrypted_master_key, email, passphrase, iterations=600000):
    temp_key = hashlib.pbkdf2_hmac('sha256', passphrase.encode(), email.encode(), iterations, 32)
    master_enc_key = hkdf_expand(temp_key, b'enc', 32, hashlib.sha256)
    master_mac_key = hkdf_expand(temp_key, b'mac', 32, hashlib.sha256)
    return decrypt(encrypted_master_key, master_enc_key, master_mac_key)
Below is the complete decryption script, this time without any sensitive information in the code:
from base64 import b64decode
from getpass import getpass
import hashlib
import hmac
import pyaes
from hkdf import hkdf_expand

def decrypt(encrypted_data, enc_key, mac_key):
    version, payload = encrypted_data.split('.', 2)
    if version != '2':
        raise ValueError('Unsupported encryption version')
    fields = payload.split('|')
    if len(fields) != 3:
        raise ValueError('Invalid encrypted data')
    iv = b64decode(fields[0])
    ciphertext = b64decode(fields[1])
    mac = b64decode(fields[2])

    calculated_mac = hmac.new(mac_key, iv + ciphertext, hashlib.sha256).digest()
    if calculated_mac != mac:
        raise ValueError('Invalid data or key')

    decrypter = pyaes.Decrypter(pyaes.AESModeOfOperationCBC(enc_key, iv))
    return decrypter.feed(ciphertext) + decrypter.feed()

def decrypt_master_key(encrypted_master_key, email, passphrase, iterations=600000):
    temp_key = hashlib.pbkdf2_hmac('sha256', passphrase.encode(), email.encode(), iterations, 32)
    master_enc_key = hkdf_expand(temp_key, b'enc', 32, hashlib.sha256)
    master_mac_key = hkdf_expand(temp_key, b'mac', 32, hashlib.sha256)
    return decrypt(encrypted_master_key, master_enc_key, master_mac_key)

encrypted_master_key = '2.i5dH92a79wJ8L8tsqQEdLw==|a5swb8CeW5cTM2N+XQZCF+mX263BMaag+ghxiu+ci4W+fqqLZ82g+i7ReIcdiPLafoCAmeWZE48PETGJOsoOb6DcrK3sRdvHCx8xbRt1Xas=|MhY1/he1RntesSYJyZqFh8s8dQTXqmPRQM2hVcsjIWk='
encrypted_secret = '2.IkWFb104bXv7Zwl7eFbsnQ==|SB42jIOvjhV32hSusW/J7WfAnQV8DKIV/CJQB7IDaiz4lQv4lIcXzWp9+IT0ncVQ|S8Tcp2klhcOOzZvoA0C9WRURaWUq+U1F9jbuBskDIz0='

email = input('Email address: ')
passphrase = getpass('Passphrase: ')

master_key = decrypt_master_key(encrypted_master_key, email, passphrase)
enc_key = master_key[:32]
mac_key = master_key[32:]
print('Secret:', decrypt(encrypted_secret, enc_key, mac_key).decode())
To be able to decode the example secret from above you will need to use the email and passphrase that I've chosen for this example, which are
somebody@example.com
and
the moon landing was fake
respectively. Here is an example run of the script showing the decoded secret:
$ python decrypt.py
Email: somebody@example.com
Passphrase: the moon landing was fake
Secret: The quick brown fox jumps over the lazy dog
Encrypting secrets
The script that I shared in the previous section could serve as the basis for a complete secret decryption solution that is designed to work with a database such as the one Vaultwarden maintains, without the need to use web APIs or actually any networking at all.
At this point I wondered if I could also work out how to encrypt, which would allow me to insert new secrets in the same way the Bitwarden clients do it. And as it turns out, after figuring out the decryption, adding encryption was easy.
To do this I just worked backwards through the
decrypt()
function to build
encrypt()
:
import random
# ...

def encrypt(secret, enc_key, mac_key):
    if isinstance(secret, str):
        secret = secret.encode()
    iv = random.randbytes(16)
    encrypter = pyaes.Encrypter(pyaes.AESModeOfOperationCBC(enc_key, iv))
    ciphertext = encrypter.feed(secret) + encrypter.feed()
    mac = hmac.new(mac_key, iv + ciphertext, hashlib.sha256).digest()
    return f'2.{b64encode(iv).decode()}|{b64encode(ciphertext).decode()}|{b64encode(mac).decode()}'
First, and only as a convenience, if the secret that is passed to the function is a string, I convert it to bytes. Encryption and decryption always works with bytes.
As you recall, the three parts of the secret are
iv
,
ciphertext
and
mac
. When encrypting, the
iv
part can be any sequence of 16 random bytes, which are used to initialize the encryption engine. The bytes that are used do not matter, as long as the decryption side uses the same ones. The
ciphertext
component is the secret after it is encrypted with the AES algorithm, so here I used
pyaes
to generate it. Finally we already know how to calculate the
mac
signature, so that is done exactly as before.
Once all the parts are generated, the function returns a string formatted as Bitwarden likes it, starting with version
2
, a period, and then the three parts of the encrypted secret with
|
separators.
As a bonus, I also created a function that encrypts master keys:
def encrypt_master_key(master_key, email, passphrase, iterations=600000):
    temp_key = hashlib.pbkdf2_hmac('sha256', passphrase.encode(), email.encode(), iterations, 32)
    master_enc_key = hkdf_expand(temp_key, b'enc', 32, hashlib.sha256)
    master_mac_key = hkdf_expand(temp_key, b'mac', 32, hashlib.sha256)
    return encrypt(master_key, master_enc_key, master_mac_key)
Now with the
encrypt()
and
encrypt_master_key()
functions I can generate secrets that are fully interoperable with those stored by Bitwarden and Vaultwarden. I can even generate new accounts with their own master keys. The following example generates a brand new master key, encrypts a secret with it, and then prints both the encrypted master key and the encrypted secret:
email = input('Email address: ')
passphrase = getpass('Passphrase: ')

master_key = random.randbytes(64)
encrypted_master_key = encrypt_master_key(master_key, email, passphrase)
print(f'Master key: {encrypted_master_key}')

enc_key = master_key[:32]
mac_key = master_key[32:]
encrypted_secret = encrypt('The quick brown fox jumps over the lazy dog', enc_key, mac_key)
print(f'Secret: {encrypted_secret}')
If someone gets hold of your encrypted master key and secret, they would need to guess your email and your passphrase to decode them. Without those, they would have no way to exploit them.
Conclusion
Now that I know how Bitwarden secrets are encrypted I think I'll probably end up writing my own little client. I like the idea of having all my secrets conveniently stored in a local SQLite database, so I'll probably build a solution that syncs with a Vaultwarden database, but keeps secret management local.
In any case, I hope you enjoyed discovering how Bitwarden secrets work with me! There are many more Bitwarden features to explore, so this will probably turn out to be the first of a series of articles. Feel free to let me know below in the comments what other aspects of Bitwarden or Vaultwarden you would want me to cover!
Thank you for visiting my blog! If you enjoyed this article, please consider supporting my work and keeping me caffeinated with a small one-time donation through
Buy me a coffee
. Thanks!
