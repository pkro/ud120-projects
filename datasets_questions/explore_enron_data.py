#!/usr/bin/python

""" 
    Starter code for exploring the Enron dataset (emails + finances);
    loads up the dataset (pickled dict of dicts).

    The dataset has the form:
    enron_data["LASTNAME FIRSTNAME MIDDLEINITIAL"] = { features_dict }

    {features_dict} is a dictionary of features associated with that person.
    You should explore features_dict as part of the mini-project,
    but here's an example to get you started:

    enron_data["SKILLING JEFFREY K"]["bonus"] = 5600000
    
"""

import pickle
import pprint as pprint

enron_data = pickle.load(open("../final_project/final_project_dataset.pkl", "r"))
#pprint.pprint(enron_data)

cnt = 0
for e in enron_data:
    if enron_data[e]['poi'] == 1:
        cnt+=1

print cnt


