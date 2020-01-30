from flask import Flask, render_template, request
import json
import requests
import sqlite3
import string
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
    #return str(type(rows))
    conn.commit()
    conn.close()
    return json.dumps(rows)
 
def if_hex(s):
    try:
        int(s, 16)
        return True
    except ValueError:
        return False
# def if_hex(string):
#     f = all(c in string.hexdigits() for c in string)
#     return f
    # flag = 1
    # for i in string:
    #     #print(i.isdigit())
    #     if(i != 'a' or i != 'b' or i != 'c' or i != 'd' or i != 'e' or i != 'f' or (not i.isdigit())):
    #         print(i)
    #         return 0
    # return flag
@app.route('/api/v1/users', methods=['PUT'])
def add():
    try:
        name = request.json['name']
        password = request.json['password']
        insert = "'"+name+"','"+password+"'"
        names = requests.post('http://127.0.0.1:5000/api/v1/db/read', json={"table": "users","columns":"username","where":"username!='hdughuhuhfguihufdhuidhgfuhduhgiu'"})
        names = names.json()
        l = []
        for i in names:
            l.append(i[0])
        names = l
        if(len(password) == 40 and if_hex(password) and name not in names):
            r = requests.post('http://127.0.0.1:5000/api/v1/db/write', json={"insert": insert,"column":"username,password","table":"users"})
        else:
            return '400'
        return "201"
    except:
        return '500'



@app.route('/api/v1/users/<string:name>', methods=['DELETE'])
def delete(name):
    try:
        name = str(name)
        names = requests.post('http://127.0.0.1:5000/api/v1/db/read', json={"table": "users","columns":"username","where":"username!='hdughuhuhfguihufdhuidhgfuhduhgiu'"})
        names = names.json()
        l = []
        for i in names:
            l.append(i[0])
        names = l
        if(name in names):
            conn = sqlite3.connect('Rideshare.db')
            c = conn.cursor()
            c.execute("DELETE FROM users WHERE username="+"'"+name+"'")
            conn.commit()
            conn.close()
            return '201'
        else:
            return '400'
    except Exception as e:
        print(e)
        return '500'

@app.route('/api/v1/rides', methods=['POST'])
def create_ride():
    try:
        created_by = request.json['created_by']
        timestamp = request.json['timestamp']
        source = request.json['source']
        destination = request.json['destination']
        name = created_by
        names = requests.post('http://127.0.0.1:5000/api/v1/db/read', json={"table": "users","columns":"username","where":"username!='hdughuhuhfguihufdhuidhgfuhduhgiu'"})
        names = names.json()
        l = []
        for i in names:
            l.append(i[0])
        names = l
        if(name in names):
            insert = "'"+created_by+"',"+"'"+timestamp+"',"+"'"+source+"','"+destination+"'"
            print(insert)
            r = requests.post('http://127.0.0.1:5000/api/v1/db/write', json={"insert": insert,"column":"created_by,timestamp,source,destination","table":"ride"})
            return '201'
        else:
            return '400'
    except Exception as e:
        print(e)
        return '500'

@app.route('/api/v1/rides', methods=['GET'])
def upcoming_ride():
    try:
        if request.method == "GET":
            source = request.args.get('source')
            destination = request.args.get('destination')
            names = requests.post('http://127.0.0.1:5000/api/v1/db/read', json={"table": "ride","columns":"ride_id,created_by,timestamp","where":"source='"+source+"' and destination='"+destination+"'"})
            names = names.json()
            return str(names)
    except Exception as e:
        print(e)
        return '500'

@app.route('/api/v1/rides/<string:ride_id>', methods=['GET'])
def list_rides(ride_id):
    try:
        ride_id = str(ride_id)
        #print(ride_id)
        
        ride_ids = requests.post('http://127.0.0.1:5000/api/v1/db/read', json={"table": "ride","columns":"ride_id","where":"source!='hasdfuhuhasujdhjkh'"})
        ride_ids = ride_ids.json()

        l = []
        for i in ride_ids:
            l.append(str(i[0]))
        ride_ids = l
        print(ride_id)
        print(ride_ids)
        if(ride_id in ride_ids):
            result = requests.post('http://127.0.0.1:5000/api/v1/db/read', json={"table": "ride","columns":"ride_id,created_by,timestamp,source,destination","where":"ride_id='"+ride_id+"'"})
            result1 = requests.post('http://127.0.0.1:5000/api/v1/db/read', json={"table": "join_ride","columns":"username","where":"ride_id='"+ride_id+"'"})
            result1 = result1.json()
            result = result.json()
            return str(result+result1)
        else:
            return '400'
    except Exception as e:
        print(e)
        return '500'

@app.route('/api/v1/rides/<string:ride_id>', methods=['POST'])
def join_rides(ride_id):
    try:
        ride_id = str(ride_id)
        ride_ids = requests.post('http://127.0.0.1:5000/api/v1/db/read', json={"table": "ride","columns":"ride_id","where":"ride_id!='2341356'"})
        ride_ids = ride_ids.json()
        names = requests.post('http://127.0.0.1:5000/api/v1/db/read', json={"table":"users","columns":"username","where":"username!='sdjhfjsdhfjkhfjksdhfjksfhkjdshfjksdh'"})
        names = names.json()
        l = []
        for i in ride_ids:
            l.append(i[0])
        ride_ids = l
        l = []
        for i in names:
            l.append(i[0])
        names = l
        username = request.json['username']
        username = str(username)
        # print(username)
        # print(names)
        # print(type(ride_id))
        # print(ride_ids)
        if((username in names) and (int(ride_id) in ride_ids)):
            insert = "'"+ride_id+"','"+username+"'"
            requests.post('http://127.0.0.1:5000/api/v1/db/write', json={"insert": insert,"column":"ride_id,username","table":"join_ride"})
            return '201'
        else:
            return '400'
    except Exception as e:
        print(e)
        return '500'  


@app.route('/api/v1/rides/<string:ride_id>', methods=['DELETE'])
def delete_ride(ride_id):
    try:
        ride_id = str(ride_id)
        ride_ids = requests.post('http://127.0.0.1:5000/api/v1/db/read', json={"table": "ride","columns":"ride_id","where":"ride_id!='2341356'"})
        ride_ids = ride_ids.json()
        l = []
        for i in ride_ids:
            l.append(i[0])
        ride_ids = l
        print(ride_ids)
        print(ride_id)
        if(int(ride_id) in ride_ids):
            conn = sqlite3.connect('Rideshare.db')
            c = conn.cursor()
            query = "DELETE FROM ride WHERE ride_id='"+ride_id+"'"
            c.execute(query)
            conn.commit()
            conn.close()
            return '201'
        else:
            return '400'
    except Exception as e:
        print(e)
        return '500'

if __name__ == '__main__':
    app.run()
