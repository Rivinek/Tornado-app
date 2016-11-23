import datetime

import sqlalchemy
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm import scoped_session

import settings


Base = declarative_base()


def init_db(engine):
    Base.metadata.create_all(bind=engine)


def create_session():
    engine = sqlalchemy.create_engine(settings.SQLALCHEMY_URL,
                                      convert_unicode=True,
                                      echo=settings.DEBUG)
    init_db(engine)
    return scoped_session(sessionmaker(bind=engine))


class UserRequest(Base):
    __tablename__ = 'userrequest'

    id = sqlalchemy.Column(sqlalchemy.Integer, primary_key=True)
    result = sqlalchemy.Column(sqlalchemy.DateTime)
    created_at = sqlalchemy.Column(sqlalchemy.DateTime,
                                   default=datetime.datetime.utcnow)
    ip = sqlalchemy.Column(sqlalchemy.String)


class DateDifference(Base):
    __tablename__ = 'datedifference'

    id = sqlalchemy.Column(sqlalchemy.Integer, primary_key=True)
    difference = sqlalchemy.Column(sqlalchemy.Float)
    user_request_id = sqlalchemy.Column(
        sqlalchemy.Integer,
        sqlalchemy.ForeignKey(UserRequest.id, ondelete='CASCADE'))
