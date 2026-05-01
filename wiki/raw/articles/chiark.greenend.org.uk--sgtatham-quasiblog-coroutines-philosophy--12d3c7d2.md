---
title: "Philosophy of coroutines"
url: "https://www.chiark.greenend.org.uk/~sgtatham/quasiblog/coroutines-philosophy/"
fetched_at: 2026-05-01T07:00:58.052144+00:00
source: "chiark.greenend.org.uk/~sgtatham"
tags: [blog, raw]
---

# Philosophy of coroutines

Source: https://www.chiark.greenend.org.uk/~sgtatham/quasiblog/coroutines-philosophy/

Philosophy of coroutines
[Simon Tatham, initial version 2023-09-01, last updated 2025-03-25]
[Coroutines trilogy:
C preprocessor
|
C++20 native
|
general philosophy
]
Introduction
I’ve been a huge fan of coroutines since the mid-1990s.
I encountered the idea as a student, when I first read
The
      Art of Computer Programming
. I’d been programming already
      for most of my childhood, and I was completely blown away by the
      idea, which was entirely new to me. In fact, it’s probably not
      an exaggeration to say that in the whole of
TAOCP
that
      was the single thing that changed my life the most.
Within a few months of encountering the idea for the first
      time, I found myself wanting to use it in real code, during a
      vacation job at a (now defunct) tech company. Sadly I was coding
      in C at the time, which didn’t support coroutines. But I didn’t
      let that stop me: I came up with a C preprocessor trick that
      worked well enough to fake them, and did it anyway.
The trick I came up with has limitations, but it’s reliable
      enough to use in serious code. I wrote it up a few years later
      in the
      article ‘
Coroutines
      in C
’, and I’ve been using it ever since, in both C and C++,
      whenever the code I’m trying to write looks as if it would be
      most naturally expressed in that style.
Or rather, I do that in code bases
where I can get away
      with it
, because it’s unquestionably a weird and unorthodox
      style of C by normal standards, and not everyone is prepared to
      take it in their stride. Mostly I limit my use of C-preprocessor
      coroutines to free software projects where I’m the lead or only
      developer (in
      particular,
PuTTY
and
spigot
),
      because there, I get to choose what’s an acceptable coding style
      and what’s not. The only time I’ve ever used the same technique
      in code I wrote for an employer was in that original vacation
      job where I invented the trick – and I’m sure I only got away
      with it that time because my team didn’t practise code
      review.
Of course, I’m also happy to use coroutine-style idioms in any
      language where you
don’t
have to resort to trickery,
      such as using generators in Python whenever it seems like a good
      idea.
Whenever I
can’t
use coroutines, I feel limited,
      because it’s become second nature to me to spot parts of a
      program that
want
to be written in coroutine style, and
      would be more awkward to express in other ways. So I’m very much
      in favour of coroutines becoming more mainstream – and I’ve been
      pleased to see support appearing in more and more languages over
      the decades. At the time of writing this, Wikipedia has
      an
impressive
      list of languages
that now include coroutine support; from
      my own perspective, the big ones are Python generators, and the
      addition of a coroutine system to C++20.
I recently got round
      to
learning
      about the C++20 system
in detail. In the course of that, I
      had conversations about coroutines with several friends and
      colleagues, which made me think more seriously about the fact
      that I’m so fond of them, and wonder if I had anything more
      specific to say about that than ‘they’re really useful’.
It turned out that I did. So this article presents my
      ‘philosophy of coroutines’:
why
I find them so useful,
      what kinds of thing they’re useful for, tricks I’ve learned for
      getting the most out of them, and even a few different ways of
      thinking
about
them.
But it discusses coroutines as a general concept, not specific
      to their implementation in any particular language. So where I
      present code snippets, they’ll be in whatever language is
      convenient to the example, or even in pure pseudocode.
Why I’m so enthusiastic about coroutines
Go on then, why
do
I like coroutines so much?
Well, from first principles, there are two possibilities.
      Either it’s because they really are awesome, or it’s because
      they suit my personal taste. (Or a combination of the two, of
      course.)
I can think of arguments for both of those positions, but I
      don’t think I have the self-awareness to decide which is more
      significant. So I’ll just present both sets of arguments, and
      let you make up your own mind about whether you end up also
      thinking they’re awesome.
The objective view: what makes them useful?
To answer ‘what makes coroutines useful?’, it’s useful to start
      by deciding what we’re
comparing
them to. I can’t answer
      ‘why is a coroutine more useful than
X?
’ without knowing
      what
X
we’re talking about. And there’s more than one
      choice.
Versus explicit state machines
Two decades ago, when I wrote
      ‘
Coroutines
      in C
’, I included an explanation of why coroutines are
      useful, based on the idea that the alternative was to write an
      ordinary function containing an explicit state machine.
Suppose you have a function that consumes a stream of values,
      and due to the structure of the rest of your program, it has to
      receive each individual value via a separate function call:
function process_next_value(v) {
    // ...
}
And suppose the nature of the stream is such that the way you
      handle each input value depends on what the previous values
      were. I’ll show an example similar to the previous article,
      which is a simple run-length decompressor processing a stream of
      input bytes: the idea is that most input bytes are emitted
      literally to the output, but one byte value is special, and is
      followed by a (length, output byte) pair indicating that the
      output byte should be repeated a number of times.
To write that as a conventional function accepting a single
      byte on each call, you have to keep a state variable of some
      kind to remind you of what you were going to use the next byte
      for:
function process_next_byte(byte) {
    if (state == TOP_LEVEL) {
        if (byte != ESCAPE_BYTE) {
            // emit the byte literally and stay in the same state
            output(byte);
        } else {
            // go into a state where we expect to see a run length next
            state = EXPECT_RUN_LENGTH;
        }
    } else if (state == EXPECT_RUN_LENGTH) {
        // store the length
        run_length = byte;
        // go into a state where we expect the byte to be repeatedly output
        state = EXPECT_OUTPUT;
    } else if (state == EXPECT_OUTPUT) {
        // output this byte the right number of times
        for i in (1,...,run_length)
            output(byte);
        // and go back to the top-level state for the next input byte
        state = TOP_LEVEL;
    }
}
(This is pseudocode, so I’m not showing the details of how you
      arrange for
state
and
run_length
to be
      preserved between calls to the function. Whatever’s convenient
      in your language. These days they’re probably member variables
      of a class, in most languages.)
This is pretty unwieldy code to write, because structurally, it
      looks a lot like a collection of blocks of code connected by
      ‘goto’ statements. They’re not
literally
goto
      statements – each one works by setting
state
to
      some value and returning from the function – but they have the
      same semantic effect, of stating by name which part of the
      function is going to be run next.
The more complicated the control structure is, the more
      cumbersome it becomes to write code in this style, or to read
      it. Suppose I wanted to enhance my run-length compression format
      so that it could efficiently represent repetitions of
      a
sequence
of bytes, not just
AAAAAAA
but
ABABABAB
or
ABCDEABCDE
? Then I
      wouldn’t just need an
output
loop to emit
n
copies of something; I’d also need a loop on the input side,
      because the input format would probably contain an ‘input
      sequence length’ byte followed by that many bytes of literal
      input. But I can’t write that one as a
for
statement, because it has to return to the caller to get each
      input byte; instead, I’d have to build a ‘for loop’ structure
      out of these small building blocks.
The more code you write in this style, the more you probably
      wish that the caller and callee were the other way round. If you
      were writing the same run-length decompression code in a context
      where you
called
a function to read the next byte, it
      would look a lot more natural (not to mention shorter), because
      you could call the get-byte function in multiple places:
function run_length_decompress(stream) {
    while (byte = stream.getbyte()) {
        if (byte != ESCAPE_BYTE) {
            output(byte);
        } else {
            run_length = stream.getbyte();
            byte_to_repeat = stream.getbyte();
            for i in (1,...,run_length)
                output(byte_to_repeat);
        }
    }
}
This function actually contains the same state machine as the
      previous version – but it’s entirely implicit. If you want to
      know what each piece of code will do when its next input byte
      arrives (say, during debugging), then in the state-machine
      version you answer it by asking for the value
      of
state
– but in this version, you’d answer it by
      looking at a stack backtrace to find out which of the calls
      to
stream.getbyte()
the byte will be returned from,
      because that’s what controls where execution will resume from.
In other words, each of the three state
      values
TOP_LEVEL
,
EXPECT_RUN_LENGTH
and
EXPECT_OUTPUT
in the state-machine code
      corresponds precisely to one of the three calls
      to
stream.getbyte()
in this version. So there’s
      still a piece of data in the program tracking which of those
      ‘states’ we’re in – but it’s the
program counter
, and
      doesn’t need to be a named variable with a set of explicit named
      or numbered state values.
And if you needed to extend
this
version of the code
      so that it could read a list of input bytes to repeat, it would
      be no trouble at all, because there’s nothing to stop you
      putting a call to
stream.getbyte()
in a loop:
num_output_repetitions = stream.getbyte();
            num_input_bytes = stream.getbyte();
            for i in (1,...,num_input_bytes)
                input_bytes.append(stream.getbyte());
            for i in (1,...,num_output_repetitions)
                for byte in input_bytes
                    output(byte);
and you wouldn’t have to mess around with inventing extra
      values in your state enumeration, coming up with names for them,
      checking the names weren’t already used, renaming other states
      if their names had become ambiguous, carefully writing
      transitions to and from existing states, etc. You can just
      casually write a loop, and the programming language takes care
      of the rest.
(I tend to think of the state-machine style as ‘turning the
      function inside out’, in a more or less literal sense: the calls
      to a ‘get byte’ function ought to be nested
      deeply
inside
the code’s control flow, but instead,
      we’re forced to make them the
outermost
layer, so that
      ‘now wait for another byte’ consists of control falling off the
      end of the function, and ‘ok, we’ve got one now, carry on’ is at
      the top.)
Using coroutines, you can write the code in this latter style,
      with the explicit state machine replaced by the implicit program
      counter,
even
if the rest of the program needs to work
      by passing each output byte to a function call.
In other words, you can write this part of the program ‘the way
      it wants to be written’ – the way that is most convenient for
      the nature of what the code has to do. And you didn’t have to
      force the
rest
of the program to change its structure
      to compensate. That might have required equally awkward
      contortions elsewhere, in which case you’d only have moved the
      awkwardness around, and not removed it completely.
Coroutines give you greater freedom to choose the structure of
      each part of your program, independently of the other parts. So
      each part can be as clear as possible.
Coroutines mean never having to turn your code inside
      out.
Versus conventional threads
In the 1990s and early 2000s, that was the only argument I felt
      I needed in favour of coroutines. But now it’s 2023, and
      coroutines have another competitor: multithreading.
Another way to solve the code-structure dilemma in the previous
      section would be to put the decompression code into its own
      thread. You’d have to set up a thread-safe method of giving it
      its input values – say, some kind of lock-protected queue or ring
      buffer, which would cause the decompressor thread to block if
      the queue was empty, and the thread providing the data to block
      if it was full. But then there would be no reason
      to
pretend
either side was making a function call when
      it really wasn’t. Each side
really would
be making a
      function call to provide an output byte or read an input byte,
      and there would be no contradiction, because the call stacks of
      the two threads are completely independent.
One of my software
      projects,
spigot
,
      is a complicated C++ program completely full of coroutines that
      generate streams of data. I was chatting to a friend recently
      about the possibility – in principle – of rewriting it in Rust.
      But I don’t actually know a lot about Rust yet (if I did try
      this, it would be a learning experience and a half!), and so of
      course I asked: ‘What about all the coroutines? Would I
      implement those using async Rust in some way, or what?’
