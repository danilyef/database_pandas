"""
This package is created for:
1. Connection simplification between database and python(mostly jupyter notebook)
2. More convinient way for select and insert statements

Package is based on sqlaclhemy and pandas.

Functionality: 

Right now consists of 1 class only(for MySQL database):

You can import class the following way: 
from database_pandas import MySQLDatabase

MySQLDatabase class consists of the following arguments(user-defined)
1.database - schema name.
2.drivername - in this cas mysql.
3.username - username of the database.
4.password - password to the database.
5.host - host of the database.

MySQLDatabase class consists of following functions:
1. get_url - retrieves back connection string to your database.
2. connect_database - connects to your database.
3. disconnect_database - disconnects to your database.
4. select_sql - runs sql statement.
5. insert_sql - isnert pandas dataframe into user-defined table.
6. get_tables_regex - gets tables in the schema based on the (optional)regex expression.

for more detailed information look use name_of_function.__doc__

"""




import numpy as np
from sqlalchemy.engine.url import URL
import pandas as pd
from sqlalchemy import create_engine


#2.Database class

class MySQLDatabase:
    """
    MySQLDatabase class consists of the following arguments(user-defined)
    1.database - schema name.
    2.drivername - in this cas mysql.
    3.username - username of the database.
    4.password - password to the database.
    5.host - host of the database.
    """
    def __init__(self,database,drivername,username,password,host):
        self.database = database
        self.drivername = drivername
        self.username = username
        self.password = password
        self.host = host
        self.query = {'charset': 'utf8'}
        

    def get_url(self):
        """
        Retrieves url to your database.
        Example: 
        from database_pandas import MySQLDatabase
        your_database = MySQLDatabase(your_arguments)
        your_database.get_url()

        """
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
        """
        connects to database
        Example: 
        from database_pandas import MySQLDatabase
        your_database = MySQLDatabase(your_arguments)
        your_database.connect_database()

        """
        url = self.get_url()
        self.engine = create_engine(url, encoding="utf8")
        return self.engine
    
    def disconnect_database(self):
        """
        disconnects to database
        Example: 
        from database_pandas import MySQLDatabase
        your_database = MySQLDatabase(your_arguments)
        your_database.disconnect_database()

        """
        self.engine.dispose()
        
        
    def select_sql(self,sql_statement):
        """
        Executes select statement
        Example: 
        from database_pandas import MySQLDatabase
        your_database = MySQLDatabase(your_arguments)
        your_database.select_sql('select * from table')
        """
        sql_execution = pd.read_sql(sql_statement,self.engine)
        return sql_execution
    
    def insert_sql(self,data_frame,sql_table,if_exists = 'append',index = False):
        """
        Executes insert statement into user-defined table
        Function consists of the following arguments:
        
        1.data_frame - which dataframe to insert.
        2.sql_table - in which table to insert.
        3.if_exists(default = 'append'):
        
        possible values: ‘fail’, ‘replace’, ‘append’}
        How to behave if the table already exists.
        - fail: Raise a ValueError.
        - replace: Drop the table before inserting new values.
        - append: Insert new values to the existing table.

        4.index - Write DataFrame index as a column. 


        Example: 
        from database_pandas import MySQLDatabase
        your_database = MySQLDatabase(your_arguments)
        your_database.insert_sql(data_frame,'table_name')
        """


        data_frame.to_sql(name = sql_table,con = self.engine,if_exists = if_exists,index = index)
    
    
    def get_tables_regex(self,**kwargs):
        """
        Get list of tables in the schema(using select statement from information schema)
        **kwargs argument allow you to put as many where operation in select statement as possible.
        But you have to define where operators(like 'and'/'or')with numbers. For example 'and' operator will be 'and1' or operator will
        be 'or1'.

        Example: 
        from database_pandas import MySQLDatabase
        your_database = MySQLDatabase(your_arguments)
        tables = your_database.get_tables_regex(and1 = 'some_regex',and2 = 'some_regex')

        """
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