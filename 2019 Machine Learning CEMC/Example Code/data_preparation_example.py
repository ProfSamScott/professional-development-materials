""" Example of loading and preparing a built-in data set from
sklearn. 

Run, then look at the variables in the shell to see what happened.

https://scikit-learn.org/stable/datasets/index.html

Sam Scott, Mohawk College, 2019."""

import numpy as np
from sklearn import datasets

## load the iris data set
dataset = datasets.load_iris() # see https://scikit-learn.org/stable/datasets/ for others

## pull out the important information
data = dataset.data         # each row is a single example
labels = dataset.target     # related to data array, holds the label of each row

label_names = dataset.target_names    # optional - the name of each label 
feature_names = dataset.feature_names # optional - the name of each feature

## split into training and testing data

i = np.arange(data.shape[0])       # generate and shuffle indices
np.random.shuffle(i)

split = int(data.shape[0] * 0.75)  # the split point for 75% train, 25% test data

train_data = data[i[:split]]       # the first 75% of the shuffled data and labels
train_labels = labels[i[:split]] 

test_data = data[i[split:]]        # the last 25% of the shuffled data and labels
test_labels = labels[i[split:]] 

