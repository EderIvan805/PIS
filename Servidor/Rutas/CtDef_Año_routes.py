from flask import Blueprint, jsonify
from Modelos.CtDef_Año import CtDef_Año, ctDef_Año_schema

ct_def_Año_routes = Blueprint('ct_def_Año_routes', __name__)

@ct_def_Año_routes.route("/CtDef_Anio/<int:Cve>", methods=['GET'])
def get_ctdef_anio_by_clave(Cve):
    ct_def_anio = CtDef_Año.query.filter_by(Cve=Cve).first()
    if ct_def_anio:
        return ctDef_Año_schema.jsonify(ct_def_anio)
    else:
        return jsonify(message='No se encontró ningún registro con el número de cve especificado.'), 404