### Guess the number ###
""" This program is a guessing game. The user has 10 guesses to correctly guess a number generated internally by the
 computer. each time the user will get a hint weather the number he entered is greater or smaller than the actual number
 Print no. of guesses remaining in each iteration. Print game over in case all guesses exhausted. Print no. of guesses
 he took. Print you win when user guesses correctly"""

import random


def game_logic(x):
    guess = 0
    num = random.randrange(1, x)

    print(f"\nHello! Welcome to the guessing game. you have 10 guesses to guess the number hidden in the computer."
          f"Happy guessing\nGuess a number between 1 and {x}\n")

    while True:
        guess = guess + 1
        user_input = input("Enter your guess: ")
        print()

        if guess >= 10:
            print("Game over! Hard Luck")
            break
        elif not user_input.isnumeric():
            print("invalid input!", f"You have {str(10 - guess)} guesses remaining!\n")
        elif int(user_input) == num:
            print(f"Congratulation! You Win. You took {str(guess)} guesses to win")
            break
        else:
            print("Your guess is wrong!", end="")
            if int(user_input) > num:
                print("The number you entered is Greater than the hidden number")
            else:
                print("The number you entered is Less than the hidden number")
            print(f"You have {str(10 - guess)} guesses remaining!\n")


game_logic(10)
