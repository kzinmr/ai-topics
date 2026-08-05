---
title: "Creating a fake agile wrapper that is technically agile but is not useful outside its home apartment, part 2"
url: "https://devblogs.microsoft.com/oldnewthing/20260804-00/?p=112586"
fetched_at: 2026-08-05T10:12:32.766584+00:00
source: "devblogs.microsoft.com/oldnewthing"
tags: [blog, raw]
---

# Creating a fake agile wrapper that is technically agile but is not useful outside its home apartment, part 2

Source: https://devblogs.microsoft.com/oldnewthing/20260804-00/?p=112586

Last time,
we hatched a plan for holding a reference to an object in another apartment that automatically expires when the apartment runs down
. Let’s try to implement that plan.
template<typename T>
struct fake_agile_ref
{
private:
    using Smart = std::conditional_t<
        std::is_base_of_v<winrt::Windows::Foundation::IUnknown, T>,
        T, winrt::com_ptr<T>>;
We define
Smart
to represent the smart pointer that holds a
T
. If
T
is a projected type, then it is already a smart pointer. Otherwise,
T
is a COM interface, and we put it inside a
com_ptr
. This is the same pattern that the C++/WinRT
agile_ref<T>
uses.
winrt::com_ptr<IContextCallback> m_context;
    ULONG_PTR m_token = 0;
    winrt::com_ptr<IGlobalInterfaceTable> m_git;
    DWORD m_cookie = 0;
    void* m_raw = nullptr;
Our fake agile reference starts with a callback context and a context token. These are used to detect whether we are in the correct apartment when it comes time to access the original non-agile COM object.
Next comes a reference to the GIT and a cookie that records the registered reference to the original non-agile COM object.
Finally, we keep a raw (non-refcounted) pointer to the original non-agile COM object.
The fake agile reference is considered “empty” if the cookie is zero, meaning that it does not refer to any object. In the case of an empty fake agile reference, none of the other members contains anything meaningful.
public:
    fake_agile_ref(std::nullptr_t = nullptr) noexcept {}
Constructing an empty
fake_
agile_
ref
is easy: Just leave everything at its initial state. In particular, the
m_cookie
is zero, meaning that there is nothing inside. The values of all the other members are irrelevant, as long as they can be safely destructed.
fake_agile_ref(Smart const& p) : m_raw(winrt::get_abi(p))
    {
        if (m_raw) {
            m_context = winrt::capture<IContextCallback>(CoGetObjectContext);
            m_token = get_context_token();
            m_git = winrt::create_instance<IGlobalInterfaceTable>(CLSID_StdGlobalInterfaceTable);
            winrt::check_hresult(m_git->RegisterInterfaceInGlobal(
                static_cast<::IUnknown*>(m_raw), __uuidof(IUnknown), &m_cookie));
        }
    }
To construct a
fake_
agile_
ref
from a smart pointer, we extract the raw pointer and check whether it is null. If so, then the smart pointer is empty, and we leave the
m_cookie
at zero. But if it is not null, we initialize the context information (so we can recognize this apartment later), and we register the COM object in the GIT to retain a reference to it for as long as the apartment is valid.
fake_agile_ref(fake_agile_ref&& other) noexcept :
        m_context(std::move(other.m_context)),
        m_token(std:exchange(other.m_token, 0)),
        m_git(std::move(other.m_git)),
        m_cookie(std::exchange(other.m_cookie, 0)),
        m_raw(other.m_raw)
    {
    }
Since we will have a nontrivial destructor, we need copy and move constructors per the Rule of Five. The move constructor merely steals all the content from the source and leaves the source in the empty state. We don’t need to create a copy constructor because the move constructor causes the implicitly-defined copy constructor to become deleted. (The fake agile reference is not copyable because we don’t know how to copy the cookie.)
fake_agile_ref& operator=(fake_agile_ref&& other) noexcept
    {
        using std::swap;
        swap(m_context, other.m_context);
        swap(m_token, other.m_token);
        swap(m_git, other.m_git);
        swap(m_cookie, other.m_cookie);
        swap(m_raw, other.m_raw);
    }
The fake agile reference also needs a move assignment operator to satisfy the Rule of Five. It just swaps the contents with the assigned-from object. Again, we don’t need a copy assignment operator because the declared move assignment operator causes the implicitly-defined copy assignment operator to become deleted.
bool empty() const noexcept
    {
        return m_cookie == 0;
    }

    explicit operator bool() const noexcept
    {
        return !empty();
    }
An explicit boolean conversion operator lets callers test the fake agile pointer to see whether it is empty.
~fake_agile_ref()
    {
        if (!empty()) {
            m_git->RevokeInterfaceFromGlobal(std::exchange(m_cookie, 0));
        }
    }
We have reached our nontrivial destructor: If we have a GIT cookie, we revoke it. It would have been nice to let this be a custom deleter of a
unique_ptr
, but a cookie is not a pointer, and
unique_ptr
works only with pointers.
[[nodiscard]] Smart get() const
    {
        if (empty()) {
            return nullptr;
        }
        if (m_token != get_context_token()) {
            throw winrt::hresult_error(CO_E_NOT_SUPPORTED);
        }

        Smart result{ nullptr };
        winrt::copy_from_abi(result, m_raw);
        return result;
    }
Here is where the excitement is. To recover the original COM object, we first check if the fake agile pointer is empty. If so, then there is no COM object to return. If the fake agile pointer is nonempty, but we are in the wrong apartment, then we throw the
CO_
E_
NOT_
SUPPORTED
exception which is the same thing that
Ro­Get­Agile­Reference
does.
Otherwise, we are in the correct context. Our cookie is keeping the original object alive, so we can just recover it from the raw pointer. (We could also redeem the cookie from the GIT, but this is faster.)
};
That ends the definition of
fake_
agile_
ref
, but we’re not done yet.
template<typename T> fake_agile_ref(winrt::com_ptr<T> const&)
    -> fake_agile_ref<T>;
template<typename T> fake_agile_ref(T const&)
    -> fake_agile_ref<T>;
These deduction guides allow class template argument deduction (CTAD) to deduce the
T
from the constructor parameter: If the constructor parameter is a
com_ptr<T>
, then the template type parameter is
T
. Otherwise, the template type parameter matches the constructor parameter, which we assume is a projected type.
We can now use this fake agile reference as a drop-in replacement for the normal agile reference in the case that the delegate is not marshalable.
template<typename Delegate>
std::remove_reference_t<Delegate> make_agile_delegate(Delegate&& d)
{
    if (d.try_as<::IAgileObject>()) {
        return d;
    }

    if (d.try_as<::INoMarshal>()) {
        return [agile =
fake_agile_ref
(d)](auto&&...args) {
            return agile.get()(std::forward<decltype(args)>(args)...);
        };
    }

    return [agile = winrt::agile_ref(d)](auto&&...args) {
        return agile.get()(std::forward<decltype(args)>(args)...);
    };
}
Unfortunately, when we take this out for a spin and give it a non-marshalable delegate, it fails at this line:
winrt::check_hresult(m_git->RegisterInterfaceInGlobal(
                static_cast<::IUnknown*>(m_raw), __uuidof(IUnknown), &m_cookie));
That’s because
Register­Interface­In­Global
will not register objects that deny marshalability.
Oh great, so we’re back to square one.
We’ll break the cycle of despair next time.
