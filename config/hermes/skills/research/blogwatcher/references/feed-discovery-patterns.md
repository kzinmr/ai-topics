# Feed Discovery Patterns

Known RSS/Atom feed URL patterns by platform, discovered during curated-list ingestion sessions.

## Platform Patterns

| Platform | Feed URL Pattern | Notes |
|---|---|---|
| **WordPress** | `https://example.com/feed/` | Most common. Also `/comments/feed/` |
| **Blogger/Blogspot** | `https://example.blogspot.com/feeds/posts/default` | Also works: `?alt=rss` param |
| **GitHub Pages (Jekyll)** | `https://username.github.io/feed.xml` | Or `/index.xml`, `/atom.xml` |
| **Hugo** | `https://example.com/index.xml` | Default Hugo output |
| **Quarto (GitHub Pages)** | `https://username.github.io/blog/index.xml` | **False positive risk**: `feed: true` in `_quarto.yml` generates a `<link>` tag for `index.xml`, but the file may not exist on `gh-pages` branch. Always verify with `curl -sI`. See blogwatcher skill: "Quarto on GitHub Pages: False Positive RSS Feeds". |
| **Substack** | `https://example.substack.com/feed` | Or `/feed.xml` |
| **Ghost** | `https://example.com/rss/` | Common Ghost default |
| **Bear Blog** | `https://example.bearblog.dev/feed/` | |
| **Medium** | `https://medium.com/feed/@username` | |
| **Write.as / WriteFreely** | `https://example.com/feed/` | Atom feed |
| **Micro.blog** | `https://example.micro.blog/feed.xml` | |
| **Notion-based sites** | Often no RSS; use `--scrape-selector` | |
| **YouTube Channel** | `https://www.youtube.com/feeds/videos.xml?channel_id=CHANNEL_ID` | Find channel ID: `yt-dlp --print channel_id --playlist-end 1 "URL"`. Channel IDs are permanent (unlike handles). Returns video descriptions, not transcripts. |

## Feed Discovery Commands

### Auto-discover via HTML `<link>` tags
```bash
curl -sL https://example.com | grep -iE '(rss|atom|feed)' | grep -oP 'href="[^"]*\.(xml|rss|atom)"'
```

### Python-based discovery (more robust)
```python
import urllib.request, re
req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
resp = urllib.request.urlopen(req, timeout=10)
html = resp.read().decode('utf-8', errors='replace')

# Find <link> with type application/rss+xml or application/atom+xml
for m in re.finditer(
    r'<link[^>]*?(?:type\s*=\s*["\'](?:application/(?:rss|atom)\+xml)["\'])[^>]*?(?:href\s*=\s*["\']([^"\']+)["\'])',
    html, re.I):
    print(m.group(1))
```

### Test feed URL directly
```bash
# Check if URL returns XML (200 + content-type)
curl -sI "https://example.com/feed.xml" | head -5
```

### Verify Quarto feeds on GitHub Pages
```bash
# Step 1: Check if index.xml exists
curl -sI "https://username.github.io/blog/index.xml" | head -5

# Step 2: Check the gh-pages branch for xml files
curl -sL "https://api.github.com/repos/owner/repo/git/trees/gh-pages?recursive=1" | \
  python3 -c "import sys,json; [print(t['path']) for t in json.load(sys.stdin).get('tree',[]) if 'xml' in t['path'].lower()]"
```

## Feed URLs Discovered for ClickHouse Curated List (2026-05-04)

| Blog | Platform | Feed URL |
|---|---|---|
| Daniel Lemire | WordPress | `https://lemire.me/blog/feed/` |
| Ash Vardanyan | Hugo? | `https://ashvardanian.com/feed.xml` |
| Wojciech Muła | Custom | `http://0x80.pl/notesen.rss` |
| Daniel Kutenin | WordPress | `https://danlark.org/feed/` |
| Alisa Sireneva | Custom | `https://purplesyringa.moe/blog/feed.rss` |
| Peter Kankowski | Drupal | `https://www.strchr.com/?feed=/` |
| Fangrui Song | Custom | `https://maskray.me/atom.xml` |
| Justine Tunney | Custom | `https://justine.lol/rss.xml` |
| LLVM Blog | GitHub Pages | `https://blog.llvm.org/index.xml` |
| LWN.net | Custom | `https://lwn.net/headlines/rss` |
| Kyle Kingsbury (Jepsen) | Custom | `https://jepsen.io/blog/feed.xml` |
| Database Architects | Blogger | `https://databasearchitects.blogspot.com/feeds/posts/default` |
| Mark Callaghan | Blogger | `https://smalldatum.blogspot.com/feeds/posts/default` |
| Marc Brooker | Hugo? | `https://brooker.co.za/blog/rss.xml` |
| Yann Collet | Blogger | `https://fastcompression.blogspot.com/feeds/posts/default` |
| Russ Cox | Custom | `https://research.swtch.com/feed.atom` |
| Kamila Szewczyk | Custom | `https://iczelia.net/feed.xml` |
| Charles Bloom | Blogger | `https://cbloomrants.blogspot.com/feeds/posts/default` |
| Brendan Gregg | Custom | `https://www.brendangregg.com/blog/rss.xml` |
| Dan Luu | Custom | `https://danluu.com/atom.xml` |
| Nikita Lapkov | Hugo? | `https://laplab.me/posts/index.xml` |
| Ben Boyter | Hugo | `https://boyter.org/index.xml` |
| Andrej Karpathy | GitHub Pages | `https://karpathy.github.io/feed.xml` |
| Jay Mody | GitHub Pages | `https://jaykmody.com/feed.xml` |
| Bartosz Ciechanowski | Custom | `https://ciechanow.ski/archives/atom.xml` |
| Fabien Sanglard | Custom | `https://fabiensanglard.net/rss.xml` |
| Julia Evans | Custom | `https://jvns.ca/atom.xml` |
| Malte Skarupke | WordPress | `https://probablydance.com/feed/` |
| Preshing | Custom | `https://preshing.com/feed` |
| Marek Vavruša | Custom | `https://idea.popcount.org/rss.xml` |
| V8 Blog | Custom | `https://v8.dev/features.atom` |
| Matt Mahoney | Custom | `https://mattmahoney.net/dc/feed.xml` |
| **LangChain Blog** | **Webflow** | `https://www.langchain.com/blog/rss.xml` |
