---
title: "How I Reversed Amazon's Kindle Web Obfuscation Because Their App Sucked"
url: "https://blog.pixelmelt.dev/kindle-web-drm/"
fetched_at: 2026-07-04T07:01:40.770965+00:00
source: "blog.pixelmelt.dev"
tags: [blog, raw]
---

# How I Reversed Amazon's Kindle Web Obfuscation Because Their App Sucked

Source: https://blog.pixelmelt.dev/kindle-web-drm/

How I bypassed Amazon’s Kindle web DRM | Hacker News
This article hit #1 on Hacker News, thanks all!
TL;DR
I bought my first ebook from amazon
Amazon's Kindle Android app was really buggy and crashed a bunch
Tried to download my book to use with a functioning reader app
Realized Amazon no longer lets you do that
Decided to reverse engineer their obfuscation system out of spite
Discovered multiple layers of protection including randomized alphabets
Defeated all of them with font matching wizardry
Amazon Made This Personal
The One Time I Tried To Do Things The Right Way
I've been reading ebooks from various sources for years. But this time, I thought: "Let's support the author."
Download Kindle app on Android. Open book.
Crash.
I Just Wanted To Read My Book
App crashes. Fine, I'll use the web reader.
Oh wait, can't download it for offline reading. What if I'm on a plane?
Hold on, I can't even export it to Calibre? Where I keep ALL my other books?
So let me get this straight:
I paid money for this book
I can only read it in Amazon's broken app
I can't download it
I can't back it up
I don't actually own it
Amazon can delete it whenever they want
This is a rental, not a purchase.
This does not say "Rent"
It Becomes Personal
I could've refunded and "obtained" it in 30 seconds. Would've been easier.
But that's not the point.
The point is I PAID FOR THIS BOOK. It's mine. And I'm going to read it in Calibre with the rest of my library even if I have to reverse engineer their web client to do it.
Reversal Time
Kindle Cloud Reader (the web version) actually works. While looking through the network requests, I spotted this:
https://read.amazon.com/renderer/render
To download anything, you need:
1. Session cookies - standard Amazon login
2. Rendering token - from the startReading API call
3. ADP session token - extra auth layer
Sending the same headers and cookies the browser does returns a TAR file.
What's Inside The TAR?
page_data_0_4.json   # The "text" (spoiler: it's not text)
glyphs.json          # SVG definitions for every character
toc.json             # Table of contents
metadata.json        # Book info
location_map.json    # Position mappings
Amazon's Obfuscation Layers of Ebook Hell
Downloaded the first few pages, expected to see text. Got this instead:
{
  "type": "TextRun",
  "glyphs": [24, 25, 74, 123, 91, 18, 19, 30, 4, ...],
  "style": "paragraph"
}
These aren't letters. They're glyph IDs. Character 'T' isn't Unicode 84, it's glyph 24.
And glyph 24 is just a series of numbers that define a stroke path, its just an image of a letter.
It's a substitution cipher! Each character maps to a non-sequential glyph ID.
The Alphabet Changes Every. Five. Pages.
Downloaded the next batch of pages. Same letter 'T' is now glyph 87.
Next batch? Glyph 142.
They randomize the entire alphabet on EVERY request.
This means:
You can only get 5 pages at a time (API hard limit)
Each request gets completely new glyph mappings
Glyph IDs are meaningless across requests
You can't build one mapping table for the whole book
Let Me Show You How Bad This Is
For my 920-page book:
184 separate API requests
needed
184 different random alphabets
to crack
361 unique glyphs
discovered (a-z, A-Z, punctuation, ligatures)
1,051,745 total glyphs
to decode
Fake Font Hints (They're Getting Sneaky)
Some SVG paths contained this garbage:
M695.068,0 L697.51,-27.954 m3,1 m1,6 m-4,-7 L699.951,-55.908 ...
Looking at it, we see these tiny
m3,1 m1,6 m-4,-7
commands, they are micro MoveTo operations.
Why this is evil:
Browsers handle them fine (native Path2D)
Python SVG libraries create spurious connecting lines
Makes glyphs look corrupted when rendered naively
Breaks path-sampling approaches
This is deliberate anti-scraping. The glyphs render perfectly in browser but make it so we cant just compare paths in our parser.
Take a look
Fun!
Eventually I figured out that filling in the complete path mitigated this.
Multiple Font Variants
Not just one font. FOUR variants:
bookerly_normal (99% of glyphs)
bookerly_italic (emphasis)
bookerly_bold (headings)
bookerly_bolditalic (emphasized headings)
Plus special ligatures: ff, fi, fl, ffi, ffl
More variations = more unique glyphs to crack = more pain.
OCR Is Mid (My Failed Attempt)
Tried running OCR on rendered glyphs. Results:
178/348 glyphs recognized (51%)
170 glyphs failed completely
OCR just sucks at single characters without context. Confused 'l' with 'I' with '1'. Couldn't handle punctuation. Gave up on ligatures entirely.
OCR probably need words and sentences to work well.
The Solution That Actually Worked
Every request includes `glyphs.json` with SVG path definitions:
{
  "24": {
    "path": "M 450 1480 L 820 1480 L 820 0 L 1050 0 L 1050 1480 ...",
    "fontFamily": "bookerly_normal"
  },
  "87": {
    "path": "M 450 1480 L 820 1480 L 820 0 L 1050 0 L 1050 1480 ...",
    "fontFamily": "bookerly_normal"
  }
}
Glyph IDs change, but SVG shapes don't.
Why Direct SVG Comparison Failed
First attempt: normalize and compare SVG path coordinates.
Failed because:
Coordinates vary slightly
Path commands represented differently
Pixel-Perfect Matching
Screw coordinate comparison. Let's just render everything and compare pixels.
Render that A
1.
Render every SVG as an image
Use cairosvg (lets us handle those fake font hints correctly)
Render at 512 x 512px for accuracy
2.
Generate perceptual hashes
Hash each rendered image
The hash becomes the unique identifier
Same shape = same hash, regardless of glyph ID
3.
Build normalized glyph space
Map all 184 random alphabets to hash-based IDs
Now glyph "a1b2c3d4..." always means letter 'T'
4.
Match to actual characters
Download Bookerly TTF fonts
Render every character (A-Z, a-z, 0-9, punctuation)
Use SSIM (Structural Similarity Index) to match
Why SSIM Is Perfect For This
SSIM compares image structure, not pixels directly. It handles:
Slight rendering differences
Anti-aliasing variations
Minor scaling issues
For each unknown glyph, find the TTF character with highest SSIM score. That's your letter.
Handling The Edge Cases
Ligatures:
ff, fi, fl, ffi, ffl
These are single glyphs for multiple characters
Had to add them to TTF library manually
Special characters:
em-dash, quotes, bullets
Extended character set beyond basic ASCII
Matched against full Unicode range in Bookerly
Font variants:
Bold, italic, bold-italic
Built separate libraries for each variant
Match against all libraries, pick best score
Now It All Works
Final Statistics
=== NORMALIZATION PHASE ===
Total batches processed: 184
Unique glyphs found: 361
Total glyphs in book: 1,051,745

=== MATCHING PHASE ===
Successfully matched 361/361 unique glyphs (100.00%)
Failed to match: 0 glyphs
Average SSIM score: 0.9527

=== DECODED OUTPUT ===
Total characters: 5,623,847
Pages: 920
Perfect. Every single character decoded correctly.
EPUB Reconstruction With Perfect Formatting
The JSON includes positioning for every text run:
{
  "glyphs": [24, 25, 74],
  "rect": {"left": 100, "top": 200, "right": 850, "bottom": 220},
  "fontStyle": "italic",
  "fontWeight": 700,
  "fontSize": 12.5,
  "link": {"positionId": 7539}
}
I used this to preserve:
Paragraph breaks (Y-coordinate changes)
Text alignment (X-coordinate patterns)
Bold/italic styling
Font sizes
Internal links
The final EPUB is near indistinguishable from the original!
The Real Conclusion
Amazon put real effort into their web obfuscation.
Was It Worth It?
To read one book? No.
To prove a point? Absolutely.
To learn about SVG rendering, perceptual hashing, and font metrics? Probably yes.
Use This Knowledge Responsibly
This is for backing up books YOU PURCHASED.
Don't get me sued into oblivion thanks.
Due to the nature of this post, if you are in any way affiliated with Amazon, please reach out to pixelmelt + at + protonmail.com.
