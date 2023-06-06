from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow

db = SQLAlchemy()
ma = Marshmallow()

class CtDef_Año(db.Model):
    __tablename__ = 'CtDef_Año'
    Cve = db.Column(db.SmallInteger, primary_key=True)
    Descrip = db.Column(db.String(50), nullable=False)

    def __init__(self, Cve, Descrip):
        self.Cve = Cve
        self.Descrip = Descrip

class CtDef_AñoSchema(ma.Schema):
    class Meta:
        fields = ('Cve', 'Descrip')

ctDef_Año_schema = CtDef_AñoSchema()