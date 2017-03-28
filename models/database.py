from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker
from sqlalchemy.ext.declarative import declarative_base
import os


engine = create_engine('sqlite:///{}'.format(os.path.abspath('database.db')))
db_session = scoped_session(sessionmaker(autocommit=False,
                                         autoflush=False,
                                         bind=engine))
Base = declarative_base()
Base.query = db_session.query_property()

def init_db():
    # import all modules here that might define models so that
    # they will be registered properly on the metadata.  Otherwise
    # you will have to import them first before calling init_db()
    import models.user
    import models.assignment
    import models.attendance
    import models.checkpoint
    import models.submission
    import models.teams
    Base.metadata.create_all(bind=engine)