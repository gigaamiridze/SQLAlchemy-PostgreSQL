class Config(object):
    # Database settings
    DB_USER = 'gigaamiridze'
    DB_PASSWORD = 'qwerty123'
    DB_HOST = 'localhost'
    DB_PORT = 5432
    DB_NAME = 'database'

    DB_URL = f'postgresql+psycopg2://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}'

    SQLALCHEMY_DATABASE_URI = DB_URL
    SQLALCHEMY_TRACK_MODIFICATIONS = False
