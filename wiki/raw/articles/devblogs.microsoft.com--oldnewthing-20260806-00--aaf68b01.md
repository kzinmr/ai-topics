---
title: "Creating a fake agile wrapper that is technically agile but is not useful outside its home apartment, part 4"
url: "https://devblogs.microsoft.com/oldnewthing/20260806-00/?p=112595"
fetched_at: 2026-08-07T10:19:28.220903+00:00
source: "devblogs.microsoft.com/oldnewthing"
tags: [blog, raw]
---

# Creating a fake agile wrapper that is technically agile but is not useful outside its home apartment, part 4

Source: https://devblogs.microsoft.com/oldnewthing/20260806-00/?p=112595

Last time, we successfully
our plan to use the global interface table to hold created a fake agile wrapper that is technically agile, even though it isn’t useful outside its home apartment
. I noted that there are opportunities for fine-tuning.
One thing we can do is move the non-marshalable COM object rather than copying it. This means forwarding the reference all the way into the
force_
marshal
wrapper.
template<typename Smart>
struct force_marshal :
    winrt::implements<force_marshal<Smart>, IUnknown, winrt::non_agile>
{
template<typename Arg>
force_marshal(Arg&& arg) : m_p(std::forward<Arg>(arg)) {}
Smart m_p;
};
The
force_
marshal<Smart>
now takes anything and forwards it into the smart pointer. This means that if the inbound parameter is an rvalue reference to a smart pointer, the COM reference is moved into the
force_
marshal<Smart>
object rather than copied.
Now it’s a matter of plumbing this reference all the way down.
template<typename T>
struct fake_agile_ref
{
    ⟦ ... ⟧
template<typename Arg>
fake_agile_ref(
Arg&&
p) : m_raw(winrt::get_abi(p))
    {
        if (m_raw) {
            m_context = winrt::capture<IContextCallback>(CoGetObjectContext);
            m_token = get_context_token();
            m_git = winrt::create_instance<IGlobalInterfaceTable>(CLSID_StdGlobalInterfaceTable);
            winrt::check_hresult(m_git->RegisterInterfaceInGlobal(
                winrt::make<force_marshal<Smart>>(
std::forward<Arg>(p)
).get(),
                __uuidof(IUnknown), &m_cookie));
        }
    }

    ⟦ ... ⟧
};

template<typename Delegate>
std::remove_reference_t<Delegate> make_agile_delegate(Delegate&& d)
{
    if (d.try_as<::IAgileObject>()) {
        return d;
    }

    if (d.try_as<::INoMarshal>()) {
        return [agile = fake_agile_ref(
std::forward<Delegate>(d)
](auto&&...args) {
            return agile.get()(std::forward<decltype(args)>(args)...);
        };
    }

    return [agile = winrt::agile_ref(d)](auto&&...args) {
        return agile.get()(std::forward<decltype(args)>(args)...);
    };
}
Note that we didn’t have to update the deduction guides for
fake_
agile_
ref
to add forwarding support. Deduction guides are matched against the constructor invocation to determine which template specialization to use, but they are not used for actually invoking the constructor. That happens by matching against the constructors themselves. So if somebody tries to create a
fake_
agile_
ref
from an rvalue reference, the deduction guide for
const&
steers class template argument deduction (CTAD) toward the correct specialization, and then when the compiler actually looks for a constructor, it finds the one that takes an rvalue reference.
Remember how I complained that we couldn’t use
std::
unique_ptr
to avoid a lot of boilerplate in
fake_
agile_
ref
to manage the fact that cookies cannot be copied?
Yeah, so maybe I lied.
We’ll look at it next time.
