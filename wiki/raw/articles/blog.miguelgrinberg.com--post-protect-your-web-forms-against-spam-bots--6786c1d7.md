---
title: "Protect Your Web Forms Against Spam Bots"
url: "https://blog.miguelgrinberg.com/post/protect-your-web-forms-against-spam-bots"
fetched_at: 2026-11-28T10:00:45.893120+00:00
source: "miguelgrinberg.com"
tags: [blog, raw]
---

# Protect Your Web Forms Against Spam Bots

Source: https://blog.miguelgrinberg.com/post/protect-your-web-forms-against-spam-bots

The comments form that appears at the bottom of every article in this blog is under constant abuse by spam bots. I added a
CAPTCHA
to it a few years ago and at the time it seemed to help some, but spammers have now figured out how to bypass them. As a result, my comments inbox has been getting out of control lately.
In this article I'm going to share a solution that I built to help me reduce spam on this blog from 30-40 messages per day to just about 2-3 per month. It is based on the "
proof of work
" concept, and unlike CAPTCHAs, it does not rely on third-party services. It is also better for users, because it does not require them to solve silly puzzles or even know that they are being verified. I have implemented the solution in Python and Flask, because that is what this blog runs on, but once you understand how it works you should have no trouble porting it to other languages or frameworks.
Introduction to proof-of-work solutions
Proof-of-work schemes were devised in the 1990s as a way to fight email spam. They were later used (abused is probably a better word) by Bitcoin as a core part of its mining process. In the present they have made a comeback as an effective method to deter bots, and are used by mainstream projects such as Cloudflare Turnstile and Anubis.
The concept is somewhat similar to CAPTCHAs, in that the server gives the client a
challenge
to solve. But these problems are solved through code, so the user is not actively involved.
The interesting property of proof-of-work challenges is that solving them is much more computationally intensive than verifying them. The server can send a challenge that will take the client a second or two of computation to solve, but once the client sends the solution back the server can verify it with very little effort. This works nicely for form submissions, where the server can attach a JavaScript proof-of-work challenge solver to the submit event of a form, resulting in the solution being submitted as an additional hidden field with the form data. Then on the server this hidden field is validated before the form is processed.
Solving a proof-of-work challenge during a form submission just adds a small delay after the user clicks the submit button, so it is barely noticeable. But this throws spammers a curveball, because most of them do not even use web browsers to submit spam at scale. A spammer will be less interested in sending to you if you force them to use a real browser with JavaScript enabled, and even less if they are going to have to waste precious time running useless calculations as a requirement to getting their spam accepted.
An example
You are probably wondering what is this mysterious "work" that the client needs to do to be accepted by the server.
The typical task in these schemes involves finding a string that when hashed with a cryptographic function returns a hash that has certain properties, such as having some of its bits set to predetermined values. Let's look at a concrete example that will make this more clear.
A possible proof-of-work challenge would be to ask the client to find a string that starts with a given prefix, let's say
"abcde"
, that when hashed with the SHA-512 function returns a hash that in hexadecimal starts with the digit
0
, which is equal to saying that the first four bits of the hash have to be zero. To solve this challenge the client can try to hash
"abcde1"
,
"abcde2"
and keep going like that until it finds a string that has a hash that starts with the required
0
.
How much work is this? Let's try some hashes by hand in Python and see if we can find a solution to this challenge:
>>> from hashlib import sha512
>>> sha512(b'abcde1').hexdigest()
'97b0befcc466c532a0358720f9a0175efbf6c5fcdf158ac0cbdc391bbe1114e2062d086676252c696fe0b03be7bd4264333ef4dc9c1097770df04bc163504425'
>>> sha512(b'abcde2').hexdigest()
'53688a316d4c852717a231e3d2e90b9f1d6e53018bea4120ec6b03b4c4689391685cd053c9731b7a95de910932cca3314c48977fafc3175e81bb7f045252ef06'
...
>>> sha512(b'abcde12').hexdigest()
'0ec5048e9afafa5cd2ceb272d47f05caaa239ab6bac6e475683642b5d9cdda3aca389a88dadaa5d5b1636e111998232950bf2bf0e1ad01ed31eba5c54928139c'
For this challenge, we had to do 12 attempts, because the string
"abcde12"
has a hex hash that starts with a
0
. So one valid solution to this challenge is the suffix
12
.
You may argue that hashing 12 strings isn't really that much computation, and you would be correct, since most computers or even phones can do that much work really quickly. But we can make the challenge harder by increasing the number of zeros we require on the hash. Let's call the above a "level 1" challenge. A "level 2" challenge would require that the hash starts with two hex zeros, or 8 zero bits, which is much more unlikely, so on average clients will need to work more to find a solution. And of course levels 3, 4 and higher are also on the table.
The idea is to fine tune the complexity of the challenge so that it is a bit hard to find a solution, but not too hard, since this is meant to slow down spammers and bots without causing a significant impact to legitimate users.
JavaScript implementation
For the form submission use case we want the challenge to be solved in the browser, so we need a JavaScript version of the work I did in the previous section to find solutions to challenges. Here is my attempt:
async function sha512(message) {
  const encoder = new TextEncoder();
  const data = encoder.encode(message);
  const hash = await window.crypto.subtle.digest("SHA-512", data);
  return new Uint8Array(hash).toHex();
}

