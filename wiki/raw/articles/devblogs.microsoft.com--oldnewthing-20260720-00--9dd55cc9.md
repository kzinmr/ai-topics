---
title: "Making an agile version of a Windows Runtime delegate in C++/WinRT, part 1"
url: "https://devblogs.microsoft.com/oldnewthing/20260720-00/?p=112545"
fetched_at: 2026-07-21T07:01:36.747040+00:00
source: "devblogs.microsoft.com/oldnewthing"
tags: [blog, raw]
---

# Making an agile version of a Windows Runtime delegate in C++/WinRT, part 1

Source: https://devblogs.microsoft.com/oldnewthing/20260720-00/?p=112545

Suppose you have some C++/WinRT code that receives a delegate from an outside source, and you might invoke that delegate from a potentially different COM context. However, the original delegate may not be agile. How can you make an agile version of that delegate?
The easy way is to wrap the delegate in an
agile_
ref
, and then resolve the
agile_
ref
back to a delegate when you want to invoke it.
template<typename Delegate>
Delegate make_agile_delegate(Delegate const& d)
{
    return [agile = winrt::agile_ref(d)](auto&&...args) {
        return agile.get()(std::forward<decltype(args)>(args)...);
    };
}
But if it were that easy, why would we call this article “part 1”?
More in part 2.
