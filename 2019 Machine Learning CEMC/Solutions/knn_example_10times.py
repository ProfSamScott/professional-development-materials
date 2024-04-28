""" Example of loading, preparing, normalizing, and classifying a built-in data set from sklearn. 

General Info...
https://scikit-learn.org/stable/modules/neighbors.html#nearest-neighbors-classification

The KNeighborsClassifier Object...
https://scikit-learn.org/stable/modules/generated/sklearn.neighbors.KNeighborsClassifier.html#sklearn.neighbors.KNeighborsClassifier


Sam Scott, Mohawk College, 2019."""

import numpy as np
from sklearn import datasets
from sklearn.neighbors import KNeighborsClassifier

## load the iris data set
dataset = datasets.load_wine() # see https://scikit-learn.org/stable/datasets/ for others


## pull out the important information
data = dataset.data         # each row is a single example
labels = dataset.target     # related to data array, holds the label of each row

label_names = dataset.target_names    # optional - the name of each label 
#feature_names = dataset.feature_names # optional - the name of each feature


## uncomment this code to normalize your data using the procedure shown in the handout
# min = data.min(axis=0)
# spread = data.max(axis=0) - min
# data = (data - min) / spread


## or uncomment this code below to normalize with sklearn
# from sklearn.preprocessing import normalize
# data = normalize(data, axis=0)

## ITERATE 10 TIMES
accuracy_sum = 0
num_iterations = 10

for testcase in range(0,num_iterations):
    ## split into training and testing data
    
    i = np.arange(data.shape[0])    # generate and shuffle indices
    np.random.shuffle(i)
    
    split = int(data.shape[0] * 0.75)    # the split point for 75% train, 25% test data
    
    train_data = data[i[:split]]     # the first 75% of the shuffled data and labels
    train_labels = labels[i[:split]] 
    
    test_data = data[i[split:]]     # the last 25% of the shuffled data and labels
    test_labels = labels[i[split:]] 
    
    
    ## run the kNN classifier
    k = 5  # the number of neighbors
    
    clf = KNeighborsClassifier(k)           # creates the classifier object
            # try the weights parameter for weighted voting
            # try the p parameter for Manhattan or other Minkowski distances
            
    clf.fit(train_data, train_labels)       # trains the classifier on the training set
    
    predictions = clf.predict(test_data)    # gets the predictions for the test set
    
    correct = (predictions == test_labels).sum()    # sums up the correct predictions
    
    accuracy = correct / test_data.shape[0] * 100   # works out the % accuracy
    
    print()
    print()
    print("kNN Results")
    print("===========")
    print("k =",k)
    print("correct =",correct,"/",predictions.shape[0])
    print("accuracy =",accuracy)
    print()
    
    accuracy_sum += accuracy

## Final Summary
accuracy_avg = accuracy_sum / num_iterations
print()
print()
print("Average Accuracy =",accuracy_avg)