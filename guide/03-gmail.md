# Gmail

## Send-as addresses

Settings, See all settings, Accounts, Send mail as, Add another email address.

- Use a clear name per brand, for example `Example Support` for `support@example.com`.
- Leave "Treat as an alias" ticked.
- Give `no-reply@` a reply-to of `support@` on the same domain.
- Under "When replying to a message", choose **Reply from the same address to which the message was
  sent**, so replies go out from the right brand automatically.

## Signatures

Create one signature per identity (personal, each brand), then set **Signature defaults** for every
address. Use the same signature for new mail and for replies. Leave `no-reply@` without one. See
[accessible signatures](04-signatures.md) and the [signature builder](../signatures/signature-builder.html).

## Labels and filters

Nested labels keep the sidebar short. A label named `Brand/Support` sits under `Brand`.

| Group | Example sub-labels |
| --- | --- |
| Personal | Enquiries, Sign-ups, Shopping, Automated |
| Each brand | Enquiries, Support, Dev, Team, Newsletter, Automated, Other |
| GitHub | One per organisation, plus Needs you |
| Reports | DMARC |

[`gmail/filters-example.xml`](../gmail/filters-example.xml) implements this. Replace the example
domains, then import it.

### Importing

1. Settings, Filters and blocked addresses.
2. Delete any old filters you are replacing, so old and new rules do not both run.
3. Import filters, choose the file, tick **Apply new filters to existing email**, then Create filters.

### Quiet GitHub notifications

The example filters move GitHub mail out of the inbox, except mail where you are mentioned, asked to
review or assigned. That mail stays in the inbox under `GitHub/Needs you`. GitHub adds a line such
as "You are receiving this because you were mentioned" to each notification, which the filter
matches.

> [!WARNING]
> Never delete a parent label without checking what is nested under it. Gmail removes the nested
> labels too. Label names also ignore case, so `brand` and `Brand` are the same label. Create new
> parent labels before removing old ones.
