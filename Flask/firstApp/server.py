from crypt import methods
from flask import Flask, render_template, request
app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")
@app.route("/users")
def users():
    db_users = [
        {"first_name":"Jonathon", "last_name": "Alsum", "email":"jon@pudding.com"},
        {"first_name":"Bob", "last_name": "Bee", "email":"bob@pudding.com"},
        {"first_name":"Tim", "last_name": "Mee", "email":"tim@pudding.com"},
        {"first_name":"Mr", "last_name": "Nibbles", "email":"mr@pudding.com"},
    ]
    return render_template("users.html", users = db_users)

@app.route("/others")
def others():
    db_users = [
        {"first_name":"This", "last_name": "Guy", "email":"this@pudding.com"},
        {"first_name":"That", "last_name": "Girl", "email":"that@pudding.com"},
    ]
    return render_template("users.html", users = db_users)

@app.route("/add/user")
def add_user():
    return render_template("add_user.html")

@app.route("/create/user", methods=['POST'])
def create_user():
    print (request.form['first_name'])
    print (request.form['last_name'])
    print (request.form['email'])


if __name__ == "__main__":
    app.run(debug=True)