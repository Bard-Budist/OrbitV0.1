#!/usr/bin/python3
from flask import jsonify
from Web_Server.app import app
from flaskext.mysql import MySQL

mysql = MySQL()

app.config['MYSQL_DATABASE_USER'] = 'root'
app.config['MYSQL_DATABASE_PASSWORD'] = ''
app.config['MYSQL_DATABASE_DB'] = 'orbit_agent'
app.config['MYSQL_DATABASE_HOST'] = 'localhost'
mysql.init_app(app)
