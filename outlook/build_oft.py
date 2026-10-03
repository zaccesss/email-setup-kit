"""Build Outlook .oft templates from outlook/templates.py.

Usage, from the repository root:
    python3 -m venv .venv && .venv/bin/pip install -r outlook/requirements.txt
    .venv/bin/python outlook/build_oft.py

The files are written to outlook/build/. Import them in Outlook on the web
under Settings, Email, Templates, Add, Add OFT.
"""

import html
import importlib.util
import sys
from pathlib import Path

import msgforge

HERE = Path(__file__).resolve().parent
OUT = HERE / "build"

spec = importlib.util.spec_from_file_location("templates", HERE / "templates.py")
templates = importlib.util.module_from_spec(spec)
spec.loader.exec_module(templates)

FONT = "font-family:Aptos,Arial,sans-serif;font-size:14pt;color:#111111;"


def paragraphs(text: str) -> str:
    return "".join(
        f'<p style="margin:0 0 12px;">{html.escape(p).replace(chr(10), "<br>")}</p>'
        for p in text.split("\n\n")
    )


def build() -> int:
    OUT.mkdir(exist_ok=True)
    for old in OUT.glob("*.oft"):
        old.unlink()
    signature = templates.SIGNATURE.strip()
    for number, (name, subject, body) in enumerate(templates.TEMPLATES, 1):
        sig_html = f"<br>{paragraphs(signature)}" if signature else ""
        html_body = f'<html><body><div style="{FONT}">{paragraphs(body)}{sig_html}</div></body></html>'
        text_body = f"{body}\n\n{signature}" if signature else body
        message = msgforge.Message(subject=subject, html_body=html_body, text_body=text_body)
        message.save(OUT / f"{number:02d} {name}.oft")
    return len(templates.TEMPLATES)


if __name__ == "__main__":
    expected = build()
    built = len(list(OUT.glob("*.oft")))
    print(f"built {built} of {expected} templates in {OUT}")
    sys.exit(0 if built == expected else 1)
