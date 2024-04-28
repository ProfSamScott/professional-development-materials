"""Solutions for nested loops exercises
Sam Scott, February 2015"""
import random

def lottery_number():
    """ sorry, turns out we don't need a nested loop here"""
    digit1 = random.randint(0,9)
    digit2 = random.randint(0,9)
    while digit1 == digit2:
        digit2 = random.randint(0,9)
    return str(digit1)+str(digit2)

def isprime(n):
    """ returns true if n is prime, otherwise false"""
    if n <= 1:
        return False
    f = 2
    while f <= n**0.5:
        if n % f == 0:
            return False
        f += 1
    return True

def allprimes(limit):
    """ all primes up to and including limit """
    for n in range(1,limit+1):
        if isprime(n):
            print(str(n)+" ",end='')

def allprimes_pretty(limit):
    """ all primes up to and including limit, printed nicely """
    count = 0
    for n in range(1,limit+1):
        if isprime(n):
            print(format(n, '4d'),end='')
            count += 1
            if count % 10 == 0:
                print()

def allprimes2_pretty(numprimes):
    """ pretty-prints the specified number of primes """
    n = 1
    count = 0
    while count <= numprimes:
        if isprime(n):
            print(format(n, '6d'),end='')
            count += 1
            if count % 10 == 0:
                print()
        n += 1    

def getfloat(min, max):
    """ sorry, no nested loop needed here either"""
    goodinput = False
    while not goodinput:
        try:
            num = float(input('Please enter a number between '+str(min)+' and '+str(max)+': '))
            if num >= min and num <= max:
                break
            print('ERROR: Number is out of range.')
        except:
            print('ERROR: That was not a number.')
    return num

def patterns():
    """ solution for 5.18 in Introduction to Java Programming """
    for row in range(1,7):
        for col in range(1, row+1):
            print(str(col)+' ',end='')
        print()
    print('------------')
    for row in range(1,7):
        for col in range(1, 7-row+1):
            print(str(col)+' ',end='')
        print()
    print('------------')
    for row in range(1,7):
        print('  '*(6-row),end='')
        for col in range(row,0,-1):
            print(str(col)+' ',end='')
        print()
    print('------------')
    for row in range(1,7):
        print('  '*(row-1),end='')
        for col in range(1,7-row+1):
            print(str(col)+' ',end='')
        print()

def pyramid():
    """ solution for 5.19 in Introduction to Java Programming """
    for row in range(1,9):
        print('    '*(8-row),end='')
        for col in range(1,row+1):
            print(format(2**(col-1),"4d"),end='')
        for col in range(row-1,0,-1):
            print(format(2**(col-1),"4d"),end='')
        print()        