# A Language For Agents

- **Author:** Armin Ronacher (@mitsuhiko)
- **Published:** 2026-02-09
- **Source:** https://lucumr.pocoo.org/2026/2/9/a-language-for-agents/
- **Description:** What programming languages would agents want to program in?
- **Saved:** 2026-05-18

---

A Language For Agents | Armin Ronacher's Thoughts and Writings 

  {
    "@context": "https://schema.org",
    "@type": "BlogPosting",
    "headline": "A Language For Agents",
    "description": "What programming languages would agents want to program in?",
    "author": {
      "@type": "Person",
      "name": "Armin Ronacher",
      "url": "https://lucumr.pocoo.org/about/"
    },
    "datePublished": "2026-02-09T00:00:00",
    "url": "https://lucumr.pocoo.org/2026/2/9/a-language-for-agents/",
    "mainEntityOfPage": {
      "@type": "WebPage",
      "@id": "https://lucumr.pocoo.org/2026/2/9/a-language-for-agents/"
    },
    "publisher": {
      "@type": "Person",
      "name": "Armin Ronacher",
      "url": "https://lucumr.pocoo.org/about/"
    },
    "image": {
      "@type": "ImageObject",
      "url": "https://lucumr.pocoo.org/social/2026-02-09-a-language-for-agents-social.png",
      "width": 1200,
      "height": 630
    },
    "keywords": ["ai"]
  }

      {
        "prefetch": [
          {
            "where": { "href_matches": "/*" },
            "eagerness": "moderate"
          }
        ]
      }

      let $THEME = null;

      function selectTheme(theme) {
        const node = document.documentElement;
        if (theme === "system") {
          localStorage.removeItem("theme");
        } else {
          localStorage.setItem("theme", theme);
        }
        node.setAttribute("data-theme", theme);
        $THEME = theme;
      }

      selectTheme(localStorage.getItem("theme") || "system");
      document.documentElement.setAttribute("data-initial-load", "true");

      if (history.scrollRestoration) {
        history.scrollRestoration = 'manual';
      }

         Armin Ronacher 's Thoughts and Writings

            blog 
            archive 
            projects 
            travel 
            talks 
            about 

   A Language For Agents 

   written on February 09, 2026 

   Last year I first started thinking about what the future of programming
languages might look like now that agentic engineering is a growing thing.
Initially I felt that the enormous corpus of pre-existing code would cement
existing languages in place but now I&#8217;m starting to think the opposite is true.
Here I want to outline my thinking on why we are going to see more new
programming languages and why there is quite a bit of space for interesting
innovation.  And just in case someone wants to start building one, here are some
of my thoughts on what we should aim for! 
 Why New Languages Work 
 Does an agent perform dramatically better on a language that it has in its
