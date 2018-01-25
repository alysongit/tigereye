
import os



class DefaultConfig(object):
    DEBUG = True

    BASE_DIR = os.path.join(os.path.dirname(__file__), '../..')
    LOG_DIR = os.path.join(BASE_DIR, 'logs')
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:zq05535360050@localhost/tigereye'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_ECHO = True
