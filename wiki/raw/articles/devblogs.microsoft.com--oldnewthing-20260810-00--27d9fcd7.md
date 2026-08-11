---
title: "How can I perform a Copy­File&shy in unbuffered mode?"
url: "https://devblogs.microsoft.com/oldnewthing/20260810-00/?p=112600"
fetched_at: 2026-08-11T10:16:32.218009+00:00
source: "devblogs.microsoft.com/oldnewthing"
tags: [blog, raw]
---

# How can I perform a Copy­File&shy in unbuffered mode?

Source: https://devblogs.microsoft.com/oldnewthing/20260810-00/?p=112600

A customer was copying a file with
Copy­File&shy
, but they wanted the file handles to be opened as
FILE_
FLAG_
NO_
BUFFERING
.
We saw some time ago that
you can use the progress callback to
Copy­File­Ex
or
Copy­File2
to flush the output handle
. Maybe we can use the progress callback to open the handle as unbuffered?
Nope, that doesn’t work because the progress callback gives you the already-opened handle. You can’t change its buffering flag after the fact.
But that’s okay, because
Copy­File­Ex
and
Copy­File2
also have a flags parameter, and one of the flags is
COPY_
FILE_
NO_
BUFFERING
, which means that the handle should be opened as
FILE_
FLAG_
NO_
BUFFERING
.
BOOL success = CopyFileEx(
    sourceFilePath, destinationFilePath,
    nullptr, nullptr, nullptr,
    COPY_FILE_NO_BUFFERING);
You can do the same with
Copy­File2
, but the flags are in the options structure.
COPYFILE2_EXTENDED_PARAMETERS parameters{};
parameters.dwSize = sizeof(parameters);
parameters.dwCopyFlags = COPY_FILE_NO_BUFFERING;
HRESULT hr = CopyFile2(sourceFilePath, destinationFilePath, &parameters);
