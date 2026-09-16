---
title: "The developer’s guide to SSO"
url: "https://workos.com/guide/the-developers-guide-to-sso?utm_source=daringfireball&utm_medium=newsletter&utm_campaign=q32026"
fetched_at: 2026-09-16T10:01:34.172697+00:00
source: "daringfireball.net"
tags: [blog, raw]
---

# The developer’s guide to SSO

Source: https://workos.com/guide/the-developers-guide-to-sso?utm_source=daringfireball&utm_medium=newsletter&utm_campaign=q32026

If you want more people using your product, the easiest place to start is making it easier to actually sign up. Adding SSO to your app will help you land those larger enterprise deals and remove the signup friction that keeps causing your visitors to drop off. For modern developers though, the world of XML, SOAP, and OASIS standards can be opaque.
Our guide will walk you through SSO: what it is, why it’s important, and best practices for setting it up and integrating it with your app.
The basics: what SSO is and why you should care
The easiest way to understand SSO quickly is to think about your app’s authentication as a service. Most developers build the service themselves: you take care of creating usernames and passwords, add them into a database, and check credentials every time someone logs in. But in the same way that you skip building payments infrastructure and use Stripe, you can “outsource” your auth and have someone else do it; and that’s what SSO is.
If you’ve heard of SSO before, you’re probably thinking of it as a security feature and that’s true, but where it really shines is through
increased engagement
. Making it easier to sign up and sign-in to your product lowers friction for users, increases retention through smoother login flows, and helps you land those elusive enterprise deals (many enterprises can’t work with vendors who don’t support SSO).
Apps with SSO enabled allow users to authenticate through someone else’s service. Instead of managing usernames and passwords, you integrate with a provider like Okta or OneLogin that does it for you. Those services, called Identity Providers (IdPs), are generally more full-featured and secure than what your typical growing startup would be able to build themselves.
SSO is a given among everyone from high growth startups to more traditional enterprises. Here’s Vercel's login page: they support SSO with Okta, Google, OneLogin, and more.
Slack, Asana, Notion, Loom, and Webflow all support SSO too. It’s pretty much part of the standard growth playbook.
Learning the lingo: SAML, SPs, IdPs, and assorted acronyms
Let’s get a little deeper into how SSO works. One thing worth noting: SAML isn’t the only protocol you can use to implement SSO.
OAuth (1.0 and 2.0)
are also popular, as well as WS-Fed and
OpenID Connect (OIDC)
. The broad concepts can carry over across protocols, too.
If you’re integrating SSO into your app, you’re a service provider (SP). Your app is the service. The provider that you’re “outsourcing” identity to, like Okta or OneLogin, is called the identity provider (IdP). Where things start to get complex is when your app needs to communicate with IdPs to actually authenticate your users. SSO works with a communication protocol called SAML (Security Assertion Markup Language) that governs these phone lines.
Let’s walk through a typical SAML flow, starting with a user trying to sign in through your site.
When a user navigates to your login page, they’ll either enter their email or click a button that takes them to an IdP portal like Okta. Your app issues a SAML request (and a browser redirect) to the IdP. It’s basically saying, “Hey, this user wants to sign in, do me a favor and verify that I should let them in.”
At the IdP, the user will enter their full credentials, and deal with more extensive security measures like 2FA. Once they’ve successfully authenticated with the IdP, the IdP sends your app a response containing an assertion: this user is good to go, and you can let them in. We call this assertion a SAML authorization response.
The app receives the response from the IdP, checks it, and sends an one-time auth code.
The app receives the user profile. The user is now able to access the application without needing to log in again. The user's session is managed by the service provider, which maintains the authentication state and ensures the user remains logged in as long as the session is valid.
SAML works through
assertions
. These are recorded and transferred as XML documents (for all those SOAP fans out there. Nobody? Ok).
Here’s an example of what a response containing an assertion might look like (thanks to
OneLogin
):
<samlp:Response xmlns:samlp="urn:oasis:names:tc:SAML:2.0:protocol" xmlns:saml="urn:oasis:names:tc:SAML:2.0:assertion" ID="_8e8dc5f69a98cc4c1ff3427e5ce34606fd672f91e6" Version="2.0" IssueInstant="2014-07-17T01:01:48Z" Destination="http://sp.example.com/demo1/index.php?acs" InResponseTo="ONELOGIN_4fee3b046395c4e751011e97f8900b5273d56685">
  <saml:Issuer>http://idp.example.com/metadata.php</saml:Issuer>
  <samlp:Status>
    <samlp:StatusCode Value="urn:oasis:names:tc:SAML:2.0:status:Success"/>
  </samlp:Status>