My Rust-programmer friend replied: no, don’t even bother. Just
      use threads. Turn each of
spigot
’s coroutines into
      ordinary non-async Rust code, and run it in its own thread,
      passing its output values to some other thread which will block
      until a value is available.
It’ll be fine. Threads are
      cheap.
I have to start by acknowledging my personal biases:
      my
first
reaction to that attitude is purely emotional.
      It just gives me the heebie-jeebies.
My own programming style has always been single-threaded
      wherever possible. I mostly only use extra threads when I really
      can’t avoid it, usually because some operating system or library
      API makes it impossible, or
astonishingly
awkward, to
      do a thing any other way.
I’ve occasionally gone as far as parallelising a large number of
      completely independent computations using some convenient
      ready-made system like Python
multiprocessing
, but
      I’m at least as likely to do that kind of thing by putting each
      computation into a completely separate
process
, and
      parallelising them at the process level, using
      a
make
-type tool or GNU
parallel
.
Partly, that’s because I still think of threads as heavyweight.
      On Linux, they consume a process id, and those have a limited
      supply. Switching between threads requires a lot more saving and
      restoring of registers than an ordinary function call,
      and
also
needs a transfer from user mode to kernel mode
      and back, with an extra set of saves and restores for that. The
      data structures you use to transfer data values between the
      threads must be protected by a locking mechanism, which costs
      extra time and faff.
Perhaps
all of these
      considerations are minor in 2023, where they were significant in
      2000? I still
feel
as if I wouldn’t want to commit to
      casually making 250 threads in the course of a
      single
spigot
computation (which is about the
      number of coroutines it constructs in the course of computing a
      few hundred digits
      of
e
π
−
π
),
or
to doing a kernel-level thread switch for every single time one
      of those threads passes a tuple of four integers to
      another.
spigot
is slow enough as it is – and one
      of my future ambitions for it is to be able to parallelise 1000
      of
those
computations! But I have to admit that I
      haven’t actually tried this strategy and benchmarked it.
      So
maybe
I have an outdated idea of what it would
      cost.
Also, I think of threads as
dangerous
. You have to do
      all that locking and synchronisation to prevent race conditions,
      and it’s often complicated, and easy to get wrong. My instinct
      is to view any non-trivial use of threads as 100 data-race bugs
      waiting to happen. (And if you manage to avoid all of those,
      probably half a dozen deadlocks hiding behind them!) Now in
      this
particular
conversation we were talking about
      Rust, and that’s a special case on this count, because Rust’s
      unique selling point is to guarantee that your program is free
      of data races by the time you’ve managed to get it to compile at
      all. But in more or less any other language I think I’m still
      right to be scared!
So I have strong prejudices against ‘just use real threads,
      it’ll be fine’. But I accept that I
might
be wrong
      about those. Supposing I am, are there any other arguments for
      using coroutines instead?
One nice feature of everything being in the same system thread
      is debuggability. If you’re using an interactive debugger, you
      don’t have to worry about which thread you’re debugging, or
      which thread a breakpoint applies to: if the whole overall
      computation is happening in the same thread then you can just
      place a breakpoint in the normal way and it will be hit.
And if you prefer debugging via ‘recompile with print
      statements’, that’s
also
more convenient in a
      single-threaded setup where the transfers of control are
      explicit, because you don’t have to worry about adding extra
      locks to ensure the debug messages themselves are atomic when
      multiple threads are producing them. You might not mind having
      to do fiddly lock-administration when you’re setting up
      the
real
data flow of your program, but it definitely
      slows down investigation if you have to do it for every
      throwaway print statement!
But another nice thing about coroutines is that they’re easy
      to
abandon
. If a thread is in the middle of blocking on
      a lock, and you suddenly discover you no longer need that thread
      (and, perhaps, not the one it was blocking on either, or 25
      surrounding threads), then depending on your language’s
      threading system, it can get very painful to arrange to
      interrupt all those threads and terminate them. Even if you
      manage it at all, will all the resources they were holding get
      cleaned up? (File descriptors closed, memory freed, etc.)
I don’t think thread systems are generally great at this. But
      coroutines
are
: a suspended coroutine normally has an
      identity as some kind of actual object in your programming
      language, and if you destroy or delete or free it, then you can
      normally arrange for it to be cleaned up in a precise manner,
      freeing any resources.
Using
spigot
as an example again: most of its
      coroutines run indefinitely, and are prepared to yield an
      infinite stream of data if you want them to. At some point the
      ultimate consumer of the whole computation decides it’s got
      enough output, and destroys the entire web of connected
      coroutines. Using C++ with preprocessor-based coroutines, this
      is reliably achieved with zero memory leaks. I’d hate to have to
      figure out how to terminate 250 actual system threads as
      cleanly.
Also, having a language object identifying the coroutine
      instance can be used for other stunt purposes. I’ll talk more
      about that in
a later section
.
So
I
still prefer coroutines to threads. But I have to
      acknowledge that my reasons are a little bit more borderline
      than the reasons in the previous section.
(However, this discussion is all about
pre-emptive
threads.
Cooperative
threads which yield to each other
      explicitly are a different matter, and I’ll talk about
      those
later
as well.)
The subjective view: why do
I
like
      them so much?
This is already the kind of essay where I acknowledge my own
      bias. So I should also admit the possibility that it’s not so
      much that coroutines are objectively amazing, but rather, that
      they appealed especially strongly to
me personally
for
      some reason that doesn’t apply to everybody.
I have a couple of theories about what that reason might be, if
      there is one.
“Teach the student when the student is ready”
One possibility is that the concept was presented to me at
      exactly the right stage in my education.
I’d already been programming for a number of years when I
      read
TAOCP
, so I’d already felt for myself the
      frustration of having to write a piece of code ‘inside out’ –
      that is, in the form of an explicit state machine that I’d
      rather have avoided – and I hadn’t thought of any way to make
      that less annoying. So when Donald Knuth helpfully presented me
      with one, I pounced on it with gratitude.
But if I’d encountered the idea of coroutines
      earlier,
before
I’d felt that frustration, then I might
      not have appreciated it as much. It would have been one among
      many concepts that went through my brain as I read the books,
      and I’d have thought, ‘ok, fine, I expect that’s useful
      for
something
’, and then I’d have forgotten it (along
      with half of the rest of
TAOCP
, because there’s
      a
lot
of stuff in there!). And perhaps I might not have
      managed to recall it later, when the problem did appear in my
      life.
Conversely, the idea of coroutines might
also
have had
      less impact on me if I’d learned about it
later
. I have
      a strong suspicion that if I’d spent another (say) five years
      writing pieces of code inside out because I had no idea there
      was another option, I’d have got much
better
at writing
      code inside out, and much more used to it, and then the
      opportunity to avoid having to do it wouldn’t have seemed like
      such a huge boon any more.
Also, by that time, I’d probably have thought of some actual
      advantages to the inside-out state-machine style of coding, and
      started making use of them. There are often silver linings to be
      found in situations like this. In this case I can’t say for sure
      what they might be (since I never
did
become that
      practised at the skill); but one possibility that springs to
      mind is that an explicit list of states might make exhaustive
      testing more convenient (you can ensure you’ve tested every
      state and every transition). But whatever the compensating
      advantage might be, once I’d noticed it, I’d have been reluctant
      to lose it for the sake of (as I would have seen it)
      not
that
much extra convenience.
(This is probably related to Paul Graham’s idea of
      the
Blub
      Paradox
, in which you look at a less powerful language than
      your favourite one and you
know
it’s less powerful,
      because it lacks some feature you’re used to, and you can’t
      imagine how you’d get anything done without that. But you look
      at a more powerful language that has features yours doesn’t, and
      whatever they are, you seem to have been getting along fine
      without them – so you conclude that they can’t be
that
important, and that the ‘more powerful’ language isn’t that much
      better really.)
So perhaps it’s just that coroutines hit me at precisely my
      moment of peak frustration with exactly the problem they solve,
      and that’s why I adopted them with so much enthusiasm.
They suit my particular idea of code clarity
When you look at an existing piece of code, there are two
      different ways you might want to understand it.
One way is:
on its own terms, what does this code do, and
      how do I modify it to do it differently?
For example, in
      the
decompressor example
a few
      sections ago, suppose you wanted to look at the code and figure
      out what the compressed data format was – either to write a
      specification, or to check it against an existing specification.
      Or suppose someone had just
changed
the specification
      for the compressed data format, and you had to adjust the code
      for the new spec.
For that purpose, it doesn’t really matter how the code fits
      into the rest of the program. In fact you don’t even need
      to
see
the rest of the program. You could figure out
      the format from
either
of the code snippets I showed
      (the one with a state machine, or the one that
      calls
stream.getbyte()
), and it wouldn’t matter at
      all that the rest of the program hasn’t even been written. In
      both cases, you can see that the code is getting a stream of
      bytes from
somewhere
, be it a caller or a subroutine;
      you can follow the logic through and see what bytes cause what
      effects; if you’re updating the code, you just have to follow
      the existing idioms for input and output.
But although you
can
do that level of work on either
      version of the code, it’s much easier to do it on the version
      that calls a ‘get byte’ function. At least, I think so; if
      anyone actually finds the state machine version
easier
to work with in that kind of way, I’d be interested to know
      why!
But the other way you might want to understand a piece of code
      is:
how does this fit into the rest of the program, and how
      can I change that?
If you had no interest at all in the
      compressed data format and no reason to think this decompressor
      was delivering incorrect output, but you were concerned with
      what was being done
next
with the data being
      decompressed, then you’d want to find out not ‘what bytes are
      output, and how can I change that?’, but ‘when a byte is output,
      where does it go next, and is it the right place, and how do I
      reroute it to somewhere else?’.
For
this
purpose, coroutines often make things less
      clear, rather than more. That’s especially true if they’re based
      on my C preprocessor system, because a person coming fresh to a
      function in that style is going to see some
      weirdo
crReturn
macro, look up the definition, be
      further baffled (it’s fairly confusing if you don’t already
      recognise the trick), and probably conclude that I’m throwing
      obstacles in their path on purpose! But other less ad-hoc
      coroutine systems have the same property; for example, in C++20
      coroutines, the mechanism for dealing with yielded data values
      lives in a ‘promise class’ type, which is inferred from the type
      signature of the coroutine itself by a system of template
      specialisations that could be almost anywhere in the source file
      or any of its header files. If there isn’t clear documentation
      somewhere in your code base, it might be legitimately quite hard
      to find out what happens to data after it leaves a C++20
      coroutine; you might very well find that the simplest way to
      answer the question was to step through the yield in a debugger
      and see what happened next.
Which of these kinds of clarity is more important? Of course,
      both of them
are
important, because both are things you
      might need to understand, or fix, or update in your code. But if
      you spend 90% of time working on the code in one of those ways,
      and 10% of your time in the other way, you’re going to prefer
      the kind of clarity that helps you 90% of the time over the kind
      that helps you 10% of the time.
And it so happens that my own preference skews towards the
      first kind. Perhaps that has to do with the types of program I
      work on. All my life I’ve gravitated to programs that solve
      complicated problems, because that’s the kind of thing I enjoy
      doing. In those programs, the individual subproblems are
      complicated and so are the pieces of code that deal with them;
      the data flow between them is a small part of the overall
      system. So I don’t want to make debugging each sub-piece of code
      harder, just for the sake of making the data flow more explicit.
      I’d rather each piece made sense on its own terms at the expense
      of the data flow being a little more opaque.
