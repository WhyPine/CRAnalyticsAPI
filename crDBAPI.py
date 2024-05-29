from flask import Flask, jsonify, request
import psycopg2
import os

conn_str = os.environ['AZURE_POSTGRESQL_CONNECTIONSTRING']
conn_str_params = {pair.split('=')[0]: pair.split('=')[1] for pair in conn_str.split(' ')}

DATABASE_URI = 'postgresql+psycopg2://{dbuser}:{dbpass}@{dbhost}/{dbname}'.format(
    dbuser=conn_str_params['user'],
    dbpass=conn_str_params['password'],
    dbhost=conn_str_params['host'],
    dbname=conn_str_params['dbname']
)

DB_USER=conn_str_params['user']
DB_PASS=conn_str_params['password']
DB_HOST=conn_str_params['host']
DB_NAME=conn_str_params['dbname']

conn = psycopg2.connect(
    dbname=DB_NAME,
    user=DB_USER,
    password=DB_PASS,
    host=DB_HOST
)
cursor = conn.cursor()

app = Flask(__name__)


@app.route(('/shows'), methods=['GET'])
def getShows():
    cursor.execute("SELECT title FROM SHOWS;")
    titles = cursor.fetchall()
    return jsonify(titles)