import random
words = ("toy", "rainbow", "pool", "tinkuu", "towel", "actor", "sambhar")
choice = random.choice(words)
while True:
    word = input("guess the letter: ")
    guess = ""
    for char in choice:
        if char in guess:
            print(char, end="")
        else: 
            print("__")