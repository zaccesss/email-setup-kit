# email-setup-kit

Custom-domain email done properly: one inbox for several domains, mail that passes SPF, DKIM and
DMARC, Gmail filters that keep the inbox calm, accessible signatures and Outlook templates built from
code.

## What is inside

| Folder | What it gives you |
| --- | --- |
| [`guide/`](guide/) | Step-by-step guides, from domains and DNS to filters, signatures and Outlook |
| [`signatures/`](signatures/) | `signature-builder.html`: fill in your details, preview and copy accessible signatures straight into Gmail or Outlook |
| [`gmail/`](gmail/) | `filters-example.xml`: an importable filter set with nested labels and quiet GitHub notifications |
| [`outlook/`](outlook/) | A Python builder that turns plain text into importable Outlook `.oft` templates |

## Start here

1. [Domains and mailboxes](guide/01-domains.md): one account, several domains, every address on all
   of them.
2. [Deliverability](guide/02-deliverability.md): SPF, DKIM and DMARC records that actually pass.
3. [Gmail](guide/03-gmail.md): send-as addresses, signature defaults, labels and filters.
4. [Accessible signatures](guide/04-signatures.md): what makes a signature readable for everyone.
5. [Outlook](guide/05-outlook.md): signatures, rules and templates on Microsoft 365.
6. [Gotchas](guide/06-gotchas.md): the problems that are hard to spot until they bite.

> [!TIP]
> Replace every `example.com` and `Your Name` with your own details. The builder page and the filter
> file have them in obvious places.

## Building Outlook templates

```bash
python3 -m venv .venv
.venv/bin/pip install -r outlook/requirements.txt
.venv/bin/python outlook/build_oft.py
```

The `.oft` files land in `outlook/build/`. Import them in Outlook on the web under Settings, Email,
Templates, Add, Add OFT.

## Licence

[MIT](LICENSE).
