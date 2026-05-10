---
title: "Why is building a UI in Rust so hard?"
source: "Warp Blog"
url: "https://www.warp.dev/blog/why-is-building-a-ui-in-rust-so-hard"
scraped: "2026-05-10T01:28:26.604398+00:00"
lastmod: "2026-04-24T14:40:05.000Z"
type: "sitemap"
---

# Why is building a UI in Rust so hard?

**Source**: [https://www.warp.dev/blog/why-is-building-a-ui-in-rust-so-hard](https://www.warp.dev/blog/why-is-building-a-ui-in-rust-so-hard)

Engineering
Why is building a UI in Rust so hard?
Aloke Desai
February 14, 2023
What Makes Rust Unique?
Why is UI in Rust So Hard?
Functional UI to the Rescue
If you’ve read Hacker News recently, it’s hard to not think that Rust is the future: it’s being used in the
Linux kernel
and in the
Android
OS, by
AWS
for critical infrastructure, and in
ChromeOS
and
Firefox
. However, as wonderful as Rust is–it has yet to take off as a general language for building UI. In 2019, “GUI” was the
6th most highly requested feature
that was preventing adoption of Rust. This is fundamentally a limitation in Rust: the design of the language itself makes modeling common approaches to building UI difficult.
At
Warp
, we’ve been building a custom UI framework
1
in Rust that we use to render on the GPU. Building this framework has been very tricky and was a big investment, but it has served us well in building a terminal that has rich UI elements and is
as fast as any other terminal
on the planet. This level of performance would have been virtually impossible had we used a UI library like Electron or Flutter.
In this post, I’ll discuss why Rust’s unique memory management model and lack of inheritance makes traditional techniques to build a UI framework difficult and a few of the ways we’ve been working around it. I believe one of these approaches, or some combination of them, will ultimately lead to a stable cross-platform UI toolkit for high-performance UI rendering that everyone can use.
What Makes Rust Unique?
Rust handles memory management through a concept called “ownership” that is enforced at compilation time. This differs from other languages that offer automatic memory management through the use of a
garbage collector
) to remove unused objects at runtime.
Rust ownership works by enforcing the following rules:
Values are owned by variables
Values can be
referenced
by other variables (with some caveats mentioned below)
When the owning variables go out of scope, the memory the value is occupying is deallocated
Rust
fn main() {
    let mut original_owner = format!("Hello world");
    
    // move occurs to new owner    
    let new_owner = original_owner;
    
    // attempt to use original_owner will 
    // lead to compile time error    
    println!("{}", original_owner)
}
error[E0382]: borrow of moved value: `original_owner`
Taking the example above, the Rust compiler enforces that there is only a single owner of
a given value at any given time. Rust prevents us from assigning
new_owner
to the
value of
original_owner
, because there would be two owners of the value at the same
time.
Rust also protects against data races at compile time through rules on when a value can be referenced mutably and immutably. In tandem, these rules enforce that there are no data races caused by two threads updating the same value at the same time:
At any given time, you can have either one mutable reference or any number of immutable references.
References must always be valid.
The value can not be mutated while there are valid references.
Source: https://rufflewind.com/2017-02-15/rust-move-copy-borrow
Rust is also not an object oriented language like Java, C++, or Javascript–it does not support class inheritance or abstract classes. This was an intentional design decision: Rust is designed for
composition over inheritance
.
Thankfully, it’s still possible to achieve polymorphism in Rust with the use of
traits
(Rust’s versions of an interface) and trait objects.
Let’s say we wanted to build a UI library
2
that draws different UI components (such as a
Button
,
Text
and
Image
) onto a screen. In a traditional OOP language you would probably do this by starting
with a base
Component
class with a
draw
method. Each of these
components would inherit from the base
Component
class, and
we would use the common
draw
method to draw each component onto the screen.
In Rust, we can achieve something very simple with the use of a trait and a trait object.
We can add a common trait called Draw to our library:
Rust
pub trait Draw {
    fn draw(&self);
}
Components in our UI framework would all implement this trait and define their own logic for drawing the contents of the component onto the screen.
To render all of the components onto the screen, we want to be able to reference all the components in an abstract way that is agnostic of the type of component.
In Rust, we would do this using a trait object (
Box
):
Rust
pub struct Screen {
    pub components: Vec<Box<dyn Draw>>,
}
The key piece here is that we can reference our list of components
as a vector of type
Box
--any object that implements the
Draw
trait.
We have to use a
Box
(a pointer to an object on the heap) here because
we don’t know the size of the actual object that implements Draw at
compile time. This lets us interact with these components using the functions
on the trait (in this case
draw
) without knowing the type of each object. In our
case, we can call
draw
on each component to actually paint the screen:
Rust
impl Screen {
    pub fn run(&self) {
        for component in self.components.iter() {
            component.draw();
        }
    }
}
This approach works as an adequate solution to achieve polymorphism without inheritance. However, it doesn’t give us all of the features of OOP or inheritance generally: we can’t define a common class and extend its functionality while continuing to reference the fields or methods of the base class.
Traits just define a set of common functionality (a list of functions),
but don’t specify any of the data defined within each
implementation of the trait. In this case, there’s nothing
stopping us from implementing the
Draw
trait on a random
object that has nothing to do with a UI component. For example, we
could implement it on this random struct named Foo that definitely
isn’t a valid UI component:
Rust
struct Foo;

