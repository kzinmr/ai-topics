---
title: "A noob learns FFT"
url: "https://entropicthoughts.com/fft"
fetched_at: 2026-08-11T10:16:31.915024+00:00
source: "entropicthoughts.com"
tags: [blog, raw]
---

# A noob learns FFT

Source: https://entropicthoughts.com/fft

I can’t say what this data really means, but fortunately I have a corny cover
story ready: outside my children’s bedroom, they’re constructing a building.
We’ll pretend I have a measuring device that records the increase in building
height every hour, and it’s been doing that for a year.
Because the construction workers primarily work during the day, and on weekdays,
I expect daily cycles (building growth from day to day), and weekly cycles
(lulls in growth during weekends). In the plot below, the frequency spectrum has
been changed to a period spectrum. Thus, a peak at 7 in the spectrum corresponds
to a weekly cycle, rather than a frequency of 7 per day.
The tallest bar in the spectrum corresponds to a cycle with a period of
365 days. Obviously, given just one year of data, we cannot know whether this is
a repeating cycle or not; the bar really only represents a general increase
toward the end of the year, and that’s probably true: it seems that building
growth has increased.
Aside from the one-day and seven-day cycles we expected, there is also a
prominent cycle with a period of 3.5 days. This shows up because the weekday
pattern is really a square wave with a duty cycle of 5-on, 2-off. The harmonics
we expect to be prominent for that square wave are cycles of length 3.5 days,
2.4 days, 1.4 days, and 1.2 days. There are peaks corresponding to all of those
cycles in the spectrum!
Although it’s not visible on this small plot, the spectrum also contains a cycle
with a period of two hours. It would be interesting to see if there’s an hourly
cycle, but the Nyquist limit says the shortest cycle we can extract from hourly
data is one with a period of two hours.
But if we look up from the spectrum onto the time series, we see some sharp
peaks in the data. Those are not, generally, real growth. To roll with our corny
example, we can pretend that these are artifacts of someone bumping into the
table which holds the measuring device, causing a false signal. I want to see
what the real growth is over the year, so I need to somehow
subtract the bumps
from the signal.
Thinking back to our earlier experimentation, we may realise that the bumps are
impulses! Maybe we can assume they contribute equally to all frequencies. Then
we ought to be able to subtract a constant magnitude from all frequencies and
get rid of the worst of the table bumps. I didn’t expect it to work, but it kind
of does.
Looking at the filtered time series at the top, the weekly cycles become so much
more apparent after filtering out the worst of the false signals. It seems
increasingly like there’s one specific day of the week where they do most of the
actual construction of the building.
2
I notice that my cover story is
starting to break apart. Please suspend your disbelief.
We can tell from the period spectrum that the filtering operation had the
practical effect of attenuating much of the high-frequency noise, i.e. that with
periods shorter than one day. The result is somewhat similar to a rolling
median, but the
fft
based approach retains the day-to-day variation better.
For the rolling median have sufficient bump-filtering strength, it must have a
window size that is also large enough that it also smooths out much of the daily
cycle.
If we think of the peaks as a high-frequency component instead of as separate
impulses, we would instead attempt to filter them out with a low-pass filter.
This would also zero out the short-period components of the spectrum, but it
wouldn’t have any effect on the long-period components. I tried this also, but
it didn’t work as well.
I suspct the reason we can’t think of the peaks as high-frequency components is
that they are somewhat randomly dispersed. They don’t make up one unified
high-frequency signal. Maybe if we made a spectrum for a zoomed-in part of the
time series, we could think of them as high-frequency components. Let’s
formalise that idea a bit.
