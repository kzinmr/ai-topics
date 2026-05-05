---
title: "Testing Vue components in the browser"
url: "https://jvns.ca/blog/2026/05/02/testing-vue-components-in-the-browser/"
fetched_at: 2026-05-05T07:01:45.964951+00:00
source: "Julia Evans (jvns)"
tags: [blog, raw]
---

# Testing Vue components in the browser

Source: https://jvns.ca/blog/2026/05/02/testing-vue-components-in-the-browser/

Hello! One of my long term projects on here is
figuring out how to write frontend Javascript without using Node
or any other server JS runtime.
One issue I run into a lot in my frontend JS projects is that I don’t know how
to write tests for them. I’ve tried to use Playwright in the past, but it felt
slow and unwieldy to be starting these new browser processes all the time, and
it involved some Node code to orchestrate the tests.
The result is that I just don’t test my frontend code which doesn’t feel great.
Usually I don’t update my projects much either so it doesn’t come up that much,
but it would be nice to be able to make changes with more confidence!
So a way to do frontend testing that I like has been on my wishlist for a long time.
Alex Chan wrote a great post a while back called
Testing JavaScript without a (third-party) framework
in response to one of my previous posts in this series that explained how to
write a tiny unit-testing framework that runs in a page in browser.
I loved this post at the time, but it only talked about unit testing and I
wanted to write end-to-end integration tests for my Vue components, and I didn’t
know how to do that.
So when I was talking to
Marco
the other day and he said something like “you know, you can just run tests
for your Vue components in the browser”, I thought “hey, I should try that
again!!!”
I just did all of this yesterday so certainly there’s a lot to improve but I
wanted to write down a few things I noticed about the process before I forget.
This was a bit tricky for me because the Vue site usually assumes that you’re
using Node as part of your build process in some way (there’s a lot of “step 1:
npm install THING
), and I didn’t want to use Node/Deno/etc. But it turned
out to not be too complicated.
The project I’m going to talk about testing is this
zine feedback site I wrote in 2023
.
I used
QUnit
. It worked great but I don’t have anything
interesting to say about how it works so I’ll leave it at that. I think that
Alex’s “write your own test framework” approach would have
worked too. I followed
these directions
.
I did appreciate that QUnit has a “rerun test” button that will only rerun 1
test. Because there are so many network requests in my tests, having a way to
run just 1 test makes it a lot less confusing to debug the test.
The first thing I needed to do was get my Vue
components set up in the test environment.
I changed my main app to put all my components in
window._components
,
kind of like this:
const components = {
  'Feedback': FeedbackComponent,
  ...
}
window._components = components;
Then I was able to write a
mountComponent
function which
does basically exactly the same thing my normal main app does
(render a tiny template with the component I want to use).
The only differences are:
I can optionally pass some some extra data to use as its props.
It mounts the component to a temporary invisible div which will get removed
from the DOM after the test is done. The div is positioned off the page
(
position: absolute; top: -10000, ...
) so you can’t see it.
Here’s what using the
mountComponent
function looks like:
const {div} = mountComponent(
  '<Page :feedbacks="feedbacks" id=2 />',
  {feedbacks: [testFeedback]},
);
and here’s the code for it:
function mountComponent(template, data) {
  const app = Vue.createApp({
    template: template,
    data: () => data,
  })
  for (const [c, v] of Object.entries(window._components)) {
    app.component(c, v);
  }
  const div = document.getElementById('qunit-fixture')
             .appendChild(document.createElement('div'));
  return div;
}
The result is a div where I can programmatically click, fill in form data, check
that the right content appears, etc.
Because I was writing end-to-end integration tests to make sure my client JS
worked properly with my server, I needed to have some test data in my database.
So I wrote ~25 lines of SQL to set up some test data in my database, and added
an endpoint to my dev server to run the SQL to reset the test data to a known
state.
async function reset() {
    return fetch('/api/reset_test_data', {method: "POST"})
}
Then I just run
await reset()
at the beginning of any test that needs the
test data.
My
reset()
function actually doesn’t always totally reset everything which is
kind of bad, but it was workable to start with and can always be improved.
Here’s what a basic test looks like! Basically we’re rendering the div
and make sure it contains some approximately correct data.
QUnit.test('renders feedback content', async function (assert) {
  const {div} = mountComponent(
    '<Page :feedbacks="feedbacks" id=2 image=2 page_hash=2 />',
    {feedbacks: [testFeedback]},
  );
  assert.ok(div.textContent.includes('loved this section'));
})
Those are all the basic pieces! Now here are a few issues I ran into along the
way
I have a lot of network requests in my tests, and it takes time for them to
finish and for the Vue code to do what it has to do with the results and update
the DOM.
I think we all learned a long time ago that putting random
sleep()
calls in
your tests and hoping that the timings are right is slow and flaky and extremely
frustrating, so I needed a different way.
As far as I can tell the normal way to deal with this is to figure out a way to
tell from the DOM whether it’s okay to proceed or not. Like “if this button is
visible, we can “.
So I wrote a little
waitFor()
function that polls every 20ms to see if a
condition has finished yet. It times out after 2 seconds.
Here’s what using it looks like:
QUnit.test("click item", async function (assert) {
  const {div} = mountComponent(
    '<Feedback zine_id="test123" image_width="800px" />',
    {});
  const item = await waitFor(() => div.querySelector('.feedback-item'));
  item.click();
  // rest of test goes here... 
})
It looks like there are a lot of implementations of this concept out there and they’re all
better thought-through than mine. (from a quick Google:
qunit-wait-for
,
playwright expect.poll
)
In some cases I
thought
I’d identified the right thing to wait for in the DOM
(“just wait for this textarea to appear!’) but it turned out that because of
some internal details of how my program works, actually I needed to wait for
something else later on which was hard to pin down.
I ended up changing one of my components to add some random value to the DOM
when it was finished an important action (like
data-this-thing-is-ready=true
)
which didn’t feel great.
My best guess is that the right way to fix this kind of test issue is a refactor
that also makes the app more reliable for the users: if there’s an element
in the DOM that isn’t actually ready for the user to interact with, maybe I
shouldn’t be displaying it yet!
I ended up adding a few classes to HTML elements that I needed to find in the tests,
either because I needed to click on them or wait for them to appear in the DOM.
I might want to change this approach later - frontend testing frameworks seem to
suggest avoiding using CSS classes and instead using something like
getByRole
or as a last resort something like a
data-testid
.
Feels like there’s a way to make the app more accessible and easier to test at the same time.
To fill out a form, I can’t just set the
value
, I also need to dispatch an
event to tell Vue that the element has changed. For example,
checkbox
and
textarea
need different kinds of events.
textarea.value = 'banana banana banana';
textarea.dispatchEvent(new Event('input'));
checkbox.checked = true;
checkbox.dispatchEvent(new Event('change'));
This is kind of annoying and it made me realize why I might want to use some
kind of UI testing library, for example:
I want to have an idea of what my test coverage was, and it turns out that
Chrome actually has a built-in
code coverage
feature for JS and CSS!
My JS is bundled into a file called
bundle.js
with esbuild, so I could just
look at
bundle.js
and see which lines weren’t covered.
The process was a little finicky: I had to turn off sourcemaps in the Chrome
devtools to get this to work, and there’s a specific not super obvious
series of actions I have to do in order to see the coverage data.
As usual with these posts I’ve never really worked as a frontend or backend
developer (other than for myself!) and I feel like I’m constantly learning how
to do super basic tasks.
I really had a blast doing this. My frontend projects always feel so fragile
because they’re untested, and maybe one day I’ll have a test suite I’m confident
in!
Some things I’m still thinking about:
While writing this post I found this frontend testing library called
Testing Library
that has a lot of
guidelines for how to write tests that are very different from my initial ideas.
I experimented with rewriting everything to use Testing Library and it felt
pretty good, so we’ll see how that goes. They distribute a
.umd.js
file
that works without Node.
I’m not sure how I feel about not having a way to run these tests on the
command line at all. Maybe there’s a simple way to work primarily in the
browser but have an way to run them in CI too if I want?
