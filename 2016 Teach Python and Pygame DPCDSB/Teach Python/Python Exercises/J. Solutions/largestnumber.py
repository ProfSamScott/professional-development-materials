print('Enter 10 numbers')
largest = float(input())
count = 2
while count <= 10:
    x = float(input())
    if x > largest:
        largest = x
    count = count + 1
print('Largest:',largest)