# MILESTONE PROJECT NAME:  PRACTICAL PYTHON - HEY RIDDLE DIDDLE.COM
## NAME:  GIANCARLO FIORLETTA


## INTRODUCTION:

In this project I have created a riddle based web application game to demonstrate my understanding of 
Python and the Flask Micro Framework.  From a user perspective the website should provide some fun riddles 
and the opportunity for the user to ascend to the top of the sites leaderboard.

## UX

### AIMS:

The main aims of the project are as follows...

1)  To allow the user to play a working riddles game
2)  To allow the user to climb the leaderboard if them perform well enough verses other users
3)  To provide a platform for each user to log in and out and update their profile
4)  To develop a theme that attracts the user to the site

The website should also be responsive so that it works across all devices and media sizes.  It should be intuitive and easy for the user to use.

### USER STORIES:

To understand why people might choose to use this site and therefore provide direction on its creation, I created a number of user stories as follows...

Story 1:  As a fan of comics, I want to visit a stylish website featuring my favourite characters and artwork.

Story 2: As a silver surfer, I want to play a game that is simple but tests my brain power!

Story 3:  As a fan of riddles, I want to play a game where I can top the leaderboard and show how clever I am!

Story 4:  As someone who likes to socialise, I want to play a game that I can test my friends on and discuss the answers!

I think a riddles website with a comic book theme based on the riddler would be an excellent idea especially for the first user.  Comic books are hugely popular and stylish, even people
who are not fans would generally agree with that!  If ever anyone starts talking about riddles the riddler always quickly springs to mind so I'm sure it would be a popular choice.  This will help
to direct the colours of the site as the riddler is often associated with green and purple attire.

Riddles have been around forever and are also enjoyed by the older generations who tend to like things to be simple, so the site should be simple to match their needs.  Anyone who is good
at riddles like to boast about their achievements and there is often a huge amount of satisfaction when delivering the right answer after thinking about the riddle so hard, therefore a 
leaderboard is another good idea for the site.

Finally, lots of people like to get involved with riddles, and if you can't find the answer then what's better than discussing the riddle with friends!  There is a big social aspect to riddles
that will work well for user 4.

### WIREFRAMES:
My website will be divided into 9 pages.  The home page which will feature a welcome message and links to the log in, sign up and riddles pages.  There will then be the riddles page itself and an about us page, 
in addition there needs to be a page for a user to update their details, a page that displays when the user logs out, the leaderboard page to display the highest scores and a congratulations page for 
user who answer all of the riddles correctly.

I have created some basic wireframes to show how these pages will be laid out, but it is the comic book artwork that will sit behind each of the pages that should help the site stand out and be a draw to
any new visitors.

**Please see the Wireframes folder for the designs.**

## FEATURES

### EXISTING FEATURES:

#### PAGE 1 - HOME PAGE (index.html):

The home page has two main sections and has been arranged to make the site look stylish and feel straightforward.  The first section has a full size picture of the riddlers face in his trademark colours and a header
floats in to welcome the user to the page, alternating between white and purple to catch the eye.  Underneath, a picture of the Riddler tipping his cap greets the user with the option to sign up, sign in, or get to the
riddles, giving the user immediate access to the main features of the site.

The nav-bar is fixed to the top of the screen to give the user easy access no matter where they are in the page, on mobile this changes to a standard drop down list so that the users view is never unintentionally obscured.
At the bottom of the page is a footer that the user can click to be redirected to more information about the site.

If signed in, a javascript function will scroll section 2 into view with a message to welcome back the user and personalise their experience.

#### PAGES 2,3,4,5 - USER PAGES (log_in.html, logout.html, sign_up.html & account.html):

The user pages are an important feature of this website, allowing the user to register and thereby giving them the opportunity for their score to be shown on the leaderboard if they score highly enough.  The log in, sign up
and account pages have all been designed in a similar fashion to keep some visual consistency on what are similar pages.  When signing up or signing in, the Python script completes a number of checks to ensure that the same user 
can't sign up twice, to make sure passwords match and to redirect the user in each situation.  

