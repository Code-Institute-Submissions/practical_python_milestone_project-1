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

Story 1:  As a 

Story 2: As a gamer, I want to play a new easy going game to relax.

Story 3:  As a lover of gaming music, I want to play a game that has some ear catching tunes.

Story 4:  As a gaming enthusiast, I want to play a game that tells me how great I am!

A memory game is perfect for the majority of these users.  Memory games have been proven to help keep the memory sharp and are reliably stress and hassle free.  
It will incorporate two game modes to keep it interesting.  'Classic', which will mirror the original SIMON game, and 'Picture', which will allow the user
to see a part of the picture for every square they click correctly.  There will be 12 buttons in this mode and 12 pictures for the user to uncover.  There will be 
a music track for each game mode. There should also be options for the user to experiment with such as game speed and game difficulty.  The game will feature a scoring 
system of sorts and will apply a category to a user dependant on their progress which will then display a message on completion.


### WIREFRAMES:
This will be a Single-Page Application with the game being the only focus.  I have designed it to be very simple and have decided it should be split into 3 sections, the header, the game mode box for selecting
which game to play and the game buttons themselves, which will switch to being the feedback area at the end of each game.  As it is a single page application I would like it to keep the same format on 
all devices and simply scale it down to maintain and hold the whole content to the size of the users screen, so what you will see on mobile will be the same as you would see on desktop.  This is a simple
pick up and play on the go game in principle and therefore I have chosen to go with a mobile first approach.  **Please see the Wireframes folder for the design.**

## FEATURES

### EXISTING FEATURES:

#### PAGE 1 - SINGLE PAGE APPLICATION (index.html):

All of the contents of this site will sit within index.html.  As the page loads, a logo that I have designed will appear as if an app was loading on a smartphone to show the user who the game is made by.
This logo quickly fades out and displays the main contents of the site.

There is a h1 at the top of the screen which can also be used to redirect to the page, effectively resetting the game.  It spins vertically too, the majority of the boxes do not have moving images, they just simply
fade in and out in sync with each other, so the animation on the header just provides something interesting and eye catching on the page.  

In the second part of the page is the first sliding box.  At the top of this box are two icons that are utilised as buttons.  When clicked, the first box displays the game settings and allows the user to choose 
the speed and difficulty of the game, as well as whether or not to allow the application to play the sounds or in game music.  The difficulty applies to the classic mode of the game and will set the maximum
number of levels the player needs to complete to win, this is initially set at 6 levels for easy, 10 for normal and 15 for hard (these were chosen after user testing and those numbers felt right).  The second icon will
display the rules of the game when clicked.  Both displays cover the whole screen.

In the center of the first sliding box a welcome message displays and a 'play now' button.  On click, a sound effect plays and changes to the mode selection box.  Here, 'classic' or 'picture' modes can be selected.
If the mode selected is not the same as the game mode ready to be played, the bottom section will change between 4 buttons (classic mode) and 12 (picture mode).  A button will also appear in the first section
for the player to click when ready to start the game.

On start, a series of messages will be displayed before the player can click a game button.  When the 'repeat' message is displayed, the player can then chose the button/s they wish to click.  When the game is over,
a message is displayed in the upper box as well as an option to try either mode again, and a feedback box is displayed in the bottom section to tell the player how they have performed.

### FUTURE FEATURES:

#### Endless game mode:
Another mode that could be incorporated for the classic mode is endless mode where the player keeps playing to clock up the highest score.  This could then lead to a leaderboard and provide more incentive to return to 
the game.  This would work best if a database was utilised so that the score could be stored permanently, as currently the score would be reset every time the user refreshes the site but this could be incorporated in 
the future.

#### Picture Game difficulty:
To make the picture game more accessible a difficult level could be set to dictate how many boxes cover the picture.  12 boxes is currently moderately difficult so an 8 and 15 box version could be applied.

#### All out memory game:
If the scoring system was improved and the endless mode was incorporated, the game could be used as an all out memory game and users could be scored from grades E to A+ on their memory abilities, with additional feedback on
their performance.  Tips could also be displayed on how to sharpen your memory at each grading which the user may find generally useful and hopefully help them with the game.

## TECHNOLOGIES USED:

#### 1:  NAME - JQuery

LINK - https://jquery.com/

REASON - Jquery has been used as it provides some very useful methods when working with javascript and these have often been utilised throughout my javascript code.

#### 2: NAME - Google Fonts

LINK - https://fonts.google.com/

REASON - Used to style the two types of fonts incorporated into the style of the site.

#### 3: NAME - Font Awesome

LINK - https://fontawesome.com/

REASON - Font awesome has been used to incorporate its icons onto the site as it has multiple options to ensure that the icon used is relevant to the content it is being used for, in this case a cog for the settings box
and a question mark for the instructions box.

#### 4:  NAME - Howler.JS

LINK - https://howlerjs.com/

