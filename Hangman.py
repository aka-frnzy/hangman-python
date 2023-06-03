# importing required modules
import random
from asciihangman import hangman
import os
import platform
import time
from logo import logo
from wrong import wrong
from correct import correct
from Final import LOST, WON


# For Clearing The Console
def clear_console():
    if platform.system() == "Windows":
        os.system("cls")
    else:
        os.system("clear")


def main():
    """This is main Function for The Hangman Code I Wrote"""
    # hangman_logo
    print(logo)
    time.sleep(1)
    clear_console()
    # Required Variables
    lives = 6
    gameOver = False
    hint1 = 0
    hint2 = 0

    # Response for Getting Word List from Online
    word_list = []
    file = open("wordlist.txt", "r")
    word = file.read()
    file.close()
    word_list = word.split("\n")
    # Other Variables
    word_chosen = random.choice(word_list)
    word_length = len(word_chosen)
    hint1 = random.randint(0, word_length - 1)
    hint1 = random.randint(0, word_length - 1)
    display = ["_" for i in range(len(word_chosen))]

    # Adding two hints
    display[hint1] = word_chosen[hint1]
    display[hint2] = word_chosen[hint2]

    # Main Game loop:
    while gameOver == False:
        print(hangman[lives], end=" ")
        print(f"\n====Remaining Lives: {lives}=========\n")
        print(display)
        guess = input("Guess The Letter:").lower()
        for position in range(word_length):
            if word_chosen[position] == guess:
                clear_console()
                display[position] = guess
                print(correct)
                time.sleep(0.5)
                clear_console()
        if guess not in word_chosen:
            lives -= 1
            clear_console()
            print(wrong)
            time.sleep(1)
            clear_console()
        if "_" not in display or lives == 0:
            gameOver = True
    if lives == 0:
        print(LOST)
        print(f"The word was {word_chosen}")
    else:
        print(WON)
        print(display)


if __name__ == "__main__":
    main()
