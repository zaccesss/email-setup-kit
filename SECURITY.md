# Security Policy

## Scope

This repository holds guides, a static HTML page, an example filter file and a small Python builder.
It runs no service. In scope:

- The signature builder sending anything typed into it anywhere. It is meant to run entirely in the
  browser
- `outlook/build_oft.py` reading or writing anything outside the repository
- Guidance that would weaken mail security if followed, for example a DNS record that is wrong

## Out of scope

- Behaviour of Gmail, Outlook or Google Workspace themselves
- Vulnerabilities in [msgforge](https://pypi.org/project/msgforge/), which belong with that project

## Reporting a vulnerability

> [!IMPORTANT]
> Report privately, never in a public issue. Use
> [GitHub private vulnerability reporting](https://github.com/zaccesss/email-setup-kit/security/advisories/new)
> or email contact@isaacadjei.me with details and reproduction steps. Expect an acknowledgement
> within a few days.

## The shared policy

> [!NOTE]
> The full policy is in [zaccesss/security-policy](https://github.com/zaccesss/security-policy) and on
> [my site](https://isaacadjei.me/security-policy). This file takes precedence where the two differ.