The account page allows the user to update their details and even choose a username that they would like to appear on the leaderboard (the default is the users email address if a username isn't provided).

#### PAGE 6 - RIDDLE GAME PAGE (riddles.html):

Riddles.html is the main game page and has been kept as simple as possible.  Another stylish picture of the riddler is visible to players and a stand out riddle box covers a large proportion of the screen across all devices.
On load, a riddle fades in to view prompting the user to answer the riddle in the input box.  In addition to the riddle, there is a function that advises the user how many words the correct answer is made up of, giving them
a better chance of answering correctly but also hopefully taking away any frustration with entering the right answer but not in the right way (for example entering "Piano" which would be incorrect, instead of "A Piano" which
would be the accepted answer).

Upon submission, if the answer is correct, the user is redirected to the next riddle and a text box is displayed with the answer provided to confirm that it was correct.  If this correct answer is for the final riddle in the 
riddles file, the player is redirected to the congratulations.html page which informs them that they have completed all of the existing riddles on the site.  If the answer was incorrect, a box is displayed which advises
the user what their score was (verses their highest score if they are signed in), and it gives them a number of answers that the previous users had incorrectly provided which will possibly provide some clues and perhaps
some laughs along the way!

### PAGE 7 - THE LEADERBOARD (leaderboard.html):

The leaderboard page has two main components, another stylish comic inspired picture and the leaderboard itself.  Every time this page is accessed, the leaderboard is rebuilt based on the most up to date high scores that have
been achieved by a user on completion of their game.  It displays the top ten scores and the username of the player if provided (their email address if not) and the score that had been achieved.

### PAGE 8 - ABOUT US (about_us.html):

This page features a few paragraphs about me which are meant to be humorous.  Usually this would include more details or links associated with the company or creator of the site, but in this instance as there aren't really 
any I can add, I have left it as a basic page but with my email address should any user wish to get in touch.

### PAGE 9 - CONGRATULATIONS (congratulations.html):

Another humorous message meets any user that successfully answers all of the riddles that are available on the site.  This is determined by the length of the riddles.json file so will automatically keep track of the number of
riddles available and display the page when required accordingly.

### FUTURE FEATURES:

#### Email updates
One new feature could be the addition of email updates to inform users when new riddles have been added to attract them back to the site.  In addition to this the user could be informed if their top ten position had been
superseded by another user, beckoning them back to attempt to regain their place on the leaderboard.

#### User generated riddles
In theory there could be a new page to allow users to add their own riddles.  These could then be added directly to the riddles.json file, or go to a member of the build team to be filtered and validated before being added.
This would certainly help build the database of riddles if too many users answered them all correctly and could prove attractive for people that like to be creative and create their own riddles.

#### Riddle tournaments
Each week a riddles tournament could be added for users to attempt.  Perhaps a set of 10 brand new riddles for players to attempt where the number of attempts to get the answer right and the time it took for the full
set to be completed (first to complete that week would be top of the leaderboard) could be taken into account when generating the list of winning users.  Another method of getting regular visitors to the site. 

## TECHNOLOGIES USED:

#### 1:  NAME - JQuery

LINK - https://jquery.com/

REASON - Jquery has been used as it provides some very useful methods when working with javascript and these have often been utilised in my javascript code.

#### 2: NAME - Google Fonts

LINK - https://fonts.google.com/

REASON - Used to style the two types of fonts incorporated into the style of the site.

#### 3: NAME - Font Awesome

LINK - https://fontawesome.com/

REASON - Font awesome has been used to incorporate its icons onto the site as it has multiple options to ensure that the icon used is relevant to the content it is being used for, in this case they are mainly used
in the nav-bar against each navigation option.

#### 4: NAME - SASS

LINK - https://sass-lang.com/

REASON - Sass has really helped me to organise my css code and has some really useful features such as the way it handles media queries which makes this part of styling much less painful.  It also helps the site to load 
faster through the use of placeholders which are only used when called upon.

#### 4: NAME - FLASK

LINK - http://flask.pocoo.org/

REASON - Flask is a microframework that has many useful tools and has been used primarily to create the routing for this website.  Tools such as sessions have also been essential, making it possible for multiple users
to use the website at once by storing key variables client side.  

#### 5: NAME - JINJA2

LINK - http://jinja.pocoo.org/

REASON - Jinja2 is a full featured template engine for Python.  It has enabled data to be passed from Python to the html templates and also allows logic to be used inside of the template to assist in DRY coding.

## WEBSITE WORKINGS:

The workings of the website have been broken down into four main sections in the run.py file and each of the more complex functions have been annotated to help other developers understand how they work.  However, 
here is a quick breakdown of each of the sections and their purpose:

1) USER MANAGEMENT FUNCTIONS

