---
title: "How to Host your Own Email Server"
url: "https://blog.miguelgrinberg.com/post/how-to-host-your-own-email-server"
fetched_at: 2026-05-01T07:01:30.123314+00:00
source: "miguelgrinberg.com"
tags: [blog, raw]
---

# How to Host your Own Email Server

Source: https://blog.miguelgrinberg.com/post/how-to-host-your-own-email-server

I recently started a
new platform
where I sell my books and courses, and in this website I needed to send account related emails to my users for things such as email address verification and password reset requests. The reasonable option that is often suggested is to use a paid email service such as Mailgun or SendGrid. Sending emails on your own is, according to the Internet, too difficult.
Because the prospect of adding yet another dependency on Big Tech is depressing, I decided to go against the general advice and roll my own email server. And sure, it wasn't trivial, but it wasn't all that hard either!
Are you interested in hosting your own email server, like me? In this article I'll tell you how to go from nothing to being able to send emails that are accepted by all the big email players. My main concern is sending, but I will also cover the simple solution that I'm using to receive emails and replies.
This is a longer read than my usual blog posts, and some of the steps involve waiting, so unfortunately you will not be able to set up your email server all in one day. To help you find your place as you follow these instructions over several sessions, I'm including a table of contents that will help you jump directly to each step.
High-level design
Requirements
Preparation
Basic DNS setup
Email forwarding
Postfix
Send a test email
Reverse DNS
DKIM
SPF
DMARC
Have patience
High-level design
Knowing in advance that I was going to attempt something that most people consider to be very hard, I wanted to design the simplest possible solution that allowed my web application to send emails out to people. I did not want to have to worry about other email use cases. At least not initially.
So what is there to simplify when thinking about email? I started from the two major protocols related to email:
SMTP
, the Simple Mail Transfer Protocol: This is the protocol that allows email servers to talk between each other to send and receive messages. The two popular open source SMTP servers are
Sendmail
and
Postfix
.
IMAP
, the Internet Message Access Protocol: A protocol that lets a user access and manage email stored in a remote server. A lot of people use
Dovecot
for IMAP.
Really the only thing you need to send emails is SMTP. IMAP is for accessing emails, not sending them. So from the start I decided to skip IMAP.
But I was able to simplify things even more. The "receiving" side of SMTP was also a bit annoying to have to support, as that involves managing user accounts and mailboxes in my server, and more importantly, it would require me to monitor one or more new email addresses for incoming mail. For many years I have relied on the email forwarding feature included with my domain to have those occasional emails people send to me at a
@miguelgrinberg.com
address redirected to my personal email address, and this works really well for me.
So the simplest email solution I could come up with involved an asymmetric SMTP configuration. I would use my self-hosted SMTP server for sending emails, but for receiving I would continue to use the email forwarding service that I'm currently using. This meant that I could host my email server securely behind a firewall, because it would not need to be in the receive path, and consequently it would not need to accept connections from other servers.
Requirements
Running an email server requires basically two things, and you probably have both already. You need a domain name, and a computer to run the server on. That's pretty much it in terms of things that cost money.
Having a domain is actually required to send emails on your own. You will see later that a lot of the configuration work involves changing settings on the domain and not directly on the server. If you have a domain for your website or business, then you're good to go.
As far as the computer that will run your server, you will need to have it on 24/7.
Using a Raspberry Pi or old PC in your home seems like a decent idea, but I do not recommend it. The main problem with running your email server at home is that most ISPs do not assign you a fixed IP address, and this creates a lot of complications for email servers, since it is difficult to keep your domain DNS entries up to date when your IP address can change at any time. Also, any sender reputation you accumulate when the server is on one IP address could go away when your IP address changes and other servers do not recognize you anymore. I only recommend running your server at home if your ISP gives you a fixed IP address.
The best option to host your email server is to get a cheap Virtual Private Server (VPS) from Hetzner, Digital Ocean, Linode, or similar providers, which all come with a fixed IPv4 address. If you already have a VPS for your website, you may be able to squeeze the SMTP server in it without much trouble.
The cost involved in maintaining the above items is about $6 per month, or free if you already have the domain and the VPS for your website like I do. Once the server is set up, you will be able to send as much email as you like without having any more expenses. Just for reference, consider that Mailgun charges $15/month for their base subscription tier, and SendGrid prices theirs at $19.95/month (prices are at the time I'm writing this in early 2026).
Preparation
Okay, so now that you have your domain and your computer you must check a few things.
You will need to configure the DNS entries for your domain, so make sure that your domain registrar gives you unrestricted access to your DNS. If they don't, you should transfer the domain to another provider that does.
Many email servers out there use a reputation system to decide if they accept or reject email from a given server. Before you begin, it would be useful to confirm that the IP address assigned to your server is not in any email block lists. You can search your IP address in the
Blacklist checker
tool, and if you find that it has been blocked in a previous life, then you should ask your hosting provider for a different one. If you are using a VPS, it is easy enough to delete and regenerate your server until you get one with a clean IP address.
The SMTP protocol works on port 25. Unfortunately most hosting providers block this port on their servers as an attempt to curb email spam. To check if your port 25 is blocked, open a shell on your server and try to make a
telnet
connection to a well known SMTP server. For example, try this command:
telnet mxa.mailgun.org 25
If this hangs, then your port 25 is blocked. If you get connected then you are good. You can exit the telnet connection by pressing
Ctrl+]
and typing
close
followed by Enter. If
telnet
hangs, use Ctrl+C to exit.
What do you do if your port 25 is blocked? In my experience, hosting providers lift the block if you ask and confirm that you are not going to send unsolicited email. Some, like Hetzner, have an automated form to make this request, and the unblocking happens in a couple of minutes (update: Hetzner requires one paid invoice before they allow you to request port 25 access. Digital Ocean
does not accept
requests to unblock this port anymore. Linode
still does
).
The last preparation step I'm going to mention is the hardening of your server, which I'm not going to cover in detail in this article because the exact steps depend on which flavor of Linux you use. Important hardening tasks include setting up a firewall and turning password authentication and root logins off, essentially making it impossible for an attacker to be able to infiltrate your server. I have discussed how to harden a web server in my
Flask Mega-Tutorial series
, if you are interested in learning more about this.
Basic DNS setup
At this point you need to decide what hostname you are going to use for your email server. You can use the root domain name directly (
yourdomain.com
) or you can use a subdomain (
mail.yourdomain.com
).
If you are going to host your email on the same server as your website, then it would be fine to use the root domain for your email server. But if you are using a dedicated machine for your email server and you have another machine for your website, then you should assign a subdomain to your email server, so that you can have the root domain pointed at the server that hosts your website.
To set up your DNS, log on to your domain registrar's administration console and access the DNS section. Add a new DNS entry with the following settings:
In the Host field, enter the subdomain name of your server (
mail
, for example). If you decided to use your root domain name as your email server, then you will typically leave this field empty. Some providers require you to enter
@
as host for root domain entries. If in doubt, look at other entries in your DNS to see how they were created, or ask your domain registrar what the exact format is.
In the Type field, select an
A
record.
In the Value or Data field, type the IP address of your server.
Leave other fields with their default values.
Changes to DNS take a while to propagate, so it may be an hour or two before your change is visible. Use the
DNS check
web-based tool or the
nslookup
or
dig
commands to check the state of your DNS. Here is how to use
nslookup
:
$ nslookup mail.yourdomain.com
...
Name: mail.yourdomain.com
Address: aa.bb.cc.dd
Email forwarding
The next step is to set up your email forwarding, which I recommend you do, even though it isn't technically required to send email. This will basically ensure that you receive emails sent to addresses that belong to your domain.
Go into your domain registrar's dashboard and look for the email forwarding option for your domain. Typically this is offered as a free service with your domain. You'll probably have the option to configure forwarding rules for different addresses, but I do not bother with that, and instead just set up a single catch-all rule that forwards all emails, regardless of the username, to my personal email account. This is what allows me to receive the emails you send me when you click the "Questions?" link at the bottom of all the pages in this blog, for example.
To set up forwarding, your registrar will add some entries to your domain's DNS, among them one or more
MX
and
TXT
records. After you set this up, try sending test emails from a personal email account to random usernames at your domain and confirm that you receive these emails on the redirected account. Remember that any DNS changes need to propagate, so you may have time to go grab a cup of coffee before this starts to work.
Postfix
For the actual SMTP server I decided to use
Postfix
, an open source SMTP server that has been around since 1997.
For convenience, I decided to use a container image of Postfix. I tested a few of them and liked
docker-postfix
the most. One reason I liked it is that it bundles
opendkim
in the image, a tool that is a required part of the email stack.
The container image can be used as a simple container with Docker or similar runtimes, and it can also be used in a Kubernetes deployment. If you are using Docker as your container runtime, you can launch your SMTP server with this command:
docker run --restart always -d --name postfix -e "ALLOWED_SENDER_DOMAINS=yourdomain.com" -e "DKIM_AUTOGENERATE=true" -v ~/.dkim:/etc/opendkim/keys -p 1587:587 boky/postfix
Let's review what are all the arguments that I'm passing to
docker run
:
--restart always
ensures that the container is always running. If the container dies for any reason, Docker will immediately start a new one to replace it. This also ensures that the container starts on its own after a reboot.
-d
starts the container in the background, without blocking your prompt.
--name postfix
gives the container a name. You can use this name to refer to this container in other Docker commands.
-e
defines an environment variable. I'm setting two variables that are needed to properly configure the server. The
ALLOWED_SENDER_DOMAINS
variable must be set to the root domain you will be sending from. Use the root domain even if your email server is configured on a subdomain. The
DKIM_AUTOGENERATE=true
variable tells the container to create DKIM keys for the domain when it starts.
-v ~/.dkim:/etc/opendkim/keys
defines a directory that is shared between the container and the host file system. The path
~/.dkim
in the host will map to
/etc/opendkim/keys
in the container, which is the location where the DKIM key will be stored. More on this later.
-p 127.0.0.1:1587:587
maps port 1587 in the local host to port 587 in the container. Port 587 is where Postfix accepts emails to send. In the host, I'm mapping it to port 1587 to avoid needing root access, which is required to allocate network ports below 1024. The explicit
127.0.0.1
restricts the host port to the internal network, and is the most secure setting when running your website and your email server all on the same machine.
boky/postfix
is the Postfix container image
Run the command, give it a few seconds, and then ensure that everything is running by looking at the logs:
docker logs postfix
Near the bottom you should see a few "success" lines that indicate that all the processes associated with the server are running:
2026-03-02 20:26:24,721 INFO success: cron entered RUNNING state, process has stayed up for > than 0 seconds (startsecs)
2026-03-02 20:26:24,721 INFO success: postfix entered RUNNING state, process has stayed up for > than 0 seconds (startsecs)
2026-03-02 20:26:26,927 INFO success: rsyslog entered RUNNING state, process has stayed up for > than 2 seconds (startsecs)
2026-03-02 20:26:29,932 INFO success: opendkim entered RUNNING state, process has stayed up for > than 5 seconds (startsecs)
Also check the
~/.dkim
directory in the host file system, which should have the public and private keys that will be used to generate and verify DKIM signatures. It is a good idea to create a back up of this directory, just in case.
Before moving on to the next topic, I have to give you a security warning. You saw above that I exposed the email port only on the local host. This only works when the sending application is hosted on the same machine as the email server. If you have the sending application on another machine, then you will need to configure a private network between the two computers, so that they can communicate between them without exposing the email server on the open Internet. Do not, under any circumstance, allow port 587 of the Postfix container to listen on the network interface that is connected to the world, as that would be a big security risk.
Send a test email
If you reached this point, congratulations, your email server is up and running!
Even though there are still some important tasks ahead, you can try sending a test email. The following script written in Python sends a test email.
import smtplib
from email.mime.text import MIMEText

