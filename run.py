import random

word_list = ["magical", "london", "berlin", "jazz", "thrilling", "invincible",]

word = random.choice(word_list)

health = 6

blank_word = []

for i in range(0, len(word)):
    blank_word.append("_")

print(word)
print(blank_word)



while True:
    char = input("guess: ")

    if char in word:
        print("yes!")
    else:
        print("No!")
health -= 1  # health = health -1
