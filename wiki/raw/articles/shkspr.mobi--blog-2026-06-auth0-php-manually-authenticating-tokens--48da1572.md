---
title: "Auth0 PHP - manually authenticating JWT idTokens"
url: "https://shkspr.mobi/blog/2026/06/auth0-php-manually-authenticating-tokens/"
fetched_at: 2026-06-25T07:01:40.759430+00:00
source: "shkspr.mobi"
tags: [blog, raw]
---

# Auth0 PHP - manually authenticating JWT idTokens

Source: https://shkspr.mobi/blog/2026/06/auth0-php-manually-authenticating-tokens/

I find it baffling just how poorly documented most big projects are. Auth0 by Okta has a fair bit of cash, lots of customers, and almost completely absent documentation.
Here's how to successfully authenticate a JWT supplied by Auth0.
Once your user has authenticated with Auth0, they will be given an
accessToken
and an
idToken
. Only the
idToken
is needed for our purposes.
It will look something like this:
eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6ImFiYzEyMyJ9.eyJnaXZlbl9uYW1lIjoiSm8iLCJmYW1pbHlfbmFtZSI6IlRlc3QiLCJuaWNrbmFtZSI6IkpvVGVzdCIsIm5hbWUiOiJKbyBMZSBUZXN0IiwicGljdHVyZSI6Imh0dHBzOi8vZXhhbXBsZS5jb20vam8ucG5nIiwidXBkYXRlZF9hdCI6IjIwMjYtMDQtMjhUMTM6NTk6NTUuNjcxWiIsImVtYWlsX3ZlcmlmaWVkIjp0cnVlLCJpc3MiOiJodHRwczovL2V4YW1wbGUuZXUuYXV0aDAuY29tLyIsImF1ZCI6ImFiYzEyMyIsInN1YiI6ImZhY2Vib29rfDEyMzQ1NiIsImlhdCI6MTc3NzM4NDc5NiwiZXhwIjoxNzc3NDIwNzk2LCJzaWQiOiJhYmMxMjMtNDU2LWRlZmdoaWprIiwibm9uY2UiOiIxMjM0NTY3ODkwIn0.ZgnZxOOtfczLewlm_agK6mJMYetVTZrHlBlu5qzXbADlhvZB8RraVuFKmFutLZLibMQxz_RY0oh4hRufVWDHJ0kuocW38kRHztDg7R5KOfvJEM46WW49xvhLhKprzkx9WXDDlpCRNL0QbBK2U0F1VjmRpTp1Q5cHEd8PBsa4rGAhfqudXp5JrC2Lm5e7ji0AQ_s7HJhy59b9mTb3tMqHGsrWDZS915zHPYEQtSvg5o9sSx1tCRfsyL6kdsdkaTffQjJDUrT5hpIQ-2_9tGuqioJjP4c0edQ85TaK9UnSxfzMQ8gYez963kbo_Iv1fJyaTVwXR-AVvwK-CeGJAFrheQ
Yeuch! If you stick it into
JWT.io
you'll see that it is Base64 encoded JSON containing a header, body, and signature. Each part is separated by a
.
character.
You could manually decode it, but that's a bit of a pain in the arse. So here's how to do it with
the Auth0 PHP library
. I'm
using the Symfony one
, but it should all be fairly similar.
First, import the library:
⧉
PHP
use
Auth0\SDK\Auth0
;
Next, you'll need to send the token to the PHP. You can do this in a header, GET, or similar:
⧉
PHP
$authHeader
=
$request
->
headers
->
get
(
"Auth0-Authorization"
);
Then, set up Auth0 so that it can parse and validate the token:
⧉
PHP
try
{
$token
=
$authHeader
;
$auth0
=
new
Auth0
([
"domain"
=>
$_ENV
[
"AUTH0_DOMAIN"
],
"clientId"
=>
$_ENV
[
"AUTH0_CLIENT_ID"
],
"clientSecret"
=>
$_ENV
[
"AUTH0_CLIENT_SECRET"
],
"cookieSecret"
=>
"_"
//  Dummy value.
]);
$decoded
=
$auth0
->
decode
(
token
:
$token
,
tokenType
:
\Auth0\SDK\Token
::
TYPE_ID_TOKEN
,
    );
}
catch
(\Exception
$e
) {
error_log
(
"Auth0 Error - {$e}"
);
}
The
cookieSecret
must
be set - even though you aren't using cookies. Any non-null value is fine.
The
tokenType
must also be set correctly.
Assuming you all goes well, you will have a
decoded
object which has validated against Auth0. So how do you get the user's details from it?
Well, you
could
split the original
idToken
at the period character and Base64 decode the middle one. Try it now to see what it contains! Or
print_r()
the decoded token to see it in all its cryptographic glory.
The easiest way is to do:
⧉
PHP
$claims
=
$decoded
->
toArray
();
Then you can access various properties by doing:
⧉
PHP
$username
=
$claims
[
"nickname"
];
$identifier
=
$claims
[
"sub"
];
Perhaps there is a more official way - but I couldn't find anything in the documentation. Hurrah for reading source code!