impl Draw for Foo {
    fn draw(&self) {}
}
Why is UI in Rust So Hard?
Pretty much all UI can be modeled as a tree–or more abstractly as a graph. A tree is a natural way to model UI: it makes it easy to compose different components together to build something that is visually complicated. It’s also been one of most common ways to model UI programming since at least the existence of HTML, if not earlier.
UI in Rust is difficult because it's hard to share data across this component tree without inheritance. Additionally, in a normal UI framework there are all sorts of spots where you need to mutate the element tree, but because of Rust’s mutability rules, this "alter the tree however you want" approach doesn't work.
In most UI frameworks, the concept of a component tree is built into the framework. The framework holds the root component and each component inherits from a common base component that keeps track of all of its children and how to traverse the children. Traversing the tree is critical for event handling: the framework needs to be able to walk the tree to determine which component(s) should receive an event. An example of this is event bubbling and capturing in the DOM API: with event bubbling (the default) events are handled by the deepest component in the tree and then “bubbled” up to parent elements.
A framework that does this well is Flutter–there’s a
Widget
abstract class–and additional abstract classes that
extend from
Widget
for the cases where a widget has
no children (
LeafRenderObjectElement
), one
child (
SingleChildRenderObjectElement
) and many
children (
MultiChildRenderObjectElement
). These extra layers of inheritance
ensure that leaf components don’t need to deal with any logic
around walking a component tree since
it’s all handled by a superclass.
Let’s use a timer, one of the tasks from
7GUIs
, as an example of how this tree structure would be useful. Our timer will have a progress bar to show the elapsed time, a slider to adjust the duration, and a button to reset the timer.
We can model this tree like so:
This tree approach does not map cleanly to Rust. The lack of OOP makes it harder to design a component that can have
n
number of children like in the structure above. Using our trait example from above, it’s not as simple as adding an additional function to our trait:
Rust
pub trait Draw {
    fn draw(&self);