REASON - I wanted to incorporate responsive sounds and music into my game.  Having played around with this in vanilla javascript I found there were delays when playing sounds which didn't allow them to sync with the 
things that were happening in the game.  After some research I found howler js and started experimenting.  Not only does this audio library allow sounds to be played when required, it also allows attributes like volume 
to be easily amended which helped the sound settings buttons to be implemented easily.

#### 5: NAME - SASS

LINK - https://sass-lang.com/

REASON - Sass has really helped me to organise my css code and has some really useful features such as the way it handles media queries which makes this part of styling much less painful.  It also helps the site to load 
faster through the use of placeholders which are only used when called upon.

## WEBSITE TESTING:

#### UX

The website has been designed to meet the needs of the users described in the user stories section.  Here is a brief run down of how each has been met - 

Story 1:  As a member of the older generation, I want to play a memory game to keep my memory sharp!

REFLECTION - The game works well in testing the users memory.  Feedback I have gathered from friends and family is that some struggle to complete it and others find it easy, but it definitely encourages
them to try to concentrate and engage their brainpower to try and beat it, which helps get the memory active.

Story 2: As a gamer, I want to play a new easy going game to relax.

REFLECTION - There isn't anything stressful about the game and it's designed to be a little quirky.  The sound effects and pictures help to throw some additional enjoyment into the game in an 
attempt to help the user to have fun and therefore relax.

Story 3:  As a lover of gaming music, I want to play a game that has some ear catching tunes.

REFLECTION - I have created two very different tracks on a program called FL Studio which I hope users will enjoy.  Music is often very iconic in gaming and these tunes try to have just enough variation
in their looping design to get into the users head, hopefully for their enjoyment!

Story 4:   As a gaming enthusiast, I want to play a game that tells me how great I am!

REFLECTION - Although the scoring system could be improved it does provide working feedback for the user although is currently limited.  An area for improvement but at least the mechanic is available in the 
initial version of the game.

#### STYLING

As previously stated, the design of this single page site is very straight forward and should appear about the same on every screen size.  

Each element on the site has been tested to ensure it functions as intended as follows:

**Test 1** - On Page Load - Company Logo appears and fades out after a few moments - SUCCESS

**Test 2** - Header is clicked - Page reloads - SUCCESS

**Test 3** - Cog icon clicked - Game settings appear on full screen - SUCCESS

**Test 4** - Game settings close button clicked - Game settings close and main screen appears - SUCCESS

**Test 5** - Question mark icon clicked - How to play page appears on full screen - SUCCESS

**Test 6** - Instructions close button clicked - Instructions close and main screen appears - SUCCESS

**Test 7** - Play now button is clicked - Game mode buttons appear - SUCCESS

**Test 8** - Classic button is clicked - Start button appears - SUCCESS

**Test 9** - Start button is clicked - Game begins - SUCCESS

**Test 10** - Game button is clicked until game ends - Feedback messages appear and try again mode buttons - SUCCESS

**Test 11** - Picture Mode button is clicked - Start button appears, game mode changes in bottom section - SUCCESS

**Test 12** - Start button is clicked - Game begins - SUCCESS

**Test 13** - Game button is clicked until game ends - Feedback messages appear and try again mode buttons - SUCCESS

These tests have also been performed in different orders to ensure the result and the way the game is displayed is always as intended and no errors have been found.

#### DEVICES

Using Google Chromes toggle device toolbar, I have extensively viewed the page on each of the following devices to ensure that the website looks as it was intended at each media size.  I have also 
tested the website on some live devices through the github published github pages link.  The following table signifies which tests have been carried out on each device and the status of each based on 
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

The wide range of devices tested showed no visual concerns or than on the actual ipad device but should prove a good platform to ensure that it displays well on all devices.

BUG - On the ipad there appeared to be an issue with the settings and instruction screens when they appeared on top of the rotating header.  When settings or instructions were open, this caused the screen to 
flicker and uncover some of the main page which was not intended.  After some research it seems this may be a bug in Safari which relates to rotate3d.  After putting the flipInX animation class through 
the Autoprefixer CSS online tool to try and add any missing vendor prefixes, I found that the same issue still occurred.  Therefore I added some javascript to remove the animation held within the flipInX class 
each time the menus were opened, and then to add it again once they were closed.  This appears to have resolved the issue in a simple and effective manner.

### JAVASCRIPT TESTING:

The main.js file has been written to include a step by step annotation of how the code works which is then complimented by the mainSPec.js file containing the Jasmine testing suite.  The testing suite can 
be run via the jasmine.html file which will then execute the tests.

In principle the creation of the game is quite simple.  Each time the game is played, an array of numbers will be created and used to light up the relevant game buttons.  Therefore the first set of tests ensures that
this initial array is created as expected in the "Set Up" section of tests.

In the classic game, a single number should be generated randomly between 1 and 4 and pushed into the array, so the first test ensures this is always the case.  The next test makes sure that the length of those
numbers is equal to the maximum number of levels (affected by the users settings of an easy, medium or hard game difficulty).

In the picture game mode, there are 12 buttons that can be clicked and each will only appear in the array once, so the next tests check this to ensure it is happening every time.

