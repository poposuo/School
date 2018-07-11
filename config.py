import os
basedir = os.path.abspath(os.path.dirname(__file__))

class Config:
    DEBUG = True
    # SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'data-test.sqlite')
    # SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://test:Yq!((&1024@localhost/TEST'
    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'data-test.sqlite')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SECRET_KEY = '123'
    TRAP_BAD_REQUEST_ERRORS = False # For restful api
    TRAP_HTTP_EXCEPTIONS = False
    IMAGE_SERVER = 'http://asserts.fondoger.cn/'

    @staticmethod
    def init_app(app):
        pass


class Development(Config):
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://test:Yq!((&1024@localhost/TEST'


config = {
    "default": Config,
    "development": Development,
}