This is also one example of a more general question. Is it
      better for each program to effectively define its own local
      customised variant of the language it’s written in (via very
      elaborate support libraries, metaprogramming tricks like macros,
      and the like), so that the learning curve takes a long time to
      climb, but you can work really effectively once you’ve climbed
      it? Or is it better to avoid diverging too much from the
      standard ways to use a language, so that a new programmer can
      get up to speed quickly?
Again, my preference skews toward the former. I value the
      ability to make my own life easier if I’m spending a long time
      in a code base. And I don’t much mind climbing the learning
      curves for other people’s differently customised coding
      environments, because I often learn something in the process
      (and maybe steal any good ideas I find). But I know that there
      are other people who are much more in favour of sticking to the
      orthodoxy.
(However, that’s only an argument against coroutines as long as
      they
aren’t
the orthodoxy. With more mainstream
      adoption, perhaps this argument is weakening. Generators in
      Python are
definitely
mainstream now: I’ve occasionally
      had a code reviewer tell me to use them
more!
)
Techniques for getting the most out of coroutines
Of course, another reason why one person might find a language
      feature more useful than someone else is that they’re better at
      using it: better at spotting cases where it’s useful, better at
      getting the most out of it when they do use it. And let’s not
      forget the skill of
avoiding
using it when
      it
isn’t
useful, so that you don’t get annoyed by
      situations where it’s not really a good fit.
Here’s a collection of my thoughts on when and how to use
      coroutines for best effect.
When to use coroutines, and when not to
My first general piece of advice is:
don’t be all-or-nothing
      about it
. Coroutines are useful in many situations, but
      they’re not the best tool for
every
job.
Programming language features are conveniences, not moral
      imperatives. They exist to make your life easier. So in a case
      where a feature
doesn’t
make your life easier, it’s OK
      not to use it.
(As far as I’m concerned, this applies to any language feature,
      not just coroutines. Another good example is recursion: it’s a
      very powerful and useful technique, but I have no time for
      languages that force you to use it for
everything
, even
      simple looping constructions. Especially if they also require
      you to learn all the tricks of passing extra parameters to
      permit tail recursion: to my way of thinking, that’s a clear
      sign that you’re trying to turn something into recursion that
      doesn’t really
want
to be written that way. Similarly,
      not everything needs to be a class – sorry, Java – and not
      everything needs to be immutable – sorry, Haskell.
      Multi-paradigm is the One True Way, because it’s the only way
      that doesn’t insist that there’s a One True Way!)
As I said in an earlier section, precisely one of the good
      things about coroutines is that they give you the freedom to
      structure each part of a program in the way that’s most useful,
      independently of the rest. In particular, that includes the
      freedom to
not
use a coroutine in a particular
      situation, if you don’t want to!
Coroutines are useful when successive calls to a function need
      to behave differently, in a way that ‘looks like control flow’.
      That’s hard to define, but after a while, you know the kind of
      thing when you see it: if the full sequence of function calls
      wants to exhibit a number of different behaviours one after
      another, or repeat an action lots of times with different
      actions coming before and after it, or diverge into two totally
      different sequences of operations based on some input condition
      (especially if you then re-converge into some later behaviour
      that looks the same regardless), or most especially repeat a
      sequence of things that
also
include sub-repetitions
      and conditionals of their own. Those are all the kinds of thing
      that would be very natural to write using sequential code, or
      loops, or if-statements, or nestings of those things – so once
      you recognise that ‘control flow nature’, consider writing it
      as
actual
control flow, in a coroutine.
On the other hand, some things just
don’t need
to be
      coroutines. If a function needs to do basically the same thing
      every time, you
could
write it as a coroutine anyway,
      containing nothing but an infinite ‘while true: do thing’ loop,
      but there wouldn’t be any real point. That’s just boilerplate
      that makes simple code more complicated for the sake of it. In
      that situation, don’t bother!
Types of code that might usefully become
      coroutines
Just waving my hands and saying ‘spot things that look like
      control flow’ isn’t the most helpful advice in the world, of
      course! So in this next section I’ll mention some things I’ve
      found them useful for in the past.
In coming up with the list, I found it convenient to categorise
      coroutines according to whether they yield to get inputs or to
      produce output or both, and to what other pieces of code.
Output only: generators
One of the simplest kinds of coroutine, and perhaps the most
      familiar to at least Python
      programmers
, is the kind that yields values to a
      consumer, but its input comes either from the parameters it was
      passed on creation, or from ordinary function calls.
(Of course, those function calls might be to the ‘next’ method
      of other generators, in which case you can look at this as
      taking input from a different coroutine after all! But only
      semantically: in a
later section
I’ll mention a performance concern relating to this.)
If a coroutine only generates output, then there’s a third
      alternative to making it a coroutine (as well as the
      state-machine and thread options discussed earlier): you can
      simply make it compute
all
its output ahead of time,
      and return it in full as a list or array. This gives you all the
      same advantages in terms of writing the control flow in a
      natural and readable style. For example, here are two versions
      of a simple function that finds the ‘record-breaking’ values in
      a list, i.e. every value that is larger than all the ones before
      it:
# Written as a generator
def record_breaking_values(inputs):
    it = iter(inputs)
    best = next(it)
    yield best
    for value in it:
        if value > best:
            best = value
            yield best
# Ordinary function that just returns a list
def record_breaking_values(inputs):
    it = iter(inputs)
    best = next(it)
    records = [best]
    for value in it:
        if value > best:
            best = value
            records.append(best)
    return records
In that example, the ‘just return a list’ function is one line
      longer because of the actual
return
statement. But
      that’s a trivial concern. (And I could have made it a line
      shorter instead, if I’d eliminated the
best
variable and just checked
records[-1]
, but then the
      two pieces of code wouldn’t have matched so clearly.) The point
      is that the control flow inside the function is exactly the
      same, and the algorithm is equally clear to a reader, and
      equally easy to modify.
The advantages of the coroutine version over this are space and
      time. The space advantage is obvious: if that returned list
      is
long
, then it’s nicer to avoid ever having to store
      all of it in memory at once, and instead, throw away each value
      after it’s been used. This doesn’t reduce flexibility, because
      (at least in Python) there’s a very concise idiom for turning
      the output of a generator back into a list at the call site if
      you really do need it all available at once.
(Of course, this is exactly the same reason that Unix provides
      a system for piping data between processes, in place of the more
      obvious approach of writing the data to an intermediate
      temporary file. One way to look at coroutines is that they’re
      the in-process analogue of a Unix
      pipe
!)
The time advantages are more subtle. In fact it’s not
      immediately obvious how there’s a time advantage at all: surely
      the same
calculations
have to happen, whether we select
      the record-breaking values in advance of using them or
      interleaved with using them.
And, of course, that’s true. If we really are going to
      use
all
the returned data, then the
overall
time taken to do the calculations is the same.
But sometimes we’re concerned with intermediate timings as well
      as the overall time. For example, if an interactive program
      needs to output the next value in a sequence when the user
      performs a UI action, then it’s nicer if the time taken to
      compute that value is reasonably bounded, rather than the
      program
occasionally
saying “Hold on, I need to
      precompute the next 10000 items before I can give you the
      first of them…”
And sometimes we’re
not
intending to use all of the
      returned data. Another way to look at generator-style coroutines
      like this is that they’re a form of
lazy evaluation
: no
      value in the logical output list is computed until another part
      of the program actually needs it, and that means that
      if
nothing
ever needs the value, we never wasted the
      time of computing it. In the interactive scenario, you’d
      be
particularly
annoyed at the program wasting your
      time on precomputing the next 10000 output values if you were
      intending to look at the first ten and then quit the program!
One special case of this, where you
really can’t
compute the entire intermediate list up front, is if the
      intermediate list is potentially infinite! Some natural
      generators will just keep on and on generating data, and the
      only way to
ever
stop them is by their consumer getting
      bored and discarding them.
In any case, the takeaway from this is: any time you see a
      function that constructs and returns a list, if it functions in
      more or less ‘append only’ mode (that is, it builds the list up
      from start to finish, and doesn’t have to refer back to an
      unlimited number of the existing items to decide what to append
      next), it’s worth considering whether it would be clearer
      written as a generator-style coroutine instead, if your language
      makes it convenient.
Input only: consumers
If I’ve had a section for output-only coroutines, then
      obviously I need a section for input-only ones.
At least in normal languages where a coroutine is a special
      kind of function, these don’t often seem to be very useful. It’s
      commonplace to have one piece of code producing data and passing
      it to another that consumes it, but you usually only
      need
one
of them to be a special coroutine- or
      generator-type function; the other can just be a normal
      non-coroutine-style function that invokes the producer coroutine
      when it needs another item, e.g. by calling
next()
on a Python generator.
You generally
can
write the two pieces of code the
      other way round, so that the producer is an ordinary function
      and the consumer is a coroutine. But it doesn’t often seem to
      be the easiest way to do things.
Partly, that’s because languages don’t make it quite as easy.
      In Python, for example, you
can
pass data to a
      generator by calling
g.send(value)
and retrieve it
      inside the routine as the return value of the
yield
operator; but it’s awkward that the generator starts off in a
      state where its code hasn’t run at all yet, so you have to faff
      with it to get it to the point of first input. But other systems
      don’t have this awkwardness, or at least, you can arrange not to
      have it; for example, C++20 coroutines allow you to configure
      whether your coroutine should start off suspended, or run to the
      point of first yield / await. (Or other options.)
More importantly, the consumer end of the data pipeline is
      probably the one that’s taking the program’s main action. So you
      probably want to make
sure
it completes. I mentioned
      above that one of the virtues of coroutines is often that
      they’re safely discardable (via the language’s cleanup or
      destructor system) if you want to abandon the computation half
      way through – but that stops being a virtue if the computation
      in question is the one you want to be sure of
not
accidentally abandoning!
So I think it generally makes sense to have the producer end of
      the system be an easily discardable coroutine, and the consumer
      end be ‘normal’ code. That way, if the producer encounters an
      exceptional condition and can’t carry on producing data (e.g. a
      file it was reading from ended abruptly, or contained invalid
      data), the consumer can catch the exception and ensure it does
      something sensible, like switching to a fallback strategy, or
      deleting its half-written output file, or at the very least
      producing a useful error message. You probably don’t want it to
      be silently discarded.
Update, 2025-03-25
: on the other hand, here’s a
      case where it
does
make sense to have consumer-style
      coroutines rather than generator-style.
Suppose you’re reading a long stream of input of some kind, and
      you want to process it in multiple ways – say, to generate
      various different summaries or filtered versions of it. If your
      various summaries are generated by coroutines, the main thing
      you want is to keep them synchronised with respect to the input
      stream: if one of the coroutines reads a long way ahead of
      another, then the process must buffer all the data in between,
      so that it’s still available to deliver to the rearmost
      coroutine when it catches up.
In that situation, it makes sense to have the coroutines be
      consumers, and have a single producer that reads the input
      stream and passes each record to all of them in turn. In Python
      you might write something like this, using
      the
send()
method provided by Python generators
      which causes the sent value to be returned from
      the
yield
operator inside the function:
# Example consuming coroutine
def consumer(some_parameters):
    # Do any necessary setup

    while True:
        # Wait until an input record is available
        record = yield None
        if record is None: # signals end of stream
            break

        # Now do per-record processing

    # Do any end-of-stream processing
# Top-level function that reads the input
def toplevel(input_stream):
    # Construct a list of consumers
    consumers = [
        consumer(params)
        for params in list_of_consumers_wanted
    ]

    # Run each one to the point of first yield
    for consumer in consumers:
        next(consumer)

    # Now read through the input stream
    for record in input_stream:
        # And pass each record to every consumer
        for consumer in consumers:
            consumer.send(record)

    # Finally, tell each consumer the stream has ended
    for consumer in consumers:
        consumer.send(None)
