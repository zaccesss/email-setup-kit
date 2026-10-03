# Gotchas

Problems that are easy to hit and slow to diagnose.

| Symptom | Cause | Fix |
| --- | --- | --- |
| A signature logo shows as broken in Gmail but loads fine in a browser | Google fetches signature images through its own proxy. Bot protection on the image host blocks that proxy | Host the image somewhere without bot protection, such as GitHub's raw file host. Uploading it into the signature also works |
| Labels disappear after deleting an old one | Deleting a Gmail label also deletes the labels nested under it. Names ignore case too | Create the new parent labels first, then remove the old ones |
| A re-added domain will not verify | It was removed only moments ago and Google has not released it | Wait a few minutes and try again |
| DKIM fails after adding a new key | Two `google._domainkey` records exist | Edit the existing record instead of adding another |
| DMARC reports for one domain never arrive at another | The receiving domain has not agreed to accept them | Add `*._report._dmarc` with `v=DMARC1` on the receiving domain |
| A website contact form's mail goes to spam | The form sends as your domain through a server that is not in SPF and does not sign with DKIM | Send through an authorised provider. Sending from the provider's own domain with your address as reply-to also works |
| Filters label mail twice | Old and new filters are both running | Delete the old filters before importing new ones |
| Rules do nothing to existing mail | Outlook rules only act on new mail | Use Run rule |
