class Config:
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = "postgresql://$DB_USER:$DB_PASSWORD@pg/$DB_NAME"
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    RESTX_JSON = {'ensure_ascii': False, 'indent': 2}
    JSON_AS_ASCII = False