You can see that this is a bit awkward. As I mentioned above,
      in Python each consumer starts off suspended at the very start,
      so the top-level function has to call
next()
on
      each consumer once to get it started, so that it will run up to
      the first
yield None
and be waiting for a return
      value. Then, if the consumer needs to do any processing at the
      end of the stream, you have to explicitly signal to it that the
      end of the stream has happened, so that it can resume running
      and do whatever it needed to do at the end of the stream
      (perhaps writing some kind of summary statistics of everything
      it noticed). With generators the more normal way round, both of
      these would be more ergonomic. But in this situation, keeping
      all the consumers synchronised in the stream is a more important
      concern.
Separate input and output: adapters
Once you’ve connected a producer to a consumer, the next
      natural step is to have something in the middle be both at once,
      consuming values from one side and emitting them to the other
      side.
The
record_breaking_values()
example I showed in
      Python earlier is already an example of one of those, depending
      on how you look at it. If you pass it a static thing like a
      list, then it’s just a producer coroutine, doing computation
      based on its original parameters; but if you pass it another
      generator as an argument, then it ‘yields’ to that generator by
      calling
next()
on it, and yields to its consumer by
      using the actual
yield
statement.
There are lots of natural adapters of this kind that you might
      usefully write as coroutines. Again, it’s not
always
the right thing to write them that way, but it can very easily
      be.
For example, here’s a tiny Python generator function that I put
      in a lot of my programs, because I often find I want to use it,
      and despite being so simple, it’s not in the standard
      library:
def cyclic_pairs(inputs):
    it = iter(inputs)
    prev = first = next(it)
    for curr in it:
        yield prev, curr
        prev = curr
    yield prev, first
Given a list of inputs such
      as
a
,
b
,
c
,
d
,
e
, this returns
      each pair of adjacent list elements as a tuple, so that you get
      (
a
,
b
), (
b
,
c
), (
c
,
d
)
      and (
d
,
e
) as outputs
.
      Finally, it produces the pair that ‘wraps round the end’,
      consisting of the last element and the first, in this case
      (
e
,
a
).
If you knew the input was in the form of an already-complete
      list, you could write this easily enough by iterating over the
      list indices, and returning
(list[i], list[(i+1) %
      len(list)])
. But if you write it in this form then it can
      take any iterable as input – including another generator, which
      perhaps doesn’t even know what all its output is going to be
      yet.
What makes this a natural use case for generators? It’s the
      special cases at the start and the
      end
. If every input
      value was treated exactly the same, then you could just as
      easily write this as a tiny class storing the
prev
variable, with a
__call__
method that constructed
      each tuple and updated
prev
. But in reality,
      the
first
element from the input iterator must be
      treated specially (in that we still put it
      into
prev
but don’t yield a tuple at all), and when
      we reach the end, we have an extra thing to do (namely yielding
      that final wraparound tuple). You
could
fake that up in
      your class, perhaps by special-casing
prev=None
(but what if the input iterator contained some
      legitimate
None
values itself?), or more likely by
      a system of flag variables in the class. But then you’re in
      ‘explicit state machine when you didn’t really want one’
      territory – so it’s easier just to write code like this, which
      says directly, in sequence, what things you want to do, in what
      order.
Adapters like this fit nicely into the ‘Unix pipeline’ model,
      as I described a couple of sections earlier. So they’re still
      only a performance improvement, in space and maybe time, over
      doing things the pedestrian way with intermediate lists.
Input and output talking to the same entity:
      protocols
Now we come to the case where coroutines deliver more than a
      performance optimisation: where they do both input and output,
      but the output goes to the
same entity
that’s providing
      the input.
It doesn’t exactly matter what that entity
is
: it
      might be another part of the same program, or it might be a
      human interacting with the program, or it might be another
      program at the far end of a network connection. But if the
      entity at the other end has to see your outputs so far before
      deciding what your next input is, and you have to do the same to
      generate
your
next output, then this type of
      coroutine
can’t
be rewritten as a function that just
      generates the whole output list up front.
One of Knuth’s examples in
TAOCP
was a piece of
      code that implements a chess-playing algorithm. That’s exactly a
      case of this kind: each time you output a move, you have to wait
      to find out what my responding move is before you can even
      decide what moves you can
legally
play next, let alone
      which one is best. You can imagine a function like this talking
      to a human player through some user interface code – but you
      could also set two copies of it playing against each other,
      yielding control flow back and forth each time one of them made
      a move.
(On the other hand, I don’t know that chess is a good case for
      coroutine style, because as far as I know, chess algorithms
      these days work by analysing whatever board position they’re
      given, and if they retain any state from the previous move it
      will only be in the form of cached evaluations of potential
      future game states. So a ‘next chess move’ function probably
      wouldn’t want to be a coroutine after all. But some games’ rules
      – or optimal strategies –
do
go through sequential
      phases that would suggest a coroutine-structured playing
      function.)
But gaming is a frivolous use of this idea. A much more
      practical one is network protocols. The reason coroutines occur
      throughout PuTTY is because they’re so useful for implementing
      sequential network protocols, under the constraint that the top
      level of your program is an event loop waiting for whatever
      input event happens next out of network connections, user input,
      and sometimes timers.
A good example is the key exchange layer of the SSH protocol.
      The two sides exchange setup packets that list all the different
      cryptographic algorithms they’re prepared to use; out of those
      options, they select the best one that both sides understand,
      and then exchange several packets to perform a key exchange
      according to that algorithm. Having done that, each side
      installs a new set of cryptographic keys, and then exchange
      encrypted packets implementing the actual interactive login
      session – until one side decides it’s time to refresh the
      cryptography, and sends another key-exchange setup packet.
The sequence of packets within each key exchange method is
      different; only one of those sequences is used; and the whole
      thing takes place in a loop, restarting every time a new key
      exchange is needed. These are all markers of ‘looks like control
      flow’, and make it very natural to write the code in a style
      like this:
function key_exchange() {
    send(KEXINIT); // key exchange initialisation packet
    wait for other side’s KEXINIT;
    outer loop {
        decide what key exchange type we’re doing;
        if (it’s this type) {
            send this;
            expect that;
            send some response;
        } else if (it’s some other type) {
            expect the other side to send a packet first;
            send a totally different response packet;
        } else {
            // potentially more and more cases like this
        }
        install new keys;
        inner loop {
            get next packet from server;
            if (it’s KEXINIT) {
                // time to do another key exchange
                send our own KEXINIT;
                break from inner loop; // so we return to top of outer loop
            } else {
                pass the packet on to the next layer up;
            }
        }
    }
}
This function is structured as if it’s calling a subroutine to
      retrieve the next packet from the other side of the connection.
      But in reality, it’s going to
be
called each time a
      packet arrives – so we have to either make it a coroutine, or
      turn it inside out by setting up an explicit state machine. I
      think keeping the code in this nice sequential form
      is
far
preferable, so coroutines it is!
In fact, this kind of pattern recurs throughout SSH. The
      ‘packets’ that are arriving in the code shown above are built up
      from the actual stream of bytes coming from the network by means
      of reading an initial few bytes giving the packet length, then
      reading that many more bytes to get the rest of the packet, then
      reading the authentication code at the end (if any); doing all
      the decryption and integrity checking, and finally, having a
      packet available to output. This code too wants to be written in
      a style where it calls a ‘wait for
n
more bytes of
      network data’ function – but, again, it’s
being
called
      from the main event loop when data comes in on the network
      socket. So that layer too is a coroutine, in the simpler
      ‘adapter’ style where the input and output are separate: it
      consumes bytes from the event loop, and periodically yields a
      completed packet to the key-exchange layer shown above.
And the ‘next layer up’ – mentioned at the end of the above
      pseudocode – does all of this
again
. Initially, it’s
      the user-authentication layer of SSH, which might prompt for a
      password, or use a public key, or do something more complicated
      still; any of those might fail, in which case it has to loop
      back round and try the next fallback approach. So that’s very
      natural to write as a coroutine as well. The whole structure of
      SSH is almost
designed
to be three coroutines stacked
      on top of each other!
(Once you’ve actually logged in, things get a bit less
      coroutiney. The ‘connection layer’ that takes care of running
      shell sessions is much less sequential. In PuTTY, it’s still
      structured as a coroutine, but
mostly
that coroutine
      sits in an endless while loop just responding to each packet as
      it comes in. That would normally be the kind of boring stateless
      code that it’s not really worth making into a coroutine at all –
      except that right at the start we have to do a few setup tasks
      like opening an initial session channel, so the coroutine
      consists of a small amount of sequential setup code
      and
then
the boring while loop.)
This isn’t an article about SSH alone, of course. That’s just a
      particularly good example. Many other network protocols are just
      as sequential. For example, PuTTY’s code to connect via an HTTP
      proxy is also structured as a coroutine.
In fact, that code has an extra wrinkle too. Sometimes, when
      authentication fails in HTTP, you can try again within the same
      network connection; but sometimes you have to close the
      connection to the HTTP server and open a fresh one. So there’s
      not just a sequence of operations
within
a network
      connection: there’s also a sequence of
connections
involved. In PuTTY, this is all handled with a single HTTP proxy
      coroutine: sometimes it yields a special return value to its
      caller saying ‘please close the connection, open a fresh one,
      and call me back when that one’s ready’. Then it can go back
      round to the top of its loop and continue trying to
      authenticate.
More general, and miscellaneous
In all of the previous subsections, I’ve shown coroutines with
      at most one input channel and at most one output. Of course, you
      can also have more than one of each.
There are two conceptually different ways that a coroutine
      might consume two input streams. One is that it yields to
      a
specific
input stream each time it wants a new value,
      so that it’s in control of how fast the two input streams
      deliver data. There are lots of examples of this in purely
      computational contexts: consider, for example, a function that
      merges two sorted lists, or zips together two or more streams by
      making a tuple of one element from each stream, or other things
      of the kind you might find in Python
itertools
.
The other approach, more suited to coroutines that are doing
      asynchronous I/O, is that the coroutine might yield in such a
      way that it will be resumed when
any
of the input
      streams has data available – no matter which one it is. For
      example, some of PuTTY’s SSH coroutines have to handle both
      network data and user input: the user authentication coroutine
      will sometime respond to a network packet by presenting a
      password prompt to the user, and then it has to receive the
      password that the user typed in return and construct the network
      reply packet. But there’s no guarantee of which is going to
      happen next, out of a network packet arriving and the user
      pressing a key. So the coroutine is resumed
      whenever
either
one happens.
That style of coroutine is tricky to write well, and I have
      some advice about it in later sections. Here, I just mention
      that it’s among the possibilities.
Another slightly unexpected ‘stunt’ use of coroutines is to use
      them to reconstruct the call-stack structure of ordinary
      subroutines: replace every normal function call with a
      coroutine-style yield operation which makes a newly constructed
      instance of the subroutine start running next, and whenever a
      coroutine terminates, resume the one that invoked it.
Why on earth is
that
a useful thing to do, you might
      ask? If we want something that behaves like an ordinary function
      call stack, doesn’t the typical programming language have one
      built in already?
I’ve found that useful in the past as a means of working around
      limitations of the true function call stack. In Python, for
      example, you can only nest function calls about 1000 deep, and
      I’ve sometimes needed to recurse much more deeply than that –
      e.g. running graph algorithms over a DAG with very long chains,
      such as a git repository. It’s surprisingly convenient to
      rewrite function calls and returns in a style like this…
