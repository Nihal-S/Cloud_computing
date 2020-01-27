from flask import Flask, render_template, request
from flask_mysqldb import MySQL
import json
app = Flask(__name__)


app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'password'
app.config['MYSQL_DB'] = 'Areaname'

mysql = MySQL(app)


@app.route('/api/vi/users', methods=['PUT'])
def add():
	if request.method == "PUT":
		#details = request.json
		name = request.json['name']
		password = request.json['password']
		cur = mysql.connection.cursor()
		cur.execute("INSERT INTO users(name, password) VALUES (%s, %s)", (name, password))
		mysql.connection.commit()
		cur.close()
		return '201'

@app.route('/api/vi/users/<string:name>', methods=['DELETE'])
def delete(name):
	if request.method == "DELETE":
		#name = name.json
		#return name
		#return "DELETE FROM users WHERE name='{0}'".format(name)
		#return (name)
		name = str(name)
		cur = mysql.connection.cursor()
		cur.execute("DELETE FROM users WHERE name=%s",[name])
		mysql.connection.commit()
		cur.close()
		return '201'

@app.route('/api/vi/rides', methods=['POST'])
def create_ride():
	if request.method == "POST":
		created_by = request.json['created_by']
		created_by = created_by[1:-1]
		timestamp = request.json['timestamp']
		source = request.json['source']
		source = source[1:-1]
		destination = request.json['destination']
		destination = destination[1:-1]
		cur = mysql.connection.cursor()
		cur.execute("INSERT INTO rides(created_by, timestamp, source, destination) VALUES (%s, %s, %s, %s)", (created_by, timestamp, source, destination))
		mysql.connection.commit()
		cur.close()
		return '201'

@app.route('/api/vi/rides', methods=['GET'])
def upcoming_ride():
	if request.method == "GET":
		source = request.args.get('source')
		source = source[1:-1]
		destination = request.args.get('destination')
		#return str(source)+str(destination)
		destination = destination[1:-1]
		cur = mysql.connection.cursor()
		cur.execute("SELECT created_by,timestamp,ride_id FROM rides WHERE source='"+source+"' AND destination='"+destination+"'")
		rv = cur.fetchall()
		mysql.connection.commit()
		cur.close()
		#rv = (json.dumps(rv))
		return json.dumps(rv)

@app.route('/api/vi/rides/<string:ride_id>', methods=['POST'])
def join_ride(ride_id):
	if request.method == "POST":
		

if __name__ == '__main__':
    app.run()
