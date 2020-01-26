from flask import Flask
from flask.ext.mysqldb import MySQL
import json
app = Flask(__name__)
app.config['MYSQL_HOST'] = '127.0.0.1'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'password'
app.config['MYSQL_DB'] = 'Areaname'
mysql = MySQL(app)

@app.route('/hello')
def index():
   cur = mysql.connection.cursor()
   cur.execute('''SELECT * FROM Areaname ''')
   row_headers=[x[0] for x in cur.description] #this will extract row headers
   rv = cur.fetchall()
   json_data=[]
   for result in rv:
        json_data.append(dict(zip(row_headers,result)))
   return json.dumps(json_data)

if __name__ == '__main__':
   app.run(debug=True)