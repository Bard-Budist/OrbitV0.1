#!/usr/bin/python3
from Web_Server.app import app
from Web_Server.connection import mysql
from flask import jsonify
from flask import flash, request
import pymysql


@app.route('/user')
def user():
    try:
        con=mysql.connect()
        cur = con.cursor(pymysql.cursors.DictCursor)
        cur.execute('SELECT * from user')
        row=cur.fetchall()
        resp=jsonify(row)
        return resp
    except expression as identifier:
        return("Error "  + identifier)
    finally:
        cur.close()
        con.close()
