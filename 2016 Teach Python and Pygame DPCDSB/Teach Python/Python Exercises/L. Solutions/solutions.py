import random

def createList(value, length):
    return [value]*length

def createList2(value, length):
    if isinstance(value, list):
        newlist = value * (length // len(value) + 1)
        return newlist[:length]
    else:
        return [value]*length

def randomElement(l):
    try:
        return l[random.randint(0,len(l)-1)]
    except TypeError:
        print('ERROR: That was not a list!')    
    except ValueError:
        print('ERROR: That was an empty list!')

def randomSlice(l):
    try:
        start = random.randint(0,len(l)-1)
        end = random.randint(start+1,len(l))
        return l[start:end]
    except TypeError:
        print('ERROR: That was not a list!')    
    except ValueError:
        print('ERROR: That was an empty list!')

def addWord(l, w):
    i = random.randint(0,len(l)-1)
    while l[i] != '':
        i = random.randint(0,len(l)-1)
    l[i] = w
    return i

def fixLength(l, n):
    if len(l) > n:
        return l[:n]
    return l+[0]*(n-len(l))

def insertCopy(a, b, i):
    newlist = a[:i]+b+a[i:]
    return newlist

def findSecretMessage():
    l = ['']*20
    addWord(l,'Python')
    addWord(l,'is')
    addWord(l,'great')
    score = 0
    while score != 3:
        score = 0
        print('Enter three guesses between 0 and',len(l))
        a = int(input())       
        if a == -1:
            print(l) # debugging
        b = int(input())   
        c = int(input())
        if l[a] != '':
            score += 1
        if a != b and l[b] != '': 
            score += 1
        if a != c and b != c and l[c] != '':
            score += 1
        print('You found',score,'of the 3 words')
    print('Congrats! You found the message "Python is great".')

def findSecretMessage2():
    l = ['']*20
    positions = [addWord(l,'Python'), addWord(l,'is'), addWord(l,'great')]
    correct = 0
    while correct != 3:
        correct = 0
        close = 0
        print('Enter three guesses between 0 and',len(l))
        a = int(input())       
        if a == -1:
            print(l) # debugging
        b = int(input())   
        c = int(input())
        if a == positions[0]:
            correct += 1
        elif a == positions[1] or a == positions[2]:
            close += 1
        if b == positions[1]:
            correct += 1
        elif b == positions[0] or b == positions[2]:
            close += 1
        if c == positions[2]:
            correct += 1
        elif c == positions[0] or c == positions[1]:
            close += 1
        print('Found',correct,'in correct place and',close,'in wrong place.');
    print('Congrats! You found the message "Python is great".')