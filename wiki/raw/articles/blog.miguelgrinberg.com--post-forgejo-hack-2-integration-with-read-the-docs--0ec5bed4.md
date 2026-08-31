---
title: "Forgejo hack #2: Integration with Read The Docs"
url: "https://blog.miguelgrinberg.com/post/forgejo-hack-2-integration-with-read-the-docs"
fetched_at: 2026-08-31T10:07:34.184860+00:00
source: "miguelgrinberg.com"
tags: [blog, raw]
---

# Forgejo hack #2: Integration with Read The Docs

Source: https://blog.miguelgrinberg.com/post/forgejo-hack-2-integration-with-read-the-docs

In this second Forgejo Hack installment I'll tell you how to connect a git repository that lives in your self-hosted Forgejo instance to
Read the Docs
, so that commits to the repository automatically trigger documentation builds, exactly like it works with GitHub.
What is Read the Docs?
I suspect this article isn't for you if you don't know the answer to this question, but just so that I don't leave anyone in the dark, Read The Docs is a great platform to host documentation for open source projects. I host the documentation for all my open source projects with them.
When working with GitHub, Read the Docs creates an integration for you that triggers rebuilds of the documentation every time a new commit is pushed to the repository. But Read the Docs does not currently offer similar support for repositories hosted on Forgejo, so the connection between the two platforms needs to be built manually. Keep reading to find out how.
The Read the Docs side
Okay, so now I'm going to show you how to build a manual integration that is similar in functionality to the GitHub one. To begin, log in to your
Read the Docs dashboard
. For the following steps, I'm going to assume that you already have your project in this dashboard, and that it has an active GitHub integration that needs to be migrated to Forgejo.
Click on the project you want to migrate. Then click on "Settings". Finally, select "Integrations" on the left sidebar. If you have an integration called "GitHub incoming webhook", then delete it by clicking the little trashcan icon to its right. This will effectively disconnect your GitHub repository, so that it does not trigger documentation builds anymore.
Next, click again on "Settings" and update the "Repository" section. Here you want to check "Use manually configured repository URL". Then enter the URL to your repository in the "Repository URL" field. Scroll all the way to the bottom and click "Save" to update your settings.
For the next step click again on "Settings" and then on "Integrations". Now you can click the "Add Integration" button to create the new integration. The only detail Read the Docs wants is the integration type. As I said above, at this time Forgejo is not a supported integration, so we are going to trick Read the Docs so that it thinks it is talking to GitHub. Go ahead and select "GitHub incoming webhook" as type, and click "Add Integration".
This will bring you to the integration settings page. Here you will see a big red warning, claiming that the git provider is unsupported. We already know that, so you can close the warning. Luckily Forgejo uses a webhook format that is similar to GitHub's, so everything works anyway.
This completes the Read the Docs side of the integration. Keep this page open, as you will need to grab the webhook URL and secret in a little bit.
The Forgejo side
Okay, now we have to do some work on the Forgejo side.
Open your Forgejo repository on your browser. Click on "Settings" and then on "Webhooks". Next, click on the "Add webhook" button, and select "Forgejo" from the dropdown.
Now copy the URL and the secret from the Read the Docs webhook page into the corresponding fields of the Forgejo webhook. Make sure that the "HTTP method" field is set to "POST", and that the "Trigger on" field is set to "Push events". Scroll to the bottom of the page and click on "Add webhook" to save.
And that is it! The next time you push to your repository the webhook will send a notification to Read the Docs to kick off a build of your documentation.
The GitHub side
This step isn't technically required, but if you want to leave things neat and clean, then pay one last visit to your old repository on GitHub. Click on "Settings" at the top, and then on "Webhooks" on the left. Look for the webhook that has a
readthedocs.org
URL and delete it, since this webhook has been invalidated when you deleted it on the Read the Docs side.
Conclusion
I hope this has been useful. Please let me know what you think of this solution, and if you have a better one!
Thank you for visiting my blog! If you enjoyed this article, please consider supporting my work and keeping me caffeinated with a small one-time donation through
Buy me a coffee
. Thanks!
