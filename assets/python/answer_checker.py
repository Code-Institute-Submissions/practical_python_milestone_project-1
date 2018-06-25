from byotests import *

def correct_answer(guess, answer):
    your_guess = str(guess)
    
    # If no answer is provided...
    
    if your_guess == "":
        return "You didn't provide an answer!"
        
    # If the guess matches the answer...
    elif len(your_guess) > len(answer):
        return "Your answer has too many characters"
    elif your_guess.lower() == answer.lower():
        return True
        
    # If the answer and guess dont match...
    else:
        return False

test_guess_is_blank(correct_answer("", "Dog"), "You didn't provide an answer!")
test_guess_is_too_long(correct_answer("Horse", "Dog"), "Your answer has too many characters")
test_guess_matches_answer(correct_answer("dog", "Dog"), True)
test_guess_does_not_match_answer(correct_answer("dog", "cat"), False)

print("All tests have passed")