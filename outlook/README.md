# Outlook template builder

Turns the plain-text templates in [`templates.py`](templates.py) into `.oft` files that Outlook can
import, so a set of email templates can live in version control and be rebuilt in one command.

```bash
python3 -m venv .venv
.venv/bin/pip install -r outlook/requirements.txt
.venv/bin/python outlook/build_oft.py
```

The files land in `outlook/build/`, which Git ignores. Import each one in Outlook on the web under
Settings, Email, Templates, Add, Add OFT.

> [!TIP]
> Import one file first to check it, then the rest. Each `.oft` is imported separately.

The builder uses [msgforge](https://pypi.org/project/msgforge/), a pure Python writer for Outlook's
file format, so it runs on macOS, Linux and Windows without Outlook installed.
