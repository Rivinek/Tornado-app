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


class BaseModel():
    @classmethod
    def get_or_create(cls, session, **kwargs):
        instance = session.query(cls).filter_by(**kwargs).first()
        if instance:
            return instance
        else:
            instance = cls(**kwargs)
            session.add(instance)
            session.commit()
            return instance


class UserRequest(BaseModel, Base):
    __tablename__ = 'userrequest'

    id = sqlalchemy.Column(sqlalchemy.Integer, primary_key=True)
    result = sqlalchemy.Column(sqlalchemy.DateTime)
    created_at = sqlalchemy.Column(sqlalchemy.DateTime,
                                   default=datetime.datetime.utcnow)
    ip = sqlalchemy.Column(sqlalchemy.String)

    def average_difference(self, session):
        all_differences = session.query(DateDifference).filter(
            DateDifference.user_request_id==self.id).all()
        difference_count = sum([difference.difference
                                for difference in all_differences])
        return difference_count / len(all_differences)


class DateDifference(BaseModel, Base):
    __tablename__ = 'datedifference'

    id = sqlalchemy.Column(sqlalchemy.Integer, primary_key=True)
    difference = sqlalchemy.Column(sqlalchemy.Float)
    user_request_id = sqlalchemy.Column(
        sqlalchemy.Integer,
        sqlalchemy.ForeignKey(UserRequest.id, ondelete='CASCADE'))
