""" Example of loading, preparing, normalizing, and classifying a built-in data set from sklearn. 

General Info...
https://scikit-learn.org/stable/modules/tree.html

The KNeighborsClassifier Object...
https://scikit-learn.org/stable/modules/generated/sklearn.tree.DecisionTreeClassifier.html#sklearn.tree.DecisionTreeClassifier

Sam Scott, Mohawk College, 2019."""

import numpy as np
from sklearn import datasets
from sklearn import tree
from sklearn.tree import DecisionTreeClassifier

## load the iris data set
dataset = datasets.load_iris() # see https://scikit-learn.org/stable/datasets/ for others


## pull out the important information
data = dataset.data         # each row is a single example
labels = dataset.target     # related to data array, holds the label of each row

label_names = dataset.target_names    # optional - the name of each label 
feature_names = dataset.feature_names # optional - the name of each feature

## split into training and testing data

i = np.arange(data.shape[0])    # generate and shuffle indices
np.random.shuffle(i)

split = int(data.shape[0] * 0.75)    # the split point for 75% train, 25% test data

train_data = data[i[:split]]     # the first 75% of the shuffled data and labels
train_labels = labels[i[:split]] 

test_data = data[i[split:]]     # the last 25% of the shuffled data and labels
test_labels = labels[i[split:]] 


## run the kNN classifier
clf = DecisionTreeClassifier()           # creates the classifier object
        
clf.fit(train_data, train_labels)       # trains the classifier on the training set

predictions = clf.predict(test_data)    # gets the predictions for the test set

correct = (predictions == test_labels).sum()    # sums up the correct predictions

accuracy = correct / test_data.shape[0] * 100   # works out the % accuracy

print()
print()
print("Decision Tree Results")
print("=====================")
print("correct =",correct,"/",predictions.shape[0])
print("accuracy =",accuracy)
print()
print("Note that for a better estimate of accuracy, you should run the algorithm multiple times on different random splits and average the results.")

## Graph the Decision Tree!
# The line below creates a .dot file in "graphviz" format. 
# To quickly view the tree the file represents, open the .dot file in notepad++ and paste it into the text box at http://webgraphviz.com/

tree.export.export_graphviz(clf, out_file="tree.txt", feature_names=dataset.feature_names, class_names=dataset.target_names)

# WARNING: There is a graphviz package for python that should make the above easier, however my attempts to import it into Anaconda 3.6 all resulted in a permanently broken installation of Python, so I do not recommend it (re-installation fixed it). 

# There is also supposed to be a plot_tree function that will make a graphical representation of the tree. But at the time of writing, I cannot get this to work either. If anyone tries and succeeds in installing the graphviz package in Anaconda and/or in producing a graphical decision tree from python, please let me know how you did it!