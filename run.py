import random

word_list = ["magical", "london", "berlin", "jazz", "thrilling", "invincible",]

word = random.choice(word_list)

char = input("guess: ")

if char in word:
    print("yes!")
else:
    print("No!")
