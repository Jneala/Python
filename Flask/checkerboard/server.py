from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/")
def index():
    
    return render_template('index.html', across = 8, down = 8)
    
@app.route("/<num>")
def oneInt(num):
    return render_template('index.html', across = 8, down = int(num))

@app.route("/<x>/<y>")
def twoInt(x,y):
    return render_template('index.html', across = int(x), down = int(y))

@app.route("/<x>/<y>/<col1>/<col2>")
def twoIntColor(x,y,col1,col2):
    return render_template('index.html', across = int(x), down = int(y), col1 = col1, col2 = col2)


if __name__ == "__main__":
    app.run(debug=True)