async function solve(challenge, level) {
  let hash;
  let solution = 0;
  do {
    hash = await sha512(challenge + ++solution);
  } while(hash.substr(0, level) !== "0".repeat(level));
  return solution;
}
The
sha512()
function is a helper function that wraps all the logic calls to hash a string using the
SubtleCrypto
API, which is available in all modern browsers.
The
solve()
function does what I did manually in the Python prompt, which is to append an auto-incrementing number to the challenge string and calculating its hash until we find one that starts with a
level
number of hex zero digits.
Do you want to give this code a try? You can do it in your browser's developer console. Copy and paste the above code (both functions) to your console, and then run the solver for the example challenge from the previous section:
>> await solve('abcde', 1);
12
>> await solve('abcde', 2);
212
>> await solve('abcde', 3);
10932
>> await solve('abcde', 4);
264673
Here you can see how increasing the level of the challenge results in a lot more work for the
solve()
function. On my machine, the level 4 challenge took about 2 seconds to return the solution. But verifying this solution can be done in negligible time regardless of how high the level is set, with just one hashing operation and one string comparison. All we need to do is calculate the SHA-512 hash of the prefix and the solution combined and verify that it starts with the correct number of zeros. For now let's just confirm that the level 4 solution is correct in the Python prompt:
>>> from hashlib import sha512
>>> sha512(b'abcde264673').hexdigest().startswith('0000')
True
>>> sha512(b'abcde264673').hexdigest()
'000071d5bf6881002552b8988d22d17bc350b3ed1f51af4c897941aa43531ecb928b4dfe588b90db11cc979b7da1ccb8db730d1ed8f9958b0d8f20f1e5208725'
One interesting improvement that could be made to the JavaScript solver is to put it inside a
web worker
. This would be useful if you decide to use a level high enough that requires the solver to work for a long time, because the solver blocking the main thread could make the page appear unresponsive. I have decided not to worry about it for now because I plan to keep the challenges relatively short, but this is something you should consider if your use case requires challenges that take longer to solve.
Python implementation
We can now start to think about how to integrate proof-of-work challenges into a Python back end application. To begin, let's put all the logic that deals with these challenges in a class:
import hashlib

class ProofOfWork:
    def __init__(self, level):
        self.level = level

    def validate_solution(self, challenge, solution):
        return hashlib.sha512(
            (challenge + solution).encode()
        ).hexdigest().startswith('0' * self.level)

    @staticmethod
    def get_js_solver():
        return '''
            async function sha512(message) {
              const encoder = new TextEncoder();
              const data = encoder.encode(message);
              const hash = await window.crypto.subtle.digest("SHA-512", data);
              return new Uint8Array(hash).toHex();
            }
            async function solve(challenge, level) {
              let hash;
              let solution = 0;
              do {
                hash = await sha512(challenge + ++solution);
              } while(hash.substr(0, level) !== "0".repeat(level));
              return solution;
            }
        '''
