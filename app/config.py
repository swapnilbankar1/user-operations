import urllib.parse
urllib.parse.quote_plus('P@ssw0rd1234')

class Config:
    SQLALCHEMY_DATABASE_URI = 'mysql+mysqldb://swapnil:P%40ssw0rd1234@localhost/mydatabase'
    SQLALCHEMY_TRACK_MODIFICATIONS = False


class DevelopmentConfig(Config):
    DEBUG = True

class ProductionConfig(Config):
    DEBUG = False
