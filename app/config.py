class Config:
    SQLALCHEMY_DATABASE_URI = 'sqlite:///app.db'
    DEBUG = False

class DevelopmentConfig(Config):
    DEBUG = True

class ProductionConfig(Config):
    DEBUG = False
