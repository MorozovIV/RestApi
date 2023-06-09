# app.py
# https://pythonist.ru/rest-api-na-python-s-flask-connexion-i-sqlalchemy-chast-1/
# https://realpython.com/flask-connexion-rest-api/
# https://translated.turbopages.org/proxy_u/en-ru.ru.102065f8-64831568-40e46fac-74722d776562/https/www.geeksforgeeks.org/python-build-a-rest-api-using-flask/
# https://translated.turbopages.org/proxy_u/en-ru.ru.102065f8-64831568-40e46fac-74722d776562/https/www.geeksforgeeks.org/how-to-build-a-web-app-using-flask-and-sqlite-in-python/
# https://translated.turbopages.org/proxy_u/en-ru.ru.102065f8-64831568-40e46fac-74722d776562/https/www.geeksforgeeks.org/connect-flask-to-a-database-with-flask-sqlalchemy/
from flask import render_template # Remove: import Flask
import connexion
app = connexion.App(__name__, specification_dir="./")
app.add_api("swagger.yml")
@app.route("/")
def home():
    return render_template("home.html")
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000, debug=True)