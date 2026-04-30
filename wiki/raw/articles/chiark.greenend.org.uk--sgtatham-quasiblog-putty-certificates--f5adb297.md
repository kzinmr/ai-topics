---
title: "Implementing OpenSSH certificate support in PuTTY"
url: "https://www.chiark.greenend.org.uk/~sgtatham/quasiblog/putty-certificates/"
fetched_at: 2026-04-30T07:00:49.809882+00:00
source: "chiark.greenend.org.uk/~sgtatham"
tags: [blog, raw]
---

# Implementing OpenSSH certificate support in PuTTY

Source: https://www.chiark.greenend.org.uk/~sgtatham/quasiblog/putty-certificates/

Implementing OpenSSH certificate support in PuTTY
[Simon Tatham, 2022-12-03]
In 2022, PuTTY gained support for the OpenSSH certificate system, allowing you to configure your client to accept host keys automatically if they're signed by a local CA, and pass certified user keys to servers that are configured to accept them.
My sponsor and lead partner for this work was
Teleport
. After the work was done, they asked if I'd write something about it.
Full-stack difficulty
A lot of new features in PuTTY are ‘local’, in the sense that they mostly affect just one part of the code – say, the SSH layer, or the cryptography, or the terminal. Perhaps they might need a small piece of support elsewhere (say, a checkbox in the GUI to turn the new feature on, or an identifier in the SSH protocol to negotiate the new crypto algorithm), but those parts are usually easy. The typical feature is only hard in one place.
But certificate support is hard almost everywhere. The mere fact that some keys are certificates
at all
required changes in the internal APIs for public keys, and so did the idea that multiple public key types are strongly related to each other (the certified and uncertified versions of the same algorithm). The SSH code that decides whether to accept a host key needed to be restructured; there were design challenges in Pageant, in the user interface, and in the configuration data format. This feature impacts almost every part of the code except the terminal emulation, and most of those parts needed thought about how to do it
right
.
The only part that
wasn't
too hard was the low-level cryptography, because OpenSSH's certificate format is based on public-key algorithms and data formats that an SSH implementation has to support already to work at all. (That's one reason OpenSSH designed it this way, rather than using the more popular but
far
more complicated X.509 format.)
So to implement a feature as far-reaching as this, I wasn't going to be able to just keep my brain focused on one system. And I couldn't implement it one subsystem at a time in strict order, either (say, crypto layer, then SSH layer, then UI), because all the design requirements on those systems affect each other, and I had no confidence that I wouldn't get half way through one layer and realise I should have done another layer differently. Maybe somebody somewhere can plan a piece of work like this with perfect foresight – but I'm not that person.
So instead, I implemented all those pieces in parallel with each other, switching back and forth between all the different parts of the code, and revising each part whenever work on another part revealed the need for changes. I didn't totally avoid rework of previous decisions, but I at least never had to
completely
tear down and redo any particular part – and it's cheaper to rework something that's only half done than it is once it's all done.
That extra context-switching is cognitively hard, of course. But more: it's
emotionally
hard, because I find it easy to get into a mental state where whichever part I'm not focusing on right now just doesn't seem very interesting to me. And then when I switch contexts and work on that part, it's often a part that a moment ago I was thinking of as boring and unmotivating. So I had to keep consciously readjusting my
feelings
about the code I was working on, so that I'd give each part the attention it deserves, and resist the temptation to do a sloppy rush job that I'd regret later.
In particular, user interface polish is always tempting to neglect when I'm focusing on something lower-level. (‘I'm trying to make it
secure!
Why should I care about line wrapping in some dialog box?’) Especially because of all the switching back and forth, it took constant effort to remind myself that both are important, and the UI details needed as much thought as – if not more than – the low-level crypto details and security considerations. Looked at the right way, the line wrapping in your dialog box
is
a security consideration – if the important information falls off the right-hand edge of the window, the user won't know the thing they need to!
Refactorings big and small
Any significant feature, added to a code base that wasn't previously designed for it, is going to demand some refactoring. I couldn't just drop certificates into the PuTTY code as it was before. First I had to make a certificates-shaped space to drop them into. This involved a lot of changes, big and small.
A lot of them were the usual kind of pure-refactoring changes. For example, separating pieces of code that had previously been tied together, so that one of them can be reused at a second call site. I won't go through them in detail: most of them were tiny, meaningless to someone not already familiar with the code, and not that interesting.
Another slightly more interesting class of refactoring involved automating a previously cumbersome manual operation, so that we could do it more often without losing patience. For example, PuTTY's host key dialog boxes used to be painful to edit, because the line breaking in the text was done by hand and baked into the Windows dialog box definition. But that was all right because we only had two of them (for a new host key or a changed one). But once certificates get involved, there's a much larger range of things the host key prompt might need to tell you about, so the message has to be assembled at run time from a set of optional pieces. So I wrote code to lay out the dialog box automatically, with word wrapping and automatically getting the window size right.
The most interesting kind of change is when something now has to work in a completely new way. One example of this is the new need for global configuration.
For the whole of PuTTY's lifetime, saved sessions have been independent of each other. The settings for connecting to a given host are stored completely separately from all other hosts. This keeps things simple, although it's always been a bit awkward in some situations (if I change my mind about my favourite font, I have to edit every saved session in turn). But it's absolutely intolerable when it comes to host key certificates, because the
whole point
of those is to configure your CA just once, and then never have to worry again about connecting to any host in the domain it covers, even one you've never connected to before.
If you had to configure each saved session separately to indicate which CA it should use, it would be hopeless – each new host you connected to would need configuring by hand. And it would be even worse if each saved session contained a list of (CA key, wildcard) pairs – that would handle new hosts all right (you'd have your full list of CAs in Default Settings), but for any saved session describing just one host, having a list of CAs that didn't apply to that host wouldn't even make sense!
So, for the first time, I've had to introduce a system of
global
PuTTY configuration, that applies regardless of your saved session. And the CA configuration lives there.
This also means there needs to be a separate dialog box containing that configuration, to keep it clear to the user what's global and what's per-session. So
that
needed a pile of refactoring of the UI code, because our general system for cross-platform dialog box layout has only ever had to apply to one dialog box before (the main configuration dialog), and was tied closely to it. Now the general mechanism had to be separated cleanly from its existing caller, so that another caller (the new CA configuration dialog) could reuse it.
Another big refactoring involved changing the way Pageant stores its private keys. But that was also one of the tricky design questions, so I'll come to it later.
Tricky design question: host CA configuration
One way to spot the hardest parts of the job is to look for whatever got done
last
. If you look at PuTTY's git history over this year, you can see that
some
kind of initial support for certificates was working within two weeks of me starting work – but it was another month before I settled on the final system for configuring what CAs are trusted to verify what host keys. That's because it took me that long to turn it all over in my head and come to a decision.
What made that hard? The user interface, and the data storage format.
The most obvious host CA configuration would be something like: your organisation, let's say ‘
example.com
’, publishes a CA key that they'll use to sign host keys for all their SSH servers. So you enter that CA key into PuTTY, and say that you trust it to sign the host key of any machine in the domain ‘
example.com
’. Perhaps via a wildcard, so you write ‘
*.example.com
’, and any hostname matching that pattern is accepted.
(You shouldn't configure a client to trust any CA for
all
host keys regardless of domain – that gives the issuer's sysadmins the ability to quietly intercept some kinds of SSH connections to machines outside the organisation.)
But it's easy to think of lots of exceptions to that policy. Like, perhaps there's some ultra-secure subdomain, say ‘
top-secret.example.com
’, which even the primary sysadmins aren't trusted to handle. So you need to make sure the main CA is
not
trusted to sign host keys for that subdomain. Or perhaps the CA is only supposed to sign host keys for the primary SSH server on a given machine, on the default port number (22), but SSH servers on other ports are their own problem and might make different arrangements.
So you need to be able to enter compound rules, like ‘hostnames in this domain, but only with port 22’, or ‘hostnames in this domain, but here's an exception’. How far do you take that? Do you allow exceptions to the exceptions, or exceptions to the exceptions to the exceptions?
There are two aspects to this kind of decision. One of them is ease of use: however much expressive power you introduce at the high end, to permit really complicated cases, you don't want to make the
easy
cases complicated. Alan Kay famously said:
make simple things simple, make difficult things possible
. The missing word in the middle is
and
, not
or
– you can't afford to neglect the first half in order to satisfy the second.
The other aspect is futureproofing. Our CA configuration is entered through a dialog box, and saved as a set of key-value pairs into either the Registry (on Windows) or a similarly structured collection of files in
~/.putty
(on Unix). If we commit to a data storage format with limited power, then adding more flexibility later is painful.
For example, one obvious design option would be:
just do it the same way OpenSSH did it.
It's their certificate system, after all. And at the time of writing this, OpenSSH only permits one layer of exceptions in their
known_hosts
configuration syntax: you can configure a CA to be valid for
these
domains, except that it's not valid for
those
domains, but you can't write an exception to the exception.
But it's easy for OpenSSH to do that, because their configuration format is textual. If they should decide later that three-layer exceptions are needed, they can always extend the syntax. In a storage system of key-value pairs, it might be a lot more difficult for
us
to change that decision later – so it's more important to think of something futureproof up front.
So I thought it would be better to permit arbitrary nesting of exceptions to begin with, and not have to worry about it later. But now the question of
user interface
comes in: regardless of the storage format, you want to present the information in the configuration GUI in a way that's not confusing. How?
One option is to have a list of ‘accept’ and ‘reject’ rules that are processed in order, and the first match wins. So if you wanted a system of the form ‘accept X, but reject its subdomain Y, but accept the sub-subdomain Z’, you'd list the rules in the order: accept Z, reject Y, accept X. But this has two problems. Firstly, dragging entries up and down a list box is an implementation pain in any GUI, and more so if you have to do it for both Windows and multiple versions of GTK. But more importantly, you might very easily forget
which way round
the order goes – in this very paragraph, I listed my set of three example rules both ways round, and both seemed natural even to me, in different ways. And that's not a trivial concern: in this system, if the user absentmindedly listed those three example rules backwards, they'd
silently introduce a security hole
, accepting hostnames in the intermediate subdomain Y that they meant to reject!
Another approach is to
implicitly
order rules by how specific they are. This design is used by applications such as Linux routing tables (matching IP addresses rather than domain names). If you have rules matching ‘
example.com
’, ‘
subdomain.example.com
’ and ‘
innermost.subdomain.example.com
’, then you could make the innermost rule match with highest priority
because
it describes a subset of the other rules, no matter what order the rules appear in. This is a nice system because it lets the user list rules in whatever order they think is clearest – but it all falls apart as soon as the rules
aren't
nicely nested. Which one wins out of ‘reject ports other than 22’ and ‘accept this particular subdomain’? Which wins out of ‘
*.domain
’ and ‘
hostname.*
’? You just can't always order your rules by the subset relation – sometimes neither of two rules is a subset of the other.
In the end, I decided the least bad approach was to let the user write an actual Boolean expression, so that your various ‘accept this’ and ‘don't accept that’ sub-rules can be connected
explicitly
to show how they relate to each other, with
&&
and
||
and parentheses.
But to keep the simple things simple, I made the innermost components of the Boolean expression as free of syntax as possible. The natural thing, once you're thinking along these lines, would be to use an actual programming language, or something very like one, to write expressions along the lines of
wildcard(hostname, "*.example.com") && port == 22
But that seemed like way too much verbiage for the common case. If the user wants to just match everything in one domain, they shouldn't have to go and look up the name of the matching function, or the string literal syntax. You want to just write ‘
*.example.com
’ in the box and be done with it. So I ended up designing a custom expression syntax that lets you use hostname wildcards on their own. So that example would
actually
be written
*.example.com && port:22
And I think
that
makes simple things simple, makes difficult things possible, and (because I've left extension space in the syntax) it's also futureproof. Phew!
Tricky design question: user certificate configuration
Certificates work both ways round, in SSH. The host key a server uses to prove its identity to you can be signed by a CA, and so can the user key you use to prove
your
identity to the server.
The second half of this had a design challenge too: what's the best way to provide a certificate to go with your user authentication key?
After I finished up the initial stage of implementation work, there was already one way to do it, as a natural side effect of work I'd already done. Every public-key algorithm supported by PuTTY is automatically supported by the
.ppk
file format (‘PuTTY Private Key’), which stores a matching pair of the public and private keys together. So, simply because I added the certificate key types to the same list as all the existing ones, it became possible for PuTTY to offer a certified key to a server, if you gave it a PPK file citing the certified algorithm name, and including the certificate in its public key field. And the same was automatically true for Pageant: you could load that PPK into your agent, in the same way.
But at the time, PuTTYgen had no ability to
create
a PPK file of that form. I could do it for test purposes by faffing about with PuTTY's diagnostic and test tools, but there was no nice user interface for the operation yet.
It wasn't very clear to me whether this was a way that users would
want
to do things, either. In PuTTY's private key format, the passphrase-based encryption only applies to the private key, but most of the rest of the file is covered by the authentication code derived from the same passphrase – including the public key. So in order to make a
valid
PPK by replacing the public key in an existing one, you'd have to provide the passphrase, so that a new authentication code could be generated for the modified key file. Otherwise PuTTY's (or Pageant's) tamperproofing would reject the key at decryption time.
OpenSSH doesn't do things that way. Their private key format
never
includes a certificate. Instead, you simply put the certificate file alongside the private key file, and the client will load both of them together. So my current way of doing things was going to involve running PuTTYgen and entering your passphrase, where OpenSSH's approach would not. It's an extra awkward step for PuTTY users.
So, what to do instead? Or rather: what to do
as well?
I kept the ‘modify the PPK’ approach (and gave it a user-facing UI), because it worked already, and seemed likely to be useful to
somebody
. But I expected people would want another option.
Just like in the previous section, there's an obvious design choice:
just do it the same way OpenSSH did it.
If I'm not going to do that, I should have a reason why not!
In this case, I did have a reason: OpenSSH's approach doesn't match existing PuTTY policy. For OpenSSH, it was very natural to load the certificate from alongside the private key file, because for decades, OpenSSH has already been loading the ordinary
public
key file from alongside the private key in the same way. Their whole usage model is already expecting you to store files alongside each other with related names, and this is just another case of the same thing, so it fits well.
But PuTTY has never used that approach before. We always had the unencrypted public key
incorporated
into our private key format (unlike OpenSSH's original PEM private key format, which was encrypted from beginning to end). So you always configured PuTTY by giving it
just one
file name, and it never had to look alongside the file you specified to find a related one. And I didn't want to start now.
Additionally, I wasn't happy with the flexibility of this approach. One of the options that a CA can add to a user certificate is a forced command: if you authenticate with
this
certificate then the server will only permit you to run
that
command, and not get a general shell. It struck me that a CA making use of this ability might very well issue more than one certificate to the same user, each forcing a different one of the (say) five operations that user was allowed to invoke. In that situation, you'd find it inconvenient to have your certificate loaded from a fixed location alongside the private key – you'd want to specify
which
certificate, in each connection.
So I did it a different way. If you want to use a certificate which hasn't been baked into your PPK file by PuTTYgen, you have to
explicitly
tell PuTTY where to find the certificate, using a separate GUI configuration box, or a separate command-line option. That way, you can keep multiple certificates for the same private key, and easily configure this or that session to use a particular one.
Another advantage of this system is that you can keep just the
base
private key in Pageant, if you prefer, and configure the use of certificates entirely in PuTTY. The private key, and the signature format, are the same for the base key and for any certified copy of the key. So Pageant delivers the same signature regardless, and PuTTY can choose to send any certificate to the server alongside it.
So now we've got
lots
of different ways to specify a user certificate:
bake it into your PPK and load that PPK into Pageant
bake it into your PPK and use that PPK directly with PuTTY
point PuTTY at your bare certificate file and have it use a signature from the matching private key in Pageant
point PuTTY at your bare certificate file
and
a PPK of your base private key
There didn't seem to be any reason to choose just one of these. They're not mutually exclusive, and any of them might be useful. So the released PuTTY supports them all!
Tricky design question: Pageant deferred decryption
PuTTY's SSH agent, Pageant, has a feature that OpenSSH's does not. In recent versions, you can load a key into Pageant
without
decrypting it, and Pageant will store it still encrypted until you first try to authenticate with the key. Then it will pop up a dialog box asking for the passphrase. Once you enter the passphrase, the key is decrypted, and stays that way.
This is convenient because it lets you start Pageant automatically at login time, and not have to enter any annoying SSH passphrases right at the start of your session. In fact, if your session doesn't involve any SSH at all (perhaps you logged in to do something totally different today), you never have to type a passphrase at all. But try to make an SSH connection, and
then
you enter your passphrase – and after that, you can make as many more SSH connections as you need in the same login session.
Also, there's an option to re-encrypt all the keys in Pageant, or just a particular one. You might use that if you're leaving a logged-in session until the next day, for example, so that if someone gains access to your session in the middle of the night, they don't get
all
your crown jewels.
This deferred decryption feature has an interesting interaction with certificates. What if Pageant is storing more than one key file which are related to each other? Say, both the uncertified and certified versions of the same key? Or two certificates on the same key signed by different CAs, or with different options?
The most obvious design choice, and certainly the easiest, would be:
so what? Just ignore the issue.
Treat the two keys as completely separate, so that decrypting one, or re-encrypting it, has no effect on the status of the other.
The problem with that is that it's security theatre. If two keys differ only in the certificate, then they share the same private key, and the signatures they generate are identical. (That's why the feature I mention in the previous section makes sense: PuTTY can request a signature from the
base
key in Pageant, and accompany it with a certified version of the public key that Pageant never knew about, and nothing goes wrong.)
So, suppose Pageant is holding two related keys A and B, differing only in certificates; and suppose you re-encrypt A, to make sure someone gaining access to your SSH agent can't use it. If B is still unencrypted, you haven't helped at all – an attacker could list all the keys, spot that B had the same base public key as A, and request a signature from B instead of from A. So it's
pointless
to encrypt only one of a set of related keys.
Worse, you might do it
by accident
. If you'd had key A for ages, and you were accustomed to re-encrypting it at the end of the working day (perhaps even via some shell script that automated the operation), and now suddenly you're loading the certified version B into Pageant as well, then your existing habit is no longer delivering the security benefit you were expecting. This isn't just confusing: it's giving users an opportunity to make security mistakes.
So it needed a fix. But to make the fix, I had to completely refactor how Pageant stores its keys.
Previously, Pageant had just one data structure, indexed by the complete public key, and containing both the public and private keys. That's where this problem came from: your two related keys A and B would occupy completely separate entries in that structure, each with its own copy of the private key, which could be decrypted or re-encrypted independently, leading to the problem I've just described.
Now it has two separate data structures, one for the public keys and one for the private keys. The two related keys A and B each have their own entry in the
public
key list – but they each refer to the same entry in the
private
key list. If you delete one of the two public keys, the private key is kept, because the other one still needs it. The private key is only wiped from Pageant's memory when the last of its corresponding public keys is deleted.
And
private
keys, not public ones, are the unit of decryption and re-encryption. So now, when you decrypt the first one of your related keys A and B, both become available without any further use of the passphrase. And at the end of the day, when you precautionary re-encrypt key A, key B becomes encrypted as well. Problem solved!
... Well, nearly. There's one other subtlety, relating to decryption prompts.
Suppose your related keys A and B are both loaded into Pageant in the form of encrypted PPK files. Suppose they have different comment strings (which is one advantage of putting a certificate in your PPK – you can give it a comment to remind you which file it is). And suppose they're also encrypted with different passphrases. You load both into Pageant, and later on, try to make a connection using one of them. Which key comment does Pageant print in the decryption prompt?
It
seems
obvious. If your SSH connection is trying to generate a signature from key B (say), why would Pageant
not
print the comment from key B in the decryption prompt? This is also the most natural thing to write in the code, because each public-key record has its own comment field, and the code is holding a particular public-key record in its hand at the moment it generates the prompt. Why would it
not
use the comment field that's right there to hand?
Answer: because of the data-structure organisation I've just described, in which Pageant only keeps
one
copy of the encrypted key file. You loaded in the encrypted PPKs for both keys A and B, but Pageant only kept one of them, because they're as good as each other. So it's going to need you to tell it the passphrase that goes with the key file it actually kept. That's the only one that will allow it to do the decryption.
But in that case, the comment it has to print in the decryption prompt must be the one that goes with
that key file
– no matter which version of the key is the one you requested a signature for!
So in just this one case, Pageant has to follow the link from the public key in the user's request, to the private key record it shares with all the related keys, and use the comment field from
that
. Otherwise, the confused user may never manage to type the right passphrase.
Most embarrassing bug: repeat key exchange
Writing an article like this
after
the work was done, it's tempting to present an idealised account of the design and development process, in which I made all the right decisions for wise reasons, and never put a foot wrong during implementation.
Of course, nothing could be further from the truth. So perhaps I should include at least one story of an embarrassing mistake.
After I finished the initial draft implementation, a couple of weeks after starting the project, I decided it was good enough to be tested in live use (even if the configuration was still clunky, a few outlying features were missing, and lots of polishing still had to be done). So I sent it off to my initial testers, and asked them to tell me what was wrong with it.
One of their first responses was: an SSH session using a certified host key crashes after being connected for an hour or so.
As soon as they said that, it was obvious to me what had gone wrong. The time period of an hour is enough of a clue by itself, because that's the default time until PuTTY performs a repeat key exchange, to refresh the session encryption keys. So obviously the rekey was going wrong in some way.
As it turned out, it was
always
going to go wrong: there was just no way that a rekey would work at all, if a certified host key was in use. How on earth didn't I spot it?
Answer: because, of course, when you're trying to develop
fast
, you don't leave test sessions lying around for an hour! You start one, see if it worked, fix the bug, try again. Or it
does
work, in which case you move on to some other part of the job. In two weeks I never even thought to test rekeying.
That was pretty embarrassing, because it
should
have been obvious. I've been doing SSH for twenty years, and I
know
that rekeying presents its own set of difficulties, different from initial key exchange. Even if I couldn't have anticipated
exactly
what would go wrong, it should have been second nature to me to
test rekeying at least once before declaring it done
, just in case. But did I? I did not.
I have a personal adage I like to call the ‘Law of the Easy Bit’: if there's an easy bit and a hard bit, you'll concentrate on the hard bit and quite likely get it right, and then embarrassingly mess up the easy bit. This was a perfect example of that!
It's fixed in the actual release, of course. But it made me feel very silly at the time.
Conclusion
For all the reasons above (and more), this was a very complicated feature to add to PuTTY. That means a lot of chances to make mistakes and introduce bugs.
So, for the first time ever (though we've wondered about this before), when we set up pre-release builds of the 0.78 release on our website, we sent out an announcement through the same mailing list we use to announce the releases themselves. We hoped that would get more users to try out the pre-releases, and report bugs
before
the release was finalised, to avoid us finding them out two days
afterwards
.
It more or less worked. I'm pretty sure we got a lot of useful fixes in during the long pre-release stabilisation period. (Even if a few more than I'd have liked came in at the very last minute!) And at the time of writing this, 0.78 has been out for several weeks, and nobody has yet reported any large certificates bug.
But, of course, now I've said
that
in a public article, I'm sure that it's only a matter of time!
