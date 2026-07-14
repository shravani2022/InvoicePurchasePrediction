import pymysql
from configure import *

def mysqlconnection():
    return pymysql.connect(
        host = MYSQL_HOST,
        user= MYSQL_USER,
        password = MYSQL_PASSWORD,
        database = MYSQL_DB,
        cursorclass=pymysql.cursors.DictCursor
    )