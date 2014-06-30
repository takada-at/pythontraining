import sys
import os
from sqlalchemy import create_engine

sys.path.append(os.path.realpath(os.path.join(os.path.basename(__file__), '..')))

from bbs.models import Base
from bbs.database import create_session

def testsession():
    db = create_engine('sqlite:///:memory:')
    metadata = Base.metadata
    metadata.bind = db
    metadata.create_all(db)
    return create_session(db)

