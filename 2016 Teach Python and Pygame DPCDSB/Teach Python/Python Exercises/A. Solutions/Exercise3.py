"""Solution to exercise 3 from the chapter 2 handout
Sam Scott, January 2015"""

print("First Name?")
first = input()
print("Last Name?")
last = input()
print("Favorite positive integer?")
num = int(input())
msg = ("Hello "+first+" "+last+"! ")*num
print(msg)