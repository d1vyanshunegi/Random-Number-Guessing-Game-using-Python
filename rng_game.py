# Random Number Guessing Game

import random

def rng():
    '''
    Function to return a random number between 1 to 100
    '''
    return random.randint(1,100)


continue_parameter = 'Y'   
'''
This variable acts as a condition to continue the game after first round.
Depends on user input.
'''


while continue_parameter == 'Y':
    
    correct_answer = rng() # Random number generated 
    
    print('******************* START *******************')
    print('Guess a number between 1 and 100')
    user_guess = int(input('Enter guess: '))
    user_score = 1 
    '''
    This is a counter that stores number of times user takes to guess correct value
    and outputs it as the score
    '''
    
    while user_guess != correct_answer:
        user_score += 1
        if user_guess > correct_answer:
            print('Too High!')
        else:
            print('Too Low!')
        user_guess = int(input('Enter guess: '))
    
    if user_guess == correct_answer:
        print('*******************')
        print('You Win!')
        print(f'Correct Answer: {correct_answer}\nYour Score: {user_score}')
        print('*******************')
    
    while continue_parameter != 'Y' or continue_parameter != 'N':
        continue_parameter = input('Play Again(Y/N)?').upper()
        if continue_parameter == 'N':
            exit()
        elif continue_parameter == 'Y':
            break
        else:
            print('Enter a valid input!')

exit()