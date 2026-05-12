"""Comments hook placeholder.

The comment system is intentionally disabled. Keep this hook as a no-op so
enabling it by mistake won't load a third-party comment backend.
"""


def on_page_markdown(markdown, **kwargs):
    return markdown


def on_page_content(html, **kwargs):
    return html
