from typing import List, Dict
import mysql.connector
import simplejson as json
from flask import Flask, Response
import sqlite3

app = Flask(__name__)


def cities_import() -> List[Dict]:
    config = {
        'user': 'afu2',
        'password': 'root',
        # 'host': 'db',
        'host': '127.0.0.1',
        'port': '3306',
        'database': 'citiesData'
    }
    connection = mysql.connector.connect(**config)
    cursor = connection.cursor(dictionary=True)
    # connection = sqlite3.connect(r"C:\Users\Admin\PycharmProjects\PythonDockerFlaskPycharm\db\init.sql")
    # cursor = connection.cursor(dictionary=True)

    cursor.execute('SELECT * FROM tblCitiesImport')
    result = cursor.fetchall()

    cursor.close()
    connection.close()

    return result


@app.route('/')
def index() -> str:
    js = json.dumps(cities_import())
    resp = Response(js, status=200, mimetype='application/json')
    return resp


if __name__ == "__main__":
    # app.run(host='0.0.0.0')
    app.run(host='0.0.0.0', port=5000)
