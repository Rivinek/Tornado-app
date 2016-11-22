import tornado.web
import tornado.wsgi
import wsgiref.simple_server


class MainHandler(tornado.web.RequestHandler):
    def get(self):
        self.write("Hello, world")


application = tornado.web.Application([
    (r"/", MainHandler),
])
wsgi_app = tornado.wsgi.WSGIAdapter(application)


if __name__ == "__main__":
    server = wsgiref.simple_server.make_server('', 8000, wsgi_app)
    server.serve_forever()