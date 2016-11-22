import datetime

import sqlalchemy
from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base()


def init_db(engine):
    Base.metadata.create_all(bind=engine)


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
    user_request = sqlalchemy.Column(sqlalchemy.ForeignKey('userrequest.id'))
