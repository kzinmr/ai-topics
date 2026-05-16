---
title: "The case of the Create­File­Mapping that always reported ERROR_ALREADY_EXISTS"
url: "https://devblogs.microsoft.com/oldnewthing/20260515-00/?p=112327"
fetched_at: 2026-05-16T07:01:10.855787+00:00
source: "devblogs.microsoft.com/oldnewthing"
tags: [blog, raw]
---

# The case of the Create­File­Mapping that always reported ERROR_ALREADY_EXISTS

Source: https://devblogs.microsoft.com/oldnewthing/20260515-00/?p=112327

A customer reported that whenever their program called
Create­File­Mapping
to create a named file mapping, the call succeeded, but the resulting mapping was not the size they wanted. They requested a 1 megabyte mapping, but the mapping they got back was only 4KB, which they noticed because the program crashed once it accessed the 4097th byte. As an additional data point, if they call
Get­Last­Error()
after creating the file mapping, they get
ERROR_
ALREADY_
EXISTS
, suggesting that the file mapping already created. But this happens even the first time their program was run, and it even happens immediately after a reboot so there shouldn’t be any leftover mappings.
HANDLE h = CreateFileMappingW(INVALID_FILE_HANDLE, nullptr, PAGE_READWRITE,
            0, 65536, L"MyFileMapping");
My guess is that they are getting
ERROR_
ALREADY_
EXISTS
beacuse the mapping already exists. (
Quelle surprise !
)
After a fresh reboot, the customer used Process Explorer to search all processes to see if any of them already had a handle to their file mapping, and lo and behold, they found one: It was some companion software for their webcam, and it chose the exact same uncreative file mapping name.
The customer appended a GUID to their file mapping name, thereby removing the possibility of an accidental name collision. (Of course, there is still the possibility of an
intentional
name collision.
Not much you can do to protect yourself against an attacker at the same or higher privilege
.)
Related reading
:
You can name your car, and you can name your kernel objects, but there is a qualitative difference between the two
.
