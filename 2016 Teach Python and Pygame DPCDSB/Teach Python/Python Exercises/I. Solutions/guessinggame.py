import random

def guess1():
    n = random.randint(1,10)
    while True:
        x = int(input("I'm thinking of a number from 1 to 10. Guess it: "))
        if x >= 1 and x <= 10:
            break
        print('My number is between 1 and 10. Try again.')
    if x == n:
        print('Correct!')
    else:
        print('Wrong.')

def guess2():
    n = random.randint(1,10)
    while True:
        try:
            x = int(input("I'm thinking of a number from 1 to 10. Guess it: "))
            if x >= 1 and x <= 10:
                break
            print('My number is between 1 and 10. Try again.')
        except:
            print("That wasn't a number! Try again.")
    if x == n:
        print('Correct!')
    else:
        print('Wrong.')

def guess3():
    n = random.randint(1,10)
    x = 0
    while n != x:
        while True:
            try:
                x = int(input("I'm thinking of a number from 1 to 10. Guess it: "))
                if x >= 1 and x <= 10:
                    break
                print('My number is between 1 and 10. Try again.')
            except:
                print("That wasn't a number! Try again.")
        if x == n:
            print('Correct!')
        elif x < n:
            print('Too low.')
        else:
            print('Too high')