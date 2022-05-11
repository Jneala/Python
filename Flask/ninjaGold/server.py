from crypt import methods
from random import Random, random, randrange
from flask import Flask, redirect, render_template, session, request
app = Flask(__name__)
app.secret_key = "no gold for you"

@app.route('/')
def index():
    if not 'your_gold' in session:
        session['your_gold'] = 0
        session['activities'] = []
        session['count'] = 0
    return render_template('/index.html')
@app.route('/reset')
def reset():
    session.clear()
    return redirect('/')
@app.route('/won')
def won():
        you_won = "<h2>You Won! Play Again!</h2>"
        reset = "<input type='submit' value='Reset' id='reset'>"
        return render_template('/index.html', you_won = you_won, reset = reset)
@app.route('/lost')
def lost():
        you_won = "<h2 style='color: red'>You Lost! Play Again!</h2>"
        reset = "<input type='submit' value='Reset' id='reset'>"
        return render_template('/index.html', you_won = you_won, reset = reset)

@app.route('/process', methods=['POST'])
def process():

    if request.form['building'] == 'farm':
        num = randrange(-2, 10)
        session['your_gold'] += num
        session['activities'] += ["You found " + str(num) + " on the farm!"]
        session['count'] += 1
    if request.form['building'] == 'cave':
        num = randrange(-15, 30)
        session['your_gold'] += num
        session['activities'] += ["You found " + str(num) + " around the cave!"]
        session['count'] += 1
    if request.form['building'] == 'house':
        num = randrange(-5, 15)
        session['your_gold'] += num
        session['activities'] += ["You found " + str(num) + " in the house!"]
        session['count'] += 1
    if request.form['building'] == 'casino':
        num = randrange(-50, 50)
        session['your_gold'] += num
        session['activities'] += ["You found " + str(num) + " at the casino!"]
        session['count'] += 1
    if session['count'] >= 15:
        return redirect('/lost')
    if session['your_gold'] >= 50:
        return redirect('/won')
    return redirect('/')
if __name__ == '__main__':
    app.run(debug=True)