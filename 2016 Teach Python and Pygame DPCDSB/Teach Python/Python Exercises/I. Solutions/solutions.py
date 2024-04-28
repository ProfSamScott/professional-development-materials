def countup():
    count = 1
    while count <= 1000:
        print(count)
        count = count + 1

def countup2():
    count = 10
    while count <= 1000:
        print(count)
        count = count + 10

def countup3():
    count = 1
    while count <= 1000:
        if count % 5 == 0 and count % 6 == 0:
            print(count)
        count = count + 1

def addup(n):
    count = 1
    total = 0
    while count <= n:
        newnum = int(input())
        total += newnum
        count += 1
    return total