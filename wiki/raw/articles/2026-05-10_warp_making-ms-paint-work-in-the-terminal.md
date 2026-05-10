---
title: "Making MS Paint work in the Terminal"
source: "Warp Blog"
url: "https://www.warp.dev/blog/making-ms-paint-work-in-the-terminal"
scraped: "2026-05-10T01:27:51.188283+00:00"
lastmod: "2026-04-24T14:39:42.000Z"
type: "sitemap"
---

# Making MS Paint work in the Terminal

**Source**: [https://www.warp.dev/blog/making-ms-paint-work-in-the-terminal](https://www.warp.dev/blog/making-ms-paint-work-in-the-terminal)

Engineering
Making MS Paint work in the Terminal
Advait Maybhate
January 9, 2024
Did you know that you can use MS Paint within your terminal? 🤯
textual-paint
is a program that emulates MS Paint within your terminal. To try it out, install it via pip (a package manager for Python) using
pip install textual-paint
. Then, run the command
textual-paint
within your terminal. Check out a demo below!
MS Paint in the terminal!
In this blog post, we’ll dive into some of the engineering challenges we faced when enabling textual-paint to function correctly within Warp.
If you’re not yet familiar with
Warp
, it’s a reimagination of the command line terminal with some unique features like AI assistance, team collaboration, and modern IDE-style input. Due to the inherent nature of how the terminal interacts with the shell, via the PTY (pseudo-terminal), supporting certain user interactions can be quite interesting to implement. Read on to learn more!
The Problem
When we tried playing with textual-paint in Warp, we noticed that its hover effects don’t function correctly–something that worked well in other terminals (GIFs below). After a bit of exploration, we identified the crux of the matter: Warp wasn’t conveying mouse-hover events to the PTY when in the alt-screen, a broader issue. Below, we’ll dive into the interplay between the terminal and PTY, and offer a primer on the mechanics of ANSI escape codes. If you’re not familiar with these technical terms - don’t worry, we’ll elaborate on them below!
No hover effects within Warp 😢
Correct hover effects from default Mac terminal
Understanding the PTY & ANSI Escape Codes
Inside every terminal, the vital conduit for all interactions with the shell is the PTY, or pseudo-TTY. In essence, the PTY is the contemporary counterpart to the hardware terminals of the past, where physical wires linked devices. In the 1970’s, a "terminal" consisted of an input device, like a keyboard, and a display device, such as a monitor or even a sheet of paper. This device, known as the TTY (short for teletypewriter), was responsible for handling communications with the mainframe computers via serial connections.
Fast forward to today, where everything unfolds within a single machine, and we find pairs of file descriptors forming the PTY. These file descriptors effectively serve as the two ends of the metaphorical wire, transmitting user-entered input into programs and relaying program output back to the user. If you're intrigued and eager to delve deeper into the workings of the PTY, I encourage you to check out our
blog
on the subject!
The VT100 - a popular terminal of the past
Warp - a modern-day terminal
The PTY can only transmit bytes. Therefore, every instruction or event must manifest as a sequence of characters. To standardize this, terminal protocols have delineated "special sequences", commonly referred to as ANSI escape sequences. Terminal emulators harness them in their input/output, deciphering them as commands, not merely text. For instance,
\u001b[31m
is used to render red text in your terminal output. To print red text to the terminal, you could use the following Python code:
Rust
>>> print("\u001b[31mHello, world!\u001b[0m")
Hello, world!
In this particular case, ANSI escape codes are also used for reporting mouse events to the PTY.
Constructing the right escape code for hover events
In our case, we were interested in mouse events within the alt-screen, which is the alternative buffer that takes over the entire terminal window, used for programs such as Vim or textual-paint. Applications can activate "mouse reporting" by dispatching particular ANSI escape codes to the terminal, instructing it to monitor and relay mouse events. In response, the terminal communicates mouse activity to the underlying program, through the PTY, by sending corresponding ANSI escape codes. Within Warp, we already supported reporting mouse events for click events, drag events, etc, but, we didn’t support hover events i.e. mouse motion without clicking. Hence, we needed to identify the appropriate ANSI escape code for mouse motion.
We were using “0” and “2” as escape codes for left/right buttons respectively, but where could I go to find out, authoritatively, what the correct escape code for mouse motion is? Well, I dug through the xterm docs (the standard terminal emulator for the X Window System), various GitHub threads and articles on the internet which were rabbit holes of information, though it was hard to pinpoint exactly what I needed (due to the modifiers involved). We can see other terminal emulators, such as Alacritty, also having issues with following the correct specification - see threads/commits
here
and
here
.
Ultimately, I decided to bypass the manual search approach and executed a local terminal emulator, Alacritty in this instance, that was already proficient in reporting such events. This hands-on approach led me to "35" – the quintessential escape code I’d been seeking.
If you’re interested in the technical details: this “35” corresponds to xterm extension DECSM 1003, which encodes mouse hover events as 32 (base value) plus 3 (button released), giving us 35 (see
Vim's libvterm seqs
for a full list).
Loom demonstrating how I found the correct escape code for hover interactions
Here's a glimpse into how we craft our escape sequences:
Rust
pub mod EscCodes {
 // Mouse-related escape codes
 pub const MOUSE_LEFT: u8 = 0;
 pub const MOUSE_RIGHT: u8 = 2;
 pub const MOUSE_DRAG: u8 = 32;
 pub const MOUSE_MOVE: u8 = 35;
}
...
 to_escape_sequence(&self) -> Option<Vec<u8>> {
 let action = match self.action() {
            MouseAction::Released => 'm',
            MouseAction::Pressed => 'M',
 };
 let (button, repeats) = match self.button() {
            MouseButton::Left => (EscCodes::MOUSE_LEFT, 1),
            MouseButton::Right => (EscCodes::MOUSE_RIGHT, 1),
            MouseButton::Move => (EscCodes::MOUSE_MOVE, 1),
 ...
 };
 let point = self.maybe_point()?;
 let msg = format!(
 "{}<{};{};{}{}",
            C1::to_utf8(C1::CSI),
            button,
            point.col + 1,
            point.row + 1,
            action
 ).repeat(repeats);
 return Some(msg.into_bytes());
}
Let's unravel the essence of the escape sequence directed to the PTY. Consider the sequence
\u{1b}[<35;23;23M
which represents mouse motion, the event we were adding. This sequence is an amalgamation of several components:
Control Sequence Introducer:
This is a universal precursor for all control sequences i.e. the C0 control code for “ESC
“ which is
\u{1b}[
.
Button's Escape Code:
It signifies which mouse button instigated the action e.g. 35 representing mouse motion (corresponds to the underlying xterm extensions).
Alt-Screen Coordinate:
This denotes the exact location of interaction within the alt-screen e.g (23, 23) from the above sequence. Note that these coordinates correspond to the one-indexed grid coordinates within the alt-screen (rows and columns). See
xterm docs
for more details.
Nature of the Action:
For mouse events, this refers to whether the button was pressed or released e.g.
M
representing pressed above (for historical reasons, hover-events are tracked as “presses” with generic mouse motion escape codes).
For actions that encompass movement across a span, like scrolling, this control sequence gets reiterated for each corresponding line of motion. Note that these mouse events should only be reported when we’re in the correct ANSI terminal mode i.e.
MOUSE_MOTION
(defined by bit sequence flags).
A slightly related brain teaser
During our journey to iron out the hover functionality, we stumbled upon another intriguing challenge. Warp was inadvertently dispatching surplus mouse events, leading to anomalies in hover and drag behaviors. To be precise, we were generating synthetic mouse motion events. Why? To sustain consistent product behavior in particular scenarios.
Imagine this: A user decides to close a tab. The immediate tab to its right gracefully slides into place. Now, while the mouse isn’t physically “moving” over this new tab (we simply had a click event and the cursor is stationary), we'd still want it to exude the "hovered" aura. Hence, our need for such synthetic mouse events. However, this meant that we had to differentiate these synthetic events from the genuine mouse movements initiated by the user to ensure we didn't misreport events on the alt-screen. Notably, we’ll eventually move to a world where we have the concept of “layout changes” to avoid such synthetic events.
Preserving hover state on tab when closing tabs (right tab slides over)
Culmination: Bringing MS Paint to Warp
Post the meticulous implementation of mouse-motion reporting, we unlocked a delightful achievement. Fancy sketching on MS Paint via Warp 😛? We made it possible! Check out our demo with our brand-new hover effects:
Loom showing the hover effects working with some commentary
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
