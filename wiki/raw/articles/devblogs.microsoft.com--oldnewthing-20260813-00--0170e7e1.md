---
title: "A little helper class for managing LPPROC_THREAD_ATTRIBUTE_LISTs"
url: "https://devblogs.microsoft.com/oldnewthing/20260813-00/?p=112611"
fetched_at: 2026-08-14T10:21:53.208766+00:00
source: "devblogs.microsoft.com/oldnewthing"
tags: [blog, raw]
---

# A little helper class for managing LPPROC_THREAD_ATTRIBUTE_LISTs

Source: https://devblogs.microsoft.com/oldnewthing/20260813-00/?p=112611

The
LPPROC_
THREAD_
ATTRIBUTE_
LIST
is a bit annoying to manage. You have to allocate memory for it yourself, but you don’t know how much; you have to ask
Initialize­Proc­Thread­Attribute­List
. And then when you’re done, you have to call
Delete­Proc­Thread­Attribute­List
before freeing the memory.
We suffered through this when
we controlled which handles are inherited by a new process
.
I wrote a helper function
to try to make it easier, by taking the attributes as a separate parameter beyond the parameters to
Create­Process
but I’m not sure if it was entirely successful.
Here’s another try, this time building on the Windows Implementation Library.
namespace details
{
    inline void FreeProcThreadAttributeList(
        _Pre_valid_ _Frees_ptr_ LPPROC_THREAD_ATTRIBUTE_LIST list)
    {
        ::DeleteProcThreadAttributeList(list);
        ::HeapFree(::GetProcessHeap(), 0, list);
    }
};

using unique_proc_thread_attribute_list = wil::unique_any<LPPROC_THREAD_ATTRIBUTE_LIST,
    decltype(&details::FreeProcThreadAttributeList), details::FreeProcThreadAttributeList>;

HRESULT make_proc_thread_attribute_list_nothrow(
    DWORD attributeCount, _Out_ LPPROC_THREAD_ATTRIBUTE_LIST* result)
{
    *result = nullptr;
    SIZE_T size = 0;
    InitializeProcThreadAttributeList(nullptr, attributeCount, 0, &size);
    auto p = wil::unique_process_heap_ptr<std::remove_pointer_t<LPPROC_THREAD_ATTRIBUTE_LIST>>(
        static_cast<LPPROC_THREAD_ATTRIBUTE_LIST>(::HeapAlloc(::GetProcessHeap(), 0, size)));
    RETURN_IF_NULL_ALLOC(p);
    RETURN_IF_WIN32_BOOL_FALSE(InitializeProcThreadAttributeList(p.get(), attributeCount, 0, &size));
    *result = p.release();
    return S_OK;
}

unique_proc_thread_attribute_list make_proc_thread_attribute_list(DWORD attributeCount)
{
    unique_proc_thread_attribute_list result;
    THROW_IF_FAILED(make_proc_thread_attribute_list_nothrow(attributeCount, result.put()));
    return result;
}
We start by declaring a helper function that cleans up an
LPPROC_
THREAD_
ATTRIBUTE_
LIST
by deleting the contents, and then freeing the buffer. We use that to define a
unique_
proc_
thread_
attribute_
list
which holds a heap-allocated pointer that has been initialized as a
LPPROC_
THREAD_
ATTRIBUTE_
LIST
.
The first helper function is the nonthrowing version: it asks for the required size of a
LPPROC_
THREAD_
ATTRIBUTE_
LIST
for the specified number of attributes, then allocates that much memory on the heap, storing it in a
unique_
process_
heap_
ptr
so that it will be freed if we fail to initialize it. Declaring that
unique_
process_
heap_
ptr
is a bit of a pain because we want it to be a “unique pointer to whatever it is that
LPPROC_
THREAD_
ATTRIBUTE_
LIST
points to.” It’s also annoying that we have to repeat ourselves in both the template type parameter as well as in the cast of the heap-allocated pointer, because CTAD doesn’t work here.
After we allocate the memory, we try to initialize it. If that fails (and I can’t imagine why), we propagate the error, and the RAII type frees the (uninitialized) heap memory.
If initialization succeeds, we return the pointer to the caller, who now takes responsibility for freeing it.
Note that the temporary holding place has to be a
unique_
process_
heap_
ptr
and not a
unique_
proc_
thread_
attribute_
list
: If the initialization fails, we must not call
Delete­Proc­Thread­Attribute­List
, so we have to hold the heap pointer in something that won’t try to call
Delete­Proc­Thread­Attribute­List
.
We can easily use the nonthrowing version to build a throwing version.
My next idea was to let you pass the attributes you want to pre-fill into the attribute list.
struct proc_thread_attribute {
   template<typename T = void>
   proc_thread_attribute(DWORD_PTR attribute, T* value, SIZE_T size = sizeof(T)) :
      attribute(attribute), value(value), size(size) {
   }

   DWORD_PTR attribute;
   PVOID value;
   SIZE_T size;
};

template<typename C>
HRESULT update_proc_thread_attribute_list_nothrow(
    LPPROC_THREAD_ATTRIBUTE_LIST list, C&& attributes)
{
    for (auto&& attribute : attributes) {
        RETURN_IF_WIN32_BOOL_FALSE(
            UpdateProcThreadAttribute(list, 0, attribute.attribute,
                attribute.value, attribute.size, nullptr, nullptr));
    }
    return S_OK;
}

