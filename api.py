import pymysql
from app import app
from db_config import mysql
from flask import jsonify
from flask import request


@app.route('/POST_endpoint', methods=['POST'])
def POST_endpoint_function():
    try:
        _json = request.json
        _param1 = _json['param1']
        _param2 = _json['param2']

        if _param1 and _param2 and request.method == 'POST':
            # insert record in database
            sqlQuery = "INSERT INTO table_name(param1,param2) VALUES(%s, %s)"
            data = (_param1, _param2)
            conn = mysql.connect()
            cursor = conn.cursor()
            cursor.execute(sqlQuery, data)
            conn.commit()
            res = jsonify('Value inserted successfully.')
            res.status_code = 200
            return res
        else:
            return not_found()

    except Exception as e:
        print(e)

    finally:
        cursor.close()
        conn.close()


@app.route('/GET_endpoint', methods=['GET'])
def get_endpoint_function():
    try:
        conn = mysql.connect()
        cursor = conn.cursor(pymysql.cursors.DictCursor)
        cursor.execute("{SELECT QUERY GOES HERE}")
        rows = cursor.fetchall()
        res = jsonify(rows)
        res.status_code = 200
        return res

    except Exception as e:
        print(e)

    finally:
        cursor.close()
        conn.close()


@app.errorhandler(404)
def not_found(error=None):
    message = {
        'status': 404,
        'message': 'There is no record: ' + request.url,
    }
    res = jsonify(message)
    res.status_code = 404
    return res


if __name__ == "__main__":
    app.run()
