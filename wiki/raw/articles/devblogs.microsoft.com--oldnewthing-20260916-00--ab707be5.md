---
title: "Magic statics vs. std::call_once"
url: "https://devblogs.microsoft.com/oldnewthing/20260916-00/?p=112703"
fetched_at: 2026-09-18T10:00:52.295893+00:00
source: "devblogs.microsoft.com/oldnewthing"
tags: [blog, raw]
---

# Magic statics vs. std::call_once

Source: https://devblogs.microsoft.com/oldnewthing/20260916-00/?p=112703

Suppose you have some function like
bool should_use_widgets()
{
    bool supported = ⟦ complex code to check OS features ⟧;
    return supported && is_configuration_enabled("widgets");
}
Since OS Widget support is not something that changes during the lifetime of the program, you want to calculate it once and cache the result.
One way is to use a so-called “magic static”:
bool should_use_widgets()
{
    static const bool supported = [] {
        return ⟦ complex code to check OS features ⟧;
    }();
    return supported && is_configuration_enabled("widgets");
}
Function-local statics are initialized the first time execution reaches the variable. On subsequent executions, nothing happens.
Another way is to use
std::call_once
.
bool is_supported_cached;
std::once_flag is_supported_once;

bool are_widgets_supported()
{
    std::call_once(is_supported_once, [] {
        is_supported_cached = ⟦ complex code to check OS features ⟧;
    });
    return is_supported_cached && is_configuration_enabled("widgets");
}
Why would you choose one over the other?
Magic statics are certainly more convenient. You don’t have to juggle two variables. You just declare a function-local
static
and initialize it. One problem is that they have to be a function-local static. Multiple functions can’t access that same cached variable. But that’s easy to work around: Have a function whose sole job is to manage that one static.
bool are_widgets_supported_in_os()
{
    static const bool supported = [] {
        return ⟦ complex code to check OS features ⟧;
    }();
    return supported;
}

bool are_widgets_supported()
{
    return are_widgets_supported_in_os() &&
        is_configuration_enabled("widgets");
}

bool are_widget_carriers_supported()
{
    return are_widgets_supported_in_os() &&
        is_configuration_enabled("widget_carriers");
}
This trick is often used for singleton patterns.
class Singleton
{
public:
    static Singleton& GetInstance()
    {
        static Singleton instance;
        return instance;
    }

    ⟦ various methods go here ⟧;

private:
    Singleton() = default;
    Singleton(Singleton const&) = delete;
    Singleton& operator=(Singleton const&) = delete;
    ~Singleton() = default;
}
So when would you use
call_once
?
Magic statics work only for statics. Maybe you want to lazy-initialize a non-static data member.
Suppose we have a
Gadget
that is constructed with an associated
Widget
. And suppose that the
Gadget
support for polarity reversal is dependent on whether the
Widget
supports polarity reversal. Furthermore, polarity reversibility is expensive to calculate, but since it is an immutable property, we can calculate it only once and cache the result.
class Gadget
{
public:
    Gadget(std::shared_ptr<Widget> const& widget) : widget(widget) {}

    bool can_reverse_polarity()
    {
        return can_reverse_polarity_cached;
    }

private:
    std::shared_ptr<Widget> const widget;
    bool can_reverse_polarity_cached =
        is_configuration_enabled("polarity_reversal") &&
        is_widget_polarity_reversible(*widget);
};
The
can_
reverse_
polarity_
cached
is a non-static data member with an explicit initializer, so it initializes at the construction of the
Gadget
class, rather than initializing on demand the first time somebody calls
can_
reverse_
polarity
.
“No problem,” you say. “I can use a magic static.”
bool can_reverse_polarity()
    {
static bool can_reverse_polarity_cached =
is_configuration_enabled("polarity_reversal") &&
is_widget_polarity_reversible(*widget);
return can_reverse_polarity_cached;
    }
Function-static variables in a member function are static with respect to the member function. All instances of
Gadget
share the same member function, and therefore they all share the same
can_
reverse_
polarity_
cached
variable. The time you call
Gadget::
can_
reverse_
polarity()
, it calculates the reversibility of the
Widget
that is associated with the
Gadget
you called it from, and that value is then locked in for all future calls to
Gadget::
can_
reverse_
polarity()
, even though the future calls may be on unrelated
Gadget
s.
What we want is a variant of magic statics that initialize for each
instance
of the class, rather than once for all instances.
That’s the case for
std::
call_once
.
class Gadget
{
public:
    Gadget(std::shared_ptr<Widget> const& widget) : widget(widget) {}

    bool can_reverse_polarity()
    {
std::call_once(can_reverse_polarity_once, [] {
can_reverse_polarity_cached =
is_configuration_enabled("polarity_reversal") &&
is_widget_polarity_reversible(*widget);
});
return can_reverse_polarity_cached;
    }

private:
    std::shared_ptr<Widget> const widget;
bool can_reverse_polarity_cached; // initializes on demand
std::once_flag can_reverse_polarity_once;
};
I guess you could encapsulate this in a
lazy<T>
type.¹
template<typename T, typename L>
struct lazy
{
    lazy(L&& l) : init(std::forward<L>(l)) {}

    T& get() {
        std::call_once(once, [&] {
            value.emplace(init());
        });
        return *value;
    }
private:
    std::optional<T> value;
    std::once_flag once;
    std::decay_t<L> init;
};

template<typename T, typename L>
lazy<T, L> make_lazy(L&& l)
{
    return { std::forward<L>(l) };
}

void test()
{
    auto v = make_lazy<int>([] {
        printf("Slow calculation\n");
        return 42;
    });

    printf("Value is %d\n", v.get());
    printf("Value is still %d\n", v.get());
}
But wait, we also have
std::async
with deferred execution. Should we use that? We’ll look at this question next time.
¹ Note that this is not the same as
the
std::lazy
proposal
.
