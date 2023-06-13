from db import db

class Indicadores_Entidad_Residencia_2020(db.Model):
    __tablename__ = 'Indicadores_Entidad_Residencia_2020'
    Clave_EntFed = db.Column(db.SmallInteger, nullable=True)
    Total_Defunciones_Menores5 = db.Column(db.Integer, nullable=True)
    Poblacion_Menor5 = db.Column(db.Integer, nullable=True)
    Tasa_Mortalidad_Menores5 = db.Column(db.Float, nullable=True)
    Ent_Res = db.Column(db.String(100), nullable=True)
    Total_Defunciones_Menores1 = db.Column(db.Integer, nullable=True)
    Nacimientos_Anio = db.Column(db.Integer, nullable=True)
    Tasa_Mortalidad_Infantil = db.Column(db.Float, nullable=True)

    def to_dict(self):
        return {
            'Clave_EntFed': self.Clave_EntFed,
            'Total_Defunciones_Menores5': self.Total_Defunciones_Menores5,
            'Poblacion_Menor5': self.Poblacion_Menor5,
            'Tasa_Mortalidad_Menores5': self.Tasa_Mortalidad_Menores5,
            'Ent_Res': self.Ent_Res,
            'Total_Defunciones_Menores1': self.Total_Defunciones_Menores1,
            'Nacimientos_Anio': self.Nacimientos_Anio,
            'Tasa_Mortalidad_Infantil': self.Tasa_Mortalidad_Infantil
        }
