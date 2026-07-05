---
title: "Combined 1D and 2D Barcodes"
url: "https://shkspr.mobi/blog/2026/07/combined-1d-and-2d-barcodes/"
fetched_at: 2026-07-05T07:00:46.121271+00:00
source: "shkspr.mobi"
tags: [blog, raw]
---

# Combined 1D and 2D Barcodes

Source: https://shkspr.mobi/blog/2026/07/combined-1d-and-2d-barcodes/

This was a little idea gnawing at the back of my brain. The humble barcode has been in use
since the 1970s
. In the next few years it will likely be replaced with a
2D QR Code
.
I couldn't find anyone who'd made a QR code with an embedded UPC - so I decided to make one.
If you move your phone close to the code (so it can't see the squares in the corners) it should read the number in the 1D barcode. Zoom out and it'll read the URl in the QR code.
The QR code has a high level of error correction - which allows graphics to be placed within it,
as I discussed in 2010
.
The UPC has some whitespace padding around its edges - which makes it easier for some scanners to find, although not all scanners seem to accept it.
Is this in any way useful or desirable? I doubt it! I guess most point-of-sale barcode scanners are somewhat regularly updated - so they should all have the ability to scan newer codes. The embedded code destroys some of the error correction, thus making the QR code more fragile.
It isn't a good idea
.
Still, nice to fiddle about with something, eh?
You may also enjoy:
