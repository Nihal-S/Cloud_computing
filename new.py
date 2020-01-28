from flask import Flask, render_template, request
import json
import sqlite3
app = Flask(__name__)

#8
@app.route('/api/v1/db/write', methods=['POST'])
def write_db():
    conn = sqlite3.connect('Rideshare.db')
    c = conn.cursor()
    data = request.json['insert']
    column = request.json['column']
    #return column
    table = request.json['table']
    #return table
    query = "INSERT INTO "+table+" ("+column+") "+"VALUES ("+data+")"
    #return query
    c.execute(query)
    conn.commit()
    conn.close()
    return '201'

#9
@app.route('/api/v1/db/read', methods=['POST'])
def read():
    conn = sqlite3.connect('Rideshare.db')
    c = conn.cursor()
    table = request.json['table']
    columns = request.json['columns']
    where = request.json['where']
    query = "SELECT "+columns+" FROM "+table+" WHERE "+where
    #return query
    c.execute(query)
    rows = c.fetchall()
    conn.commit()
    conn.close()
    return str(rows)
 


if __name__ == '__main__':
    app.run()
