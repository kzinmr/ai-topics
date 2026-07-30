---
title: "Making an agile version of a Windows Runtime delegate in C++/WinRT, part 8"
url: "https://devblogs.microsoft.com/oldnewthing/20260729-00/?p=112570"
fetched_at: 2026-07-30T10:06:58.335213+00:00
source: "devblogs.microsoft.com/oldnewthing"
tags: [blog, raw]
---

# Making an agile version of a Windows Runtime delegate in C++/WinRT, part 8

Source: https://devblogs.microsoft.com/oldnewthing/20260729-00/?p=112570

Last time, we
fixed the problem of an exception thrown from the custom deleter’s constructor resulting in a reference leak
. But wait, there’s another source of exceptions.
To recap, here is where we left off:
if (d.try_as<::INoMarshal>()) {
        in_context_deleter del;
        void* p;
        if constexpr (std::is_reference_v<Delegate>) {
            p = winrt::detach_abi(d);
        } else {
            winrt::copy_to_abi(d, p);
        }
        return
            [p = std::unique_ptr<void, in_context_deleter>(p, std::move(del)),
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
Precreating the deleter means that an exception in its construction happens before we do any funny business with the raw pointer. That way, we close the gap between creating the raw pointer (with its reference obligation) and putting it into a
unique_ptr
.
Or did we?
In C++, the order of construction of the captures of a lambda is
unspecified
.
[expr.prim.lambda.capture]
(10.2) ⟦ … ⟧ For each entity captured by copy, an unnamed non-static data member is declared in the closure type. The declaration order of these members is
unspecified
.
Since the order of construction is the order of declaration, the fact that the declaration order is unspecified implies that the order of construction is unspecified. And just to make sure you get the point, this is reiterated in paragraph 15 where it discusses the initialization of captures:
(15) ⟦ … ⟧ These initializations are performed when the
lambda-expression
is evaluated and in the (
unspecified
) order in which the non-static data members are declared.
Therefore, it’s possible that the
get_
context_
token()
happens before the creation of the
std::
unique_
ptr
, and if
get_
context_
token()
fails, then the reference held in the raw pointer is leaked because it never got put into a
unique_ptr
.
One solution is to put it into a
unique_ptr
before we create the lambda.
if (d.try_as<::INoMarshal>()) {
        in_context_deleter del;
        void* p;
        if constexpr (std::is_reference_v<Delegate>) {
            p = winrt::detach_abi(d);
        } else {
            winrt::copy_to_abi(d, p);
        }
std::unique_ptr<void, in_context_deleter> up(p, std::move(del));
return
            [p =
std::move(up)
,
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
By creating the
unique_ptr
immediately, we remove any opportunity for an exception to sneak in between the time we create an obligation in the raw pointer and the time we assign that obligation to the
unique_ptr
.
One thing that bugs me about this is that we introduce another
unique_ptr
, which means that its destructor will have to check something for null, when it’s almost always null.
We can avoid this temporary
unique_ptr
by using copy elision directly into the capture.
if (d.try_as<::INoMarshal>()) {
auto make = [](auto&& d) {
in_context_deleter del;
            void* p;
            if constexpr (std::is_reference_v<Delegate>) {
                p = winrt::detach_abi(d);
            } else {
                winrt::copy_to_abi(d, p);
            }
return std::unique_ptr<void,
in_context_deleter>(p, std::move(del));
};
return
            [p =
make(std::forward<Delegate>(d))
,
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
Bonus reading
:
Previously, in copy elision
.
But an easier solution is to create the token early, just like we did with the deleter.
if (d.try_as<::INoMarshal>()) {
        in_context_deleter del;
auto token = get_context_token();
void* p;
        if constexpr (std::is_reference_v<Delegate>) {
            p = winrt::detach_abi(d);
        } else {
            winrt::copy_to_abi(d, p);
        }
        return
            [p = std::unique_ptr<void, in_context_deleter>(p, std::move(del)),
token
](auto&&...args) {
                if (token == get_context_token()) {
                    std::remove_reference_t<Delegate> d;
                    winrt::copy_from_abi(d, p.get());
                    d(std::forward<decltype(args)>(args)...);
                } else {
                    throw winrt::hresult_error(CO_E_NOT_SUPPORTED);
                }
            };
    }
Okay, are we done?
Maybe.
But maybe this all wasn’t worth it.
We’ll talk about that next time.