<saml:Assertion xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xmlns:xs="http://www.w3.org/2001/XMLSchema" ID="pfxa099680e-6fc0-2c7a-90fa-4202bb29faa4" Version="2.0" IssueInstant="2014-07-17T01:01:48Z">
  <saml:Issuer>http://idp.example.com/metadata.php</saml:Issuer><ds:Signature xmlns:ds="http://www.w3.org/2000/09/xmldsig#">
  <ds:SignedInfo><ds:CanonicalizationMethod Algorithm="http://www.w3.org/2001/10/xml-exc-c14n#"/>
    <ds:SignatureMethod Algorithm="http://www.w3.org/2000/09/xmldsig#rsa-sha1"/>
  <ds:Reference URI="#pfxa099680e-6fc0-2c7a-90fa-4202bb29faa4"><ds:Transforms><ds:Transform Algorithm="http://www.w3.org/2000/09/xmldsig#enveloped-signature"/><ds:Transform Algorithm="http://www.w3.org/2001/10/xml-exc-c14n#"/></ds:Transforms><ds:DigestMethod Algorithm="http://www.w3.org/2000/09/xmldsig#sha1"/><ds:DigestValue>YOCfzMPwhVQibcTRRyuCb5vlTDU=</ds:DigestValue></ds:Reference></ds:SignedInfo><ds:SignatureValue>VXQGwtQsc/rTuCFspZwD6k4i6fKr4ymYfCiI5Ve9JO5LYRG7VNPzIq5Mr/JW/0btpui4cmQVK//wA89nLe+g2wxDizx32CnOBsshoF3YTDOs586SJt+Ty/h/X886Xhqu8XsdMiD/spyU8rGhIQP2OL65k6HoSFxtPqKt1+KOdkE=</ds:SignatureValue>
<ds:KeyInfo><ds:X509Data><ds:X509Certificate>MIICajCCAdOgAwIBAgIBADANBgkqhkiG9w0BAQ0FADBSMQswCQYDVQQGEwJ1czETMBEGA1UECAwKQ2FsaWZvcm5pYTEVMBMGA1UECgwMT25lbG9naW4gSW5jMRcwFQYDVQQDDA5zcC5leGFtcGxlLmNvbTAeFw0xNDA3MTcxNDEyNTZaFw0xNTA3MTcxNDEyNTZaMFIxCzAJBgNVBAYTAnVzMRMwEQYDVQQIDApDYWxpZm9ybmlhMRUwEwYDVQQKDAxPbmVsb2dpbiBJbmMxFzAVBgNVBAMMDnNwLmV4YW1wbGUuY29tMIGfMA0GCSqGSIb3DQEBAQUAA4GNADCBiQKBgQDZx+ON4IUoIWxgukTb1tOiX3bMYzYQiwWPUNMp+Fq82xoNogso2bykZG0yiJm5o8zv/sd6pGouayMgkx/2FSOdc36T0jGbCHuRSbtia0PEzNIRtmViMrt3AeoWBidRXmZsxCNLwgIV6dn2WpuE5Az0bHgpZnQxTKFek0BMKU/d8wIDAQABo1AwTjAdBgNVHQ4EFgQUGHxYqZYyX7cTxKVODVgZwSTdCnwwHwYDVR0jBBgwFoAUGHxYqZYyX7cTxKVODVgZwSTdCnwwDAYDVR0TBAUwAwEB/zANBgkqhkiG9w0BAQ0FAAOBgQByFOl+hMFICbd3DJfnp2Rgd/dqttsZG/tyhILWvErbio/DEe98mXpowhTkC04ENprOyXi7ZbUqiicF89uAGyt1oqgTUCD1VsLahqIcmrzgumNyTwLGWo17WDAa1/usDhetWAMhgzF/Cnf5ek0nK00m0YZGyc4LzgD0CROMASTWNg==</ds:X509Certificate></ds:X509Data></ds:KeyInfo></ds:Signature>
    <saml:Subject>
      <saml:NameID SPNameQualifier="http://sp.example.com/demo1/metadata.php" Format="urn:oasis:names:tc:SAML:2.0:nameid-format:transient">_ce3d2948b4cf20146dee0a0b3dd6f69b6cf86f62d7</saml:NameID>
      <saml:SubjectConfirmation Method="urn:oasis:names:tc:SAML:2.0:cm:bearer">
        <saml:SubjectConfirmationData NotOnOrAfter="2024-01-18T06:21:48Z" Recipient="http://sp.example.com/demo1/index.php?acs" InResponseTo="ONELOGIN_4fee3b046395c4e751011e97f8900b5273d56685"/>
      </saml:SubjectConfirmation>
    </saml:Subject>
    <saml:Conditions NotBefore="2014-07-17T01:01:18Z" NotOnOrAfter="2024-01-18T06:21:48Z">
      <saml:AudienceRestriction>
        <saml:Audience>http://sp.example.com/demo1/metadata.php</saml:Audience>
      </saml:AudienceRestriction>
    </saml:Conditions>
    <saml:AuthnStatement AuthnInstant="2014-07-17T01:01:48Z" SessionNotOnOrAfter="2024-07-17T09:01:48Z" SessionIndex="_be9967abd904ddcae3c0eb4189adbe3f71e327cf93">
      <saml:AuthnContext>
        <saml:AuthnContextClassRef>urn:oasis:names:tc:SAML:2.0:ac:classes:Password</saml:AuthnContextClassRef>
      </saml:AuthnContext>
    </saml:AuthnStatement>
    <saml:AttributeStatement>
      <saml:Attribute Name="uid" NameFormat="urn:oasis:names:tc:SAML:2.0:attrname-format:basic">
        <saml:AttributeValue xsi:type="xs:string">test</saml:AttributeValue>
      </saml:Attribute>
      <saml:Attribute Name="mail" NameFormat="urn:oasis:names:tc:SAML:2.0:attrname-format:basic">
        <saml:AttributeValue xsi:type="xs:string">test@example.com</saml:AttributeValue>
      </saml:Attribute>
      <saml:Attribute Name="eduPersonAffiliation" NameFormat="urn:oasis:names:tc:SAML:2.0:attrname-format:basic">
        <saml:AttributeValue xsi:type="xs:string">users</saml:AttributeValue>
        <saml:AttributeValue xsi:type="xs:string">examplerole1</saml:AttributeValue>
      </saml:Attribute>
    </saml:AttributeStatement>
  </saml:Assertion>
