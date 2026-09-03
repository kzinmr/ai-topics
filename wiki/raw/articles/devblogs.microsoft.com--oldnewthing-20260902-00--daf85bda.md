---
title: "The perils of binding to value types in XAML"
url: "https://devblogs.microsoft.com/oldnewthing/20260902-00/?p=112668"
fetched_at: 2026-09-03T10:00:50.325623+00:00
source: "devblogs.microsoft.com/oldnewthing"
tags: [blog, raw]
---

# The perils of binding to value types in XAML

Source: https://devblogs.microsoft.com/oldnewthing/20260902-00/?p=112668

A colleague ran into trouble with their XAML program. They were using a
FlipView
control to bind to a collection, but when the user tried to navigate the
FlipView
using an assistive technology tool, there were cases where the navigation failed.
Some time later, they came back with the solution to the mystery.
The team noticed that their data model consisted only of strings and other value types, so they decided to declare their data model as a
struct
rather than a full
runtimeclass
, thereby avoiding a lot of boilerplate typing.
If defined as a
runtimeclass
:
// MyComponent.idl
runtimeclass MyPageContent
{
    String Title { get; };
    String Description { get; };
    String LinkUri { get; };
    Boolean IsNew{ get; };
}

// MyPageContent.h

namespace winrt::MyComponent
{
    struct MyPageContent : implements<MyPageContent>
    {
        MyPageContent(hstring const& title,
                    hstring const& description,
                    hstring const& link,
                    bool isNew) :
            m_title(title),
            m_description(description),
            m_link(link),
            m_isNew(isNew) {}

        hstring Title() const { return m_title; }
        hstring Description() const { return m_description; }
        hstring Link() const { return m_link; }
        bool IsNew() const { return m_isNew; }

    private:
        hstring m_title;
        hstring m_description;
        Windows::Foundation::Uri m_link;
        bool m_isNew;
    };
}

// Consumer.cpp

m_pages.Append(winrt::make<MyPageContent>(
                    title, description, link, isNew));
But if you define it as a
struct
, then most of this code isn’t necessary:
// MyComponent.idl
struct
MyPageContent
{
    String Title;
    String Description;
    String Link;
    Boolean IsNew;
}

//
MyPageContent.h
not needed

// Consumer.cpp

m_pages.Append(MyPageContent(title, description, link, isNew));
Tastes great, less filling
.
Now, the thing that makes value types value types is that they are copy-by-value, not copy-by-reference. This means that when XAML calls
GetAt(n)
on the
m_pages
to get the
n
th item, it gets a
copy
of the
MyPageContent
and binds to the copy.
And that’s the source of the problem.
When the code wants to navigate to a specific item at the request of the assistive technology tool, it passes the
MyPageContent
to navigate to, but that’s just another copy because value types are always passed by copy. XAML says, “I don’t have that guy” and fails the navigation. (XAML doesn’t realize that it has a guy who
looks just like
that guy. Not that it matters, because it’s not the same guy.)
The clever shortcut turned out to be the problem.
Now, while it’s true that there’s a bunch of typing needed to implement a C++/WinRT runtime class, there are helpers to reduce the amount of typing required. In the Windows Implementation Library (wil), the
cppwinrt_authoring.h
header contains classes to simplify the implementation of events and properties. It exploits CRTP
in the same way I discussed some time ago
.
// MyPageContent.h

namespace winrt::MyComponent
{
    struct MyPageContent : implements<MyPageContent>
    {
        MyPageContent(hstring const& title,
                    hstring const& description,
                    hstring const& link,
                    bool isNew) :
            m_title(title),
            m_description(description),
            m_link(link),
            m_isNew(isNew) {}
wil::single_threaded_property<hstring> Title;
wil::single_threaded_property<hstring> Description;
wil::single_threaded_property<hstring> Link;
wil::single_threaded_property<bool> IsNew;
};
}
We can get away with using a
single_
threaded_
property
because the properties are written only at construction, so concurrent reads are not going to cause problems.
