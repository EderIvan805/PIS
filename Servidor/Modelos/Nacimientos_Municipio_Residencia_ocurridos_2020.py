from db import db

class Nacimientos_Municipio_Residencia_ocurridos_2020(db.Model):
    __tablename__ = 'Nacimientos_Municipio_Residencia_ocurridos_2020'
    Entidad_Res = db.Column(db.SmallInteger, primary_key=True)
    Descripcion_Ent_Res = db.Column(db.String(100))
    Municipio_Res = db.Column(db.SmallInteger)
    Descripcion_Mun_Res = db.Column(db.String(100))
    Total_Nacimientos = db.Column(db.Integer)

    def to_dict(self):
        return {
            'Entidad_Res': self.Entidad_Res,
            'Descripcion_Ent_Res': self.Descripcion_Ent_Res,
            'Municipio_Res': self.Municipio_Res,
            'Descripcion_Mun_Res': self.Descripcion_Mun_Res,
            'Total_Nacimientos': self.Total_Nacimientos
        }
