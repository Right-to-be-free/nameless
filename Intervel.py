import numpy as np
import matplotlib.pyplot as plt
import scipy.stats as stats

# Sample parameters
sample_mean = 75  # Mean of sample data
sigma = 10  # Standard deviation
n = 100  # Sample size
confidence_level = 0.95  # 95% confidence level

# Compute Z-score for 95% confidence interval
z_score = stats.norm.ppf((1 + confidence_level) / 2)

# Compute Margin of Error (MOE)
margin_of_error = z_score * (sigma / np.sqrt(n))

# Compute Confidence Interval
ci_lower = sample_mean - margin_of_error
ci_upper = sample_mean + margin_of_error

# Plot Confidence Interval
x = np.linspace(sample_mean - 4 * sigma / np.sqrt(n), sample_mean + 4 * sigma / np.sqrt(n), 100)
y = stats.norm.pdf(x, sample_mean, sigma / np.sqrt(n))

plt.figure(figsize=(8, 5))
plt.plot(x, y, color='blue', label="Sampling Distribution")
plt.axvline(ci_lower, color='red', linestyle='--', label=f"Lower Bound ({ci_lower:.2f})")
plt.axvline(ci_upper, color='red', linestyle='--', label=f"Upper Bound ({ci_upper:.2f})")
plt.axvline(sample_mean, color='green', linestyle='-', label=f"Sample Mean ({sample_mean})")
plt.fill_between(x, y, where=(x >= ci_lower) & (x <= ci_upper), color='gray', alpha=0.3)
plt.xlabel("Sample Mean Values")
plt.ylabel("Probability Density")
plt.title(f"95% Confidence Interval: ({ci_lower:.2f}, {ci_upper:.2f})")
plt.legend()
plt.grid(True)
plt.show()