# Before
def routine(x):
    i = subroutine(x+1)
    j = subroutine(x*i)
    return i+j
# After
def routine(x):
    i = yield Call(subroutine(x+1))
    j = yield Call(subroutine(x*i))
    yield Return(i+j)
… and then have a small piece of ‘executor’ code which
      maintains a stack of currently active generators in an array,
      and contains a loop which always resumes the innermost generator
      on the stack. If that yields a
Call
object
      containing another generator, push that one on the stack, so
      that it will be the one resumed next; if it yields
      a
Return
containing a return value, pop the stack,
      and pass the value to the new topmost generator when it’s
      resumed.
When I’ve done this in the past, my reason has always been to
      get round Python’s recursion depth limit. But I can think of
      other reasons for reifying your stack into explicit data
      objects.
One reason is so that those objects can be saved and restored.
      Given the right language support, you might be able to tweak a
      system like this to allow the entire state of a half-finished
      recursive computation to be written out to a disk file; then the
      program could be terminated, and when run again later, reload
      the file and carry on from where it left off. (Although you
      would also need a method of saving the
internal
state
      of each coroutine, which might be harder.)
Another is that once you replace the language’s built-in
      control flow with your own imitation, it becomes easy to extend
      or modify it. You could imagine adding a third kind of data
      object alongside
Call
and
Return
which
      had a different effect on the executor. For example, you might
      have two or more call stacks and switch between them,
      implementing ‘co-threads’ (which I’ll talk about more
      in
a later section
).
In fact, perhaps you might decide that keeping the active
      function calls in an array was itself a limitation you wanted to
      go beyond. Not all languages insist on a linear stack in that
      way. Scheme, for example, has multiple control-flow features
      (continuations and
dynamic-wind
) with the effect
      that the stack is replaced by a general DAG of function
      activations, and several branches of the DAG can be resumable.
      (This also means that the stack frames must be subject to
      garbage collection.) A technique like this could be used to
      implement continuations in languages that don’t have them
      natively!
Speaking of messing about with control flow, another stunt use
      of coroutines – in the right context – is to invent your own
      control flow
statements
, alongside standard things like
      ‘for’, ‘while’ and ‘if’.
Some languages encourage you to invent control flow primitives
      of your own, by means of making it easy to pass blocks of code
      to a function call:
function my_control_structure(code) {
    set up stuff;
    while (some condition)
        code.run();
    clean up stuff;
}

# now the braced block becomes the ‘code’ parameter to the above function
my_control_structure {
    statements;
}
The
wrong
way to implement this language feature is to
      literally wrap up the code block at the call site into a lambda
      function, and have the control-structure function execute the
      block using a normal function call. The problem with this is
      that then the code blocks don’t really run in the context of the
      containing function. They might be able to access the function’s
      local variables, by virtue of lexically scoped lambda capture,
      but the control flow is isolated. If one of those blocks
      executes a ‘return’ statement, then it only returns from
      the
block
, not the containing function (as it would if
      you executed the same return inside, say, a while loop). And if
      you want to ‘break’ from a loop implemented by these means, then
      executing the ‘break’ statement inside the lambda doesn’t work
      at all. This all makes your artificial control structure look
      ‘second class’ compared to the language’s built-in ones.
Instead of doing that, the
right
way – and some
      languages actually do this, such as Ruby – is for the
      control-structure function to be a coroutine. Instead of its
      code blocks being ordinary functions that it calls in the
      ordinary way, they should remain in the context of the original
      function, and the control structure should
yield
back
      to the original function, telling it which block to run next.
      Then custom control structures would be just as good as the
      standard ones, and wouldn’t behave surprisingly differently in
      edge cases
.
Of course, if you’re not using a language that already works
      this way, then finding a way to implement it can be tricky or
      impossible. But once I just about found a way to do it in C,
      combining
      my
preprocessor
      coroutine system
with
another
      preprocessor trick
for making custom control structures at
      all. In C++ you might do it more easily by having the macro at
      the call site expand to a range-
for
loop. It will
      depend on the language.
Coroutines large and small
That ‘control flow nature’ that makes a piece of code a natural
      fit for coroutines can occur at all scales, from the largest to
      the smallest.
Among the examples in previous sections, I’ve already shown
      examples at both ends of that spectrum. Some of the largest and
      most complicated parts of PuTTY’s SSH code, such as the key
      exchange or the user authentication protocol layers, are
      implemented as a giant coroutine. On the other hand, that
      tiny
cyclic_pairs
Python generator is not far off
      being the smallest possible piece of coroutine-shaped code
      that’s worth bothering to write.
It’s also worth considering various ways to slice up, or break
      down, the problem. In SSH the multiple protocol layers lend
      themselves nicely to being a coroutine
each
; they’d be
      much more unwieldy implemented as one single one. On the other
      hand, for some network protocols, a single coroutine might be
      suitable for running the entire network connection.
And in some other situations, you might have a variable number
      of coroutines, with each one tracking the progress of a single
      transaction
within
a network protocol. I have an
      example of that too in the PuTTY code: the SSH agent, Pageant,
      is mostly a non-coroutine loop that answers queries in whatever
      order they arrive – but whenever a client of the agent requests
      a signature from one of Pageant’s private keys, it spawns a
      small coroutine to handle the progress of
that specific
      signing request
, because sometimes it will need to prompt
      the user for a passphrase, loop round again if that didn’t work,
      be prepared to abandon the attempt if the user clicks Cancel,
      etc. This is all control-flow-shaped code – but it suited the
      problem best to have a coroutine for
each
signature
      request, not one for the whole connection.
So, when you’re on the lookout for coroutine-shaped parts of a
      program, don’t forget to look for the large ones, the small
      ones, and everything in between!
Activation energy
Of course, depending on the language, that might not be good
      advice after all.
In Python, writing a generator is made extremely easy. It’s no
      harder than an ordinary function; you just
      write
yield
at least once in the body, and
      everything is taken care of for you. So there’s no reason
      I
shouldn’t
write things like
      that
cyclic_pairs()
function as a generator, if
      it’s only a tiny bit clearer. There’s essentially no cost. The
      next five lines of my code would look a bit nicer as a
      generator? Fine, dash off a generator, why not?
But if you were writing in C++20, there’s a much higher barrier
      to entry. C++20 coroutines
      are
very
      expensive
to set up – not so much in runtime cost (though
      I’m sure there is
some
), but in programming effort. You
      have to write a whole ‘promise class’ with lots of methods
      explaining how the coroutine should behave in this or that
      circumstance. If the only actual coroutine you wanted to write
      was going to save you (say) five lines of code, then writing
      a whole C++20 promise class from scratch wouldn’t be a net win,
      because it would cost you a hundred or so lines to set up the
      necessary infrastructure. You have to
really want
coroutines to bother setting them up in a C++20 program.
However, C++20 does let you reuse the promise class for
      multiple coroutines that want to work in similar ways. So if you
      had
twenty
five-line snippets you wanted to write that
      way, it might become worth it. But if you’d already written the
      first 19 in ordinary non-coroutine style, then when you got to
      the break-even point, it might
still
not seem worth
      your while to go to the effort of writing the promise
      class
and
converting all the existing cases to use
      it…
(Also, this is only a temporary complaint about C++. C++23 will
      bring
std::generator
, which should make this kind
      of simple job
actually
simple again.)
Combine with input queues
In
TAOCP
’s presentation of coroutines, and many
      others, the whole point is that you yield to the other piece of
      code precisely when you have data to transfer. If a producer is
      constructing a stream of objects and sending them to a consumer,
      then you write the producer as if it has a function it can call
      for ‘here, I have this object for you’, and you write the
      consumer as if it has a function for ‘ok, what’s my next
      object?’, and there’s exactly one pair of transfers of control
      for each object that traverses the boundary.
But sometimes that’s not the best way to do it. When it’s not,
      don’t do it that way!
One case where it’s awkward is the
case I
      mentioned previously
of having a coroutine that can receive
      more than one type of input, and doesn’t know which one will
      come next. For example, PuTTY’s SSH authentication layer used to
      implement password / passphrase prompts itself, so it received a
      stream of events in which SSH packets and user keystrokes were
      interleaved, and any call to the main userauth coroutine might
      be providing
either
of those kinds of event.
But if you’re writing code in a coroutine-structured style,
      then in a lot of cases, you know which input type
you
want to see next – and it’s very annoying to have to put a
      handler for the other one after each yield. For example, if
      you’re
not
in the middle of presenting a password
      prompt to the user, what do you do with a keystroke when you
      receive one? Conversely, if you’re waiting for the user to
      finish typing a password, and another network packet comes in,
      what do you do?
In those early versions of PuTTY, I mostly ignored the problem.
      While the userauth coroutine was waiting for network packets, if
      it was called with a keystroke, it would simply discard it –
      drop it on the floor.
An effect of that was that you couldn’t open a PuTTY window and
      immediately start typing the first shell command you wanted to
      run in your session,
even
if you knew that
      authentication was going to succeed without needing any prompts
      (say, because you were using an SSH agent). You’d expect to be
      able to ‘type ahead’, and have your keystrokes buffered until
      the main shell session was ready to use them. Instead, for as
      long as authentication hadn’t finished yet, they’d just be
      thrown away.
After a while, that became annoying. I wanted keystrokes
      to
never
be dropped. But I also wanted to write my
      userauth coroutine in the most convenient way. What to do?
Instead of passing SSH packets or keystrokes directly to the
      userauth coroutine, I made two
queues
in the SSH layer,
      to hold SSH packets and user input respectively. So when the
      lower layer had a packet to deliver to the userauth layer, it
      wouldn’t pass the packet directly to the userauth function;
      instead, it would put the packet on the userauth layer’s
      incoming packet queue, and then call the userauth function with
      no arguments, just saying ‘hello, it’s worth waking up and
      checking your queues’. And the same went for user input.
This solved my problem. Now, when userauth knows the next thing
      it’s expecting is an SSH packet, it can run a little resume loop
      that says ‘Is there a packet waiting in my queue? If not,
      suspend, and look again when we’re resumed.’ If user input
      arrives in the meantime, it goes on the
other
queue,
      and will still be there when the userauth layer gets to a
      different place in the code where it needs some user input – or
      perhaps it won’t be consumed by userauth at all, and will be
      picked up by the connection layer (the one that runs shell
      sessions after you log in), so that you
can
type ahead
      into the shell prompt you expect to see later.
In particular, sometimes the userauth layer wouldn’t need to
      suspend itself at all. It would look at its queue and discover
      there was
already
something there, and charge straight
      on without ever having to yield.
(In C, using preprocessor coroutines, this little loop was the
      easiest way to wait for a particular one of the possible input
      events. If I were rewriting this code using the C++20 coroutine
      system, I could formalise it, by defining a
      specific
co_await
idiom for ‘now I want to wait
      until there’s something in this queue’. That could be set up so
      that it would avoid resuming the coroutine
at all
until
      that queue stopped being empty – and it could also automate the
      initial check of ‘maybe we don’t even need to suspend at all
      because we already have a packet waiting’.)
Another case where queues are useful is if the data objects are
      very small and numerous. For example, if you wanted to write a
      coroutine that received a stream of
bytes
from another
      part of the program – say, because the producer was a file
      decompressor, or the consumer was a file compressor – then it
      would be bad for performance to require two coroutine-transfer
      overheads per individual byte. Instead, the producer would
      prefer to provide as many bytes in one go as it conveniently can
      (especially since it might have read lots of them in a block
      from a file, or a decompressor might have generated a lot at a
      time from a run-length record or an LZ77 copy). But then the
      consumer might not need exactly that many for
