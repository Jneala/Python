from crypt import methods
from turtle import width
from unittest import result
from flask import Flask, render_template, session, request, redirect
import random

app = Flask(__name__)
app.secret_key = "guess again"

@app.route('/')
def index():
    session['randomNum'] = random.randint(1, 100)
    session['count'] = 0
    return render_template('/index.html')
@app.route('/clear')
def clear():
    session.clear()
    return redirect('/')

@app.route('/guess', methods=['POST'])
def guess():
    session['guess'] = int(request.form['guess'])
    session['count'] += 1
    if session['count'] > 6:
        return redirect('/toomany')
    if session['randomNum'] > session['guess']:
        return redirect('/toolow')
    if session['randomNum'] < session['guess']:
        return redirect('/toohigh')
    if session['randomNum'] == session['guess']:
        return redirect('/correct')
@app.route('/toohigh')
def toohigh():
    color = "red"
    width = "200px"
    height = "200px"
    guessed = "Too High!"
    return render_template('/guessed.html', color = color, width = width, height = height, guessed = guessed)
@app.route('/toolow')
def toolow():
    color = "red"
    width = "200px"
    height = "200px"
    guessed = "Too Low!"
    return render_template('/guessed.html', color = color, width = width, height = height, guessed = guessed)
@app.route('/toomany')
def toomany():
    color = "red"
    width = "200px"
    height = "200px"
    guessed = "Too Many Guesses! Haaa! Try Again!"
    return render_template('/correct.html', color = color, width = width, height = height, guessed = guessed)
@app.route('/correct')
def correct():
    color = "green"
    width = "180px"
    height = "180px"
    guessed = "You Got It! " + str(session['guess']) + " Was the Number!"

    return render_template('/correct.html', color = color, width = width, height = height, guessed = guessed)

if __name__ == "__main__":
    app.run(debug=True)