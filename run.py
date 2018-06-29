import os
import json
from flask import Flask, render_template, request, flash, redirect
from answer_checker import *

app = Flask(__name__)
app.secret_key = 'hey_riddle_diddle_123'

current_user = {"name":"guest"}
current_riddle = 0

def add_a_new_user(email, password):
    new_user_list = []
    user_dict = {"email": email, "password": password}
    new_user_list.append(user_dict)
    new_user_list_str = "," + str(new_user_list)
    with open("data/users.json", "a") as user_list:
        user_list.write(new_user_list_str)
    
def user_has_logged_in(email):
    global current_user
    current_user["name"] = email
    return current_user

def add_guess_to_file(guess):
    f = open('data/guesses.txt', 'a')
    this_guess = str(guess) + "\n"
    f.writelines(this_guess)
    f.close()

def check_answer(guess, data, index):
    if guess.lower() == data[index]["answer"].lower():
        global current_riddle
        current_riddle +=1
        print("correct " + data[index]["answer"])
        flash("Correct!  {} was the right answer!\n Time for your next riddle...!".format(guess.upper()))
    else:
        current_riddle = 0
        flash("I'm sorry!  {} was incorrect!\n Please try again from the beggining :(".format(guess.upper()))
        print("Incorrect " + data[index]["answer"])

@app.route('/')
@app.route('/<username>')
def index(username=current_user["name"]):
    return render_template("index.html", page_title="Home", username=current_user["name"])

@app.route('/sign_up.html', methods=["GET", "POST"])
def sign_up():
    if request.method == "POST":
        """
        Check if email already exists in users.json and if not add new username
        """
        add_a_new_user(request.form["email"], request.form["pwd1"])
        flash("Hi {}, thanks for signing up!  Please feel free to log in and play.\n Your username should now appear on the leaderboard if you get a high score!".format(request.form["email"]))
    return render_template("sign_up.html", page_title="Sign Up", username=current_user["name"])

@app.route('/log_in.html', methods=["GET", "POST"])
def log_in():
    if request.method == "POST":
        user_has_logged_in(request.form["email"])
        return redirect(current_user["name"])
    return render_template("log_in.html", page_title="Log In", username=current_user["name"])

@app.route('/<username>/riddles.html', methods=["GET", "POST"])
def riddles(username):
    data = []
    with open("data/riddles.json", "r") as json_data:
        data = json.load(json_data)
    if request.method == "POST":
        add_guess_to_file(request.form["guess-entry"])
        check_answer(request.form["guess-entry"], data, current_riddle)
    return render_template("riddles.html", page_title="Riddles", riddles_data=data, username=current_user["name"], riddle_index=current_riddle)

@app.route('/leaderboard.html')
def leaderboard():
    return render_template("leaderboard.html", page_title="Leaderboard", username=current_user["name"])

@app.route('/account.html')
def account():
    with open("data/users.json", "r") as json_data:
        user_data = json.load(json_data)
    return render_template("account.html", page_title="Account", username=current_user["name"], user_data=user_data)

if __name__ == "__main__":
    app.run(host=os.environ.get('IP'),
        port=int(os.environ.get('PORT')),
        debug=True)