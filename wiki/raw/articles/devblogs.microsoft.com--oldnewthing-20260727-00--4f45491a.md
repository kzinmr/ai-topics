---
title: "Making an agile version of a Windows Runtime delegate in C++/WinRT, part 6"
url: "https://devblogs.microsoft.com/oldnewthing/20260727-00/?p=112566"
fetched_at: 2026-07-28T10:08:50.647120+00:00
source: "devblogs.microsoft.com/oldnewthing"
tags: [blog, raw]
---

# Making an agile version of a Windows Runtime delegate in C++/WinRT, part 6

Source: https://devblogs.microsoft.com/oldnewthing/20260727-00/?p=112566

It looked like we were done when we
fixed the problem of releasing a non-marshalable delegate on the correct thread
.
But we missed something.
Again.
if (d.try_as<::INoMarshal>()) {
        void* p;
        if constexpr (std::is_reference_v<Delegate>) {
            p = winrt::detach_abi(d);
        } else {
            winrt::copy_to_abi(d, p);
        }
        return
            [p = std::unique_ptr<void, in_context_deleter>(p),
            token = get_context_token()](auto&&...args) {
                if (token == get_context_token()) {
                    std::remove_reference_t<Delegate> d;
                    winrt::copy_from_abi(d, p.get());
                    d(std::forward<decltype(args)>(args)...);
                } else {
                    throw winrt::hresult_error(CO_E_NOT_SUPPORTED);
                }
            };
    }
The first part gets a raw ABI pointer, either by moving it out of the inbound delegate if we can, else by copying it from the inbound delegate. The reference count is owned by the raw pointer.
The second part wraps the raw ABI pointer inside a
std::
unique_ptr
with our custom deleter. The unique pointer now owns the reference count, and the custom deleter will release it.
The problem is that one of the requirements for a custom deleter is that if you use the
unique_ptr(p)
constructor, the custom deleter must not throw an exception at construction.
[unique.ptr.single.ctor]
constexpr explicit unique_ptr(type_identity_t<pointer> p) noexcept;
Constraints:
is_
pointer_
v<deleter_
type>
is
false
and
is_
default_
constructible_
v<deleter_
type>
is
true
.
Preconditions:
D
meets the Cpp17DefaultConstructible requirements, and that
construction does not throw an exception
.
But our custom deleter could throw an exception if
Co­Get­Object­Context
fails. So it doesn’t meet the preconditions.
We can fix that by using the constructor that takes an explicit deleter from which the stored deleter can be move-constructed. If an exception occurs, it happens during the creation of the parameter and not inside the
unique_
ptr
constructor.
if (d.try_as<::INoMarshal>()) {
        void* p;
        if constexpr (std::is_reference_v<Delegate>) {
            p = winrt::detach_abi(d);
        } else {
            winrt::copy_to_abi(d, p);
        }
        return
            [p = std::unique_ptr<void, in_context_deleter>(p,
{}
),
            token = get_context_token()](auto&&...args) {
                if (token == get_context_token()) {
                    std::remove_reference_t<Delegate> d;
                    winrt::copy_from_abi(d, p.get());
                    d(std::forward<decltype(args)>(args)...);
                } else {
                    throw winrt::hresult_error(CO_E_NOT_SUPPORTED);
                }
            };
    }
Okay, so now we’re done?
Nope, still broken.
More next time.
