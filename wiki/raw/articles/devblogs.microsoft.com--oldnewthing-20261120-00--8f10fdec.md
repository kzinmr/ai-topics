---
title: "Another failed attempt to get the icon for the icon for the .. parent folder"
url: "https://devblogs.microsoft.com/oldnewthing/20261120-00/?p=112883/"
fetched_at: 2026-11-21T10:01:11.293403+00:00
source: "devblogs.microsoft.com/oldnewthing"
tags: [blog, raw]
---

# Another failed attempt to get the icon for the icon for the .. parent folder

Source: https://devblogs.microsoft.com/oldnewthing/20261120-00/?p=112883/

Last time, we looked at
why asking
SHGet­File­Info
for the icon of
..
(the parent folder) produces inconsistent results
. One of the things the customer tried was concatenating the
..
to the current directory:
SHGetFileInfo(L"C:\\dir\\..", 0, &info, sizeof(info),
    SHGFI_ICON | SHGFI_SMALLICON | SHGFI_SYSICONINDEX);
This in fact made it worse: The function failed!
What’s going on?
As I noted last time, if the thing you pass in looks like a relative path, it will be resolved against the current directory. But in this case, the string we passed doesn’t look like a relative path, so no such resolution occurs. The string
C:\dir\..
is then sent through the namespace parser.
The shell namespace is structured as a tree of “folders”, and each folder knows how to parse its immediate children (some of which which might be folders). Parsing starts at the root folder (the Desktop), which parses enough to identify what the immediate child item is, and if that child item is a folder, it passes the unparsed portion of the string to that child folder, and the process continues until the entire string is parsed.
In the case of
C:\dir\..
, the first component is
C:\
, which is recognized as a drive letter. The drive letter is then given what’s left:
dir\..
, and it recognizes that
dir\
is a subdirectory. The folder
dir
then tries to parse
..
, and it says “I don’t have a file or subdirectory named
..
.” The parse fails.
The shell namespace doesn’t have the concept of “something that looks like a child but really means to un-parse the last item.” If you want to “move up” the namespace, you do it by deleting the last component from the item ID list, not by appending a “move up” item.
Bonus chatter
: Sure, but couldn’t the parser have simplified the string
C:\dir\..
to
C:\
before parsing?
While it’s true that backslashes are used to separate file path components, there is no requirement that they be used to separate shell namespace components, nor are shell namespace folders prohibited from having
..
be the name of a valid child item. Each shell namespace folder can define its own syntax for sub-items, and while many of them carry forward the backslash convention, this is not a requirement. For example, the Internet Folder parses URIs, and in URIs, a backslash is just another boring character with no special meaning.
If you want a function to resolve relative paths against the current directory while also compressing out
.
and
..
in paths, you can use
Get­Full­Path­Name
. If all you care about is compressing out
.
and
..
, you can use
Path­Alloc­Combine
or one of its moral equivalents.
