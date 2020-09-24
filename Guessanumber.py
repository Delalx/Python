import random

hidden = random.randrange(1, 51)

#Boolean
win = False

while win == False:
    guess = int(input("Please enter your guess: "))
    if guess == hidden:
        win = True
        print("Hit!")
    elif guess < hidden:
        print ("Your guess is too low")
    else:
        print("Your guess is too high")
