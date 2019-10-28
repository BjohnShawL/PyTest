import os
import datetime
import psycopg2
import psycopg2.extras
import tornado.web
import tornado.ioloop
import tornado.httpserver
import json
import uimodules

from requestHandlers import allUsersHandler
from requestHandlers import rootRequestHandler
from requestHandlers import insertUserHandler

def main():
# configure webapp
    settings = dict(
    cookie_secret = str(os.urandom(45)),
    template_path= os.path.join(os.path.dirname(__file__),"templates"),
    static_path= os.path.join(os.path.dirname(__file__),"static"),
    ui_modules = uimodules,
    xsrf_cookies = True,
    autoreload = True,
    gzip = True,
    debug= True,
    login_url = '/login',
    autoescape = None
)
# create webapp
    app = tornado.web.Application([
        (r"/", rootRequestHandler),
        (r"/insert",insertUserHandler),
        (r"/users",allUsersHandler)
    ], **settings)

    http_server = tornado.httpserver.HTTPServer(app)
    port = int(os.environ.get("PORT", 8881))
    http_server.listen(port)
    tornado.ioloop.IOLoop.instance().start()

if __name__ == "__main__":
    main()

#cleanup

