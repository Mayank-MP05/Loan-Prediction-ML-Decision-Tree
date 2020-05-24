from flask import Flask
from markupsafe import escape

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, World!'

@app.route('/login')
def login():
    return f"This is Login Page"

@app.route('/logout')
def logout():
    return f"This is Logout Page"


@app.route('/user/<string:userid>')
def sendUser(userid):
    return f"UUID is {escape(userid)}"