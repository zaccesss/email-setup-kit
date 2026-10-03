# Sending services and newsletters

Websites, apps and newsletters should send through a dedicated service, not a personal mailbox. It
protects your inbox's reputation and gives you delivery logs.

## Use a subdomain

Send automated mail from a subdomain such as `mail.example.com` or `news.example.com`. If a campaign
causes complaints, the damage stays on that subdomain and your main address keeps a clean reputation.

## Records each service needs

| Record | Purpose |
| --- | --- |
| DKIM | The service's own signing key, usually one or more `TXT` or `CNAME` records it gives you |
| SPF | Usually on a return-path subdomain the service names, so your main SPF record stays short |
| MX (sometimes) | For bounce handling on the return-path subdomain |
| DMARC | Inherited from the main domain unless you add one for the subdomain |

> [!IMPORTANT]
> An SPF record may trigger at most 10 DNS lookups. Every `include:` counts. Putting each service's
> SPF on its own subdomain avoids hitting the limit.

## Newsletters

- Send from an address people recognise, such as `newsletter@example.com`, with replies going to a
  real inbox.
- Use double opt-in so only people who confirmed their address are added.
- Include a working unsubscribe link. Large mailbox providers also expect one-click unsubscribe
  headers from bulk senders. Most newsletter services add them automatically.
- Keep bulk mail off the domain your people send personal mail from.

## Website contact forms

A contact form should send through a sending service as `no-reply@example.com` with the visitor's
address as reply-to. Sending as the visitor's own address fails their domain's DMARC and lands in
spam.