template<typename C>
void update_proc_thread_attribute_list(
    LPPROC_THREAD_ATTRIBUTE_LIST list, C&& attributes)
{
    THROW_IF_FAILED(update_proc_thread_attribute_list_nothrow(
        list, std::forward<C>(attributes)));
}
The container parameter can be anything iterable whose value type has
attribute
,
value
, and
size
members. It’s probably a collection of
proc_
thread_
attribute
s, but it doesn’t have to be. (Maybe it’s a collection of things derived from
proc_
thread_
attribute
.)
We can add this to our
make_
proc_
thread_
attribute_
list
function so that callers can pass in a list of attributes they want, and we’ll make a list that holds them all. And as an extra bonus, you can request room for additional attributes beyond those in the collection you passed in. For example, you might have some attributes that you always use, and then some others you decide on dynamically.
// No changes to this function
HRESULT make_proc_thread_attribute_list_nothrow(
    DWORD attributeCount, _Out_ LPPROC_THREAD_ATTRIBUTE_LIST* result)
{
    *result = nullptr;
    SIZE_T size = 0;
    InitializeProcThreadAttributeList(nullptr, attributeCount, 0, &size);
    auto p = wil::unique_process_heap_ptr<std::remove_pointer_t<LPPROC_THREAD_ATTRIBUTE_LIST>>(
        static_cast<LPPROC_THREAD_ATTRIBUTE_LIST>(::HeapAlloc(::GetProcessHeap(), 0, size)));
    RETURN_IF_NULL_ALLOC(p);
    RETURN_IF_WIN32_BOOL_FALSE(InitializeProcThreadAttributeList(p.get(), attributeCount, 0, &size));
    *result = p.release();
    return S_OK;
}

// New overload that takes a list of attributes to preload,
// with room for any additional attributes you want to add later.

template<typename C>
HRESULT make_proc_thread_attribute_list_nothrow(
    C&& attributes, DWORD extraAttributeCount,
    _Out_ LPPROC_THREAD_ATTRIBUTE_LIST* result)
{
    *result = nullptr;
    unique_proc_thread_attribute_list list;
    RETURN_IF_FAILED(make_proc_thread_attribute_list_nothrow(
        static_cast<DWORD>(attributes.size()) + extraAttributeCount,
        list.put()));
    RETURN_IF_FAILED(update_proc_thread_attribute_list_nothrow(
        list.get(), std::forward<C>(attributes)));

    *result = list.release();
    return S_OK;
}

// New overload that takes a list of attributes to preload,
// with no room for more.

template<typename C>
std::enable_if_t<!std::is_integral_v<C>, HRESULT>
    make_proc_thread_attribute_list_nothrow(
        C&& attributes,
        _Out_ LPPROC_THREAD_ATTRIBUTE_LIST* result)
{
    return make_proc_thread_attribute_list_nothrow(
        std::forward<C>(attributes), 0, result);
}
Note that without the
std::enable_if_t
on the third overload, we would have an ambiguity if somebody called
make_
proc_
thread_
attribute_
list_
nothrow(1, p)
because the parameter
1
would satisfy both the
DWORD
parameter from the first overload as well as matching the third overload with
C = int
. To force the third one to be rejected, we use SFINAE to make the return type a substitution failure if the parameter is integral.
We can then build a throwing version out of the nonthrowing version.
unique_proc_thread_attribute_list
    make_proc_thread_attribute_list(DWORD attributeCount)
{
    unique_proc_thread_attribute_list result;
    THROW_IF_FAILED(make_proc_thread_attribute_list_nothrow(
        attributeCount, result.put()));
    return result;
}

template<typename C = std::initializer_list<proc_thread_attribute>>
std::enable_if_t<!std::is_integral_v<C>, unique_proc_thread_attribute_list>
    make_proc_thread_attribute_list(
        C&& attributes, DWORD extraAttributeCount = 0)
{
    unique_proc_thread_attribute_list result;
    THROW_IF_FAILED(make_proc_thread_attribute_list_nothrow(
        std::forward<C>(attributes), extraAttributeCount,
        result.put()));
    return result;
}
We use a defaulted parameter to collapse the “collection initializer” and “collection initializer with additional space” overloads into one. We still need to use SFINAE to avoid an ambiguity that tries to treat a sole integer parameter as a collection.
You can use this to build process/thread attribute lists at one go.
HANDLE handles[2] = { handle1, handle2 };
DWORD protection = PROTECTION_LEVEL_SAME;
auto list = make_proc_thread_attribute_list({
    { PROC_THREAD_ATTRIBUTE_HANDLE_LIST, &handles, sizeof(handles) },
    { PROC_THREAD_ATTRIBUTE_PROTECTION_LEVEL, &protection, sizeof(protection) },
});
Or you can build it up with some premade attributes, and others that you add conditionally:
HANDLE handles[2] = { handle1, handle2 };
DWORD protection = PROTECTION_LEVEL_SAME;
auto list = make_proc_thread_attribute_list({
    { PROC_THREAD_ATTRIBUTE_HANDLE_LIST, &handles, sizeof(handles) },
    { PROC_THREAD_ATTRIBUTE_PROTECTION_LEVEL, &protection, sizeof(protection) },
}, 1); // "1" leaves room for one more attribute
if (job != nullptr) {
    UpdateProcThreadAttribute(list.get(),
        PROC_THREAD_ATTRIBUTE_JOB_LIST,
        &job, sizeof(job), nullptr, nullptr);
}
