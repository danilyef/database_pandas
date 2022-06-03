# database_pandas
Package for working with databases in Python, based on pandas and sqlalchemy.

### Details
This package is created for:
1. Connection simplification between database and python(mostly jupyter notebook)
2. More convinient way for select and insert statements

Package is based on sqlaclhemy and pandas.

### Functionality: 

Right now consists of 1 class only(for MySQL database):

You can import class the following way: 
```python
from database_pandas import MySQLDatabase
```

MySQLDatabase class consists of the following arguments(user-defined):
1. database - schema name.
2. drivername - in this cas mysql.
3. username - username of the database.
4. password - password to the database.
5. host - host of the database.

MySQLDatabase class consists of following functions:
1. get_url - retrieves back connection string to your database.
2. connect_database - connects to your database.
3. disconnect_database - disconnects to your database.
4. select_sql - runs sql statement.
5. insert_sql - isnert pandas dataframe into user-defined table.
6. get_tables_regex - gets tables in the schema based on the (optional)regex expression.

for more detailed information look use name_of_function.__doc__


### Example:

**Initialisation and data base connection:**

```python
from database_pandas import MySQLDatabase
your_database = MySQLDatabase(database = database_name,drivername = 'mysql',username = db_username,password = db_password,host = db_host)
your_database.connect_database()
```

**Performing select * from:**
```python
your_database.select_sql('select * from table')
```

**Performing insert into table:**

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

```python
your_database.insert_sql(data_frame,'table_name',if_exists = 'replace')
```

**Get list of tables in schema**

**kwargs argument allow you to put as many where operation in select statement as possible.
But you have to define where operators(like 'and'/'or')with numbers. For example 'and' operator will be 'and1' or operator will
be 'or1'.

Example: 

```python
tables = your_database.get_tables_regex(and1 = 'some_regex',and2 = 'some_regex')
```