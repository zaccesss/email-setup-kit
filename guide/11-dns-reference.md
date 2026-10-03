# DNS reference

Every record a well set up mail domain uses, in one table. Replace `example.com` with your domain.
Exact values come from your provider.

| Record | Type | Name | Example value | Needed? |
| --- | --- | --- | --- | --- |
| Verification | TXT | `@` | `google-site-verification=...` | Once, to prove you own the domain |
| Mail servers | MX | `@` | Provider's mail servers with priorities | Yes, to receive mail |
| SPF | TXT | `@` | `v=spf1 include:_spf.google.com ~all` | Yes |
| DKIM | TXT or CNAME | `google._domainkey` (name varies) | Provider's public key | Yes |
| DMARC | TXT | `_dmarc` | `v=DMARC1; p=quarantine; rua=mailto:dmarc@example.com` | Yes |
| Report authorisation | TXT | `*._report._dmarc` | `v=DMARC1` | Only when another domain sends its DMARC reports here |
| MTA-STS | TXT | `_mta-sts` | `v=STSv1; id=20260101` | Optional |
| TLS reporting | TXT | `_smtp._tls` | `v=TLSRPTv1; rua=mailto:tls@example.com` | Optional |
| BIMI | TXT | `default._bimi` | `v=BIMI1; l=https://example.com/logo.svg` | Optional |
| Sending service | TXT or CNAME | Given by the service | DKIM and return-path records | When a website or newsletter sends mail |

> [!IMPORTANT]
> Keep exactly one SPF record and one DMARC record per name. Two records under the same name make the
> check fail.

## A domain that sends no mail at all

Stop others from sending as a domain you only use for a website:

| Type | Name | Value |
| --- | --- | --- |
| TXT | `@` | `v=spf1 -all` |
| TXT | `_dmarc` | `v=DMARC1; p=reject` |
| MX | `@` | `.` with priority `0` (a "null MX") |
