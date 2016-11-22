import pytz
import datetime
import dateutil.parser

import tornado.wsgi
import wsgiref.simple_server

import models
from utils import base


class MainHandler(base.BaseHandler):
    def get(self):
        self.write("Hello, world")

    def post(self):
        str_date = self.get_argument("result", default=None, strip=False)
        # client_ip = self.request.headers.get("X-Real-IP")
        # date_now = datetime.datetime.now(pytz.timezone('Europe/Berlin'))
        # user_request = models.UserRequest(result=date_now, ip=client_ip)
        #
        # to_commit = [user_request]
        # if str_date:
        #     given_date = dateutil.parser.parse(str_date)
        #     difference_value = date_now - given_date
        #     to_commit.append(
        #         models.DateDifference(user_request=user_request,
        #                               difference_value=difference_value))
        # self.db.add(to_commit)
        # self.db.commit()
        # self.send_response({'ok': 'ok'}, status=201)


application = base.Application([
    (r"/", MainHandler),
])
wsgi_app = tornado.wsgi.WSGIAdapter(application)


if __name__ == "__main__":
    server = wsgiref.simple_server.make_server('', 8000, wsgi_app)
    server.serve_forever()