Any user, registered or unregistered can use this website but only registered users can be placed on the leaderboard.  These functions are all based around user management.  Throughout these functions, user data is 
written to the users.json file and some of this data is passed client side into the session['user'] variable for the site to identify when a user is active.  

There is a function to add a new user using the created 'user' class, a function to update a users details and a function to validate a users password and behave accordingly dependant on the outcome.

2) GAME MECHANICS

The riddles game works from a number of variables stored in client side flask sessions so that multiple users can play at the same time and not impact each others games.  The determine riddle order function simply creates 
a list of numbers in a random order that relate to the index numbers of the riddles in the riddles file.  This dictates the order in which the riddles will be shown on each attempt at the game.

The check answer function then determines if the given answer matches the answer in the file, ignoring spaces and case, and either resets the game or moves to the next riddle in the list if the answer is correct.  If the final
riddle has been answered correctly, the site will display the congratulations page.

There is also a function which identifies how many words are in the correct answer which is fed back to the user via template logic.

3) GUESSES FILE FUNCTIONS

Once the game has ended, the code will use the session["last_riddle"] variable to identify which riddle was answered incorrectly and write the given answer to the guesses.json file which is then displayed to other users if
they get the same question wrong.

4) HIGH SCORE FUNCTIONS

The update high score function looks at the score currently held by the logged in user and updates that within the users file if their new score is higher.  The update leaderboard function then sorts the users by score and
selects the ten best scores which is used to populate the leaderboard.

## WEBSITE TESTING:

#### UX

The website has been designed to meet the needs of the users described in the user stories section.  Here is a brief run down of how each has been met - 

Story 1:  As a fan of comics, I want to visit a stylish website featuring my favourite characters and artwork.

REFLECTION - I have tried hard to get the design of the site to be as stylish as possible by using riddler relevant colours and artwork and I am personally quite pleased with the result.  I would hope that throughout the site 
both fans of the genre and neutrals alike would enjoy the visual style and variety of riddler characters on display.

Story 2: As a silver surfer, I want to play a game that is simple but tests my brain power!

REFLECTION - After testing on older family members they really enjoyed the site and didn't struggle to get to grips with the mechanics of the game.  One older user even set the high score!  Therefore on reflection
I think the site serves this purpose very well.

Story 3:  As a fan of riddles, I want to play a game where I can top the leaderboard and show how clever I am!

REFLECTION - A lot of testing has been done on the leaderboard to ensure it behaves correctly and any user who signs up and ends the game with a high enough score should find themselves on the leaderboard.  Mission
accomplished here!

Story 4:  As someone who likes to socialise, I want to play a game that I can test my friends on and discuss the answers!

REFLECTION - Upon driving home from a football match a few hours away, we found a good amount of amusement on the site trying to answer riddles and discussing the answers between the five of us who went.  There was also
enthusiasm for the site with friends at a restaurant meet, who seemed pretty engaged so this leads me to believe this object has been fulfilled.

#### STYLING / FUNCTIONALITY

Each element on the site has been manually tested to ensure it functions as intended as follows:

