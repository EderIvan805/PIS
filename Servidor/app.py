from flask import Flask
from config import *
from db import db
from Rutas.CtDef_Anio import bp_def_anio
from Rutas.CtNac_Si_No import bp_nac_si_no

app = Flask(__name__)
app.config.from_object(__name__)
db.init_app(app)

app.register_blueprint(bp_def_anio, url_prefix='/PIS')
app.register_blueprint(bp_nac_si_no, url_prefix='/PIS')

# Manejo de errores
@app.errorhandler(404)
def pagina_no_encontrada(error):
    return "<h1>Página no encontrada </h1>", 404

if __name__ == '__main__':
    app.run(debug=app.config['DEBUG'])