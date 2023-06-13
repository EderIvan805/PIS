from db import db

class CtNac_Localidades_202203_2(db.Model):
    __tablename__ = 'CtNac_Localidades_202203_2'

    Cve_Ent = db.Column(db.String(10))
    Cve_Mun = db.Column(db.SmallInteger, primary_key=True)
    Cve_Loc = db.Column(db.SmallInteger, primary_key=True)
    Nom_Loc = db.Column(db.String(100), nullable=False)
    Estatus = db.Column(db.String(50))

    def to_dict(self):
        return {
            'Cve_Ent': self.Cve_Ent,
            'Cve_Mun': self.Cve_Mun,
            'Cve_Loc': self.Cve_Loc,
            'Nom_Loc': self.Nom_Loc,
            'Estatus': self.Estatus
        }
