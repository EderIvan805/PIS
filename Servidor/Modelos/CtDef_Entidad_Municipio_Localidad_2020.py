from db import db

class CtDef_Entidad_Municipio_Localidad_2020(db.Model):
    __tablename__ = 'CtDef_Entidad_Municipio_Localidad_2020'
    Cve_Ent = db.Column(db.SmallInteger, primary_key=True)
    Cve_Mun = db.Column(db.SmallInteger, primary_key=True)
    Cve_Loc = db.Column(db.SmallInteger, primary_key=True)
    Nom_Loc = db.Column(db.String(100), nullable=False)

    def to_dict(self):
        return {
            'Cve_Ent': self.Cve_Ent,
            'Cve_Mun': self.Cve_Mun,
            'Cve_Loc': self.Cve_Loc,
            'Nom_Loc': self.Nom_Loc
        }
