from app import db

class Conjunto_De_Datos_Defunciones_Registrados_2020(db.Model):
    __tablename__ = 'Conjunto_De_Datos_Defunciones_Registrados_2020'
    Ent_regis = db.Column(db.SmallInteger, primary_key=True)
    Mun_regis = db.Column(db.SmallInteger, primary_key=True)
    Ent_resid = db.Column(db.SmallInteger, primary_key=True)
    Mun_resid = db.Column(db.SmallInteger, primary_key=True)
    Tloc_resid = db.Column(db.SmallInteger, primary_key=True)
    Loc_resid = db.Column(db.SmallInteger, primary_key=True)
    Ent_ocurr = db.Column(db.SmallInteger, primary_key=True)
    Mun_ocurr = db.Column(db.SmallInteger, primary_key=True)
    Tloc_ocurr = db.Column(db.SmallInteger, primary_key=True)
    Loc_ocurr = db.Column(db.SmallInteger, primary_key=True)
    Causa_def = db.Column(db.String(50), nullable=False)
    Lista_mex = db.Column(db.String(50), nullable=False)
    Sexo = db.Column(db.SmallInteger, nullable=False)
    Edad = db.Column(db.SmallInteger, nullable=False)
    Dia_ocurr = db.Column(db.SmallInteger, nullable=False)
    Mes_ocurr = db.Column(db.SmallInteger, nullable=False)
    Anio_ocur = db.Column(db.SmallInteger, nullable=False)
    Dia_regis = db.Column(db.SmallInteger, nullable=False)
    Mes_regis = db.Column(db.SmallInteger, nullable=False)
    Anio_regis = db.Column(db.SmallInteger, nullable=False)
    Dia_nacim = db.Column(db.SmallInteger, nullable=False)
    Mes_nacim = db.Column(db.SmallInteger, nullable=False)
    Anio_nacim = db.Column(db.SmallInteger, nullable=False)
    Ocupacion = db.Column(db.SmallInteger, nullable=False)
    Escolarida = db.Column(db.SmallInteger, nullable=False)
    Edo_civil = db.Column(db.SmallInteger, nullable=False)
    Presunto = db.Column(db.SmallInteger, nullable=False)
    Ocurr_trab = db.Column(db.SmallInteger, nullable=False)
    Lugar_ocur = db.Column(db.SmallInteger, nullable=False)
    Necropsia = db.Column(db.SmallInteger, nullable=False)
    Asist_medi = db.Column(db.SmallInteger, nullable=False)
    Sitio_ocur = db.Column(db.SmallInteger, nullable=False)
    Cond_cert = db.Column(db.SmallInteger, nullable=False)
    Nacionalid = db.Column(db.SmallInteger, nullable=False)
    Derechohab = db.Column(db.SmallInteger, nullable=False)
    Embarazo = db.Column(db.SmallInteger, nullable=False)
    Rel_emba = db.Column(db.SmallInteger, nullable=False)
    Horas = db.Column(db.SmallInteger, nullable=False)
    Minutos = db.Column(db.SmallInteger, nullable=False)
    Capitulo = db.Column(db.SmallInteger, nullable=False)
    Grupo = db.Column(db.SmallInteger)
    Lista1 = db.Column(db.SmallInteger, nullable=False)
    Gr_lismex = db.Column(db.String(20), nullable=False)
    Vio_fami = db.Column(db.SmallInteger, nullable=False)
    Area_ur = db.Column(db.SmallInteger, nullable=False)
    Edad_agru = db.Column(db.SmallInteger, nullable=False)
    Complicaro = db.Column(db.SmallInteger, nullable=False)
    Dia_cert = db.Column(db.SmallInteger, nullable=False)
    Mes_cert = db.Column(db.SmallInteger, nullable=False)
    Anio_cert = db.Column(db.SmallInteger, nullable=False)
    Maternas = db.Column(db.String(20))
    Lengua = db.Column(db.SmallInteger, nullable=False)
    Cond_act = db.Column(db.SmallInteger, nullable=False)
    Par_agre = db.Column(db.SmallInteger, nullable=False)
    Ent_ocules = db.Column(db.SmallInteger, nullable=False)
    Mun_ocules = db.Column(db.SmallInteger, nullable=False)
    Loc_ocules = db.Column(db.SmallInteger, nullable=False)
    Razon_m = db.Column(db.SmallInteger, nullable=False)
    Dis_re_oax = db.Column(db.SmallInteger, nullable=False)
    Edad_descodificada = db.Column(db.SmallInteger)

    def __init__(self, Ent_regis, Mun_regis, Ent_resid, Mun_resid, Tloc_resid, Loc_resid, Ent_ocurr, Mun_ocurr,
                 Tloc_ocurr, Loc_ocurr, Causa_def, Lista_mex, Sexo, Edad, Dia_ocurr, Mes_ocurr, Anio_ocur,
                 Dia_regis, Mes_regis, Anio_regis, Dia_nacim, Mes_nacim, Anio_nacim, Ocupacion, Escolarida,
                 Edo_civil, Presunto, Ocurr_trab, Lugar_ocur, Necropsia, Asist_medi, Sitio_ocur, Cond_cert,
                 Nacionalid, Derechohab, Embarazo, Rel_emba, Horas, Minutos, Capitulo, Grupo, Lista1, Gr_lismex,
                 Vio_fami, Area_ur, Edad_agru, Complicaro, Dia_cert, Mes_cert, Anio_cert, Maternas, Lengua,
                 Cond_act, Par_agre, Ent_ocules, Mun_ocules, Loc_ocules, Razon_m, Dis_re_oax, Edad_descodificada):
        self.Ent_regis = Ent_regis
        self.Mun_regis = Mun_regis
        self.Ent_resid = Ent_resid
        self.Mun_resid = Mun_resid
        self.Tloc_resid = Tloc_resid
        self.Loc_resid = Loc_resid
        self.Ent_ocurr = Ent_ocurr
        self.Mun_ocurr = Mun_ocurr
        self.Tloc_ocurr = Tloc_ocurr
        self.Loc_ocurr = Loc_ocurr
        self.Causa_def = Causa_def
        self.Lista_mex = Lista_mex
        self.Sexo = Sexo
        self.Edad = Edad
        self.Dia_ocurr = Dia_ocurr
        self.Mes_ocurr = Mes_ocurr
        self.Anio_ocur = Anio_ocur
        self.Dia_regis = Dia_regis
        self.Mes_regis = Mes_regis
        self.Anio_regis = Anio_regis
        self.Dia_nacim = Dia_nacim
        self.Mes_nacim = Mes_nacim
        self.Anio_nacim = Anio_nacim
        self.Ocupacion = Ocupacion
        self.Escolarida = Escolarida
        self.Edo_civil = Edo_civil
        self.Presunto = Presunto
        self.Ocurr_trab = Ocurr_trab
        self.Lugar_ocur = Lugar_ocur
        self.Necropsia = Necropsia
        self.Asist_medi = Asist_medi
        self.Sitio_ocur = Sitio_ocur
        self.Cond_cert = Cond_cert
        self.Nacionalid = Nacionalid
        self.Derechohab = Derechohab
        self.Embarazo = Embarazo
        self.Rel_emba = Rel_emba
        self.Horas = Horas
        self.Minutos = Minutos
        self.Capitulo = Capitulo
        self.Grupo = Grupo
        self.Lista1 = Lista1
        self.Gr_lismex = Gr_lismex
        self.Vio_fami = Vio_fami
        self.Area_ur = Area_ur
        self.Edad_agru = Edad_agru
        self.Complicaro = Complicaro
        self.Dia_cert = Dia_cert
        self.Mes_cert = Mes_cert
        self.Anio_cert = Anio_cert
        self.Maternas = Maternas
        self.Lengua = Lengua
        self.Cond_act = Cond_act
        self.Par_agre = Par_agre
        self.Ent_ocules = Ent_ocules
        self.Mun_ocules = Mun_ocules
        self.Loc_ocules = Loc_ocules
        self.Razon_m = Razon_m
        self.Dis_re_oax = Dis_re_oax
        self.Edad_descodificada = Edad_descodificada
