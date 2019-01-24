import pymysql.cursors
from flask import g
import urllib.parse

def connect_db():

    host='ls-fa436eab182b99c63f34a2f9f223d5b7d82e204b.cjonxsdsuo2r.us-east-2.rds.amazonaws.com'
    user='dbmasteruser'
    password=r'mERHoUS|YXWy|HSs1ckc#1PvM1vH124%'
    db = 'innodb'
    charset = 'utf8mb4'

    # print ("Connecting")

    return pymysql.connect(
        host=host,
        user=user,
        password=password,
        db=db,
        charset=charset
    )

def get_db():
    if not hasattr(g, 'connection'):
        g.connection = connect_db()
    return g.connection

def log_interested(Word, Interested):
    connection = get_db()
    with connection.cursor() as cursor:
        sql = """DELETE FROM Keywords WHERE Word=%s;"""
        print(Word)
        params = (Word)
        cursor.execute(sql, params)

        # sql = """DELETE FROM Keywords WHERE Word=%s;"""
        # print(urllib.parse.quote(Word))
        # params = (urllib.parse.quote(Word))
        # cursor.execute(sql, params)
    
        sql = """INSERT INTO Keywords (Word, Interested)
                VALUES (%s, %s)"""
        params = (Word, Interested)
        cursor.execute(sql, params)
    connection.commit()
    return Word

def log_keyword(Word):
    connection = get_db()
    with connection.cursor() as cursor:
        sql = """SELECT Word FROM Keywords WHERE Word=%s;"""
        params = (Word)
        cursor.execute(sql, params)
        if cursor.fetchone() is None:
            log_interested(Word, -1)

def get_interests():
    connection = get_db()
    with connection.cursor() as cursor:
        sql = """SELECT Word FROM Keywords WHERE Interested=1;"""
        cursor.execute(sql)
        return cursor.fetchall()

def get_keywords():
    connection = get_db()
    with connection.cursor() as cursor:
        sql = """SELECT Word, Interested from Keywords;"""
        cursor.execute(sql)
        return cursor.fetchall()

def get_unsorted():
    connection = get_db()
    with connection.cursor() as cursor:
        sql = """SELECT Word from Keywords WHERE Interested=-1;"""
        cursor.execute(sql)
        return cursor.fetchall()
