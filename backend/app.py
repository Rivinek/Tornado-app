import tornado.wsgi
import wsgiref.simple_server

from utils import base


class MainHandler(base.BaseHandler):
    def get(self):
        self.write("Hello, world")

    def post(self):
        pass


application = base.Application([
    (r"/", MainHandler),
])
wsgi_app = tornado.wsgi.WSGIAdapter(application)


if __name__ == "__main__":
    server = wsgiref.simple_server.make_server('', 8000, wsgi_app)
    server.serve_forever()
