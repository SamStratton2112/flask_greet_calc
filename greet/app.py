from flask import Flask

# Greet
# In the greet folder, Make a simple Flask app that
#  responds to these routes with simple text messages:

# /welcome
# Returns “welcome”

# /welcome/home
# Returns “welcome home”

# /welcome/back
# Return “welcome back”

# Once you’ve finished this, run the tests for it:

app = Flask(__name__)

@app.route('/welcome')
def say_welcome():
    return 'Welcome!'

@app.route('/welcome/home')
def wel_home():
    return 'Welcome home!!'

@app.route('/welcome/back')
def wel_back():
    return 'Welcome back!!'