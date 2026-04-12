# exe.dev Email Receiving - Complete Documentation Summary

## Overview
exe.dev VMs can receive emails at wildcard addresses: `*@<vmname>.exe.xyz`. Any address with any local part (before the @) will be delivered to the VM.

## How to Enable/Disable

**Enable:**
```bash
ssh exe.dev share receive-email <vmname> on
```

**Disable:**
```bash
ssh exe.dev share receive-email <vmname> off
```
Disabling does NOT delete existing emails.

## Email Addresses
- Format: `<anything>@<vmname>.exe.xyz`
- Wildcard: ANY local part works (e.g., `support@myvm.exe.xyz`, `alerts@myvm.exe.xyz`, `foo.bar.baz@myvm.exe.xyz`)
- Only `*.exe.xyz` domain — no custom domains yet

## How Incoming Emails Are Processed
- Emails are delivered as files in **Maildir format** to `~/Maildir/new/` on the VM
- Each email is a separate file in that directory
- NO webhooks, NO scripts auto-triggered — it's purely file-based delivery
- A `Delivered-To:` header is injected as the first line of each email, containing the envelope recipient address
- **Important**: Use `Delivered-To:` header (NOT `To:` or `CC:`) to determine what address the email was sent to

## Watching for New Mail
Two approaches: polling or inotify. Recommended inotify example:

```bash
inotifywait -m ~/Maildir/new -e create -e moved_to |
  while read dir action file; do
    FILE="$dir/$file"
    # process email in $FILE
    mv "$FILE" ~/Maildir/cur/
  done
```

## Critical Rules & Limitations
1. **Must process promptly**: Move emails out of `~/Maildir/new/` quickly
2. **1000 file limit**: If >1000 files accumulate in `~/Maildir/new/`, email receiving is AUTO-DISABLED. Clear the backlog and re-enable to fix.
3. **1MB max message size**
4. **No safety filtering**: No spam, virus, phishing, or safety checks — raw bits are delivered
5. **Strict authentication**: Mail that fails authentication may be rejected
6. **No custom domains**: Only `*.exe.xyz`

## Related: Sending Email
VMs can also send emails (outbound) to the VM owner only, via:
```bash
curl -X POST http://169.254.169.254/gateway/email/send \
  -H "Content-Type: application/json" \
  -d '{"to": "owner@example.com", "subject": "Subject", "body": "Body text"}'
```
- `to` must be the VM owner's email address
- Rate-limited with token bucket
