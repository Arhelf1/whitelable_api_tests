import pyodbc
from sql.config import conn_string


def connect_db():
    conn = ''
    try:
        conn = pyodbc.connect(conn_string)
        return conn.cursor()
    except pyodbc.Error:
        print('Connection create error.')
        conn.close()


def run_sql(cursor, query, query_parameter):
    try:
        cursor.execute(query, query_parameter)
        return cursor.fetchall()
    except pyodbc.Error:
        print('Sql exec error.')
        cursor.close()
