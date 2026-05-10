---
title: "Font Fallback in a WASM Terminal"
source: "Warp Blog"
url: "https://www.warp.dev/blog/font-fallback-in-a-wasm-terminal"
scraped: "2026-05-10T01:27:25.916190+00:00"
lastmod: "2026-04-19T15:37:21.000Z"
type: "sitemap"
---

# Font Fallback in a WASM Terminal

**Source**: [https://www.warp.dev/blog/font-fallback-in-a-wasm-terminal](https://www.warp.dev/blog/font-fallback-in-a-wasm-terminal)

Engineering
No Glyph Left Behind: Font Fallback in a WASM Terminal
Daniel Peng
December 5, 2024
We’re building Warp, the intelligent terminal with AI and your team’s knowledge built-in. Warp is built in Rust, and we recently took advantage of Rust’s ability to cross-compile to WebAssembly (WASM) to bring Warp to the web. Enabling Warp in the browser brings us closer to our vision of making the terminal more accessible and collaborative!
As part of this effort, we had to dive deep into the world of fonts and Unicode. At some point, you’ve probably been using your computer and encountered text with some weird boxes. What’s going on when that happens?
A primer on font fallback
Whenever your computer renders a character, it searches through font files for a matching graphical representation of that character, called a glyph. Each font file contains hundreds or even thousands of glyphs. A typical Western font might contain glyphs for the latin alphabet, numbers, punctuation, and some symbols.
A preview of some of the glyphs available in Helvetica.
But what about non-Western scripts, like Arabic or Chinese? What about emoji or icons? It turns out, it’s not practical for fonts to include glyphs for every possible character – there are over 150,000 characters defined in the latest Unicode standard. The font files would get impractically large, and asking a font designer to create all these glyphs would be a herculean task.
Searching for the right glyph to represent a character is done via a mechanism called font fallback. Typically, applications will have a cascading list of available fonts. If a glyph is not available in the application’s default font, it will check the next font in the font fallback chain, repeating all the way to the end. You might be familiar with CSS’s implementation: the
font-family
property accepts a list of fonts that act as its font fallback chain.
A CSS font fallback chain.
As a last resort, if none of the fonts contain a glyph for a character, the application will choose how to handle the missing character. Some applications will render nothing at all, while others will render the empty rectangle (sometimes known as the “tofu” character due to its resemblance to a block of tofu). So when you see those weird boxes in the middle of some text, that’s the application saying it doesn’t know how to render that character.
Constraints when building a web WASM app
Having a robust font fallback mechanism is important for Warp. The value is clear for supporting different scripts, symbols, and emoji. Warp has a global user base and supporting these types of input is the standard for any modern user-facing application. As a terminal, we also want to support the many users that use
Nerd Fonts
, developer-focused patched fonts containing a large number of extra icons. These icons are commonly used in plugins for editors such as
Neovim
and in popular custom prompts like
Powerlevel10k
.
However, this calculus is complicated by building a WASM application for the browser. On the native version of Warp, we have access to fonts installed on your system and OS-level libraries that create a font-fallback chain for us. The browser has no such access to system fonts, for security reasons. Our in-house
UI framework
renders Warp directly to an HTML canvas via the GPU, bypassing any chance of us using CSS’s font fallback mechanism. This necessitated us to build our own font fallback implementation for the web.
There’s one more major constraint to consider: our WASM binary size. The entire WASM executable must be loaded before Warp can run in the user’s browser. Time-to-first-load is a critical part of the user experience, so keeping our binary size small was a priority (for more on how we reduced our WASM binary size, see our other
blog post
).
Where we landed
We built an asynchronous font fallback mechanism into our UI framework, allowing consumers of the UI framework to define their own font fallback mappings. Each mapping consists of a range of Unicode points and an associated URL to a font that contains glyphs for that Unicode range.
Some example font fallback mappings that we’ve defined for Warp.
When the UI framework tries to render a character that doesn’t have a glyph in any of the bundled fonts, it will check the supplied font fallback mappings to see if the application has defined a fallback font. If it does, it will fetch the font from the URL, add the font file to the font fallback chain, evict our local glyph caches, and re-render the scene when the font has been loaded. On the next render, the UI framework knows to use the loaded font!
An example of a font being loaded asynchronously in Warp on the web.
By loading in these fallback fonts lazily, we avoid bloating our binary size with a plethora of fallback fonts. In practice, we find that lazy loading doesn’t degrade user experience. Loading the fonts on most internet connections is fast and browser caching means the cost is usually only paid on first load.
We had to determine which fonts we actually wanted to fall back to, since we don’t have the user’s system fonts to rely on. For this, we looked to the
Noto font family
. Noto, short for “no tofu”, is a free set of fonts designed to cover all the scripts encoded by Unicode along with comprehensive emoji and symbol support, making it perfect for our needs. Choosing fonts from the same family means we also maintain a consistent look and feel in Warp, even across different scripts. The one non-Noto font we included in our fallback fonts was a patched version of
Hack
that includes Nerd Font icons. These icons are used in many popular plugins that developers use to customize their terminals. Including Nerd Font icons allows these plugins to look and feel as they would on a native version of Warp.
A
Powerlevel10k
prompt in Warp on web, before and after font fallback.
Unicode itself partitions the range of Unicode points into blocks. Each block represents a contiguous range of characters that generally are used to support a single language or symbol type. This was a useful starting point for determining which Unicode ranges we wanted to map to which fallback fonts.
Sharing a session in Warp on the web, with 3 different fallback fonts in use: Noto Sans SC, Noto Color Emoji, and Hack Nerd Font!
As a result of our efforts, we were able to build out a web version of Warp with support for rendering the different scripts, icons, and symbols that you would expect from a native terminal, while not compromising on user experience. Font fallback was a fun example of the types of technical challenges we faced when building for WASM: needing to build out something from scratch that developers would usually take for granted. We’re excited to be launching Warp on the web and getting this into the hands of our users!
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
