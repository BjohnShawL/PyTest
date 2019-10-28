import psycopg2
import psycopg2.extras
import json


class Connector(object):
    _host =''
    _database='' 
    _user =''
    _password='' 

    def __init__(self):    
        with open('pgdbconfig.json') as config_file:
            data = json.load(config_file)

            pgconfig = data['postgres']
            Connector._host = pgconfig['host']
            Connector._database = pgconfig['database']
            Connector._user = pgconfig['user']
            Connector._password = pgconfig['password']

    def connect(self):
        conn = psycopg2.connect(
            host=self._host,
            database=self._database,
            user=self._user,
            password=self._password
        )
        return conn
