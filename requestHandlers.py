import tornado.web
import tornado.ioloop
import psycopg2
import psycopg2.extras
import json
import datetime

from connector import Connector

class rootRequestHandler(tornado.web.RequestHandler):
    def get(self):
        self.render("index.html")


class allUsersHandler(tornado.web.RequestHandler):
    def get(self):

        # create connection to postgres database
        _connector = Connector()
        conn = _connector.connect()

        # create cursor
        cur = conn.cursor()

        cur.execute("select * from public.users LIMIT(100)")
        _result = cur.fetchall()
        self.render("testInsert.html", result=_result)
        cur.close()
        conn.close()

class externalRequestHandler(tornado.web.RequestHandler):
    def get(self):

        # create connection to postgres database
        _connector = Connector()
        conn = _connector.connect()

        # create cursor
        cur = conn.cursor()

        cur.execute("select * from public.users LIMIT(100)")
        _result = cur.fetchall()
        self.render("testInsert.html", result=_result)
        cur.close()
        conn.close()

class insertUserHandler(tornado.web.RequestHandler):
    def get(self):
                # create connection to postgres database
        _connector = Connector()
        conn = _connector.connect()

        # create cursor
        cur = conn.cursor()
        cur.execute("select * from public.users where id = 1")
        _result = cur.fetchall()
        self.render("testInsert.html",result=_result)
    def post(self):
        # create connection to postgres database
        _connector = Connector()
        conn = _connector.connect()

        # create cursor
        cur = conn.cursor()

        #define query parameters
        _firstname = self.get_argument("_firstname_field")
        _lastname = self.get_argument("_lastname_field")
        _timenow = datetime.datetime.now()
        _query = "INSERT INTO public.users(firstname, lastname, created_on) VALUES (%s,%s,%s)"
        cur.execute(_query,(_firstname,_lastname,_timenow))
        conn.commit()

        self.write("Submitted correctly")