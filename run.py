import os
import json
from flask import Flask, render_template, request, flash, redirect
from answer_checker import *

app = Flask(__name__)
app.secret_key = 'hey_riddle_diddle_123'

current_user = "guest"
users = []

def add_a_new_user(email, password):
    user_dict = {"email": email, "password": password}
    users.append(user_dict)
    print(users)
    
def user_has_logged_in(email):
    global current_user
    current_user = email
    return current_user

@app.route('/')
@app.route('/<username>')
def index(username=current_user):
    return render_template("index.html", page_title="Home", username=current_user)

@app.route('/sign_up.html', methods=["GET", "POST"])
def sign_up():
    if request.method == "POST":
        """
        Check if email already exists in users.json and if not add new username
        """
        add_a_new_user(request.form["email"], request.form["password"])
        flash("Hi {}, thanks for signing up!  Please feel free to log in and play.\n Your username should now appear on the leaderboard if you get a high score!".format(request.form["email"]))
    return render_template("sign_up.html", page_title="Sign Up", username=current_user)

@app.route('/log_in.html', methods=["GET", "POST"])
def log_in():
    if request.method == "POST":
        user_has_logged_in(request.form["email"])
        return redirect(current_user + "/riddles.html")
    return render_template("log_in.html", page_title="Log In", username=current_user)

@app.route('/<username>/riddles.html', methods=["GET", "POST"])
def riddles(username):
    data = []
    with open("data/riddles.json", "r") as json_data:
        data = json.load(json_data)
    return render_template("riddles.html", page_title="Riddles", riddles_data=data, username=current_user)

@app.route('/leaderboard.html')
def leaderboard():
    return render_template("leaderboard.html", page_title="Leaderboard", username=current_user)

@app.route('/account.html')
def account():
    return render_template("account.html", page_title="Account", username=current_user)

if __name__ == "__main__":
    app.run(host=os.environ.get('IP'),
        port=int(os.environ.get('PORT')),
        debug=True)