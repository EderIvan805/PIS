from db import db

class CtDef_Sitio_Ocurrencia(db.Model):
    __tablename__ = 'CtDef_Sitio_Ocurrencia'
    Cve = db.Column(db.TinyInteger, primary_key=True)
    Descrip = db.Column(db.String(50), nullable=False)

    def to_dict(self):
        return {
            'Cve': self.Cve,
            'Descrip': self.Descrip
        }