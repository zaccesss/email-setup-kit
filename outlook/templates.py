"""Email templates to build into Outlook .oft files.

Each entry is (file name, subject, body). Edit the list, change SIGNATURE to
your own and run build_oft.py. Square brackets mark the parts to fill in each
time a template is used.
"""

GREETING = "Hello [Name],"

# plain text appended under every body; leave empty to rely on Outlook's own signature
SIGNATURE = """Your Name
Your role
example.com"""

TEMPLATES = [
    ("Meeting request", "Meeting request: [topic]", f"""{GREETING}

I would like to arrange a short meeting to discuss [topic].

I am free on [day and time] or [day and time], in person or online. If neither suits, I am happy to work around your availability.

Thank you for your time.

Kind regards,
[Your first name]"""),
    ("Follow-up after a meeting", "Thank you: [topic] meeting on [date]", f"""{GREETING}

Thank you for meeting with me on [date] to discuss [topic].

To confirm what we agreed:
1. [Point or action]
2. [Point or action]
3. [Next step and date]

Please let me know if I have missed anything.

Kind regards,
[Your first name]"""),
    ("Absence notice", "Absence on [date]", f"""{GREETING}

I will be unable to attend [meeting, class or shift] on [day, date] because [brief reason].

I will catch up on anything I miss through [how]. Please let me know if anything needs doing in the meantime.

Kind regards,
[Your first name]"""),
    ("Question", "Question about [topic]", f"""{GREETING}

I have a question about [topic].

[Your question.]

So far I have [what you have tried or checked].

Thank you for your help.

Kind regards,
[Your first name]"""),
    ("Update to a group", "Update: [topic]", """Hello everyone,

A quick update on [topic].

What happened: [summary]
What happens next: [next step and date]
What you need to do: [action and deadline or nothing]

Reply to this email with any questions.

Best wishes,
[Your first name]"""),
]
