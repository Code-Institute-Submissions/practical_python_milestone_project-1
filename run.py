import os
import json
from random import *
from flask import Flask, render_template, request, flash, session, redirect, url_for
from operator import itemgetter
from answer_checker import *

app = Flask(__name__)
app.secret_key = 'hey-riddle-diddle-123'

# File variables
users_file = "data/users.json"
guesses_file = "data/guesses.json"
riddles_file = "data/riddles.json"

# GENERAL---------------------------------------------------------------------------------------

# Shortcut for loading json files
def load_json_data(jsonfile_path, access_mode):
    with open(jsonfile_path, access_mode) as opened_file:
        json_file = json.load(opened_file)
        return json_file

# USER MANAGEMENT FUNCTIONS --------------------------------------------------------------------

def user_has_logged_in(email):
    session['user'] = email
    
def determine_current_user(session_data):
    if 'user' in session:
        return session['user']
    else:
        return "guest"

def validate_password_on_log_in(email_given, password_given):
    
    json_users = load_json_data(users_file,"r")
    """
    Here we will append a message to a list if the email address exists, if the password matches an okay status will be added,
    if the password is wrong an incorrect status will be added.  If the email address doesn't exist no message will be added
    and a message will be advised accordingly
    """
        
    log_on_validation_status = []
        
    for user in json_users:
        if email_given.lower() == user["email"].lower() and password_given == user["password"]:
            user_has_logged_in(email_given)
            log_on_validation_status.append("username & password match")
            break
        elif email_given.lower() == user["email"].lower() and password_given != user["password"]:
            log_on_validation_status.append("username found, password incorrect")
            break
        
    if log_on_validation_status == []:
        flash("I'm sorry, email address {} does not appear to have been registered.  Please sign up now or try again!".format(email_given))
    elif log_on_validation_status[0] == "username & password match":
        return True
    elif log_on_validation_status[0] == "username found, password incorrect":
        flash("I'm sorry, the password you entered does not match with our records.  Please feel free to try again!")

# Helps creates an instance of a user
class User(object):
    def __init__(self, email, password, username, firstname, surname):
        self.email = email.lower()
        self.password = password
        self.username = username
        self.firstname = firstname
        self.surname = surname
        self.highscore = 0
        
def jsonDefault(object):
    return object.__dict__  

def add_a_new_user(email, password, confirm_password):
    if password == confirm_password:
        
        user = User(email, password, "TBC", "TBC", "TBC")
    
        json_users_data = load_json_data(users_file, "r+")
    
        """
        This will check if the email address is already in the users.json file
        """
        existing_email = 0
    
        for existing_user in json_users_data:
            if existing_user["email"] == email:
                existing_email += 1
                break
        
        if existing_email != 0:
            flash("I'm sorry, this email address -  {}, has already been registered.\n  Please log in if you've signed up previously or try a different email address.".format(email))
            return False
        else:
            """
            If the email address does not already exist, then a new user will be written to the file
            """
            json_users_data.append(user)
            new_data = json.dumps(json_users_data, default=jsonDefault, indent=4, separators=(',', ': '))
            with open(users_file, "w") as f:
                f.write(new_data)
            user_has_logged_in(email)
            return True
    else:
        flash("I'm sorry, your passwords didn't match.\n  Please try again!")
            
def update_user_details(current_user, new_email, new_password, new_username, new_firstname, new_surname):
    data = load_json_data(users_file, "r")
    """
    This will check through the json file of users until it finds the right user.  It then deletes that users data and adds
    a new user with the details provided
    """
    for user in range(len(data)):
        if data[user]["email"].lower() == session['user'].lower():
            print("Okay")
            data[user]["email"] = new_email.lower()
            data[user]["surname"]  = new_surname.capitalize()
            data[user]["password"]  = new_password
            data[user]["username"]  = new_username.lower()
            data[user]["firstname"]  = new_firstname.capitalize()
            break
        else:
            print("Not found")
    
    with open(users_file, "w") as f:
        new_data = json.dumps(data, default=jsonDefault, indent=4, separators=(',', ': '))
        f.write(new_data)
    flash("Hey {}, thanks for updating your details!".format(new_email))
        
# GAME MECHANICS -----------------------------------------------------------------------------

def set_up_client_side_game_variables():
    try:
        session["current_riddle"]
    except:
        session["current_riddle"] = 0
        session["game_in_play"] = True
        session["score_last_game"] = 0
        session["riddle_order"] = []
        session["last_riddle"] = 0

