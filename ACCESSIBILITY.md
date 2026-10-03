# Accessibility

Email is read with screen readers, in dark mode, on small screens and by people with low vision. This
repository is built around that.

## The signature builder

| Need | What it does |
| --- | --- |
| Screen readers | Every form field has a visible label. Signatures use real text. The logo gets the description you type as its alt text |
| Low vision | Name and body text are near-black on white. The page follows your system's light or dark setting |
| Colour vision differences | Links are underlined as well as coloured. The builder warns when the accent colour falls below a 4.5:1 contrast ratio on white |
| Keyboard use | Every field and button can be reached with Tab, with a clear focus outline |

## The guides

- A real heading outline, tables for comparisons and code blocks for every command and record.
- Link text says where it goes.
- Callouts are labelled (Tip, Important, Warning) rather than relying on colour.

## Known gaps

> [!WARNING]
> The copy buttons use the browser clipboard. If a browser blocks it, select the dashed box and press
> Cmd+C (Ctrl+C on Windows and Linux).

- Mail clients decide how a pasted signature finally looks. Outlook dark mode, for example, changes
  text colours but not images, which the [signature guide](guide/04-signatures.md) explains.

## Feedback wanted

If something here gets in the way, open an [issue](https://github.com/zaccesss/email-setup-kit/issues/new/choose)
describing what happened and what would work better.

## The shared statement

> [!NOTE]
> I keep one shared accessibility statement for all my projects:
> [zaccesss/accessibility](https://github.com/zaccesss/accessibility) or on
> [my site](https://isaacadjei.me/accessibility). This file takes precedence where the two differ.