    fn children(&self) -> Vec<Box<dyn Draw>>;
}
Since traits don’t hold data, this requires each component to individually store its children. Since we’ve just added on a
children
function–there’s nothing stopping a poorly-written component from returning an empty vector here even though the component stores, and draws, multiple components. These inconsistencies make it much harder to walk the tree–in an object-oriented language all of this logic would be abstracted away into a super class that could walk the tree using the source-of-truth of any of its children (the field itself).
Rust’s constraints around mutability here also makes trees hard to model if you want to be able to mutate the tree (which is a must since we’ll need to add and remove components as well as mutate the actual components themselves). Rust’s rules that prevent multiple mutable references to a single value discourages the use of shared mutable state–but that is often necessary in a tree where the tree owns and mutates the nodes but other app logic also needs to mutate each node in the tree.
Dealing with shared mutable state is also an issue when handling events. Most UI frameworks handle user interactions through the use of an event loop that polls for input. The framework can mutate any number of components at any time upon receiving an event.
There are ways to workaround with shared mutable state in Rust, but it produces non-ergonomic code that defers many of these checks to runtime.
A common solution to this is to use
interior mutability
using the
RefCell
type that is provided in the Rust standard library.
RefCell
works by moving Rust ownership checks to runtime instead of compile time. To get a mutable reference to an object, you can call
borrow\_mut
:
Rust
pub fn borrow_mut(&self) -> RefMut<'_, T>
If there is already an existing mutable reference to the underlying object–
borrow_mut
will panic to ensure that ownership guarantees aren’t violated.
Using
RefCell
mostly works, but is by no means ergonomic. It also has safety concerns–by deferring ownership checks to runtime the app can panic if there are ever two calls to
borrow_mut
.
Functional UI to the Rescue
Now that we have enough context on some of the difficulties with building a UI framework in Rust, let’s quickly touch on some approaches that have worked well in Rust.
The short answer is that there are many different solutions to these problems, which is why the UI landscape in Rust
is so fractured
and there isn’t a clear one-size-fits-all UI framework solution in Rust.
One of the most common solutions to these issues in Rust is to avoid using these object oriented patterns at all. Even though most UI frameworks were designed for Object-Oriented Programming, UI programming does not inherently need to be object oriented.
A good example of this is the
Elm architecture
, which makes heavy use of functional, reactive programming.
Iced
is the most popular Rust framework inspired by this architecture. This architecture separates the UI program into three high-level components: a Model type, a
view
function, and an
update
function.
The model is a simple dumb-data-object that holds all of the state for the view. At render time,
view
is responsible for converting the model into something that is displayed on the screen (in this case, by outputting HTML).
update
is responsible for mutating the model using programmer-defined
Msg
s . When a user interacts with the app, the programmer specifies which
Msg
should be used to update the model. The framework knows it needs to re-render (by calling
view
) since the Model has changed.
The Elm model works very well in Rust for a few reasons:
Functional and immutable:
there’s no need to deal with mutability issues since everything flows through
update
, where you take an owned value to a model and return a new owned value of the model. This maps well to Rust’s ownership model since there is a single owner of the Model.
Messages can be cleanly expressed with Rust enums:
Rust has very expressive enum support, which lets you model messages with different data types very easily. This ends up producing clear and declarative code where you can pattern match on each variant.
A good example how cleanly messages can be mapped to Rust enums is
iced’s
example for a numeric input where a user can either specify a number using an input or increment and decrement the number using buttons.
Messages can be defined as:
Rust
#[derive(Debug, Clone)]
pub enum Event {
    InputChanged(String),
    IncrementPressed,
    DecrementPressed,
}
And we would derive
update
as follows:
Rust
fn update(
    &mut self,
    _state: &mut Self::State,
    event: Event,
) -> Option<Message> {
    match event {
        Event::IncrementPressed => Some((self.on_change)(Some(
            self.value.unwrap_or_default().saturating_add(1),
        ))),
        Event::DecrementPressed => Some((self.on_change)(Some(
            self.value.unwrap_or_default().saturating_sub(1),
        ))),
        Event::InputChanged(value) => {
            if value.is_empty() {
                Some((self.on_change)(None))
            } else {
                value
                    .parse()
                    .ok()
                    .map(Some)
                    .map(self.on_change.as_ref())
            }
        }
    }
}
If Elm reminds you of Redux, then you are on the right path. Redux was inspired by Elm–you can think of
Redux resolvers
as analogous to updaters in Elm.
This architecture does have some downsides: componentizing components is not as intuitive as it is in other frameworks. In fact, the Elm docs
explicitly discourage
componentizing. Instead of creating new components that have their own Model, Elm encourages adding helper view and update functions that take in specific parameters from the model. For example, you could add a
header_view
function that takes specific parameters needed to render a header. This approach works just fine, but is not as intuitive as componentizing based on the visual structure of your application like you would in React or Flutter.
An Elm-like approach is by no means the only approach that seems to be getting traction. An Entity-Component-System (ECS) architecture also works well in Rust to avoid issues around shared mutable state.
In ECS, the framework owns all of the components. Components continue to be responsible for holding their own state, responding to user input, and painting onto the screen but the framework is responsible for storing the relationship between the components (the tree we mentioned above) and for any interaction between the components. This helps solve a lot of the issues in the Rust compiler around mutability: the single owner for all of the components is the framework. This approach isn’t perfect–the system now needs to track when to remove old components. It also litters references to this central store throughout your codebase since that is the only way to read out the state from any component.
This is roughly the approach we chose to take at Warp: we represent each component (what we call a
View
) with a unique ID called an
EntityId
. Each window stores a mapping of the
EntityId
to the actual View that is identified by the ID:
Rust
/// A structure holding all application state that is linked to a particular
/// window.
#[derive(Default)]
pub(super) struct Window {
    /// The set of views owned by this window, keyed by view ID.
    pub views: HashMap<EntityId, Box<dyn AnyView>>,

