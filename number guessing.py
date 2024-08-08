import random
choice = random.randint(1,10)
while True:
    num = int(input("Guess the number :" ))

    if num == choice:
        print("Yes! You won the game: ")
        break
    elif num>choice:
        print("you have guessed number too high: ")
    elif num<choice:
        print("you have guessed number too low: ")
    else: 
        print("Opps you lost: ")