**Test 1** - On home page, logo is clicked - reloads home page - SUCCESS
**Test 2** - On home page, Home is clicked on the navbar - reloads home page - SUCCESS
**Test 3** - On home page, Log In is clicked on the navbar - loads log in page - SUCCESS
**Test 4** - On home page, Sign Up is clicked on the navbar - loads sign up page - SUCCESS
**Test 5** - On home page, Riddles is clicked on the navbar - loads riddle page, a riddle fades in with correct number of answer words displayed - SUCCESS
**Test 6** - On home page, Leaderboard is clicked on the navbar - loads leaderboard page, with 10 best scored users - SUCCESS
**Test 7** - On home page, Sign Up text is clicked in bottom section - loads sign up page - SUCCESS
**Test 8** - On home page, Log in text is clicked in bottom section - loads log in page - SUCCESS
**Test 9** - On home page, purple riddles button is clicked in bottom section - button increases in size when hovered and loads riddles page - SUCCESS
**Test 10** - On home page, about us text is clicked in footer - font increases in size when hovered and loads about us page - SUCCESS
**Test 11** - On sign up page, attempted to sign up with an existing users email address - denied, flashed message to advise - SUCCESS
**Test 12** - On sign up page, attempted to sign up with passwords that dont match - denied, flashed message to advise - SUCCESS
**Test 13** - On sign up page, attempted to sign up with unique details and matching passwords - user added to users.json, redirected to riddles page and flashed message to welcome - SUCCESS
**Test 14** - On home page, clicked log out on nav, redirected to logout page and nav bar returns to options for guest users - SUCCESS
**Test 15** - On log in page, attempted to log in existing user with incorrect password - denied, flashed message to advise - SUCCESS
**Test 16** - On log in page, attempted to log in a user that does not yet exist - denied, flashed message to advise - SUCCESS
**Test 17** - On log in page, attempted to log in an existing user with the correct password - accepted, redirected to home page with customised welcome message, screen goes straight to message - SUCCESS
**Test 18** - On home page, User is clicked on the navbar - redirected to account page prepopulated with any existing user details - SUCCESS
**Test 19** - On account page, updated all user details - page reloads with new details and flashed message to confirm details were updated - SUCCESS
**Test 20** - On riddles page, entered correct answer for riddle - flashed message displays to confirm answer was correct before next riddle fades in - SUCCESS
**Test 21** - On riddles page, entered incorrect answer for riddle - Message displays to advise of incorrect answer, your score, your best score and some guesses that other people made, window closes on button click, game has restarted - SUCCESS
**Test 22** - On riddles page, answered multiple riddles and generated a new high score - leaderboard.html has been updated with new score and ranking order - SUCCESS
**Test 23** - On riddles page, answered all riddles correctly - redirected to congratulations page, game has reset - SUCCESS

These tests have also been performed in different orders to ensure the result and the way the game is displayed is always as intended and no errors have been found.

#### DEVICES

Using Google Chromes toggle device toolbar, I have extensively viewed the page on each of the following devices to ensure that the website looks as it was intended at each media size.  I have also 
tested the website on some live devices via the published heroku link.  The following table signifies which tests have been carried out on each device and the status of each based on 
how the site looks visually:

