---
title: "Creating a fake agile wrapper that is technically agile but is not useful outside its home apartment, part 5"
url: "https://devblogs.microsoft.com/oldnewthing/20260807-00/?p=112597"
fetched_at: 2026-08-08T10:13:47.347201+00:00
source: "devblogs.microsoft.com/oldnewthing"
tags: [blog, raw]
---

# Creating a fake agile wrapper that is technically agile but is not useful outside its home apartment, part 5

Source: https://devblogs.microsoft.com/oldnewthing/20260807-00/?p=112597

Last time, I confessed that
I lied when i said that we can’t use
std::
unique_ptr
to manage the registration cookie
.
The trick here is that the registration cookie is of type
DWORD
, which fits in a pointer, so we can smuggle the integer value inside a pointer.
template<typename T>
struct fake_agile_ref
{
private:
    using Smart = std::conditional_t<
        std::is_base_of_v<winrt::Windows::Foundation::IUnknown, T>,
        T, winrt::com_ptr<T>>;
struct git_deleter
{
winrt::com_ptr<IGlobalInterfaceTable> m_git;
void operator()(void* p)
{
m_git->RevokeInterfaceFromGlobal(static_cast<DWORD>(reinterpret_cast<uintptr_t>(p)));
}
};
winrt::com_ptr<IContextCallback> m_context;
    ULONG_PTR m_token = 0;
std::unique_ptr<void, git_deleter> m_cookie;
void* m_raw = nullptr;
Our custom deleter holds a pointer to the Global Interface Table and uses it to revoke the cookie on destruction. The cookie is an integer smuggled inside a pointer, so we cast the pointer back to an integer by passing through a
uintptr_t
to avoid a compiler warning about casting between an integer and pointer of different sizes.
We are relying on the fact that Windows implementations are required to support round-tripping integers through pointers. Macros like
MAKEINTRESOURCE
rely on it. It’s also codified in Windows with helper functions like
PtrToInt
and
IntToPtr
, but I’m writing it out for expository purposes rather than using those helpers.
We can then store the Global Interface Table pointer and the corresponding cookie in the
unique_ptr
:
fake_agile_ref(Smart const& p) : m_raw(winrt::get_abi(p))
    {
        if (m_raw) {
            m_context = winrt::capture<IContextCallback>(CoGetObjectContext);
            m_token = get_context_token();
auto& git = m_cookie.get_deleter().m_git;
git = winrt::create_instance<IGlobalInterfaceTable>(CLSID_StdGlobalInterfaceTable);
DWORD cookie;
winrt::check_hresult(
git
->RegisterInterfaceInGlobal(
                winrt::make<force_marshal<Smart>>(p).get(),
                __uuidof(IUnknown), &m_cookie));
m_cookie.reset(reinterpret_cast<void*>(static_cast<uintptr_t>(cookie)));
}
    }
And now that we are letting
unique_ptr
manage the lifetime of the cookie, we don’t need a custom destructor, which allows us to use the Rule of Zero and simply not have any copy or move constructors or assignment operators.
//
fake_agile_ref(fake_agile_ref&& other) noexcept :
//
m_context(std::move(other.m_context)),
//
m_token(std:exchange(other.m_token, 0)),
//
m_git(std::move(other.m_git)),
//
m_cookie(std::exchange(other.m_cookie, 0)),
//
m_raw(other.m_raw)
//
{
//
}
//
fake_agile_ref& operator=(fake_agile_ref&& other) noexcept
//
{
//
using std::swap;
//
swap(m_context, other.m_context);
//
swap(m_token, other.m_token);
//
swap(m_git, other.m_git);
//
swap(m_cookie, other.m_cookie);
//
swap(m_raw, other.m_raw);
//
}
//
~fake_agile_ref()
//
{
//
if (m_cookie) {
//
m_git->RevokeInterfaceFromGlobal(std::exchange(m_cookie, 0));
//
}
//
}
Since we are storing the cookie in a
unique_ptr
, we need to adjust the
empty
method:
bool empty() const noexcept
    {
        return
reinterpret_cast<uintptr_t>(m_cookie.get())
!= 0;
    }
Bonus chatter
: The Windows Implementation Library (wil) has a class similar to
unique_ptr
called
wil::unique_any
that lets you apply cleanup to any data type, not just a pointer.
