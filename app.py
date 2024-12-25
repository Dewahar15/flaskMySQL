from flask import Flask
from flaskext.mysql import MySQL

app = Flask (__name__)

ip="172.17.0.2"
user="dewa"
password="redhat"
dbname="newdb"

app.config['MYSQL_DATABASE_USER'] = user
app.config['MYSQL_DATABASE_HOST'] = ip
app.config['MYSQL_DATABASE_PASSWORD'] = password
app.config['MYSQL_DATABASE_DB'] = dbname

mysql = MySQL()

mysql.init_app(app)

@app.route("/data")
def lwdata():
    conn = mysql.connect()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM students")
    data = cursor.fetchall()
    return str(data)

app.run(host='0.0.0.0')