|DEVICE NAME         |VIRTUAL/DEVICE TESTED           |PAGE VISITED             |STATUS
|--------------------|--------------------------------|-------------------------|-------------------
|iPhone 5            |Virtual(chrome)                 |Index.html               |Renders as intended
|iPhone 6/7/8        |Virtual(chrome)                 |Index.html               |Renders as intended
|iPhone 6/7/8 Plus   |Virtual(chrome)                 |Index.html               |Renders as intended
|iPhone X            |Virtual(chrome)                 |Index.html               |Renders as intended
|Galaxy S5           |Virtual(chrome)                 |Index.html               |Renders as intended
|Galaxy S9           |Actual device                   |Index.html               |Renders as intended
|Pixel 2             |Virtual(chrome)                 |Index.html               |Renders as intended
|Pixel 2 XL          |Virtual(chrome)                 |Index.html               |Renders as intended
|iPhone X            |Virtual(chrome)                 |Index.html               |Renders as intended
|iPad                |Actual device                   |Index.html               |Renders as intended
|iPad Pro            |Virtual(chrome)                 |Index.html               |Renders as intended
|Laptop (15.4 inch)  |Actual device                   |Index.html               |Renders as intended
|Desktop (24 inch)   |Actual device                   |Index.html               |Renders as intended
|iPhone 5            |Virtual(chrome)                 |riddles.html             |Renders as intended
|iPhone 6/7/8        |Virtual(chrome)                 |riddles.html             |Renders as intended
|iPhone 6/7/8 Plus   |Virtual(chrome)                 |riddles.html             |Renders as intended
|iPhone X            |Virtual(chrome)                 |riddles.html             |Renders as intended
|Galaxy S5           |Virtual(chrome)                 |riddles.html             |Renders as intended
|Galaxy S9           |Actual device                   |riddles.html             |Renders as intended
|Pixel 2             |Virtual(chrome)                 |riddles.html             |Renders as intended
|Pixel 2 XL          |Virtual(chrome)                 |riddles.html             |Renders as intended
|iPhone X            |Virtual(chrome)                 |riddles.html             |Renders as intended
|iPad                |Actual device                   |riddles.html             |Renders as intended
|iPad Pro            |Virtual(chrome)                 |riddles.html             |Renders as intended
|Laptop (15.4 inch)  |Actual device                   |riddles.html             |Renders as intended
|Desktop (24 inch)   |Actual device                   |riddles.html             |Renders as intended
|iPhone 5            |Virtual(chrome)                 |about_us.html            |Renders as intended
|iPhone 6/7/8        |Virtual(chrome)                 |about_us.html            |Renders as intended
|iPhone 6/7/8 Plus   |Virtual(chrome)                 |about_us.html            |Renders as intended
|iPhone X            |Virtual(chrome)                 |about_us.html            |Renders as intended
|Galaxy S5           |Virtual(chrome)                 |about_us.html            |Renders as intended
|Galaxy S9           |Actual device                   |about_us.html            |Renders as intended
|Pixel 2             |Virtual(chrome)                 |about_us.html            |Renders as intended
|Pixel 2 XL          |Virtual(chrome)                 |about_us.html            |Renders as intended
|iPhone X            |Virtual(chrome)                 |about_us.html            |Renders as intended
|iPad                |Actual device                   |about_us.html            |Renders as intended
|iPad Pro            |Virtual(chrome)                 |about_us.html            |Renders as intended
|Laptop (15.4 inch)  |Actual device                   |about_us.html            |Renders as intended
|Desktop (24 inch)   |Actual device                   |about_us.html            |Renders as intended
|iPhone 5            |Virtual(chrome)                 |account.html             |Renders as intended
|iPhone 6/7/8        |Virtual(chrome)                 |account.html             |Renders as intended
|iPhone 6/7/8 Plus   |Virtual(chrome)                 |account.html             |Renders as intended
|iPhone X            |Virtual(chrome)                 |account.html             |Renders as intended
|Galaxy S5           |Virtual(chrome)                 |account.html             |Renders as intended
|Galaxy S9           |Actual device                   |account.html             |Renders as intended
|Pixel 2             |Virtual(chrome)                 |account.html             |Renders as intended
|Pixel 2 XL          |Virtual(chrome)                 |account.html             |Renders as intended
|iPhone X            |Virtual(chrome)                 |account.html             |Renders as intended
|iPad                |Actual device                   |account.html             |Renders as intended
|iPad Pro            |Virtual(chrome)                 |account.html             |Renders as intended
|Laptop (15.4 inch)  |Actual device                   |account.html             |Renders as intended
|Desktop (24 inch)   |Actual device                   |account.html             |Renders as intended
|iPhone 5            |Virtual(chrome)                 |congratulations.html     |Renders as intended
|iPhone 6/7/8        |Virtual(chrome)                 |congratulations.html     |Renders as intended
|iPhone 6/7/8 Plus   |Virtual(chrome)                 |congratulations.html     |Renders as intended
|iPhone X            |Virtual(chrome)                 |congratulations.html     |Renders as intended
|Galaxy S5           |Virtual(chrome)                 |congratulations.html     |Renders as intended
|Galaxy S9           |Actual device                   |congratulations.html     |Renders as intended
|Pixel 2             |Virtual(chrome)                 |congratulations.html     |Renders as intended
|Pixel 2 XL          |Virtual(chrome)                 |congratulations.html     |Renders as intended
|iPhone X            |Virtual(chrome)                 |congratulations.html     |Renders as intended
|iPad                |Actual device                   |congratulations.html     |Renders as intended
|iPad Pro            |Virtual(chrome)                 |congratulations.html     |Renders as intended
|Laptop (15.4 inch)  |Actual device                   |congratulations.html     |Renders as intended
|Desktop (24 inch)   |Actual device                   |congratulations.html     |Renders as intended
|iPhone 5            |Virtual(chrome)                 |leaderboard.html         |Renders as intended
|iPhone 6/7/8        |Virtual(chrome)                 |leaderboard.html         |Renders as intended
|iPhone 6/7/8 Plus   |Virtual(chrome)                 |leaderboard.html         |Renders as intended
|iPhone X            |Virtual(chrome)                 |leaderboard.html         |Renders as intended
|Galaxy S5           |Virtual(chrome)                 |leaderboard.html         |Renders as intended
|Galaxy S9           |Actual device                   |leaderboard.html         |Renders as intended
|Pixel 2             |Virtual(chrome)                 |leaderboard.html         |Renders as intended
|Pixel 2 XL          |Virtual(chrome)                 |leaderboard.html         |Renders as intended
|iPhone X            |Virtual(chrome)                 |leaderboard.html         |Renders as intended
|iPad                |Actual device                   |leaderboard.html         |Renders as intended
|iPad Pro            |Virtual(chrome)                 |leaderboard.html         |Renders as intended
|Laptop (15.4 inch)  |Actual device                   |leaderboard.html         |Renders as intended
|Desktop (24 inch)   |Actual device                   |leaderboard.html         |Renders as intended
|iPhone 5            |Virtual(chrome)                 |log_in.html              |Renders as intended
|iPhone 6/7/8        |Virtual(chrome)                 |log_in.html              |Renders as intended
|iPhone 6/7/8 Plus   |Virtual(chrome)                 |log_in.html              |Renders as intended
|iPhone X            |Virtual(chrome)                 |log_in.html              |Renders as intended
|Galaxy S5           |Virtual(chrome)                 |log_in.html              |Renders as intended
|Galaxy S9           |Actual device                   |log_in.html              |Renders as intended
|Pixel 2             |Virtual(chrome)                 |log_in.html              |Renders as intended
|Pixel 2 XL          |Virtual(chrome)                 |log_in.html              |Renders as intended
|iPhone X            |Virtual(chrome)                 |log_in.html              |Renders as intended
|iPad                |Actual device                   |log_in.html              |Renders as intended
|iPad Pro            |Virtual(chrome)                 |log_in.html              |Renders as intended
|Laptop (15.4 inch)  |Actual device                   |log_in.html              |Renders as intended
|Desktop (24 inch)   |Actual device                   |log_in.html              |Renders as intended
|iPhone 5            |Virtual(chrome)                 |logout.html              |Renders as intended
|iPhone 6/7/8        |Virtual(chrome)                 |logout.html              |Renders as intended
|iPhone 6/7/8 Plus   |Virtual(chrome)                 |logout.html              |Renders as intended
|iPhone X            |Virtual(chrome)                 |logout.html              |Renders as intended
|Galaxy S5           |Virtual(chrome)                 |logout.html              |Renders as intended
|Galaxy S9           |Actual device                   |logout.html              |Renders as intended
|Pixel 2             |Virtual(chrome)                 |logout.html              |Renders as intended
|Pixel 2 XL          |Virtual(chrome)                 |logout.html              |Renders as intended
|iPhone X            |Virtual(chrome)                 |logout.html              |Renders as intended
|iPad                |Actual device                   |logout.html              |Renders as intended
|iPad Pro            |Virtual(chrome)                 |logout.html              |Renders as intended
|Laptop (15.4 inch)  |Actual device                   |logout.html              |Renders as intended
|Desktop (24 inch)   |Actual device                   |logout.html              |Renders as intended
|iPhone 5            |Virtual(chrome)                 |sign_up.html             |Renders as intended
|iPhone 6/7/8        |Virtual(chrome)                 |sign_up.html             |Renders as intended
|iPhone 6/7/8 Plus   |Virtual(chrome)                 |sign_up.html             |Renders as intended
|iPhone X            |Virtual(chrome)                 |sign_up.html             |Renders as intended
|Galaxy S5           |Virtual(chrome)                 |sign_up.html             |Renders as intended
|Galaxy S9           |Actual device                   |sign_up.html             |Renders as intended
|Pixel 2             |Virtual(chrome)                 |sign_up.html             |Renders as intended
|Pixel 2 XL          |Virtual(chrome)                 |sign_up.html             |Renders as intended
|iPhone X            |Virtual(chrome)                 |sign_up.html             |Renders as intended
|iPad                |Actual device                   |sign_up.html             |Renders as intended
|iPad Pro            |Virtual(chrome)                 |sign_up.html             |Renders as intended
|Laptop (15.4 inch)  |Actual device                   |sign_up.html             |Renders as intended
|Desktop (24 inch)   |Actual device                   |sign_up.html             |Renders as intended

