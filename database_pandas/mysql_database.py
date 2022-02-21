import numpy as np
from sqlalchemy.engine.url import URL
import pandas as pd
from sqlalchemy import create_engine


#2.Database class

class MySQLDatabase:
    def __init__(self,database,drivername,username,password,host):
        self.database = database
        self.drivername = drivername
        self.username = username
        self.password = password
        self.host = host
        self.query = {'charset': 'utf8'}
        

    def get_url(self):
        self.url = URL(**
        {
            'database': self.database,
            'drivername': self.drivername,
            'username': self.username,
            'password': self.password,
            'host': self.host,
            'query': self.query
        }
        )
        return self.url
        
    
    def connect_database(self):
        url = self.get_url()
        self.engine = create_engine(url, encoding="utf8")
        return self.engine
    
    def disconnect_database(self):
        self.engine.dispose()
        
        
    def select_sql(self,sql_statement):
        sql_execution = pd.read_sql(sql_statement,self.engine)
        return sql_execution
    
    def insert_sql(self,data_frame,sql_table,if_exists = 'append',index = False):
        data_frame.to_sql(name = sql_table,con = self.engine,if_exists = if_exists,index = index)
    
    
    def get_tables_regex(self,**kwargs):
        sql_statement = '''
            select table_name from information_schema.tables
            where table_schema = '{0}'
        '''.format(self.database)
        
        if len(kwargs.items()) !=0:
            for operator,regex in kwargs.items():
                #delete numbers from string operator
                operator = ''.join([i for i in operator if not i.isdigit()])
                sql_statement += ' ' + operator + " table_name regexp '" + regex + "'"

        tables = pd.read_sql(sql_statement,self.engine)      
        tables = tables.iloc[:,0].to_numpy()
        
        return tables