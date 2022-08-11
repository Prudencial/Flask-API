from crypt import methods
from app.database import query_data, store_data

from flask import render_template, redirect, url_for, jsonify, request
from app import app

# route simply states how to interact with our db #
@app.route('/index')
def index():
    return "Hello, World"


@app.route('/Products', methods=['GET', 'POST'])
def Product():
    
    if request.method == "GET":
        sql = "SELECT * FROM Products"
        q_data = query_data(sql, ())
        return jsonify(q_data)

    elif request.method == "POST":
        r_data = request.get_json()
        sql = "INSERT INTO Products (Suppliers) VALUES(%s)"
        params = (r_data["Suppliers"],)
        store_data(sql, params)
        return jsonify({"status": "success"})
    
    return jsonify({"status": "failed"})


@app.route('/Products/<id>', methods=['PUT', 'PATCH'])
def updateTodo(id):
    if request.method == "PUT":
        sql = "UPDATE Products SET Suppliers=%s WHERE id=%s"
        # get the request data
        r_data = request.get_json()
        params = (r_data["Suppliers"], id, )
        store_data(sql, params)

        return jsonify({"status": "success"})