</samlp:Response>
The flow we just outlined is called
​
SP-initiated​
, because it started at ​your​ app, and you’re the service provider.
There’s another way this can go down though: users can ​start​ at their IdP (like the Okta app directory), click on which app they want to sign into, and then authenticate and redirect. That’s called ​
IDP-initiated​
.
Getting practical: how to add SSO to your app
Like pretty much anything in software, there are two ways to add SSO to your app: you can build it yourself or pay someone else to do it for you.
Option 1: b
uilding SSO from scratch
Building SSO yourself is all about handling and working with the protocol you choose, assuming you’re targeting larger companies, we’re talking about SAML here. This isn’t a technical tutorial, but here are a few high-level components you’ll need to write:
A SAML controller for handling requests and providing responses to your integrated IdPs.
A SAML service to verify x509 certs, entity IDs, and IdP URLs, alongside parsing SAML assertions and creating and validating SAML responses. You’ll particularly enjoy the XML parsing and IdP-specific request formats.
A strategy to correctly authenticate users in your app based on the attributes that IdPs send back (you’ll need to normalize these if you’re supporting multiple customers).
If any of this sounds weirdly unfamiliar to you, that’s because it probably is: there’s a lot of upfront research required to understand the right way to do it. It’s not as simple as adding a new frontend library and skimming through the docs.
Part of the challenge of building SSO from scratch is customization: you’ll need to build SAML flows for each IdP independently. SAML is a standard and like any good standard it’s often fractured and can sometimes be a pain to work with.
Over the past few years, the web dev ecosystem has developed a few packages that take care of some of the repeatable work. Middleware like
​passport.js
​
can help you avoid building everything from scratch; or if your backend is in Python, OneLogin offers a
python-saml​
package.
Option 2: use an SSO provider
If you don’t want to build SSO yourself (I mean, why would you?), there are a bunch of great third-party services that offer SDKs and packages to make integration as easy as a few lines of code. Some of the available providers are WorkOS,
‍
Auth0, AWS Cognito, and GCP Identity Platform.
Best practices from some engineers who have done it before
Here are a few tips that might make your SSO integration process just a bit easier, whether you’re using a third-party provider or building it from scratch.
Security
‍
Disallow username and password logins, password resets, and email address changes:
If an organization is using SSO with your product, give admins the ability to disable username/password based auth for their users. It creates a more seamless SSO experience by avoiding false login starts and keeps things secure.
‍
Enforce session timeouts
: Expire idle user sessions to make sure users aren't signed in indefinitely — it's good practice to grab the SAML response's session timeout value and use that, but there are cases where having a "time to live" setting for each account is useful too.
‍
Force sign-in for active browser sessions
: If your app gets a new sign-in request, replace any currently active browser sessions with the newly authenticated session. This is particularly important for apps that lean toward multi-tab use, like IDEs or CRMs.
Routing
‍
Ask users for the information to determine the right IDP
: If you plan on supporting multiple IDPs in your SSO implementation, ask users for their email address, account subdomain, or unique account URL to determine the correct identity provider for their login.
‍
Make sure to deep link
: If you’re asking users to authenticate from an existing product page or they’re expecting to land somewhere in particular in your product, you’ll want to implement deep linking in your SAML flows. You can use ​SAML’s RelayState parameter​ to get this working.
UX
‍
Replace one-off email verification with
domain verification
: If your app sends verification emails on username/password signups, it may be more effective to switch to domain verification. Essentially, when domain verification is employed, users logging in with email addresses from a verified domain do not require separate email verification. This approach is particularly useful if the user's email is associated with an IDP from a verified domain. Domain verification is crucial for establishing security and trust between service providers and organizations, ensuring that only authorized users can make changes to an organization's settings in the service provider.
‍
Use
Just-In-Time (JIT) User Provisioning
for first time sign-ins
: JIT user provisioning
​
automates the account creation process for users signing in to your app for the first time via SAML. If they exist in their organization’s IDP, you’ll just create their account automatically instead of asking them to sign up from scratch. This lowers friction for new users ​significantly​ and helps make your app more attractive to larger organizations.
‍
Prompt users for IDP logouts
: When users log out of your app, prompt them to see if they’d like to log out of their IDP as well. The two intents often overlap, and you can save your users some time.
