import os
import json
from flask import Flask, render_template, request, flash
from answer_checker import *

app = Flask(__name__)
app.secret_key = 'hey_riddle_diddle_123'

def add_users(email, password):
    users.append("{}:{}".format(email, password))

@app.route('/')
@app.route('/<user>')
def index(user="Guest"):
    return render_template("index.html", page_title="Home", user=user)

@app.route('/sign_up.html', methods=["GET", "POST"])
def sign_up():
    if request.method == "POST":
        """
        Check if email already exists in users.json and if not add new username
        """
        
        flash("Hi {}, thanks for signing up!  Please feel free to log in and play.\n Your username should now appear on the leaderboard if you get a high score!".format("who knows"))
    return render_template("sign_up.html", page_title="Sign Up")

@app.route('/log_in.html', methods=["GET", "POST"])
def log_in():
    if request.method == "POST":
        flash("Welcome back {}, we've missed you!  Are you ready for a Jimmy Riddle?!".format(request.form["email"]))
    return render_template("log_in.html", page_title="Log In")

@app.route('/riddles.html' , methods=["GET", "POST"])
def riddles():
    data = []
    with open("data/riddles.json", "r") as json_data:
        data = json.load(json_data)
    return render_template("riddles.html", page_title="Riddles", riddles_data=data)

@app.route('/leaderboard.html')
def leaderboard():
    return render_template("leaderboard.html", page_title="Leaderboard")

@app.route('/account.html')
def account():
    return render_template("account.html", page_title="Account")

if __name__ == "__main__":
    app.run(host=os.environ.get('IP'),
        port=int(os.environ.get('PORT')),
        debug=True)