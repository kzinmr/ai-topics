---
title: "Working around a strange Python problem"
url: "https://www.johndcook.com/blog/2026/10/22/pep-723/"
fetched_at: 2026-10-23T10:01:32.846663+00:00
source: "johndcook.com"
tags: [blog, raw]
---

# Working around a strange Python problem

Source: https://www.johndcook.com/blog/2026/10/22/pep-723/

A Python script that worked a few days ago wouldn’t work today. I suspect it might have something to do with my updating everything I could think of in response to recent security breaches.
I got an error message that said
error: The script contains multiple PEP 723 metadata blocks
I searched on what that means, then took out the blank line in my header
#!/usr/bin/env -S uv run --script

# /// script
# dependencies = ["pyperclip"]
# ///
but I still got the same error message.
The script in question copies miscellaneous snippets of text to the clipboard for me. One of those snippets is the header block that uv requires. The script contains the header block marker
# ///
, and that was the source of the problem.
According to Grok
The PEP 723 parser is purely textual (it uses a regex that scans the whole file). It does not understand Python syntax, so the
# ///
sequences inside your triple-quoted string are treated as a second metadata block.
It suggested changing my quoted string to use
# / / /
and then take out the extra spaces:
"""#!/usr/bin/env -S uv run --script
# / / / script
# dependencies = ["numpy", "matplotlib"]
# / / /
import numpy as np
import matplotlib.pyplot as plt
""".replace("# / / /", "# ///")
This is a dirty hack, but it works.
