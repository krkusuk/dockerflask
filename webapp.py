from flask import Flask,render_template,request
from flask_sqlalchemy import SQLAlchemy
import os,urllib,sys

app = Flask(__name__)


@app.route("/")
def index():
    return 'Hello from Krishan desktop through docker again. This time from vscode.'

@app.route("/version")
def version():
    return sys.version


server = <database server>
database = <database name>
username = <user name>
password = <password>


runenv = os.environ['RUNENV']
print(runenv)
if runenv == 'local':
    #My local machine is windows
    drivername = 'SQL Server'
else:
    drivername = 'ODBC Driver 17 for SQL Server'
conDEBUG = 'DRIVER={'+drivername+'};SERVER='+server+';PORT=1443;DATABASE='+database+';UID='+username+';PWD='+ password

print(conDEBUG)
conDEBUG = urllib.parse.quote_plus(conDEBUG)
conDEBUG = "mssql+pyodbc:///?odbc_connect=%s" % conDEBUG
app.config['SQLALCHEMY_DATABASE_URI'] = conDEBUG
db = SQLAlchemy(app)

@app.route("/algos")
def algos():
    from models.algorithms import Algorithm
    algos = Algorithm.query.all()
    return render_template('showalgos.html',algos=algos)

@app.route("/addalgo", methods=['GET'])
def addalgo():
    return render_template('addalgo.html')

@app.route("/addalgo", methods=['POST'])
def addalgo_post():
    from models.algorithms import Algorithm
    name = request.form.get('algoname')
    grain = request.form.get('grain')
    newalgo = Algorithm(name=name,grain_in_minutes=grain)
    try:
        db.session.add(newalgo)
        db.session.commit()
        return render_template('success.html')
    except Exception as e:
        return render_template('failure.html',error = 'Error while adding value in db.'+ str(e))
    


if __name__ == "__main__":
    #app.config['DEBUG'] = True
    if runenv == 'local':
        app.run(host='0.0.0.0',port=8000)
    else:
        app.run(host='0.0.0.0',port=6000)

