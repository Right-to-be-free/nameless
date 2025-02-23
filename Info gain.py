import numpy as np
from scipy.stats import entropy

# Calculate entropy
def calculate_entropy(data):
    value, counts = np.unique(data, return_counts=True)
    probs = counts / len(data)
    return entropy(probs, base=2)

# Information Gain function
def information_gain(data, feature, target):
    # Calculate the entropy of the original dataset
    original_entropy = calculate_entropy(data[target])

    # Get unique values of the feature
    feature_values = np.unique(data[feature])
    
    weighted_entropy_sum = 0
    for value in feature_values:
        # Subset the data for the current value of the feature
        subset = data[data[feature] == value]
        
        # Calculate the entropy for the subset
        subset_entropy = calculate_entropy(subset[target])
        
        # Calculate the weight of the subset (based on the number of samples)
        weight = len(subset) / len(data)
        
        # Add the weighted entropy of the subset
        weighted_entropy_sum += weight * subset_entropy

    # Information Gain is the difference between the original entropy and the weighted entropy
    return original_entropy - weighted_entropy_sum

# Sample dataset
import pandas as pd

data = pd.DataFrame({
    'Study Time': ['High', 'Low', 'High', 'Low', 'High'],
    'Outcome': ['Pass', 'Fail', 'Pass', 'Fail', 'Pass']
})

# Calculate Information Gain for the "Study Time" feature
info_gain = information_gain(data, 'Study Time', 'Outcome')
print(f'Information Gain for "Study Time": {info_gain}')
