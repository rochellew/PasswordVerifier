# A very simple Flask Hello World app for you to get started with...

from flask import Flask, request
from password_verifier import password_strength

app = Flask(__name__)
app.config["DEBUG"] = True

@app.route('/', methods=["GET", "POST"])
def hello_world():
    errors=''
    if request.method == 'POST':
        password = ''
        try:
            password = request.form["password"]
        except:
            errors += "<p>{!r} is not a string.</p>\n".format(request.form["password"])
        if len(password) > 0:
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
            errors += "<p>Please enter a password.</p>\n"

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