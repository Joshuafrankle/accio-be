from app import app


# MySQL imports
from flaskext.mysql import MySQL
from pymysql.cursors import DictCursor

# Rows from cursors will always be of type dict || cursorclass=DictCursor
mysql = MySQL(cursorclass=DictCursor)

# MySQL configurations
app.config['MYSQL_DATABASE_USER'] = ""
app.config['MYSQL_DATABASE_PASSWORD'] = ""
app.config['MYSQL_DATABASE_DB'] = ""
app.config['MYSQL_DATABASE_HOST'] = ""
mysql.init_app(app)
