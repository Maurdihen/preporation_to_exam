class Config:
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = "postgresql://flask_app:flask_app_password@pg/flask_app"
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    JSON_AS_ASCII = False