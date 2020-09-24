import random
target_num, guess_num = random.randint(1, 50), 0

guess_num = int(input('Guess a number between 1 and 50 until you get it right : '))

while target_num != guess_num:
    if guess_num>target_num:
        print("Your guess it too high")
        guess_num = int(input('Guess a number between 1 and 50 until you get it right : '))
    elif guess_num<target_num:
        print("Your guess it too low")
        guess_num = int(input('Guess a number between 1 and 50 until you get it right : '))
print('Well guessed!')