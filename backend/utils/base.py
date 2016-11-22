import json

import sqlalchemy
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm import scoped_session
import tornado.web

import models
import settings


class Application(tornado.web.Application):
    def __init__(self, handlers):
        configs = {'debug': settings.DEBUG,
                   'xsrf_cookies': False}
        tornado.web.Application.__init__(self, handlers, **configs)
        engine = sqlalchemy.create_engine(settings.SQLALCHEMY_URL,
                                          convert_unicode=True,
                                          echo=settings.DEBUG)
        models.init_db(engine)
        self.db = scoped_session(sessionmaker(bind=engine))


class BaseHandler(tornado.web.RequestHandler):
    @property
    def db(self):
        return self.application.db

    def send_response(self, data, status=200):
        json_data = json.dumps(data)
        self.write(json_data)
        self.set_status(status)
        self.set_header('Content-Type', 'application/json')
