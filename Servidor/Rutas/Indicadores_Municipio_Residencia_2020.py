from flask import Blueprint, jsonify, request
from Modelos.Indicadores_Municipio_Residencia_2020 import Indicadores_Municipio_Residencia_2020
from sqlalchemy.exc import SQLAlchemyError
import pyodbc

bp_indicadores_municipio_residencia_2020 = Blueprint('indicadores_municipio_residencia_2020', __name__)

@bp_indicadores_municipio_residencia_2020.route('/indicadoresMunicipioResidencia2020', methods=['GET'])
def obtener_indicadores_municipio_residencia_2020():
    try:
        query = Indicadores_Municipio_Residencia_2020.query

        # Obtener los valores de los parámetros de solicitud
        Entidad_Res = request.args.get('Entidad_Res')
        Municipio_Res = request.args.get('Municipio_Res')

        # Agregar los filtros si los parámetros están presentes
        if Entidad_Res:
            query = query.filter_by(Entidad_Res=Entidad_Res)
        if Municipio_Res:
            query = query.filter_by(Municipio_Res=Municipio_Res)

        indicadoresMunicipioResidencia2020 = query.all()

        indicadoresMunicipioResidencia2020_dict = [indicadoresMunicipioResidencia2020.to_dict() for indicadoresMunicipioResidencia2020 in indicadoresMunicipioResidencia2020]
        return jsonify({'Indicadores': indicadoresMunicipioResidencia2020_dict}), 200
    except SQLAlchemyError as db_error:
        return jsonify({'error': 'Error de conexión a la base de datos: ' + str(db_error)}), 500
    except pyodbc.OperationalError as connection_error:
        return jsonify({'error': 'Error de conexión con el servidor: ' + str(connection_error)}), 500
    except ValueError as value_error:
        return jsonify({'error': 'Error de formato: ' + str(value_error)}), 400
    except Exception as e:
        return jsonify({'error': 'Error desconocido: ' + str(e)}), 500