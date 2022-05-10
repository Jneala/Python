from flask import Flask, render_template, request
app = Flask(__name__)

@app.route('/')
def index():
    db_users = [
        {"first_name":"Jonathon", "last_name": "Alsum", "email":"jon@pudding.com"},
        {"first_name":"Bob", "last_name": "Bee", "email":"bob@pudding.com"},
        {"first_name":"Tim", "last_name": "Mee", "email":"tim@pudding.com"},
        {"first_name":"Mr", "last_name": "Nibbles", "email":"mr@pudding.com"},
    ]
    return render_template("index.html", users = db_users)


if __name__ == "__main__":
    app.run(debug=True)