#!/usr/bin/env python3
"""Simple wiki browser - serves markdown files as HTML with Obsidian-style wikilinks."""
import os
import re
from pathlib import Path
from http.server import HTTPServer, SimpleHTTPRequestHandler
from urllib.parse import unquote

WIKI_DIR = Path.home() / "wiki"
PORT = 8000

HTML_TEMPLATE = """
<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{title} - AI Topics Wiki</title>
<link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/github-markdown-css@5/github-markdown-light.min.css">
<script src="https://cdn.jsdelivr.net/npm/marked/marked.min.js"></script>
<style>
  body {{ max-width: 900px; margin: 0 auto; padding: 20px; font-family: -apple-system, system-ui, sans-serif; }}
  .nav {{ background: #f6f8fa; padding: 12px 16px; border-radius: 8px; margin-bottom: 20px; display: flex; gap: 16px; align-items: center; }}
  .nav a {{ color: #0969da; text-decoration: none; }}
  .nav a:hover {{ text-decoration: underline; }}
  .file-list {{ list-style: none; padding: 0; }}
  .file-list li {{ padding: 6px 0; border-bottom: 1px solid #eee; }}
  .file-list a {{ color: #0969da; text-decoration: none; }}
  .file-list .dir {{ font-weight: bold; }}
  .markdown-body {{ padding: 16px; }}
  .breadcrumb {{ color: #666; font-size: 0.9em; }}
</style>
</head>
<body>
<div class="nav">
  <a href="/"><strong>📚 AI Topics Wiki</strong></a>
  <a href="/index.md">Index</a>
  <a href="/SCHEMA.md">Schema</a>
  <a href="/log.md">Log</a>
  <a href="/raw/articles/">Raw Sources</a>
</div>
{content}
</body>
</html>
"""


def render_directory(dirpath: Path, url_path: str) -> str:
    """Render directory listing."""
    items = sorted(dirpath.iterdir(), key=lambda p: (not p.is_dir(), p.name.lower()))
    lines = [f'<h2>📁 {url_path or "/"}</h2>', '<ul class="file-list">']
    if url_path and url_path != "/":
        parent = "/".join(url_path.rstrip("/").split("/")[:-1]) or "/"
        lines.append(f'<li><a href="{parent}">⬆️ ..</a></li>')
    for item in items:
        rel = item.relative_to(WIKI_DIR)
        if item.name.startswith("."):
            continue
        if item.is_dir():
            lines.append(f'<li class="dir"><a href="/{rel}/">📁 {item.name}/</a></li>')
        elif item.suffix == ".md":
            lines.append(f'<li><a href="/{rel}">📄 {item.name}</a></li>')
        else:
            lines.append(f'<li>📎 {item.name}</li>')
    lines.append('</ul>')
    return HTML_TEMPLATE.format(title=url_path or "Home", content="\n".join(lines))


def render_markdown(filepath: Path) -> str:
    """Render markdown file as HTML."""
    text = filepath.read_text(encoding="utf-8")
    # Convert wikilinks to markdown links
    text = re.sub(r'\[\[([^|\]]+)\|([^\]]+)\]\]', r'[\2](\1.md)', text)
    text = re.sub(r'\[\[([^\]]+)\]\]', r'[\1](\1.md)', text)
    # Escape for JS
    text_escaped = text.replace('\\', '\\\\').replace('`', '\\`').replace('${', '\\${')
    content = f"""
    <div class="breadcrumb">{filepath.relative_to(WIKI_DIR)}</div>
    <div class="markdown-body" id="content"></div>
    <script>
    document.getElementById('content').innerHTML = marked.parse(`{text_escaped}`);
    </script>
    """
    return HTML_TEMPLATE.format(title=filepath.stem, content=content)


class WikiHandler(SimpleHTTPRequestHandler):
    def do_GET(self):
        path = unquote(self.path).rstrip("/") or "/"
        filepath = WIKI_DIR / path.lstrip("/")

        if path == "/" or (filepath.is_dir()):
            dirpath = WIKI_DIR if path == "/" else filepath
            if dirpath.is_dir():
                html = render_directory(dirpath, path)
                self.send_response(200)
                self.send_header("Content-Type", "text/html; charset=utf-8")
                self.end_headers()
                self.wfile.write(html.encode())
                return

        if filepath.exists() and filepath.suffix == ".md":
            html = render_markdown(filepath)
            self.send_response(200)
            self.send_header("Content-Type", "text/html; charset=utf-8")
            self.end_headers()
            self.wfile.write(html.encode())
            return

        if filepath.exists():
            return super().do_GET()

        self.send_error(404)

    def log_message(self, format, *args):
        pass  # Suppress logs


if __name__ == "__main__":
    server = HTTPServer(("", PORT), WikiHandler)
    print(f"Wiki server running on http://0.0.0.0:{PORT}")
    server.serve_forever()
