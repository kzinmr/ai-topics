---
title: "C++ reminder: Function-local static variables are initialized only once, even if it looks like they get initialized multiple times"
url: "https://devblogs.microsoft.com/oldnewthing/20260928-00/?p=112738/"
fetched_at: 2026-09-29T10:01:08.223579+00:00
source: "devblogs.microsoft.com/oldnewthing"
tags: [blog, raw]
---

# C++ reminder: Function-local static variables are initialized only once, even if it looks like they get initialized multiple times

Source: https://devblogs.microsoft.com/oldnewthing/20260928-00/?p=112738/

When you write a static variable inside a function, it is initialized only once, specifically
at the first time that execution reaches the variable’s declaration
, If execution reaches the variable again in the future, no initialization occurs. It just retains its old value.
Some time ago, I noted an attempt to fix a lifetime issue by making a variable static.
The original code used this header from an external widget library:
// widget.h
struct WidgetController
{
    virtual WidgetKind GetKind() = 0;
    virtual WidgetFlags GetFlags() = 0;
    virtual void OnOpening() = 0;
    ⟦ and so on ⟧
};

std::shared_ptr<Widget>
    MakeWidget(std::shared_ptr<WidgetController> const& controller);
The idea is that you give it a
Widget­Controller
object that the widget consults at various times, allowing you to customize the widget behavior.
The application code called it like this:
// The basic Widget controller provides information but
// does not override any default behaviors.

struct BasicWidgetInfo
{
    WidgetKind kind;
    WidgetFlags flags;
    ⟦ and so on ⟧
};

struct BasicWidgetController : WidgetController
{
    BasicWidgetController(BasicWidgetInfo const& info) :
        m_info(info) {}

    WidgetKind GetKind() override { return m_info.kind; }
    WidgetFlags GetFlags() override { return m_info.flags; }

    // Do not customize any dynamic actions.
    void OnOpening() override { }
    ⟦ and so on ⟧

private:
    BasicWidgetInfo const& m_info;
}

struct Gadget
{
    std::shared_ptr<Widget> m_widget;

    void CreateWidget(GadgetFlags flags)
    {
        BasicWidgetInfo info = {
            WidgetKind::Vanilla,
            WidgetFlags::Openable |
            (flags & GadgetFlags::ClosableWidget ?
                WidgetFlags::Closable : WidgetFlags::None)
        };

        auto controller = std::make_shared<BasicWidgetController>(info);

        m_widget = MakeWidget(controller);
    }

    ⟦ other gadget stuff ⟧
};
The catch is that the
Widget­Options
constructor takes a reference to a
Gadget­Options
and saves the reference. Later, when the widget asks the controller for the flags, the controller will look up the answer in the
BasicWidgetInfo
structure, but that
BasicWidgetInfo
had already destructed when
Create­Custom­Widget
returned, so it returns garbage (or possibly even crashes).
This is a use-after-free bug.
To solve this problem, they made the
info
static. Static objects continue to exist even after the function returns.
void CreateWidget(GadgetFlags flags)
    {
static
BasicWidgetInfo info = {
            WidgetKind::Vanilla,
            WidgetFlags::Openable |
            (flags & GadgetFlags::ClosableWidget ?
                WidgetFlags::Closable : WidgetFlags::None)
        };

        auto controller = std::make_shared<BasicWidgetController>(info);

        m_widget = MakeWidget(controller);
    }
Now the program doesn’t crash. Yay!
However, there is a catch: If two Gadgets both try to create a widget, all of them will have the same options as the first one, because function-local static variables are shared among all instances of a class and are initialized only the first time execution reaches the variable. Whatever flags were passed when you called it the first time get locked into the
info
, and it doesn’t matter what flags you pass subsequent times because
info
has already been initialized; it’s not going to initialize again.
If you want it to initialize each time, then you have to modify it each time.
void CreateWidget(GadgetFlags flags)
    {
static BasicWidgetInfo info;
info = {
WidgetKind::Vanilla,
            WidgetFlags::Openable |
            (flags & GadgetFlags::ClosableWidget ?
                WidgetFlags::Closable : WidgetFlags::None)
        };

        auto controller = std::make_shared<BasicWidgetController>(info);

        m_widget = MakeWidget(controller);
    }
