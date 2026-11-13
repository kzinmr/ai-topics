---
title: "How can I pass more than one parameter to co_await?"
url: "https://devblogs.microsoft.com/oldnewthing/20261112-00/?p=112851/"
fetched_at: 2026-11-13T10:01:08.981417+00:00
source: "devblogs.microsoft.com/oldnewthing"
tags: [blog, raw]
---

# How can I pass more than one parameter to co_await?

Source: https://devblogs.microsoft.com/oldnewthing/20261112-00/?p=112851/

Suppose you have an awaitable object, but you want the caller to pass a bonus parameter when they do a
co_await
. For example, you may want the caller to be able to pass a priority or a timeout or something else that modifies how the await occurs.
struct Widget
{
    ⟦ ... other stuff ... ⟧

    bool await_ready() const { return ⟦ ... ⟧; }

    bool await_suspend(std::coroutine_handle<> handle)
    {
        int priority = ??? how do I get a priority ???;

        return internal_start(handle, priority);
    }

    auto await_resume() { return ⟦ ... ⟧; }
};

// This doesn't work
auto result = co_await (widget, priority);
So how do you pass two parameters to
co_await
so they can be used in
await_
suspend
?
It’s a trick question. You can’t. The
co_await
operator takes only one parameter.
So you’ll have to take all the things you want to use and put them into a single parameter.
Wrap the awaitable object and its parameters into a larger object, and then await the larger object.
First, let’s rename away the coroutine methods inside
Widget
since we aren’t awaiting it directly any more.
struct Widget
{
    ⟦ ... other stuff ... ⟧
private:
bool
inner_
await_ready() const { return ⟦ ... ⟧; }

    bool
inner_
await_suspend(std::coroutine_handle<> handle)
    {
        int priority = ??? how do I get a priority ???;

        return internal_start(handle, priority);
    }

    auto
inner_
await_resume() const { return ⟦ ... ⟧; }
};
Now we can add a priority parameter to the
inner_
await_
suspend
:
struct Widget
{
    ⟦ ... other stuff ... ⟧

private:
    bool inner_await_ready() const { return ⟦ ... ⟧; }

    bool inner_await_suspend(std::coroutine_handle<> handle,
int priority
)
    {
        return internal_start(handle, priority);
    }

    auto inner_await_resume() const { return ⟦ ... ⟧; }
};
And finally, we create a helper class (which is a friend of
Widget
) that wraps the original object and its priority into a single new awaitable object.
struct Widget
{
    ⟦ ... other stuff ... ⟧

private:
friend struct widget_with_priority;
⟦ ... as before ... ⟧
};
struct widget_with_priority
{
widget_with_priority(Widget const& widget, int priority) :
m_widget(widget), m_priority(priority) {}
bool await_ready() const { return m_widget.inner_await_ready(); }
auto await_suspend(std::coroutine_handle<> handle)
{
return m_widget.inner_await_suspend(handle, m_priority);
}
auto await_ready() {
return m_widget.await_ready();
}
Widget const& m_widget;
int m_priority;
};
You can now do
co_await widget_with_priority(widget, priority);
This solves the problem but is rather unwieldy. We’ll address that next time.
