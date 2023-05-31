from flask import Flask, jsonify
import urllib.parse
import pyodbc
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow

app = Flask(__name__)

params = urllib.parse.quote_plus('DRIVER={SQL Server};SERVER=DESKTOP-CND7JM2;DATABASE=InstitutoSalud;Trusted_Connection=yes;')
app.config['SQLALCHEMY_DATABASE_URI'] = "mssql+pyodbc:///?odbc_connect=%s" % params
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)
ma = Marshmallow(app)

# Definir el modelo CtNac_Si_No y el esquema correspondiente

class CtNac_Si_No(db.Model):
    __tablename__ = 'CtNac_Si_No'
    clave = db.Column(db.Integer, primary_key=True)
    descripcion = db.Column('Descripción', db.String(50))

    def __init__(self, clave, descripcion):
        self.clave = clave
        self.descripcion = descripcion

class CtNac_Si_No_Schema(ma.Schema):
    class Meta:
        fields = ('clave', 'descripcion')

ctNac_Si_No_Schema = CtNac_Si_No_Schema()

# Ruta para obtener todos los datos de la tabla CtNac_Si_No

@app.route("/CtNac_Si_No/<int:clave>", methods=['GET'])
def get_CtNac_Si_No_by_clave(clave):
    ct_nac_si_no = CtNac_Si_No.query.filter_by(clave=clave).first()
    if ct_nac_si_no:
        return ctNac_Si_No_Schema.jsonify(ct_nac_si_no)
    else:
        return jsonify(message='No se encontró ningún registro con el número de clave especificado.'), 404

if __name__ == '__main__':
    app.run(debug=True)
