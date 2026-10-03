# Workflows

| Workflow | Runs on | What it does |
| --- | --- | --- |
| [`markdownlint.yml`](markdownlint.yml) | Push to `main`, every pull request | Lints every markdown file against [`.markdownlint.json`](../../.markdownlint.json) |
| [`build-templates.yml`](build-templates.yml) | Every pull request | Builds the example Outlook templates and fails if any does not build |

Both can also be run by hand from the Actions tab.
