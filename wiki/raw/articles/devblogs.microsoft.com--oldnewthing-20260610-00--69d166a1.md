---
title: "What's the opposite of Clip­Cursor that lets me exclude the cursor from a region?"
url: "https://devblogs.microsoft.com/oldnewthing/20260610-00/?p=112412"
fetched_at: 2026-06-11T07:00:58.002286+00:00
source: "devblogs.microsoft.com/oldnewthing"
tags: [blog, raw]
---

# What's the opposite of Clip­Cursor that lets me exclude the cursor from a region?

Source: https://devblogs.microsoft.com/oldnewthing/20260610-00/?p=112412

A customer wanted to prevent the user from dragging an object into a specific region of their window. Their current implementation detects that the mouse is an in illegal location and uses
Set­Cursor­Pos
to move it to a nearby legal location. However, this creates flicker because the cursor actually does enter the illegal region and then jumps out.
Let’s illustrate this with
our scratch program
.
POINT g_pt;
const RECT g_rcExclude = { 100, 100, 200, 200 };

RECT ItemRect(POINT pt)
{
    return RECT{ pt.x - 10, pt.y - 10, pt.x + 10, pt.y + 10 };
}
The
g_pt
variable holds the location of our object, and the
g_rcExclude
is the rectangle in which the object is forbidden. The
ItemRect
function produces a bounding rectangle for our object so we can draw something there.
void
PaintContent(HWND hwnd, PAINTSTRUCT* pps)
{
    FillRect(pps->hdc, &g_rcExclude, (HBRUSH)(COLOR_WINDOWTEXT + 1));
    RECT rcItem = ItemRect(g_pt);
    FillRect(pps->hdc, &rcItem, (HBRUSH)(COLOR_APPWORKSPACE + 1));
}
Painting our content is a straightforward matter of drawing the forbidden rectangle in the text color and drawing the object in the app workspace color.
void OnMouseMove(HWND hwnd, int x, int y, UINT keyFlags)
{
    POINT ptNew = { x, y };

    if (PtInRect(&g_rcExclude, ptNew)) {
        // Clamp to nearest legal position
        int leftMargin = ptNew.x - g_rcExclude.left;
        int topMargin = ptNew.y - g_rcExclude.top;
        int rightMargin = g_rcExclude.right - ptNew.x;
        int bottomMargin = g_rcExclude.bottom - ptNew.y;

        int dx, dy;
        int x, y;
        if (leftMargin < rightMargin) {
            x = g_rcExclude.left;
            dx = leftMargin;
        } else {
            x = g_rcExclude.right;
            dx = rightMargin;
        }
        if (topMargin < bottomMargin) {
            y = g_rcExclude.top;
            dy = topMargin;
        } else {
            y = g_rcExclude.bottom;
            dy = bottomMargin;
        }
        if (dx < dy) {
            ptNew.x = x;
        } else {
            ptNew.y = y;
        }
        POINT ptScreen = ptNew;
        ClientToScreen(hwnd, &ptScreen);
        SetCursorPos(ptScreen.x, ptScreen.y);
    }

    if (g_pt.x != ptNew.x || g_pt.y != ptNew.y) {
        RECT rcItem = ItemRect(g_pt);
        InvalidateRect(hwnd, &rcItem, TRUE);
        g_pt = ptNew;
        rcItem = ItemRect(g_pt);
        InvalidateRect(hwnd, &rcItem, TRUE);
    }
}

// Add to WndProc

        HANDLE_MSG(hwnd, WM_MOUSEMOVE, OnMouseMove);
When the mouse moves, we take the mouse position and see if it is in the forbidden rectangle. If so, we update the coordinates to the nearest legal position and move the mouse there with
Set­Cursor­Pos
.
Whether or not we had to update the coordinates, if the result produces a new location, then invalidate the object’s old location (so it will be erased at the next paint cycle), update the object position, and then invalidate the object’s new position (so it will be drawn at the next paint cycle).
When you run this program, you can try to move the mouse into the forbidden rectangle, but the program will shove the mouse back out. However, it flickers a lot bcause the mouse briefly enters the forbidden rectangle before it is expelled from it.
The customer saw that there is a
Clip­Cursor
function to constrain the mouse to remain
inside
a rectangle, but is there an inverse version that forces the mouse to remain
outside
a rectangle?
There is no such function, but that’s okay.
What you can do when the mouse is in an illegal position is just pretend that it’s in a legal position. Let the user move the mouse into a illegal position, but show the feedback at the nearest legal position, and if they drop the object, let it drop at the nearest legal position.
In the above program, that means we remove the call to
Set­Cursor­Pos
.
void OnMouseMove(HWND hwnd, int x, int y, UINT keyFlags)
{
    POINT ptNew = { x, y };

    if (PtInRect(&g_rcExclude, ptNew)) {
        // Clamp to nearest legal position
        int leftMargin = ptNew.x - g_rcExclude.left;
        int topMargin = ptNew.y - g_rcExclude.top;
        int rightMargin = g_rcExclude.right - ptNew.x;
        int bottomMargin = g_rcExclude.bottom - ptNew.y;

        int dx, dy;
        int x, y;
        if (leftMargin < rightMargin) {
            x = g_rcExclude.left;
            dx = leftMargin;
        } else {
            x = g_rcExclude.right;
            dx = rightMargin;
        }
        if (topMargin < bottomMargin) {
            y = g_rcExclude.top;
            dy = topMargin;
        } else {
            y = g_rcExclude.bottom;
            dy = bottomMargin;
        }
        if (dx < dy) {
            ptNew.x = x;
        } else {
            ptNew.y = y;
        }
//
POINT ptScreen = ptNew;
//
ClientToScreen(hwnd, &ptScreen);
//
SetCursorPos(ptScreen.x, ptScreen.y);
}

    if (g_pt.x != ptNew.x || g_pt.y != ptNew.y) {
        RECT rcItem = ItemRect(g_pt);
        InvalidateRect(hwnd, &rcItem, TRUE);
        g_pt = ptNew;
        rcItem = ItemRect(g_pt);
        InvalidateRect(hwnd, &rcItem, TRUE);
    }
}
This time, we don’t try to punish you for moving the mouse into the forbidden rectangle. But the object won’t follow the mouse into a forbidden region.
