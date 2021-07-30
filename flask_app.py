# A very simple Flask Hello World app for you to get started with...

from flask import Flask, request
from password_verifier import password_strength
import requests

app = Flask(__name__)
app.config["DEBUG"] = True

@app.route('/', methods=["GET", "POST"])
def verify_password():
    errors=''
    if request.method == 'POST':
        password = ''
        try:
            password = request.form["password"]
        except:
            errors += "<p>{!r} is not a string.</p>\n".format(request.form["password"])
        if len(password) in range (8,21):
            result = password_strength(password)
            return '''
                <html>
                    <body>
                        <p>Your password strength is {result} out of 10.</p>
                        <p><a href="/">Click here to verify another password.</a></p>
                    </body>
                </html>
            '''.format(result=result)
        else:
            return '''
                <p>Please enter a password between 8 and 20 characters long.</p>
                <p><a href="/">Click here to verify another password.</a></p>
                '''

    return '''
        <html>
            <body>
                {errors}
                <p>Enter your password:</p>
                <form method="post" action=".">
                    <p><input name="password" /></p>
                    <p><input type="submit" value="Check password strength" /></p>
                </form>
            </body>
        </html>
    '''.format(errors=errors)