# Accessible signatures

A signature is read by screen readers, in dark mode, on phones and by people with low vision. These
choices keep it readable everywhere.

| Need | What to do |
| --- | --- |
| Screen readers | Use real text, never one image of the whole signature. Give every logo alt text. Give purely decorative icons empty alt text (`alt=""`) so they are skipped |
| Low vision | Dark text on white with a contrast ratio of at least 7:1. Keep names bold and the body text at a comfortable size |
| Colour vision differences | Underline links as well as colouring them. Make link text say where it goes ("Book a meeting", never "click here") |
| Dark mode | Many clients turn text light but leave images unchanged. Draw logos so they read on light and dark backgrounds. A dark logo can sit on a small white tile instead |
| Phones | Keep a plain-text version for mobile apps, which often break formatted signatures |

## Images

> [!IMPORTANT]
> Mail clients show neither SVG nor colour-scheme switching, so logos must be PNG. Host them at a
> stable public address. Gmail loads images through Google's image proxy, which some bot-protection
> services block. If a logo shows as broken, host it somewhere plain such as GitHub's raw file host.

Uploading the image straight into the signature editor also works and avoids hosting entirely.

## Layout

The [signature builder](../signatures/signature-builder.html) uses a two-column table: the logo on
the left, a thin coloured divider, then name, role and links on the right. Tables are used because
email clients support them far better than modern CSS layout.

## A short reply signature

On long threads a full signature on every reply adds clutter. A short one (name, role and one line of
links) set as the default for replies keeps threads tidy, with the full signature on new mail.
