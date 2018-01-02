from postnews.core import db


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String, nullable=False)
    pw_hash = db.Column(db.String(255), nullable=False)
