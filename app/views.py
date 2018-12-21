from init import app
import sys

@app.route("/hi")
def hi():
    return "Hi from views"

@app.route("/version")
def version():
    return sys.version
