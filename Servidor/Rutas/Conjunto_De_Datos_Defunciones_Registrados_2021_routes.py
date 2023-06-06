from flask import Blueprint, jsonify
from Modelos.Conjunto_De_Datos_Defunciones_Registrados_2021 import db, Conjunto_De_Datos_Defunciones_Registrados_2021

# Crear el blueprint
defunciones2021_bp = Blueprint('defunciones2021', __name__)

# Ruta para obtener todos los registros de la tabla
@defunciones2021_bp.route('/defunciones2021', methods=['GET'])
def get_defunciones():
    try:
        defunciones = Conjunto_De_Datos_Defunciones_Registrados_2021.query.all()
        result = []
        for defuncion in defunciones:
            result.append(defuncion.__dict__)
        return jsonify(result)
    except Exception as e:
        return jsonify({'error': str(e)}), 500

# Ruta para obtener un registro por su id
@defunciones2021_bp.route('/defunciones2021/<int:defuncion_id>', methods=['GET'])
def get_defuncion(defuncion_id):
    try:
        defuncion = Conjunto_De_Datos_Defunciones_Registrados_2021.query.get(defuncion_id)
        if defuncion is None:
            return jsonify({'message': 'Defunción no encontrada'}), 404
        return jsonify(defuncion.__dict__)
    except Exception as e:
        return jsonify({'error': str(e)}), 500