weights?  Obviously yes.  But there are less obvious factors that affect how
good an agent is at programming in a language: how good the tooling around it is
and how much churn there is. 
 Zig seems underrepresented in the weights (at least in the models I&#8217;ve used)
and also changing quickly.  That combination is not optimal, but it&#8217;s still
passable: you can program even in the upcoming Zig version if you point the
agent at the right documentation.  But it&#8217;s not great. 
 On the other hand, some languages are well represented in the weights but agents
still don&#8217;t succeed as much because of tooling choices.  Swift is a good
example: in my experience the tooling around building a Mac or iOS application
can be so painful that agents struggle to navigate it.  Also not great. 
 So, just because it exists doesn&#8217;t mean the agent succeeds and just because it&#8217;s
new also doesn&#8217;t mean that the agent is going to struggle.  I&#8217;m convinced that
you can build yourself up to a new language if you don&#8217;t want to depart
everywhere all at once. 
 The biggest reason new languages might work is that the cost of coding is going
down dramatically.  The result is the breadth of an ecosystem matters less. I&#8217;m
now routinely reaching for JavaScript in places where I would have used Python.
Not because I love it or the ecosystem is better, but because the agent does
much better with TypeScript. 
 The way to think about this: if important functionality is missing in my
language of choice, I just point the agent at a library from a different
language and have it build a port.  As a concrete example, I recently built an
Ethernet driver in JavaScript to implement the host controller for our sandbox.
Implementations exist in Rust, C, and Go, but I wanted something pluggable and
customizable in JavaScript.  It was easier to have the agent reimplement it than
to make the build system and distribution work against a native binding. 
 New languages will work if their value proposition is strong enough and they
evolve with knowledge of how LLMs train.  People will adopt them despite being
underrepresented in the weights.  And if they are designed to work well with
agents, then they might be designed around familiar syntax that is already known
to work well. 
 Why A New Language? 
 So why would we want a new language at all?  The reason this is interesting to
think about is that many of today&#8217;s languages were designed with the assumption
that punching keys is laborious, so we traded certain things for brevity.  As an
example, many languages — particular modern ones — lean heavily on type
inference so that you don&#8217;t have to write out types.  The downside is that you
now need an LSP or the resulting compiler error messages to figure out what the
type of an expression is.  Agents struggle with this too, and it&#8217;s also
frustrating in pull request review where complex operations can make it very
hard to figure out what the types actually are.  Fully dynamic languages are
even worse in that regard. 
 The cost of writing code is going down, but because we are also producing more
of it, understanding what the code does is becoming more important.  We might
actually want more code to be written if it means there is less ambiguity when
we perform a review. 
 I also want to point out that we are heading towards a world where some code is
never seen by a human and is only consumed by machines.  Even in that case, we
still want to give an indication to a user, who is potentially a non-programmer,
about what is going on.  We want to be able to explain to a user what the code
will do without going into the details of how. 
 So the case for a new language comes down to: given the fundamental changes in
who is programming and what the cost of code is, we should at least consider
one. 
 What Agents Want 
 It&#8217;s tricky to say what an agent wants because agents will lie to you and they
are influenced by all the code they&#8217;ve seen.  But one way to estimate how they
are doing is to look at how many changes they have to perform on files and how
many iterations they need for common tasks. 
 There are some things I&#8217;ve found that I think will be true for a while. 
 Context Without LSP 
 The language server protocol lets an IDE infer information about what&#8217;s under
the cursor or what should be autocompleted based on semantic knowledge of the
codebase.  It&#8217;s a great system, but it comes at one specific cost that is tricky
for agents: the LSP has to be running. 
 There are situations when an agent just won&#8217;t run the LSP — not because of
technical limitations, but because it&#8217;s also lazy and will skip that step if it
doesn&#8217;t have to.  If you give it an example from documentation, there is no easy
way to run the LSP because it&#8217;s a snippet that might not even be complete.  If
you point it at a GitHub repository and it pulls down individual files, it will
just look at the code.  It won&#8217;t set up an LSP for type information. 
 A language that doesn&#8217;t split into two separate experiences (with-LSP and
without-LSP) will be beneficial to agents because it gives them one unified way
of working across many more situations. 
 Braces, Brackets, and Parentheses 
 It pains me as a Python developer to say this, but whitespace-based indentation
is a problem.  The underlying token efficiency of getting whitespace right is
tricky, and a language with significant whitespace is harder for an LLM to work
with.  This is particularly noticeable if you try to make an LLM do surgical
changes without an assisted tool.  Quite often they will intentionally disregard
whitespace, add markers to enable or disable code and then rely on a code
formatter to clean up indentation later. 
 On the other hand, braces that are not separated by whitespace can cause issues
