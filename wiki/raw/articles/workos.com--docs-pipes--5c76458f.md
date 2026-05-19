---
title: "Pipes - WorkOS Docs"
url: "https://workos.com/docs/pipes?utm_source=daringfireball&utm_medium=newsletter&utm_campaign=q22026"
fetched_at: 2026-05-19T07:01:16.452206+00:00
source: "daringfireball.net"
tags: [blog, raw]
---

# Pipes - WorkOS Docs

Source: https://workos.com/docs/pipes?utm_source=daringfireball&utm_medium=newsletter&utm_campaign=q22026

Enable your customers to connect their third-party accounts to your application.
Copy page
Pipes allows your users to securely connect their third-party accounts to your
application. With Pipes, you can easily integrate with popular services like
GitHub, Slack, Google, Salesforce, and many more without managing OAuth flows,
token refresh logic, or credential storage.
To make an provider available to your users, you will need to configure it in
the WorkOS Dashboard.
Visit the
Pipes
section of the WorkOS Dashboard to get started. Click
Connect
provider
then choose the provider from the list. If you don’t see the provider
you need, please reach out to
our team
.
Configure the provider with your own OAuth credentials:
Create an OAuth application
within the provider’s dashboard.
You can find instructions on setting up the provider in the documentation section of the setup modal.
Use the provided
redirect URI
when configuring the provider.
Set the
client ID and secret
from the provider.
Specify the required
scopes
for your application.
You may need to set these scopes in the provider configuration as well.
Provide an optional
description
. This will be used in the widget to inform users
on how your application will use their data from the provider.
Commonly used scopes are provided in-line, but you should consult each provider’s documentation for the full list of available scopes.
Provider management in your application
The
Pipes Widget
provides a pre-built UI for users to connect
and manage their connected accounts. The widget shows the user which
providers are available, and lets them easily initiate the authorization
flow. It communicates with the WorkOS API and stores the connection information
for the user. If there’s ever a problem with the user’s access token, the widget
will let them know they need to reauthorize.
The description in the widget is set in the provider’s configuration in the WorkOS Dashboard.
Once a user has connected a provider, you can
fetch access tokens
from your
backend to make API calls to the connected service on their behalf. Pipes takes
care of refreshing the token if needed, so you’ll always have a fresh token. If
there’s a problem with the token, the endpoint will return information about the issue so you can
direct the user to the correct it. This may require sending the user to re-authorize directly
or via the page with the Pipes widget.
Providers
Explore the third-party providers available for Pipes integrations
