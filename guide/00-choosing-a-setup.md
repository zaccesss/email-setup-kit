# Choosing a setup

Before touching DNS, decide how mail for your domain will be received and sent. There are three common
shapes.

| Setup | How it works | Good for | Cost |
| --- | --- | --- | --- |
| **Hosted mailbox** | A provider such as Google Workspace, Microsoft 365, Fastmail, Proton Mail or Zoho Mail hosts the inbox for your domain | Anyone who wants one proper inbox with their own domain | A monthly fee per user on most plans |
| **Forwarding only** | A free forwarding service (for example Cloudflare Email Routing) passes mail on to an inbox you already have. You send through that inbox using its SMTP server | Personal domains on a budget | Free |
| **Sending only** | A transactional or newsletter service sends from your domain. Replies go somewhere else | Websites, apps and newsletters | Usually free at low volume |

Most people combine them: a hosted mailbox or forwarding for people, plus a sending service for the
website. Each needs its own DNS records, covered in [deliverability](02-deliverability.md).

> [!TIP]
> Check each provider's current plans before choosing. Free tiers, user limits and alias limits change
> often.

## Questions that decide it

- **How many people need their own login?** One person can usually cover several domains with one
  mailbox. A team usually needs a mailbox each or shared mailboxes.
- **Do you need calendars, documents and video calls together?** Then a suite (Google Workspace or
  Microsoft 365) is simpler than separate tools.
- **Is privacy the priority?** Providers such as Proton Mail and Fastmail focus on it.
- **Will a website or app send mail?** Add a sending service for that, rather than sending through
  a personal mailbox.

## Next steps

- Hosted mailbox: [domains and mailboxes](01-domains.md).
- Forwarding only: [forwarding setup](07-forwarding.md).
- Moving from an existing provider: [migration](08-migration.md).