An instance of the
ProofOfWork
class stores the
level
attribute that we want to use for the challenges. Given a challenge and its solution, the
validate_solution()
method checks if the solution is correct or not. Finally, we are going to need to embed the JavaScript code that solves these challenges into an HTML template, so I've added the
get_js_solver()
method to return this code as a string. Note that I have not written a solver in Python, because the solving effort is always going to happen in the browser.
Assuming the code above is in a file named
pow.py
, here is how to use it directly from the Python prompt to verify the level 4 solution we saw above:
>>> from pow import ProofOfWork
>>> pow = ProofOfWork(4)
>>> pow.validate_solution('abcde', '264673')
True
>>> pow.validate_solution('abcde', '264672')
False
Flask integration
As I'm sure many of my readers know, on my Flask applications I use the
Flask-WTF
extension to handle form processing. So the next step is to wrap the code I shared above in a custom
WTForms
field that can be easily added to a Flask-WTF form. This is actually where the meat of this solution lives, so I'll go slowly to make sure everything is clear, especially for those who just want to learn the technique and are less interested in the Python and/or Flask bits.
Design
Before I show you the code to integrate proof-of-work challenges with a Flask application let me share how I designed this solution to work, as this is going to be helpful when you try to understand and adapt this solution to match your own needs.
The form will include a hidden field that is dedicated to the proof-of-work challenge. The JavaScript solver functions will be added to the page as well, along with a custom submit event for the form. The chosen level for the change will be rendered to the page so that it is known to the solver when it runs.
The user will open or navigate to the page with the form, and eventually they'll hit the form's submit button. Our custom submit handler will prevent the form from being submitted right away. Instead, the handler will send a quick request to the server to ask for a challenge to solve. The server will generate a new challenge using a random number generator and return it. The server needs to "remember" this challenge so that it can verify the solution later on, so it will store a copy of it in the user session.
Once the client receives the challenge, it will launch the JavaScript solver with it, and when the solution is found it will set it as the value of the hidden field. Then it will allow the normal form submission process to resume, so the form will be sent to the server, with the solution to the challenge stored in the hidden field. To complete the process the server will retrieve the challenge from the user session and verify that the value of the hidden form field is a valid solution to it.
Security considerations
Covering the security aspects of the solution is extremely important, now that we live in a world of constant vulnerabilities being exposed. It is generally a good idea to put as many restrictions as possible, to prevent loopholes that may allow a bot to bypass or hack our challenge verification.
The attack vector for this solution is a client that can somehow choose a known in advance challenge for which they have a pre-calculated solution. I could think of two variations on this potential attack: either the client finds a way to override the challenge chosen by the server with their own, or they reuse a legitimate server-generated challenge multiple times, which means they would need to calculate a solution only once.
To prevent the client from overriding the challenge that the server assigns, we are storing the chosen challenge in the user session. I intend to implement this solution for Flask, which by default stores user sessions in a client-side cookie. The session cookie is protected with a cryptographic signature, so the client will not be able to rewrite its contents. For systems that use server-side storage for user sessions, the chosen challenge is also secure.
The second type of attack is more tricky to defend against when user sessions are stored in a cookie, because the user can take a session cookie that includes a valid challenge, calculate a solution for it, and then ignore any new session cookies that the server sends with new challenges and instead keep submitting the same session cookie and the same solution. This is called a
replay attack
, and to prevent it we will give each challenge a short period of validity after which the server will not accept it anymore. We can store the challenge expiration time also in the session, since the client will not be able to change it.
Another option that can prevent replay attacks that can be used alone or as a complement to the expiration time is to store challenges that were successfully used in a database that can be searched to ensure that a repeat challenge is refused.
That is really all the potential threats I could come up with, but please do let me know if you find other ways in which my solution can be insecure!
Challenge generator
As discussed in the design I provided above, we need an endpoint that will return challenges to clients. This would be what we use instead of the
"abcde"
from the manual examples I shared above.
Here is a simple Flask endpoint that does this job nicely:
from secrets import token_hex
from time import time
from flask import session

@app.route('/_challenge')
def _challenge():
    session['_ch'] = token_hex()
    session['_chexp'] = time() + 15
    return {'challenge': session['_ch']}
This uses the
token_hex()
function of the
secrets
package of the Python standard library to generate a random token of a reasonable length. To be able to recall this token we are storing it in the user session under the
_ch
key. And to make sure that this token is only used for a short period of time after it is generated, we add a
_chexp
key with the timestamp of the expiration time, which in this example I set at 15 seconds from the time of generation, which should give the client enough time to run the solver for 1-2 seconds and then submit the solution.
Custom field
Now let's write the custom proof-of-work field for Flask forms. A custom WTForms field is defined with three classes: a field, a widget and a validator. The field class is used to instantiate the field in the form definition. The widget and the validator are auxiliary classes that the field uses to render the HTML for the field and to check that the value submitted by the user is valid respectively.
Here is the validator class for the field:
from time import time
from wtforms.validators import ValidationError
from flask import session

