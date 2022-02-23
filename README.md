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
