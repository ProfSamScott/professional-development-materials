"""This file is a demonstration of a few features of arrays that are not 
covered in the "Introduction to Numpy and Scipy" readings. This assumes that
you are already familiar with at least pages 3 to 14 of that reading.

Sam Scott, Mohawk College, 2017"""

import numpy as np

# creating a random array
print("RANDOM ARRAY")
a = np.random.randint(-100,100,(5, 3)) # third parameter is the array shape
print(a)

# broadcasted array operations
print("\n\nBROADCASTING SINGLE VALUE")
a = a * 2
print(a)

# broadcasting with rows
print("\n\nBROADCASTING A ROW")
multipliers = np.array([10,100,1000])
a = a * multipliers
print(a)

# using a step value on a slice (this also works with ordinary lists)
print("\n\nUSING A STEP VALUE WITH A SLICE")
a = np.arange(1000)  # this creates an array with ints from 0 to 999
print(a[2:20:2])      # this prints from index 2 to 19 with a step of 2
print(a[20:2:-1])     # this prints from index 20 to 3 with a step of -1 
print(a[-1:-100:-10]) # prints from last index down to 99th last index by 10

a = a[::-1]          # reverses the array

# access a list of indices
print("\n\nUSING A LIST OF INDICES")
indices = [55, 100, 200]
print(a[indices])    # prints index 55, 100, and 200 from a (now reversed)
print(a[ [a.argmax(),a.argmin()] ])    # prints highest and lowest in a

# using argsort with related arrays
print("\n\nARGSORT WITH RELATED ARRAYS")
names = np.array( ["Ahmad", "Betty", "Christopher", "Daphne", "Ernesto"]) #players
scores = np.array([1000,        592,           222,     1001,         4], dtype=int) #scores

print(scores)
print(scores.argsort())  # shows the indices from scores in ascending order
print(scores.argsort()[::-1])  # shows the indices from scores in descending order
print(names[scores.argsort()[::-1]] )  # shows the player names from highest to lowest score
