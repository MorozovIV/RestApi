# app.py
# https://pythonist.ru/rest-api-na-python-s-flask-connexion-i-sqlalchemy-chast-1/
# https://realpython.com/flask-connexion-rest-api/
from flask import render_template # Remove: import Flask
import connexion
app = connexion.App(__name__, specification_dir="./")
app.add_api("swagger.yml")
@app.route("/")
def home():
    return render_template("home.html")
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000, debug=True)