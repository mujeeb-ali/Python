import numpy as np
from scipy.stats import trim_mean

# Example: Imagine analyzing daily website response times (ms)
response_times = [120, 123, 122, 119, 118, 500, 117, 120, 121, 600, 119]
print(np.sum(np.array(response_times) / 11))

Mean = np.mean(response_times)
Trimmed_Mean = trim_mean(response_times, 0.3)  # Trim 30% of data from each end
print("Mean:", Mean)
print("30% Trimmed Mean:", Trimmed_Mean)

# import numpy as np

# Student scores
scores = [85, 90, 72, 88]

# Weights (20% assignment, 20% quiz, 30% midterm, 30% final)
weights = [0.2, 0.2, 0.3, 0.3]

# Weighted mean
weighted_mean = np.average(scores, weights=weights)
print(weighted_mean)


