from flask import Flask
from flask_restful import Api, Resource
import current_time
import sqlite3

app = Flask(__name__)
api = Api()
current_time.time()
conn = sqlite3.connect('bd')
# conn = psycopg2.connect( host=hostname, user=username, password=password, dbname=database //РostgreSQL
cursor = conn.cursor()
cursor.execute("insert into Artist values (Null, 'A Aagrh!') ")

class Main(Resource):
    def get(self):
        return {'info': "Some info", "num": 56, "current_time": current_time.time()}

api.add_resource(Main, "/api/main")
api.init_app(app)

conn.close()
if __name__== "__main__":
    app.run(debug=True, port=3000, host="127.0.0.1")