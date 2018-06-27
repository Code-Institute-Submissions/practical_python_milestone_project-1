import os
import json
from flask import Flask, render_template, request, flash
from answer_checker import *

app = Flask(__name__)
app.secret_key = 'hey_riddle_diddle_123'

users_data = []
logged_in_user = "Guest"

def add_user(email, password):
    global logged_in_user
    logged_in_user = email

@app.route('/')
def home_page():
    return render_template("index.html", page_title="Home", logged_in_user=logged_in_user)

@app.route('/sign_up.html', methods=["GET", "POST"])
def sign_up():
    if request.method == "POST":
        flash("Hi {}, thanks for signing up!  Please feel free to log in and play.\n Your username should now appear on the leaderboard if you get a high score!".format(request.form["email"]))
    return render_template("sign_up.html", page_title="Sign Up",logged_in_user=logged_in_user)

@app.route('/log_in.html', methods=["GET", "POST"])
def log_in():
    if request.method == "POST":
        add_user(request.form["email"], request.form["password"])
        flash("Welcome back {}, we've missed you!  Are you ready for a Jimmy Riddle?!".format(request.form["email"]))
    return render_template("log_in.html", page_title="Sign In", logged_in_user=logged_in_user)

@app.route('/riddles.html', methods=["GET", "POST"])
def riddles():
    data = []
    with open("data/riddles.json", "r") as json_data:
        data = json.load(json_data)
    return render_template("riddles.html", page_title="Riddles", riddles_data=data, logged_in_user=logged_in_user)

@app.route('/leaderboard.html')
def leaderboard():
    return render_template("leaderboard.html", page_title="Leaderboard", logged_in_user=logged_in_user)

@app.route('/account.html')
def account():
    return render_template("account.html", page_title="account", logged_in_user=logged_in_user)

if __name__ == "__main__":
    app.run(host=os.environ.get('IP'),
        port=int(os.environ.get('PORT')),
        debug=True)