---
title: "C++ futures part 1: The mental model"
url: "https://devblogs.microsoft.com/oldnewthing/20261012-00/?p=112767/"
fetched_at: 2026-10-13T10:01:08.370485+00:00
source: "devblogs.microsoft.com/oldnewthing"
tags: [blog, raw]
---

# C++ futures part 1: The mental model

Source: https://devblogs.microsoft.com/oldnewthing/20261012-00/?p=112767/

The C++ standard library has a group of related functions and classes:
std::promise
,
std::packaged_task
,
std::async
,
std::future
, and
std::shared
future
.
The idea is that all of these classes are built of a single unnamed class which the C++ standard library calls the “state”, but for the purpose of discussion, I’m going to call it the
source
, since it is the thing that produces the value, and it behaves analogously to a C# task completion source.
The
source
conceptually supports these operations:
Set a value.
Set an exception.
Wait for a value or exception to be set.
Retrieve the value or rethrow the exception.
Here’s a simplified version that doesn’t support references.
template<typename T>
struct source
{
private:
    enum what {
        nothing,
        value,
        exception,
        consumed,
    } d; // discriminant

    union {
        T value;
        std::exception_ptr ex;
    } r; // result

    std::mutex m;
    std::condition_variable cv;
The discriminant tells us what is in the union: Nothing (because nobody has set anything), a value, an exception, or nothing (because the value has been consumed).
The mutex ensures thread-safe access to the other members, and the condition variable lets us wait for somebody to set a value or exception.
void must_be_empty() {
        if (d != what::empty) {
            throw std::future_error(future_errc::promise_already_satisfied);
        }
    }
You can call the
set
methods only when the source is empty, so we’ll factor out the emptiness check.
public:
    void set_value(T& v) {
        std::lock_guard g(m);
        must_be_empty();
        new(&r.value) T(v); // "r.value = v"
        d = what::value;
        cv.notify_all();
    }
You can set a value or exception only once, so if there is already a value or exception, we yell at you. Otherwise, we save the value and notify anybody who was waiting for a value to be set.
I won’t bother with the overload that takes
T&&
; it’s the same thing, but with a
std::move()
.
There is also a
set_
value_
at_
thread_
exit
which will be another topic for another day.
Instead of setting a value, you can set an exception:
void set_exception(std::exception_ptr ex) {
        std::lock_guard g(m);
        must_be_empty();
        new(&r.ex) std::exception_ptr(ex); // "r.ex = ex"
        d = what::exception;
        cv.notify_all();
    }
It’s basically the same as
set_
value
except that we store an exception.
That’s how values an exceptions go
into
the source. The next part is waiting for the source to become nonempty.
void wait() {
        std::lock_guard g(m);
        while (d == what::empty) {
            cv.wait(g);
        }
    }

    void wait_for(duration dur) {
        std::lock_guard g(m);
        cv.wait_for(g, dur, [&] { return d != what::empty; });
    }
You can either wait indefinitely or wait for a particular duration. The
wait_for
method is why we have a condition variable at all. If it weren’t for that guy, we could have used
std::
atomic
‘s
wait
and
notify_
all
methods.
The last part is getting the values out.
void can_get() {
        if (d == what::consumed) {
            throw std::future_error(future_errc::future_already_retrieved);
        }
        if (d == what::exception) {
            std::rethrow_exception(r.ex);
        }
    }
Regardless of how we intend to retrieve the value, it’s not legal to retrieve a value that has already been consumed. Also, if the result is an exception, we rethrow the exception.
T consume() {
        wait();
        std::lock_guard g(m);
        can_get();
        d = what::consumed;
        return std::move(r.v);
    }

    const T& get() {
        wait();
        std::lock_guard g(m);
        can_get();
        return r.v;
    }
};
You can get the value, which returns a const reference to the underlying storage. Or you can consume the value, which moves the value out of the underlying storage and marks the value as consumed so nobody can consume or get it (because it’s not there any more).
We can now build our other objects and functions out of this guy. We’ll do that next time.
Bonus chatter
: Writing the destructor is left as an exercise for the reader. It’s not hard, but it’s annoying because of the union.
Bonus bonus chatter
: I’m writing the series because I always forget how it works, but writing it down helps me remember.