its
next
      operation. So it would make sense to append bytes to a queue
      (probably in the form of a circular buffer, or chain of small
      buffers, or something else space-efficient per element). The
      producer could generate as much data as was convenient (or would
      fit in the buffer), and then yield at the point when producing
      the next byte would need actual effort; then the consumer could
      eat as much of the queue as possible, and yield back when it
      wanted more bytes than were available.
But, just like I’ve been saying about everything else in this
      article, don’t take it to extremes. Using an input queue or
      buffer isn’t
always
the right thing. One of the effects
      of representing a stream of data as a coroutine is that the
      stream is lazily evaluated: no element is computed until it’s
      really needed. So if some or all of the data values
      are
expensive
to compute, then either don’t use an
      intermediate queue at all, or else make sure you never put more
      than one thing in the queue
unless they’re easy
.
(
spigot
is a good example of this problem. The
      coroutines in that are mostly generators that yield streams of
      integer matrices. For some generators, the matrices are uniform
      and simple; for others, an occasional matrix
      is
exceptionally
costly to compute. So in that
      application, queues didn’t seem worth the effort; yielding
      exactly once per matrix is the simplest way to be absolutely
      sure that we never even start trying to compute a matrix until
      its consumer knows it’s needed.)
Combine with ambient pre-filters
Here’s one more trick on the theme of ‘only use coroutines for
      the coroutine-shaped parts’.
Sometimes, a stream of data contains things that have to be
      handled sequentially,
interleaved
with things that
      should be handled the same at any time.
An example of this is the key-exchange ‘transport layer’ of
      SSH. This includes all the packet types I
      mentioned
earlier
(the
KEXINIT
start packet, various sequences of
      packets to perform different key exchanges, and
      a
NEWKEYS
message to signal that you’re about to
      switch to the newly generated encryption keys); but
      it
also
includes a small number of messages that can
      arrive at any time and must be handled correctly when they do.
The handling isn’t always
difficult
. One key example
      is the
IGNORE
message, which either side may send
      at any time, and the other side – as suggested by the name –
      must ignore it. That’s the single easiest possible way to handle
      a packet.
But now suppose you’ve written your transport layer in the form
      of a coroutine. There will be lots of separate points in the
      code where you yield, wait for the next packet, and expect it to
      be of a particular type (typically, whatever comes next in the
      key exchange you’re performing). Now
every one
of those
      yield points has to have an extra check for
      the
IGNORE
message, which loops round to get the
      packet after it:
// What you’d like to write
function transport_layer() {
    // ...
    pktin = co_await PacketInputQueue;
    if (pktin.type != FOO)
        disconnect("got packet type %s, wanted FOO");
    // ...
}
// What you have to write instead every time
function transport_layer() {
    // ...
    while (true) {
        pktin = co_await PacketInputQueue;
        if (pktin.type != IGNORE)
            break;
    }
    if (pktin.type != FOO)
        disconnect("got packet type %s, wanted FOO");
    // ...
}
If you’ve got even ten or twenty yield points in your
      coroutine, this is a lot of tedious boilerplate code – and
      worse, a lot of places to accidentally leave out that extra
      clause, and introduce a latent bug that will only show up when a
      server actually
does
happen to send
IGNORE
in that particular context. And it only gets worse when you have
      to support the rest of SSH’s any-time message types. Ignoring
      that
IGNORE
message
isn’t
the easiest
      thing in the world, it turns out!
So don’t do it that way.
Instead, a structure I’ve found useful is to have a
      ‘pre-filter’ on the queue, which isn’t part of the coroutine at
      all. Whenever new packets arrive on the queue, they’re seen
      first by the pre-filtering code. That will handle things that
      can arrive at any time, like
IGNORE
and its
      friends. The only remaining packets are the ones
      that
are
expected to appear in a sensible sequence
      that’s natural to write as a coroutine. And
those
are
      passed to the main transport-layer coroutine, which can handle
      them in the natural way, without having to do anything at a
      yield point that isn’t related to what that
particular
yield point is trying to achieve.
So this lets the coroutine handle only the coroutine-shaped
      parts of the protocol: the things that happen in sequences, or
      conditionally, or in loops, and look like control flow.
      Meanwhile, the awkward things that can interrupt your nice
      orderly control flow are simply removed from the coroutine’s
      view of the input and handled by a central dispatch function.
      Then each style of code can do what it does best; or, looking at
      it the other way round, each part of the problem can be solved
      in the way that’s most natural for that part.
(
How
do you wedge this pre-filter system into a world
      organised by coroutines? PuTTY uses C preprocessor coroutines,
      in which there’s a convenient slot within the coroutine function
      itself – just before the
crBegin
macro – where you
      can put code that will run on every single resume, before
      control is transferred to wherever the function last suspended.
      For languages which implement coroutines natively, that slot
      probably doesn’t exist, so you’ll have to do it the more
      pedestrian way of hiding the coroutine resume operation behind a
      separate wrapper function, and having that wrapper do any
      pre-filtering necessary before resuming the actual coroutine.)
The SSH packets I’ve been talking about here are fixed. They
      can be sent at any time at all in the protocol, and
      they
never
want to be handled by the coroutine code.
      But in other situations, there are message types which
      you
sometimes
want to handle in the sequential
      coroutine code, even though at other times you’d rather they
      were handled by the pre-filter so that the sequential code can
      concentrate on something else.
In this situation, you can still keep the sequential code in
      the coroutine and the any-time handlers in the nicely separate
      filter function, by means of the coroutine setting variables
      that affect how much the filter function filters. Then the
      coroutine can dynamically control what subset of the inputs it
      sees, and always focus its attention on the ones that behave
      sequentially.
Those variables can be as simple or as complicated as you like.
      It might be as simple as having a single boolean flag saying
      whether the coroutine would currently like to see whatever kind
      of thing is only sometimes interesting to it. Or you might need
      some kind of set variable saying which types of thing you
      currently care about. Or maybe the filter might need to be a
      complicated lambda function, who knows. It will depend on how
      much control you need to have over the filter.
One idea along these lines that I haven’t yet had the
      opportunity to try is to have a
lexically scoped
handler, installed for the duration of a particular block of
      code, and uninstalled again automatically by an object’s
      destructor. It might look something like this (details
      completely made up):
function event_stream_consuming_coroutine() {
    // Here, we can receive any event type
    event = co_await EventQueue;

    {
        // Install a handler for a particular event we don’t want
        // to be bothered with in the next loop
        HandlerInstaller hi(EventQueue, EVENT_BORING, lambda(event) {
            fixed code to handle this event;
        });

        // Now do some kind of a loop over the remaining event
        // types, which can assume EVENT_BORING never appears.
        while (some condition) {
            // imagine lots of subsidiary control flow here
            event = co_await EventQueue;
        }

        // At the end of this block, the HandlerInstaller object
        // goes out of scope, and its handler is uninstalled
    }

    // And here we’re back to being able to receive any event,
    // even EVENT_BORING
    event = co_await EventQueue;
}
The idea is that the
HandlerInstaller
class has a
      constructor which arranges to add the specified event type to
      the pre-filtering system sitting in front of this coroutine. In
      this example, I’ve also shown it taking a lambda function as an
      argument, so that we can say
what
to do with one of
      those
EVENT_BORING
events if it happens within
      this block.
Then, when the
HandlerInstaller
goes out of scope
      at the end of the block, its destructor runs, and uninstalls the
      handler again. So after the block
      ends,
EVENT_BORING
is no longer being filtered
      out of the coroutine’s input, and the
      final
co_await
could receive one.
I haven’t had a chance to experiment with this style yet,
      because you can’t do it with preprocessor coroutines. (Not even
      in C++, where you do have destructors. Preprocessor coroutines
      in C++ require all the coroutine’s persistent variables to be
      members of its containing class, so they can’t be scoped to
      sub-blocks of a function.) But you could do it in C++20’s native
      coroutines, where you get to declare block-local variables in a
      natural way. So when I write my first real system based on C++20
      coroutines, I might give it a try!
Coroutine paradigms
Finally, in this last section, I’ll talk about some different
      ways to
think
about coroutines, in the sense of what
      kind of thing they even are.
I’ve mentioned a couple of things of that kind in passing, in
      previous sections: I said that coroutines can be seen as the
      in-process analogue of a Unix pipe, or as the
      imperative-programming analogue of lazy evaluation (particularly
      something like Haskell’s lazy lists). But those were more about
      the kind of
tasks
you can use them for; the next few
      sections will be more about what they
are
than what you
      can use them as.
TAOCP
’s coroutines: symmetric, utterly stackless
Knuth’s presentation of coroutines in
The Art of Computer
      Programming
calls them a ‘generalisation’ of subroutines.
      That characterisation doesn’t make sense in all contexts, but in
      that particular context, it does.
In
TAOCP
, all the example programs are written in
      machine code for the fictitious MIX architecture. MIX is strange
      by modern standards – entire generations of CPU architecture
      fashion have come and gone
between
MIX and the
      more-or-less RISC architectures of today.
In particular, MIX has no real commitment to the existence of
      a
stack
. Typical CPU architectures of today consider a
      stack to be a fundamental necessity: there’s a special register
      reserved for use as the stack pointer, which it’s either
      impossible to use for any other purpose, or at least highly
      inadvisable. Too much of the design is based on the assumption
      that
of course
you’ll want a stack.
But in MIX, nobody is making you use a stack. And Knuth, in
      many cases, doesn’t. His example MIX programs are generally set
      up so that each function has just one copy of its variables,
      stored at fixed addresses – and when one function calls another,
      the return address is just another of those variables.
This way of organising code works fine for every purpose except
      recursion (and multithreading): if a function’s variables always
      live at the same address, it follows that you can’t have two
      independent instances of the function active at once. So a
      function may never call itself, either directly or through any
      other chain of intermediate functions. Or rather: if
      you
do
need a particular function to have multiple
      concurrent activations, you’ll have to make a special effort to
      enable it to do so – for example, by manually implementing a
      stack inside that function.
(It’s surprising to the modern eye how little
      emphasis
TAOCP
puts on recursion, in fact! Current
      treatments of programming tend to consider it to be one of the
      most fundamental and important techniques, to be taught early
      and used often. By contrast, Knuth clearly
knows
about
      it, but is able to get a startling amount done without having to
      resort to it.)
Anyway. The relevance of all this to coroutines is:
The MIX subroutine call instruction works like most RISC call
      instructions: rather than pushing the return address on to a
      stack in memory, it simply writes it into a particular register
      called rJ, and then it’s up to the callee to decide what to do
      with it. So a normal MIX function call works by the caller doing
      one of these jumps, and then the callee saves the rJ register in
      one of its own memory
      locations
, so that it can remember where to jump back
      to at the end of its task.
The MIX call instruction is also its normal jump instruction.
      (rJ isn’t used for anything else, so that’s generally safe.) So
      the callee uses the same instruction when it returns, to
      transfer back to the caller. The only difference is that the
      caller jumps to the
start
of the callee, whereas the
      callee saves the rJ register on entry and jumps to wherever it
      said. On return, the caller
also
receives a value in
      rJ, because that jump instruction updated it too – but it
      ignores it, because it doesn’t care which particular place in
      the callee control came back from.
And that’s the sense in which coroutines ‘generalise’
      subroutines. With subroutines, each side receives a value in rJ,
      but only one of them bothers to remember it. With coroutines
      written in MIX in this style, the only difference is
      that
both
sides remember the value they receive in rJ,
      and
both
sides use it as the place to transfer control
      to next.
