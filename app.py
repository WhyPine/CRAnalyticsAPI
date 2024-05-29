from flask import Flask, jsonify, request
import psycopg2
import os



ENV_VARS = os.environ.get("DATABASE_CONNECTION_STRING")
PARAMS = {pair.split('=')[0]: pair.split('=')[1] for pair in ENV_VARS.split(' ')}
print(ENV_VARS)

DB_USER=PARAMS['user']
DB_PASS=PARAMS['password']
DB_HOST=PARAMS['host']
DB_NAME=PARAMS['dbname']

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