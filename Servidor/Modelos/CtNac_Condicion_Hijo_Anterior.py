from db import db

class CtNac_Condicion_Hijo_Anterior(db.Model):
    __tablename__ = 'CtNac_Condicion_Hijo_Anterior'
    Clave = db.Column(db.TinyInteger, primary_key=True)
    Descripcion = db.Column(db.String(50), nullable=False)

    def to_dict(self):
        return {
            'Clave': self.Clave,
            'Descripcion': self.Descripcion
        }
