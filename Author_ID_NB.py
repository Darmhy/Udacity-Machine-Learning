#!/usr/bin/python

""" 
    This is the code to accompany the Lesson 1 (Naive Bayes) mini-project. 
    Use a Naive Bayes Classifier to identify emails by their authors
    
    authors and labels:
    Sara has label 0
    Chris has label 1
"""
    
import sys
from time import time
sys.path.append("../tools/")
from email_preprocess import preprocess


### features_train and features_test are the features for the training
### and testing datasets, respectively
### labels_train and labels_test are the corresponding item labels
features_train, features_test, labels_train, labels_test = preprocess()

#########################################################
### your code goes here ###

""" compute the accuracy of your Naive Bayes classifier """
### import the sklearn module for GaussianNB
from sklearn.naive_bayes import GaussianNB

### create classifier
clf = GaussianNB()

### fit the classifier on the training features and labels
t0 = time()
clf.fit(features_train, labels_train)
print "training time:", round(time()-t0, 3), "s"


### calculate and return the accuracy on the test data
### this is slightly different than the example,
### where we just print the accuracy
### you might need to import an sklearn module
t0 = time()
clf.predict(features_test)
print "predict time:", round(time()-t0, 3), "s"

#accuracy = clf.score(features_test, labels_test)
#print(accuracy)
#return accuracy
#########################################################
