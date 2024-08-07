import random
guess = random.randint(1,6)
print(guess)
if guess == 1:
    print("[-----]")
    print("[     ]")
    print("[  0  ]")
    print("[     ]")
    print("[-----]")
    print("Opps! Better luck next time: ")
    
elif guess == 2: 
    print("[-----]")
    print("[ 0   ]")
    print("[     ]")
    print("[   0 ]")
    print("[-----]")
elif guess == 3:
    print("[-----]")
    print("[     ]")
    print("[0 0 0]")
    print("[     ]")
    print("[-----]")
elif guess == 4:
        print("[-----]")
        print("[0   0]")
        print("[     ]")
        print("[0   0]")
        print("[-----]")
elif guess == 5:
        print("[-----]")
        print("[0   0]")
        print("[  0  ]")
        print("[0   0]")
        print("[-----]")
elif guess == 6:
        print("[-----]")
        print("[0 0 0]")
        print("[     ]")
        print("[0 0 0]")
        print("[-----]")
        print("Wow! You are lucky: ")
