# Domains and mailboxes

The aim: one inbox that receives mail for several domains, where every address you create works on
all of them, without paying for extra mailboxes.

## One account, several domains

In Google Workspace a domain can be added in two ways:

| Type | How it behaves | Use it for |
| --- | --- | --- |
| **User alias domain** | Mirrors the primary domain. Every user and alias on the primary domain also exists on this one automatically | Every extra domain you own, including brand or project domains |
| **Secondary domain** | Separate. Each address has to be created by hand and uses up alias slots | Rarely needed for a single person |

> [!IMPORTANT]
> Prefer alias domains. A user can have only 30 aliases. On a secondary domain every address uses
> one. On an alias domain, `hello@primary.example` automatically becomes `hello@brand.example` too,
> with no extra slots.

## Planning the addresses

Create aliases once on the primary domain. They then appear on every alias domain. Standard role
addresses cover most needs:

| Address | Use |
| --- | --- |
| `contact@` | The main public address on a website or in a repository |
| `hello@` or `info@` | A friendlier general address. Pick one, not both |
| `support@` | Help requests from customers or users |
| `billing@` | Invoices and payments |
| `security@` | Vulnerability reports. Pair it with a `security.txt` file on your website |
| `privacy@` | Data protection and privacy requests |
| `postmaster@` | Expected by mail standards for delivery problems. Every domain should have one |
| `abuse@` | Expected for spam and abuse reports |
| `no-reply@` | The sender for automated mail. Give it a reply-to that reaches a person |
| `team@` | Reaching everyone involved in a project |

> [!TIP]
> For sign-ups and shopping, use plus-addressing instead of new aliases: `you+shop@example.com`
> arrives in your normal inbox and is easy to filter. Gmail and Microsoft 365 both support it.

> [!TIP]
> Before deleting an alias, search the inbox for mail sent to it. An address you no longer use may
> still be the login for an account somewhere.

## Switching a domain from secondary to alias

There is no in-place switch. The order that avoids losing anything:

1. List every address on the secondary domain.
2. Make sure each one exists on the primary domain. Free a slot by deleting the secondary copy first
   if the account is full.
3. Remove the secondary domain, then add it straight back as a user alias domain. The DNS records
   stay, so it usually verifies at once.
4. Activate Gmail for it, then generate a new DKIM key (see [deliverability](02-deliverability.md)).

Mail to that domain bounces only for the few minutes between steps 3 and 4.

## Parking a domain that has no website yet

A domain with mail but no site can still send visitors somewhere useful. With the DNS on Cloudflare:

1. Add `AAAA` records for `@` and `www` pointing to `100::`, proxied. This placeholder address exists
   only so Cloudflare can answer the request.
2. Add a redirect rule in that domain's zone: all incoming requests, static, `302` to the page you
   want, for example a GitHub organisation.

A `302` is temporary, so a real site can replace it later without browsers having cached the
redirect.
