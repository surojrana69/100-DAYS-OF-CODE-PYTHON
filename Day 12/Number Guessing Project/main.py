from random import randint

EASY_LEVEL=10
HARD_LEVEL=5

turns=0

#THIS FUNCTION WILL CHECK USER GUESSES WITH ACTUAL ANSWER
def check_answer(user_guess,actual_answer,turns):
    if user_guess > actual_answer:
        print("You guess is too high ")
        return turns -1

    elif user_guess < actual_answer:
        print("Your gess is too low")
        return turns -1
    else:
        print(f"You are correct! The answer is {actual_answer}")

#FUCNTION FOR DIFFICULTY SET

def difficulty():
    level=input("Choose a difficulty. Type 'easy' or 'hard':")
    if level=='easy':
        return EASY_LEVEL
    else:
        return HARD_LEVEL

from art import  logo
print(logo)

def game():
    print("Welcome to Number Guessing Gaming!")
    print("Please choose the number between 0 and 100")
    answer=randint(0,100)
    print(answer)

    turns = difficulty()


    guess=0
    while guess!=answer:
        print(f"You have {turns} attempts remaining to guess the number.")
        guess=int(input("Write your guess: "))
        turns=check_answer(guess,answer,turns)
        if turns==0:
            print("You have used your all attempts. Try Again!")
            return
        elif guess!=answer:
            print("Guess again")
game()