#!/usr/bin/python

import matplotlib.pyplot as plt
from prep_terrain_data import makeTerrainData
from class_vis import prettyPicture
from sklearn.metrics import accuracy_score
from time import time

features_train, labels_train, features_test, labels_test = makeTerrainData()

### the training data (features_train, labels_train) have both "fast" and "slow"
### points mixed together--separate them so we can give them different colors
### in the scatterplot and identify them visually
grade_fast = [features_train[ii][0] for ii in range(0, len(features_train)) if labels_train[ii]==0]
bumpy_fast = [features_train[ii][1] for ii in range(0, len(features_train)) if labels_train[ii]==0]
grade_slow = [features_train[ii][0] for ii in range(0, len(features_train)) if labels_train[ii]==1]
bumpy_slow = [features_train[ii][1] for ii in range(0, len(features_train)) if labels_train[ii]==1]


#### initial visualization
plt.xlim(0.0, 1.0)
plt.ylim(0.0, 1.0)
plt.scatter(bumpy_fast, grade_fast, color = "b", label="fast")
plt.scatter(grade_slow, bumpy_slow, color = "r", label="slow")
plt.legend()
plt.xlabel("bumpiness")
plt.ylabel("grade")
plt.show()

def showVis(clf, features_test, labels_test):
    try:
        prettyPicture(clf, features_test, labels_test)
    except NameError:
        pass
################################################################################


### your code here!  name your classifier object clf if you want the 
### visualization code (prettyPicture) to show you the decision boundary

'''
# k nearest neighbeour
from sklearn import neighbors
clf = neighbors.KNeighborsClassifier(n_neighbors=8)
t0 = time()
clf.fit(features_train, labels_train)
print "{}{}{}\n{}".format("*"*60, "\n", str(clf.__class__)[8:-2], clf.get_params())
print "training time: {}s".format(time() - t0)

t0 = time()
pred = clf.predict(features_test)
print "prediction time: {}s".format(time() - t0)

acc = accuracy_score(pred, labels_test)
print "accuracy: {}".format(acc)


# adaboost
from sklearn.ensemble import AdaBoostClassifier

clf = AdaBoostClassifier(n_estimators=50)

t0 = time()
clf.fit(features_train, labels_train)
print "{}{}{}\n{}".format("*"*60, "\n", str(clf.__class__)[8:-2], clf.get_params())
print "training time: {}s".format(time() - t0)

t0 = time()
pred = clf.predict(features_test)
print "prediction time: {}s".format(time() - t0)

acc = accuracy_score(pred, labels_test)
print "accuracy: {}".format(acc)

'''
# random forest
from sklearn.ensemble import RandomForestClassifier

clf = RandomForestClassifier(n_estimators=5)

t0 = time()
clf.fit(features_train, labels_train)
print "{}{}{}\n{}".format("*"*60, "\n", str(clf.__class__)[8:-2], clf.get_params())
print "training time: {}s".format(time() - t0)

t0 = time()
pred = clf.predict(features_test)
print "prediction time: {}s".format(time() - t0)

acc = accuracy_score(pred, labels_test)
print "accuracy: {}".format(acc)




showVis(clf, features_test, labels_test)


'''
Results:
************************************************************
sklearn.neighbors.classification.KNeighborsClassifier
{'n_neighbors': 8, 'n_jobs': 1, 'algorithm': 'auto', 'metric': 'minkowski', 'metric_params': None, 'p': 2, 'weights': 'uniform', 'leaf_size': 30}
training time: 0.00300002098083s
prediction time: 0.00400018692017s
accuracy: 0.944
************************************************************
sklearn.ensemble.weight_boosting.AdaBoostClassifier
{'n_estimators': 50, 'base_estimator': None, 'random_state': None, 'learning_rate': 1.0, 'algorithm': 'SAMME.R'}
training time: 0.179999828339s
prediction time: 0.00800013542175s
accuracy: 0.924
************************************************************
sklearn.ensemble.forest.RandomForestClassifier
{'warm_start': False, 'oob_score': False, 'n_jobs': 1, 'min_impurity_decrease': 0.0, 'verbose': 0, 'max_leaf_nodes': None, 'bootstrap': True, 'min_samples_leaf': 1, 'n_estimators': 5, 'min_samples_split': 2, 'min_weight_fraction_leaf': 0.0, 'criterion': 'gini', 'random_state': None, 'min_impurity_split': None, 'max_features': 'auto', 'max_depth': None, 'class_weight': None}
training time: 0.0210001468658s
prediction time: 0.00300002098083s
accuracy: 0.928

'''

