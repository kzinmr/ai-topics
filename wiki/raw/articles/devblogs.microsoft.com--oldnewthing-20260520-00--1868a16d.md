---
title: "The classic TreeView control lets me sort by name or by lParam, but why not both?"
url: "https://devblogs.microsoft.com/oldnewthing/20260520-00/?p=112343"
fetched_at: 2026-05-21T07:01:28.202221+00:00
source: "devblogs.microsoft.com/oldnewthing"
tags: [blog, raw]
---

# The classic TreeView control lets me sort by name or by lParam, but why not both?

Source: https://devblogs.microsoft.com/oldnewthing/20260520-00/?p=112343

The Win32 TreeView control in the common controls library provides two ways of sorting elements.
TVM_­SORT­CHILDREN
: Sorts children alphabetically by name.
TVM_­SORT­CHILDREN­CB
: Sorts children via custmm callback.
The custom callback is provided the
lParam
of the two tree items being compared. But what if you want to sort by a combination of both the text and the
lParam
? How do you get both?
There are two general designs for using UI controls that represent collections.
One model is for the UI control to be the data repository. Everything you need to know about the item resides in the UI control, somewhere in its name, its check state, its selection state, whatever. If you need to know something about an item, you ask the UI control for the information.
The second model is for the data repository to be some sort of object that itself does not have any UI. (This is known in the biz as a “data model”.) You then construct UI elements to be the representation of those objects.
Windows controls generally lean toward the data model approach because there is usually a lot of information about an item that is not present in its UI representation. The data model approach also allows for optimizations in which where very large collections of items create UI elements only for the items that are visible on screen. You can see this in the XAML ListView control as well as in the classic Win32 ListView control when placed into owner-data mode.
For the controls in the common controls library, the general pattern is to provide a place to store a pointer-sized value that is not shown in the UI, typically called “item data” or just
lParam
. Here is where you store a pointer to the data model object that the UI object represents.
Okay, so let’s look at the TreeView sort methods again.
The
TVM_­SORT­CHILDREN­CB
message takes a callback which is passed the
lParam
s of two items to compare. The theory is that these
lParam
s are pointers to larger data structures that describe the item, and you use those larger data structures to decide the ordering of the two items.
The
TVM_­SORT­CHILDREN
message doesn’t take a callback. It is a convenience method for the case where you are just sorting by name, so it uses the already-available name assigned to the item.
The case where you would need both is the case where the
lParam
is not enough to recover the name, either because it’s a pointer to a structure that doesn’t include a name, or because it’s not a pointer at all.
I can imagine running into this case if the only information you need to track for each TreeView item is its name and a pointer-sized piece of data. You put the name in the TreeView item text and the other data in the
lParam
. This plan works great until you need to sort the items, and your sort comparison function wants access to both pieces of data.
The solution is to switch to a data model pattern. Allocate a structure for each TreeView item and put the string and additional data in that structure. (Alternatively, you could just be sneaky and have the structure be the
HTREEITEM
and the additional data. Then you can recover the string by using the
TVM_
GET­ITEM
message.)
Bonus chatter
: In theory, the
TVM_­SORT­CHILDREN­CB
could have passed the
HTREEITEM
s to the callback. The callback could then use the
HTREEITEM
to obtain both the string and the
lParam
. I suspect this didn’t happen because most callback functions would just ask for the
lParam
from the
HTREEITEM
,
TVM_­SORT­CHILDREN­CB
is doing you a favor and saving you a bunch of work by giving you the thing you probably wanted in the first place.
