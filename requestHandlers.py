import tornado.web
import tornado.ioloop
import psycopg2
import psycopg2.extras
import json
import datetime

from connector import Connector
from resultsService import ResultsService
from queries import Queries
from Models.timesheetModel import *

class rootRequestHandler(tornado.web.RequestHandler):
    def get(self):
        self.render("index.html")
        conn = Connector()
        session = conn.r_connect()
        test = session.query(object_type=Timesheet).where_in("NumericID",[1800,1799])
        for ts in test:
            print(ts.tsStatus)
        

class allUsersHandler(tornado.web.RequestHandler):
    def get(self):
# Region Set Up
        #create resultService object
        _resultsService = ResultsService()
        q= Queries()

        # create connection to postgres database
        _connector = Connector()
        conn = _connector.connect(2)

        # create cursor
        cur = conn.cursor()
# endregion
# Region Main Block
        cur.execute(q._get_all_users)
        _result = cur.fetchall()
        _result_to_json = _resultsService.parse(_result)
        self.render("testInsert.html", result=_result_to_json)
        cur.close()
        conn.close()
# endregion
class deleteUserHandler(tornado.web.RequestHandler):
    def post(self):
# Region Set Up
        _resultsService = ResultsService()
        _q = Queries()
        _connector = Connector()
        conn = _connector.connect(2)
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
# endregion
class insertUserHandler(tornado.web.RequestHandler):
    def get(self):
        # create connection to postgres database
        _connector = Connector()
        conn = _connector.connect(2)

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
        conn = _connector.connect(2)

        # create cursor
        cur = conn.cursor()

        #define query parameters
        _firstname = self.get_argument("_firstname_field")
        _lastname = self.get_argument("_lastname_field")
        _timenow = datetime.datetime.now()
# endregion
# Region main block 
        
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
# endregion

class ShipClassHandler(tornado.web.RequestHandler):
    def get(self):
        _q = Queries()
        _resultsService = ResultsService()
        # create connection to postgres database
        _connector = Connector()
        conn = _connector.connect(2)

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
        conn = _connector.connect(2)

        # create cursor
        cur = conn.cursor()

        #define query parameters
        _firstname = self.get_argument("_firstname_field")
        _lastname = self.get_argument("_lastname_field")
        _timenow = datetime.datetime.now()

# endregion
#Region main block 
        
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
# endregion

class EmailFailHandler(tornado.web.RequestHandler):
    def get(self):
        # create connection to postgres database
        
        self.render("emailMonitor.html")
    
    def post(self):
# Region Set Up
        
        #create resultService object
        _resultsService = ResultsService()
        #load queries
        q= Queries()
        # create connection to postgres database
        _connector = Connector()
        conn = _connector.connect(1)

        # create cursor
        cur = conn.cursor()

        #define query parameters
        _failID = self.get_argument("_failureId")
        
# endregion
# Region main block 
        
        
        cur.execute(q._email_failure,(_failID,))
        _result = cur.fetchall()
        _result_to_json = _resultsService.parse(_result)

        self.render("emailMonitor.html",results=_result)

        cur.close()
        conn.close
        
# endregion
    
