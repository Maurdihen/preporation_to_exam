class Config:
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = "postgresql://flask_app:flask_app_password@pg/flask_app"
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    RESTX_JSON = {'ensure_ascii': False, 'indent': 2}
    JSON_AS_ASCII = False
