import os
import json
from flask import Flask, render_template, request, flash, redirect
from answer_checker import *

app = Flask(__name__)
app.secret_key = 'hey_riddle_diddle_123'

current_user = "guest"
current_riddle = 0

class User(object):
    def __init__(self, email, password, username, firstname, surname):
        self.email = email
        self.password = password
        self.username = username
        self.firstname = firstname
        self.surname = surname

class Guess(object):
    def __init__(self, guess, index):
        self.index = guess
        
def jsonDefault(object):
    return object.__dict__        

def add_a_new_user(email, password):
    
    user = User(email, password, "TBC", "TBC", "TBC")
    jsonuser = json.dumps(user, default=jsonDefault, indent=4, separators=(',', ': '))
    
    with open("data/users.json", "r+") as user_list:
        str_list = user_list.read()
        str_list_length = len(str_list)
        
        if email in str_list:
            flash("I'm sorry, username {} has already been taken.\n  Please log in if you've signed up previously or try a different email address.".format(email))
        else:
            if str_list == "":
                user_list.write("[" + jsonuser + "]")
            else:
                new_user_str = ",\n {}]".format(jsonuser)
                user_list.seek(str_list_length -1)
                user_list.write(new_user_str)
            flash("Hi {}, thanks for signing up!  Please feel free to log in and play.\n Your username should now appear on the leaderboard if you get a high score!".format(email))

def update_user_details(current_user, new_email, new_password, new_username, new_firstname, new_surname):
    with open('data/users.json', "r") as f:
        data = json.load(f)
        
        for user in data:
            if user["email"] == current_user:
                for user in range(len(data)):
                    if data[user]["email"] == current_user:
                        del data[user]
                        updated_user = {"email":new_email, "password":new_password, "username":new_username, "firstname": new_firstname, "surname":new_surname}
                        data.append(updated_user)
                        break
    f.close()    
    
    with open('data/users.json', "w") as f:
        new_data = json.dumps(data, default=jsonDefault, indent=4, separators=(',', ': '))
        f.write(new_data)
    
def add_guess_to_file(guess, index):
    
    guess = Guess(guess, index)
    jsonguess = json.dumps(guess, default=jsonDefault, indent=4, separators=(',', ': '))
    
    with open('data/guesses.json', "r+") as guesses_file:
        guess_text = guesses_file.read()
        guesses_txt_length = len(guess_text)

        if guess_text == "":
            guesses_file.write("[\n" + jsonguess + "\n]")
        else:
            new_guess_str = ",\n{}]".format(jsonguess)
            guesses_file.seek(guesses_txt_length -1)
            guesses_file.write(new_guess_str)

def user_has_logged_in(email):
    global current_user
    current_user = email
    return current_user

def check_answer(guess, data, index):
    if guess.lower() == data[index]["answer"].lower():
        global current_riddle
        current_riddle +=1
        print("correct " + data[index]["answer"])
        flash("Correct!  {} was the right answer!\n Time for your next riddle...!".format(guess.upper()))
    else:
        add_guess_to_file(request.form["guess-entry"], current_riddle)
        current_riddle = 0
        flash("I'm sorry!  {} was incorrect!\n Please try again from the beginning :(".format(guess.upper()))
        print("Incorrect " + data[index]["answer"])

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
        add_a_new_user(str(request.form["email"]), str(request.form["pwd1"]))
    return render_template("sign_up.html", page_title="Sign Up", username=current_user)

@app.route('/log_in.html', methods=["GET", "POST"])
def log_in():
    if request.method == "POST":
        user_has_logged_in(request.form["email"])
        return redirect(current_user)
    return render_template("log_in.html", page_title="Log In", username=current_user)

@app.route('/<username>/riddles.html', methods=["GET", "POST"])
def riddles(username):
    data = []
    with open("data/riddles.json", "r") as json_data:
        data = json.load(json_data)
    if request.method == "POST":
        check_answer(request.form["guess-entry"], data, current_riddle)
    return render_template("riddles.html", page_title="Riddles", riddles_data=data, username=current_user, riddle_index=current_riddle)

@app.route('/leaderboard.html')
def leaderboard():
    return render_template("leaderboard.html", page_title="Leaderboard", username=current_user)

@app.route('/<username>/account.html', methods=["GET", "POST"])
def account(username):
    user_data = []
    with open("data/users.json", "r") as json_data:
        user_data = json.load(json_data)
    if request.method == "POST":
        update_user_details(username, request.form["email"], request.form["password"], request.form["username"], request.form["firstname"], request.form["surname"])
        with open("data/users.json", "r") as json_data:
            user_data = json.load(json_data)
    return render_template("account.html", page_title="Account", username=current_user, user_data=user_data)

if __name__ == "__main__":
    app.run(host=os.environ.get('IP'),
        port=int(os.environ.get('PORT')),
        debug=True)