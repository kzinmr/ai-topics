---
title: "How can I make it easier to use the helper class that lets me pass more than one parameter to co_await?"
url: "https://devblogs.microsoft.com/oldnewthing/20261113-00/?p=112856/"
fetched_at: 2026-11-15T10:00:56.334082+00:00
source: "devblogs.microsoft.com/oldnewthing"
tags: [blog, raw]
---

# How can I make it easier to use the helper class that lets me pass more than one parameter to co_await?

Source: https://devblogs.microsoft.com/oldnewthing/20261113-00/?p=112856/

Last time, we figured out
how to pass more than one parameter to
co_await
by combining the multiple parameter into a single mega-parameter.
But having to name the mega-parameter is annoying. Sure, today we have
widget_
with_
priority
, and then we get
gadget_
with_
timeout
, and then
doodad_
with_priority_
and_
timeout
, and oh my goodness it’s out of control.
Instead of making the caller have to name the mega-parameter, we can create a helper method that produces it.
struct Widget
{
    ⟦ ... other stuff ... ⟧

private:
    bool inner_await_ready() const { return ⟦ ... ⟧; }

    bool inner_await_suspend(std::coroutine_handle<> handle, int priority)
    {
        return internal_start(handle, priority);
    }

    auto inner_await_resume() const { return ⟦ ... ⟧; }

    struct with_priority
    {
        with_priority(Widget const& widget, int priority) :
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
public:
with_priority start(int priority = 0) {
return with_priority(*this, priority);
}
};
Now callers can write
co_await widget.start(priority);
As a convenience, I gave the
start()
method a default priority, so you can write
co_await widget.start();
You might even decide to bring back awaiting the widget directly, and having it mean “start with default priority”.
struct Widget
{
    ⟦ ... other stuff ... ⟧

    ⟦ ... as before ... ⟧

public:
    with_priority start(int priority = 0) {
        return with_priority(*this, priority);
    }
// Or you can await the Widget directly, which starts it with
// default priority.
auto await_ready() const { return inner_await_ready(); }
auto await_suspend(std::coroutine_handle<> handle)
{
return internal_start(handle, 0);
}
auto await_resume() const { internal_await_resume(); }
};
At this point you can simplify the class by just renaming the internal awaitable methods back to their original names.
struct Widget
{
    ⟦ ... other stuff ... ⟧

public:
    // Awaiting the Widget starts it with default priority.
    bool
await_ready
() const { return ⟦ ... ⟧; }

    bool
await_suspend
(std::coroutine_handle<> handle, int priority = 0)
    {
        return internal_start(handle, priority);
    }

    auto
await_resume
() const { return ⟦ ... ⟧; }

private:
    struct with_priority
    {
        with_priority(Widget const& widget, int priority) :
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

public:
    // start() lets you start with custom priority.
    with_priority start(int priority = 0) {
        return with_priority(*this, priority);
    }
};
