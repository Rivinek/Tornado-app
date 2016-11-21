from tornado.httpclient import AsyncHTTPClient
import greenlet
import functools

# this gives us access to the main IOLoop (the same used by uWSGI)
from tornado.ioloop import IOLoop
io_loop = IOLoop.instance()

def sleeper(me):
    #TIMED OUT
    # finally come back to WSGI callable
    me.switch()

# this is called at the end of the external HTTP request
def handle_request(me, response):
    if response.error:
        print("Error:", response.error)
    else:
        me.result = response.body
    # add another callback in the chain
    me.timeout = io_loop.add_timeout(time.time() + 10, functools.partial(sleeper, me))

def application(e, sr):
    me = greenlet.getcurrent()
    http_client = AsyncHTTPClient()
    http_client.fetch("http://localhost:9191/services", functools.partial(handle_request, me))
    # suspend the execution until an IOLoop event is available
    me.parent.switch()
    # unregister the timer
    io_loop.remove_timeout(me.timeout)
    sr('200 OK', [('Content-Type','text/plain')])
    return me.result