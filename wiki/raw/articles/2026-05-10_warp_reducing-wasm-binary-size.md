---
title: "Reducing WASM binary size"
source: "Warp Blog"
url: "https://www.warp.dev/blog/reducing-wasm-binary-size"
scraped: "2026-05-10T01:28:02.941615+00:00"
lastmod: "2026-04-19T15:37:21.000Z"
type: "sitemap"
---

# Reducing WASM binary size

**Source**: [https://www.warp.dev/blog/reducing-wasm-binary-size](https://www.warp.dev/blog/reducing-wasm-binary-size)

Engineering
Reducing WASM binary size: lessons from building a web terminal
Jack Nichols
December 11, 2024
We’re building Warp, an intelligent terminal written in Rust. We recently decided to cross-compile our app to web via
WASM
and are now making Warp available through the browser. Bringing Warp to the web is another step towards making our app more available and more useful for collaborative development!
When we set out to bring Warp to the web, we faced several engineering challenges. One of the most significant was that the Warp executable was simply too large. It was 21.4MB after
gzip
compression. After digging in here, our big wins were (a) getting our Rust compiler options right and (b) building a framework for loading assets asynchronously. We ended up at 8MB. How did we get there?
Consider making an engineering choice like this: we want to show a background theme image in Warp as soon as the application opens. If we want the image to appear even when the user is offline and to appear without being subject to unknowable network latencies, it makes sense for the image to be bundled directly into the executable. On desktop platforms like Mac and Linux, the extra image in our executable implies that first-time users have to wait longer for the application to download. It also means we require a larger footprint on a user’s potentially-limited disk. We don’t want either of those things, yet the user experience of having the image bundled directly into the binary is clearly way better than loading the image dynamically from the internet. The tradeoff here doesn’t always favor building small.
Building for web is a different calculus. On web, how fast the application – now a WASM file – loads over a network is a fundamental piece of the user experience. The larger the executable, the longer a user is kept waiting each and every time they want to use Warp in the browser. We realized quickly that the size of the WASM binary is a recurring cost and it’s paid at a critical moment in the user experience.  Unlike on desktop where we can download updates in the background, on web if the user needs a new version of the app (say when the cache expires), downloading it blocks them from using Warp. Hence, we set out to make our WASM binary as small as possible.
To start, we evaluated our
cargo
build configuration in light of new priorities:
opt-level
. The opt-level setting is a configurable high-level determinant of what the compiler should be optimizing for and to what extent: faster runtime code, shorter compile times, or smaller binaries. We played with aggressively optimizing for size by disabling loop vectorization (“z”) but ultimately settled on a more conservative profile (“s”) to avoid any noticeable performance hits at runtime.
lto
. We enabled lto to allow
LLVM
to perform its own set of link-time optimizations, winning back about one megabyte pre-compression.
wasm-split
. We introduced wasm-split with the flags –strip and –strip-names to extricate debug information from the binary.
build-std
. We learned that Rust ships pre-built copies of the standard library with its toolchains, and that the prebuilt libstd is optimized for speed rather than size. The cargo feature build-std forces libstd to compile from source, inheriting whatever optimizations are included in the cargo profile, but, because this feature is still under development and considered unstable, we decided against adding it to our build pipeline for now.
Next, we re-designed how Warp manages assets. Assets is a general term for external objects in our app like images, font files, icon files, text files, and so on. Images – specifically jpegs – are a particularly acute source of bloat since these files are already compressed and each high-resolution image we bundle costs us hundreds of kilobytes, even megabytes in some cases. On our desktop platforms, images that we use as theme backgrounds take up about 10 megabytes of space in the binary.
With the goal of removing assets from our web binary, we introduced the concept of async assets into the app. These assets are bundled directly into the binary using
RustEmbed
in all cases except for web builds. In web builds, these assets are fetchable from a URL. Then, in code, we identify assets and where they come from using an enum:
Rust
pub enum AssetSource {
    URL {
        url: String,
    },
    Bundled {
	 // Assets that are statically included in the bundle can be statically 		 // referenced.
        path: &'static str,
    },
    LocalFile { 
 path: String 
    },
}
Whenever we try to access the contents of an asset - such as when we attempt to render it - our
UI framework
does the work of finding the data. If the source is a URL, that means spawning a future that fetches the bytes over the network. If it’s bundled, it means passing back a reference to the bytes in the RustEmbed. If it’s a local file, that means opening the file and asynchronously reading out its contents. We built this in a way that supports eager fetching for more popular assets. This means, for example, the fetch of an image might be kicked off immediately at app startup to offset latency when the image is actually needed.
To make async assets more ergonomic in our code, we built a Rust macro that resolves a file name to an AssetSource at compile time based on whether we’re building to WASM. This means that we declare async assets as
bundled_or_fetched_asset!(“snowy_bg.jpg”)
and we know that in web builds this resolves to a fetchable asset whereas in desktop builds it’s a bundled asset. The result here is that different Warp builds can fetch the same asset from different places without much complexity in code.
Removing assets from the binary changes the user experience. There’s now the possibility that, say, selecting a new theme in Warp might be a network-bound operation. This is a worthwhile tradeoff in user experience, and from our testing the difference between a bundled and fetched asset is indistinguishable in most cases.
The result of our efforts so far is that our WASM binary is about 65% smaller than our desktop binaries, and we’re looking to make even more improvements here in the future. As for now, we’re excited to be introducing a Warp on web with the snappiness that users expect from their terminals.
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
