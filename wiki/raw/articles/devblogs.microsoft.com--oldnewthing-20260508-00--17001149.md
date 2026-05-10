---
title: "Developing more confidence when tracking renames via Read­Directory­ChangesW"
url: "https://devblogs.microsoft.com/oldnewthing/20260508-00/?p=112310"
fetched_at: 2026-05-10T07:00:44.237254+00:00
source: "devblogs.microsoft.com/oldnewthing"
tags: [blog, raw]
---

# Developing more confidence when tracking renames via Read­Directory­ChangesW

Source: https://devblogs.microsoft.com/oldnewthing/20260508-00/?p=112310

A customer was using
Read­Directory­ChangesW
to monitor the contents of a directory, and they were concerned about the
FILE_
ACTION_
RENAMED_
OLD_
FILE
and
FILE_
ACTION_
RENAMED_
NEW_
FILE
pair of actions. The documentation doesn’t guarantee that the two always occur consecutively, or even that they always appear in pairs. For peace of mind, the customer was looking for a way to match up each
FILE_
ACTION_
RENAMED_
OLD_
FILE
with a
FILE_
ACTION_
RENAMED_
NEW_
FILE
to make sure they were tracking the rename properly.
Yes, you can do it by switching from
Read­Directory­ChangesW
. to
Read­Directory­Changes­ExW
and asking for
Read­Directory­Notify­Extended­Information
. This produces the
FILE_
NOTIFY_
EXTENDED_
INFORMATION
structure, and that structure includes the
FileId
of the affected file. You can then match that up between the
FILE_
ACTION_
RENAMED_
OLD_
FILE
and
FILE_
ACTION_
RENAMED_
NEW_
FILE
to confirm that they are the two halves of the same rename operation.
