from db import db

class CtNac_Persona_Atendio_Parto(db.Model):
    __tablename__ = 'CtNac_Persona_Atendio_Parto'
    Clave = db.Column(db.TinyInteger, primary_key=True)
    Descripcion = db.Column(db.String(50), nullable=False)

    def to_dict(self):
        return {
            'Clave': self.Clave,
            'Descripcion': self.Descripcion
        }