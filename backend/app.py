import datetime
import dateutil.parser
import json

import tornado.wsgi
import wsgiref.simple_server

import models
from utils import base


class MainHandler(base.BaseHandler):
    def get(self):
        self.write("Hello, world")

    def post(self):
        str_date = json.loads(self.request.body)['result']
        client_ip = self.request.headers.get("X-Real-IP")
        date_now = datetime.datetime.now()
        user_request = models.UserRequest.get_or_create(self.db,
                                                        ip=client_ip)
        response_data = {'request': date_now.isoformat()}
        if str_date:
            given_date = dateutil.parser.parse(str_date)
            difference_value = (date_now - given_date).total_seconds()
            date_difference = models.DateDifference(
                user_request_id=user_request.id,
                difference=difference_value)
            self.db.add(date_difference)
            self.db.commit()
            average_difference = user_request.average_difference(self.db)
            response_data['difference'] = {'result': difference_value}
            response_data['average_difference'] = average_difference

        self.send_response(response_data, status=201)


application = base.Application([
    (r"/", MainHandler),
])
wsgi_app = tornado.wsgi.WSGIAdapter(application)


if __name__ == "__main__":
    server = wsgiref.simple_server.make_server('', 8000, wsgi_app)
    server.serve_forever()
