from flask import Blueprint, jsonify
from Modelos.CtNac_Si_No import CtNac_Si_No

bp_nac_si_no = Blueprint('nac_si_no', __name__)

@bp_nac_si_no.route('/nacSiNo', methods=['GET'])
def obtener_si_no():
    si_no = CtNac_Si_No.query.all()
    si_no_dict = [valor.to_dict() for valor in si_no]
    return jsonify({'Nacimientos si_no': si_no_dict})
