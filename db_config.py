from app import app
from flask.ext.mysql import MySQL
mysql = MySQL()

# MySQL configurations
app.config['MYSQL_DATABASE_USER'] = "root"
app.config['MYSQL_DATABASE_PASSWORD'] = ""
app.config['MYSQL_DATABASE_DB'] = "employees"
app.config['MYSQL_DATABASE_HOST'] = "127.0.0.1"
mysql.init_app(app)