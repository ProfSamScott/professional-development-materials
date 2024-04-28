# THE QUICK LIST PROCESSING EXERCISES
def printList(l):
    for e in l:
        print(e)

def printListReverse(l):
    for i in reversed(range(len(l))): # an you do this without "reversed"?
        print(l[i])

def printListN(l, n):
    for i in range(0,len(l),n):
        print(l[i])

def getbiglist(n):
    biglist = [0]*n
    for i in range(len(biglist)):
        biglist[i] = i+1
    return biglist

# MAP, FILTER, REDUCE EXERCISES
def largest(l): # reduce (or filter)
    """returns largest element in list l"""
    if not isinstance(l, list):
        print("error - not a list")
        return None
    if l == []:
        print("error - empty list")
        return None
    largestSoFar = l[0]
    for element in l:
        if element > largestSoFar:
            largestSoFar = element
    return largestSoFar

def average(l): # reduce
    total = 0
    for e in l:
        total += e
    return total / len(l)

def lastDigits(listin): # map
    listout = listin[:] # copy original list
    for i in range(len(listout)):
        listout[i] = listout[i] % 10
    return listout

def betterThanAvg(listin): # filter
    avg = average(listin)
    listout = []
    for e in listin:
        if e >= avg:
            listout.append(e)
    return listout

def removeDuplicates(listin): #filter
    listout = []
    for e in listin:
        if e not in listout:
            listout.append(e)
    return listout

# STRING PROCESSING EXERCISES
def reverse_sentence(sentence):
    slist = sentence.split()
    result = []
    for word in slist:
        result = [word] + result
    return ' '.join(result)