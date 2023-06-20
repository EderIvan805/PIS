from flask import Flask
from config import *
from db import db
from Rutas.CtDef_Anio import bp_def_anio
from Rutas.CtNac_Si_No import bp_nac_si_no
from Rutas.CtDef_Area_Urbana_Rural import bp_def_areaUrbana
from Rutas.CtDef_Asistencia_Medica import bp_def_asistenciaMedica
from Rutas.CtDef_Capitulo_Grupo import bp_def_capituloGrupo
from Rutas.CtDef_Causa_Defuncion import bp_def_causaDefuncion
from Rutas.CtDef_Certificante import bp_def_certificante
from Rutas.CtDef_Complicaron_Embarazo import bp_def_complicaron_embarazo
from Rutas.CtDef_Condicion_Actividad import bp_def_condicion_actividad
from Rutas.CtDef_Condicion_Embarazo import bp_def_condicion_embarazo
from Rutas.CtDef_Derechohabiencia import bp_def_derecho_habiencia
from Rutas.CtDef_Dia import bp_def_dia
from Rutas.CtDef_Edad_Agrupada import bp_def_edad_agrupada
from Rutas.CtDef_Edad import bp_def_edad
from Rutas.CtDef_Entidad_Municipio_Localidad_2020 import bp_def_entidadMunicipioLocalidad_2020
from Rutas.CtDef_Escolaridad import bp_def_escolaridad
from Rutas.CtDef_Estado_Civil import bp_def_estado_civil
from Rutas.CtDef_Grupo_Lista_Mexicana import bp_def_grupo_lista_mexicana
from Rutas.CtDef_Hora import bp_def_hora
from Rutas.CtDef_Lengua_Indigena import bp_def_lengua_indigena
from Rutas.CtDef_Lista1 import bp_def_lista1
from Rutas.CtDef_Lugar_Ocurrencia import bp_def_lugar_ocurrencia
from Rutas.CtDef_Mes import bp_def_mes
from Rutas.CtDef_Minuto import bp_def_minuto
from Rutas.CtDef_Nacionalidad import bp_def_nacionalidad
from Rutas.CtDef_Necropsia import bp_def_necropsia

app = Flask(__name__)
app.config.from_object(__name__)
db.init_app(app)

app.register_blueprint(bp_def_anio, url_prefix='/PIS')
app.register_blueprint(bp_nac_si_no, url_prefix='/PIS')
app.register_blueprint(bp_def_areaUrbana, url_prefix='/PIS')
app.register_blueprint(bp_def_asistenciaMedica, url_prefix='/PIS')
app.register_blueprint(bp_def_capituloGrupo, url_prefix='/PIS')
app.register_blueprint(bp_def_causaDefuncion, url_prefix='/PIS')
app.register_blueprint(bp_def_certificante, url_prefix='/PIS')
app.register_blueprint(bp_def_complicaron_embarazo, url_prefix='/PIS')
app.register_blueprint(bp_def_condicion_actividad, url_prefix='/PIS')
app.register_blueprint(bp_def_condicion_embarazo, url_prefix='/PIS')
app.register_blueprint(bp_def_derecho_habiencia, url_prefix='/PIS')
app.register_blueprint(bp_def_dia, url_prefix='/PIS')
app.register_blueprint(bp_def_edad_agrupada, url_prefix='/PIS')
app.register_blueprint(bp_def_edad, url_prefix='/PIS')
app.register_blueprint(bp_def_entidadMunicipioLocalidad_2020, url_prefix='/PIS')
app.register_blueprint(bp_def_escolaridad, url_prefix='/PIS')
app.register_blueprint(bp_def_estado_civil, url_prefix='/PIS')
app.register_blueprint(bp_def_grupo_lista_mexicana, url_prefix='/PIS')
app.register_blueprint(bp_def_hora, url_prefix='/PIS')
app.register_blueprint(bp_def_lengua_indigena, url_prefix='/PIS')
app.register_blueprint(bp_def_lista1, url_prefix='/PIS')
app.register_blueprint(bp_def_lugar_ocurrencia, url_prefix='/PIS')
app.register_blueprint(bp_def_mes, url_prefix='/PIS')
app.register_blueprint(bp_def_minuto, url_prefix='/PIS')
app.register_blueprint(bp_def_nacionalidad, url_prefix='/PIS')
app.register_blueprint(bp_def_necropsia, url_prefix='/PIS')

# Manejo de errores
@app.errorhandler(404)
def pagina_no_encontrada(error):
    return "<h1>Página no encontrada </h1>", 404

if __name__ == '__main__':
    app.run(debug=app.config['DEBUG'])