from init import db
from sqlalchemy import UniqueConstraint

class Algorithm(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(20),unique=True)
    grain_in_minutes = db.Column(db.Integer)


#application.hello()