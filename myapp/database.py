from sqlalchemy import create_engine

def get_database(app):
    #DATABASE = 'mysql://user:%(passwd)s@localhost/%(db)s?charset=utf8'
    DATABASE = 'sqlite:///myapp.db'
    engine = create_engine(DATABASE, pool_recycle=3600)
    return engine
