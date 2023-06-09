from flask import Blueprint, jsonify
from Modelos.CtDef_Anio import CtDef_Anio

bp_def_anio = Blueprint('def_anio', __name__)

@bp_def_anio.route('/defAnio', methods=['GET'])
def obtener_anios():
    anios = CtDef_Anio.query.all()
    anios_dict = [anio.to_dict() for anio in anios]
    return jsonify({'Defunciones por anio': anios_dict})
