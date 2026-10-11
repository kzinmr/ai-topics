# Unsloth Studio — Sandboxing in Unsloth

- Source: https://unsloth.ai/docs/new/studio/sandboxing-in-unsloth
- Retrieved: 2026-10-11
- Discovered via: X reply by @danielhanchen (Daniel Han, Unsloth co-founder), 2026-10-10:
  "It's auto enabled by default ... as more details!"

## Summary

Unsloth Studio (local app for running/training models) added OS-level sandboxing: all tool
calls are isolated to certain folders without doing OS-level harm. Two modes:

- **Low sandbox**: software-only — string/AST/regex checks on every tool call (blocks
  `rm -rf`, token exfiltration, etc.). ~1-2ms extra latency per call.
- **High sandbox**: true OS-level sandboxing on all platforms, auto-enabled by default where
  the OS primitive is available.

## OS sandbox primitives & latency

| OS | Sandbox software | Latency | Low mode | High mode |
|----|------------------|---------|----------|-----------|
| Windows | MXC (Windows official) | 164ms | 8ms | 164ms |
| Linux | Bubblewrap / Bwrap | 50ms | 3ms | 50ms |
| macOS | Seatbelt (built-in) | 110ms | 10ms | 110ms |

Enablement: Windows MXC pre-installed on Win 11 24H2+; Linux bwrap can be installed by
Unsloth when you select "High"; macOS Seatbelt pre-installed → auto-enabled.

## Software sandboxing blocked operations

- Deleting/disk tools: rm, dd, mkfs, fdisk, mount, umount
- Permissions/privilege: chmod, chown, sudo, su, doas, pkexec, passwd
- Network: curl, wget, nc/ncat/netcat, socat, ssh, scp, sftp, rsync
- Processes/power: kill, killall, pkill, shutdown, reboot, halt, poweroff
- Unseen script execution: eval, source
- Windows only: rmdir, takeown, icacls, runas, powershell, pwsh
- Python (AST read before run): os.system / subprocess with non-literal commands
- Network calls: requests, urllib, raw sockets; sensitive reads (e.g. /etc/passwd)
- Signal/timeout tampering

Applied to every call in both modes: secret env vars stripped, Studio credential files
refused, limits on processes / file size (100 MB) / memory (8 GB) / CPU time (600s) so a fork
bomb hits the process limit, plus per-call timeout.

"Full Access" button disables all sandboxing (0 constraints).

Windows MXC partnership with the Windows team acknowledged; MXC launch blog post linked.
