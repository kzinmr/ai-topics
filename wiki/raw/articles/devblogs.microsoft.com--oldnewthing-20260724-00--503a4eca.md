---
title: "Making an agile version of a Windows Runtime delegate in C++/WinRT, part 5"
url: "https://devblogs.microsoft.com/oldnewthing/20260724-00/?p=112562"
fetched_at: 2026-07-25T10:10:36.868492+00:00
source: "devblogs.microsoft.com/oldnewthing"
tags: [blog, raw]
---

# Making an agile version of a Windows Runtime delegate in C++/WinRT, part 5

Source: https://devblogs.microsoft.com/oldnewthing/20260724-00/?p=112562

So far, we have
handled the case of a non-marshalable delegate
by wrapping it in a delegate that fails with
CO_
E_
NOT_
SUPPORTED
if used in a manner that would require marshaling.
But we missed something.
Let’s look at it again.
if (d.try_as<::INoMarshal>()) {
        return [d, token = get_context_token(),
                context = winrt::capture<IContextCallback>(CoGetObjectContext)](auto&&...args) {
            if (token == get_context_token()) {
                d(std::forward<decltype(args)>(args)...);
            } else {
                throw winrt::hresult_error(CO_E_NOT_SUPPORTED);
            }
        };
    }
While we copy and invoke the delegate only from its original context, we still
destruct
it from a possibly-wrong context.
This is a serious problem not just because the non-agile delegate might not be using thread-safe atomic instructions to manage its reference count, but even worse, if the release drops the reference count to zero, the delegate will destruct on the wrong thread, and that will probably create lots of problems.
We have to destruct the non-agile delegate in its original context. We can do this with a
std::
unique_
ptr
and a custom deleter. The
std::
unique_
ptr
handles all the move operations and the deleter cleans up the last pointer.
struct in_context_deleter
{
    winrt::com_ptr<IContextCallback> context =
                winrt::capture<IContextCallback>(CoGetObjectContext);

    void operator()(void* p)
    {
        if (p) {
            ComCallData data{};
            data.pUserDefined = p;
            context->ContextCallback([](ComCallData* data) {
                winrt::IUnknown{ data->pUserDefined, winrt::take_ownership_from_abi };
                return S_OK;
            }, &data, __uuidof(IContextCallback), 5, nullptr);
        }
    }
};
This stateful deleter remembers the context to use for final destruction. When it’s time to do the destruction, we switch into the target context via
IContext­Callback::
Context­Callback
and take ownership of the raw pointer into a
winrt::
IUnknown
. The destructor of the
winrt::
IUnknown
will perform the release.
We can use this stateful deleter around the raw delegate pointer.
// Don't use this yet - read to the end of the series

template<typename Delegate>
std::remove_reference_t<Delegate> make_agile_delegate(Delegate&& d)
{
    if (d.try_as<::IAgileObject>()) {
        return d;
    }
    if (d.try_as<::INoMarshal>()) {
void* p;
if constexpr (std::is_reference_v<Delegate>) {
p = winrt::detach_abi(d);
} else {
winrt::copy_to_abi(d, p);
}
return
            [
p = std::unique_ptr<void, in_context_deleter>(p),
/*
context = winrt::capture<IContextCallback>(CoGetObjectContext),
*/
token = get_context_token()](auto&&...args) {
                if (token == get_context_token()) {
                    std::remove_reference_t<Delegate> d;
                    winrt::copy_from_abi(d, p.get());
                    d(std::forward<decltype(args)>(args)...);
                } else {
                    throw winrt::hresult_error(CO_E_NOT_SUPPORTED);
                }
            };
    } else {
        return [agile = winrt::agile_ref(d)](auto&&...args) {
            return agile.get()(std::forward<decltype(args)>(args)...);
        };
    }
}
The first block gets a raw ABI pointer, either by moving it out of the inbound delegate if we can, else by copying it from the inbound delegate.
The second part wraps the raw ABI pointer inside a
std::
unique_ptr
with our custom deleter, and the custom deleter makes sure that the
Release
of the original delegate happens in the correct context.
Are we done?
No!
More next time.
