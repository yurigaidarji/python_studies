from random import randint

answer = 0
EASY_LEVEL_TURNS = 10
HARD_LEVEL_TURNS = 5

#choosing a random number
def game_setup():
    print("Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100.")
    return randint(1,100)

#Function to check users' guess
def check_answer(user_guess, correct_answer):
    if user_guess > correct_answer:
        print("Too high")
    elif user_guess < correct_answer:
        print("Too low")
    else:
        print(f"You got it! The answer was {correct_answer}")

#Setting the dificulty
def set_difficulty():
    level = input("Choose a difficulty. Type 'easy' or 'hard': ")
    if level == 'easy'
        return EASY_LEVEL_TURNS
    else:
        return HARD_LEVEL_TURNS


answer = game_setup()
turns = set_difficulty()
# Let the user guess a number
guess = int(input("Make a guess: "))
