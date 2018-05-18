#!/usr/bin/python


def outlierCleaner(predictions, ages, net_worths):
    """
        Clean away the 10% of points that have the largest
        residual errors (difference between the prediction
        and the actual net worth).

        Return a list of tuples named cleaned_data where 
        each tuple is of the form (age, net_worth, error).
    """
    
    cleaned_data = []
    for age, prediction, net_worth in zip(ages, predictions, net_worths):
        error = abs(prediction[0] - net_worth[0])**2
        cleaned_data.append((age[0], net_worth[0], error))
    
    cleaned_data = sorted(cleaned_data, key=lambda x: x[2])
    
    for e in cleaned_data:
        print e[2]

    return cleaned_data[:81]

