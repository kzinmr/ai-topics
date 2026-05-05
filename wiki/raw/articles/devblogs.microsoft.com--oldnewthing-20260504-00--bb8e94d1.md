---
title: "How do I inform Windows that I'm writing a binary file?"
url: "https://devblogs.microsoft.com/oldnewthing/20260504-00/?p=112296"
fetched_at: 2026-05-05T07:00:57.390178+00:00
source: "devblogs.microsoft.com/oldnewthing"
tags: [blog, raw]
---

# How do I inform Windows that I'm writing a binary file?

Source: https://devblogs.microsoft.com/oldnewthing/20260504-00/?p=112296

A customer wanted to know how to inform Windows that they were opening a file in text mode, as opposed to binary mode. That way, Windows can perform text conversions as necessary, like adding carriage returns before linefeeds, or converting ASCII to Unicode.
Windows doesn’t know whether your file is binary or text. As far as Windows is concerned, it’s just a bunch of bytes, and it’s up to you to interpret it. So in a sense, all files are binary files. If you want to insert carriage returns before linefeeds, you will have to do it yourself.
Now, it is often the case that you are using a higher level library, like the C runtime, in which case you can ask the library to do it for you, such as opening the file in
"w"
mode to indicate that the runtime should treat the file as a text file, or in
"wb"
to open as a binary file. But this work happens in the runtime library, not in Windows itself. The runtime library performs the necessary transformations and passes binary data to Windows. There are no further transformations once the data hits
Write­File
.
“But wait, there’s an old MS-DOS ioctl
AH=4401h (Set device information)
where you pass flags in DX, and
bit 5 is the raw (binary) mode bit
. So what’s the Windows version of this ioctl?”
If you look more closely, that MS-DOS ioctl applies only to character devices.
If you try to use it on a disk file, you get
ERROR_
INVALID_
FUNCTION
.
ioctl_check_permissions:
        CMP     AL,2
        JAE     ioctl_control_string
        CMP     AL,0
        MOV     AL,BYTE PTR ES:[DI+sf_fcb+fcb_devid]
        JZ      ioctl_read              ; read the byte
        OR      DH,DH
        JZ      ioctl_check_device      ; can I set with this data?
        error   error_invalid_data      ; no DH <> 0

ioctl_check_device:
        TEST    AL,devid_ISDEV          ; can I set this handle?
JZ      ioctl_bad_fun           ; no, it is a file.
...

ioctl_bad_fun:
        error   error_invalid_function
This IOCTL can be used to tell the console things like whether to perform line buffering on input. The Win32 equivalent is
Set­Console­Mode
, roughly corresponding to the Unix
stty
.
If you want to perform content transformations on files, you’ll have to do it yourself, or ask someone else (like the runtime library) to do it for you.
