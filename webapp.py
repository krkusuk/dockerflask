from flask import Flask,render_template,request
import os,urllib,sys


from init import app

@app.route("/")
def index():
    return render_template('index.html')


runenv = os.environ['RUNENV']
if __name__ == "__main__":
    app.config['DEBUG'] = True
    if runenv == 'local':
        app.run(host='0.0.0.0',port=8000)
    else:
        app.run(host='0.0.0.0',port=6000)

