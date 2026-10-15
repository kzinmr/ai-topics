---
title: "One way of thinking about access specifiers in C++/WinRT implementation types"
url: "https://devblogs.microsoft.com/oldnewthing/20261009-00/?p=112764/"
fetched_at: 2026-10-12T10:10:59.566488+00:00
source: "devblogs.microsoft.com/oldnewthing"
tags: [blog, raw]
---

# One way of thinking about access specifiers in C++/WinRT implementation types

Source: https://devblogs.microsoft.com/oldnewthing/20261009-00/?p=112764/

In C++/WinRT, Windows Runtime classes are exposed to the outside world through the projection, but internally they are represented by their implementation type. Since the outside world sees only the projection, implementation types are visible only to the module that produced them.
This realization lets you reinterpret the C++ access specifiers for C++/WinRT implementation types.
Declared on
implementation as
C# and C++/CX
equivalent
Accessible to
implemented interface
public
Anyone
public
internal
Code in the same module
protected
protected
Code in derived classes
private
private
Code in the same class
In code:
struct Widget : winrt::implements<Widget, IStringable>
{
public:
    // This is a member of IStringable,
    // so it is accessible to anyone.
    winrt::hstring ToString();

    // This does not implement any member from IStringable,
    // so it is accessible to other code in the same module.
    void Recolor(winrt::Windows::UI::Color newColor);

protected:
    // Accessible to implementation classes that derive from Widget.
    void Reverse();

private:
    // Accessible only to Widget itself.
    void Reset();
};
Note that if you are implementing a runtime class, then C++/WinRT autogenerates a template for you that auto-declares all of the declared interfaces of that class.
// Widget.idl

namespace Contoso
{
    runtimeclass Widget : Windows.Foundation.IStringable
    {
        String Name{ get; };
        void Toggle();
    }
}
The IDL compiler autogenerates an interface
IWidget
with a property
Name
and a method
Toggle()
.
// implementation
namespace winrt::Contoso
{
    struct Widget :
WidgetT<Widget>
{
        ⟦ ... ⟧
    };
}
The
WidgetT<Widget>
expands to
implements<Widget, IWidget, Windows::Foundation::IStringable>
because those are the interfaces declared by the IDL file.
