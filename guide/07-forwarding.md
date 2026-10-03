# Forwarding setup (free)

Receive mail for your domain in an inbox you already have. Then send as your domain from that same
inbox. This example uses Cloudflare Email Routing with a Gmail account. Other forwarding services
work the same way.

## Receiving

1. Move the domain's DNS to Cloudflare if it is not there already.
2. In the Cloudflare dashboard, open the domain, then Email Routing. Enable it. Cloudflare adds its
   own MX and SPF records.
3. Add a destination address (your existing inbox) and confirm it from the email Cloudflare sends.
4. Create routing rules: `hello@example.com` forwards to the destination. A catch-all rule can forward
   everything else, but it also forwards spam sent to made-up addresses.

## Sending as your domain from Gmail

1. Turn on two-step verification for the Google account. Then create an app password (Google account,
   Security, App passwords).
2. In Gmail: Settings, See all settings, Accounts, Send mail as, Add another email address.
3. Enter your name and `hello@example.com`, then Next step.
4. SMTP server `smtp.gmail.com`, port `587`, username your full Gmail address, password the app
   password, TLS selected.
5. Confirm the code Gmail sends to `hello@example.com`. It arrives through the forwarding rule.

> [!WARNING]
> Mail sent this way leaves through Gmail's servers, so add Google to the domain's SPF record:
> `v=spf1 include:_spf.mx.cloudflare.net include:_spf.google.com ~all`. Gmail cannot sign it with
> your domain's DKIM key, so DMARC passes through SPF alignment only. Start DMARC at `p=none` and read
> the reports before tightening.

## Limits worth knowing

- Forwarding services do not store mail. If the destination inbox is full or down, mail can bounce.
- Forwarded spam counts against the destination inbox's reputation. Keep catch-all rules off unless
  you need them.
- For a team, a hosted mailbox is usually less work in the long run.
