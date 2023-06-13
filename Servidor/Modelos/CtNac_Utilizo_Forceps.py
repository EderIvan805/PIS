from db import db

class CtNac_Utilizo_Forceps(db.Model):
    __tablename__ = 'CtNac_Utilizo_Forceps'
    Clave = db.Column(db.TinyInteger, primary_key=True)
    Descripcion = db.Column(db.String(50), nullable=False)

    def to_dict(self):
        return {
            'Clave': self.Clave,
            'Descripcion': self.Descripcion
        }
