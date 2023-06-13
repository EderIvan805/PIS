from db import db

class CtNac_Afiliacion_Certificados(db.Model):
    __tablename__ = 'CtNac_Afiliacion_Certificados'
    Clave = db.Column(db.TinyInteger, primary_key=True)
    Descripcion = db.Column(db.String(50), nullable=False)

    def to_dict(self):
        return {
            'Clave': self.Clave,
            'Descripcion': self.Descripcion
        }
