from flask import Flask
from flask.helpers import send_from_directory
import os

app = Flask(__name__, static_url_path='', static_folder='.')
app.config['CORS_HEADERS'] = 'Content-Type'

# CORS section


@app.after_request
def after_request_func(response):
    response.headers.add("Access-Control-Allow-Origin", "*")
    response.headers.add('Access-Control-Allow-Headers', "*")
    response.headers.add('Access-Control-Allow-Methods', "*")
    return response
# end CORS section


import error_handles

# Add your API endpoints here
from routes import mail
# from routes import cars
# ...


@app.route('/')
def get_endpoint_function():
    try:
        res = "<h1 style='position: fixed; top: 50%;  left: 50%; transform: translate(-50%, -50%);'>FLASK API HOME</h1>"
        return res

    except Exception as e:
        print(e)


# Setting Favicon
@app.route('/favicon.ico')
def favicon():
    return send_from_directory(os.path.join(app.root_path, 'static'),
                               'favicon.ico', mimetype='image/vnd.microsoft.icon')


if __name__ == "__main__":
    app.run(debug=True)
