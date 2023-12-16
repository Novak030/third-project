import random

word_list = ["magical", "london", "berlin", "jazz", "thrilling", "invincible"]

word = random.choice(word_list)

health = 6

blank_word = []

for i in range(0, len(word)):
    blank_word.append("_")

while True:
    print(blank_word)
    char = input("\nguess: ")

    if char in word:
        print("Correct!")
        for i in range(0, len(word)):
            if char == word[i]:
                blank_word[i] = char

    else:
        health -= 1  # health = health -1
        print(f"health remaining {health}")
    
    if "_" not in blank_word:
        print("You won!")
        break
    elif health <= 0:
        print("You lost!")
        break