This time, we set the values as a step separate from construction, which means that it executes each time, and the
info
gets updated with the most recent flags.
Of course, this is still a problem if two Gadgets create Widgets with overlapping lifetime, because the two
Basic­Widget­Controller
s are sharing the same
info
. At the second call to
Create­Widget
, its updates to
info
secretly alter the values being used by the first one.
Plus, of course, if
Create­Widget
is called by two threads simultaneously, you have a data race on the writes to the
info
variable, and then the results will be unpredictable.
The underlying problem is that the
Basic­Widget­Controller
wants to extend the lifetime of its
info
, but a reference gives you no way to do it, so it has to rely on the kindness of strangers.
One idea would be to put the
info
somewhere else, so that its lifetime can be extended some other way. Maybe you put it in the
Gadget
:
struct Gadget
{
    std::shared_ptr<Widget> m_widget;
BasicWidgetInfo m_info;
void CreateWidget(GadgetFlags flags)
    {
m_info = {
WidgetKind::Vanilla,
            WidgetFlags::Openable |
            (flags & GadgetFlags::ClosableWidget ?
                WidgetFlags::Closable : WidgetFlags::None)
        };

        auto controller = std::make_shared<BasicWidgetController>(
m_info
);

        m_widget = MakeWidget(controller);
    }

    ⟦ other gadget stuff ⟧
};
Now your job is to make sure that the
m_info
is not destructed before the last shared pointer to the
Basic­Widget­Controller
. This is tricky, since you don’t really know when the last shared pointer to the
Basic­Widget­Controller
will be destructed, although you might have some heuristics given that its lifetime is probably tied to the
Widget
.
Is there a way to hook into the destruction of the final
shared_ptr
?
Yes, and in fact we already used that feature without realizing it.
You can use an aliasing shared pointer that points at a
Basic­Widget­Controller
but whose lifetime controls both a
Basic­Widget­Controller
and its associated
Basic­Widget­Info
.
struct BasicWidgetControllerWithInfo
{
    BasicWidgetControllerWithInfo(BasicWidgetInfo const& info) :
        m_info(info),
        m_controller(m_info) {}

    // The m_info must come before the m_controller because the
    // m_controller initializer depends on the m_info.
    BasicWidgetInfo m_info;
    BasicWidgetController m_controller;
};

    void CreateWidget(GadgetFlags flags)
    {
        BasicWidgetInfo info = {
            WidgetKind::Vanilla,
            WidgetFlags::Openable |
            (flags & GadgetFlags::ClosableWidget ?
                WidgetFlags::Closable : WidgetFlags::None)
        };

        auto controllerAndInfo = std::make_shared<BasicWidgetControllerWithInfo(info);
auto controller = std::shared_ptr<BasicWidgetController>(
controllerAndInfo, &controllerAndInfo->m_controller);
m_widget = MakeWidget(controller);
    }

    ⟦ other gadget stuff ⟧
};
We use an aliasing constructor with a pointer to the controller, but telling it to control the lifetime of the
Basic­Widget­Controller­With­Info
.
Of course, all of this is a problem of the application’s own creation. They should just fix the
Basic­Widget­Controller
to
copy
the
Basic­Widget­Info
instead of taking a reference.
struct BasicWidgetController : WidgetController
{
    BasicWidgetController(BasicWidgetInfo const& info) :
        m_info(info) {}

    WidgetKind GetKind() override { return m_info.kind; }
    WidgetFlags GetFlags() override { return m_info.flags; }

    // Do not customize any dynamic actions.
    void OnOpening() override { }
    ⟦ and so on ⟧

private:
    BasicWidgetInfo
/*
const&
*/
m_info;
}
Now the original code works again.
void CreateWidget(GadgetFlags flags)
    {
        BasicWidgetInfo info = {
            WidgetKind::Vanilla,
            WidgetFlags::Openable |
            (flags & GadgetFlags::ClosableWidget ?
                WidgetFlags::Closable : WidgetFlags::None)
        };

        auto controller = std::make_shared<BasicWidgetController>(info);

        m_widget = MakeWidget(controller);
    }
