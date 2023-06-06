from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow

db = SQLAlchemy()
ma = Marshmallow()

class CtNac_Si_No(db.Model):
    __tablename__ = 'CtNac_Si_No'
    clave = db.Column(db.Integer, primary_key=True)
    descripcion = db.Column('Descripción', db.String(50))

    def __init__(self, clave, descripcion):
        self.clave = clave
        self.descripcion = descripcion

class CtNac_Si_No_Schema(ma.Schema):
    class Meta:
        fields = ('clave', 'descripcion')

ctNac_Si_No_Schema = CtNac_Si_No_Schema()