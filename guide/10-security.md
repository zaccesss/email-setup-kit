# Security

Email is the key to every other account, since password resets arrive there. Protect it first.

## The account

- **Two-step verification** with an authenticator app or a security key. Avoid SMS where possible.
- **Recovery codes** stored in a password manager, never as a file in Downloads or in cloud notes.
- **A recovery address** on a different provider, so losing one account does not lock you out of
  both.
- **Review connected apps** every few months and remove anything you no longer use.

## The domain

- **Registrar lock and two-step verification** on the domain registrar account. Losing the domain
  means losing every address on it.
- **Auto-renew** on, with a card that will not expire before the renewal date.
- **DMARC at `p=quarantine` or `p=reject`** once the reports show every legitimate sender passes, so
  nobody can send convincing mail as you.

## Transport security (optional)

| Standard | What it does | Record |
| --- | --- | --- |
| MTA-STS | Tells other servers to deliver to you only over encrypted connections | `_mta-sts` TXT plus a policy file at `https://mta-sts.example.com/.well-known/mta-sts.txt` |
| TLS-RPT | Sends daily reports about failed encrypted deliveries | `_smtp._tls` TXT, for example `v=TLSRPTv1; rua=mailto:tls@example.com` |
| BIMI | Shows your logo next to your mail in supporting inboxes | `default._bimi` TXT. Needs DMARC enforcement. Gmail also needs a mark certificate |

## Everyday habits

- Check the real sender address and the link destination before acting on any request for money,
  passwords or codes.
- Use separate addresses or plus-addressing (`you+shop@example.com`) for sign-ups, so a leaked
  address shows where it came from and is easy to filter.
- Never put passwords or recovery codes in an email, even to yourself.
