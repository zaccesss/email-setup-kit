# Deliverability: SPF, DKIM and DMARC

Three DNS records decide whether your mail lands in the inbox and whether anyone else can pretend to
be you. Every domain that sends or receives mail needs all three, alias domains included.

## SPF

A `TXT` record on the domain itself that lists who may send as it.

```text
v=spf1 include:_spf.google.com ~all
```

Add an `include:` for every other service that sends as the domain, for example a newsletter or
transactional mail provider, before the final `~all`. Keep to one SPF record per domain.

## DKIM

A signing key published as a `TXT` record, usually at `google._domainkey`. In the Google Admin
console: Apps, Google Workspace, Gmail, Authenticate email. Choose the domain, generate a new record,
add it in your DNS, then click Start authentication.

> [!WARNING]
> Edit the existing `google._domainkey` record rather than adding a second one. Two records under the
> same name make DKIM fail.

## DMARC

A `TXT` record at `_dmarc` that tells other providers what to do with mail that fails SPF and DKIM,
and where to send reports.

```text
v=DMARC1; p=quarantine; rua=mailto:dmarc@example.com
```

- `p=quarantine` sends failing mail to spam. Start with `p=none` if you are unsure every sender is
  signing correctly, watch the reports for a week, then tighten.
- Check every service that sends as the domain first. A website contact form that sends from your
  domain through a server you do not control will fail DMARC.

### Reports for several domains in one place

If `rua` on `brand.example` points to an address on a different domain, the receiving domain must
agree to accept those reports. Add this record on the domain that receives them:

| Type | Name | Content |
| --- | --- | --- |
| TXT | `*._report._dmarc` | `v=DMARC1` |

## Checking it works

```bash
dig +short TXT example.com
dig +short TXT google._domainkey.example.com
dig +short TXT _dmarc.example.com
```

Then send a message to an external address and open the original message: the headers should show
`spf=pass`, `dkim=pass` and `dmarc=pass`.
