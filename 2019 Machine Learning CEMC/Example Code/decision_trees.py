"""Sample Decision Tree learning code. 

See the comments below for explanation and for links to the sklearn documentation

Sam Scott, Mohawk College, 2018"""

import numpy as np

## Load a built-in data set
# https://sklearn.org/tutorial/basic/tutorial.html#loading-an-example-dataset
# 
# For the built in data sets, use the following attributes
# dataset.data            <- 2D array of data
# dataset.target          <- related array of classification labels
# dataset.feature_names   <- the name of each feature (column) in dataset.data
from sklearn import datasets
dataset = datasets.load_breast_cancer()

## Create a random split of 80% training, 20% testing
# https://sklearn.org/tutorial/statistical_inference/supervised_learning.html

indices = np.random.permutation(len(dataset.data))  # permutes the numbers from 0 to len-1

split = round(len(indices) * 0.8)                   # Number of training data items

train = dataset.data[indices[:split]]               # Now get the training/testing sets
train_target = dataset.target[indices[:split]]
test = dataset.data[indices[split:]]
test_target = dataset.target[indices[split:]]

## Create the Decision Tree object
# https://sklearn.org/modules/tree.html
#
# Try these optional keyword parameters: criterion, splitter, max_depth, min_samples_split, min_samples_leaf, and max_leaf_nodes
# For more nifo on what these parameters do, go to...
# https://sklearn.org/modules/generated/sklearn.tree.DecisionTreeClassifier.html

from sklearn import tree

clf = tree.DecisionTreeClassifier()

## Train the Classifier
# Use the training data for this

clf = clf.fit(train, train_target)

## Classify and measure accuracy

print("======== TRAINING DATA ============")
prediction = clf.predict(train)
marking = (prediction == train_target)          # Creates an array of True and False
correct = len(np.argwhere(marking == True))     # Number of Trues
print("Correct:",correct)
print("Incorrect:",len(prediction)-correct)
print("Accuracy:",correct/len(prediction)*100)


print("======== TESTING DATA =============")
prediction = clf.predict(test)
marking = (prediction == test_target)
correct = len(np.argwhere(marking == True))
print("Correct:",correct)
print("Incorrect:",len(prediction)-correct)
print("Accuracy:",correct/len(prediction)*100)

## Graph the Decision Tree!
# The line below creates a .dot file in "graphviz" format. 
# To quickly view the tree the file represents, open the .dot file in notepad++ and paste it into the text box at http://webgraphviz.com/

tree.export.export_graphviz(clf, out_file="tree.txt", feature_names=dataset.feature_names, class_names=dataset.target_names)

# WARNING: There is a graphviz package for python that should make the above easier, however my attempts to import it into Anaconda 3.6 all resulted in a permanently broken installation of Python, so I do not recommend it (re-installation fixed it). 

# If anyone tries and succeeds in installing the graphviz package in Anaconda and producing a graphical decision tree from python, please let me know how you did it!