class ProofOfWorkValidator:
    def __init__(self, message='Verification failed'):
        self.message = message

    def __call__(self, form, field):
        if time() <= session.pop('_chexp', 0):
            pow = ProofOfWork(field.level)
            challenge = session.pop('_ch', '')
            if field.data and pow.validate_solution(challenge, field.data):
                return True
        raise ValidationError(self.message)
The validator retrieves information that was stored in the session ahead of time in the challenge endpoint from the previous section. If first ensures that the timestamp stored under the
_chexp
key in the session is in the future, because if it is in the past it means that this challenge has expired and cannot be used anymore.
To perform the actual validation the class creates an instance of the
ProofOfWork
class I shared above, and sets the level, which is an attribute of the WTForms custom field. The challenge is retrieved from the session's
_ch
key, and the solution comes from the
data
attribute of the field, which is where WTForms stores the value that was submitted by the client. The
validate_solution()
method of the
ProofOfWork
class does the verification.
If the checks done by the validator are successful, then
True
is returned and that will allow the form to be accepted. In case of a failed check a
ValidationError
is raised to halt the form processing.
Next let's look at the widget part of this custom field:
from wtforms.widgets import html_params
from markupsafe import Markup

class ProofOfWorkWidget:
    def __call__(self, field, error=None, **kwargs):
        kwargs.setdefault('id', field.id)
        kwargs.setdefault('name', field.name)
        attributes = html_params(**kwargs)
        return Markup(f'''
            <input {attributes} type="hidden" value="">
            <script>
              {ProofOfWork.get_js_solver()}
              document.addEventListener('DOMContentLoaded', () => {{
                const field = document.getElementById('{field.name}');
                const form = field.form;
                form.addEventListener('submit', async (e) => {{
                  e.preventDefault();
                  e.submitter.disabled = true;
                  const response = await fetch('/_challenge');
                  if (response.ok) {{
                    const challenge = (await response.json())['challenge'];
                    field.value = await solve(challenge, {field.level});
                  }}
                  HTMLFormElement.prototype.submit.call(form);
                }});
              }});
            </script>
            ''')
The widget is in charge of rendering the field to the HTML page. There is a lot going on here, with a significant portion of the action being in JavaScript and HTML code that will be sent to the client.
The return value of the
__call__
method is the code that will be inserted in the HTML page for this field. This is an instance of the
Markup
class, which marks the text given to it as safe, which is necessary to bypass the default escaping. To generate the code for this field I'm using an f-string, which is very useful as a simple template language, even though it has the drawback that all the
{
s and
}
s used in the JavaScript code have to be doubled so that they are not interpreted as an f-string replacement section.
The first line in the f-string renders the field as a hidden field. The
attributes
variable contains all the HTML attributes that belong to this field, including the
id
and
name
which are added even if they were not provided by the caller.
The rest of the code generated for this field is in a
<script>
block. First, the JavaScript solver code that we have in the
ProofOfWork
class is added. After that a handler for the
DOMContentLoaded
is defined. This is the modern way to attach logic to run after the page loads, equivalent to the
$(document).ready(...)
that you may have used back when jQuery ruled the world.
The
DOMContentLoaded
event handler retrieves the DOM field element, and then from it it gets the DOM form element, to which it attaches a
submit
event that will trigger when the form's submit button is clicked. The name of the field is generated in the f-string, since this name is known when the form is rendered on the Python side.
The submit event for the form starts by calling
preventDefault()
to halt the form submission. This is because the solution to the challenge needs to be calculated and included in this submission. Next the submit button for the form is disabled, to prevent the user from clicking it again and launching multiple submissions in parallel. After that comes the core of the proof-of-work flow, which starts by sending an asynchronous request to the challenge endpoint, which I called
/_challenge
above. This is done with the
fetch()
function, which is available in all browsers.
When the challenge is received, the JavaScript solver is called. Note how the level that is required for this challenge is inserted in the Python f-string, so it will appear hardcoded when you look at the source code for the page in the browser. The solution returned by the solver is added to the hidden field's
value
attribute.
Once the solution is added to the form field, the original form submission event handler is invoked to do the submission. This is going to cause the page to change, so there is no need to worry about re-enabling the submit button.
The last component of the custom field is the class that represents the field itself, which relies on the above two classes as helpers:
from wtforms import Field

