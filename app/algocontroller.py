from init import app,db
from flask import  render_template, request

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
    
