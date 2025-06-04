from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

#Clasa student definita pentru stocare de date folosint SQL Alchemy 
class Student(db.Model):
    __tablename__ = 'studenti'
    id = db.Column(db.Integer, primary_key=True)
    nume = db.Column(db.String(100), nullable=False)
    grupa = db.Column(db.String(10), nullable=False)
    specializare = db.Column(db.String(100), nullable=True)
    email = db.Column(db.String(120), nullable=True)
    credite = db.Column(db.Integer, nullable=True)
    nota_m1 = db.Column(db.Float, nullable=True)
    nota_m2 = db.Column(db.Float, nullable=True)
    media = db.Column(db.Float, nullable=True)  # calculată înainte de salvare
    judet = db.Column(db.String(100), nullable=True)
    oras = db.Column(db.String(100), nullable=True)
    an = db.Column(db.String(1))  # '1', '2', '3'