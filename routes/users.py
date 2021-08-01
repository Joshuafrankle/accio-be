import pymysql
from app import app, forbidden
from config import mysql
from flask import jsonify, request


@app.route('/users', methods=['POST', 'GET'])
def insert_cars():
    try:
        _form = request.form
        _name = _form['name']
        _email = _form['email']

        if _name and _email and request.method == 'POST':
            # insert record in database
            conn = mysql.connect()
            cursor = conn.cursor()
            cursor.execute(
                f"INSERT INTO users(name,email) VALUES({_name}, {_email})")
            conn.commit()
            cursor.close()
            conn.close()
            res = jsonify('success')
            res.status_code = 200
            return res

        elif request.method == 'GET':
            # Get record in database
            _email = request.args["email"]
            conn = mysql.connect()
            cursor = conn.cursor()
            cursor.execute(
                f"SELECT * FROM `users` WHERE email='{_email}'")
            res = cursor.fetchall()
            cursor.close()
            conn.close()
            res.status_code = 200
            return jsonify(res)

        else:
            return forbidden()

    except Exception as e:
        print(e)
