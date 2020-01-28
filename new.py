from flask import Flask, render_template, request
import json
import requests
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
 
def if_hex(string):
    for i in string:
        if(i != 'a' or i != 'b' or i != 'c' or i != 'd' or i != 'e' or i != 'f' or not i.isDigit()):
            return 0
        else:
            return 1
@app.route('/api/v1/users', methods=['PUT'])
def add():
    name = request.json['name']
    password = request.json['password']
    insert = "'"+name+"','"+password+"'"
    #return insert
    names = requests.post('http://127.0.0.1:5000/api/v1/db/read', json={"table": "users","columns":"username","where":"username!='hdughuhuhfguihufdhuidhgfuhduhgiu'"})
    #return str(names)
    if(len(password) == 40 and if_hex(password) and name not in names):
        r = requests.post('http://127.0.0.1:5000/api/v1/db/write', json={"insert": insert,"column":"username,password","table":"users"})
    else:
        return '400'
    
    return "201"

if __name__ == '__main__':
    app.run()
