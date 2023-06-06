from flask import Flask, jsonify
import urllib.parse
import pyodbc
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
from Modelos.CtNac_Si_No import db, ma
from Rutas.CtNac_Si_No_routes import ct_nac_si_no_routes
from Modelos.CtDef_Año import db, ma
from Rutas.CtDef_Año_routes import ct_def_Año_routes

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = "mssql+pyodbc:///?odbc_connect=%s" % urllib.parse.quote_plus('DRIVER={SQL Server};SERVER=DESKTOP-CND7JM2;DATABASE=InstitutoSalud;Trusted_Connection=yes;')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)
ma.init_app(app)

if __name__ == '__main__':
    app.register_blueprint(ct_nac_si_no_routes)
    app.register_blueprint(ct_def_Año_routes)
    app.run(debug=True)
