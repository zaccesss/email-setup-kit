# Moving from an old provider

Switching provider without losing mail comes down to doing things in the right order.

## Before the switch

1. **Lower the TTL** on the domain's MX record to 300 seconds a day before the move, so the change
   spreads quickly.
2. **List every address** on the old provider: mailboxes, aliases, groups and forwards.
3. **Create the same addresses** on the new provider before changing anything in DNS.
4. **Note every service that logs in with one of those addresses** (banks, registrars, app stores).
   They must keep working after the move.

## The switch

1. Add the new provider's verification record and wait for it to verify.
2. Replace the MX records with the new provider's. Keep only one provider's MX set.
3. Update SPF to include the new provider. Remove the old one only once nothing sends through it.
4. Generate a DKIM key on the new provider and publish it.
5. Send test messages from an outside address to every important address.

## Bringing the old mail across

Most providers offer an import tool that copies mail over IMAP from the old account:

- Google Workspace: Data import in the Admin console.
- Microsoft 365: IMAP migration in the Exchange admin centre.
- Smaller providers: an import page in settings. A desktop mail app can also copy folders between two
  accounts.

> [!TIP]
> Keep the old account for a month after the move. Mail sent during the DNS change can still land
> there. It is also a safety net if the import missed anything.

## After the switch

- Raise the MX TTL back to its normal value.
- Check the DMARC reports for a week to confirm nothing still sends from the old provider.
- Update signatures, out-of-office replies and any website forms that mention old addresses.
