from flask import Blueprint, jsonify
from Modelos.CtNac_Si_No import CtNac_Si_No, ctNac_Si_No_Schema

ct_nac_si_no_routes = Blueprint('ct_nac_si_no_routes', __name__)

@ct_nac_si_no_routes.route("/CtNac_Si_No/<int:clave>", methods=['GET'])
def get_CtNac_Si_No_by_clave(clave):
    ct_nac_si_no = CtNac_Si_No.query.filter_by(clave=clave).first()
    if ct_nac_si_no:
        return ctNac_Si_No_Schema.jsonify(ct_nac_si_no)
    else:
        return jsonify(message='No se encontró ningún registro con el número de clave especificado.'), 404


