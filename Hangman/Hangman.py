import random
import string
from words import words


def valid_word(words_list):
    word = '-'
    while '-' in word or ' ' in word:
        word = random.choice(words_list)
    return word.upper()


def hangman():
    word = valid_word(words)
    word_letters = set(word)
    alphabets = string.ascii_letters
    used_letters = set()
    lives = 8

    while len(word_letters) != 0 and lives != 0:
        print()
        # print the letters used already
        print("You have {1} lives remaining. You have already used the following letters: {0}".format(
            " ".join(used_letters), lives))

        # print the current word eg - D__E, etc
        lst = ["_" if letter in word_letters else letter for letter in word]
        print("The word is -", "".join(lst))

        # take user input and game logic
        used_input = input("Guess a letter: ").upper()
        if used_input in alphabets and used_letters not in used_letters:
            used_letters.add(used_input)
            if used_input in word_letters:
                word_letters.remove(used_input)
                print("You have correctly guessed one letter.")
            else:
                lives -= 1
                print("Your guess is incorrect!")
        elif used_input in used_letters:
            print("You have already used this letter. Please try again.")
        else:
            print("Invalid Input!! Please try again!!")

    if lives == 0 and len(word_letters) != 0:
        print(f"Sorry! You lost as you have exhausted all the lives. The word was - {word}")
    else:
        print(f"Congratulation, you have guessed the word, {word}, correctly")


hangman()
