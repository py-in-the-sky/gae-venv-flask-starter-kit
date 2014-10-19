from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello():
    return 'Hello, world!'

# uncomment lines below if you wish to run in debug mode in your dev environment
# from werkzeug.debug import DebuggedApplication
# app.debug = True
# app = DebuggedApplication(app, evalex=True)

# @app.route('/test')  # for intentionally triggering the Flask debugger
# def test():
#     assert app.debug == False
#     return 'not in debug mode'