So, unlike most languages’ built-in coroutines (and certainly
      unlike my C preprocessor approach), this setup is completely
      symmetric. There is no sense in which one of the two functions
      ‘really is’ the caller, and the other one is just ‘pretending to
      be’ the caller using a special kind of yield statement. Each one
      is doing exactly the same thing as the other. They
      are
co
-routines, in the sense of “equal partners”.
A subroutine that can resume from where it last left off
Of course, in modern CPU architectures, there
is
a
      stack. And in almost all high-level languages (by which, in this
      case, I mean ‘any higher than assembly’ – even COBOL counts),
      there will be a function call and return system that assumes a
      stack, and each function will store its local variables on the
      stack. So if we want to have functions interoperating in a coroutine
      style, and each of those functions occupies a region of memory
      on the call stack, then one function is going to
have
to be higher up the stack than the other.
This introduces an ugly asymmetry into the perfectly symmetric
      system Knuth described. We have to make an arbitrary decision
      about which way up to order the two functions on the stack, and
      whichever way round we make the decision, you might reasonably
      ask “Why wouldn’t it be just as good to do it the other way?”
But it has to be done, so we make a choice, and designate one
      of our formerly equal coroutines as the ‘caller’ and one as the
      ‘callee’. What are the consequences?
An invariant of the conventional stack-based function call
      system is that the currently executing function must be the
      deepest one on the stack. You just aren’t allowed to have extra
      stuff occupying stack space
      below
the frame of the current function. (One
      reason is that asynchronous things like signal handlers or
      interrupts might overwrite that space without warning.)
So, when the caller is executing,
the callee can’t have a
      stack frame at all
. There would be nowhere for it to live.
Therefore, when the caller transfers control to the callee, the
      callee has to
construct
a stack frame. And when control
      transfers back the other way, that stack frame has to be thrown
      away again. So the physical view of what’s happening on the
      stack looks exactly like the caller making multiple independent
      calls to some subroutine: each time, a new stack frame is
      created, lives briefly, and is destroyed again.
The only differences between this and an ordinary subroutine is
      that the callee coroutine has to preserve all its variables
      between calls – which means they have to be stored
      somewhere
other
than on the stack – and that every time
      it’s ‘called’, it has to resume from just after wherever it last
      returned from.
This is the compromise that most languages’ coroutine systems
      end up settling on. My C preprocessor coroutine system is
      exactly this: a coroutine-structured function contains a macro
      at the start that can arrange to transfer control to any of the
      yield points in the function, and at each of those yield points,
      a variable is updated to mark that point as the one to resume
      from next time, and then the yield macro executes the ordinary
      C
return
statement. So the function’s physical
      stack frame is destroyed (which is OK because all the important
      state is kept in a
struct
elsewhere), and on the
      next call, a fresh stack frame is created.
The same is true of C++20 coroutines; it’s better hidden, but
      the low-level code generation will be doing basically this if
      you look deep enough. I expect the same is true of other
      languages that compile to ordinary stack-based native code.
This ‘resumable subroutine’ architecture has consequences
      beyond the details of the low-level implementation. Here are
      two:
Firstly, what happens if you want to divide up the work of the
      callee coroutine into subroutines? (For example, in Python, a
      generator can
yield from
another generator, so that
      the second one runs to completion and delivers all its results
      to the same place as the first generator.) The most obvious way
      to implement a ‘sub-coroutine’ is to have the parent coroutine
      call it repeatedly in a loop, passing its results back one by
      one:
function parent_coroutine() {
    yield START;

    // Make an instance of a sub-coroutine
    coroutine_instance sub = sub_coroutine();
    // And run it to completion, passing on all its yields
    while (sub is not finished)
        yield sub.next_yielded_thing();

    yield END;
}
Now if even the
parent
coroutine is having its stack
      frame demolished completely on every yield, then the same thing
      must be happening to the sub-coroutine. So if we nest
      sub-coroutine ‘calls’
n
layers deep, then every time the
      innermost one yields and resumes, the implementation will have
      to tear down
n
stack frames and set them all up
      again.
The resumable-subroutine model makes deeply nested
      sub-coroutines expensive in performance.
There might be a way to get round this, one way or another. For
      example, in C++20 coroutines, you
      can
set
      up a promise class
in such a way that the logical ‘stack’ of
      sub-coroutines never occupies the physical stack all at once:
      instead, at each stage, a physical stack frame is only needed
      for the
currently executing
coroutine in the logical
      stack. But it’s not necessarily the
default
way that
      things will work, so it’s something you have to keep in mind and
      watch out for: if there’s a special way to avoid this stack
      usage problem, remember to do it if your nesting gets too deep,
      and if there isn’t one, don’t
let
your nesting get too
      deep.
Secondly, if your language supports exceptions, what happens if
      a coroutine throws one?
Exceptions propagate up the physical stack. So if the callee
      coroutine throws an exception, it can propagate out into the
      caller. (For example, an exception in a Python generator
      propagates out into the function that called
next()
on it.) But if the caller throws an exception, it can’t
      propagate in the reverse direction.
It may be possible to configure this to some extent. C++20
      coroutine systems let you explicitly control what happens to an
      exception thrown in the coroutine. But you still can’t propagate
      an exception from ‘normal’ code
into
a coroutine by any
      sensible method.
So, if you care about exceptions, perhaps that might drive your
      choice of which of those two ‘equal’ coroutines to turn into the
      caller, and which the callee: in which direction (if any) would
      you like exceptions to travel between the two? Whichever
      direction that is, it might be easiest to make that ‘up the
      stack’.
(And if, in some extra-confusing scenario, you want exceptions
      to be able to travel in
both
directions – maybe based
      on the type of the exception – then you
really
have a
      challenge on your hands. Good luck, and have fun.)
Cooperative threads that identify which thread to transfer to next
I performed a minor sleight of hand in the previous section.
      Did you spot it?
I said: if we want two functions to interoperate in coroutine
      style, and each one occupies a region of the stack, then one
      function has to be higher up the stack than the other.
But hang on. “The” stack?
Who said there was only
      one?
This is the 2020s, and we’ve met multithreading by now. So
      we’re already used to the idea that a complicated program might
      contain
multiple
stacks, in widely separated regions of
      memory. We could put our two interoperating coroutines
      on
separate
stacks.
This immediately solves the problem of sub-coroutines. Now each
      coroutine is free to be reorganised into as many subroutines as
      it likes, without impacting performance by having to forward
      values up and down a long chain, or having to constantly destroy
      and rebuild physical stack frames. Either stack can yield to the
      other, no matter how deep it’s currently nested; when it does,
      execution resumes in the other stack from wherever it left off,
      by restoring the
stack pointer
as well as the location
      within the current function.
Working in this style, it becomes natural for sub-coroutines to
      have a ‘return value’, separate from whatever data they yielded.
      (For example, C++20 has
co_return
, separate
      from
co_yield
.) Just as an ordinary function
      performing I/O can return a value to its caller indicating
      success or failure, or returning the result of its I/O
      operation, a sub-coroutine that you call to yield on your behalf
      can return a value to you, perhaps communicating the same kind
      of thing.
Having two stacks restores the elegant symmetry of MIX’s
      coroutines: once again, our two (or more) stacks are equal
      partners in the program’s overall endeavour, with neither one
      being forced to take an artificially subordinate role.
But this is also what I meant when I said earlier that Knuth’s
      account of coroutines as ‘a generalisation of subroutines’
      didn’t make sense in all contexts. In
this
model,
      coroutines and subroutines aren’t more and less general versions
      of the same concept: they’re
independent
concepts, and
      you have both of them at once. I like to imagine them at right
      angles to each other: coroutine transfers go left or right
      between stacks, whereas subroutine calls or returns go up and
      down within a stack.
OK. So: if each of our coroutines comes with its own stack,
      then doesn’t that make them a lot like threads? What’s the
      difference?
Firstly, these coroutine stacks are
cooperative
.
      Control only transfers between them when they ask for it on
      purpose. This makes them unlike ordinary threads, which are
      pre-emptively switched by the OS kernel, or (better still, if
      possible) actually run simultaneously on more than one CPU of
      your multi-core computer.
This cooperative nature makes it easy to avoid the
      synchronisation problems of real threads. You don’t need to take
      out a lock to stop another coroutine stack from accessing the
      same data as you: all you have to do is
not yield to it
while you’re in the middle of a critical section, and then it’s
      guaranteed not to be running at the time.
Cooperative multithreading isn’t totally unheard of even in
      normal OS contexts. In the late 1980s, for example, RISC OS came
      out, which was a GUI operating system that let you run multiple
      programs at once, but it was cooperatively
      multithreaded
: your program
      would continue running without interruption until you called the
      ‘wait for a GUI event’ system service, and only then would the
      OS switch to running another process. And until
that
process made the same system call,
you’d
never get
      control back.
But when you did that, you didn’t know which other program
      would run next. It wasn’t really your business to know: the
      other programs were independent of you. If you exchanged data
      with another program at all, it would be mediated through the
      OS, perhaps via drag-and-drop or copy-and-paste, and you might
      not care
what
other program it was, only that it was
      providing data you had to do something with.
But in a coroutine-organised program, the data flow between the
      coroutines is highly structured, and the whole point. If you’re
      a coroutine stack acting as an adapter in between a producer and
      a consumer, then you most certainly do care which stack runs
      next: the consumer mustn’t run until you have a data item ready
      for it, and the producer mustn’t run until you’ve disposed of
      the one you’re holding.
That’s the other vital difference. Coroutine stacks get
      to
identify which stack to switch to next.
That adapter
      thread doesn’t just ‘yield to whoever has something to do’: it
      has two fundamentally different operations, ‘yield to the
      producer’ and ‘yield to the consumer’.
So, that’s my third model of what kind of thing coroutines can
      be. They’re like cooperative threads, except that switching
      between them is done in a manner like a coroutine yield rather
      than like a system call: the yielding ‘thread’ chooses which
      ‘thread’ is going to run next, and maybe passes it a data object
      of some kind, which it might need in order to resume running at
      all.
I’ve been talking about the CPU’s physical call stack structure
      throughout this section, but now I’ll contradict myself by
      saying that, at the physical low level, depending on the
      language implementation, the ‘stack’ of each of these ‘threads’
      need not
actually
look anything like a physical call
      stack.
You
could
make it look like one. You could allocate a
      piece of memory for a coroutine stack; let the coroutines on it
      push and pop stack frames like ordinary function calls; and have
      a special ‘yield’ function that swaps out the stack pointer and
      switches over to executing on another stack. In fact, that’s not
      a bad way to add coroutines to a language that doesn’t already
      have them, because it doesn’t need the compiler to have any
      special knowledge of what’s going on. You could add coroutines
      to C in this way if you wanted to, and the approach would have
      several advantages over my preprocessor system. (Though also
      some disadvantages: this way, you have to anticipate every CPU
      architecture your code will need to run on, and write and test
      the low-level stack setup and switching code for all of them.
      Also, you lose the advantage I’m about to talk about in the
next
section.)
But it’s just as likely that a language’s implementation of
      coroutines will choose to do it another way. For example, in
      C++20, you can certainly arrange for coroutines to be able to
      call each other as subroutines, but the natural way to set it up
      involves the logical ‘stack’ of those calls being an array or a
      linked list inside the coroutines’ promise objects. A separate
      physical call stack is never allocated, and (as I mentioned in
      the previous section) a call frame on the existing physical
      stack is only allocated for the currently running coroutine.
I’ll end this section on an extra-confusing note: if the
      coroutine stacks are kept in a format completely separate from
      the physical call stack of a thread, that opens the possibility
      of combining stacks of coroutines
