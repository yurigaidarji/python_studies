import random

is_end_game = False

def generate_number(min, max):
    return random.randint(min, max)

def evaluate_guess(guess, answer):
    if guess == answer:
        print(f"You got it! The answer was {answer}")
        return 0
    elif guess > answer:
        print("Too High")
        return 1
    else:
        print("Too Low")
        return 1


print("Welcome to the Number Guessing Game!")
print("I'm thinking of a number between 1 and 100.")
pc_number = generate_number(1,100)
print(f"Number is {pc_number}")
user_difficulty_mode = input("Choose a difficulty. Type 'easy' or 'hard': ")
user_chances = 5 #hard by default

if user_difficulty_mode == 'easy':
    user_chances = 10

while not is_end_game:
    if user_chances >= 1:
        print(f"You have {user_chances} attempts remaining to guess the right number.")
        user_guess = int(input("Make a guess: "))
        guess_result = evaluate_guess(user_guess, pc_number)
        if guess_result == 0:
            is_end_game = True
        user_chances -= guess_result
    else:
        print("Refresh the page to start again.")
        is_end_game = True