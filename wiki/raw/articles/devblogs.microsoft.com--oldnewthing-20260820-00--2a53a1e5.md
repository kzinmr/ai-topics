---
title: "Reducing C++ template bloat by factoring out the type-dependent portions of the function"
url: "https://devblogs.microsoft.com/oldnewthing/20260820-00/?p=112629"
fetched_at: 2026-08-21T10:01:06.781423+00:00
source: "devblogs.microsoft.com/oldnewthing"
tags: [blog, raw]
---

# Reducing C++ template bloat by factoring out the type-dependent portions of the function

Source: https://devblogs.microsoft.com/oldnewthing/20260820-00/?p=112629

C++ templates let you reuse code, but it comes at a cost: Each template expansion results in a different function. This is not a big deal for small functions, but the less trivial your function becomes, the larger the cost of the repeated expansions.
This is particularly expensive for functions that accept lambdas because every lambda is a unique type, so each time you invoke the template function with a lambda you get a different template expansion.
Sometimes I see large template functions that have very few type dependencies.
template<typename Table>
void something(Database const& db)
{
    // extensive preparations
    auto statusIndicator = ⟦ calculate status indicator ⟧
    auto primaryTugboat = ⟦ calculate primary tugboat ⟧
    std::vector<Staircase> staircases;

    for (auto&& column : Table::Columns()) {
        ⟦ operate on each column using the stuff we prepared ⟧
        ⟦ maybe add things to the staircases and update the tugboat ⟧
    }

    ⟦ lots more code ⟧
}
In this extreme case, the only type dependency is the
Table::Columns()
. (A more common source of type dependencies would be method calls on a templated inbound parameter.)
This is a large function, and it will be re-expanded for each
Table
. Since each table has a different set of columns, and probably a different number of columns, there is no opportunity for COMDAT folding, so the different expansions will all be distinct.
One way to mitigate the explosion is to wrap all the common pieces into a helper object.
struct SomethingState {
    Database const& db;
    Indicator statusIndicator;
    Tugboat primaryTugboat;
    std::vector<Staircase> staircases;

    __declspec(noinline)
    SomethingState(Database const& db) : db(db)
    {
        statusIndicator = ⟦ calulate status indicator ⟧
        primaryTugboat = ⟦ calulate primary tugboat ⟧
    }

    __declspec(noinline)
    void ProcessColumn(Column const& column)
    {
        ⟦ operate on each column using the stuff we prepared ⟧
        ⟦ maybe add things to the staircases and update the tugboat ⟧
    }

    __declspec(noinline)
    void Finish()
    {
        ⟦ lots more code ⟧
    }
};

template<typename Table>
void something(Database const& db)
{
SomethingState state(db);
for (auto&& column : Table::Columns()) {
state.ProcessColumn(column);
}
state.Finish();
}
Now, the different expansions of the
something
function can share the
SomethingState
constructor and methods, so the unique functions are fairly small.
We mark the
SomethingState
constructor and methods as “no-inline” to discourage the compiler from inlining them, because inlining them would defeat our factoring.
Related
:
A noinline inline function? What sorcery is this
?
Another way to reduce the code explosion problem is to do the factoring the other way: Instead of factoring out the common logic and keeping the type-dependent stuff, we factor out the type-dependent stuff and keep the common logic.
The trick with this approach is finding some common type that all of the expansions share. I’ll assume that the
Table::Colums()
is a C-style array of
Column
objects, or a
std::vector
of
Column
objects, or a
std::array
of
Column
objects, or otherwise something that can produce a
std::span
of
Column
objects.
void somethingWorker(Database const& db,
std::span<Column> columns
)
{
    // extensive preparations
    auto statusIndicator = ⟦ calculate status indicator ⟧
    auto primaryTugboat = ⟦ calculate primary tugboat ⟧
    std::vector<Staircase> staircases;

    for (auto&& column :
columns
) {
        ⟦ operate on each column using the stuff we prepared ⟧
        ⟦ maybe add things to the staircases and update the tugboat ⟧
    }

    ⟦ lots more code ⟧
}

template<typename Table>
void something(Database const& db)
{
    somethingWorker(db,
Table::Columns()
);
}
We capture the columns ahead of time and then use the captured values to perform the enumeration inside a non-templated worker function. Since the worker function is non-templated, there is no template explosion when it is called by each
something<Table>
.
One thing to watch out for is that we are changing the order of evaluation, The old code didn’t call
Table::Columns()
until after the preparations were complete. You can look at the code to confirm, but I suspect that
Table::Columns()
just returns a reference to some pre-existing source of column information, so it doesn’t matter when you call it. Even if it returned the columns by value (say, by cloning an internal vector), retrieving the columns early does change the point at which that vector is generated, but generating it even if the preparatory steps fail is probably not a problem because (1) generating it has no interesting side effects, (2) the order of evaluation is not important, and (3) the failure case is probably rare, so the extra cost of generating a vector that is not used is inconsequential.
We’ll apply these principles to
our previous example
and make a surprising discovery that will shock and amaze you.
