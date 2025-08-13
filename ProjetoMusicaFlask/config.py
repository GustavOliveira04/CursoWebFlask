import os

SECRET_KEY = 'senhamusicas'

SQLALCHEMY_DATABASE_URI = '{SGBD}://{usuario}:{senha}@{servidor}/{database}'.format(
    SGBD = 'mysql+mysqlconnector',
    usuario = 'root',
    senha = '4858',
    servidor = 'localhost',
    database = 'playmusica'
)

UPLOAD_PASTA = os.path.dirname(os.path.abspath(__file__)) + '/uploads'