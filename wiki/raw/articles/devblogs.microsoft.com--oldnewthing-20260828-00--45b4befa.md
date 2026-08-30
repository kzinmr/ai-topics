---
title: "On forcing all derived classes to implement a specific non-virtual method, part 2"
url: "https://devblogs.microsoft.com/oldnewthing/20260828-00/?p=112654"
fetched_at: 2026-08-29T10:01:01.740682+00:00
source: "devblogs.microsoft.com/oldnewthing"
tags: [blog, raw]
---

# On forcing all derived classes to implement a specific non-virtual method, part 2

Source: https://devblogs.microsoft.com/oldnewthing/20260828-00/?p=112654

Last time, we observed that
one way to force all derived classes to implement a specific non-virtual method is simply not to implement it in the base class
and sit back and wait for the compile-time fireworks. I noted that we can do better than this, though.
The problem is that the compiler tells you what is wrong, but the details are often buried in the “supplementary error information”, and it may not be obvious how to dig it out, or maybe you dig it out but you don’t understand how to fix it.
You can steer people to the correct error by implementing the method as deleted.
// C++/WRL

struct OneWayConverter
{
    // Derived classes must implement Convert()
    HRESULT STDMETHODCALLTYPE Convert(IInspectable* value,
        ABI::Windows::UI::Xaml::Interop::TypeName targetType,
        IInspectable* parameter, HSTRING language,
        IInspectable** result)
= delete
;

    // One-way converters cannot convert back
    HRESULT STDMETHODCALLTYPE ConvertBack(IInspectable* /*value*/,
        ABI::Windows::UI::Xaml::Interop::TypeName /*targetType*/,
        IInspectable* /*parameter*/, HSTRING /*language*/,
        IInspectable** result)
    {
        *result = nullptr;
        return E_NOTIMPL;
    }
};

// C++/WinRT

struct OneWayConverter
{
    // Derived classes must implement Convert()
    winrt::Windows::Foundation::IInspectable
        Convert(
            winrt::Windows::Foundation::IInspectable const& /*value*/,
            winrt::Windows::UI::Xaml::Interop::TypeName const& /*targetType*/,
            winrt::Windows::Foundation::IInspectable const& /*parameter*/,
            winrt::hstring const& /*language*/)
= delete
;

    // One-way converters cannot convert back
    winrt::Windows::Foundation::IInspectable
        ConvertBack(
            winrt::Windows::Foundation::IInspectable const& /*value*/,
            winrt::Windows::UI::Xaml::Interop::TypeName const& /*targetType*/,
            winrt::Windows::Foundation::IInspectable const& /*parameter*/,
            winrt::hstring const& /*language*/)
    {
        throw winrt::hresult_not_implemented();
    }
};

// Plain C++ analogous scenario

struct OneWayConverter
{
    // Derived classes must implement Convert()
    Color Convert(Widget const&amp /*value*/)
= delete
;

    // One-way converters cannot convert back
    Widget ConvertBack(Color const& /*color*/)
    {
        throw std::exception("not implemented");
    }
};
This has a few benefits.
One is that the developer can see the exact function signature that they need to implement: It’s the one that got deleted in the base class.
Another is that the error message takes them to the deleted function, and if they go to that line of code, they will see the comment that explains why it is deleted.
winrt\windows.ui.xaml.data.h(1469,90): error C2280: 'winrt::
Windows::
Foundation::
IInspectable OneWayConverter::
Convert(
const winrt::
Windows::
Foundation::
IInspectable &,
const winrt::
Windows::
UI::
Xaml::
Interop::
TypeName &,
const winrt::
Windows::
Foundation::
IInspectable &,
const winrt::
hstring &)': attempting to reference a deleted function
      see declaration of 'OneWayConverter::Convert'
      test.cpp(60,9):
      'winrt::
Windows::
Foundation::
IInspectable OneWayConverter::
Convert(
const winrt::
Windows::
Foundation::
IInspectable &,const winrt::
Windows::
UI::
Xaml::
Interop::
TypeName &,const winrt::
Windows::
Foundation::
IInspectable &,
const winrt::
hstring &)':
function was explicitly deleted
⟦ other error message spew the same as before ⟧
Starting in C++26, you can do even better yet: You can put a custom message directly in the
delete
!
struct OneWayConverter
{
    // Derived classes must implement Convert()
    winrt::Windows::Foundation::IInspectable
        Convert(
            winrt::Windows::Foundation::IInspectable const& /*value*/,
            winrt::Windows::UI::Xaml::Interop::TypeName const& /*targetType*/,
            winrt::Windows::Foundation::IInspectable const& /*parameter*/,
            winrt::hstring const& /*language*/)
        = delete
("If you derive from OneWayConverter, you must implement Convert()")
;

    // One-way converters cannot convert back
    winrt::Windows::Foundation::IInspectable
        ConvertBack(
            winrt::Windows::Foundation::IInspectable const& /*value*/,
            winrt::Windows::UI::Xaml::Interop::TypeName const& /*targetType*/,
            winrt::Windows::Foundation::IInspectable const& /*parameter*/,
            winrt::hstring const& /*language*/)
    {
        throw winrt::hresult_not_implemented();
    }
};
The Microsoft Visual C++ compiler doesn’t support this feature yet, but other compilers do, and they include the custom message in the primary error text.
// clang
error: attempt to use a deleted function:
If you derive from OneWayConverter, you must implement Convert()
// gcc
error: use of deleted function 'winrt::
Windows::
Foundation::
IInspectable OneWayConverter::
Convert(
winrt::
Windows::
Foundation::
IInspectable const&,
winrt::
Windows::
UI::
Xaml::
Interop::
TypeName const&,
winrt::
Windows::
Foundation::
IInspectable const&,
winrt::
hstring const&)':
If you derive from OneWayConverter, you must implement Convert()
While this works for C++/WinRT and plain C++, it doesn’t work for C++/WRL because WRL derives from the abstract base class, and you cannot delete a method implemented by a base class. (Presumably because the method is still callable by casting to the base class.)
So the
delete
trick works only if your declaration is not an override of a base class declaration.
Tweaking the implementation to provide better compiler error messages is another example of
compiler error message metaprogramming
, which is one of the under-appreciated aspects of authoring a code library.