The wide range of devices tested showed no visual concerns and should prove a good platform to ensure that it displays well on all devices.

### AUTOMATED TESTING:

Using the byotests.py file, a number of tests have been carried out in the test section of run.py to ensure that the core functions of the game are behaving correctly.  Each test was initially built to fail and then adjusted 
to pass.

The first and potentially most important set of tests check to ensure that the correct redirection takes place when a player gives an answer.  There are several scenarios here to ensure that when an answer is given it will always 
result in the expected outcome, which then dictates the path the game should take next.

There are then some test to ensure that the function that tells the player how many words the answer should be is always providing correct information as this is key to making the game as user friendly as possible.  There 
are three different scenarios here to ensure that there aren't any bugs.

Finally there are two tests on the function that creates the order that the riddles are displayed, if this was operating incorrectly then the game could easily break.  The tests check that the number of indices in the list match 
the number of riddles in the file and also that each number indices appears in the list.  By default if both tests pass it tells us that none of the indices are duplicated so the tests cover all eventualities for this function.

#### BUGS

There were two bugs I experienced when creating this site:

1)  It became apparent from user feedback that there was some frustration because their scores and user details were disappearing intermittently when returning to the site.  After some investigation it appears this is 
due to the filing system that is used on Heroku and the fact that this project uses local json files to store data.  Unfortunately any data saved when using Heroku in this way does not persist and so this is one bug that cannot be 
fixed while the site is in it's current form but could be repaired at a later date by using external databases to store the three sets of data instead.

