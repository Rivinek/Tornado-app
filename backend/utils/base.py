import sqlalchemy
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm import scoped_session
from tornado import web

import models
import settings


class Application(web.Application):
    def __init__(self, handlers):
        configs = {'debug': settings.DEBUG,
                   'xsrf_cookies': True}
        web.Application.__init__(self, handlers, **configs)
        engine = sqlalchemy.create_engine(settings.SQLALCHEMY_URL)
        models.init_db(engine)
        self.db = scoped_session(sessionmaker(bind=engine))


class BaseHandler(web.RequestHandler):
    @property
    def db(self):
        return self.application.db