def determine_riddle_order():
    riddles = load_json_data(riddles_file, "r")
    new_riddle_order = []
    while len(new_riddle_order) < len(riddles):
        ran_num = pick_a_riddle()
        if ran_num not in new_riddle_order:
            new_riddle_order.append(ran_num)
    session["riddle_order"] = new_riddle_order
            
def pick_a_riddle():
    riddles = load_json_data(riddles_file, "r")
    ran_num = randint(0, len(riddles)-1)
    return ran_num

def words_in_answer(data, index, riddle_list):
    correct_riddle_index = riddle_list[index]
    this_answer = data[correct_riddle_index]["answer"]
    word_count = this_answer.split()
    length_of_answer = len(word_count)
    if length_of_answer == 1:
        return "1 word"
    else:
        return "{} words".format(length_of_answer)
    
def check_answer(guess, data, index, username, riddle):
    
    no_spaces_guess = guess.replace(" ", "")
    no_spaces_answer = data[index]["answer"].replace(" ", "")
    
    if no_spaces_guess.lower() == no_spaces_answer.lower():
        if riddle +1 == len(session["riddle_order"]):
            session["score_last_game"] = session["current_riddle"]
            session["last_riddle"] = session["riddle_order"][session["current_riddle"]]
            session["game_in_play"] = False
            update_high_score(session["current_riddle"])
            session["current_riddle"] = 0
            session["riddle_order"] = []
            determine_riddle_order()
            return "Winner"
        else:
            session["game_in_play"] = True
            session["current_riddle"] +=1
            flash("Correct!  {} was the right answer!\n Time for your next riddle...!".format(data[index]["answer"].upper()))
    else:
        session["score_last_game"] = session["current_riddle"]
        session["last_riddle"] = session["riddle_order"][session["current_riddle"]]
        session["game_in_play"] = False
        add_guess_to_file(request.form["guess-entry"], session["riddle_order"][session["current_riddle"]]-1)
        update_high_score(session["current_riddle"])
        session["current_riddle"] = 0
        session["riddle_order"] = []
        determine_riddle_order()
        flash("I'm sorry!  {} was incorrect!\n Please try again from the beginning!".format(guess.upper()))

# GUESSES FILE FUNCTIONS -----------------------------------------------------------------------------------


# Indexs a guess to a riddle
class Guess(object):
    def __init__(self, guess, index):
        self.question = index + 1
        self.guess = guess

def add_guess_to_file(guess, index):
    
    guess = Guess(guess, index)
    jsonguess = json.dumps(guess, default=jsonDefault, indent=4, separators=(',', ': '))
    
    with open(guesses_file, "r+") as open_file:
        guess_text = open_file.read()
        guesses_txt_length = len(guess_text)

        if guess_text == "[]":
            new_guess_str = "\n{}]".format(jsonguess)
            open_file.seek(guesses_txt_length -1)
            open_file.write(new_guess_str)
        else:
            new_guess_str = ",\n{}]".format(jsonguess)
            open_file.seek(guesses_txt_length -1)
            open_file.write(new_guess_str)

def other_users_guesses(riddle):
    guess_data = load_json_data(guesses_file, "r")
    user_guesses = []
    num_of_related_guesses = 0
    for guess in guess_data:
        if guess["question"] == riddle:
            user_guesses.append(guess["guess"])
            num_of_related_guesses +=1
        
    if num_of_related_guesses != 0:
        while len(user_guesses) > 18:
            user_guesses.pop(0)
        return user_guesses
    else:
        return ["No other guesses so far"]

# HIGH SCORE FUNCTIONS -----------------------------------------------------------------------------------

def update_high_score(new_score):
    if 'user' in session:
        data = load_json_data(users_file, "r")
    
        for user in range(len(data)):
            if data[user]["email"] == session['user']:
                if any("highscore" in x for x in data[user]):
                    if data[user]["highscore"] < new_score:
                        data[user]["highscore"]  = new_score
                        break
                else:
                    data[user]["highscore"] = new_score
                    break
    
        with open(users_file, "w") as f:
            new_data = json.dumps(data, default=jsonDefault, indent=4, separators=(',', ': '))
            f.write(new_data) 

def create_leaderboard(userdata):

    sorted_user_scores = sorted(userdata, key=lambda k: k['highscore'], reverse=True) 
    
    top_ten = []
    
    if len(sorted_user_scores) < 10:
        max_leaderboard = len(scores_sorted_by_highscore)
    else:
        max_leaderboard = 10
    
    i = 0
    while i < max_leaderboard:
        top_ten.append(sorted_user_scores[i])
        i+= 1
    
    return top_ten

