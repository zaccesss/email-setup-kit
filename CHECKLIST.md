# Setup checklist

Work through it top to bottom. Each line links to the guide that explains it.

## Domain and provider

- [ ] Choose a setup: hosted mailbox, forwarding or both ([choosing a setup](guide/00-choosing-a-setup.md))
- [ ] Turn on registrar lock, auto-renew and two-step verification at the registrar ([security](guide/10-security.md))
- [ ] Add and verify the domain with the provider ([domains](guide/01-domains.md))
- [ ] Add extra domains as alias domains where the provider supports it ([domains](guide/01-domains.md))

## DNS

- [ ] MX records for the provider ([DNS reference](guide/11-dns-reference.md))
- [ ] One SPF record covering every sender ([deliverability](guide/02-deliverability.md))
- [ ] DKIM generated and published, then authentication started ([deliverability](guide/02-deliverability.md))
- [ ] DMARC at `p=none` first, then `p=quarantine` once the reports are clean ([deliverability](guide/02-deliverability.md))
- [ ] Domains that send no mail locked down with a null MX, `-all` and `p=reject` ([DNS reference](guide/11-dns-reference.md))

## Addresses

- [ ] Role addresses created: `contact@`, `support@`, `postmaster@`, `abuse@` ([domains](guide/01-domains.md))
- [ ] `no-reply@` sends with a reply-to that reaches a person ([Gmail](guide/03-gmail.md))
- [ ] Send-as addresses added with clear names ([Gmail](guide/03-gmail.md))

## Inbox

- [ ] Labels and filters imported ([Gmail](guide/03-gmail.md))
- [ ] Signatures created and set as defaults per address ([signatures](guide/04-signatures.md))
- [ ] Short reply signature and a plain-text phone signature ([signatures](guide/04-signatures.md))
- [ ] Out-of-office text written, switched off until needed ([inbox habits](guide/12-inbox-habits.md))

## Security

- [ ] Two-step verification on with an app or security key ([security](guide/10-security.md))
- [ ] Recovery codes in a password manager ([security](guide/10-security.md))
- [ ] Recovery address on a different provider ([security](guide/10-security.md))

## Website and newsletters

- [ ] Sending service on its own subdomain with DKIM ([sending services](guide/09-sending-services.md))
- [ ] Contact form sends as `no-reply@` with the visitor as reply-to ([sending services](guide/09-sending-services.md))

## Final check

- [ ] Test mail from an outside address shows `spf=pass`, `dkim=pass` and `dmarc=pass` ([deliverability](guide/02-deliverability.md))
