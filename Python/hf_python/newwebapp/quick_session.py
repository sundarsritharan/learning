from flask import Flask,session

app = Flask(__name__)

app.secret_key = 'testing'

@app.route('/setuser/<user>')
def set_user(user: str) -> str:
    """ set the user supplied value to the session """ 
    session['user'] = user
    return 'User value set to ' + session['user']

@app.route('/getuser')
def get_user() -> str:
    """ get the stored session details """ 
    return 'User value is currently set to: ' + session['user']

@app.route('/status')
def check_status() -> str:
    """ provide the status of your login"""
    if 'logged_in' in session:
        return 'You are now logged in.'
    
    return 'You are NOT logged in.'


if __name__ == '__main__':
    app.run(debug=True) 