2)  The second bug I experienced earlier in the project was also Heroku related.  If a brand new user set a high score via Heroku and then tried to access the leaderboard, they would receive a getitem error which was not happening for
either existing users or users who signed up via the cloud9 portal.  After some tinkering with the function that created the data that populated the leaderboard I traced the issue back to the way the data was being sorted.  
I then imported itemgetter and used the 'sorted' function to sort the data as a work around and that fixed the bug, however it is still interesting that the original function worked via the cloud9 link!


## DEPLOYMENT:

My code has simply been deployed via heroku pages at the following link - https://hey-riddle-diddle.herokuapp.com/

In order to do this I created a new app on the heroku site and linked to the app via the cloud9 terminal.  

I created a Procfile and requirements.txt file which I then pushed to heroku with the main files.  These tell heroku that this is a web application and what tools in needs to load for the app to run correctly.

On Heroku I have set the config vars to 0.0.0.0 for the IP address and 5000 for the PORT to enable the site to work.

All commits have been made to the same master git branch.  

I also added an environment variable for the applications secret key and changed the debug mode back to false on completion of the site.


## CREDITS:

Content - 
1)  A number of the riddles on this site were taken from the following source - https://www.riddles.com/best-riddles

Media - 
1) File name - riddle-mark.jpg          Taken from - https://wallpapercave.com/the-riddler-wallpaper
2) File name - riddler-left-light.jpg   Taken from - https://wallpapercave.com/the-riddler-wallpaper
3) File name - riddler-lime-left.jpg    Taken from - https://wallpapercave.com/the-riddler-wallpaper
4) File name - riddler-mark.png         Taken from - https://wallpapercave.com/the-riddler-wallpaper
5) File name - riddler-mask.jpg         Taken from - https://wallpapercave.com/the-riddler-wallpaper
6) File name - riddler-right-dark.jpg   Taken from - https://wallpapercave.com/the-riddler-wallpaper
7) File name - riddler-white-right      Taken from - https://wallpapercave.com/the-riddler-wallpaper
8) File name - riddler-right.jpg        Taken from - https://wallpapercave.com/the-riddler-wallpaper
9) File name - riddler-winner.jpg       Taken from - https://wallpapercave.com/the-riddler-wallpaper
10) File name - riddler.jpg                 Taken from - https://wallpapercave.com/the-riddler-wallpaper


## AREAS FOR IMPROVEMENT:

1) Testing - I started by trying to use a test driven development approach to my automated testing and in the early commits you will see that I had built some functions to test the logic of the outcome of the 
answers provided by the user.  As I progressed through the site, in my inexperience other parts of the project clouded my desire to continue with this approach and before I knew it I had become carried away and 
had to retrospectively create some automated testing as a fail safe for the main functions of the site.  I did try to create these tests using a step by step approach in the same way that TDD tests are conducted 
and hopefully you will see from the code that this was a fair effort in that regard.  However going forward I will be more mindful of TDD and try to apply that philosophy to ensure better and more robust development 
practices.


Thank you for reviewing my website!  I hope you liked it as much as I did creating it!  :)