import scipy.stats as stats

# Given values
X = 85  # Observed value (student's score)
mu = 70  # Mean of exam scores
sigma = 10  # Standard deviation

# Compute Z-score
Z = (X - mu) / sigma

# Compute probability from Z-table (area to the left of Z)
probability = stats.norm.cdf(Z)

# Compute probability of scoring higher than X
probability_above = 1 - probability

print(Z, probability, probability_above)