sender = 'you@yourdomain.com'  # your sending address
recipients = 'someone@gmail.com'  # comma separated list of recipients
msg = MIMEText("""Hello,

This is a test email.

I hope it works!
""")

msg['Subject'] = 'Test email'
msg['From'] = sender
msg['To'] = recipients.replace(',', ';')

s = smtplib.SMTP('localhost', 1587)
s.sendmail(sender, recipients.split(','), msg.as_string())
s.quit()
Note the connection to the SMTP server is using
localhost
and port
1587
. This matches the port number that the Docker container maps to in the host.
Copy this script to your email server and save it as
send_email.py
. Change the
sender
variable to an address based on your domain, and change
recipients
to an address you receive email at, like maybe a Google Mail one. If you want to send the test email to multiple addresses, put them all in the
recipients
variable as a single string with the addresses separated by commas. Run the script from the shell in your server as follows:
python send_email.py
You are probably not going to see any output. The script opens a connection to the Postfix process running in the Docker container and puts an email on the send queue, and this should succeed. But it is highly unlikely that you will receive the email on the account(s) indicated by the
recipients
variable. The most likely scenario is that the email will bounce. You can check the logs in the Docker container to see what happened:
docker logs postfix | grep status=
The above command prints the lines in the Postfix log that have the string
status=
. You will likely find more than one line, so you should look for a line that references the recipient address that you used in Python script. At this stage it is totally expected to see
status=bounced
on this line, along with an error message from the recipient's email server. If you somehow got lucky and the email was sent, then you will see
status=sent
. Another possible status that you may see is
status=deferred
.
If the email bounced, then Postfix will try to notify you of this error by sending you an email. This may not happen immediately after you run the Python script, but shortly after you should find a second line with
status=
in it that is addressed to the sender. If you set up email forwarding as I recommended, then this log line should show a
status=sent
, because this email would have been received by the email server that your domain registrar uses for the forwarding service. In this case this email should arrive at the inbox of the account you selected to receive the redirected emails.
The remaining tasks are intended to make your server look legitimate to other servers it talks to when trying to deliver emails to them. This is what is going to prevent the emails from bouncing.
Reverse DNS
Many email servers nowadays check that a reverse DNS entry is set up for the IP address asigned to your email server as a measure to reduce spam.
Your reverse DNS is configured via your hosting provider, not your domain registrar. You will need to find the section in your server's administration console that allows you to edit the reverse DNS record of your server. All you need to do is enter your email server's hostname, including the subdomain if you used one. Your hosting provider will use it to update its DNS records.
Because this is also a DNS change, it needs a bit of time to propagate. You can use the
Reverse IP lookup
tool on your browser or the same
nslookup
or
dig
commands that you used to check your reverse DNS entry. Here is how the output looks for
nslookup
:
$ nslookup aa.bb.cc.dd
dd.cc.bb.aa.in-addr.arpa      name = mail.yourdomain.com.
After you implement reverse DNS, you should have a perfect DNS loop. The DNS on your email server domain should point to the IP address, and the DNS on the IP address should point back to the exact server domain.
DKIM
The
DKIM
policy, short for DomainKeys Identified Mail, uses
public key cryptography
provides email servers with a method to verify the legitimacy of emails.
Here is how DKIM works. The server is configured with a private and public key pair. The private key stays private in the server, and the public key is added to a
TXT
record in your domain's DNS configuration, making it accessible to anyone. For each outgoing email, the server computes a cryptographic signature using the private key, and adds the signature to the email. The receiving server can then get the public key from the sending server's DNS record and use it to verify that the signature is valid, which proves that your server is the true sender.
The Postfix container that you started earlier is already computing and sending DKIM signatures, thanks to it coming integrated with
opendkim
. The key files that the server is using are in the
~/.dkim
host directory, which is shared with the container. The part that is missing to complete the DKIM configuration is storing the public key in a DNS record that other servers can see.
Go back to your domain DNS configuration page and add a new DNS record with the following details:
In the Host field, enter
mail._domainkey
.
In the Type field, select a
TXT
record.
For the Value or Data field, you need to look in the
~/.dkim/
directory for a file with a
.txt
extension. This file has the DKIM public key. The public key file is in the DNS zone file format, which breaks long strings into smaller parts, so you will need to carefully assemble the long string from the sections. See below for an example.
Leave other fields with their default values.
Just in case you have trouble extracting the public key, here is an example of what this file looks like, with the three parts of the key highlighted in red. You will need to join the three parts into a single long string (without the quote delimiters) and paste that in the value field of the DNS entry.
mail._domainkey IN      TXT     ( "
v=DKIM1; h=sha256; k=rsa; s=email;
"
          "
p=MIIBIjANBgkqhkiG9w0BAQEFAAOCAQ8AMIIBCgKCAQEAtbCq6nB5tEeO2gRPbbW8ELF4QPNqR90vxfNSMiWJ3rrC1wATbEq4pC23ZBLLTsOErcv03rZzsWmb/aqdw3ageiN1ByBJk275AJwPDWYU5S1tRFNDig8iTI0IgSzC5VitLC79Ymv79pDAbcfimkSZqsUj1shW8HDt55DYcrI+EuCgq8Pl/S/+CbjPkhIM+N1YJFQDkHQbAf3aYw
"
          "
629uTYeAOBvNE9EsPH1BYu6TCigQheTsl1JSjhnLzOKuCdqtnBT7ChkR/xxdoYVEjS2DsOMY9x1pcXfLbky/Zp502QByxD2DIeSBo2Cu2TU8KAfPFqCQdRvCJEKYulNz1xxqWgtQIDAQAB
" )  ; ----- DKIM key mail for yourdomain.com
It is possible that you have another DKIM key in your DNS records, for the email forwarding service. To be able to coexist, multiple DKIM keys must have different
selectors
(the
mail
name in the
mail._domainkey
host). If you have the bad luck to have a previous DKIM key in your DNS that uses
mail
as selector, then you will need to pick a different selector for Postfix. In that case, you will need to update the selector name in the first line of the
.txt
file, and pass
-e DKIM_SELECTOR=new-selector
as an argument in the
docker run
command.
After giving your DNS changes some time to propagate through the Internet, you can verify the configuration using the
DKIM Record Lookup
tool. For this tool you will need to enter the domain of your server and the the DKIM selector that you used, which as stated above, is
mail
by default.
SPF
The next policy that your server needs to support is
SPF
, which is short for Sender Policy Framework. SPF allows you to announce the list of servers that are authorized to send email using your domain. This helps prevent email spoofing, because it allows the receiving server to discard emails that come from an email server that is not listed as authorized to handle the domain.
As with DKIM, an SPF record must be added in the DNS settings of your domain:
Leave the Host field empty, or type
@
if your registrar requires it for root domain entries.
In the Type field, select a
TXT
record.
For the Value or Data field, enter
v=spf1 ip4:aa.bb.cc.dd -all
, replacing
aa.bb.cc.dd
with the IP address of your email server.
Leave other fields with their default values.
After the version specifier, the SPF record must include a list of allowed sending servers. Here I decided to use the
ip4
specifier to provide the IP address of the only server that is authorized to send my website's emails. The SPF specification supports
other ways
to authorize servers that may be useful in more complex cases. If necessary, multiple sources can be given, separated by spaces.
The last
-all
term is called a "hard fail" clause. This item instructs the receiving server to reject emails that do not come from any of the declared sources. You can replace it with
~all
to configure a "soft fail", which is less strict and can help debug email deliverability issues.
As with DKIM, you will likely have another SPF record, added by your registrar for use with email forwarding. When a domain has multiple SPF records, their contents need to be merged into a single record. I believe most registrars perform this merge automatically, so this should not be a problem. If your registrar does not automatically merge multiple SPF records, there is a
SPF Record Merge
tool that you can use, but I suggest you ask your registrar what is their recommended way to handle multiple SPF records.
Give these changes some time to propagate, and then verify them with the
SPF Record Check
tool.
DMARC
There is one last policy to implement called
DMARC
, which is short for Domain-based Message Authentication, Reporting and Conformance. It is similar to DKIM and SPF in the sense that it too uses a
TXT
DNS record.
DMARC introduces the concept of "alignment", which occurs when the domain given in the
From
line of the email matches the domain that was validated by DKIM and SPF. Alignment can be complete when both DKIM and SPF are aligned, or partial when only one of them is.
The need for DMARC may not be initially clear, but it makes more sense when you consider that neither DKIM nor SPF look at the
From
address of the email. DKIM includes the signing domain in the
DKIM-Signature
header, along with the computed signature. SPF obtains the sender domain from the
Return-Path
header, also called the "envelope" sender. You could have a message that passes DKIM and SPF with flying colors, while it has a spoofed address in the
From
field, which is the address the user will see when they open the email. DMARC addresses this by making sure that the
From
address comes from the same domain that was validated by DKIM and SPF.
Open your server's DNS configuration page one last time, and add one more entry with these details:
In the Host field, enter
_dmarc
.
In the Type field, select a
TXT
record.
For the Value or Data field, enter
v=DMARC1; p=reject; sp=reject; aspf=s; adkim=s;
.
Leave other fields with their default values.
The DMARC record includes a series of
tags
, separated by a semicolon. The tags that I included above are:
v
, to set the DMARC policy version
p
, to set the policy for emails that fail the DMARC test. Values, from the more relaxed to the more strict, can be
none
,
quarantine
or
reject
. Email servers want to see
reject
here, because that shows you are committed to only sending legitimate email. You can lower this to
quarantine
if you are having trouble getting your emails delivered, but assuming DKIM and SPF are correctly configured you shouldn't have to.
sp
to set the policy for sub-domains of the email server. This isn't needed for the setup that I'm describing in this article, but I thought it best to include it in case I need it in the future. Same values as the
p
tag.
aspf
, the SPF alignment mode, which can be
s
for strict or
r
for relaxed. The relaxed mode allows subdomains, while the strict mode requires an exact match. I'm using
s
, but you can change this to
r
in configurations that are more complex than mine.
adkim
, the DKIM alignment mode, also
s
or
r
.
One area in which DMARC is different than DKIM and SPF is that it includes options to produce reports. Postmark offers a free
DMARC weekly report
for your email server that I find useful, because it tells me how many emails I sent during that week and if any failed the DMARC alignment test. It also gives me a list of emails that were sent by unauthorized servers with a spoofed address of mine. If you decide to subscribe to these reports, you will need to provide Postmark with your personal email address and your domain.
After you subscribe, they'll ask you to edit your DMARC policy to include the
rua
field, set to a specific email address they'll assign to you. This address will be used by all the email servers that handle emails that reference your domain to report successes and failures. You can add this field at the end of the policy. My current policy looks like the following:
v=DMARC1; p=reject; sp=reject; aspf=s; adkim=s; rua=mailto:xxxxx@dmarc.postmarkapp.com;
Have patience
This was a long journey, but by now you should have a server that is configured with all the security features modern email requires. However, if you send another test email and check the logs of the Postfix service like you did before, you may find that it bounces again.
Unfortunately many servers use a reputation system to decide if they accept or reject emails. These servers may need a bit of time to start trusting your server, so the best you can do is to continue sending test emails to as many different addresses and different domains you have access to. If your reverse DNS and your policies are correctly configured, then you will see that eventually your emails will start to be accepted. Initially they may be delivered to spam folders, but keep at it and this will improve.
You should continue to monitor the Postfix container logs, because there is always the chance that you made a mistake in your configuration. If a receiving server decides to bounce an email you sent, the log will tell you why, and this can give you the clues you need to troubleshoot the problem.
To conclude, I'm going to mention two end-to-end email delivery tests that I've found useful when setting up my server.
The
Mail Tester
site is very simple to use. When you open this page you'll get a randomly generated email address. All you need to do is send an email to this address, and then this site will run a series of tests on it and give you the results. To send this email you can use the Python script I shared above, editing the recipient to match the address they provide.
The other testing tool is the
EasyDMARC email deliverability test
, a more advanced test that asks you to send an email to a large number of email addresses and checks if they are received. For this test, they ask you to include a randomly generated code in the body of the message, so that they can identify your messages on their end. To use the Python script for this test you will need to make a couple of changes. First, you'll need to paste the long string with the email addresses in the
recipients
variable:
recipients = 'xxx@gmail.com,yyy@gmail.com,zzz@live.com,...'
Next, you will need to add the random code somewhere in the message body. You can leave the text of the message the same, as long as the code appears within the text.
A few minutes after sending these emails, the tool will offer you to request a report by email. Once you get the report, you'll be able to see which services are rejecting your emails, and which are sending your emails to spam. It is unlikely you'll get perfect results, but running this test every few days or weeks will give you an idea of how your email server is improving its reputation. I should note that the few times I did this test I've got a bunch of email bounces that were caused by the addresses themselves being invalid, so be sure to check the logs to determine which errors are actionable and which are not.
Conclusion
I hope with all these tools and some patience you will be able to have a functional email server. I'd love to hear if you had a good or bad experience going through these instructions, so please do write a comment below!
Thank you for visiting my blog! If you enjoyed this article, please consider supporting my work and keeping me caffeinated with a small one-time donation through
Buy me a coffee
. Thanks!
