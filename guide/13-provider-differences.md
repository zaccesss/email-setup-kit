# How providers differ

Something that works in Gmail may not work in Outlook. The reverse happens too. This guide covers the
differences that matter most when setting up and sending mail. Providers change their features
often, so check their current help pages before relying on a detail.

## Organising mail

| | Gmail | Outlook and Microsoft 365 | Apple Mail and iCloud | Proton Mail | Fastmail |
| --- | --- | --- | --- | --- | --- |
| Model | Labels. One message can have several | Folders. One message lives in one folder. Categories add colour tags | Folders | Folders and labels | Folders. Labels can be switched on |
| Server-side filters | Filters | Rules | Rules on iCloud.com. Rules in the Mac app run only while the app is open | Filters, written as Sieve scripts under the hood | Rules, written as Sieve scripts under the hood |
| Export and import | Filters as an XML file | Not on the web. Classic Outlook for Windows exports rules as a `.rwz` file | No | Sieve scripts can be copied | Sieve scripts can be copied |

> [!TIP]
> A rule that runs on the server works on every device. A rule that runs in a desktop app only works
> while that app is open, so prefer server-side rules wherever possible.

## Addresses

| | Gmail | Outlook and Microsoft 365 | iCloud | Proton Mail | Fastmail |
| --- | --- | --- | --- | --- | --- |
| Plus-addressing (`you+tag@`) | Yes | Yes in Microsoft 365 | Check current support. Hide My Email offers random addresses instead | Yes | Yes |
| Several domains on one account | Alias domains in Workspace | Accepted domains, then addresses added per mailbox | Custom domains on iCloud+ | Custom domains on paid plans | Several domains per account |
| Catch-all | Workspace routing rules | Not on standard plans | No | On paid plans | Yes |

## Signatures

| | Where they live | Notes |
| --- | --- | --- |
| Gmail | Per account, synced everywhere. A default can be set per send-as address | The phone app uses its own mobile signature |
| Outlook on the web and new Outlook | Per account in the cloud, synced between web and new Outlook | Classic Outlook for Windows keeps its own local signatures |
| Outlook phone app | Its own setting | Plain text is the reliable option |
| Apple Mail | Per device | Signatures made on a Mac do not reliably appear on an iPhone. Set each device |
| Proton Mail and Fastmail | Per account or per address | Images are best hosted or uploaded through the web app |

## How HTML renders

The same signature or newsletter can look different in each app. The biggest differences:

| Feature | Gmail | Outlook on the web and new Outlook | Classic Outlook for Windows | Apple Mail |
| --- | --- | --- | --- | --- |
| Rendering | Browser engine | Browser engine | Microsoft Word's engine | Browser engine |
| Tables for layout | Yes | Yes | Yes. The most reliable layout method | Yes |
| Rounded corners and shadows | Mostly | Mostly | No | Yes |
| SVG images | No | No | No | Yes |
| Web fonts | Limited | Limited | No. Falls back to a system font | Yes |
| Dark mode | Can recolour text and backgrounds | Can recolour text and backgrounds | Can recolour text and backgrounds | Follows the colour scheme of the message |

> [!IMPORTANT]
> For anything that must look the same everywhere, use tables for layout, inline styles, PNG images
> with set width and height and fonts that every system has, such as Arial. The
> [signature builder](../signatures/signature-builder.html) follows these rules.

## Templates and canned replies

| | Gmail | Outlook | Apple Mail |
| --- | --- | --- | --- |
| Feature | Templates (switch on under Advanced settings) | My templates on the web, `.oft` files in desktop Outlook | Stationery and saved drafts only |
| Shareable as a file | No | Yes, as `.oft` | No |

The [Outlook builder](../outlook/) produces `.oft` files. For Gmail, keep the template text in a
document and paste it into a new template once.
