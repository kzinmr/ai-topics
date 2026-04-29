---
title: "Scheduling Do-Not-Disturb in GNOME"
url: "https://jyn.dev/do-not-disturb-in-gnome/"
fetched_at: 2026-04-29T07:02:12.061100+00:00
source: "jyn.dev"
tags: [blog, raw]
---

# Scheduling Do-Not-Disturb in GNOME

Source: https://jyn.dev/do-not-disturb-in-gnome/

Do Not Disturb
GNOME has a little button that lets you turn on Do-Not-Disturb for notifications:
Unfortunately, it has
no way of scheduling DnD
.
Good news, though! It does support turning on DnD through the CLI:
gsettings set org.gnome.desktop.notifications show-banners false
. I put that in a script named
toggle-dnd
in my dotfiles:
$
cat bin/toggle-dnd
case
$
{
1
:-
}
in
true
)
new
=
false
;;
false
)
new
=
true
;;
*
)
if
[
"
$
(
gsettings
get org.gnome.desktop.notifications show-banners
)
"
=
true
]
then
new
=
false
else
new
=
true
fi
;;
esac
gsettings
set org.gnome.desktop.notifications show-banners
$
new
scheduling
I tried putting that in cron, had a sneaking suspicion it wouldn't work, set it to run every minute, and saw this very unhelpful line of logging:
$
journalctl
--
unit
cron
--
since
'
5m ago
'
Feb 22 12:00:01 pop-os CRON[1623131]: (CRON) info (No MTA installed, discarding output)
Ok, fine. Let's pipe the output to the system log, since clearly cron can't handle that itself.
* * * * * bash -lc 'org.gnome.desktop.notifications show-banners false 2>&1 | logger -t toggle-dnd'
That at least shows more useful output.
$
journalctl
-
t
toggle-dnd
Feb 22 05:59:01 pop-os toggle-dnd[1376772]: /bin/sh: 1: toggle-dnd: not found
Oh right. Cron is running things with a default PATH. Technically there are ways to configure this , but the simple solution is just to run a bash login shell which sources all the directories i would normally have in a shell. at this point, however, it is getting somewhat annoying to test via cron, so let's replicate cron's environment:
$
env
-
i
HOME=
"
$
HOME
"
TERM=
"
$
TERM
"
PS1=
'
$
'
HISTSIZE=-1 HISTFILE= bash
--
norc
--
noprofile
$
echo
$
PATH
/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin
$
bash
-
l
$
echo
$
PATH
/home/jyn/Documents/node-v20.12.2-linux-x64/bin:/home/jyn/.local/bin:/home/jyn/src/dotfiles/bin:/home/jyn/.local/lib/cargo/bin:/snap/bin:/usr/games:/home/jyn/perl5/bin:/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:/snap/bin
neat. let's run  make sure our command runs.
before:
after running
toggle-dnd
in our login shell:
... nothing happened.
we can confirm this on the CLI:
$
gsettings
get org.gnome.desktop.notifications show-banners
true
$
gsettings
set org.gnome.desktop.notifications show-banners false
$
gsettings
get org.gnome.desktop.notifications show-banners
true
DBUS
at this point i started to get annoyed and ran
systemctl --user status
in hopes of writing a systemd timer instead. fortunately, i did that inside the bash login shell, which gave me this helpful error message:
$
systemctl
--
user
status
Failed to connect to bus: $DBUS_SESSION_BUS_ADDRESS and $XDG_RUNTIME_DIR not defined (consider using --machine=<user>@.host --user to connect to bus of other user)
It turns out that both
gsettings
and
systemctl
are trying to communicate over DBUS, and DBUS is linked to your "user session", set when you login. Unsetting environment variables disables DBUS .
I found a helpful
stackoverflow post
that helps us reconnect to DBUS :
export
XDG_RUNTIME_DIR
=
"
/run/user/
$
UID
"
export
DBUS_SESSION_BUS_ADDRESS
=
"
unix:path=
$
{
XDG_RUNTIME_DIR
}
/bus
"
Let's write a little abstraction for that, too .
:
"
$
{
XDG_RUNTIME_DIR
:=
"
/run/user/
$
UID
"
}
"
:
"
$
{
DBUS_SESSION_BUS_ADDRESS
:=
"
unix:path=
$
{
XDG_RUNTIME_DIR
}
/bus
"
}
"
export
XDG_RUNTIME_DIR
DBUS_SESSION_BUS_ADDRESS
exec
"
$
@
"
Now, finally, we can put the pieces together:
$
crontab
-
l
0 20 * * * bash -lc 'dbus-run-user toggle-dnd true  2>&1 | logger -t toggle-dnd'
0 8  * * * bash -lc 'dbus-run-user toggle-dnd false 2>&1 | logger -t toggle-dnd'
P.S.
X11
just setting up DBUS doesn't set up our X11 environment again. I didn't happen to need that. but now that we have DBUS, you can retrieve it pretty easily:
$
dbus-run-user
systemctl
--
user
show-environment
|
grep
^DISPLAY
DISPLAY=:1
You can do something similar for
XAUTHORITY
,
TMUX*
, and
XDG_*
environment variables. Note that
systemctl --user
may be using a tmux session or pane that no longer exists; use caution.
why were you doing this in the first place
hahahaha so i had the foolish idea that this would get discord to silence notifications at night.
it does not do that
. i ended up just turning off desktop notification sounds altogether.
