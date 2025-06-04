import os
#obtinere cale absoluta
basedir = os.path.abspath(os.path.dirname(__file__))

class Config:
    #Definim calea pentru instance 
    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'instance', 'students.db')

    SQLALCHEMY_TRACK_MODIFICATIONS = False
