import sqlalchemy
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


def init_db(engine):
    Base.metadata.create_all(bind=engine)


class UserRequest(Base):
    __tablename__ = 'userrequest'

    id = sqlalchemy.Column(sqlalchemy.Integer, primary_key=True)
    name = sqlalchemy.Column(sqlalchemy.String)
