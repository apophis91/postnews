import os


BASE_DIR = os.path.dirname(os.path.dirname(__file__))


def get_env(name, default=None):
    return os.environ.get(name, default)


default_database = 'sqlite:///' + os.path.join(BASE_DIR, 'postnews.sqlite')


class BaseConf:
    TESTING = False
    DEBUG = False
    SECRET_KEY = get_env('SECRET_KEY', 
                         '8647425bdc4b1113a79f4b105156b0f1')
    SQLALCHEMY_DATABASE_URI = get_env('DATABASE_URI', default_database)
    SQLALCHEMY_TRACK_MODIFICATIONS = False


class DevelopmentConf(BaseConf):
    DEBUG = True


class TestingConf(BaseConf):
    TESTING = True
    SQLALCHEMY_DATABASE_URI = 'sqlite://'


class ProductionConf(BaseConf):
    pass


config = {
    'development': DevelopmentConf,
    'production': ProductionConf,
    'testing': TestingConf
}
