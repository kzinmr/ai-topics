---
title: "Soju User Delete Hash"
url: "https://susam.net/soju-user-delete-hash.html"
fetched_at: 2026-04-28T07:01:42.772132+00:00
source: "susam.net"
tags: [blog, raw]
---

# Soju User Delete Hash

Source: https://susam.net/soju-user-delete-hash.html

Soju User Delete Hash
By
Susam Pal
on 14 Feb 2026
In
my last post
, I talked about
  switching from ZNC to Soju as my IRC bouncer.  One thing that caught
  my attention while creating and deleting Soju users was that the
  delete command asks for a confirmation, like so:
$
sudo sojuctl user delete soju
To confirm user deletion, send "user delete soju 4664cd"
$
sudo sojuctl user delete soju 4664cd
deleted user "soju"
That confirmation token for a specific user never changes, no matter
  how many times we create or delete it.  The confirmation token is
  not saved in the Soju database, as can be confirmed here:
$
sudo sqlite3 -table /var/lib/soju/main.db 'SELECT * FROM User'
+----+----------+--------------------------------------------------------------+-------+----------+------+--------------------------+---------+--------------------------+--------------+
| id | username |                           password                           | admin | realname | nick |        created_at        | enabled | downstream_interacted_at | max_networks |
+----+----------+--------------------------------------------------------------+-------+----------+------+--------------------------+---------+--------------------------+--------------+
| 1  | soju     | $2a$10$yRj/oYlR2Zwd8YQxZPuAQuNo2j7FVJWeNdIAHF2MinYkKLmBjtf0y | 0     |          |      | 2026-02-16T13:49:46.119Z | 1       |                          | -1           |
+----+----------+--------------------------------------------------------------+-------+----------+------+--------------------------+---------+--------------------------+--------------+
Surely, then, the confirmation token is derived from the user
  definition?  Yes, indeed it is.  This can be confirmed at the
source
  code here
.  Quoting the most relevant part from the source code:
hashBytes := sha1.Sum([]byte(username))
hash := fmt.Sprintf("%x", hashBytes[0:3])
Indeed if we compute the same hash ourselves, we get the same token:
$
printf soju | sha1sum | head -c6
4664cd
This allows us to automate the two step Soju user deletion process
  in a single command:
sudo sojuctl user delete soju "$(printf soju | sha1sum | head -c6)"
But of course, the implementation of the confirmation token may
  change in future and Soju helpfully outputs the deletion command
  with the confirmation token when we first invoke it without the
  token, so it is perhaps more prudent to just take that output and
  feed it back to Soju, like so:
sudo sojuctl $(sudo sojuctl user delete soju | sed 's/.*"\(.*\)"/\1/')
