import os
from sqlalchemy import create_engine

def get_local_db_conf():
    path = os.path.dirname(os.path.abspath(__file__))
    local_dbauth_path = os.path.join(path, 'dbauth')
    if not os.path.exists(local_dbauth_path):
        return
    with open(os.path.join(path, 'dbauth')) as f:
        return f.readline().rstrip().split(':')

def get_database(app):
    PUBLIC_MYSQL_URI = 'mysql+pymysql://{}:{}@localhost/bbs?charset=utf8'
    DATABASE = PUBLIC_MYSQL_URI.format(*get_local_db_conf())
    #DATABASE = 'sqlite:///myapp.db'
    engine = create_engine(DATABASE, pool_recycle=3600)
    return engine
