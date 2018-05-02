#!/usr/bin/python

""" 
    This is the code to accompany the Lesson 2 (SVM) mini-project.

    Use a SVM to identify emails from the Enron corpus by their authors:    
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

from sklearn import svm
#clf = svm.SVC(kernel = 'linear')
clf = svm.SVC(kernel = 'rbf', C=10000.0)
from time import time
# test with 100th of data
#features_train = features_train[:len(features_train)/100] 
#labels_train = labels_train[:len(labels_train)/100] 

t0 = time()
clf.fit(features_train, labels_train)
print 'fitting time: {}s'.format(time()-t0)

t0 = time()
pred = clf.predict(features_test)
print 'prediction time: {}s'.format(time()-t0)

from sklearn.metrics import accuracy_score
accuracy = accuracy_score(pred, labels_test)
print accuracy
for e in [10,26,50]:
    print "item {} predicted class: {}".format(e, pred[e])

chris = sum(e for e in pred if e == 1)
print "Chris items: {}".format(chris)

'''
Linear:
    Full set:
    no. of Chris training emails: 7936
    no. of Sara training emails: 7884
    fitting time: 155.990999937s
    prediction time: 16.1320002079s
    0.9840728100113766

    100th of set:
    fitting time: 0.0940001010895s
    prediction time: 1.03399991989s
    0.8845278725824801

rbf: 
    100th of set:
    fitting time: 0.110000133514s
    prediction time: 1.14399981499s
    0.6160409556313993
    
    with C = 10.0:
    fitting time: 0.131999969482s
    prediction time: 1.17100000381s
    0.6160409556313993
    
    with C = 100.0:
    fitting time: 0.108999967575s
    prediction time: 1.15700006485s
    0.6160409556313993
    
    with C = 10000.0:
    fitting time: 0.110000133514s
    prediction time: 0.925999879837s
    0.8924914675767918        
    
    Full set with C = 10000.0:
    fitting time: 102.638000011s
    prediction time: 10.2109999657s
    0.9908987485779295
'''

#########################################################
### your code goes here ###

#########################################################


