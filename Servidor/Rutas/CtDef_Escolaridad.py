from flask import Blueprint, jsonify, request
from Modelos.CtDef_Escolaridad import CtDef_Escolaridad
from sqlalchemy.exc import SQLAlchemyError
import pyodbc

bp_def_escolaridad = Blueprint('def_escolaridad', __name__)

@bp_def_escolaridad.route('/defEscolaridad', methods=['GET'])
def obtener_escolaridades():
    try:
        Cve = request.args.get('Cve')

        if Cve:
            def_escolaridad = CtDef_Escolaridad.query.filter_by(Cve=Cve).all()
        else:
            def_escolaridad = CtDef_Escolaridad.query.all()

        escolaridad_dict = [escolaridad.to_dict() for escolaridad in def_escolaridad]
        return jsonify({'Escolaridades': escolaridad_dict}), 200
    except SQLAlchemyError as db_error:
        return jsonify({'error': 'Error de conexión a la base de datos: ' + str(db_error)}), 500
    except pyodbc.OperationalError as connection_error:
        return jsonify({'error': 'Error de conexión con el servidor: ' + str(connection_error)}), 500
    except ValueError as value_error:
        return jsonify({'error': 'Error de formato: ' + str(value_error)}), 400
    except Exception as e:
        return jsonify({'error': 'Error desconocido: ' + str(e)}), 500