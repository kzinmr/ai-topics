---
title: "Why do I get inconsistent results when I ask for the icon for the .. parent folder?"
url: "https://devblogs.microsoft.com/oldnewthing/20261119-00/?p=112879/"
fetched_at: 2026-11-21T10:01:11.350126+00:00
source: "devblogs.microsoft.com/oldnewthing"
tags: [blog, raw]
---

# Why do I get inconsistent results when I ask for the icon for the .. parent folder?

Source: https://devblogs.microsoft.com/oldnewthing/20261119-00/?p=112879/

A customer wanted their program to show a file listing with icons, and they also wanted to include an entry for the parent folder, programmatically known as
..
(double period).
Update
: The idea is that they are showing a file listing unrelated to the file system. For example, they are an online photo album browser. They want to show all the photos in the current album, plus an icon that means “Go to the parent folder.”
End update
They obtained icons by calling the
SHGetFileInfo
function, but they got weird, inconsistent results when they asked for the icon of the
..
parent folder.
SHGetFileInfo(L"..", 0, &info, sizeof(info),
    SHGFI_ICON | SHGFI_SMALLICON | SHGFI_SYSICONINDEX);
They found that when they ran the program in a debugger, it gave them the desired folder icon 🗀. But when it ran on the customer’s system, it showed a drive icon 🖴. What’s going on? Why is the icon changing depending on who is running the program?
My psychic debugging powers¹ told me that the developer told their debugger to run the program with the current directory equal to something that is at least two directory levels away from the root. Perhaps they are using Visual Studio and accepted the default configuration that sets the current directory to
$(ProjectDir)
, and their project directory is eomthing like
C:\
Users\
name\
repos\
contoso
. On the other hand, the customer is running the program while the current directory is set to an immediate subdirectory of the drive root, like
C:\
Contoso
.
When you pass
".."
to
SHGetFileInfo
, it is recognized as a relative path and is resolved against the current directory. And then you get the icon for whatever that turns out to be.
Resulting iconfolderdrive
Current directory
C:\repos\contoso
C:\contoso
".."
resolves to
C:\repos
C:\
So what should you do if you want to get a folder icon?
You can pass the
SHGFI_
USE­FILE­ATTRIBUTES
flag, which means, “Just pretend that I gave you a valid path to a thing with the attributes I passed as the second parameter. What icon would you use for it?”
SHGetFileInfo(
L"C:\\a", FILE_ATTRIBUTE_DIRECTORY
, &info, sizeof(info),
SHGFI_USEFILEATTRIBUTES |
SHGFI_ICON | SHGFI_SMALLICON | SHGFI_SYSICONINDEX);
We pass a file path of
C:\a
and say that its attributes are
FILE_
ATTRIBUTE_
DIRECTORY
. The actual path is not important, as long as it is a syntactically valid path.
Next time, we’ll look at a follow-up question related to this problem.
¹ I want to remind you that if you force me to do psychic debugging, then you have
failed
. When I coined the term “psychic debugging”, I used it to describe the case of debugging a problem where the person asking the question omitted crucial information, forcing me to go to the extra effort of obtaining that information through supernatural means. It’s like showing up at the passport office without having the proper forms filled out. The clerk can probably give you the correct form and help you fill it out, but they’re not going to be happy about it because you’re just creating extra work for them due to being ill-prepared.
