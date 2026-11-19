---
title: "NGINX2Root: Remote Code Execution vulnerabilities in nginx"
url: "https://lwn.net/Articles/1108362/"
fetched_at: 2026-11-19T10:03:58.014763+00:00
source: "LWN.net"
tags: [blog, raw]
---

# NGINX2Root: Remote Code Execution vulnerabilities in nginx

Source: https://lwn.net/Articles/1108362/

NGINX2Root: Remote Code Execution vulnerabilities in nginx
[Posted November 18, 2026 by jzb]
Xint is
reporting
that
it has discovered a collection of
five
critical vulnerabilities
in the
NGINX
web
server. The worst flaw, it says, would
allow
an unauthenticated attacker to execute commands on an affected nginx server with
HTTP/2 enabled
. The company also reports a local-privilege escalation (LPE)
kernel
vulnerability
, which was introduced in the 4.15 kernel, in the
Stream Control Transmission
Protocol (SCTP)
subsystem. If chained with the NGINX vulnerability,
it would allow an attacker to gain root privileges on the host. A kernel patch for this
is not yet available.
We also obtained a root shell on the host in a setup where nginx was running in
a Docker container. On many Linux distributions, the SCTP module is installed by
default and the kernel loads it automatically the first time a program opens an
SCTP socket. Whether SCTP is reachable on a given host still depends on the
kernel, the available modules, and the container's restrictions. Where it is
reachable, the attacker can take over the host kernel. Since all containers on
the host share that kernel, this gives the attacker control of the host and
every container on it.
Xint recommends updating to
NGINX
1.31.9
, which was just released, and to
block the SCTP module on hosts that do not need it until a kernel fix is
available. See the
mitigations
section of their report for more information.
The LWN site is currently under high scraper load, so comment
    display has been suppressed for anonymous users.
    If you are a
        human, you may read the comments by clicking the button below:
Note
: you can avoid this step in the future by logging
        into your LWN account.
