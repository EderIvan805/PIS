import os

# Configuración de la conexión a la base de datos
DB_SERVER = 'DESKTOP-CND7JM2'
DB_NAME = 'InstitutoSalud'
DB_USERNAME = 'eder'
DB_PASSWORD = '123456'

# Ruta hacia la carpeta que contiene el archivo odbc.ini
ODBC_SYSINI_FOLDER = 'C:/Windows/System32/odbc.ini'

# Construcción de la cadena de conexión
SQLALCHEMY_DATABASE_URI = f'mssql+pyodbc://{DB_USERNAME}:{DB_PASSWORD}@{DB_SERVER}/{DB_NAME}?driver=ODBC+Driver+17+for+SQL+Server'

# Configuración de Flask
DEBUG = True

# Configuración de SQLAlchemy
SQLALCHEMY_TRACK_MODIFICATIONS = False

# Configuración de la variable de entorno ODBCSYSINI
os.environ['ODBCSYSINI'] = ODBC_SYSINI_FOLDER
