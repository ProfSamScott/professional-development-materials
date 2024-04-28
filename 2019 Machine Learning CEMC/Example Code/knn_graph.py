""" Visualizing the Decisions - kNN

In this example, a decision tree classifier is trained using
the first two features of the iris data set. This is a difficult 
classification task with only those two dimensions.

The first figure shows the correct classifications.

The remaining figures shows how every point in the space would get 
classified, so that you can see the decision boundaries.

Sam Scott, Mohawk College, 2018"""

from sklearn import datasets
from sklearn.neighbors import KNeighborsClassifier
from matplotlib import pyplot as plt
import numpy as np

## Load a data set
dataset = datasets.load_iris()

## Graph Size
xlim=[4,8]
ylim=[1.5,4.5]
plt.figure("kNN Decision Boundaries", figsize=(10,6.67))

## Graph the Actuals
plt.subplot(231)
plt.title("Correct Classifications")
plt.xlim(xmin=xlim[0], xmax=xlim[1])
plt.ylim(ymin=ylim[0], ymax=ylim[1])
plt.scatter((dataset.data[dataset.target==0])[:,0], (dataset.data[dataset.target==0])[:,1],color="red")
plt.scatter((dataset.data[dataset.target==1])[:,0], (dataset.data[dataset.target==1])[:,1],color="blue")
plt.scatter((dataset.data[dataset.target==2])[:,0], (dataset.data[dataset.target==2])[:,1],color="green")

## Create a points grid 100x100
min = np.array([xlim[0],ylim[0]])
max = np.array([xlim[1],ylim[1]])
ranges = max-min
points = []
x = min[0]
while x <= max[0]:
    y = min[1]
    while y <= max[1]:
        points += [[x,y]]
        y += ranges[1]/100
    x += ranges[0]/100
    
points = np.array(points)


## Show Prediction Spaces
i = 2
for k in [1, 3, 7, 11, 15]:
    clf = KNeighborsClassifier(n_neighbors=k)
    clf.fit(dataset.data[:,:2], dataset.target)
    pred = clf.predict(points)
    plt.subplot(230+i)
    i += 1
    plt.title("k = "+str(k))
    plt.xlim(xmin=xlim[0], xmax=xlim[1])
    plt.ylim(ymin=ylim[0], ymax=ylim[1])
    plt.scatter((points[pred==0])[:,0], (points[pred==0])[:,1],color="red", marker=".")
    plt.scatter((points[pred==1])[:,0], (points[pred==1])[:,1],color="blue", marker=".")
    plt.scatter((points[pred==2])[:,0], (points[pred==2])[:,1],color="green", marker=".")

plt.show()