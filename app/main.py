from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello():
    return 'Hello, world!'

# uncomment line below if you wish to run in debug mode in your dev environment
# app.debug = True
