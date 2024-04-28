""" Sample solutions for numpy exercises 
Sam Scott, Mohawk College, 2019
"""
import numpy as np
import csv

print("\nExercise 1")
a = np.random.randint(-1000000,1000000,(100,100))
print(a.min(), a.max(), a.mean())

print("\nExercise 2")
sums = a.sum(axis=1)
print(sums.max(), sums.min(), sums.mean())

print("\nExercise 3")
maxrow = a[sums.argmax()]
print(maxrow.min(), maxrow.max())

print("\nExerise 4")
x = np.random.randint(-100, 100, 20)
y = np.random.randint(100, 200, 20)
print (x.min(), y[x.argmin()])
sort = y.argsort()
y = y[sort]
x = x[sort]
print (x.min(), y[x.argmin()])

print("\nExerise 5")
distance = ((x-100)**2 + (y-100)**2)**0.5
print(distance[x.argmin()])

print("\nExerise 6")
close_x = x[distance <= 100]
close_y = y[distance <= 100]
close = distance[distance <= 100]
print(close_x)
print(close_y)
print(close)