    /// A handle to the window's root view (top of the view hierarchy), if any.
    pub root_view: Option<AnyViewHandle>,

    /// The ID of the currently focused view, if any.
    pub focused_view: Option<EntityId>,
}
We use this
EntityID
as the key to store any state that references the view. For example, we store a mapping of each view to its parent view (see the
parents
field) so that we can traverse the view tree upwards. We also store a mapping of what each view rendered onto the screen in the last frame (see the
rendered_views
field).
Rust
pub struct Presenter {
    window_id: WindowId,
    scene: Option<Rc<Scene>>,
    rendered_views: HashMap<EntityId, Box<dyn Element>>,
    parents: HashMap<EntityId, EntityId>,
    font_cache: Arc<FontCache>,
    asset_cache: Arc<assets::Cache>,
    text_layout_cache: LayoutCache,
    stack_context: StackContext,
}
In an object oriented world, all of the state for each of these components would be encoded
within
the component. In ECS, this data is denormalized into a series of maps and lists owned by the system. We use this
EntityID
as the key across any structure that holds state for a view. In this screenshot below of Warp we have three different views, each of which have unique
EntityID
s:
The use of these
EntityIds
allow us to encode a component tree structure without inheritance. The actual view tree for the screenshot above would look something like:
Entity-Component-Systems and Elm are not the only two approaches to solve this by any means. Others have investigated using
immediate mode GUI
, or even using the DOM to render while keeping application logic in Rust (see
Tauri
).
Looking Forward
Building a proper UI framework in Rust is hard and often unintuitive. It’s also not yet set up for a great developer experience when using a framework: it doesn’t support hot reloading which can lead to a slow and clunky experience of recompiling code to make the smallest of UI changes.
Rust’s strong commitments to portability and performance, and active ecosystem still makes it a compelling choice for UI programming: especially for cases where high performance is critical.
In our case, our UI framework has served us well to achieve our performance goals and is not a major source of velocity issues for our developers. It has its shortcomings though–some of which are shortcomings with its design and others because of Rust. For example, we don’t have an easy way to traverse the tree of elements we paint onto the screen in any order of direction–this makes event handling more difficult. We also use a
RefCell
to handle shared mutability when receiving platform events from the event loop–though it’s rare, we’ve had a few crashes from users in the wild due to concurrent calls to
borrow_mut
.
The future of UI in Rust will likely continue to be innovative yet fragmented as the community experiments with many different approaches. We don’t yet have a one-size-fits-all framework, but I have no doubt that one, if not many, will succeed in the coming years. As hardware advances, Rust will be a good choice to build a buttery-smooth UI in a way that is cross-platform. And if you’re curious in trying our Rust-based UI, you can download Warp here:
\---
Footnotes
1
We built this framework in collaboration with
Nathan Sobo
, the co-founder of Atom and
zed.dev
.
2
Example from https://doc.rust-lang.org/book/ch17-02-trait-objects.html
Related articles
May 4, 2026  ·  9 min
Open-sourcing our docs and the agents that maintain them
Today, we’re moving our product documentation at docs.warp.dev onto a stack we control end-to-end, and open-sourcing it at github.com/warpdotdev/docs.
Apr 29, 2026  ·  16 min
The Block Model Behind Warp's Agentic Development Environment
Warp has come a long way since it initially set out to modernize the terminal. In the screenshot above, an agent is working through a plan alongside a developer's own shell commands — running its own commands, reasoning, proposing a diff — all in the same scroll stream. Five years ago, none of that would have had a place in Warp; today it's a core part of how people use it.
Apr 16, 2026  ·  2 min
Introducing Claude Opus 4.7 in Warp
Claude Opus 4.7 is now available in Warp on paid plans and is the new default model for auto (genius), bringing stronger performance on multi-step coding tasks, debugging, and agent workflows.