# ROUTES ------------------------------------------------------------------------------        

@app.before_request
def before_request():
    protected_route = ['account']
    if request.endpoint in protected_route and 'user' not in session:
        return redirect('/login')

@app.route('/')
@app.route('/<username>')
def index(username=None):
    current_user = determine_current_user(session)
    set_up_client_side_game_variables()
    
    return render_template("index.html", page_title="Home", username=current_user)
    
@app.route('/sign_up.html', methods=["GET", "POST"])
def sign_up():
    if request.method == "POST":
        """
        Add a new user will check if email already exists in users.json and if not add new username
        """
        if add_a_new_user(str(request.form["email"]), str(request.form["pwd1"]), str(request.form["pwd2"])) == True:
            flash("Hi {}, thanks for signing up! Your username should now appear on the leaderboard if you get a high score! Now get ready to riddle...!".format(request.form["email"]))
            return redirect(url_for('riddles', username=session['user']))
    return render_template("sign_up.html", page_title="Sign Up", username="guest")

@app.route('/log_in.html', methods=["GET", "POST"])
def log_in():
    session.pop('user', None)
    
    if request.method == "POST":
        """
        Validate_password_on_log_in will check to see if a user is already signed up and then if the password
        given matches the users stored password
        """
        if validate_password_on_log_in(request.form["email"], request.form["password"]) == True:
            return redirect(request.form["email"])
        else:
            return render_template("log_in.html", page_title="Log In", username="guest")
    return render_template("log_in.html", page_title="Log In", username="guest")

@app.route('/<username>/riddles.html', methods=["GET", "POST"])
def riddles(username):
    
    guesses_data = []
    riddles_data=load_json_data(riddles_file, "r")    
    answer_words = words_in_answer(riddles_data, session["current_riddle"], session["riddle_order"])
    current_user = determine_current_user(session)
    
    if session["riddle_order"] == [] or len(riddles_data) != len(session["riddle_order"]):
        determine_riddle_order()
    
    if request.method == "POST":
        
        if check_answer(request.form["guess-entry"], load_json_data(riddles_file, "r"), session["riddle_order"][session["current_riddle"]], current_user, session["current_riddle"]) == "Winner":
            return redirect(url_for("congratulations", username=current_user))
        guesses_data = other_users_guesses(session["last_riddle"])
        answer_words = words_in_answer(riddles_data, session["current_riddle"], session["riddle_order"])
    
    return render_template("riddles.html", page_title="Riddles", riddles_data=riddles_data, user_data=load_json_data(users_file, "r"), username=current_user, riddle_index=session["current_riddle"], 
    guesses=guesses_data, game_in_play=session["game_in_play"], score=session["score_last_game"], riddle_order=session["riddle_order"], last=session["last_riddle"], word_count=answer_words)

@app.route('/leaderboard.html')
def leaderboard():
    top_ten = create_leaderboard(load_json_data(users_file, "r"))
    current_user = determine_current_user(session)
    return render_template("leaderboard.html", page_title="Leaderboard", top_ten = top_ten, username=current_user)

@app.route('/<username>/account.html', methods=["GET", "POST"])
def account(username):
    user_data = load_json_data(users_file, "r")
    for user in user_data:
        if user["email"].lower() == username.lower():
            this_user = user
    
    if request.method == "POST":
        update_user_details(username, request.form["email"], request.form["password"], request.form["username"], request.form["firstname"], request.form["surname"])
        user_data = load_json_data(users_file, "r")
        for user in user_data:
            if user["email"].lower() == username.lower():
                this_user = user
        return render_template("account.html", page_title="Account", username=session['user'], this_user = this_user)
    
    return render_template("account.html", page_title="Account", username=session['user'], this_user = this_user)

    
@app.route('/logout.html')
def logout():
    session.pop('user', None)
    current_user = determine_current_user(session)
    
    return render_template("logout.html", page_title="Logged Out", username=current_user)

@app.route('/about-us.html')
def about_us():
    current_user = determine_current_user(session)
    return render_template("about-us.html", page_title="About Us", username=current_user)

@app.route('/congratulations.html')
def congratulations():
    current_user = determine_current_user(session)
    return render_template("congratulations.html", page_title="Winner", username=current_user)

if __name__ == "__main__":
    app.run(host=os.environ.get('IP'),
        port=int(os.environ.get('PORT')),
        debug=True)