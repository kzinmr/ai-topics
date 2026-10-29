---
title: "C++/WinRT overcorrection: Using make_self and immediately converting it to the projected interface"
url: "https://devblogs.microsoft.com/oldnewthing/20261028-00/?p=112803/"
fetched_at: 2026-10-29T10:01:27.458291+00:00
source: "devblogs.microsoft.com/oldnewthing"
tags: [blog, raw]
---

# C++/WinRT overcorrection: Using make_self and immediately converting it to the projected interface

Source: https://devblogs.microsoft.com/oldnewthing/20261028-00/?p=112803/

In C++/WinRT, there are two ways of creating objects that you yourself implement.
For the purpose of this discussion, let
Impl
be the class you wrote that implements a Windows Runtime object. If you are implementing something that was declared in an IDL file, it will be the
winrt::
Namespace::
implementation::
ClassName
for the instance object or it will be the
winrt::
Namespace::
factory_
implementation::
ClassName
for the factory object. If it wasn’t declared in an IDL file, then it is the class that you manually derived from
winrt::
implements
.
One way to create the object is to use
make<Impl>
, which creates the implementation object and then returns the Windows Runtime projection version of that object. (If
Impl
is manually-derived from
winrt::
implements
, the projection is the first implemented interface.)
From that Windows Runtime projection, you can regain access to the implementation object by doing
get_self<Impl>(projected)
, if you want to access things in the implementation object that aren’t exposed in the projection.
Alternatively, you use
make_self<Impl>
, which creates the object but returns a
winrt::
com_ptr<Impl>
instead of a projection. You can then access things in the implementation object from that
winrt::
com_ptr
, and convert it to the projected type with the
*
operator.
make
make_self
↓
↓
projection
get_self
→
implementation
←
operator*
Which one you choose depends on where you want to go first.
If you are first going to access
non-projected public members of the implementation class
, use the
->
operator on the
com_ptr<Impl>
. For example, you might want to set up the object before returning the projection.
winrt::IVector<winrt::Widget>
    MakeWidgets(int style, int count)
{
    std::vector<winrt::Widget> v(count, nullptr);
    std::generate(v.begin(), v.end(), [&] {
auto widget = winrt::make_self<implementation::Widget>(style);
widget->Enabled(true);
return *widget;
    });
    return winrt::multi_threaded_vector(std::move(v));
}
But if you are just going to use the projection, you can take the direct route instead of going the long way.
// The long way

winrt::IVector<winrt::Widget>
    MakeWidgets(int style, int count)
{
    std::vector<winrt::Widget> v(count, nullptr);
    std::generate(v.begin(), v.end(), [&] {
auto widget = winrt::make_self<implementation::Widget>(style);
return *widget;
    });
    return winrt::multi_threaded_vector(std::move(v));
}
make_self
↓
projection
←
operator*
implementation
↓
returned
In this case, you don’t need to pass through the implementation type.
// The short way

winrt::IVector<winrt::Widget>
    MakeWidgets(int style, int count)
{
    std::vector<winrt::Widget> v(count, nullptr);
    std::generate(v.begin(), v.end(), [&] {
        return winrt::make_self<implementation::Widget>(style);
    });
    return winrt::multi_threaded_vector(std::move(v));
}
make
↓
projection
↓
return
My guess is that the people who go the long way don’t realize that there are two ways. They learned only one way and just rely on it even if there’s a shorter way.
