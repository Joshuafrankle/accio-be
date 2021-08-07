from __future__ import print_function
from app import app

# MySQL imports
from flaskext.mysql import MySQL
from pymysql.cursors import DictCursor



# Send In Blue SMTP Imports
import sib_api_v3_sdk


# Rows from cursors will always be of type dict || cursorclass=DictCursor
mysql = MySQL(cursorclass=DictCursor)

# MySQL configurations and Init
app.config['MYSQL_DATABASE_USER'] = "tux"
app.config['MYSQL_DATABASE_PASSWORD'] = "licet@123"
app.config['MYSQL_DATABASE_DB'] = "stretch"
app.config['MYSQL_DATABASE_HOST'] = "opencloud.pattarai.in"
app.config['MYSQL_DATABASE_PORT'] = 8306
mysql.init_app(app)


# Default Admin Account Profile Pic
adminProfilePic='https://i.ibb.co/wzxcjL1/89220ce13495803921f570b7bf95426f.jpg'

# Default Admin password
defaultAdminPassword = "stretch@123"


# SendInBlue Config and Init
mail_config = sib_api_v3_sdk.Configuration()
mail_config.api_key['api-key'] = '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'

# Uncomment below lines to configure API key authorization using: partner-key
# configuration = sib_api_v3_sdk.Configuration()
# configuration.api_key['partner-key'] = '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'