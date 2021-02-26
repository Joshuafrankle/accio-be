import pymysql
from app import app, forbidden
from db_config import mysql
from flask import jsonify, request


'''
@app.route('/POST_endpoint', methods=['POST'])
def POST_endpoint_function():
    try:
        _form = request.form
        _param1 = _form['param1']
        _param2 = _form['param2']

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
            return forbidden()

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

'''
