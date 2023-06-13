from db import db

class CtDef_Tamaño_Localidad(db.Model):
    __tablename__ = 'CtDef_Tamaño_Localidad'
    Cve = db.Column(db.TinyInteger, primary_key=True)
    Descrip = db.Column(db.String(50), nullable=False)

    def to_dict(self):
        return {
            'Cve': self.Cve,
            'Descrip': self.Descrip
        }
