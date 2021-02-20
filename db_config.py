from app import app
from flask.ext.mysql import MySQL
mysql = MySQL()

# MySQL configurations
app.config['MYSQL_DATABASE_USER'] = ""
app.config['MYSQL_DATABASE_PASSWORD'] = ""
app.config['MYSQL_DATABASE_DB'] = ""
app.config['MYSQL_DATABASE_HOST'] = ""
mysql.init_app(app)