with
conventional
      threads – so that when a coroutine stack has some work it can
      do, it could be resumed on the call stack of any thread that was
      free!
A named object identifying a program activity
Finally, I want to go back to a point I touched on
      in
a previous section
.
While I was comparing coroutines to ordinary threads
      (pre-emptive or genuinely concurrent), I mentioned that it’s
      useful that a suspended coroutine is always in a state where it
      can be conveniently destructed, if the computation or data
      stream or activity it’s producing is no longer needed.
More generally, once you’ve started a coroutine and it’s
      suspended itself, there will typically be some kind
      of
object
in the programming language that represents
      its state. That object will behave like any other: you can
      assign it (or maybe a pointer to it) into a named variable, and
      you can store that variable wherever you like. You could have
      other objects contain pointers to activities they care about;
      you could keep all your activities in an array; you could store
      each one in a separate variable with an easy-to-remember
      name.
If your language supports automatically destructing things when
      they go out of scope, this lets you tie the lifetime of the
      coroutine to some other lifetime you already cared about. For
      example, if a particular other class is consuming the
      coroutine’s output, you can keep the coroutine object inside
      that class, and then you
just don’t need to worry
about
      clearing it up: the coroutine will automatically be thrown away
      exactly when nothing can possibly need its output any more, even
      if it was only half-finished. And if it had any internal
      variables that also needed cleaning up, that will all happen
      automatically too, because the language should arrange
      that
their
destructors run. In a language using RAII,
      even external resources like open files should be cleaned up
      with no fuss.
(If your language
doesn’t
support automatic
      destruction, you still get an echo of this usefulness. For
      example, if you’re using my preprocessor coroutine system in C,
      then each coroutine already has to have a structure type storing
      all its internal state. If you want to be able to abandon an
      unfinished coroutine, then you have to accompany the coroutine
      with a hand-written function that frees that state structure and
      any subsidiary resources its fields point to. But in C, you’re
      accustomed to writing those functions all the time anyway, so
      coroutines are no different – and if a non-coroutine object of
      some kind owns a coroutine state, then the free function for the
      first object will naturally call the free function for the
      coroutine state. And
vice versa
. So it’s still natural
      to set up your code so that coroutines are cleanly destroyed; C
      makes you do all the
work
yourself, but it’s easy
      to
organise
it sensibly. This is one of the reasons I
      mentioned in the previous section for why I still use
      preprocessor coroutines in C instead of low-level stack
      switching: it would be a much harder job to free an
      in-progress
physical call stack
and all the resources
      allocated by unfinished calls on it!)
An interesting thing about this ‘conveniently destructible’
      nature is that it wasn’t anywhere in
TAOCP
’s
      presentation of coroutines, and I presume therefore not in
      earlier work either. (That’s not
surprising
, of course,
      since languages with automatic destruction weren’t around in
      those days.) I only really thought about it that way myself when
      someone suggested to me the idea of combining coroutines with
      threads (as I mentioned at the end of the previous section), and
      wondered what the advantage might be over
just
using
      threads. I decided this was it: if your in-progress activities
      are explicitly stored in a data structure separate from the
      threads that are executing them, then you can abandon an
      activity in an easier and cleaner way than destroying a thread.
      It’s always interesting when the most useful feature of a thing
      turns out to be one that its originator never thought of!
Anyway. This is my final way of looking at coroutines: they
      allow you to encapsulate a computation, or some other particular
      strand of your program’s activity (such as one among many
      network connections it’s handling), into an object which has a
      name in your programming language, and can be accessed from
      outside the coroutine.
If you’ve expanded each coroutine into a call stack of its own,
      as I discussed in the previous section, then this is still true:
      from outside the coroutine stack, you still have
one
named object, which encapsulates the whole stack. For example,
      if the coroutine yields data values, then that object will be
      where the rest of the program goes to get them: it will have
      the
next()
method, or the C++ iterable semantics,
      or whatever the language finds convenient. Whichever layer of
      the coroutine’s internal call stack yields a value, the values
      will all be delivered out of that same single object, without
      anyone outside the coroutine stack having to know or care about
      the internal subdivisions. And destroying that object should
      clean up the entire stack, even if it had multiple layers of
      unfinished internal subroutine calls.
But having a named object identifying an activity is useful for
      more things than just destroying it. Objects can also provide
      other methods, or expose their internal data to the rest of the
      program on purpose.
For example, if you have a coroutine object that encapsulates
      the progress of some activity, you might arrange that it
      presents methods returning details of its progress – perhaps a
      headline figure like ‘85% complete’ for the graphical progress
      bar, or perhaps details of the last subdirectory it scanned, or
      what phase of a network connection it’s in. As usual, the
      advantage of doing this with coroutines rather than threads is
      that there’s no worry about concurrent access: if the coroutine
      is suspended, then you can safely read its data (or at least the
      data it’s publishing on purpose).
You might also arrange that methods on the wrapping object
      can
modify
the progress of the coroutine in some way.
      That case is harder to think of good examples for, but they do
      sometimes come up.
One example of this comes up in an example I’ve already shown,
      from PuTTY. In
a previous section
I
      showed pseudocode of the coroutine that handles the SSH
      transport layer, which periodically does key exchanges. A repeat
      key exchange can be triggered by either side sending
      the
KEXINIT
packet. In the pseudocode earlier I
      showed the coroutine responding to the
other
end
      sending
KEXINIT
. But what if
we’re
the
      side that decides it needs to rekey first?
Suppose we had a function
trigger_rekey()
that the
      rest of the program would call when it decided that needed to
      happen. That function could construct a
KEXINIT
packet and inject it into the output packet queue. When the
      other end responded with its own
KEXINIT
,
      the
key_exchange()
coroutine would resume, and see
      it. But then how would it know that in
this
case it
      shouldn’t respond by sending one of its own? Answer:
      the
trigger_rekey()
function also wants to set a
      flag
in the coroutine’s state
that says “We’ve already
      sent our
KEXINIT
, don’t send another one”.
      Then
key_exchange()
sees the
      incoming
KEXINIT
but also sees that the flag is
      set, so it goes back round to the top of the loop without
      sending an unwanted extra
KEXINIT
first. That’s the
      kind of thing that an accompanying mutator method on a coroutine
      might usefully do.
OK; what
else
can you do with a data object in a
      programming language, as well as deleting it, reading its state,
      or changing its state?
Here’s a
really
silly idea: you can
copy
it.
      Suppose you
cloned
a coroutine object, together with
      all of its internal state?
Using my C/C++ preprocessor coroutine system, this is perfectly
      possible. In that system, all the persistent variables of the
      coroutine – including the state variable that says where to
      resume from next – have to live in an explicitly declared
      structure (in C) or be members of a class (in C++). Either way,
      there’s no difficulty with making an exact copy: in C, you’d
      have to write a cloning function that dealt with memory
      allocation and deep copying, but that’s an easy mechanical job
      and the structure definition lists all the fields you need to
      handle. And in C++, you might very well be able to use the
      class’s default copy constructor and have it Just Work.
After you do that, you’ve got two copies of the coroutine, and
      each of them will resume from the
same
part of the code
      when it next runs. It’s very like the Unix
fork
system call in that respect.
This isn’t a
deliberate
feature of my preprocessor
      system; it’s just a thing that drops out naturally from the
      implementation strategy, and turns out to be easy to do. I doubt
      that any language-native coroutine system will be willing to do
      this stunt.
But if you
can
do it, what might it be useful for?
One thing that springs to mind is testing, if your coroutine
      accepts input on each yield. Run the coroutine to a particular
      point, then repeatedly clone it and try lots of different inputs
      on independent copies of it, making sure that each one is
      handled correctly. This might be a lot less expensive that
      running from the start of the coroutine to the test
      point
again
for each test input.
Another possibility is to use the same idea at run time, to
      probe the coroutine from outside and
find
an input that
      will cause it to respond in a particular way. But I haven’t
      thought of a use for that at all!
Conclusion
I started writing this article because I wondered if I had
      anything in particular to say about coroutines. Turns out I had
      quite a lot!
Perhaps this will convince a few more people to become
      coroutine fans. Or perhaps it will give some existing coroutine
      users new ways of thinking about them and using them. Or perhaps
      not, and everyone reading this will decide I have weird opinions
      that they disagree with.
But it was fun to write, and helped me clarify my
own
thoughts. And it’s my blog so I can be self-indulgent if I want
      to. Thanks for reading!
With any luck, you should be able to read the footnotes of this
      article in place, by clicking on the superscript footnote number
      or the corresponding numbered tab on the right side of the page.
But just in case the CSS didn’t do the right thing, here’s the
      text of all the footnotes again:
1.
For
      example, in the Win32 API, if you have a bidirectional file
      handle such as a serial port or a named pipe, and you need to
      simultaneously try to read and write it, I think it
      really
is
the least inconvenient thing to have two
      threads, one trying to read the handle and one trying to write
      it. The alternative
GetOverlappedResult
approach
      ended up being
more
painful when I tried it.
2.
I talk about
      generators as if they were
the
coroutine system in
      Python, but in fact, they’re one of two: Python
also
has
      a
completely
      different kind of thing
that it actually uses the name
      ‘coroutine’ for, in which function definitions start
      with
async def
and suspend with
await
.
      I’ve never played with those, because generators are easier to
      get started with and have scratched my generalised coroutine
      itch well enough. But at some point I should at least give them
      a look.
3.
In
TAOCP
, one of Knuth’s
      suggestions for a producer/consumer chain is that you might be
      flexible enough to make a runtime decision as
      to
whether
to run both parts interleaved as coroutines,
      or whether to run them sequentially storing the intermediate
      data on disk, depending on how much memory you have. I suspect
      this was a more vital concern in the 1970s.
4.
The
      non-cyclic version of this is also useful. As of Python 3.10
      that
is
in the standard library,
      as
itertools.pairwise
, although I’m going to have
      to keep writing it by hand until I can rely on Python 3.10 or
      better being widespread enough. But as far as I know the cyclic
      version still isn’t in
itertools
.
5.
Incidentally, yes, I know,
      there’s another special case that my code doesn’t handle: if the
      input iterator has
no
values, then the example version
      of
cyclic_pairs
shown here will
      raise
StopIteration
, when perhaps you’d prefer it
      to silently generate an empty output list. Before Python 3.7
      this happened automatically, because
StopIteration
was handled differently; in many of my own use cases I never
      pass an empty list anyway. But if you were writing a version
      general enough to go in
itertools
, you’d probably
      want to check for that case properly.
6.
In my fantasy programming
      language, this would
actually
be how the standard
      control structures were implemented. The only primitives in the
      language itself would be ‘goto’ and coroutines.
All
block-structured control flow commands, even the standard things
      like ‘if’, ‘for’ and ‘while’, would be defined in the standard
      prelude as small coroutines of this kind, implemented in terms
      of ‘goto’. Then they wouldn’t need to be
      keywords!
7.
In fact, Knuth does
      this by self-modifying code. The memory location where you save
      the return address is actually the destination-address field
within the jump instruction
that performs the
      return!
8.
For the sake of not
      using too many words, I’ll assume the most common convention for
      stack layout, which is that the stack grows downwards in memory:
      pushes make SP smaller, pops make it bigger, and when you call a
      subroutine, its stack frame is below yours. If you’re used to
      one of the rare architectures that does things the other way up,
      just turn your head upside down while reading this
      section.
9.
RISC OS is still around the
      last time I heard, and will run on a Raspberry Pi in particular.
      I have no idea if it’s
still
cooperatively
      multithreaded, though. Wikipedia seems to say it is, but its
      most recent citation is from 2003…
