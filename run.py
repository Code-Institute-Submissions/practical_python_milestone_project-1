import os
import json
from flask import Flask, render_template, request, flash, redirect
from answer_checker import *

app = Flask(__name__)
app.secret_key = 'hey_riddle_diddle_123'

current_user = "guest"
current_riddle = 0
game_in_play = True
score_last_game = 0

def load_json_data(jsonfile_path, access_mode):
    with open(jsonfile_path, access_mode) as output_name:
        var_name = json.load(output_name)
        return var_name

class User(object):
    def __init__(self, email, password, username, firstname, surname):
        self.email = email
        self.password = password
        self.username = username
        self.firstname = firstname
        self.surname = surname
        self.highscore = 0
        

class Guess(object):
    def __init__(self, guess, index):
        self.question = index + 1
        self.guess = guess
        
def jsonDefault(object):
    return object.__dict__        

def add_a_new_user(email, password):
    
    user = User(email, password, "TBC", "TBC", "TBC")
    jsonuser = json.dumps(user, default=jsonDefault, indent=4, separators=(',', ': '))
    
    with open("data/users.json", "r+") as user_list:
        str_list = user_list.read()
        str_list_length = len(str_list)
        
        """
        This will check if the email address is already in the users.json file
        """
        if email in str_list:
            flash("I'm sorry, this email address -  {}, has already been registered.\n  Please log in if you've signed up previously or try a different email address.".format(email))
        else:
            """
            If the email address does not already exist, then a new user will be written to the file
            """
            if str_list == "":
                user_list.write("[" + jsonuser + "]")
            else:
                new_user_str = ",\n {}]".format(jsonuser)
                user_list.seek(str_list_length -1)
                user_list.write(new_user_str)
            flash("Hi {}, thanks for signing up!  Please feel free to log in and play.\n Your username should now appear on the leaderboard if you get a high score!".format(email))

def validate_password_on_log_in(email_given, password_given):
    
    json_users = load_json_data("data/users.json","r")
    """
    Here we will append a message to a list if the email address exists, if the password matches an okay status will be added,
    if the password is wrong an incorrect status will be added.  If the email address doesn't exist no message will be added
    and a message will be advised accordingly
    """
        
    log_on_validation_status = []
        
    for user in json_users:
        if email_given == user["email"] and password_given == user["password"]:
            user_has_logged_in(email_given)
            log_on_validation_status.append("username & password match")
            print("found user, password_okay")
            break
        elif email_given == user["email"] and password_given != user["password"]:
            log_on_validation_status.append("username found, password incorrect")
            print("found user, password incorrect!")
            break
        
    if log_on_validation_status == []:
        flash("I'm sorry, email address {} does not appear to have been registered.  Please sign up now or try again!".format(email_given))
        render_template("log_in.html", page_title="Log In", username=current_user)
    elif log_on_validation_status[0] == "username & password match":
        render_template("index.html", page_title="Home", username=current_user)
    elif log_on_validation_status[0] == "username found, password incorrect":
        flash("I'm sorry, the password you entered does not match with our records.  Please feel free to try again!")
        render_template("log_in.html", page_title="Log In", username=current_user)
            
def update_user_details(current_user, new_email, new_password, new_username, new_firstname, new_surname):
    with open('data/users.json', "r") as f:
        data = json.load(f)
        """
        This will check through the json file of users until it finds the right user.  It then deletes that users data and adds
        a new user with the details provided
        """
        for user in data:
            if user["email"] == current_user:
                for user in range(len(data)):
                    if data[user]["email"] == current_user:
                        updated_user = {"email":new_email, "password":new_password, "username":new_username, "firstname": new_firstname, "surname":new_surname, "highscore":user["highscore"]}
                        del data[user]
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
            guesses_file.write("[" + jsonguess + "]")
        else:
            new_guess_str = ",\n{}]".format(jsonguess)
            guesses_file.seek(guesses_txt_length -1)
            guesses_file.write(new_guess_str)

def user_has_logged_in(email):
    global current_user
    current_user = email
    return current_user

def check_answer(guess, data, index, username):
    if guess.lower() == data[index]["answer"].lower():
        global game_in_play
        game_in_play = True
        global current_riddle
        current_riddle +=1
        flash("Correct!  {} was the right answer!\n Time for your next riddle...!".format(guess.upper()))
    else:
        global game_in_play
        game_in_play = False
        add_guess_to_file(request.form["guess-entry"], current_riddle)
        global score_last_game
        score_last_game = current_riddle
        global current_riddle
        current_riddle = 0
        flash("I'm sorry!  {} was incorrect!\n Please try again from the beginning :(".format(guess.upper()))

@app.route('/')
@app.route('/<username>')
def index(username=current_user):
    return render_template("index.html", page_title="Home", username=current_user)

@app.route('/sign_up.html', methods=["GET", "POST"])
def sign_up():
    if request.method == "POST":
        """
        Add a new user will check if email already exists in users.json and if not add new username
        """
        add_a_new_user(str(request.form["email"]), str(request.form["pwd1"]))
    return render_template("sign_up.html", page_title="Sign Up", username=current_user)

@app.route('/log_in.html', methods=["GET", "POST"])
def log_in():
    if request.method == "POST":
        """
        Validate_password_on_log_in will check to see if a user is already signed up and then if the password
        given matches the users stored password
        """
        validate_password_on_log_in(request.form["email"], request.form["password"])
    return render_template("log_in.html", page_title="Log In", username=current_user)

@app.route('/<username>/riddles.html', methods=["GET", "POST"])
def riddles(username):
    data = []
    with open("data/riddles.json", "r") as json_data:
        data = json.load(json_data)
    
    guesses_data = []
    with open("data/guesses.json", "r") as guess_data:
        str_guess_data = guess_data.read()
        
        if str_guess_data == "":
            guesses_data = "No other guesses on this one so far!"
        else:
            with open("data/guesses.json", "r") as guess_data:
                guesses_data = json.load(guess_data)
    
    if request.method == "POST":
        check_answer(request.form["guess-entry"], data, current_riddle, current_user)
    return render_template("riddles.html", page_title="Riddles", riddles_data=data, username=current_user, riddle_index=current_riddle, guesses=guesses_data, game_in_play=game_in_play, score=score_last_game)

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