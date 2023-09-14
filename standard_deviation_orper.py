# Libraries
"""Description = How to code mean and Standard deviation?


Reviewd by Fabianne on 14.09.2023"""
__author__ = "Talayeh"
__contact__ ="Talayehsadat.arabizanjani@unil.ch"
__date__ = "14.09.2023"
__status__ = "Finished"

import numpy as np

# Calculating the mean value:
def calculate_mean(vector):
    if len(vector) == 0:
        return "Vector is empty, cannot compute mean"  # Return None for an empty vector (undefined mean)
    else:
        total = sum(vector)
        mean_of_vector = total / len(vector)
        return mean_of_vector

# Example usage for calculating the mean:
vector = [1, 2, 3, 4, 5, 6]
result = calculate_mean(vector)
print("Mean:", result)


# Calculating standard deviation:
def calculate_standard_deviation(vector):
    if len(vector) == 0: 
        return "Vector is empty, cannot compute mean"  # Return None for an empty vector (undefined mean)
    else:
        standard_deviation_np = np.std(vector)
        return standard_deviation_np
    
# Example usage for standard deviation:   
vector = [1, 2, 3, 4, 5, 6]
result = calculate_standard_deviation(vector)
print("SD:", result)