There are then two sets of almost identical tests, one for classic and one for picture mode.  When a user clicks on a button, the button clicked gets pushed into the array and the logic of the game checks if it matches
and then if it does, what to do next dependant on where the player is in the game.  These tests were written to ensure that the right game outcome method is called which can be either:

1. The player has selected the incorrect button, and therefore only the game over method is called
2. The player has selected the right button and is at a point that they can move onto the next level and only the next level game outcome is called
3. The player has selected the right button and is at a point that they have made it to the last number in the array and only the victory game outcome is called

To an extent, these tests are somewhat hardcoded, but during the testing I have changed some of the variables on these to make sure they still work.  Initially I had two fucntions for the main game logic - 
recordButtonAndEvaluate, which I used once for the classic game and a separate instance of the function called recordButtonAndEvaluatePic for the picture game.  I noticed that these were very similar so 
I refactored these to make one function that would work in each game.  This broke the tests for the picture game which I then had to adjust to make sure the suite worked again.  This provided some additional evidence
that the tests were robust.

#### BUGS

There were main bugs that I had to put right when developing the js code.

1)  When the game logic was first created there was an issue when a player levelled up to round 2 of the game.  When a button was clicked in round 2, the game would immediately end with game over, unless it was the same
button that has flashed twice, in which case the player would level up after the first click.  After testong and research it appeared that the button was being bound in javascript, so after being clicked once the next 
time it was clicked it would fire twice.  I'm still not 100% certain what causes this but I used the jquery unbind method to stop this from happening as suggested on stack overflow which worked very well.

2)  In the later stages of development, after the game had ended I found that if I clicked a game button a game outcome method would fire and interrupt the ending sequence giving unintended results.  Therefore I added an 
endGame boolean variable that switched at the start and conclusion of the game to ensure a player couldn't continue to click buttons and activate methods after the game had been completed.

## DEPLOYMENT:

My code has simply been deployed via github pages at the following link - https://ebaymademepoor.github.io/ifd_milestone_project/

It can also be run via preview in the Cloud9 IDE.

All commits have been made to the same master git branch.  No additional configuration files are required.

## CREDITS:

Content - 
1)  No written content on this site has been taken from any particular source

Media - 
1) File name - clever.png  Taken from - https://mrmen.fandom.com/wiki/Mr._Clever
2) File name - einstein.jpg Taken from - http://clipart-library.com/einstein-cartoon-image.html
3) File name - logo.png - created by myself
4) File name - patrick.jpg  Taken from - http://www.fanpop.com/clubs/spongebob-squarepants/images/31126065/title/classic-patrick-fanart
5) File name - pic1.jpg  Taken from - https://knowyourmeme.com/photos/92167-minecraft-creeper
6) File name - pic2.jpg  Taken from - https://www.google.co.uk/search?q=under+the+world&source=lnms&tbm=isch&sa=X&ved=0ahUKEwjQsquz8tjeAhUlI8AKHRaiCTEQ_AUIDygC&biw=1920&bih=938#imgrc=RCgqkjTTiKPTyM:
7) File name - pic3.jpg  Taken from - http://wall-a-day.blogspot.com/2012/07/red-un-happy-happy-face-yellow-smiley.html
8) File name - pic4.jpg  Taken from - https://www.pinterest.co.uk/pin/148689225168468096/?lp=true
9) File name - pic5.jpg  Taken from - funzug.com
10) File name - pic6.jpg  Taken from - http://wallpaperswide.com/stormtrooper_converse-wallpapers.html
11) File name - pic7.jpg  Taken from - google images (source unknown)
12) File name - pic8.jpg  Taken from - http://7-themes.com/7021941-orange-fruit-splash.html
13) File name - pic9.jpg  Taken from - http://pictures.4ever.eu/cartoons/dark-arts/grim-reaper-145466
14) File name - pic10.jpg  Taken from - https://skirmishfrogs.com/2016/07/13/the-moment-the-legend-of-zelda-windwaker/
15) File name - pic11.jpg  Taken from - google images (source unknown)
16) File name - pic12.jpg  Taken from - https://www.pinterest.co.uk/pin/425871708497346706/?lp=true
17) File name - trump.jpg  Taken from - https://www.redbubble.com/people/stuffyoubuy/works/24397298-donald-trump-cartoon-toon-drawing-funny-crazy-election?p=photographic-print

All game sounds and music were created by myself via FL Studio.

Acknowledgements - 
1) The website has been created inspired by the SIMON game - https://en.wikipedia.org/wiki/Simon_(game) & https://www.youtube.com/watch?v=1Yqj76Q4jJ4

## AREAS FOR IMPROVEMENT:

1) Testing - I'm unsure as to the level of testing that should be undertaken and whether what is currently in place is enough.  I will use any feedback from this submission to enhance future projects.
2) Design - The design of the website is very simple and could be improved upon to make it more eye catching.

Thank you for reviewing my website!  I hope you liked it as much as I did creating it!  :)