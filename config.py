SECRET_KEY = 'fecaf'

SQLALCHEMY_DATABASE_URI = \
    '{SGBD}://{usuario}:{senha}@{servidor}/{database}'.format(
        SGBD = 'mysql+mysqlconnector',
        usuario = 'root',
        senha = '8642B.f.t13062005',
        servidor = 'localhost',
        database = 'ecommerce'
    )