too.  Depending on the tokenizer, runs of closing parentheses can end up split
into tokens in surprising ways (a bit like the &#8220;strawberry&#8221; counting problem),
and it&#8217;s easy for an LLM to get Lisp or Scheme wrong because it loses track of
how many closing parentheses it has already emitted or is looking at.  Fixable
with future LLMs?  Sure, but also something that was hard for humans to get
right too without tooling. 
 Flow Context But Explicit 
 Readers of this blog might know that I&#8217;m a huge believer in async locals and
flow execution context — basically the ability to carry data through every
invocation that might only be needed many layers down the call chain.  Working
at an observability company has really driven home the importance of this for
me. 
 The challenge is that anything that flows implicitly might not be configured.
Take for instance the current time.  You might want to implicitly pass a timer
to all functions.  But what if a timer is not configured and all of a sudden a
new dependency appears?  Passing all of it explicitly is tedious for both humans
and agents and bad shortcuts will be made. 
 One thing I&#8217;ve experimented with is having effect markers on functions that are
added through a code formatting step.  A function can declare that it needs the
current time or the database, but if it doesn&#8217;t mark this explicitly, it&#8217;s
essentially a linting warning that auto-formatting fixes.  The LLM can start
using something like the current time in a function and any existing caller gets
the warning; formatting propagates the annotation. 
 This is nice because when the LLM builds a test, it can precisely mock out
these side effects — it understands from the error messages what it has to
supply. 
 For instance: 
 
```
fn issue(sub: UserId, scopes: []Scope) -> Token
    needs { time, rng }
{
    return Token{
        sub,
        exp: time.now().add(24h),
        scopes,
    }
}

test "issue creates exp in the future" {
    using time = time.fixed("2026-02-06T23:00:00Z");
    using rng  = rng.deterministic(seed: 1);

    let t = issue(user("u1"), ["read"]);
    assert(t.exp > time.now());
}

```
 
 Results over Exceptions 
 Agents struggle with exceptions, they are afraid of them.  I&#8217;m not sure to what
degree this is solvable with RL (Reinforcement Learning), but right now agents
will try to catch everything they can, log it, and do a pretty poor recovery.
Given how little information is actually available about error paths, that makes
sense.  Checked exceptions are one approach, but they propagate all the way up
the call chain and don&#8217;t dramatically improve things.  Even if they end up as
hints where a linter tracks which errors can fly by, there are still many call
sites that need adjusting.  And like the auto-propagation proposed for context
data, it might not be the right solution. 
 Maybe the right approach is to go more in on typed results, but that&#8217;s still
tricky for composability without a type and object system that supports it. 
 Minimal Diffs and Line Reading 
 The general approach agents use today to read files into memory is line-based,
which means they often pick chunks that span multi-line strings.  One easy way
to see this fall apart: have an agent work on a 2000-line file that also
contains long embedded code strings — basically a code generator.  The agent
will sometimes edit within a multi-line string assuming it&#8217;s the real code when
it&#8217;s actually just embedded code in a multi-line string.  For multi-line
strings, the only language I&#8217;m aware of with a good solution is Zig, but its
prefix-based syntax is pretty foreign to most people. 
 Reformatting also often causes constructs to move to different lines.  In many
languages, trailing commas in lists are either not supported (JSON) or not
customary.  If you want diff stability, you&#8217;d aim for a syntax that requires
less reformatting and mostly avoids multi-line constructs. 
 Make It Greppable 
 What&#8217;s really nice about Go is that you mostly cannot import symbols from
another package into scope without every use being prefixed with the package
name.  Eg: `context.Context` instead of `Context`.  There are escape hatches
(import aliases and dot-imports), but they&#8217;re relatively rare and usually
frowned upon. 
 That dramatically helps an agent understand what it&#8217;s looking at.  In general,
making code findable through the most basic tools is great — it works with
external files that aren&#8217;t indexed, and it means fewer false positives for
large-scale automation driven by code generated on the fly (eg: `sed`, `perl`
invocations). 
 Local Reasoning 
 Much of what I&#8217;ve said boils down to: agents really like local reasoning.  They
want it to work in parts because they often work with just a few loaded files in
context and don&#8217;t have much spatial awareness of the codebase.  They rely on
external tooling like grep to find things, and anything that&#8217;s hard to grep or
that hides information elsewhere is tricky. 
 Dependency Aware Builds 
 What makes agents fail or succeed in many languages is just how good the build
tools are.  Many languages make it very hard to determine what actually needs to
rebuild or be retested because there are too many cross-references.  Go is
really good here: it forbids circular dependencies between packages (import
cycles), packages have a clear layout, and test results are cached. 
 What Agents Hate 
 Macros 
 Agents often struggle with macros.  It was already pretty clear that humans
struggle with macros too, but the argument for them was mostly that code
generation was a good way to have less code to write.  Since that is less of a
concern now, we should aim for languages with less dependence on macros. 
 There&#8217;s a separate question about generics and
 comptime .  I think they fare
somewhat better because they mostly generate the same structure with different
placeholders and it&#8217;s much easier for an agent to understand that. 
 Re-Exports and Barrel Files 
 Related to greppability: agents often struggle to understand  barrel
files  and they don&#8217;t
like them.  Not being able to quickly figure out where a class or function comes
from leads to imports from the wrong place, or missing things entirely and
wasting context by reading too many files.  A one-to-one mapping from where
something is declared to where it&#8217;s imported from is great. 
 And it does not have to be overly strict either.  Go kind of goes this way, but
not too extreme.  Any file within a directory can define a function, which isn&#8217;t
optimal, but it&#8217;s quick enough to find and you don&#8217;t need to search too far.
It works because packages are forced to be small enough to find everything with
grep. 
 The worst case is free re-exports all over the place that completely decouple
the implementation from any trivially reconstructable location on disk.  Or
worse: aliasing. 
 Aliasing 
 Agents often hate it when aliases are involved.  In fact, you can get them to
even complain about it in thinking blocks if you let them refactor something
that uses lots of aliases.  Ideally a language encourages good naming and
discourages aliasing at import time as a result. 
 Flaky Tests and Dev Env Divergence 
 Nobody likes flaky tests, but agents even less so.  Ironic given how
particularly good agents are at creating flaky tests in the first place.  That&#8217;s
because agents currently love to mock and most languages do not support mocking
well.  So many tests end up accidentally not being concurrency safe or depend on
development environment state that then diverges in CI or production. 
 Most programming languages and frameworks make it much easier to write flaky
tests than non-flaky ones.  That&#8217;s because they encourage indeterminism
everywhere. 
 Multiple Failure Conditions 
 In an ideal world the agent has one command, that lints and compiles and it
tells the agent if all worked out fine.  Maybe another command to run all tests
that need running.  In practice most environments don&#8217;t work like this.  For
instance in TypeScript you can often run the code even  though it fails
type checks .  That can gaslight the agent.  Likewise
different bundler setups can cause one thing to succeed just for a slightly
different setup in CI to fail later.  The more uniform the tooling the better. 
 Ideally it either runs or doesn&#8217;t and there is mechanical fixing for as many
linting failures as possible so that the agent does not have to do it by hand. 
 Will We See New Languages? 
 I think we will.  We are writing more software now than we ever have — more
websites, more open source projects, more of everything.  Even if the ratio of
new languages stays the same, the absolute number will go up.  But I also truly
believe that many more people will be willing to rethink the foundations of
software engineering and the languages we work with.  That&#8217;s because while for
some years it has felt you need to build a lot of infrastructure for a language
to take off, now you can target a rather narrow use case: make sure the agent is
happy and extend from there to the human. 
 I just hope we see two things.  First, some outsider art: people who haven&#8217;t
built languages before trying their hand at it and showing us new things.
Second, a much more deliberate effort to document what works and what doesn&#8217;t
from first principles.  We have actually learned a lot about what makes good
languages and how to scale software engineering to large teams.  Yet,  finding
it written down, as a consumable overview of good and bad language design, is
very hard to come by.  Too much of it has been shaped by opinion on rather
pointless things instead of hard facts. 
 Now though, we are slowly getting to the point where facts matter more, because
you can actually measure what works by seeing how well agents perform with it.
No human wants to be subject to surveys, but  agents don&#8217;t
care .  We can see how successful they are and where they
are struggling. 

   This entry was tagged
    
       ai 

     copy as  /  view  markdown

    document.addEventListener('DOMContentLoaded', function() {
      const copyLink = document.getElementById('copy-markdown');
      const markdownUrl = '/2026/2/9/a-language-for-agents.md';
      
      function showFlashNotification(message) {
        // Create notification element
        const notification = document.createElement('div');
        notification.className = 'flash-notification';
        notification.textContent = message;
        
        document.body.appendChild(notification);
        
        // Fade in
        requestAnimationFrame(() => {
          notification.style.opacity = '1';
        });
        
        // Remove after 1 second
        setTimeout(() => {
          notification.style.opacity = '0';
          setTimeout(() => {
            document.body.removeChild(notification);
          }, 200);
        }, 1500);
      }
      
      async function copyMarkdown() {
        try {
          const response = await fetch(markdownUrl);
          const markdown = await response.text();
          await navigator.clipboard.writeText(markdown);
          
          showFlashNotification('page copied as markdown to clipboard');
        } catch (err) {
          console.error('Failed to copy markdown:', err);
          alert('Failed to copy markdown to clipboard');
        }
      }
      
      // Handle copy link click
      if (copyLink) {
        copyLink.addEventListener('click', function(e) {
          e.preventDefault();
          copyMarkdown();
        });
      }
      
      // Handle Ctrl+C / Cmd+C when nothing is selected
      document.addEventListener('keydown', function(e) {
        if ((e.ctrlKey || e.metaKey) && e.key === 'c') {
          const selection = window.getSelection();
          if (selection.toString().length === 0) {
            e.preventDefault();
            copyMarkdown();
          }
        }
      });
    });

         &copy; Copyright 2026 by Armin Ronacher.
         
          Content licensed under the Creative Commons
          Attribution-NonCommercial 4.0 International  License .
         
          Contact me via  mail ,
           bluesky ,
           x , or
           github .
         
          You can  sponsor me on github .
         
          More info:  imprint  &
           AI transparency .
          Subscribe via  atom  /  RSS .
         
          Color scheme:
              auto  ,
              light  ,
              dark  .
           
            document.querySelector('.theme-selector').removeAttribute('hidden');
            document.querySelectorAll('input[name="theme"]').forEach(input => {
              input.checked = input.value === $THEME;
              input.addEventListener('change', () => {
                selectTheme(input.value);
              });
            });

      window.setTimeout(() => {
        document.documentElement.removeAttribute("data-initial-load");
      }, 0);