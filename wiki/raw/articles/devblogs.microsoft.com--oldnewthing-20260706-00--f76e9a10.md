---
title: "I opened a file with FILE_FLAG_DELETE_ON_CLOSE, but now I changed my mind"
url: "https://devblogs.microsoft.com/oldnewthing/20260706-00/?p=112506"
fetched_at: 2026-07-07T07:01:42.066807+00:00
source: "devblogs.microsoft.com/oldnewthing"
tags: [blog, raw]
---

# I opened a file with FILE_FLAG_DELETE_ON_CLOSE, but now I changed my mind

Source: https://devblogs.microsoft.com/oldnewthing/20260706-00/?p=112506

The
CreateFile
function has a flag called
FILE_
FLAG_
DELETE_
ON_
CLOSE
, which means that the file will be deleted when the last handle to the file is closed. But what if you pass that flag and then change your mind? Is there a way to call take-backs?
No, there are no take-backs. The
FILE_
FLAG_
DELETE_
ON_
CLOSE
flag is permanent.
So what do you do if you want to make a file deleted when the last handle is closed, but only based on some condition determined later?
What you can do is open the file normally, and then once you realize that you want to delete it on last close, you can turn the “delete on close” flag on.
BOOL MarkFileAsDeleteOnClose(HANDLE file)
{
    FILE_DISPOSITION_INFO info{};
    info.DeleteFile = TRUE;
    return SetFileInformationByHandle(hfile,
        FileDispositionInfo, &info, sizeof(info));
Unlike
FILE_
FLAG_
DELETE_
ON_
CLOSE
, you can take back the DeleteFile disposition.
BOOL MarkFileAsNoLongerDeleteOnClose(HANDLE file)
{
    FILE_DISPOSITION_INFO info{};
    info.DeleteFile = FALSE;
    return SetFileInformationByHandle(hfile,
        FileDispositionInfo, &info, sizeof(info));
