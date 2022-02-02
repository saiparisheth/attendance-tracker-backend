from flask import Flask, request, jsonify
import sqlite3
from flask_cors import CORS
from data import organize,givedata
import json
user={
    "username":"sai",
    "password":"monesh"
}
app = Flask(__name__)
CORS(app)
test= "{'name': 'sai', 'rollno': '69', 'apply': 'leave', 'nofhours': '3', 'startdate': '2021-09-14T18:30:00.000Z', 'enddate': '2021-09-15T18:30:00.000Z', 'reason': 'summa'}"
@app.route('/auth', methods=['PUT'])
def etho():
    data=request.get_json()
    if data == user:
        return user
    else:
        return 400
@app.route('/form', methods=['POST','GET'])
def forms():
    if request.method == 'POST':
        data = request.get_json()
        formvalue = data
        organize(formvalue)
        return "saved"
    if request.method == 'GET':
        val=givedata()
        res=[]
        for i in val:
            res.append(eval(i))
        return jsonify(res)


@app.route('/')
def home():
    return jsonify([("{'values': {'id': '2', 'name': 'MONESH'}}",), ("{'values': {'id': '2', 'name': 'MONESH'}}",)]             )

if __name__ == '__main__':
    app.run(debug=True)  # important to mention debug=True
