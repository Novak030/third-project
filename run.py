# imports random module
import random
import Pyfiglet
# list of words to guess
word_list = ["magical", "london", "berlin", "jazz", "thrilling", "invincible"]
# gets a random word from the list
word = random.choice(word_list)
# number of guesses
health = 6


def welcome():
    """
    Welcome text for the user before the game starts.
    """
    print("Welcome! Here, you can enjoy a game of Hangman.")
    print("The rules are straightforward.")
    print("Pick a letter until you guessed the right word.")
    print("You must do it before your health run's out.")
    print("Lets play!\n")


welcome()

blank_word = []

"""Main section how the game works"""
for i in range(0, len(word)):  # gets the length of the actual word
    blank_word.append("_")

while True:
    print(blank_word)
    char = input("\nguess the word: ")

    if char in word:  # checks if guessed letter is found in the word
        print("\nCorrect!\n")
        for i in range(0, len(word)):
            if char == word[i]:
                blank_word[i] = char

    else:
        health -= 1  # health = health -1
        print(f"\nhealth remaining {health}\n")

    if "_" not in blank_word:
        print("You won!")
        break
    elif health <= 0:  # condition for loosing
        print("You lost!")
        break
