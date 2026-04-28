---
title: "Using PGP Keys"
url: "https://jyn.dev/using-pgp-keys/"
fetched_at: 2026-04-28T07:02:52.159297+00:00
source: "jyn.dev"
tags: [blog, raw]
---

# Using PGP Keys

Source: https://jyn.dev/using-pgp-keys/

What is GPG?
GPG
is a program for encrypting your files, including
Documents
Music
Programs
Anything else you can store digitally
Technically
, GPG implements the
PGP
standard,
which is
mandated
by the
IETF®
.
What is encryption?
Encryption
is a way of ensuring that
only
people you choose
are able to read your information. Encryption goes back thousands of years
to the
Roman empire
. It is
used every day
in the
HTTPS
protocol, which ensures that the websites you visit
are only visible to you, and that the site has not
been changed in transit
.
Cryptography therefore has two major functions:
To encrypt data: to make sure only people you choose can read it, and
To sign data: to ensure that information you read has not been altered by third parties.
How do I get GPG?
GPG is only fully-featured when used from the
command line
.
If that sounds foreign to you, I have a quick-and-dirty guide on
GitHub
.
Some binary releases:
Debian/Ubuntu:
sudo apt-get install gnupg
Windows:
GPG4Win
macOS:
without brew:
GPGtools.org
with
brew
installed:
brew install gnupg
How do I use GPG?
Now we get to the fun stuff! GPG uses what's called
asymmetric encryption
,
which allows
anyone
to send secure messages to you, but only you to read them.
In order to take full advantage, you'll need to
Make a key
Publish your key
Start signing things
Make a key
You need a
passphrase
to use a GPG key.
This prevents anyone from using your key.
gpg
--
quick-gen-key
"
Joe Shmoe <
[email protected]
>
"
Enter your passphrase into the prompt that pops up.
Publish your key
gpg
--
send-keys
Start signing things
Sign things with git:
gpg config --global commit.gpgsign true
Sign your emails with supporting clients:
Join
Keybase
More information
Appendix
Prompts are repeated
Note that the following prompt appears
twice
when you generate a key:
We need to generate a lot of random bytes.
It is a good idea to perform some other action (type on the keyboard,
move the mouse, utilize the disks) during the prime generation;
this gives the random number generator a better chance to gain enough entropy.
This is because there are actually two keys being generated:
1 private key and 1 public. The private you will store on your computer
securely. The public you will upload to a keyserver for anyone to see.
What if I'm not comfortable with shell quoting?
Use
gpg --gen-key
or
gpg --full-gen-key
.
