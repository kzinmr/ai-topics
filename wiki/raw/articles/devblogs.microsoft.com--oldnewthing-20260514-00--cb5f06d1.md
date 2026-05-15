---
title: "A constant-space linear-time algorithm for deleting all but the 10 most recent files in a directory"
url: "https://devblogs.microsoft.com/oldnewthing/20260514-00/?p=112322"
fetched_at: 2026-05-15T07:01:01.952478+00:00
source: "devblogs.microsoft.com/oldnewthing"
tags: [blog, raw]
---

# A constant-space linear-time algorithm for deleting all but the 10 most recent files in a directory

Source: https://devblogs.microsoft.com/oldnewthing/20260514-00/?p=112322

Say you have a directory full of files, and you want to delete all but the 10 most recent files. Is there a way to tell
Find­First­File
to enumerate the files in date order?
No, there is no way to tell
Find­First­File
to enumerate the files in date order. The files enumerated by
Find­First­File
are produced in whatever order the file system driver wants. For example, FAT typically enumerates them in the order the files appear in the directory listing, which could be in order of creation if the files were added sequentially, or some mishmash order if there were renames or deletions mixed in.
Since you can’t control the order in which the files are enumerated, you’ll have to do the sorting yourself. The naïve solution is to read in all the entries, sort them by last-modified date, and then delete all but the last ten. This is
O
(
n
) space and
O
(
n
log
n
) running time.
But you can do better.
This job calls for a priority queue. A priority queue is a data structure that supports these operations, where
n
is the number of items in the priority queue.
Add sorted:
O
(log
n
)
Find largest:
O
(1)
Remove largest:
O
(log
n
)
The above description is for a max-priority queue. There is also a min-priority queue where the final two operations are “find smallest” and “remove smallest”. The two versions are equivalent because you can just use a reverse-sense comparison to switch from one to the other.
What we can do is enumerate all the files and add them one by one to a min-priority queue sorted by modified date. The priority queue holds the newest items. If the priority queue size exceeds 10, then we delete the file corresponding to the “smallest” (earliest) entry in the priority queue, and the remove that entry from the priority queue.
Since the priority queue size has a fixed cap, all of the operations run in
O
(1) time because the value of
n
is bounded by a predetermined constant. (Of course, the larger the cap, the larger the constant in
O
(1).) The overall algorithm then runs in
O
(
n
) times, where
n
is the number of files in the directory.
Here’s a sketch of a solution. To get a min-priority heap, we have to reverse the sense of the comparison in
dateAscending
.
constexpr int files_to_keep = 10;

auto dateAscending = [](const WIN32_FIND_DATA& a, const WIN32_FIND_DATA& b) {
    return CompareFileTime(&a.ftLastWriteTime, &b.ftLastWriteTime) > 0;
    };

std::priority_queue<WIN32_FIND_DATA,
        std::vector<WIN32_FIND_DATA>, decltype(dateAscending)>
        names(dateAscending);

WIN32_FIND_DATA wfd;
wil::unique_hfind findHandle( FindFirstFileW(L"*.*", &wfd));
if (findHandle.is_valid())
{
    do
    {
        if (wfd.dwFileAttributes & FILE_ATTRIBUTE_DIRECTORY) {
            // Skip directories
            continue;
        }

        names.push(wfd);
        if (names.size() > files_to_keep) {
            DeleteFileW(names.top().cFileName);
            names.pop();
        }
    } while (FindNextFileW(findHandle.get(), &wfd));
}
It’s unfortunate that
std::
priority_
queue
doesn’t have a deduction guide that deduces the
Comparator
. We have to specify it explicitly, and since it comes after the
Container
, we have to write out the container type manually instead of allowing it to be deduced.
It’s also unfortunate that it’s hard to call
reserve()
on the vector hiding inside the
priority_
queue
. This means that the
names.push()
could throw an exception. At least we use an RAII type (
wil::
unique_
hfind
) to ensure that the find handle is not leaked.
If you have access to
std::
inplace_
vector
, you could use a
std::priority_queue<WIN32_FIND_DATA,
        std::inplace_vector<WIN32_FIND_DATA, files_to_keep + 1>,
        decltype(dateAscending)> names(dateAscending);
to avoid memory allocations entirely. (It also makes it clearer that the algorithm is constant-space.)
This is an example of a so-called
online algorithm
, an algorithm that does its work incrementally rather than requiring all of the input before it can start working.
Exercise
: What if the task was to delete the 10 oldest files?
