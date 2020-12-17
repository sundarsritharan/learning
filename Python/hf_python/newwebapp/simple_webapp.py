from flask import Flask,session
from checker import check_logged_in

app = Flask(__name__)

app.secret_key = 'YouWillNeverGuess'

@app.route('/')
def hello() -> str:
    """ return welcome message """
    return 'Hello from the simple webapp'

@app.route('/page1')
@check_logged_in
def page1() -> str:
    """ return page name """
    return 'This is page 1'

@app.route('/page2')
@check_logged_in
def page2() -> str:
    """ return page name """
    return 'This is page 2'

@app.route('/page3')
@check_logged_in
def page3() -> str:
    """ return page name """
    return 'This is page 3'

@app.route('/login')
def do_login() -> str:
    """ set the login flag """
    session['logged_in'] = True
    return 'You are now logged in.'

@app.route('/logout')
def do_logout() -> str:
    """ remove the login flag """
    session.pop('logged_in')
    return 'You are now logged out.'

if __name__ == '__main__':
    app.run(debug=True)