class ProofOfWorkField(Field):
    widget = ProofOfWorkWidget()

    def __init__(self, level, label='', validators=None, **kwargs):
        self.level = level
        validators = validators or [ProofOfWorkValidator()]
        super().__init__(label, validators, **kwargs)
The job of this class is to hold all the components of the custom field. The
widget
class attribute tells WTForms what widget to use to render the field, and the
validators
argument in the constructor links to the validator. A common pattern in WTForms fields is that the caller can provide a custom validator, although I don't think this is super useful for this use case. The
level
that we want to use for this challenge must be provided as an argument when the field is defined, and it is stored as an attribute so that it is available in the widget and the validator as
field.level
, as you have seen above.
A complete example
If you made it to here, then congratulate yourself, we are almost done! All that is left is to write an example Flask application with a form that we can use to test everything.
Since this is going to be just a test, the form that we are going to use will have just a name field and a submit button. The proof-of-work field is independent of whatever else is in the form, so it can be added to any form no matter how complex it is.
Here is what the form in the example looks like:
from flask_wtf import FlaskForm
from wtforms.fields import StringField, SubmitField

class TestForm(FlaskForm):
    name = StringField()
    challenge = ProofOfWorkField(level=4)
    submit = SubmitField()
Here you can see that I have decided to use a level 4 challenge, which in other words means that the client will need to find a hash that starts with
0000
. If you prefer to use quicker or slower challenges you can change the level to suit your taste.
Now we need a Flask application with an endpoint that renders the form and accepts form submissions. Using the form class above I coded a short endpoint as follows:
from flask import Flask, render_template

app = Flask(__name__)
app.config['SECRET_KEY'] = 'top-secret!'

@app.route('/', methods=['GET', 'POST'])
def index():
    form = TestForm()
    name = None
    if form.validate_on_submit():
        name = form.name.data
        form.name.data = ''
    return render_template('index.html', form=form, name=name)
Here the Flask application is created and then provisioned with a secret key, which is required because the user session uses it to generate the cryptographic signature that secures it.
The endpoint presents the form to the user when the browser requests the page, and then on submission it adds the name that the user provided to the template, so that it can show a confirmation that it was accepted. For a failed submission you would not see the name displayed, because in that case the form validation failure would cause the form to be re-rendered with an error message to give the user another chance to submit.
I assume you'll want to try this out. To make it easy for you to install this example below you have the complete application in a single source file, which you can call
pow.py
:
import hashlib
from secrets import token_hex
from time import time
from flask_wtf import FlaskForm
from wtforms.fields import Field, StringField, SubmitField
from wtforms.validators import ValidationError
from wtforms.widgets import html_params
from flask import Flask, render_template, session
from markupsafe import Markup

app = Flask(__name__)
app.config['SECRET_KEY'] = 'top-secret!'

class ProofOfWork:
    def __init__(self, level=4):
        self.level = level

    def validate_solution(self, challenge, solution):
        return hashlib.sha512(
            (challenge + solution).encode()
        ).hexdigest().startswith('0' * self.level)

    @staticmethod
    def get_js_solver():
        return '''
            async function sha512(message) {
              const encoder = new TextEncoder();
              const data = encoder.encode(message);
              const hash = await window.crypto.subtle.digest("SHA-512", data);
              return new Uint8Array(hash).toHex();
            }
            async function solve(challenge, level) {
              let hash;
              let solution = 0;
              do {
                hash = await sha512(challenge + ++solution);
              } while(hash.substr(0, level) !== "0".repeat(level));
              return solution;
            }
        '''

class ProofOfWorkValidator:
    def __init__(self, message='Verification failed'):
        self.message = message

    def __call__(self, form, field):
        if time() <= session.pop('_chexp', 0):
            pow = ProofOfWork(field.level)
            challenge = session.pop('_ch', '')
            if field.data and pow.validate_solution(challenge, field.data):
                return True
        raise ValidationError(self.message)

