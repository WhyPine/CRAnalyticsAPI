from flask import Flask, jsonify, request
import psycopg2

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