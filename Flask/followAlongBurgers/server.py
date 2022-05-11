from flask import Flask, redirect, render_template, request, session
app = Flask(__name__)
app.secret_key = "you know what I mean"

@app.route('/')
def index():
    session.clear()
    return render_template('/index.html')


@app.route('/display')
def display():
    if "buns" not in session:
        return redirect('/')
    lunch = {
        "buns" : session['buns'],
        "meats" : session['meats'],
        "veggies" : session['veggies'],
        "sauces" : session['sauces'],
        "calories" : session['calories']
    }
    return render_template('/display.html', burger = lunch)

@app.route('/process', methods=['POST'])
def process():
    session['buns'] = request.form['buns']
    session['meats'] = request.form['meats']
    session['veggies'] = request.form['veggies']
    session['sauces'] = request.form['sauces']
    session['calories'] = request.form['calories']
    return redirect('/display')

if __name__ == "__main__":
    app.run(debug=True)