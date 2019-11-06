import tornado.web
import tornado.ioloop
import psycopg2
import psycopg2.extras
import json
import datetime

from connector import Connector
from resultsService import ResultsService
from queries import Queries

class rootRequestHandler(tornado.web.RequestHandler):
    def get(self):
        self.render("index.html")

class allUsersHandler(tornado.web.RequestHandler):
    def get(self):
# Region Set Up
        #create resultService object
        _resultsService = ResultsService()
        q= Queries()

        # create connection to postgres database
        _connector = Connector()
        conn = _connector.connect()

        # create cursor
        cur = conn.cursor()
# endregion
        cur.execute(q._get_all_users)
        _result = cur.fetchall()
        _result_to_json = _resultsService.parse(_result)
        self.render("testInsert.html", result=_result_to_json)
        cur.close()
        conn.close()

class deleteUserHandler(tornado.web.RequestHandler):
    def post(self):
# Region Set Up
        _resultsService = ResultsService()
        _q = Queries()
        _connector = Connector()
        conn = _connector.connect()
        cur = conn.cursor()
 
# endregion

# Region Main Block
        cur.execute(_q._get_all_users)
        _result = cur.fetchall()
        _result_to_json = _resultsService.parse(_result)

        
        for item in _result:
            _rID = str(item[3])
            _id = self.get_arguments("_checkbox")
            if _rID in _id:
                print("Deleting "+str(item[0]))
                cur.execute(_q._delete_user,(item[3],))
                conn.commit()


        cur.close()
        conn.close()
        self.redirect("/users")

class insertUserHandler(tornado.web.RequestHandler):
    def get(self):
        # create connection to postgres database
        _connector = Connector()
        conn = _connector.connect()

        # create cursor
        cur = conn.cursor()
        cur.execute("select firstname, lastname, created_on::VARCHAR(255) from public.users LIMIT(100)")
        _result = cur.fetchall()
        self.render("testInsert.html",result=_result)
    
    def post(self):
# Region Set Up
        
        #create resultService object
        _resultsService = ResultsService()
        #load queries
        q= Queries()
        # create connection to postgres database
        _connector = Connector()
        conn = _connector.connect()

        # create cursor
        cur = conn.cursor()

        #define query parameters
        _firstname = self.get_argument("_firstname_field")
        _lastname = self.get_argument("_lastname_field")
        _timenow = datetime.datetime.now()

# endregion
        #main block 
        
        _query = q._get_all_users
        cur.execute(_query)
        _result = cur.fetchall()
        _result_to_json = _resultsService.parse(_result)

        _query = q._create_new_user
        cur.execute(_query,(_firstname,_lastname,_timenow))
        conn.commit()

        cur.close()
        conn.close
        self.redirect("/users")


class ShipClassHandler(tornado.web.RequestHandler):
    def get(self):
        _q = Queries()
        _resultsService = ResultsService()
        # create connection to postgres database
        _connector = Connector()
        conn = _connector.connect()

        # create cursor
        cur = conn.cursor()
        cur.execute(_q._get_all_ship_classes)
        _result = cur.fetchall()
        _result_to_json = _resultsService.parse(_result)
        self.render("shipClass.html",result=_result)
    
    def post(self):
# Region Set Up
        
        #create resultService object
        _resultsService = ResultsService()
        #load queries
        q= Queries()
        # create connection to postgres database
        _connector = Connector()
        conn = _connector.connect()

        # create cursor
        cur = conn.cursor()

        #define query parameters
        _firstname = self.get_argument("_firstname_field")
        _lastname = self.get_argument("_lastname_field")
        _timenow = datetime.datetime.now()

# endregion
        #main block 
        
        _query = q._get_all_users
        cur.execute(_query)
        _result = cur.fetchall()
        _result_to_json = _resultsService.parse(_result)

        _query = q._create_new_user
        cur.execute(_query,(_firstname,_lastname,_timenow))
        conn.commit()

        cur.close()
        conn.close
        self.redirect("/users")