import json

import tornado.web

import models
import settings


class Application(tornado.web.Application):
    def __init__(self, handlers):
        configs = {'debug': settings.DEBUG,
                   'xsrf_cookies': False}
        tornado.web.Application.__init__(self, handlers, **configs)
        self.db = models.create_session()


class BaseHandler(tornado.web.RequestHandler):
    @property
    def db(self):
        return self.application.db

    def send_response(self, data, status=200):
        json_data = json.dumps(data)
        self.write(json_data)
        self.set_status(status)
        self.set_header('Content-Type', 'application/json')