class ProofOfWorkWidget:
    def __call__(self, field, error=None, **kwargs):
        kwargs.setdefault('id', field.id)
        kwargs.setdefault('name', field.name)
        attributes = html_params(**kwargs)
        return Markup(f'''
            <input {attributes} type="hidden" value="">
            <script>
              {ProofOfWork.get_js_solver()}
              document.addEventListener('DOMContentLoaded', () => {{
                const field = document.getElementById('{field.name}');
                const form = field.form;
                form.addEventListener('submit', async (e) => {{
                  e.preventDefault();
                  e.submitter.disabled = true;
                  const response = await fetch('/_challenge');
                  if (response.ok) {{
                    const challenge = (await response.json())['challenge'];
                    field.value = await solve(challenge, {field.level});
                  }}
                  HTMLFormElement.prototype.submit.call(form);
                }});
              }});
            </script>
            ''')

class ProofOfWorkField(Field):
    widget = ProofOfWorkWidget()

    def __init__(self, level, label='', validators=None, **kwargs):
        self.level = level
        validators = validators or [ProofOfWorkValidator()]
        super().__init__(label, validators, **kwargs)

class TestForm(FlaskForm):
    name = StringField()
    challenge = ProofOfWorkField(level=4)
    submit = SubmitField()

@app.route('/', methods=['GET', 'POST'])
def index():
    form = TestForm()
    name = None
    if form.validate_on_submit():
        name = form.name.data
        form.name.data = ''
    return render_template('index.html', form=form, name=name)

@app.route('/_challenge')
def _challenge():
    session['_ch'] = token_hex()
    session['_chexp'] = time() + 60
    return {'challenge': session['_ch']}
In addition to the Python source code you'll need the
index.html
template file. This should go inside a
templates
folder that is in the same location as
pow.py
. Here is the template:
<html>
  <head>
    <title>Proof of Work Example</title>
  </head>
  <body>
    <h1>Proof of Work Example</h1>
    {% if name %}<p>Submission was accepted for name <b>{{ name }}</b>.</p>{% endif %}
    {% if form.errors %}
      <p>The form had the following errors:</p>
      <ul>
        {% for field, errors in form.errors.items() %}
          <li>{{ field }}: {{ ', '.join(errors) }}</li>
        {% endfor %}
      </ul>
    {% endif %}
    <form method="POST">
      {{ form.csrf_token }}
      name: {{ form.name }}
      {{ form.challenge }}
      {{ form.submit }}
    </form>
  </body>
</html>
For those who are familiar with Flask-WTF this template should look very familiar. At the top the page shows a message with the name that was received successfully in a form submission. This message is conditionally omitted when no form submission exists. Then the form is rendered as is standard for Flask-WTF and WTForms, including the list of validation errors, and each form field.
To test this example you have to install
flask
and
flask-wtf
as dependencies. My recommendation is that you create a virtual environment using your favorite tool and install these packages there. If you have no clue what I'm saying, then I recommend that you check out my
Flask Mega-Tutorial
first, then come back once you've learned the basics of working with a Flask project.
Once you try the example you are going to find that it isn't all that exciting, because you'll see a form that asks you to enter a name and submit, and once you submit it just shows you the name that you typed. The only difference with a plain form example is that you will see a slight delay when you hit the submit button. That's when the JavaScript solver is running.
If you want to see what happens when a bot attempts to submit to this form, you can try to submit with
curl
, which is actually somewhat similar to how bots do it. The following example submits the form with the
name
field and a made up value in the
challenge
field:
curl -X POST http://localhost:5000/ -H "Content-Type: application/x-www-form-urlencoded" -d "name=foo&challenge=dont-know"
The output from
curl
is going to be the HTML response. If you scan the HTML you'll find the section where the form validation errors are printed. You should see something like this:
<p>The form had the following errors:</p>
<ul>
  <li>challenge: Verification failed</li>
  <li>csrf_token: The CSRF token is missing.</li>
</ul>
In addition to the bad proof of work, this shows an error about the good old CSRF token, which is enforced by default in all Flask-WTF forms.
If you wanted to do this closer to the way the bots do it, you would need to send a
GET
request first, scan the HTML you receive for the CSRF token, then send the POST request including it. That should give you just one error about the bad or missing solution to the challenge. But if you wanted to provide a valid solution to the proof-of-work challenge, then you would need to read the JavaScript code and figure out what it does, and this is where I hope the bot operators will decide this would be too much work and isn't worth pursuing.
Let me know if this helps bring some sanity back to your forms. As I was saying above, it may not last forever, but for the last couple of months I have been enjoying near zero spam noise on my blog comments!
Thank you for visiting my blog! If you enjoyed this article, please consider supporting my work and keeping me caffeinated with a small one-time donation through
Buy me a coffee
. Thanks!
