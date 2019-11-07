import psycopg2
import psycopg2.extras
import json


class Connector(object):
    _data=''
    _host =''
    _database='' 
    _user =''
    _password=''
    _sslmode = '' 

    

    def __init__(self):    
        with open('pgdbconfig.json') as config_file:
            Connector._data = json.load(config_file)
            
            

    def connect(self, arg):
        self.switch(arg)
        conn = psycopg2.connect(
            host=self._host,
            dbname=self._database,
            user=self._user,
            password=self._password,
            sslmode=self._sslmode

        )
        return conn

    def PyTestConnect(self):
        pgconfig = Connector._data['local']
        Connector._host = pgconfig['host']
        Connector._database = pgconfig['database']
        Connector._user = pgconfig['user']
        Connector._password = pgconfig['password']
        Connector._sslmode = 'allow'
    
    def MonitoringConnect(self):
        pgconfig = Connector._data['monitor']
        Connector._host = pgconfig['host']
        Connector._database = pgconfig['database']
        Connector._user = pgconfig['user']
        Connector._password = pgconfig['password']
        Connector._sslmode = pgconfig['sslmode']
    
    switcher = {
            1: 'Monitoring',
            2: 'PyTest'
        }

    def switch(self, arg):
        
        self.x = self.switcher[arg]

        return getattr(self, self.x +'Connect')()

        # print(self.switcher.values())
        # print(self.switcher.keys())
        # print(self.switcher.values().index(1))
        # #return self.switcher.values().index(arg)
        # return self.switcher.get(arg)()
        